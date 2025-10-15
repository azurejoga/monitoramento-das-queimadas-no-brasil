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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a2f2dda-6483-3253-99a0-4fb870615010 | -4.3222 | -42.0225 | 2025-10-15 14:30:00 | GOES-19 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 146.0 |
| f6386770-f9c5-36da-a6bb-43e6b07cfef9 | -9.1532 | -46.8921 | 2025-10-15 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 25cea37e-59a3-3068-b9c1-c31236e74522 | -4.7313 | -44.9015 | 2025-10-15 14:30:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 1bc86a87-78af-3496-9ef3-b37c67fe0b77 | -4.6511 | -43.1104 | 2025-10-15 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 248.3 |
| db3fd74a-cee2-3dba-a0ee-98d71056e641 | -6.4637 | -41.8351 | 2025-10-15 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 128.4 |
| 6b8ea652-6c86-37d9-b603-38b1e638dfcd | -4.856 | -43.214 | 2025-10-15 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| ad630c57-f341-3829-9023-ea0ffce08939 | -10.8097 | -43.951 | 2025-10-15 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 6d31ec6f-03b1-356d-b4db-51d7d7a72474 | 1.0766 | -51.0611 | 2025-10-15 14:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 64983d34-cc59-3e9a-9b71-6b81a84dd64d | -5.2676 | -43.2327 | 2025-10-15 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| db674621-c85f-3e72-9a75-50c1a3e35ebe | -6.4634 | -41.8591 | 2025-10-15 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| edb2a31d-a67e-3287-889b-0b64bd7b6f8a | -11.4384 | -44.0703 | 2025-10-15 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| dd3e085a-965a-334f-9a0b-e361a27d9ab7 | -5.2496 | -40.9731 | 2025-10-15 14:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 188.3 |
| 921eebce-c9b0-38c8-9d5f-214f49d60ca3 | -10.8285 | -43.9717 | 2025-10-15 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| cdb195fd-bc15-39e8-9f30-820004a3e331 | -5.6284 | -42.69 | 2025-10-15 14:30:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| c860892d-b009-3f74-ab6e-715187a259e9 | -4.7312 | -44.9242 | 2025-10-15 14:30:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 81875321-09e6-30b6-b161-fc8dce3fb511 | -11.438 | -44.0938 | 2025-10-15 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 185068ab-1256-339e-9be4-4705403d6a97 | -5.2866 | -41.043 | 2025-10-15 14:30:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 191.8 |
| 2f5014fa-897b-39da-bf21-c4a92a1939e8 | -5.8614 | -43.8627 | 2025-10-15 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 5eec79e5-37fa-312b-bd05-01009453fe4d | -4.6696 | -43.1326 | 2025-10-15 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 201.9 |
| 7bf41d14-b309-3b65-9a10-0d688bb1245c | -4.6698 | -43.1092 | 2025-10-15 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 08e0b7a2-2310-3b9b-a771-745235bd4162 | -9.3221 | -46.9631 | 2025-10-15 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 415c2dba-a03f-37d8-9f1f-40c91bbd5f2a | -4.5917 | -43.5563 | 2025-10-15 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 25a24722-a288-368c-87a4-459f55011424 | -3.6722 | -44.3656 | 2025-10-15 14:30:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 195.3 |
| fc1b5eaf-2745-3d82-8ef9-7cd354c0251d | -3.6721 | -44.3884 | 2025-10-15 14:30:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 5834fb95-00f1-35db-9761-fffc582162f6 | -4.1375 | -41.6516 | 2025-10-15 14:40:00 | GOES-19 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 133.5 |
| fee3c696-01be-3699-8d0c-bfea1c61b6c7 | -5.4465 | -44.2159 | 2025-10-15 14:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 299.1 |
| d79628dc-6f1a-34b3-b75d-b0156e0e11c8 | -3.6908 | -44.3647 | 2025-10-15 14:40:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 844c4057-35a2-3295-bfbb-415ac8bdcabf | -2.8644 | -50.7361 | 2025-10-15 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| f3ac2f3f-9f81-33a4-aab1-453a1fffd819 | -7.7575 | -42.4458 | 2025-10-15 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 5b82373b-9fcd-3e46-845a-4ff31e707b88 | -5.2866 | -41.043 | 2025-10-15 14:40:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 222.0 |
| e21a535c-922e-399d-b6c1-32952b58c78a | -8.9476 | -45.3161 | 2025-10-15 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 62be153f-fdab-3eed-a6f5-5544fcb7853b | -8.1909 | -43.9964 | 2025-10-15 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 5c3ef925-2bf5-31a6-8f30-6d48127dad30 | -5.2676 | -43.2327 | 2025-10-15 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| cd5c752f-11a2-3dcc-8df1-de1c285ded79 | -10.1333 | -44.5545 | 2025-10-15 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e02d0dc7-a10d-36c0-98f5-007d983b5e14 | -5.8614 | -43.8627 | 2025-10-15 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 5e37cc2b-9659-37de-8361-75c08251619b | -4.3222 | -42.0225 | 2025-10-15 14:40:00 | GOES-19 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 133.1 |
| 8f1f5b53-2ff1-38b0-88d0-d359c7139324 | -5.6284 | -42.69 | 2025-10-15 14:40:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 8fb5059e-058b-364a-a697-a672fe949a95 | -10.6734 | -45.2896 | 2025-10-15 14:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 3060b4e3-75bd-3b8e-8331-65cb6fe844d1 | -5.3045 | -43.3001 | 2025-10-15 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| a182f60d-7851-34e5-ac2a-d4530ef22cd3 | -8.172 | -43.9984 | 2025-10-15 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 6fc70809-e105-351e-bd6a-f782edb42911 | -8.8539 | -45.2581 | 2025-10-15 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 6d1927c3-0bd3-3933-b1b2-82934607c20a | -5.4278 | -44.2172 | 2025-10-15 14:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 607.8 |
| 3c3404cc-70eb-3294-967f-643ac7f30fb8 | 1.3349 | -50.7253 | 2025-10-15 14:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 81.7 |
| fe59a7d1-5db7-353b-aeab-112a4a27a062 | -5.3921 | -44.0126 | 2025-10-15 14:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| bcd2961d-258b-3f25-b1ca-10292865e0bc | -10.8097 | -43.951 | 2025-10-15 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 150.4 |
| d84ecd97-cd64-3f73-9eed-0c1d666a3ed7 | 1.0766 | -51.0403 | 2025-10-15 14:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 73747e6b-1308-3046-9ce8-7f999aa4348b | -8.2089 | -44.0641 | 2025-10-15 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 63a316e4-8b2d-3816-9932-fbb2edecb8d2 | -9.1532 | -46.8921 | 2025-10-15 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 5a3ee3ed-e840-3bc4-b572-ae4a7804f6bc | -3.8101 | -43.1116 | 2025-10-15 14:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| f4b93a86-1169-3199-92f1-bd5447b6ea4f | -4.1338 | -42.2 | 2025-10-15 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |


