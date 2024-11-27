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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c6b9906-7cdb-3f4d-897c-029029d585d9 | -17.73707 | -39.52836 | 2024-11-27 03:06:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4ad136ea-c558-31b8-a670-f5cc35b4540b | -17.73123 | -39.52692 | 2024-11-27 03:06:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6412244c-ad72-37ef-a3f2-e909dd69a546 | -4.2299 | -50.8983 | 2024-11-27 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e3748d35-3382-39ac-8ea9-0a61668c7df3 | -3.1691 | -48.4394 | 2024-11-27 03:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 7ea7381e-804a-35e9-9617-5674d7d8f13a | -3.0949 | -53.2588 | 2024-11-27 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 28e56976-a261-3481-a80d-8571d2155275 | -2.8347 | -54.1125 | 2024-11-27 03:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 413f9ed3-2637-3c22-ac04-427ecdcc365c | -3.1133 | -53.2583 | 2024-11-27 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 53fefe11-e729-3002-bd4e-b4dce4b22347 | -3.1133 | -53.2381 | 2024-11-27 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 7798f2f1-712f-3c4a-a561-279eb2877427 | -5.9975 | -45.3607 | 2024-11-27 03:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 835659bd-89e2-3faa-8c99-b5abef90d8f2 | -4.1417 | -43.8135 | 2024-11-27 03:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ef81c6fc-3f4e-3820-b169-beb78eb13511 | -2.9428 | -54.7904 | 2024-11-27 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9915323b-3390-364b-b2e0-1c94dfa5972a | -3.0949 | -53.2385 | 2024-11-27 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8cec4d28-ba25-373a-96dc-28e8492fe0fd | -2.1928 | -53.7839 | 2024-11-27 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 23aa974a-8e23-3aee-b925-cc6adc0228c6 | -3.1876 | -48.4387 | 2024-11-27 03:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0c2356f2-dc31-38d3-87c3-844a625e6dc3 | -4.2114 | -50.899 | 2024-11-27 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 2e995cf0-97a8-3f90-805c-3afcf435da2f | -4.23 | -50.8774 | 2024-11-27 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b106047a-b789-39e2-882d-675f2ea93aad | -2.8346 | -54.1326 | 2024-11-27 03:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 2c0e11a5-48e7-3ffd-bde0-2c76760abe8b | -3.1692 | -48.4179 | 2024-11-27 03:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a6824af6-8cd9-3bb0-b0eb-3297dbfac5d5 | -3.9675 | -48.0634 | 2024-11-27 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 44f9613e-8cb5-3b13-8258-5e82ececeeec | -3.0393 | -48.5082 | 2024-11-27 03:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 7dac12e3-b046-3d3b-912c-549b58c92f1b | -5.9788 | -45.3621 | 2024-11-27 03:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 312eaff4-b488-3657-b70a-e9ec5db1549c | -3.9674 | -48.0851 | 2024-11-27 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b1914534-1505-3dd3-835e-98c14713d816 | -4.2115 | -50.8782 | 2024-11-27 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| bba19da9-79b2-32be-a51a-104e40211b44 | -2.8347 | -54.1125 | 2024-11-27 03:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 05d4922d-35e6-3dc9-b61b-85551eeded5a | -3.0948 | -53.2791 | 2024-11-27 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 8be404e7-e8ae-35e5-827b-b0ce785e4b3b | -1.791 | -52.7376 | 2024-11-27 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| a4019ff0-a003-3d96-9656-b889ec216e7c | -3.1133 | -53.2583 | 2024-11-27 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 916c9705-d2ff-3c26-9275-8cd0fd3a48f6 | -3.1876 | -48.4387 | 2024-11-27 03:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| deb830b3-0f85-303b-be30-9fe34198918e | -4.2115 | -50.8782 | 2024-11-27 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 972d4f5a-83ac-36ae-b136-51301183d514 | -3.1133 | -53.2381 | 2024-11-27 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| a6f32591-170d-3009-9c88-115782867e86 | -3.0393 | -48.5082 | 2024-11-27 03:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 42f7fde7-2f8a-3e74-9a22-ea3dbe2f7a3c | -2.8346 | -54.1326 | 2024-11-27 03:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 9afb2a7b-0827-3b27-9930-12184d0f6157 | -3.1877 | -48.4172 | 2024-11-27 03:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 5618ceeb-2cf3-3707-ac8c-94d972dc1062 | -5.9975 | -45.3607 | 2024-11-27 03:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| d7980c5a-8bc8-37b4-a0c1-f4a2e8fd6578 | -2.1744 | -53.7842 | 2024-11-27 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 22463419-3254-3c5c-9f38-874694b25a68 | -3.1692 | -48.4179 | 2024-11-27 03:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| f12f9947-5cbf-3acc-acbc-4992bffdeaed | -3.0949 | -53.2385 | 2024-11-27 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 4fefb414-708b-3b81-bc72-1377034c92b1 | -2.9428 | -54.7904 | 2024-11-27 03:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7fd5635c-2724-36e4-9f4f-3d5fe43228fc | -4.1417 | -43.8135 | 2024-11-27 03:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 3988b46d-cf81-3a14-8c26-28a7605701e1 | -4.2114 | -50.899 | 2024-11-27 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 57c7695d-fad9-3d1a-b981-974f4b06d656 | -3.9674 | -48.0851 | 2024-11-27 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 456648eb-c193-30fd-82c1-362eaa836ac4 | -5.9788 | -45.3621 | 2024-11-27 03:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| bb92ebae-51de-3b60-ac93-794bad618011 | -3.1691 | -48.4394 | 2024-11-27 03:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 15fdc927-32b1-3374-b829-8bd0d1494bde | -3.0578 | -48.5076 | 2024-11-27 03:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 9f8cfb31-be29-3c22-97b9-bee7cd7444fe | -4.2299 | -50.8983 | 2024-11-27 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 5e6519b9-b583-3f1d-bc4a-98b2d131ac3b | -4.23 | -50.8774 | 2024-11-27 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a106ad32-d990-3a8f-b0e6-9c25810aa4ae | -3.0949 | -53.2588 | 2024-11-27 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 164.4 |
| de359d78-a611-3810-a97a-b78ecb22e7b6 | -2.9428 | -54.7904 | 2024-11-27 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| f8c0fe13-c512-381b-8f18-37616183c3e3 | -5.9788 | -45.3621 | 2024-11-27 03:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ee7ef680-d438-377f-b033-35eac861c7ec | -3.1691 | -48.4394 | 2024-11-27 03:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| dccd773f-9562-35f2-afa6-576d1f003c86 | -4.23 | -50.8774 | 2024-11-27 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 5945215f-351c-30c8-a663-edc367e6afd8 | -4.2114 | -50.899 | 2024-11-27 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 180.1 |
| bb780d7e-5214-3b4d-be33-2d5b701486c9 | -3.1692 | -48.4179 | 2024-11-27 03:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 8b6e8c04-105f-3f14-9dc0-9601f3751e13 | -5.9975 | -45.3607 | 2024-11-27 03:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 6353b66b-3187-3d05-960f-dad01fc65e9f | -3.0948 | -53.2791 | 2024-11-27 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 4f1c746a-f6c5-35b1-84b1-f3011aacb8e1 | -2.1744 | -53.7842 | 2024-11-27 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| fd43e76f-c518-3929-9287-5aa021d4dc16 | -4.2115 | -50.8782 | 2024-11-27 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 30ce2484-cdc3-3514-a42a-0da80223f6ed | -3.0949 | -53.2385 | 2024-11-27 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| baa23201-d12f-3599-8717-58330f450af8 | -3.1133 | -53.2381 | 2024-11-27 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| b914adcb-87a8-3d64-8ac2-c8387d477ac6 | -3.0578 | -48.5076 | 2024-11-27 03:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| cd6b6db8-1c26-36b0-8473-e3db256b31f3 | -3.1876 | -48.4387 | 2024-11-27 03:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 35179edf-3717-3e83-b35b-2baa5f4c249c | -4.2299 | -50.8983 | 2024-11-27 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 72da0f74-1f0a-3446-bdff-2ffcba0567af | -3.0949 | -53.2588 | 2024-11-27 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 214.1 |
| 441514d0-5998-3e59-bc0d-4fc5b760666b | -3.1133 | -53.2583 | 2024-11-27 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 164.4 |
| 345973c1-c7c4-305e-8cad-05acd9df5a11 | -5.9975 | -45.3607 | 2024-11-27 03:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 832f17d9-ab08-3797-857a-a7e8c10411c0 | -3.0765 | -53.2593 | 2024-11-27 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 5bb1e03a-c47d-362b-aed5-bc94a49c082c | -3.1691 | -48.4394 | 2024-11-27 03:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 2f663685-e0bd-35c7-85ba-cd6386adf916 | -3.0948 | -53.2791 | 2024-11-27 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 845c01ef-dba0-3e04-b0b2-16ada4eb5597 | -3.0949 | -53.2385 | 2024-11-27 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 85a8322d-85c5-31da-b73a-81a9653acbf7 | -5.9788 | -45.3621 | 2024-11-27 03:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| d3a79d82-1af5-3ad3-a169-4e8865ccc5e3 | -3.0949 | -53.2588 | 2024-11-27 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 202.7 |
| ac952f77-df3c-3a3c-bdea-86b8dee04083 | -3.1692 | -48.4179 | 2024-11-27 03:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8b9e0547-13ad-3e65-a47a-41b621984c83 | -2.8347 | -54.1125 | 2024-11-27 03:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| dbeaa232-92a1-323e-b894-ba90f1304809 | -3.0393 | -48.5082 | 2024-11-27 03:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| fc820508-1a91-3a8c-a751-7d7a25ef710a | -2.8346 | -54.1326 | 2024-11-27 03:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 607d6562-cb30-347a-a5d1-3744100eb1f5 | -3.1133 | -53.2583 | 2024-11-27 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 08350d02-56c1-396d-8234-c5f1715c73cd | -3.1876 | -48.4387 | 2024-11-27 03:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8bfecd06-fa5e-338c-81bd-6ffcfe3c36c6 | -2.1928 | -53.7839 | 2024-11-27 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| efe9278c-476a-3985-abc1-d2b4f0c22304 | -3.1133 | -53.2381 | 2024-11-27 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 07a6ed8c-d90b-3473-aa80-a919080b7a81 | -4.2115 | -50.8782 | 2024-11-27 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ad1da01e-e8ac-3585-98bd-2511162f5feb | -2.8346 | -54.1326 | 2024-11-27 03:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 443e6d12-2a97-3696-9237-25cb97d5d3dd | -3.1876 | -48.4387 | 2024-11-27 03:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| d029bbbc-838e-3d04-895a-814d8c611a25 | -4.2299 | -50.8983 | 2024-11-27 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 824127de-568b-3b90-8eeb-971436db0ae2 | -5.9975 | -45.3607 | 2024-11-27 03:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 7db719f3-5013-3e19-9d2c-0a5e1e064da7 | -5.9788 | -45.3621 | 2024-11-27 03:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| aa814fc1-42ef-323f-bbda-20c27d72b533 | -4.2114 | -50.899 | 2024-11-27 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 3cd8e508-69ee-3dd8-b5b0-6fa588fb0cd8 | -3.0949 | -53.2385 | 2024-11-27 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 5f10f89b-b08d-3205-818b-8bf6b2a44319 | -2.9428 | -54.7904 | 2024-11-27 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 051d42ba-98e8-339d-ac85-0b07f4abbb37 | -3.1692 | -48.4179 | 2024-11-27 03:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 9dd59b71-289c-3f54-8306-01ccde1b1b77 | -3.1133 | -53.2583 | 2024-11-27 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| a4cbfd5e-78a6-3c6a-b548-500f4d24b4e6 | -3.0578 | -48.5076 | 2024-11-27 03:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| c6946954-5d74-3ad8-8708-4461d4524981 | -3.1691 | -48.4394 | 2024-11-27 03:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 8d9289e2-77f1-3c1c-9ee0-dfcaf1eaa282 | -2.8347 | -54.1125 | 2024-11-27 03:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| c31611ec-b01e-3d08-a735-fdd269bd4d11 | -4.23 | -50.8774 | 2024-11-27 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 01d089c5-3b90-31be-9faf-f1581c2f5d39 | -2.1744 | -53.7842 | 2024-11-27 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 39baa730-9500-38af-a97f-a1d02e30ed67 | -22.9841 | -50.4019 | 2024-11-27 03:50:00 | GOES-16 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| 9b57749f-2502-3bcd-8b1a-4cfdab6346f8 | -3.0949 | -53.2588 | 2024-11-27 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 066f93ff-f013-34d1-9253-cf74073b73c5 | 0.6571 | -50.8268 | 2024-11-27 03:53:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 846c4244-ae96-3dfc-9e13-54b1e20ba5e9 | 0.65297 | -50.8271 | 2024-11-27 03:53:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 46b11903-96cd-34b0-8260-61c1b4c85317 | -2.82368 | -46.83447 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README23.md)
