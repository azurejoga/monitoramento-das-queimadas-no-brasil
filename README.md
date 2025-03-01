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
| 80c0c8a9-2e6a-3e6a-906d-43417d9e59a8 | 2.1767 | -61.8534 | 2025-03-01 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0981cb4b-3ab6-333a-9071-473a8dc8f717 | 2.1949 | -61.8532 | 2025-03-01 00:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 94d07fa8-0b51-344c-a962-74a491340983 | -9.259 | -60.309 | 2025-03-01 00:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 080aab7f-cba3-359b-840c-1e33ec757337 | 0.9569 | -60.5233 | 2025-03-01 00:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 034760e3-518e-3b08-b96f-030c998f34df | 2.1767 | -61.8534 | 2025-03-01 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 70.1 |
| aa13b28a-3a53-3d7e-86c0-509b7b3b8434 | 2.1949 | -61.8532 | 2025-03-01 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| cf0bc6fa-b9cb-30f7-9780-8f3b68e18dac | 2.1767 | -61.8534 | 2025-03-01 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 5926037f-b26c-3386-845a-3d4b18ec27ce | -12.012 | -45.818298 | 2025-03-01 00:22:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c675be4c-3e59-37cd-87ef-55590900426a | -21.0651 | -43.287701 | 2025-03-01 00:22:00 | METOP-B | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e65b73d-1e40-3d79-89e9-51dbd176d6a6 | -12.0136 | -45.8256 | 2025-03-01 00:22:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bd74305c-30a1-39b6-b238-26402b2365f5 | 0.9764 | -60.495899 | 2025-03-01 00:22:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 13cc8445-f213-3263-97d4-fafa4d848067 | -21.0669 | -43.295502 | 2025-03-01 00:22:00 | METOP-B | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 22efea14-a97c-3ed8-ada5-3c5fb094b183 | 0.986 | -60.4981 | 2025-03-01 00:22:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 20488ce8-ee2c-3d5e-9c34-61ddb5e3cad5 | -22.686701 | -47.415501 | 2025-03-01 00:22:00 | METOP-B | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 76681afc-ff97-3052-95d9-537bb0d6e614 | -10.5344 | -44.647202 | 2025-03-01 00:22:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d5256198-1159-35db-90ed-7d9f80e09d2d | 0.9915 | -60.4743 | 2025-03-01 00:22:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a6314ff6-9f6d-39be-af81-1b7585d72972 | -10.5363 | -44.655399 | 2025-03-01 00:22:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8c249350-dcb8-3e94-8701-de9b0b5b8ccd | 2.2038 | -61.8116 | 2025-03-01 00:22:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 415d7556-0f83-3260-9a8c-9b5164619177 | 2.2105 | -61.783501 | 2025-03-01 00:22:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2d552fd5-14d4-344f-a1dd-249d712ce6de | -22.66 | -42.175598 | 2025-03-01 00:22:00 | METOP-B | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 81625bfc-997e-3737-9725-a4ee90c718b4 | -2.7111 | -54.604301 | 2025-03-01 00:22:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31c02ff5-798d-3dcb-aa35-345e4e6db82e | -2.7087 | -54.593601 | 2025-03-01 00:22:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9350cb6-cb56-3ab2-9601-d80d61314a2b | -21.660101 | -44.189499 | 2025-03-01 00:22:00 | METOP-B | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 94184b62-f0b1-317c-b271-0ee4c050eff6 | 0.9819 | -60.472099 | 2025-03-01 00:22:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f009d62a-d689-33f0-b505-4f5d13c4d1bd | -12.0103 | -45.811001 | 2025-03-01 00:22:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 476a1752-3f8c-3f79-975c-9f22ca4290b7 | -22.6884 | -47.423901 | 2025-03-01 00:22:00 | METOP-B | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 525e0fe2-d550-30f5-ad81-46ff2f55faa5 | -21.6143 | -48.452202 | 2025-03-01 00:22:00 | METOP-B | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7bab7b57-b063-32d0-abe9-0377f72b492f | -21.063299 | -43.2799 | 2025-03-01 00:22:00 | METOP-B | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 66ae0fbe-e2c3-39ed-8cb5-da9d02be7665 | -9.8161 | -36.2263 | 2025-03-01 00:30:00 | GOES-16 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 56.8 |
| 13c0472b-776e-331f-8cf3-46b258b555ed | 2.1767 | -61.8534 | 2025-03-01 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 17657dbb-d580-3bed-961f-30b229ec0f7a | -9.8166 | -36.1992 | 2025-03-01 00:30:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| 53a6edda-35a2-3501-b19e-740c1641849d | -9.259 | -60.309 | 2025-03-01 00:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 9656fb95-7fd7-3336-9633-8cc9c65bb8c4 | 2.1767 | -61.8534 | 2025-03-01 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| ad440d0d-daed-3dc5-9bcc-5b80d8725377 | 2.1767 | -61.8534 | 2025-03-01 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8b158ecb-df5a-34d9-bb99-0b0e0511b3e8 | 0.9569 | -60.5233 | 2025-03-01 01:00:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b8fbf1a3-44c1-3db5-84db-b9f20374cf9a | 2.1949 | -61.8532 | 2025-03-01 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| f68fe0ac-435f-351a-9fb8-94d49dd977bd | -20.25413 | -50.79104 | 2025-03-01 01:09:00 | TERRA_M-M | SANTANA DA PONTE PENSA | SÃO PAULO | Brasil | 3547205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 8fc7db27-ad50-39b8-96e9-7d04c6c68034 | -20.8786 | -54.7911 | 2025-03-01 01:09:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ea227509-fefb-3a17-9a01-f92fe801928c | -23.77988 | -55.15253 | 2025-03-01 01:09:00 | TERRA_M-M | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| d16e41f5-531f-37ee-8d81-db9a48fc64a1 | -22.68818 | -47.42954 | 2025-03-01 01:09:00 | TERRA_M-M | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8b80a780-4cac-3e81-a9c8-a98b0b5cfe94 | -20.87724 | -54.77996 | 2025-03-01 01:09:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 76292cb6-0837-38f4-8763-600d2b5f49c4 | 0.9569 | -60.5233 | 2025-03-01 01:10:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 08793822-bf70-3ff9-a879-427adfb6c396 | -17.33596 | -53.73885 | 2025-03-01 01:11:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 16b7454a-b0ff-3b04-b19f-60793a12e671 | -17.32549 | -53.73724 | 2025-03-01 01:11:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d685afcb-ef5b-3ee6-8124-4b087a7aae43 | -9.26423 | -60.31826 | 2025-03-01 01:13:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ed448cf0-22bb-35c2-acc5-e32bebd1e27c | -9.2622 | -60.302898 | 2025-03-01 01:15:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba0cc073-e9a4-38ad-a7ec-3e56cbb29d87 | 1.3369 | -60.701099 | 2025-03-01 01:15:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 65908ac2-ecac-358a-bc06-ac60afb911d0 | 2.0301 | -61.408001 | 2025-03-01 01:15:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c921989d-318a-3ff7-ab88-624373de5595 | 2.1845 | -61.856098 | 2025-03-01 01:15:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f9ecc29b-bb51-3f6a-8529-42e445fe60e0 | 0.9742 | -60.529099 | 2025-03-01 01:15:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8b525a47-8620-3a7c-810e-063e051e19b4 | -9.2641 | -60.311798 | 2025-03-01 01:15:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e3820db-4284-3189-a4bb-7d3a63313eeb | -17.336599 | -53.736599 | 2025-03-01 01:15:00 | METOP-C | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d70c62f3-01e2-3af9-91fc-c659eb470164 | 2.8269 | -60.815498 | 2025-03-01 01:15:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 60830bbb-c4af-3a74-bc62-ff39ea0c62b3 | -20.883801 | -54.777599 | 2025-03-01 01:15:00 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7d8b8396-05cb-3c47-a4b3-6b8ef3626326 | 2.1881 | -61.840401 | 2025-03-01 01:15:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c6fc304a-1538-37ad-b25f-3ae32e57f112 | -17.334999 | -53.729401 | 2025-03-01 01:15:00 | METOP-C | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b7c6f05a-ee1b-3090-8b44-fe661759f67c | 2.4427 | -60.647099 | 2025-03-01 01:15:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ca6ff49e-fd89-368c-8ffb-5d9d137671b7 | 0.9644 | -60.526901 | 2025-03-01 01:15:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 406d919f-7f4a-3e54-9a8f-d9589874cf2f | 1.307 | -60.067699 | 2025-03-01 01:15:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e165dc0f-f9e5-3cd6-b80a-da875d6ac55d | 1.6933 | -60.227402 | 2025-03-01 01:15:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3e8613b6-2c11-3eee-8421-7a551ee32b01 | 2.441 | -60.654202 | 2025-03-01 01:15:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8dadc51b-3641-3d4c-a3ab-74ea29efd060 | 0.9546 | -60.5247 | 2025-03-01 01:15:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 583c3e72-57c6-370b-adad-a5b81ddcc997 | 3.9156 | -59.9842 | 2025-03-01 01:15:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d4a5bb5c-059d-3531-b654-6277e6249428 | -20.875601 | -54.787399 | 2025-03-01 01:15:00 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1122819d-2287-31f6-ada5-31797264591b | -20.885401 | -54.785099 | 2025-03-01 01:15:00 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5806afd1-f4eb-337c-aae5-20899c954517 | 2.1863 | -61.848301 | 2025-03-01 01:15:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0f7602e8-5786-398d-93bb-726a0afe72f3 | 0.9758 | -60.5219 | 2025-03-01 01:15:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d680a65c-0bd7-39e3-8167-b7f30b13dbf6 | 0.966 | -60.519699 | 2025-03-01 01:15:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 97e38681-c112-3b82-974d-9181a04fc6ff | 3.9141 | -59.991001 | 2025-03-01 01:15:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3dd24c26-3cce-3706-8b5e-fe2a987bd8f4 | 2.8285 | -60.808399 | 2025-03-01 01:15:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 471a1a83-6adf-39a7-b21b-88232a4ad20b | 0.9627 | -60.5341 | 2025-03-01 01:15:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7515fe4f-873e-3554-8504-1597c5f169c2 | 1.3086 | -60.060699 | 2025-03-01 01:15:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a2f084f1-8337-3a45-a578-b55f9dff54af | -2.71593 | -54.61036 | 2025-03-01 01:15:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac07d03c-041b-3214-8472-8892a5857460 | -2.71725 | -54.61967 | 2025-03-01 01:15:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 735bf294-37df-3924-a68f-d375a0d67c72 | 2.44176 | -60.66257 | 2025-03-01 01:17:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e7d8ce0f-f6c0-3226-a7b4-0c6a1015cb2e | 2.18868 | -61.84137 | 2025-03-01 01:17:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4edcdf8f-3d19-3a8c-a8c5-30d7cf070ba8 | 4.33894 | -60.3621 | 2025-03-01 01:17:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9fe9b969-d924-3634-83a4-e9e7634ed690 | 1.34066 | -60.70563 | 2025-03-01 01:17:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9c653e01-b7ce-36d3-abd4-01ba39d57e9c | 3.91213 | -59.99115 | 2025-03-01 01:17:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2a1279e6-2eb5-3fc1-9b2c-7f11755e2e08 | 0.95782 | -60.53296 | 2025-03-01 01:17:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 611ca391-1173-3dcb-af3c-f3b638b5740b | 0.96814 | -60.53448 | 2025-03-01 01:17:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 37.9 |
| d22ac458-4583-33dc-afb8-c988aaa71383 | 0.97665 | -60.52897 | 2025-03-01 01:17:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ce211ace-4c57-3aaa-a735-3dbc7dca581e | 2.18656 | -61.85592 | 2025-03-01 01:17:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 3c52b069-c503-3a0d-9035-371c50f3879f | -1.66311 | -55.58027 | 2025-03-01 01:17:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5e447215-c2bf-3f5a-9a41-f709159365d4 | -1.53681 | -54.54964 | 2025-03-01 01:17:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ecd20fb6-8567-362d-a1af-be0f25031651 | -1.66436 | -55.58916 | 2025-03-01 01:17:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 797dcfa3-118c-372c-a33c-4a2873582dbf | 1.07088 | -59.23341 | 2025-03-01 01:17:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1dc2f889-0cb6-3a87-8a63-ace2a1f53269 | 1.30815 | -60.0718 | 2025-03-01 01:17:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 2b0b7d96-32be-359c-9f38-bedd426a320b | 2.0306 | -61.41133 | 2025-03-01 01:17:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0c5f04ca-65be-32e3-b275-793f0889e517 | 0.95952 | -60.52069 | 2025-03-01 01:17:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c1a8378e-09aa-3519-98d8-36a115d5b15e | 0.96983 | -60.52219 | 2025-03-01 01:17:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 91bf867c-c465-34f9-8019-366b51a857e5 | 0.9569 | -60.5233 | 2025-03-01 01:20:00 | GOES-16 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| b76e6ee0-67d0-3a8c-b5d5-39c3eff54c39 | -9.259 | -60.309 | 2025-03-01 02:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 95a507c1-5a93-317b-83c1-a5afc637b0cd | -10.82376 | -37.16721 | 2025-03-01 03:17:00 | NPP-375D | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c0843fe2-ed65-3929-81d9-a975270f4695 | -9.80238 | -37.9477 | 2025-03-01 03:17:00 | NPP-375D | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b4dcae6e-0b46-3045-9716-ed0c6c8d8290 | -22.5619 | -43.6282 | 2025-03-01 03:21:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 958891db-9108-3bbd-b30d-ab534d4f465f | -21.3341 | -41.07497 | 2025-03-01 03:21:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f5a4c5d6-a287-3476-b28a-095626788a78 | -22.56318 | -43.63022 | 2025-03-01 03:21:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5e3c0eba-afe4-38e9-a325-7e51f09c6c2e | -22.24848 | -45.92751 | 2025-03-01 03:21:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1ab2c072-03b8-3434-a8b0-e7aae4ef88c8 | -22.24209 | -45.92573 | 2025-03-01 03:21:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
