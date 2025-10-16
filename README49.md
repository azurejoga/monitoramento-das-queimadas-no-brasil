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
| 21096df4-f2be-3fae-9ee1-ae041ae8e103 | -7.21581 | -47.55361 | 2025-10-16 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46684bf7-84ac-3d35-9ad7-9b7a581417c4 | -5.32717 | -43.93794 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d44eb293-61bb-31c3-a797-100d00b5f5ed | -4.6624 | -44.08998 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5e9cf4a-63ac-38ab-92c1-75892a48615d | -1.89877 | -51.0088 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 097bcc04-724d-3238-a701-1b18981dedbc | -8.2204 | -44.10067 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8443e158-48c0-31b6-aa82-5def3e09e626 | -4.37784 | -43.39794 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8d9a85cc-e05a-3924-87f6-a4688bb31a7c | -4.11346 | -48.01319 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6e40956a-2d25-32dc-b86b-03103bd56dc3 | -5.45235 | -41.02671 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f52ac6d7-505b-3743-b83f-58c176ba30c3 | -4.81209 | -43.20816 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 699fa53a-85b9-3c42-90c5-10aacc6bc820 | -2.71121 | -49.85734 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 794951c4-600b-3374-b37b-a88721374277 | -6.18203 | -44.30034 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8454fb2e-dcf2-3a1d-a182-ce1996a6b3ee | -6.95735 | -46.1391 | 2025-10-16 04:38:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70aebeab-bb27-3f44-9bd8-d77c4593ac25 | -3.45074 | -52.81514 | 2025-10-16 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2051ecc-c0e7-3198-8aba-fb6281b74b2c | -5.88331 | -43.89481 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9fed1d2b-2ad0-366e-912d-8244481d2b32 | -5.68326 | -45.10039 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 08569707-6155-3063-80d5-52363900f229 | -7.66126 | -42.38095 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ce4b9218-b89f-32b5-8e8f-31d94ccc9cdc | -8.0698 | -45.42572 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17228cf7-9bf5-37a3-b9d0-b06b4045e966 | -5.42117 | -44.23819 | 2025-10-16 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c467736d-e845-308b-b99e-3397d96dded3 | -5.47546 | -42.93881 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aa2d752b-f003-3c8c-8e25-6fb8bd43e87d | -3.21938 | -50.2174 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2be41f25-d32f-3b81-9635-2aa18fc66eed | -6.95217 | -47.76159 | 2025-10-16 04:38:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77204207-80fb-3fd7-a2f6-80c89aea0ed5 | -3.01676 | -45.37612 | 2025-10-16 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e55975ba-2c80-30ee-91ff-59c630a593b9 | -7.75686 | -42.46782 | 2025-10-16 04:38:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 59f4d6f1-29d2-3069-8dfa-15d4d4166dc7 | -3.16272 | -51.81646 | 2025-10-16 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9437ef3d-dade-37e3-a962-96903eff78e8 | -8.22433 | -44.01279 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6de4ae2a-2573-3b22-8aab-a67a3f1a0a05 | -7.93604 | -44.12909 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 589ce243-4725-3af2-8b8a-72a8f40df282 | -3.68367 | -47.6269 | 2025-10-16 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 988147aa-dc1a-36b4-a73d-a39a47722dbd | -2.88735 | -50.73616 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cd4826e-797a-365a-aaf6-998968f8e2e7 | -3.88356 | -52.07117 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5a6e76c-a5bf-3bb8-8cdf-f8e452b65439 | -6.50771 | -44.46453 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21b2488e-e31f-3afa-a235-a23e65ad0676 | -5.18396 | -42.92703 | 2025-10-16 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea912ed2-be55-3271-82a6-d2f2e37c09b3 | -6.2038 | -42.61112 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 81e25695-e00c-3aaf-9104-779373c0cded | -5.8768 | -43.88189 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46a86863-4936-39ac-8685-edba80eb02f0 | -7.86187 | -45.97366 | 2025-10-16 04:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d75a0587-c502-3ca9-abf4-fd4290d90e3c | -8.25575 | -44.09392 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95c7ab42-1799-3a32-b54f-1135f02cd136 | -7.00433 | -43.74816 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df78fc2f-d634-3e4c-8577-e2319b79f41e | -6.19694 | -52.73472 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ccea5a20-1f5e-357e-9d94-cb8057c00d49 | -5.43665 | -42.89827 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59659b55-8076-32a4-a68e-32fef1bf1327 | -8.25558 | -44.06892 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98930273-72f3-3086-b539-cc4289dac06f | -5.51014 | -47.30729 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d15d2abf-d57f-3538-8ebf-9d6439a2f2a7 | -6.25997 | -44.02013 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41ec6703-677b-3657-b234-2df367cf62bb | -4.36011 | -45.53241 | 2025-10-16 04:38:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 74059180-04a5-328a-b181-f45c0b80eea2 | -6.53187 | -44.74089 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20dc1d79-242a-37e8-a113-a8cc472489db | -3.49212 | -50.08826 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 003dbd56-f2c1-32b5-b9df-6ed8d6d74fe9 | -2.72772 | -48.34775 | 2025-10-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 973876e7-7ef7-3ca8-b8cb-1e8a5fbed058 | -6.25479 | -44.0269 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f89c9b5f-631d-325f-a4e7-1b63be3fa8ac | -5.57371 | -41.32274 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6e9a10ed-426b-3cc9-98eb-f6a014afed94 | -5.68706 | -45.10096 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 17273ff4-96db-3b8e-89de-bee972318b27 | -1.65626 | -55.14466 | 2025-10-16 04:38:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89b41274-4378-3b1e-acde-e54af0cdeca2 | -3.49272 | -50.01934 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 648a01cc-2e34-3ce9-8574-f18584374461 | -3.28124 | -50.04408 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02e1db3c-5b1e-31ec-be26-f60f17c3ecfa | -7.47865 | -42.75081 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 4d28b796-50cf-32b9-9732-c994f06e177f | -8.21756 | -43.99963 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0e1deeb-f0be-35dd-8fa8-74737260c4a8 | -6.32355 | -44.71127 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 499b17e9-8e0f-3d74-944a-1aaed3bda4d9 | -7.61104 | -46.47774 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4757045b-dee4-3231-8cdb-38753058c5aa | -5.68078 | -44.36286 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a302d2b6-1e3a-3a22-8c05-b1e1e0a0e791 | -2.87822 | -50.72709 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 970a40e6-bc27-3f88-a90e-d1d89f5c69a2 | -3.80954 | -51.31765 | 2025-10-16 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91e00c6c-b136-37dd-8da0-aab3d238f4d5 | -6.49696 | -47.22794 | 2025-10-16 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8de2970a-bd18-34ff-bf01-108dee71cfe0 | -5.88015 | -43.85923 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f82088c-4f25-3f70-9982-20a2e6452193 | -5.9031 | -42.81522 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f04acef0-1dbc-34d5-81b4-21f8c1df4010 | -6.05291 | -41.941 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f6a2b15e-a769-3ed2-9890-1bf93a77c3e2 | -8.26135 | -43.43375 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cf67852c-058d-39ed-a4fd-279da0cac151 | -7.21929 | -45.16556 | 2025-10-16 04:38:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b74ac425-b6fb-331e-ac86-38f2f35d611f | -6.06905 | -44.30548 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddfd84d7-39da-3e81-8f6e-e383034e217a | -7.50417 | -46.64031 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b4c6e21-47cd-3eec-b0c0-4c956d7a8224 | -4.10745 | -48.03002 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 2bd4b4e2-1261-372d-9b82-3f83e12212ff | -6.66276 | -46.33459 | 2025-10-16 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adff0cb6-e63c-3adb-a109-a608fcb65132 | -5.43279 | -40.98137 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| dd313aa7-2f95-3804-9cbf-682886812d8d | -6.12545 | -44.28554 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b5cd157-b788-3237-ac77-ccc939e9b55f | -7.22031 | -47.86894 | 2025-10-16 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f702ca66-e823-3a08-81f2-bb65568d403b | -3.68657 | -52.1031 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3dffa1b8-40e8-3b45-a338-943414622485 | -8.29714 | -43.40291 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c0427ac0-596f-3db1-88a1-abbca8b1f268 | -6.06352 | -44.31536 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa4addd9-83bc-312b-9338-0a3d8b1f627c | -6.59515 | -43.9177 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d67c647-521c-370f-8ddb-f0bcc34e72fa | -7.92821 | -44.12395 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e560de3f-3503-3843-a460-221d973e1e5b | -5.40635 | -40.91571 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b819323-3b6f-39ef-96a4-a236af826902 | -4.11292 | -48.01667 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dd57db28-9901-3b69-92c5-b46d62f22105 | -5.87394 | -43.90122 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5161e0f-6c3b-355d-b217-9cd77b67efc0 | -7.9444 | -44.13033 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84cc36d6-96d9-3223-8e24-9916de02b783 | -4.85007 | -48.76962 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83a80f03-fadf-39e9-8094-9a4b7d108537 | -4.38061 | -43.37902 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d686cec-a618-3329-b341-5f56882b54e8 | -6.32928 | -44.31608 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24dfab3e-2b28-3a06-b6ba-4eb30e5eaed9 | -7.48905 | -47.02865 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4b1b1ca-a9dd-3921-8d5d-a7dc66793d58 | -5.42969 | -44.23589 | 2025-10-16 04:38:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b284bc9d-6039-3a60-8d62-c82622315ed2 | -6.9434 | -44.47387 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c909217-6436-3c70-bd39-e9a990bcee0c | -4.928 | -45.88675 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b18ff72-6f13-31da-b130-b5c7849ecb06 | -1.48598 | -55.67934 | 2025-10-16 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c5fc48b-19b6-3e2b-aa9a-6be0e97bcf52 | -6.1819 | -42.60294 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e36cf67c-f5db-356f-b07b-70d114d881e1 | -2.87244 | -50.7415 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b47413e8-cfc3-333c-a34e-c771e10ae728 | -5.46647 | -44.64552 | 2025-10-16 04:38:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29976448-a1e9-32a4-9275-396d4f260437 | -7.47932 | -42.74619 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 94f72bbc-ba47-34cd-9dab-fdcf11609c00 | -7.74882 | -42.49169 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cd7f826a-4163-3637-bbc0-391f72a434d8 | -2.38745 | -47.71194 | 2025-10-16 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82639345-7798-301e-a736-ca8a7217d324 | -6.5219 | -42.19359 | 2025-10-16 04:38:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a4110b82-69f3-3931-a1a3-6f5e69a0d6de | -8.26577 | -43.43435 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 08274cb0-4b3d-32d0-a821-8c8593f2f552 | -5.43196 | -40.98711 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 26e5345a-18ca-356c-8fb4-9bc5f6f97f64 | -5.85158 | -42.8908 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 710c4d24-be0a-30ca-b869-fda2dcdb81a1 | -5.86577 | -43.84222 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36efc65c-8f83-3d24-8ec7-d32523487085 | -6.02417 | -44.32072 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README50.md)
