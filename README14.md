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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ae3cd0e-3bf5-33a9-ac03-63d3286e3da0 | -7.9705 | -54.7658 | 2024-10-06 00:49:06 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1b403ea-9341-35b1-a70b-9172dc5fdbd5 | -7.8789 | -54.863899 | 2024-10-06 00:49:08 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05073d59-a7cf-38b0-9f71-68901622d8f4 | -7.8691 | -54.866001 | 2024-10-06 00:49:08 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a885c44f-a316-39cf-babc-970258841c07 | -7.8709 | -54.874298 | 2024-10-06 00:49:08 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf827b0-7730-36e4-8b4e-ec22984af588 | -7.8728 | -54.882702 | 2024-10-06 00:49:08 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e46f217-77d7-3df8-86de-8a4fd0fd3da7 | -5.5641 | -44.8461 | 2024-10-06 00:49:09 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc7bfc58-04fa-37de-bbfc-02673f2f7051 | -5.5677 | -44.861099 | 2024-10-06 00:49:09 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e954ab7-631e-3204-be76-ce6131ece660 | -5.5712 | -44.8759 | 2024-10-06 00:49:09 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28fba06e-51c2-3c74-8ba9-5ccb622227aa | -5.5544 | -44.848499 | 2024-10-06 00:49:09 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c2efc2f-a81d-3a2f-85e2-e9229af2ebaa | -5.5615 | -44.8783 | 2024-10-06 00:49:09 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| edc1b336-8620-39b5-8f28-c310a57c8199 | -9.1605 | -61.521301 | 2024-10-06 00:49:10 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a534cc70-025c-3994-86fb-91a1a0ece05e | -7.613 | -55.151299 | 2024-10-06 00:49:14 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f040473-891e-3e56-afc0-0cc78b576d81 | -8.2184 | -61.146702 | 2024-10-06 00:49:24 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc63d176-9a13-35ee-8919-78a9b298cc74 | -8.2087 | -61.148602 | 2024-10-06 00:49:24 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 776f5c7b-4dcd-3748-8d26-0f84f8414c7e | -3.7743 | -41.551102 | 2024-10-06 00:49:25 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e26dee2b-814d-3ca7-8449-3d6ef2fb447e | -3.7809 | -41.577999 | 2024-10-06 00:49:25 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ff52cc61-21a1-3a93-8075-b3ca1a335607 | -3.7874 | -41.604801 | 2024-10-06 00:49:25 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e10f4f30-a962-3fc6-b4ce-8699e5e64788 | -3.7647 | -41.553398 | 2024-10-06 00:49:25 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c62535a4-e114-384f-88d5-43625ad0d0f3 | -3.7713 | -41.580299 | 2024-10-06 00:49:25 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 81c66d12-a4f1-3488-9259-000905611d5d | -3.6976 | -41.6548 | 2024-10-06 00:49:26 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 61f01577-be28-3791-9231-de08fccc3d7a | -3.688 | -41.6572 | 2024-10-06 00:49:27 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 768adbed-64e7-3f09-9e05-2dc3f2c5df04 | -3.6945 | -41.683701 | 2024-10-06 00:49:27 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b06b972a-8b7b-3fa5-8998-8fade06eac49 | -4.0262 | -43.226299 | 2024-10-06 00:49:27 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ff044a4-3555-3067-8198-6baf0e7a7048 | -3.9923 | -43.2127 | 2024-10-06 00:49:28 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f1914cb9-7e5e-33ce-ae72-1cec0371b034 | -3.9972 | -43.2332 | 2024-10-06 00:49:28 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a0db805-5701-36bb-bce0-e33d50192c45 | -3.9875 | -43.2355 | 2024-10-06 00:49:28 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58ed5aa4-eee0-3d09-8699-70d697674735 | -4.1188 | -43.7826 | 2024-10-06 00:49:28 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2e366fc-ce89-3ad3-bc8f-233fbb780984 | -4.1233 | -43.801201 | 2024-10-06 00:49:28 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e591afcf-c9e2-393e-90d5-fb57fdfe47b1 | -3.9779 | -43.2379 | 2024-10-06 00:49:28 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1401b62c-de3f-3ae7-8930-ab724c3efb1a | -4.1092 | -43.784901 | 2024-10-06 00:49:28 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0551ab27-8e3d-3e13-8588-92d2c049a002 | -4.1136 | -43.803501 | 2024-10-06 00:49:28 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c88fbf5-bc87-3407-8381-e118a0043581 | -4.8121 | -46.791199 | 2024-10-06 00:49:28 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8b408c6-5b31-3b9b-b850-82b169d91a4d | -4.565 | -46.0471 | 2024-10-06 00:49:29 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb1945ca-db9a-3924-a54d-8002bda44716 | -4.568 | -46.059898 | 2024-10-06 00:49:29 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e56fb210-449b-3327-81a2-7033f6ecee11 | -7.1501 | -59.260101 | 2024-10-06 00:49:35 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4783eb38-32e0-3035-808d-a436a078d278 | -7.1533 | -59.275398 | 2024-10-06 00:49:35 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8f746b8-bb28-3fa8-b818-c97505dcc4fc | -7.1403 | -59.2621 | 2024-10-06 00:49:36 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0db3b72-98bd-36c9-9bd3-7a925c35ace6 | -4.4515 | -47.4491 | 2024-10-06 00:49:37 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 492053e4-bacd-3895-9180-403b7d3885b2 | -4.4539 | -47.459499 | 2024-10-06 00:49:37 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d89d49de-ac62-3cbd-aa66-0dba807dd8a6 | -4.4418 | -47.451302 | 2024-10-06 00:49:37 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f5e16832-a702-3842-8d96-2cfca8ad50dd | -4.4442 | -47.4617 | 2024-10-06 00:49:37 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7514ccfb-1a68-3508-9a4e-aa6261491a59 | -6.9571 | -59.0196 | 2024-10-06 00:49:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| be088a62-6b0a-3611-9e5b-493653ac71ef | -6.9602 | -59.034199 | 2024-10-06 00:49:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d09ad93-6646-3495-afb4-4a2992d9a8ed | -6.9632 | -59.048901 | 2024-10-06 00:49:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5667553c-ed58-3f08-ab63-aa46980f0f31 | -7.0297 | -59.365299 | 2024-10-06 00:49:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0dbced86-0734-3588-9dbf-e1959fc27964 | -6.9473 | -59.021599 | 2024-10-06 00:49:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef9a1e61-f456-38df-91dc-d75550fabc36 | -6.9504 | -59.036201 | 2024-10-06 00:49:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9bbf0807-d639-3b1d-970e-412a229d258f | -6.9535 | -59.0509 | 2024-10-06 00:49:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 785d9c6c-1360-3e8c-bea3-bb8b3b656c3d | -7.02 | -59.367298 | 2024-10-06 00:49:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92c7c9c5-f044-320c-9de9-29d228f50d53 | -6.994 | -59.340401 | 2024-10-06 00:49:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68f90d3b-64c4-3ad4-a5e1-0d5e69e7e919 | -6.9973 | -59.355801 | 2024-10-06 00:49:38 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4dac54d2-5384-3345-b055-9f084d1ce8c1 | -4.3017 | -47.689701 | 2024-10-06 00:49:40 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ef78dd1-7f8e-3ee8-ac89-d50a126bff3c | -4.3041 | -47.699902 | 2024-10-06 00:49:40 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc281ac-c6ea-3025-a8cc-7a93f63b4133 | -6.7797 | -60.062401 | 2024-10-06 00:49:44 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3e1de34-ce0c-3806-8cd9-c51f2215c5d2 | -4.0808 | -48.245899 | 2024-10-06 00:49:46 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a4790e2-1743-333f-b040-a9a58a75fa69 | -4.083 | -48.255402 | 2024-10-06 00:49:46 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a24a2be-53d6-31c5-b0f1-ab2cd71c4de3 | -4.0852 | -48.264801 | 2024-10-06 00:49:46 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18b81363-b92e-3724-93fb-3201719ce84a | -4.1802 | -48.854198 | 2024-10-06 00:49:46 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6cbc568-770e-32ab-9411-78f2f0676777 | -4.1822 | -48.8629 | 2024-10-06 00:49:46 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e25a5711-341d-3ac3-8925-64b53a109d24 | -3.894 | -48.328499 | 2024-10-06 00:49:49 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9d480e6-53ec-30e2-8f82-0dc83a723c7a | -3.8962 | -48.337898 | 2024-10-06 00:49:49 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fd8d8d5-ceec-3104-8928-ac1d8ba7f42f | -3.8983 | -48.347301 | 2024-10-06 00:49:49 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd1ca0fc-a12f-3b61-8e22-b62b738c5581 | -3.8864 | -48.340199 | 2024-10-06 00:49:49 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 580e2ba1-97bf-3d4b-8bbb-54284314ff42 | -4.3689 | -50.801399 | 2024-10-06 00:49:50 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e939e295-f472-395d-a3fb-ba6a199d4d33 | -4.3705 | -50.808601 | 2024-10-06 00:49:50 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b04e6ef8-7c5b-3c4e-bcbb-ac3e1552e5c4 | -3.6089 | -47.498901 | 2024-10-06 00:49:50 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 250bc321-7852-3d68-b44f-6e2003a96f5c | -3.6114 | -47.509602 | 2024-10-06 00:49:50 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16606019-f8ec-3295-b95a-b0ff0e95e599 | -3.5992 | -47.501202 | 2024-10-06 00:49:51 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b238f52-ae1d-3eee-b6cd-73de61e1e043 | -3.6017 | -47.511799 | 2024-10-06 00:49:51 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5edaaf27-19ed-3e90-9274-842a3107de59 | -3.4479 | -47.647202 | 2024-10-06 00:49:54 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7851f251-fbe8-3ae9-9fd1-31f40aeb8e19 | -3.4503 | -47.6577 | 2024-10-06 00:49:54 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cea95e3-8784-3c8a-bf31-e3f9181ee01b | -3.7822 | -49.452702 | 2024-10-06 00:49:55 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf721c5-dcc3-33e5-b042-c38b30dcb2f2 | -3.7841 | -49.460899 | 2024-10-06 00:49:55 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d543b65-ce15-3d1b-bd1a-d51cf7056e68 | -3.4884 | -48.891602 | 2024-10-06 00:49:58 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d57648d9-ebda-3179-a6d4-7e8046b4a5cd | -3.4905 | -48.900398 | 2024-10-06 00:49:58 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef9f32a8-b4f9-3910-a94b-ca15012c862f | -3.4925 | -48.909302 | 2024-10-06 00:49:58 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38390a11-ca80-3796-9c14-1fddd16b0738 | -17.81678 | -53.81309 | 2024-10-06 00:50:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| c5784ebc-4564-318e-b9e9-9724935f8771 | -17.81662 | -53.78664 | 2024-10-06 00:50:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 797.7 |
| 9a0ca878-303c-3d4e-a843-42439d1818f6 | -17.81365 | -53.77977 | 2024-10-06 00:50:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 784.4 |
| 1b9b2818-65d3-3446-9a4f-859dd598a839 | -17.81354 | -53.75626 | 2024-10-06 00:50:00 | TERRA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 29baeed3-5ec2-3058-8e67-defc9be742d2 | -17.01261 | -55.05528 | 2024-10-06 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| ac91f1f2-335f-3cbb-94d4-8e1bf2fb7899 | -17.00702 | -55.06286 | 2024-10-06 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 131.0 |
| bb7cea63-4555-35f1-8ab7-d3333023b541 | -16.93723 | -55.84132 | 2024-10-06 00:50:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 12b44cb7-59a9-31e2-ad52-c09559daa71d | -16.93643 | -55.84838 | 2024-10-06 00:50:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 9cc43677-ddc1-3123-9d5d-6523da51656a | -16.85695 | -54.86248 | 2024-10-06 00:50:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 35.4 |
| d3c9f0a7-5d7f-3c4d-9d0c-414236de9066 | -16.6561 | -55.55632 | 2024-10-06 00:50:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 32.5 |
| b9232449-abc8-39e6-b986-3f31fe77ce20 | -16.64165 | -55.55296 | 2024-10-06 00:50:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 175.9 |
| 6bfc8b96-2009-3254-b4b2-3b6c219d8c97 | -16.63894 | -55.55799 | 2024-10-06 00:50:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 166.1 |
| 83bcbbc3-6fd8-3c23-92d4-7659c12a46f5 | -16.63803 | -55.51324 | 2024-10-06 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 1978b728-d494-39a5-8226-d6a1315cbbce | -16.63508 | -55.51834 | 2024-10-06 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| e877b739-6635-38fe-b98b-112c79866fef | -16.62451 | -55.55492 | 2024-10-06 00:50:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.5 |
| cc55658c-3ad4-3dc3-935f-29a17fdf41c6 | -16.6226 | -55.93364 | 2024-10-06 00:50:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 4679cd67-03b9-38e7-b5a8-c2bbb20a9bd1 | -16.62231 | -55.93832 | 2024-10-06 00:50:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 5d2c949b-9a5f-300d-8b59-701e44d944ec | -16.61893 | -55.89077 | 2024-10-06 00:50:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 34.2 |
| fa18a404-5d0e-345e-8a93-9dd1a9ea5e98 | -16.61837 | -55.89548 | 2024-10-06 00:50:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 9f3a1f90-9337-306f-9104-056f2530a916 | -18.53577 | -44.06575 | 2024-10-06 00:50:00 | TERRA_M-M | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ae738c2-f389-38a8-adbc-5afb8d6176c9 | -25.01459 | -54.08085 | 2024-10-06 00:50:00 | TERRA_M-M | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 51.8 |
| 25448c6b-7529-3d20-9e51-f0ad032bc62a | -25.01145 | -54.08928 | 2024-10-06 00:50:00 | TERRA_M-M | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 41.4 |
| 6210ba16-f163-3487-9c37-43100f30d243 | -21.85723 | -48.45405 | 2024-10-06 00:50:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 55d7c705-bdce-3a2b-b20c-f1f37a6cc167 | -21.85558 | -48.43965 | 2024-10-06 00:50:00 | TERRA_M-M | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 17.3 |


[Clique aqui para ver as próximas entradas](README15.md)
