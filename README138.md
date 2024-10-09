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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d409efac-c7d4-3e62-b028-dd1661d541dd | -16.85207 | -57.45196 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ee6816f5-9259-3716-a37f-a70b318e2257 | -16.85135 | -57.4559 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 862aad99-bbb3-3449-b56c-e7ca21782d54 | -16.851 | -57.80609 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7df6fa40-7938-36d2-a61b-ec6b9df87162 | -16.84737 | -56.70475 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 04bc3bf3-1caa-3f37-81b3-beefa385b788 | -16.8464 | -56.71008 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fae6d470-de1d-3660-a8b2-2c25715f3aae | -16.84437 | -56.69864 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3ba64f81-ab20-3c7e-8ac4-45c4700dfcc9 | -16.8434 | -56.70397 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 0e789a73-73d2-3927-baf3-0778a4e5cbc7 | -16.84249 | -56.73145 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f213874f-185a-34ad-8ac6-ffb2a8b5eba1 | -16.84151 | -56.73679 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 308d3d04-819f-38ab-80d4-b26844635586 | -16.84053 | -56.74215 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| aa526028-3d39-334d-9148-d8cb1bf28890 | -16.83949 | -56.72533 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3f639d85-f186-3880-a7b3-0bbed316150b | -16.83942 | -56.70319 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 7bba5d1d-70f6-38cc-b7f9-2c1b07dbb6ee | -16.83851 | -56.73066 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9fe26e38-6af5-3202-a58a-25665cffec33 | -16.83753 | -56.736 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b72d8182-94e7-3624-bd3e-62b3b08ec9fb | -16.83655 | -56.74136 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dcf76d01-c761-3173-b6c8-c1182e195b4c | -16.832 | -57.44382 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f8830d13-10e9-3989-9fa8-16db2f999c5a | -16.83127 | -57.44775 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0a521be0-72c6-3ddc-ac8c-51a82249463c | -16.8293 | -57.43512 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d7d1feee-8870-3938-a33f-be9e50c03480 | -16.8266 | -57.42644 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 89115423-bc96-3e13-a0d4-0e8da9588085 | -16.82587 | -57.43036 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 00c6c407-b522-3d02-9234-b8958111c8bf | -16.82515 | -57.43428 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 914f5b2b-2e30-307d-8de3-d4fa75d74a9c | -16.82441 | -57.43821 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 06779283-d7aa-3370-8f92-01243dfeec5a | -16.82318 | -57.42168 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e3749ac5-04e9-312d-9373-6e4fc290f889 | -16.82245 | -57.4256 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 59c50e07-5c5d-300b-9cc8-5f9f82fc3454 | -16.82173 | -57.49903 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6cb89fed-680e-313f-b40e-7986c7367cd5 | -16.82172 | -57.42952 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 4e0789c1-3237-35be-baeb-52060bd9a0a7 | -16.82099 | -57.43344 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 058b3c5c-8cfb-3abc-a7b6-1f318f768015 | -16.81903 | -57.42084 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a92da0f8-e1ea-396b-96ba-c7a8075c4fb3 | -16.8183 | -57.42476 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b8044aeb-bc36-3dab-8848-27ba4787e770 | -16.81756 | -57.49819 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 56a6cb74-92b8-3b19-ad8b-1c8b88d0c7c7 | -16.81414 | -57.42392 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 07e68ee2-bcc1-3b7e-b7c2-e83cc8460fea | -16.80999 | -57.42308 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d68565c0-2f18-3748-8734-c4b2852c7d01 | -16.80462 | -57.40574 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 218c6f28-13eb-3814-805a-9f86979e34b7 | -16.79973 | -57.40881 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5a1eb474-b598-38eb-bffe-b4229c2d4549 | -16.79947 | -57.43316 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 800beaf6-67d9-3570-b023-df012f93f149 | -16.799 | -57.41273 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e64249fa-f6f6-312e-b501-7cac4109538c | -16.79873 | -57.43708 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 1bbc79fb-47e3-3309-a95c-eff4e0144008 | -16.79799 | -57.44101 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d38997e1-46e0-3215-84ad-07c6eb0c4bcc | -16.79604 | -57.4284 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 5766fb2e-33ba-3d46-b204-1610b6054b2b | -16.79531 | -57.43232 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 9da49c61-c184-378f-aafb-5589d28b0741 | -16.79457 | -57.43624 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| f074117d-0485-309d-89db-1c63c64ef159 | -16.7941 | -57.41581 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e17811d7-ec64-32f4-ac1a-7c9e61f68a5f | -16.79383 | -57.44017 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| fc821892-4580-3b07-873c-56d043555f5d | -16.79308 | -57.4441 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 7b0aae5f-4cc2-3b84-b957-9dedd24db1f2 | -16.79115 | -57.43148 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 576a9289-de4f-3b43-9aa0-c1c2dc436625 | -16.78818 | -57.4472 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 704a6969-0de8-33ed-9761-7d8a925f33e1 | -16.78699 | -57.43064 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 89d38183-bd41-30cb-bf68-ddc5138e62e0 | -16.78662 | -57.43095 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| daf702ad-5469-38d7-8446-0cdb4f880ea3 | -16.78104 | -57.46212 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 004f8477-db23-3574-ad69-53e1cf7ecf1b | -16.78089 | -57.46249 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| fdb920b1-452e-3aa6-a4b6-dd4eaac2740b | -16.78029 | -57.46606 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 6daba8f4-8421-323b-b161-c91a43638e47 | -16.78017 | -57.46645 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| bee0074a-07c6-3ebe-9292-dd152944a40f | -16.77911 | -57.44945 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| af0d6650-c0d9-3248-88a1-9bd789afc9cf | -16.77888 | -57.44979 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3a7717a8-c65f-3a1f-bc34-dd7d208a8ffe | -16.7788 | -57.47395 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 30812863-aa30-3c46-ac8d-4f47f80d34b4 | -16.77873 | -57.47437 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ad8c6b35-a733-3d24-a3cf-d1ed5602cff9 | -16.77687 | -57.46127 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2f9b7d44-cfc3-3b57-826f-070e8b741290 | -16.77672 | -57.46164 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c33f4aad-b223-3abb-9686-6dfef84b0088 | -16.77612 | -57.46522 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2d49ccee-7d29-3557-8d39-428fcfc3b548 | -16.776 | -57.4656 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 5f626c05-6bc4-3af0-8e7f-24eae53f0c16 | -16.77495 | -57.4486 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0caaaa04-a3cf-3ae7-af6e-fa884c86b033 | -16.77471 | -57.44894 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 27c4f775-48ee-39fd-9d40-bd4a6a14d15d | -16.77428 | -57.40403 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6a580fae-f466-3223-9296-42041f720ca8 | -16.7742 | -57.45255 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 57eba795-ee8d-3bf7-a527-aab02a9b7abd | -16.7727 | -57.46043 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5cab996c-4eb3-3870-bf93-96ccf00a937c | -16.77262 | -56.69935 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 27b83cab-aafb-3af1-a5ff-9166affe4d8c | -16.77255 | -57.4608 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 66c07096-246d-3b28-b10c-1b1e8521209e | -16.77165 | -56.7047 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 867c05bd-7779-3225-bba8-ad57d03cf54a | -16.76864 | -56.69856 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 749c14aa-26a9-378e-bbb8-ac077f8f054a | -16.76767 | -56.70391 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6d43f212-bdd1-366f-aa20-d56c04f1293b | -16.76466 | -56.69777 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 648653cb-b0d6-321f-8a06-bc8611fe7234 | -16.76175 | -56.71383 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8e25d358-e559-30b5-8406-c0b9ad3ac707 | -16.76165 | -56.69165 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0d464a00-4e08-3a78-85ea-822fd58a8398 | -16.76069 | -56.69698 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2ea25406-dc3c-33dd-b69f-a02fe64ab66b | -16.75777 | -56.71304 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f3110d2b-445d-3946-aa10-18fca8d28ab6 | -16.75282 | -56.71761 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 592c7847-d688-3f76-98cf-f5f6bf85b547 | -16.75175 | -56.70077 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 11ff76c4-ff17-3499-8cea-e9d6194b97ff | -16.75078 | -56.70612 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2a35675f-b22e-32d5-be82-de1001efacf9 | -16.74981 | -56.71146 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4446a0a9-b625-3f8f-af87-d3ae10de2c99 | -16.74874 | -56.69465 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 923b5f35-90da-3cf0-9ea6-4e3b1f5a23a8 | -16.74777 | -56.69999 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 342339ab-b10a-3bdc-a33c-e44aed5119e9 | -16.7468 | -56.70533 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ceb677e5-9be1-3612-9544-0ad52ef9160c | -16.74485 | -56.71603 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e472a794-99fa-3233-bb88-808f52fd128e | -16.74379 | -56.6992 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f43451a9-e165-3fa3-8c9f-1b2e06d69c2f | -16.73981 | -56.69842 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| deb7c3f0-0afa-3e40-a0ad-1caf8ee4e912 | -16.73583 | -56.69763 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d3821e00-e6ec-337c-bc33-e3bf64007bfd | -16.70852 | -55.95618 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 69b4546f-c8ed-33ff-b85b-191454401e2c | -16.7078 | -57.45999 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 7ed33981-6eee-316c-872b-12007f316fb7 | -16.70707 | -57.46394 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 4dd9e104-a9f7-3665-83f5-6b7d772707e6 | -16.70518 | -55.9304 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e1ce2702-65ef-3697-8ed5-ac25fa61a5ef | -16.70478 | -55.91031 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 24c4a042-1184-3cca-bb80-d034ce52a4b9 | -16.70471 | -55.95543 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 69c93f8e-c933-3363-9309-9258bca8e842 | -16.70432 | -55.93526 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7072f619-1879-33ad-bc8f-140212b3ad8c | -16.70385 | -55.96029 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ac693d39-65b9-3e59-be73-1d31ef3df648 | -16.70363 | -57.45914 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e3f45e33-2781-3161-bfbb-e3f4836616ee | -16.70289 | -57.4631 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 265c94be-be5f-32d9-adff-52018e225f0e | -16.70222 | -55.92482 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4e9c4cbc-12a4-3dfe-80a8-95dc63a69416 | -16.70215 | -57.46704 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 0da95b94-ea5b-3ec8-a8d4-f91c33f51346 | -16.70137 | -55.92967 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a3b04d25-48eb-30dc-9ffc-25efdd7a188a | -16.70094 | -57.45039 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |


[Clique aqui para ver as próximas entradas](README139.md)
