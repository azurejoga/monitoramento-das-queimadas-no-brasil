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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55941a5f-0e47-38c8-8ed0-69c464f05908 | -9.32936 | -37.98158 | 2025-08-20 03:15:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2257c1e5-a999-30f7-b2f0-19a392bbfef7 | -3.81436 | -41.56451 | 2025-08-20 03:15:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 62dcad75-cb90-3365-9cd6-483ab81e86c2 | -6.96766 | -42.8758 | 2025-08-20 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1261e492-9d74-3110-87cd-f8a2a036861f | -9.32988 | -37.98291 | 2025-08-20 03:15:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d3d45559-7922-3b30-9b16-bc4a45c5c16d | -4.16497 | -42.03075 | 2025-08-20 03:15:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1d09fb5b-a84f-3fee-933e-990d6e55ce6b | -5.51184 | -35.57813 | 2025-08-20 03:15:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0b10d4fe-61f5-32e4-bc07-51a6e94362f2 | -5.06964 | -37.71781 | 2025-08-20 03:15:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 80638646-f0fe-3eb0-94fb-c40cddf4cacc | -6.95225 | -42.87973 | 2025-08-20 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| fca669c1-a2ee-3f27-b031-feb0f698222b | -9.32882 | -37.98448 | 2025-08-20 03:15:00 | NOAA-20 | PARICONHA | ALAGOAS | Brasil | 2706422 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 347f399f-cdd6-30fb-834a-9d73be56827f | -6.94082 | -42.87995 | 2025-08-20 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 65148356-91b8-3ed2-9838-6205e05daf7a | -6.12987 | -42.9598 | 2025-08-20 03:15:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f7ddec54-923d-3be8-be74-76adab8d520b | -3.81323 | -41.57094 | 2025-08-20 03:15:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a880325-2941-33c0-a30f-a96c20013439 | -4.72285 | -38.39896 | 2025-08-20 03:15:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9c6cf137-8d86-3fba-8a17-88f2e0354df8 | -6.95356 | -42.87292 | 2025-08-20 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.2 |
| dbd97543-66a8-30ff-9363-a394445c2a75 | -9.5255 | -42.94205 | 2025-08-20 03:17:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dc91a606-56e5-318c-b0e1-0a8a14871958 | -9.52674 | -42.93577 | 2025-08-20 03:17:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 584c9369-f6dc-381b-918b-b37b4f78d6f8 | -9.66832 | -40.58677 | 2025-08-20 03:17:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d154a626-156d-3464-a194-7635dbb43e53 | -10.81998 | -43.28465 | 2025-08-20 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 125c5134-91d4-3817-8e01-474a2ef68fcc | -15.54525 | -42.28009 | 2025-08-20 03:19:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9e765213-bb27-30ff-8031-a649ad9e5914 | -15.54239 | -42.27935 | 2025-08-20 03:19:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 18b751ee-1a82-3b8e-af27-14798b7537d6 | -20.21567 | -44.13359 | 2025-08-20 03:19:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 197cc359-9e7d-354b-8704-66f3bf422809 | -21.50438 | -45.46379 | 2025-08-20 03:19:00 | NOAA-20 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4956d4c7-5b41-36d6-a0a5-0404f6c1cd5b | -20.0115 | -42.22829 | 2025-08-20 03:19:00 | NOAA-20 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| bb300e5a-2abc-34b1-9bbd-da2d98092689 | -20.20583 | -41.61111 | 2025-08-20 03:19:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 832c3f52-1c63-35b8-9e13-537d64cdb798 | -16.52235 | -42.51901 | 2025-08-20 03:19:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4257f24-27cc-375e-9789-0402806685dc | -20.21447 | -44.13507 | 2025-08-20 03:19:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7345654a-6162-370b-af18-cf96000aa328 | -15.54235 | -42.29415 | 2025-08-20 03:19:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6d24602e-1f1d-3113-8d1a-658dc2740d70 | -19.81837 | -41.97441 | 2025-08-20 03:19:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6fb72e6d-539b-3d70-a551-410f1e105387 | -20.46714 | -45.08042 | 2025-08-20 03:19:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ab01e6cc-03b5-3882-8283-0ddd3d21dac6 | -15.54334 | -42.28935 | 2025-08-20 03:19:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f520d18f-e346-3285-857c-4509f262b9e2 | -15.54431 | -42.28464 | 2025-08-20 03:19:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0a7bc849-bfc0-3e03-99ce-8fcb2a019126 | -15.54634 | -42.28977 | 2025-08-20 03:19:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f21d4d2-8d11-3f4b-af5a-a56cbc0b4b7f | -20.21557 | -44.13023 | 2025-08-20 03:19:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 34b4483c-5ce7-378c-9768-44099124f43f | -15.54041 | -42.28859 | 2025-08-20 03:19:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4abe2ea4-fba0-3a96-8692-8dcb579b3842 | -15.54532 | -42.29457 | 2025-08-20 03:19:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed495ebe-d132-3454-9778-8d78aa436a48 | -15.54733 | -42.28514 | 2025-08-20 03:19:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1aff55a8-dcc6-369b-87ea-74c01f445d60 | -17.55333 | -44.48302 | 2025-08-20 03:19:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 04d3ef80-e6eb-3933-aa3f-0143737e06e0 | -16.52334 | -42.51437 | 2025-08-20 03:19:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81e6076f-7810-377f-a643-44ded7dd1992 | -20.00611 | -42.22697 | 2025-08-20 03:19:00 | NOAA-20 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 32c077e6-d2cc-3186-a7c7-0e2c49dc0ba1 | -20.14628 | -40.87961 | 2025-08-20 03:19:00 | NOAA-20 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6472b484-6544-3a4a-89ce-70c7b0c3c824 | -22.71189 | -42.13738 | 2025-08-20 03:19:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d1beb9e8-c4df-30ff-8ae8-852822e92a0f | -21.39465 | -43.80738 | 2025-08-20 03:19:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f56b3149-b745-3b72-9843-9ee6b5ca04e7 | -15.54141 | -42.28393 | 2025-08-20 03:19:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 25510c4c-8454-3441-a7a9-748d5e13bae1 | -17.55218 | -44.48579 | 2025-08-20 03:19:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56aab9e9-db0e-37b4-8cfc-e6a9b392c101 | -21.29614 | -41.51218 | 2025-08-20 03:19:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1c6f9902-2c34-3570-965a-a22e1acbad77 | -21.39506 | -43.80828 | 2025-08-20 03:19:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 45e13307-ebfa-39f8-8643-4dc2e41da7c2 | -20.94948 | -46.10568 | 2025-08-20 03:19:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b299dae6-2894-393c-82ba-acd385b12f70 | -17.55364 | -44.47945 | 2025-08-20 03:19:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb5647c6-2882-3bf8-a9f4-4f7423ab54f5 | -22.71118 | -42.14064 | 2025-08-20 03:19:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d8e65458-6128-3889-9f30-02d8e9d6b486 | -17.55851 | -44.48788 | 2025-08-20 03:19:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c98be1ec-8caf-347c-a85f-ce61ec28cd38 | -15.0002 | -54.8135 | 2025-08-20 03:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| d2195152-53db-3311-a251-5d9804682dc3 | -13.3349 | -54.4027 | 2025-08-20 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 0bb07914-a597-30dc-ab37-3adef0af0f4b | -13.3346 | -54.4233 | 2025-08-20 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 8827f8d5-84fa-346b-961a-664ea7efd67c | -6.9605 | -42.8816 | 2025-08-20 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| 8777093b-97f6-31b2-a329-f42c92a13e2b | -13.1555 | -54.9357 | 2025-08-20 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 6e9b1848-6c15-3f7a-bb34-92e91fa71bc5 | -13.1364 | -54.9376 | 2025-08-20 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 38.9 |
| c412ed3c-27b1-39d7-bb39-7db6851fa3df | -20.339 | -51.7062 | 2025-08-20 03:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b77e2c22-0d5d-3464-9b98-7b270e433249 | -8.034 | -47.6639 | 2025-08-20 03:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 71ac10eb-3377-3f27-8b9c-4d1241d2f559 | -13.1558 | -54.9151 | 2025-08-20 03:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9780b488-d2f7-30bd-83c4-b584c6b224a1 | -13.1364 | -54.9376 | 2025-08-20 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 583f5e05-d57d-3f4b-be23-7dc3125825ce | -8.034 | -47.6639 | 2025-08-20 03:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 46762742-9455-3577-bd9b-1d048ce10c8e | -20.339 | -51.7062 | 2025-08-20 03:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 94.3 |
| c36830d7-85cf-3e2f-8781-001fed406a11 | -9.1895 | -59.6364 | 2025-08-20 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0d8597a8-a935-36d2-83cc-5495abf84a38 | -13.1367 | -54.9171 | 2025-08-20 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| f8c6f7b9-1b64-3422-a974-886ad78f973e | -13.1558 | -54.9151 | 2025-08-20 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| fdb886f0-2db2-36e7-a011-03f06835311f | -13.1555 | -54.9357 | 2025-08-20 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 20b656ad-690c-351e-b9f6-68ec49b24e24 | -13.3349 | -54.4027 | 2025-08-20 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| cb5fa5ae-acaf-333e-947a-6a1cb6a9c5da | -8.0152 | -47.6656 | 2025-08-20 03:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 2c44d19b-000a-36d6-8f3b-f3c76a48bb13 | -9.1895 | -59.6364 | 2025-08-20 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 7dc25ca1-0ac9-348c-95fd-25896096b1e1 | -20.339 | -51.7062 | 2025-08-20 03:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 00064a02-cec3-35e8-8c78-380959edc388 | -13.1367 | -54.9171 | 2025-08-20 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| dda62838-0826-3276-b0a2-e04a3a885840 | -13.0202 | -46.7765 | 2025-08-20 03:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| b02a0969-6d00-3746-8ef8-05db3a5d3201 | -13.0395 | -46.7736 | 2025-08-20 03:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 923faa67-2977-37ee-aa4e-d6577429f802 | -8.034 | -47.6639 | 2025-08-20 03:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 84c3e826-4b92-31ee-b723-fc80f1791cf7 | -13.1555 | -54.9357 | 2025-08-20 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 824533b1-dd97-33cd-b056-237c8f8072c0 | -13.0391 | -46.7963 | 2025-08-20 03:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9cd6fbb1-16fc-3dbf-bc2e-82cccfc79fb5 | -13.1364 | -54.9376 | 2025-08-20 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 128c4360-eac4-3feb-8f7f-e3ba62f9b2c0 | -13.1558 | -54.9151 | 2025-08-20 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 1a85315c-29dc-3bb2-9a4a-498332881db7 | -20.339 | -51.7062 | 2025-08-20 03:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 0680715b-a945-3a04-9a38-e04446c51e49 | -8.034 | -47.6639 | 2025-08-20 03:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 01896627-1a52-31e3-b65a-9cef71eb5df7 | -9.1895 | -59.6364 | 2025-08-20 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0e938901-0aba-3b43-a57c-a2fe8c6499fb | -13.1555 | -54.9357 | 2025-08-20 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 907c842c-4845-3a18-a1a4-11d924f4de8c | -13.1364 | -54.9376 | 2025-08-20 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 51f377cf-994f-3f2c-a3ec-c83c023681ae | -13.1558 | -54.9151 | 2025-08-20 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4bde564e-6b6e-3ae1-9fd8-1f8a12358f59 | -2.38371 | -47.65771 | 2025-08-20 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e29cea8-ab47-3e4e-8422-0c4f493e16ad | -2.38752 | -47.66307 | 2025-08-20 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1835949-0077-3ce2-97cc-1b4ab5f05681 | -2.54568 | -47.7015 | 2025-08-20 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9d23fdc-9f97-3d1c-b8a0-7772e6f95a09 | -2.97434 | -41.75834 | 2025-08-20 04:06:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 73e2a4b1-dc28-31e6-8e94-5586b0e57e6e | -2.44666 | -47.32808 | 2025-08-20 04:06:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 156a586f-4ec7-3ece-bd46-552aeda747f6 | -2.38296 | -47.66229 | 2025-08-20 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01504f15-a760-30b7-b7e7-1e380fc2cba5 | -2.44738 | -47.3237 | 2025-08-20 04:06:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c24b1ff7-ed9f-3c73-bf44-a31280e9480c | -2.3822 | -47.66694 | 2025-08-20 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 085e2daf-0edc-3112-8dce-9d60881472da | -4.11574 | -38.23641 | 2025-08-20 04:06:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e5dc95cf-cd5c-31e7-93a6-63d80f96f676 | -6.52583 | -45.46861 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f604bbd7-1924-346d-b340-f699b4cded5e | -5.87914 | -48.11615 | 2025-08-20 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d73e5b17-5b58-3d80-905e-34cccdefb338 | -5.39787 | -43.29879 | 2025-08-20 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abd6c437-8c9d-305e-91f0-dda6857cdafa | -7.64946 | -45.28151 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5786fa3-8bd5-386f-a520-99cc4b9fac01 | -3.81953 | -41.55421 | 2025-08-20 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5fc1bc9d-a255-3a23-a4de-76891babdfdb | -7.58062 | -45.4255 | 2025-08-20 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f2df04b-9680-3456-90ca-e6b31edac793 | -5.6499 | -43.37203 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README10.md)
