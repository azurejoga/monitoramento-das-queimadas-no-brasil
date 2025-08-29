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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 361012f3-4541-3120-ae9b-efbd58839eff | -15.0835 | -48.1367 | 2025-08-29 13:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b015ec55-dc9e-3933-a69c-fc9a7fa147c2 | -6.3883 | -45.5793 | 2025-08-29 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| d7a40bc2-af88-3dee-9809-5fcc486569e6 | -9.564 | -45.8594 | 2025-08-29 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 470deb14-7f1a-3e52-bb01-0a5512e84c21 | -10.3812 | -57.8245 | 2025-08-29 13:00:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 3c3a05a8-30a3-39e8-a93a-e16e886c469d | -12.8413 | -48.1685 | 2025-08-29 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 90f437a7-00e7-3571-aa20-1b94f1b0f860 | -11.876 | -46.4007 | 2025-08-29 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 5c7e5359-4e85-3bae-9bc5-c7305e5843d6 | -9.545 | -45.8616 | 2025-08-29 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 0acca508-5cb2-3496-83ae-8fca68b48fff | -9.1155 | -65.7699 | 2025-08-29 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 845c938c-b7b1-38d9-889f-24eb32e683c6 | -10.3812 | -57.8245 | 2025-08-29 13:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| f16cc949-bed2-34cc-815c-ab27444e5ac3 | -11.3521 | -43.5423 | 2025-08-29 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 225.9 |
| 0880528c-6b7c-363e-b801-cb4715d01003 | -9.5447 | -45.8842 | 2025-08-29 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 695.4 |
| 2b5c617f-53ee-3c1b-ab4c-cb26b138bab1 | -12.8413 | -48.1685 | 2025-08-29 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c9b23850-85ee-31e7-a254-0f0a592eaa4a | -9.4433 | -60.5499 | 2025-08-29 13:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 246.4 |
| 44412ea4-1ece-3f06-9e4f-e3f44377001e | -11.3517 | -43.566 | 2025-08-29 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 197.6 |
| e0dc9190-a115-3e33-a0e8-beaa265ec964 | -15.1225 | -48.1302 | 2025-08-29 13:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| f944031e-0347-379f-b96f-c17c9a9b7da3 | -11.5722 | -46.2844 | 2025-08-29 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 4f688569-fe1d-36cf-9b34-5bfe28ac0e80 | -7.6183 | -46.2392 | 2025-08-29 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 3e583123-6e58-3924-b169-d40b9f030861 | -9.462 | -60.549 | 2025-08-29 13:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 462.3 |
| 60d7c95f-9f08-3271-a978-aa6b99dfdebe | -10.8607 | -60.8191 | 2025-08-29 13:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 75f5643b-4b19-33e5-917b-cd4f043d4b6a | -11.5527 | -46.3097 | 2025-08-29 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| b51214a8-1f19-3fd6-a03b-7e3e25a50c8a | -9.4432 | -60.5692 | 2025-08-29 13:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 163a462d-c4cb-3842-93d0-4eae088a501e | -12.9182 | -48.1576 | 2025-08-29 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 4f2d1b9e-c86a-3a7f-a47d-d68ffdd156a6 | -8.0647 | -45.0446 | 2025-08-29 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 153.2 |
| b1c619f0-e96e-3819-b83f-e2e4c72d5959 | -13.3543 | -54.38 | 2025-08-29 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 53c0f23d-d893-3bfd-a174-ca84ff279350 | -11.3713 | -43.5394 | 2025-08-29 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| eba9f708-16f5-3433-888a-330f0c87b2b8 | -12.919 | -48.1131 | 2025-08-29 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 8857ed97-35bb-337e-8d2a-9c2d34aa37de | -12.9186 | -48.1354 | 2025-08-29 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 482b10ba-fbdb-3e69-8272-ea2f198aa6b0 | -12.9323 | -46.3362 | 2025-08-29 13:10:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 964f682b-891a-35db-b850-4f0c7750b647 | -9.545 | -45.8616 | 2025-08-29 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| d78b39f2-5742-352e-ad8c-e78cfd62b319 | -9.4618 | -60.5682 | 2025-08-29 13:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 63bab5dd-872c-3330-bac4-29421f5f844a | -11.3329 | -43.5452 | 2025-08-29 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7837ff00-9187-36bd-9d2e-63c391380d3c | -12.913 | -46.3392 | 2025-08-29 13:10:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b111fd10-5f05-3650-b985-2cc5852eb36a | -7.1106 | -44.6099 | 2025-08-29 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| b4e10b88-5830-3138-8e4c-29b9fa26fd99 | -6.3881 | -45.6018 | 2025-08-29 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 623b6dac-58df-3288-aad5-7887be93efe8 | -11.876 | -46.4007 | 2025-08-29 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| e8349d53-31f2-3d26-a584-0216f3865dc6 | -6.2495 | -44.431 | 2025-08-29 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 2e16661c-a6fd-3ea5-8fe3-e1bddad3fd65 | -10.829 | -47.5014 | 2025-08-29 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 77ddc3f3-ab4d-3dc9-8710-04d8e893ba2a | -12.8994 | -48.1381 | 2025-08-29 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| c13038a9-304b-32d3-8424-4da2777c46b6 | -12.9318 | -46.359 | 2025-08-29 13:10:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| a8c15f31-a521-332e-8e96-dff406307438 | -11.3325 | -43.5689 | 2025-08-29 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 1e3a8608-f83c-3acf-b52c-cdb354df0009 | -9.5637 | -45.882 | 2025-08-29 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 245.0 |
| dd126de2-f7d6-37a1-a7ab-600cde655463 | -12.9379 | -48.1326 | 2025-08-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| d8f2472c-340e-31ed-a9ee-e6323cf44578 | -11.5714 | -46.3298 | 2025-08-29 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 222.5 |
| dbf646ca-4a50-3847-8e6c-198d80432cae | -12.9182 | -48.1576 | 2025-08-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 73b51aa0-8d46-3edf-bdbd-23fcb57f1185 | -14.3502 | -53.2453 | 2025-08-29 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e59aec53-965d-30dc-94fc-a3d3fbbb43d8 | -11.3517 | -43.566 | 2025-08-29 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 226.3 |
| 8fd5056d-79e6-30d4-aa81-9fffc17074d2 | -10.848 | -47.4991 | 2025-08-29 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 2f92eedc-24f8-37d6-98a8-b77e726459b0 | -9.1338 | -65.8067 | 2025-08-29 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 6aa3c2b5-6609-3eff-ad79-6cdddb8a1e2d | -12.8994 | -48.1381 | 2025-08-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| bcb0d9f6-88f2-3bb1-9ea1-f524616ac65b | -11.5527 | -46.3097 | 2025-08-29 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 155.7 |
| ee610bf1-689d-37c3-b221-acba8004fb66 | -14.3299 | -53.3108 | 2025-08-29 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e3284342-0f70-3885-98be-24d8699fbb16 | -6.2741 | -43.8299 | 2025-08-29 13:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 71f4d402-69ed-3975-a12c-69b8fe250457 | -11.3521 | -43.5423 | 2025-08-29 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 313.2 |
| 50134c59-5c5e-3e41-89f6-c461a83b8b7d | -7.415 | -44.283 | 2025-08-29 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 4d0382a7-c2f5-3b1e-9883-b0937c7857f4 | -12.0362 | -50.6448 | 2025-08-29 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 8180f1c5-8a3d-37f1-a690-1f43e96a6e35 | -13.5778 | -46.8487 | 2025-08-29 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 1aea09b6-1666-3e9b-ac0e-5c56bb1fde0c | -9.5637 | -45.882 | 2025-08-29 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 154.0 |
| c3f22291-d89d-3845-b2f3-5cd0f29fc535 | -13.5584 | -46.8517 | 2025-08-29 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| c2be7503-ca9e-3eef-8418-d8550e150146 | -8.0838 | -45.0199 | 2025-08-29 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 473e7279-d485-3a28-ba1d-a03bb3204ae3 | -9.1154 | -65.7886 | 2025-08-29 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c12eeaf1-4a37-3814-a447-3561df311f1d | -12.919 | -48.1131 | 2025-08-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b5722cd8-a287-369b-a339-12b3da68a185 | -9.5447 | -45.8842 | 2025-08-29 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 239.2 |
| 27553267-c1ea-3cb8-9000-26cd48235b35 | -14.3149 | -51.8969 | 2025-08-29 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 461167e2-b9be-39fe-919f-e167f9331b6e | -12.0553 | -50.6425 | 2025-08-29 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 99c4747b-8550-3043-9868-3961e43f9b91 | -7.1106 | -44.6099 | 2025-08-29 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 25a168ba-5153-3cc5-8f76-3f81209a2c6a | -12.9186 | -48.1354 | 2025-08-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 46f39c8a-c313-380f-a745-493f98c89f10 | -6.7074 | -49.4561 | 2025-08-29 13:20:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 4dabf774-c9b3-35ca-909e-7ec8bcd97c43 | -7.1108 | -44.587 | 2025-08-29 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3380aae8-ddb3-3e08-92a2-e36a6af1dc18 | -13.5774 | -46.8714 | 2025-08-29 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 240.6 |
| 7329c477-bd4a-3c73-a063-9576aa19b4b2 | -13.558 | -46.8745 | 2025-08-29 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 753d8bc5-c414-3d0d-9ccf-717c7cf985a1 | -10.3812 | -57.8245 | 2025-08-29 13:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 95deab77-e5dd-36ea-ad7b-0747cfc5ff6c | -15.0419 | -57.1852 | 2025-08-29 13:20:00 | GOES-19 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 93ad7dd9-c5ed-3b15-bfde-67b84b2a1289 | -14.3532 | -51.9132 | 2025-08-29 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2f578f0a-72c2-31a5-b3c8-eb6bfaab982e | -9.773 | -64.2469 | 2025-08-29 13:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 46fa8bec-9ace-3e46-8588-415c1d8d8a8c | -10.8483 | -47.4768 | 2025-08-29 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 287e832a-07b9-3bd4-a11a-72eb2f341717 | -13.5576 | -46.8972 | 2025-08-29 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 99b047da-a494-3fd8-b16c-ce5bb9222d72 | -11.876 | -46.4007 | 2025-08-29 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f5946667-ceb6-3bf5-af9f-4217e6e6cb9f | -12.8413 | -48.1685 | 2025-08-29 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 5806dd5d-31e1-3a90-b4c3-30215670ad32 | -9.1155 | -65.7699 | 2025-08-29 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 78500126-483e-35ec-b366-3231e1aadf3a | -6.3881 | -45.6018 | 2025-08-29 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 6227d76e-000c-3af5-8932-e6fa42a3fb74 | -8.0647 | -45.0446 | 2025-08-29 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 176.9 |
| df9c850d-32da-352c-a5ce-ef132b2f9e3b | -15.0835 | -48.1367 | 2025-08-29 13:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| f98fed4d-281c-390b-b8d0-945c867a2cd1 | -15.1225 | -48.1302 | 2025-08-29 13:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 614cc037-848d-39b3-a1a2-88f5325a322e | -12.9182 | -48.1576 | 2025-08-29 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 328423c8-c2ca-3c30-bdbf-9f6bf24ec77a | -14.3303 | -53.2898 | 2025-08-29 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| edf81bb2-14dd-3616-b2b5-b6d4e9e9d7c9 | -11.0826 | -44.7503 | 2025-08-29 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| bf5e487d-9566-3add-a81c-b973b5fecbd4 | -14.3299 | -53.3108 | 2025-08-29 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 608c577d-a87b-3594-a670-9d49c1a410d8 | -11.8756 | -46.4234 | 2025-08-29 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 58625ad5-b0d3-3bd8-be06-9083779b4fb5 | -10.3812 | -57.8245 | 2025-08-29 13:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| eaf77ba9-df36-394d-b5ee-8173c6a82966 | -8.0647 | -45.0446 | 2025-08-29 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 2b0257ce-7436-39be-a91a-3212baceadfa | -13.558 | -46.8745 | 2025-08-29 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 50af9c63-4bec-3385-bc79-b010eea2655d | -7.1108 | -44.587 | 2025-08-29 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| e8352117-b1c2-3e7e-91f9-ccffbcfb0932 | -14.0328 | -44.487 | 2025-08-29 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| d850bd9e-204e-3104-bd18-4fba195fe1bd | -8.1964 | -45.0541 | 2025-08-29 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c76932bf-5300-322a-af40-0be8478b471a | -9.7916 | -64.2461 | 2025-08-29 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 68582108-6ed1-34cb-9995-ee8713ec31c5 | -6.3881 | -45.6018 | 2025-08-29 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 97da3992-08e9-3709-8821-619a3ffc049c | -7.1106 | -44.6099 | 2025-08-29 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 217.9 |
| 483b4758-5826-33ac-92c6-2863669239fa | -6.2743 | -43.8067 | 2025-08-29 13:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 7797b2e9-fc5b-383f-9dc8-99bc06df39af | -11.5714 | -46.3298 | 2025-08-29 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 80876919-5541-3560-b5ab-53703e12a916 | -12.9194 | -56.9672 | 2025-08-29 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |


[Clique aqui para ver as próximas entradas](README95.md)
