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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f94f0179-fcbe-3c35-ae9b-5956ea5ee2b9 | -8.8165 | -46.682 | 2025-10-02 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 3478b9f8-8b91-38de-806d-45e3a16eb191 | -6.7814 | -45.5929 | 2025-10-02 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 41e51112-37b3-39dd-a5ad-28d2065cb3a3 | -9.4083 | -47.5742 | 2025-10-02 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 36255882-62b4-3743-8645-117a1a5f57b3 | -7.7752 | -42.539 | 2025-10-02 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 347.7 |
| 1e25c806-0b17-380b-8987-a1234ff6c026 | -9.8893 | -46.945 | 2025-10-02 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| ce28f453-467c-3889-b779-0840bf0739dd | -12.7669 | -44.9137 | 2025-10-02 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 796a55be-9801-3db3-99af-f1fce9ec808c | -11.2803 | -47.8223 | 2025-10-02 14:00:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| c09dec55-af34-3496-b58e-a88be6e6145c | -7.8692 | -47.3048 | 2025-10-02 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 76ca4102-3079-38c3-9f65-7f4cc41a8702 | -14.7043 | -49.616 | 2025-10-02 14:00:00 | GOES-19 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 286.0 |
| 020f48a4-7d98-3ac8-8c65-03a281861460 | -7.7941 | -42.5369 | 2025-10-02 14:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 223.8 |
| fb495e1b-6eff-3627-8e04-4b797b1839a8 | -8.5204 | -47.8167 | 2025-10-02 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| ecb422ab-53b0-320e-ac37-be5352dab93b | -9.4086 | -47.5521 | 2025-10-02 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 72fa9bbd-4221-39c0-94a4-d93e52cef068 | -5.3382 | -43.7391 | 2025-10-02 14:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 29dd5ce2-a101-33b9-be63-4fcd7845abc8 | -14.2121 | -46.1058 | 2025-10-02 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 107.4 |
| e76bd638-4ba5-3cb6-85ee-20cd9843b097 | -5.7937 | -43.0766 | 2025-10-02 14:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 122.1 |
| 889a4df1-9be8-3782-b63e-263341e1b70f | -14.4947 | -48.4329 | 2025-10-02 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 126d524b-6a64-3019-96f1-1cfe3692bc90 | -12.7627 | -50.5567 | 2025-10-02 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 8cb4180c-4993-3ed1-8da3-e4330932b6d6 | -11.8489 | -48.0151 | 2025-10-02 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| a42e53b8-9fde-3212-84da-266ca957b1ae | -10.2779 | -50.3246 | 2025-10-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 44fff425-833c-3164-be7a-dfb58e0b4e02 | -10.1837 | -50.3128 | 2025-10-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 5e5c9d62-52e9-3a4c-bc07-7f6355da0c3d | -13.7962 | -47.5362 | 2025-10-02 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 88fd8d72-5916-3572-8fbe-c497aad88b6f | -5.4964 | -42.7707 | 2025-10-02 14:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 89a4e435-f648-3a0f-868e-35d40a364785 | -10.1839 | -50.2914 | 2025-10-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| b2386b0c-51be-39ad-a8e7-8f16eb679150 | -12.8195 | -50.5925 | 2025-10-02 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ec732399-eceb-387d-93c4-98b1838de6bf | -14.4757 | -48.4137 | 2025-10-02 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| f1db2384-2963-3618-ac4f-52cb47f421d6 | -11.0225 | -49.8167 | 2025-10-02 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7c82e200-73bd-341c-8fcc-9e50e5ac5c39 | -6.7626 | -45.5944 | 2025-10-02 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 997bb0ee-8b4b-3427-9247-ea7b4e03b008 | -14.3309 | -45.9933 | 2025-10-02 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 126.3 |
| ec49e27f-91a9-3150-93e8-ee9ba89cdbf4 | -6.7816 | -45.5703 | 2025-10-02 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 89880ea4-4798-3e8c-ad49-75978ffe5dd9 | -15.1444 | -48.0143 | 2025-10-02 14:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| fda54272-1b13-3b76-b723-b79bf5b38b16 | -15.2227 | -48.0012 | 2025-10-02 14:00:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5b475fc5-a48a-3922-b5fc-6d482526d69a | -6.2408 | -45.3424 | 2025-10-02 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| ac82ca9e-b344-35bb-ab9f-1dbda559606c | -9.3357 | -45.9532 | 2025-10-02 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 208.6 |
| f64e7322-05f6-31ed-9a42-5bc0d27d506d | -6.2411 | -45.3198 | 2025-10-02 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 58896a72-1a52-3503-82eb-7c8798282309 | -11.4796 | -44.9943 | 2025-10-02 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 265.0 |
| 6ff1a6b6-da06-3025-9949-ebaf232e9111 | -9.9182 | -43.7212 | 2025-10-02 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 278.0 |
| 92358842-e37f-3397-845e-cf4ce9a9630e | -6.4945 | -44.2962 | 2025-10-02 14:00:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 75f1f276-058c-3868-af24-444548179be9 | -15.3067 | -45.0713 | 2025-10-02 14:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 114.6 |
| a4259793-b554-3113-ba45-f1e86ef0a65f | -14.4055 | -46.1414 | 2025-10-02 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 377bc3af-4bfe-3cac-b3bb-c6fed5542487 | -5.3474 | -42.664 | 2025-10-02 14:00:00 | GOES-19 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 8f72071e-adf9-3fa1-bd76-c419000417e6 | -7.5746 | -46.8 | 2025-10-02 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f13d0ed9-3272-3941-abee-8482c57fb6d6 | -12.5001 | -50.2453 | 2025-10-02 14:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 6cdb323d-c0e8-3b60-a44d-d1f25982e0f3 | -5.7035 | -42.6841 | 2025-10-02 14:00:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 54ec8342-f6aa-306d-bf94-2f8f2b48e09d | -10.937 | -46.6618 | 2025-10-02 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| c6574583-f6cc-3d57-87ca-4643e72096c0 | -13.7864 | -48.0524 | 2025-10-02 14:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 2fcd6d3e-928f-3830-b129-f9fd9a152111 | -14.425 | -46.1381 | 2025-10-02 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 62d8f69b-5f3d-3ec8-b512-f97224ddfbff | -11.8349 | -47.7067 | 2025-10-02 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 906dfc7f-2bd6-32f3-b34d-9654fdfa1c5c | -6.6604 | -42.7917 | 2025-10-02 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| a343de70-45f9-31ec-b574-d4d5acd0dc3f | -14.425 | -46.1381 | 2025-10-02 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 426.9 |
| df9cd9f2-b356-33f9-82f5-d22c3606d9e4 | -9.4272 | -47.5722 | 2025-10-02 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 765f6c94-708f-3cc7-9f49-7ec05358b95e | -7.7311 | -46.2289 | 2025-10-02 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| b6c30c4a-e21d-3395-a3d4-65df7e15ec60 | -7.8879 | -47.3031 | 2025-10-02 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 39ab5d06-aa72-3ac0-af27-e30227aad41c | -5.3379 | -43.7855 | 2025-10-02 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| fabb1f37-237c-37d1-8437-8a817aec86e8 | -5.7223 | -42.6826 | 2025-10-02 14:10:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 2eb3c16a-94b9-3aa6-a776-b0e4a8816e2e | -8.672 | -47.7144 | 2025-10-02 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 00bb73ab-291b-39f2-8584-00b42ce18b3d | -8.2105 | -47.0084 | 2025-10-02 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 61fda21f-74e4-3131-b77d-5a84030c83a9 | -13.5841 | -51.8845 | 2025-10-02 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 1a7fb95f-b802-3dac-b293-02d71543387d | -13.7873 | -51.2189 | 2025-10-02 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 0518d6b4-98f9-3900-94b2-84bc3184c789 | -11.6126 | -45.0443 | 2025-10-02 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 143.3 |
| ca6ba568-3471-3e17-a2e6-de169de5f8dc | -14.426 | -46.0919 | 2025-10-02 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 151.7 |
| adcea2ab-681c-36ef-8b92-342609ef3d48 | -10.2025 | -50.3109 | 2025-10-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 49b5dc55-248e-38f8-9e6a-9310a7345e11 | -5.338 | -43.7623 | 2025-10-02 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 184.3 |
| deeff6cb-0b22-3fff-9a6d-8cb51b2041aa | -10.165 | -50.2933 | 2025-10-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| df4ee099-8e98-3b37-a4ce-9476957227f0 | -8.6722 | -47.6924 | 2025-10-02 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 208.4 |
| 118c4778-8413-3190-a6d0-58aa0e9b7fc5 | -14.4255 | -46.115 | 2025-10-02 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 332.1 |
| bc2e5e0f-8d7f-373b-966e-cd0694869299 | -8.2094 | -45.5301 | 2025-10-02 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 0554a459-0f76-3764-bb8f-fc18b58d571e | -18.1782 | -53.3024 | 2025-10-02 14:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 8ad76ad0-4b58-3dba-9afc-ec1188d16f9c | -6.1984 | -43.9055 | 2025-10-02 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 6d5ba6d3-c7c4-3d00-bbb1-4503f84959e2 | -9.4083 | -47.5742 | 2025-10-02 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 9a33e951-8268-3afc-bf98-f5310780c79b | -9.7851 | -46.2851 | 2025-10-02 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 771a8f98-b8de-3add-9bfa-9e3f858e2414 | -9.3389 | -45.7266 | 2025-10-02 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 6e476772-4981-3b31-942d-6d7c34c8e2fc | -5.9858 | -44.589 | 2025-10-02 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| dd2b03d2-5206-3235-83c7-8750f8e0e79e | -6.4945 | -44.2962 | 2025-10-02 14:10:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 7857a1a4-ac30-347f-bbc1-f262d5592546 | -8.5204 | -47.8167 | 2025-10-02 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 4f5b0cda-dab6-3c01-b778-6ac311c82785 | -9.938 | -43.6718 | 2025-10-02 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 99782009-2613-3f72-8508-1dc50661c40a | -6.6976 | -42.8354 | 2025-10-02 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| b6423682-e1c8-30aa-a739-114fb7434daa | -14.5937 | -48.3281 | 2025-10-02 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 5792bb06-9224-3551-b272-4d1f300593e0 | -11.4796 | -44.9943 | 2025-10-02 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 378.3 |
| 70d6fa8d-6d35-3360-9b3c-a889833cb88b | -13.7864 | -48.0524 | 2025-10-02 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| bec3ac70-179c-37ad-a454-e2b52f6ac033 | -8.1513 | -44.1397 | 2025-10-02 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 1aa5f7d4-5b1a-34f4-ab8b-8e3c2a5a2900 | -13.7876 | -51.1974 | 2025-10-02 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| ed65e3e6-bcff-3a51-b7de-be334d0d0bcf | -6.7626 | -45.5944 | 2025-10-02 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4c466d96-a693-3553-930b-8a79dd5b05f6 | -10.2028 | -50.2895 | 2025-10-02 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 217aac6a-b7c1-333e-b227-c6b0fc8608e0 | -6.7816 | -45.5703 | 2025-10-02 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 3f9a8907-1f06-3b57-8b4b-6818d91502a0 | -14.4065 | -46.0953 | 2025-10-02 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 232.3 |
| f0eb7a2c-818d-3f49-8d3a-76d68d3f48e8 | -15.3067 | -45.0713 | 2025-10-02 14:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 164.5 |
| da544262-cf4c-3c8e-8cde-630ad2a19233 | -13.9585 | -48.1376 | 2025-10-02 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 1d7729e2-77e7-3bf0-9098-a975ac07f6ef | -5.6236 | -43.23 | 2025-10-02 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 7d841658-793e-33ee-b760-d789a00b36b7 | -8.6534 | -47.6943 | 2025-10-02 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 27977e51-f195-3611-b878-b49dd6147065 | -9.062 | -46.6565 | 2025-10-02 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 97240668-d209-33e6-a0aa-511b0d7ec5cb | -7.8882 | -47.281 | 2025-10-02 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 59d10042-07dd-38ad-8ca9-21193a7bb336 | -14.3139 | -45.8811 | 2025-10-02 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| abf2d7e0-a205-3a7c-b2a9-7a92e5728a49 | -11.8238 | -45.0132 | 2025-10-02 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 170.4 |
| e58590d9-d5ec-3550-803c-33b63fdada4c | -6.6978 | -42.8118 | 2025-10-02 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| 1a4af25c-3caa-38a3-b52d-a3943a687731 | -6.2408 | -45.3424 | 2025-10-02 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 83973f37-1dbb-368c-9f49-d3ae8ba375f5 | -7.5746 | -46.8 | 2025-10-02 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b7151f4c-f22c-3598-8f34-5026b6deeb53 | -9.9372 | -43.7187 | 2025-10-02 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 191.5 |
| bc4244c3-5302-3f84-8558-a5cf5257c6ff | -9.3199 | -45.7288 | 2025-10-02 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 0502e8e7-fab9-3de8-911f-b70331d4688b | -9.8893 | -46.945 | 2025-10-02 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| fb509bdc-7214-31d8-9ca0-8988b459be0f | -13.3131 | -47.5876 | 2025-10-02 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |


[Clique aqui para ver as próximas entradas](README159.md)
