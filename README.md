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
| 10df83f0-f6df-39ed-acb0-eb9379368492 | -6.2945 | -43.6659 | 2025-07-03 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 9d6df2b7-db49-304f-ab51-d2edae3bfc45 | -6.9419 | -42.8598 | 2025-07-03 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 14bfd637-ba2c-3fac-89be-b3ee2e6bb943 | -6.0206 | -49.2234 | 2025-07-03 00:00:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| f8d8cc83-bf8f-386a-b529-2afe6f3bdcca | -17.9376 | -50.6464 | 2025-07-03 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 01b39b0e-6937-3c95-a975-5e862475de62 | -6.9416 | -42.8834 | 2025-07-03 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 247.2 |
| f6f9b767-f2a5-3c1a-a1b3-32113e9135e7 | -14.6287 | -53.9018 | 2025-07-03 00:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 001a3b9a-5c83-3894-8e8e-6476d8d74b27 | -17.9366 | -50.6907 | 2025-07-03 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d31bc52d-eee0-3bbd-a60c-f8bf15cdf9bb | -6.1792 | -48.0494 | 2025-07-03 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 88ef8d30-7f09-31ff-b011-b32b70bc9eb4 | -6.1979 | -48.0482 | 2025-07-03 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 37daa5cd-ddc8-3fe6-ab71-57858d61a9b7 | -6.9793 | -42.8798 | 2025-07-03 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.1 |
| aedfa679-806e-3c0f-b4c0-6037904059d2 | -14.6484 | -53.8785 | 2025-07-03 00:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 74840b85-c408-3609-ab07-731a656001d4 | -11.6383 | -48.0644 | 2025-07-03 00:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 2ec200e7-c026-3e88-9e6d-f59765b78feb | -17.9575 | -50.6429 | 2025-07-03 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 8e700086-bade-367e-a62f-be1f50f240d1 | -6.9607 | -42.858 | 2025-07-03 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.9 |
| 694ab25b-cd88-3c52-b1e7-e4dff333f94b | -6.6112 | -43.8941 | 2025-07-03 00:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| bb2078b5-787e-33f2-907c-9bedbfe1358a | -6.1606 | -48.0507 | 2025-07-03 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 0923b9c9-1306-309a-8bde-512a4d918c05 | -18.2 | -51.3481 | 2025-07-03 00:00:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 76d01c57-0e03-3082-8b37-326d603bd310 | -6.2943 | -43.6891 | 2025-07-03 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| a9600865-11bc-3929-95ef-14796c03f358 | -18.22 | -51.3446 | 2025-07-03 00:00:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 149.8 |
| dd00c6a3-45ac-3a33-9878-9e47b1166592 | -6.9602 | -42.9052 | 2025-07-03 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| dcf6be4a-5358-3c70-863f-fffa58c3c216 | -11.6379 | -48.0866 | 2025-07-03 00:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 8f391b12-5a34-3e67-8923-3f88ab93350f | -9.1668 | -48.7794 | 2025-07-03 00:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 1894b260-f616-3db7-99f9-494cc819d699 | -6.1791 | -48.0712 | 2025-07-03 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| f2abfbf4-eb8d-3e74-a8b1-095fddc3f18a | -11.1121 | -48.875 | 2025-07-03 00:00:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 01c6e532-c06b-3fab-9224-44d43b5c429c | -14.6291 | -53.8809 | 2025-07-03 00:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 164.8 |
| a43dc633-3ed5-3b77-a0ad-cc264f5d0008 | -9.1857 | -48.7776 | 2025-07-03 00:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 167.2 |
| 7a1611af-0630-30f7-9a7a-567842b6928e | -14.6481 | -53.8994 | 2025-07-03 00:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 2b043bf3-4a4d-3a1c-abc4-47a303b475fa | -17.9565 | -50.6872 | 2025-07-03 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 518b4fef-90a0-3099-91e4-f14bf8f93f78 | -17.9371 | -50.6685 | 2025-07-03 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 182.9 |
| d592999e-9a55-3453-a5b1-b7c78d062d8b | -9.186 | -48.7559 | 2025-07-03 00:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 76b3c2a1-72aa-3d69-8268-1ccf3529837c | -9.623 | -61.4624 | 2025-07-03 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 206d1309-08e3-301f-a885-204c4eeac9cc | -5.9938 | -43.7366 | 2025-07-03 00:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 725e48f3-b7ea-3c33-838d-05088d3ee4af | -18.2195 | -51.3666 | 2025-07-03 00:00:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| af256752-7546-3019-a77a-63dfd902a2d1 | -9.1671 | -48.7577 | 2025-07-03 00:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 57004085-f82a-3109-b4bb-4b63c09db200 | -6.9605 | -42.8816 | 2025-07-03 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 464.5 |
| 3925e78e-0f09-3145-8210-07083ef11cc4 | -6.1604 | -48.0724 | 2025-07-03 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| d9c5b6d8-027c-3703-95d4-7a1d4f38c439 | -17.957 | -50.665 | 2025-07-03 00:00:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 188.0 |
| f35bcfec-dbdc-3d55-9225-e03fdb07a612 | -11.6383 | -48.0644 | 2025-07-03 00:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 338b40f2-b103-3520-ab59-f2db28e75f89 | -9.1668 | -48.7794 | 2025-07-03 00:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 170.3 |
| de2ab0ca-fac4-3d69-85a6-1bc72d2434ee | -14.6291 | -53.8809 | 2025-07-03 00:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 136.6 |
| a6c91f9f-1f96-3c91-aad0-3cf5374f7aee | -9.623 | -61.4624 | 2025-07-03 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| ab06623d-fec3-3afd-84a6-600dede2f9a1 | -9.1857 | -48.7776 | 2025-07-03 00:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 4acbcbc0-acb2-31a6-9fba-1e7bdaff983d | -14.6481 | -53.8994 | 2025-07-03 00:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 4d3fcc3e-5ac8-38f5-b4c1-2baa1e0e8384 | -7.2222 | -43.0447 | 2025-07-03 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 243.6 |
| a0b5930a-cf33-3473-8878-317264a40052 | -11.6396 | -44.6003 | 2025-07-03 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 0cf95b67-e851-36ed-9886-810288b0a1ab | -6.0206 | -49.2234 | 2025-07-03 00:10:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| c5c18026-bfdd-337c-b589-94e32a056c86 | -7.2028 | -43.0936 | 2025-07-03 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| 9859120f-727a-3c90-8587-9e08374b1a62 | -7.2031 | -43.0701 | 2025-07-03 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| b3a2d38f-e062-3900-98a9-c4e7115b1e49 | -11.6379 | -48.0866 | 2025-07-03 00:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 5c5b7877-0e1c-3677-82ba-e36bd1e36e04 | -11.6588 | -44.5974 | 2025-07-03 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 230.4 |
| a3d35574-6ea2-30b4-883b-f3d1146bcd14 | -7.2411 | -43.0428 | 2025-07-03 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 554d3c4b-48f3-3bfa-9d8e-17508bf0933f | -6.2945 | -43.6659 | 2025-07-03 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| c1392529-6f88-3ab2-be26-ad1057cbc60f | -14.6287 | -53.9018 | 2025-07-03 00:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 17b618c4-f083-335a-be13-86f281bce2a3 | -11.64 | -44.577 | 2025-07-03 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 294.9 |
| 24699df6-f06d-3e48-a4cb-27e17ff49b98 | -9.186 | -48.7559 | 2025-07-03 00:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 84.9 |
| db85ab11-0823-3b33-b524-4a247572c2a4 | -9.1671 | -48.7577 | 2025-07-03 00:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 8a6eb4af-8a49-3931-a8dc-783b2f08b8b3 | -6.1791 | -48.0712 | 2025-07-03 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ef9365d1-ebac-3285-b89a-8b92571c8621 | -6.1606 | -48.0507 | 2025-07-03 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| aea8fd51-cc92-3b3e-b3da-a2c95abbd8e4 | -6.1792 | -48.0494 | 2025-07-03 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 510c05ca-8550-33ad-a247-9b6ab469284b | -6.1604 | -48.0724 | 2025-07-03 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1fa36c09-7d88-3098-9e27-a2ee79e88eec | -18.2195 | -51.3666 | 2025-07-03 00:10:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| cd5c0b40-bd7d-3785-b1e7-0be03a28be1b | -7.2408 | -43.0664 | 2025-07-03 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 161.0 |
| a6940ec2-41ac-34d8-8b73-e993b3a28414 | -18.2 | -51.3481 | 2025-07-03 00:10:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 1339926f-1081-3e9f-b4cd-51f601bdc4d1 | -17.957 | -50.665 | 2025-07-03 00:10:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 37.4 |
| a752b90c-e99e-36cf-b97b-4cd623ebe225 | -17.9371 | -50.6685 | 2025-07-03 00:10:00 | GOES-19 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 0785db5c-0036-3d5b-bb38-c7bc7ccbd1cf | -6.2943 | -43.6891 | 2025-07-03 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| ffbc17e1-c8de-3954-8bf2-89281b41506f | -6.6112 | -43.8941 | 2025-07-03 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 6eecc968-b8df-359d-b474-462bc2ee4662 | -11.6592 | -44.5741 | 2025-07-03 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 417.4 |
| faa6d902-e4a7-3fb2-9561-706f034621a1 | -7.2219 | -43.0682 | 2025-07-03 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 429.3 |
| f7df7109-e528-3034-86db-3f3f85b32004 | -11.1121 | -48.875 | 2025-07-03 00:10:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| ec9ef602-eaa6-37d0-8e77-12e17d45658e | -18.22 | -51.3446 | 2025-07-03 00:10:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 99ea3fd3-cc2b-3cfd-816c-97ece551e0ec | -14.6484 | -53.8785 | 2025-07-03 00:10:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 04c72ff9-3ea0-3fa6-a6ff-ece7671a0ad2 | -6.2755 | -43.6907 | 2025-07-03 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| c0711529-a0a1-30ab-b45e-da8d760bc57e | -7.2222 | -43.0447 | 2025-07-03 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 237.6 |
| 6852e0bc-1ec2-3a4f-8eed-b1333a815b0b | -9.1857 | -48.7776 | 2025-07-03 00:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 56078ace-006f-38f8-b478-2a797454beb0 | -7.2219 | -43.0682 | 2025-07-03 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 351.5 |
| a1580eee-bd62-39e5-8d93-8e1aaa2c4f96 | -9.186 | -48.7559 | 2025-07-03 00:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 475fe99a-d2be-3b0b-b9c3-78f09f7fc6e6 | -9.623 | -61.4624 | 2025-07-03 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ee4ea408-466b-3696-9839-bb236815f82d | -6.0206 | -49.2234 | 2025-07-03 00:20:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| e9ab5689-c726-34ad-91fd-ea550ea0e432 | -6.0125 | -43.7352 | 2025-07-03 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| afbf18fb-b301-3c4b-98f3-58d59b62d74c | -11.6592 | -44.5741 | 2025-07-03 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 255.4 |
| d28749e9-229b-33db-a2e5-10687790bce0 | -6.2943 | -43.6891 | 2025-07-03 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| e51d2f7b-7bdc-3a54-83c6-b8048b9fbea2 | -6.2757 | -43.6675 | 2025-07-03 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 7c9a9aae-a17e-3d04-8992-6728271c4eba | -14.6484 | -53.8785 | 2025-07-03 00:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 18ee7f92-2fcd-34c0-a83e-b2afee3a0937 | -18.2 | -51.3481 | 2025-07-03 00:20:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| f88fabba-d0cf-3d6b-95dc-940bc343c069 | -6.1606 | -48.0507 | 2025-07-03 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| aa6a82fe-fe46-3aad-a487-df07504bbffd | -7.2408 | -43.0664 | 2025-07-03 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.6 |
| 6ee1e53c-50fa-3156-b287-9a4217519237 | -6.2755 | -43.6907 | 2025-07-03 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 1ef7a2b4-c288-33af-b2f1-9947c92c7ffc | -11.6383 | -48.0644 | 2025-07-03 00:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 2410c04b-6add-3c26-a223-873eb01a8491 | -11.64 | -44.577 | 2025-07-03 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 54851d22-8387-37e2-bd04-357fc5590ee4 | -5.9935 | -43.7598 | 2025-07-03 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 8b98a9e4-3d93-3dc3-be98-7de1029f8da7 | -11.6588 | -44.5974 | 2025-07-03 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 9f2c454c-106f-3688-a7d7-487f011e4844 | -14.6481 | -53.8994 | 2025-07-03 00:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 784c87f8-db35-33af-bd7b-15b60e7992ab | -7.2028 | -43.0936 | 2025-07-03 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.1 |
| e75befc0-a2dc-3a4c-aa04-52c7baebae25 | -9.1671 | -48.7577 | 2025-07-03 00:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 100.8 |
| f0bf582b-a14c-3b61-8cd1-07a2d3c03b68 | -11.6396 | -44.6003 | 2025-07-03 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a6ed7609-6c88-307f-9984-9218b471cbb7 | -14.6287 | -53.9018 | 2025-07-03 00:20:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 15cd0fe7-63ab-3f6e-bcd5-192639a5bc62 | -18.22 | -51.3446 | 2025-07-03 00:20:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 19951b21-a471-32d2-bd07-1b9ff2883669 | -5.9938 | -43.7366 | 2025-07-03 00:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| a1a66ce5-a87a-33a9-bbc1-34256f2249de | -18.2195 | -51.3666 | 2025-07-03 00:20:00 | GOES-19 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |


[Clique aqui para ver as próximas entradas](README2.md)
