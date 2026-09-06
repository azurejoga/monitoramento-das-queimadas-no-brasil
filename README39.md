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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30a933e8-3d0b-31d2-9777-8a4bb17e71b3 | -3.4268 | -58.3298 | 2026-09-06 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 32b50cf8-e999-3798-97d8-3f62372ef7d4 | -3.1462 | -60.6317 | 2026-09-06 15:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 42f341fc-901c-3cea-bd6c-1f487b919f95 | -5.2715 | -60.1255 | 2026-09-06 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3a915691-a71f-383a-84cf-0e83fd811938 | -6.641 | -58.4987 | 2026-09-06 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0fc52d34-3b62-3ed5-99fb-1bfcfeaaadfe | -3.4003 | -61.3087 | 2026-09-06 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| beb09419-9ace-3436-a870-0dc876787b88 | -3.387 | -59.4266 | 2026-09-06 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 8155beee-876f-379d-af00-4acc02f04b03 | -3.4002 | -61.3276 | 2026-09-06 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 5b5b9a7c-dd7c-3175-8613-cb05d2ba4320 | -3.128 | -60.632 | 2026-09-06 15:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 14e7ec04-7082-3f32-84f7-7eef19d085ab | -3.3871 | -59.4075 | 2026-09-06 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 5728d21d-2f23-3753-b3f9-0b91690de226 | -1.4752 | -54.8157 | 2026-09-06 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| fae174be-62f0-3ef0-b976-c0081f6c7985 | -2.458 | -57.9226 | 2026-09-06 15:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 5a0a3ead-84cf-39ca-b0d6-310724653e8e | -3.4269 | -58.3104 | 2026-09-06 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 1e24f815-c603-3c64-9585-ca0ea50f3c60 | -3.7645 | -61.7548 | 2026-09-06 15:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 1a24e467-8912-37d8-896c-42a9283d28f6 | -5.5098 | -60.1947 | 2026-09-06 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a1af7142-31fe-35b4-ad75-acc751e723f6 | -2.9521 | -57.8946 | 2026-09-06 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ee34818e-b7de-3a99-98b5-a06d79272245 | -7.6079 | -57.616 | 2026-09-06 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 9e34c6fa-0667-31d6-bf0d-bec8bc84cd22 | -2.9338 | -57.8949 | 2026-09-06 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 77f9cd68-6b2f-3066-86b7-55f3e514252f | -5.6382 | -60.2289 | 2026-09-06 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 60cf6fdf-a60e-3374-921e-2314f52b2da4 | -5.4917 | -60.138 | 2026-09-06 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a1baa0ad-794a-3574-83f1-d5c39e34172c | -3.3688 | -59.4079 | 2026-09-06 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 1ab3d8ec-c526-323a-8cbd-8c595b8ea09f | -3.3687 | -59.427 | 2026-09-06 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6ea4d732-c82b-3970-84d4-d38042f740ff | -3.4003 | -61.3087 | 2026-09-06 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 54093e13-5132-36c7-b594-8032f77a14c5 | -3.382 | -61.3279 | 2026-09-06 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fb3f4a5e-c295-3bd0-98e8-3717dbee7eee | -3.8575 | -61.1867 | 2026-09-06 15:50:00 | GOES-19 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 6dc3f72e-a23b-3cea-9ea2-27d6ab12da6b | -5.6382 | -60.2289 | 2026-09-06 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 15cba278-8e05-3e30-827c-aa22c1e519cf | -3.128 | -60.632 | 2026-09-06 15:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 12558104-36bc-353f-bc2c-319fefcf6609 | -3.3687 | -59.427 | 2026-09-06 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| ee20e352-b03f-3840-9b3b-abce4ab80e11 | -6.6515 | -59.9258 | 2026-09-06 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 502bf8ca-39a4-35e6-b7c4-adf2029426b3 | -5.9635 | -57.6899 | 2026-09-06 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| dab6dca9-84b0-3b93-a08a-d7c810ad5cab | -5.9819 | -57.6892 | 2026-09-06 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d39263fb-aedf-3607-a59b-7a1474c553a3 | -3.4269 | -58.3104 | 2026-09-06 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 115.1 |
| ef5aad9c-9344-3454-89dc-7e896fd536c2 | -3.4185 | -61.3273 | 2026-09-06 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 78cb662c-5ee8-36f6-a455-9fe80b70b361 | -10.0542 | -50.1123 | 2026-09-06 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| e1474632-7a4e-3f10-9c46-2894080b1029 | -4.6669 | -55.635 | 2026-09-06 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 3fd9fba1-273e-3395-8686-35e38f5cb7d6 | -2.9338 | -57.8949 | 2026-09-06 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 4eb03519-29da-359e-95eb-ea7bd67661ee | -6.6699 | -59.9251 | 2026-09-06 15:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 5c8378e7-3eaf-387c-b632-6317b6ebdfda | -2.9521 | -57.8946 | 2026-09-06 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 23b93246-936b-34d7-a66d-270eb510d153 | -4.4671 | -55.0855 | 2026-09-06 15:50:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 51592598-fe7e-310f-ae29-1aec0341560e | -5.3277 | -56.0263 | 2026-09-06 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f62c9913-8cb2-35ab-a2d3-f529b835fade | -3.3871 | -59.4075 | 2026-09-06 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 108.8 |
| e26a0bae-cde9-3e89-a075-779fa5d2b520 | -3.1462 | -60.6317 | 2026-09-06 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a14e6e73-398d-3387-a95f-d9cff2d3da6d | -5.2715 | -60.1255 | 2026-09-06 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 877c71b7-8a53-3d91-ba55-d4bbf3c495fb | 1.4453 | -50.7446 | 2026-09-06 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1a19fd34-fa02-397e-bc28-60e51e8adb52 | -3.3688 | -59.4079 | 2026-09-06 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| cb7ec75b-3a2b-312a-b26f-aef4be970feb | -6.0188 | -57.6877 | 2026-09-06 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| cb01b531-7b10-3af1-a2f3-ed2ceb4ada29 | -3.387 | -59.4266 | 2026-09-06 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 765b9db8-33dc-3890-9913-3fa445894cc4 | -5.4917 | -60.138 | 2026-09-06 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 02091b5b-e765-3605-835b-357a86298355 | -5.565 | -60.1739 | 2026-09-06 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 6c18ea26-a37b-34f2-9184-f787b43de9cb | -5.5647 | -60.2312 | 2026-09-06 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 35de5f65-e437-3265-8007-833450a25afd | -5.6566 | -60.2284 | 2026-09-06 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 79a22fd8-dc26-34f4-b320-860b921815b5 | -6.641 | -58.4987 | 2026-09-06 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| afa27690-faa4-341a-a4fe-0af1c759ded8 | -8.4863 | -54.6417 | 2026-09-06 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| b30d1067-ed0b-337b-93db-20000c3bd846 | -5.6014 | -60.2492 | 2026-09-06 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f6453e87-9782-36fd-b40b-63055609f126 | -3.3871 | -59.4075 | 2026-09-06 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 115.2 |
| cee86414-4e3b-39bd-8790-bb003b82cccd | -2.9338 | -57.8949 | 2026-09-06 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 10529af1-1dee-3a21-acc8-8dab51df6171 | -3.382 | -61.3279 | 2026-09-06 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| daf2d0da-23d1-33f6-ae5a-a09b56b56716 | -5.9819 | -57.6892 | 2026-09-06 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 7ea10566-c377-30fa-ae02-0bddaf8d9116 | -3.1462 | -60.6506 | 2026-09-06 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 8e7e14fa-6e81-3ec1-a2c6-e2108661c23a | -5.6015 | -60.2301 | 2026-09-06 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 17223ecd-3634-31c9-bb81-db6b222cffb4 | -3.3687 | -59.427 | 2026-09-06 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ba86375c-b4e0-332b-973c-c8eeb9a440dc | -3.3688 | -59.4079 | 2026-09-06 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| f3db5df9-1937-37a2-8701-cf5a545bfa77 | -3.1462 | -60.6317 | 2026-09-06 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| b58a647b-1a45-3e03-845c-1df168c73b55 | -5.5651 | -60.1548 | 2026-09-06 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| f98e21c7-abdd-33f9-934d-14aec8517353 | -3.8404 | -60.7704 | 2026-09-06 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f98429a5-935d-3b20-a24d-392ef3b55e60 | -2.9521 | -57.8946 | 2026-09-06 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| be643d8e-5dbe-35f3-8026-aff68b1dc8a9 | -9.2098 | -70.8527 | 2026-09-06 16:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 8784cc0a-3e6f-3413-8df9-2211767e0b93 | -3.4002 | -61.3276 | 2026-09-06 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d086ea65-c1bc-3b85-9bfd-17af6d1f19ca | -3.8575 | -61.1867 | 2026-09-06 16:00:00 | GOES-19 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 749425ea-c51e-3768-9c74-831fa819c574 | -3.128 | -60.632 | 2026-09-06 16:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| f1e2839f-eab7-306b-b040-e3c9eda448e1 | -3.387 | -59.4266 | 2026-09-06 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| c9e43f7e-0d04-3772-b7cf-2395a62c491c | -3.4269 | -58.3104 | 2026-09-06 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 8c0b7f88-d910-38e7-bf2e-a7ea25bb9bdc | -5.9635 | -57.6899 | 2026-09-06 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 10220d85-62ea-362a-8ca0-1da4857259ef | -3.7828 | -61.7545 | 2026-09-06 16:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 83b56408-cb6e-3334-b187-730c18cfe744 | -3.382 | -61.309 | 2026-09-06 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d5b5e8e7-bdae-393e-b043-c26c81fd01fe | -3.4003 | -61.3087 | 2026-09-06 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| b068a1ae-1963-3d19-8c99-e4afedeb8950 | -6.6699 | -59.9251 | 2026-09-06 16:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| d3182de9-27e4-38e2-b391-6d37d979ff8c | -5.6566 | -60.2284 | 2026-09-06 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 7cf4ae80-2d58-326b-b936-031a5e3fc6c5 | -3.6216 | -60.547 | 2026-09-06 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| c45117dd-9216-3da8-b19a-e55204b4415d | -6.0188 | -57.6877 | 2026-09-06 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 38ab841c-bbef-3c49-99d9-fdd97c469ead | -3.4392 | -60.3985 | 2026-09-06 16:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 2defa003-93c1-3c13-bd57-41a20ba874dc | -6.7676 | -58.939 | 2026-09-06 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 6ec9caaa-d77c-3102-90b6-8c69c40e9e0f | -5.565 | -60.1739 | 2026-09-06 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 66a545c1-2d99-3b63-b4df-0065fb125f07 | -6.1362 | -59.8871 | 2026-09-06 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 61bf0ad7-2a26-354f-aa8d-796f5955d534 | -3.9363 | -59.3381 | 2026-09-06 16:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d85e557a-e3be-36be-bc24-a9866bc94682 | -6.136 | -59.9254 | 2026-09-06 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 09caed95-e370-3b1c-a18d-b8d3ab9d4621 | -3.1279 | -60.6509 | 2026-09-06 16:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 83c6bf22-e796-3a8e-8d3e-258351971c9b | -3.4185 | -61.3273 | 2026-09-06 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 2a66a4d6-cbd8-3415-9a18-2132be97aa3e | -6.1361 | -59.9063 | 2026-09-06 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 5dddc95a-6555-3c2b-ab6a-2e8724d03cf1 | -1.4935 | -54.8155 | 2026-09-06 16:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 94c1433c-b27c-38a3-a194-cf8278b6bd75 | -3.128 | -60.632 | 2026-09-06 16:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 188fda93-e90e-3f55-a689-86853ca657df | -3.382 | -61.309 | 2026-09-06 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| e5e4d298-9655-34cd-b31f-ef85427161e0 | -5.9635 | -57.6899 | 2026-09-06 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| dacb6c29-8a08-3b31-bd13-99d92d14b4d1 | -1.3932 | -49.0174 | 2026-09-06 16:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1751f597-1708-3760-b97a-a51fc3269bfe | -6.0188 | -57.6877 | 2026-09-06 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 99a78296-c88a-34a3-aff0-a7d92e0fb841 | -3.1266 | -61.2188 | 2026-09-06 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| e5c4830f-0e20-3bfd-aef4-2967dda860d3 | -5.9819 | -57.6892 | 2026-09-06 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| c5772e03-584e-385c-bf21-483b6321590a | -3.8404 | -60.7704 | 2026-09-06 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 01cfcf82-7dd0-3f82-a489-a62ffe376fb9 | -3.6216 | -60.547 | 2026-09-06 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 98ff9967-8627-3cbd-8846-22ff90dcbc73 | -9.6848 | -48.0728 | 2026-09-06 16:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 11990f80-47f8-3bd0-be37-71aba4fc387e | -3.7886 | -59.7243 | 2026-09-06 16:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |


[Clique aqui para ver as próximas entradas](README40.md)
