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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0d135de-1d52-3b08-a14e-60a1c4183f26 | -11.8812 | -64.9513 | 2025-09-22 02:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 30.4 |
| ebb1842e-e342-3f72-baeb-ca680c86dc97 | -20.274 | -55.4927 | 2025-09-22 02:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 69ffa20b-4f5d-3673-8f5b-deadacc9108a | -4.3197 | -48.0908 | 2025-09-22 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 4a20bc61-9a48-3542-96bc-476c7ca581b0 | -10.3762 | -46.0562 | 2025-09-22 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| b07b0a33-2899-3b7c-9418-230efde6a844 | -15.9969 | -59.4651 | 2025-09-22 02:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 75fde49b-57e6-3989-aebb-2614d1a1ae07 | -11.8814 | -64.9323 | 2025-09-22 02:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| bb62a16b-d040-37fc-9f50-2175d05e3ee8 | -20.2735 | -55.5141 | 2025-09-22 02:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 3541f12b-9d2a-34f5-bdaa-9199d8f5a243 | -11.8626 | -64.9332 | 2025-09-22 02:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 3092eaa6-429f-3084-bc05-ca0f89005e1a | -22.8326 | -50.5973 | 2025-09-22 02:50:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.5 |
| 15392638-9eba-3fc2-a35d-c773c9b38e41 | -10.3762 | -46.0562 | 2025-09-22 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 176a641f-82f3-39c2-b801-479eb69ca211 | -4.3197 | -48.0908 | 2025-09-22 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d173c0d0-3c44-303e-bd2b-871d6b1a9233 | -22.832 | -50.6203 | 2025-09-22 02:50:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 112.7 |
| cb43ad01-9a0e-369e-bad3-1e978eff6559 | -22.8117 | -50.6021 | 2025-09-22 02:50:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| c795b00d-b1a9-34e7-895c-8da85c1d8428 | -11.8624 | -64.9521 | 2025-09-22 02:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 35.4 |
| dc90f03a-f316-3b4b-9959-107898e7313f | -20.274 | -55.4927 | 2025-09-22 02:50:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f9a041aa-a09d-3db2-b116-d735209636a0 | -14.8067 | -51.4024 | 2025-09-22 02:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6da21020-04e0-3b65-a525-9de28f8ceb2e | -10.3572 | -46.0585 | 2025-09-22 02:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 4be4e66e-09c6-3e0c-844e-ad1a0d2372d5 | -11.8814 | -64.9323 | 2025-09-22 02:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0c9cd16b-7fda-3ee1-aafb-c20dc4a39fdd | -11.8812 | -64.9513 | 2025-09-22 02:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 2aca8fae-6341-3163-9748-7da05dd7591f | -16.0163 | -59.4633 | 2025-09-22 02:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 8bb0a2ce-001a-3df3-aa76-28493844acef | -11.8626 | -64.9332 | 2025-09-22 02:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 2e244438-cb44-3fd7-a0fa-ac35d2ee55a1 | -20.2537 | -55.4959 | 2025-09-22 02:50:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e0ed905d-ce48-33f4-8bd9-a2dd89c014f8 | -15.9969 | -59.4651 | 2025-09-22 02:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 4dd84b6e-c60f-3f41-86fe-058ff7ba6225 | -10.21044 | -36.58376 | 2025-09-22 02:58:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 1cbe9138-4d7c-30fb-b2df-40f04d5484bb | -10.20944 | -36.58876 | 2025-09-22 02:58:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| c90953ec-c12c-37e2-9be2-c8f3c3657c7c | -10.21238 | -36.58257 | 2025-09-22 02:58:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d7f564ae-23b8-3974-81e7-43f73964e744 | -10.20527 | -36.58612 | 2025-09-22 02:58:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 03b1676a-9dce-304f-827c-b249ade27063 | -10.21142 | -36.58753 | 2025-09-22 02:58:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| b9a3a726-c9d5-3cec-95d3-4376ff452ddd | -20.2537 | -55.4959 | 2025-09-22 03:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 13b542b9-a780-3d2b-ac9a-c09724f76cda | -10.3572 | -46.0585 | 2025-09-22 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| be6c3609-3a8a-313c-9614-6d01e3998c06 | -14.8067 | -51.4024 | 2025-09-22 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 6151e193-79c9-3e5a-869d-1f622a193587 | -16.5677 | -50.0885 | 2025-09-22 03:00:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| bc74f0b5-c954-376e-ada2-dc5a1f1319a8 | -11.8814 | -64.9323 | 2025-09-22 03:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| dbf9e5b5-1f7b-3b8e-af5b-387df192916a | -11.8812 | -64.9513 | 2025-09-22 03:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 23b47089-afba-3cc2-9133-311331d66b8f | -20.2533 | -55.5172 | 2025-09-22 03:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4ad9bc51-9eab-34aa-a2b2-dd97100da208 | -20.2735 | -55.5141 | 2025-09-22 03:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 8530ad12-cf56-3ae5-9798-ed434dc85909 | -22.832 | -50.6203 | 2025-09-22 03:00:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| 55791edd-12d6-31f5-9e67-03490435d948 | -16.5672 | -50.1107 | 2025-09-22 03:00:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| abb3a909-62c8-32d5-bcdc-7a8ee42e8ce7 | -11.8624 | -64.9521 | 2025-09-22 03:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 26.2 |
| f764c73d-f2e3-3e23-959f-f3d33d52e047 | -11.8626 | -64.9332 | 2025-09-22 03:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 8968dbc8-7000-3b40-b2c5-03a9fd7c9fba | -20.274 | -55.4927 | 2025-09-22 03:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 68806b88-ca96-308f-a36a-55a06d075cdb | -10.3762 | -46.0562 | 2025-09-22 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 226a0414-6028-3f32-8cce-b471c242603b | -16.0163 | -59.4633 | 2025-09-22 03:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 39e39f5d-9971-300c-8963-1bbfe48bcebe | -15.9591 | -59.3887 | 2025-09-22 03:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7c20a522-887b-3347-aa47-04241cf3644d | -19.57654 | -41.65895 | 2025-09-22 03:02:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bbb4f94b-2d72-3ed1-8e64-53b9b5799ab0 | -19.56949 | -41.65762 | 2025-09-22 03:02:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 050d0ef8-bb9a-37ec-8fa1-0bc653ba30a8 | -20.2533 | -55.5172 | 2025-09-22 03:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 17b5be0f-abbb-3dc5-be77-db45751303e7 | -11.8814 | -64.9323 | 2025-09-22 03:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 04b6ca18-8df8-35e6-a2bd-eea75ba72364 | -20.2537 | -55.4959 | 2025-09-22 03:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 5c407943-049a-3ebf-ac11-7ad8cf7c43a2 | -20.2735 | -55.5141 | 2025-09-22 03:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b4fd0fa8-d430-3cf0-9725-301f60352800 | -11.8626 | -64.9332 | 2025-09-22 03:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 27.3 |
| c8033239-e105-3e4d-a857-6d03ea6a5c2c | -16.548 | -50.0918 | 2025-09-22 03:10:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 149.2 |
| f900cece-46b4-37f8-a0da-17fae2cdbb1d | -20.274 | -55.4927 | 2025-09-22 03:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 103.9 |
| da2ea5ca-b1b5-374c-84ea-5539bee5d079 | -16.5672 | -50.1107 | 2025-09-22 03:10:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 0e60c951-5309-36e1-b2cd-3b60aeb37139 | -22.8326 | -50.5973 | 2025-09-22 03:10:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.6 |
| cb553923-902d-33ff-9a1e-6fafb5ee2589 | -16.0166 | -59.4432 | 2025-09-22 03:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| ded91b00-aa33-3cb2-ad43-107d2cb05f80 | -16.0163 | -59.4633 | 2025-09-22 03:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 131519b4-0ce8-34a5-8e6b-b2306bb0ae2d | -16.5475 | -50.1139 | 2025-09-22 03:10:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 280.8 |
| 1f8c4ae6-2ec8-3db4-bc3d-bcd6ec1d9db3 | -16.5677 | -50.0885 | 2025-09-22 03:10:00 | GOES-19 | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 78c567e9-70a8-301b-af8b-576b47b73b13 | -15.9969 | -59.4651 | 2025-09-22 03:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| f77b32c3-c994-352e-80c2-2185b7407c4d | -11.8814 | -64.9323 | 2025-09-22 03:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 8deef866-838f-399f-b7de-bfc1cf0a2eab | -16.0166 | -59.4432 | 2025-09-22 03:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| f58f9927-7412-3edf-b8f1-ff0663e76185 | -16.0163 | -59.4633 | 2025-09-22 03:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| fb7fd195-f574-3209-8e6e-53e22de7e66c | -20.274 | -55.4927 | 2025-09-22 03:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a647e078-eaeb-3a07-a451-5e60a937a6cf | -11.8626 | -64.9332 | 2025-09-22 03:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 29.1 |
| d9bba86a-5985-39de-9a87-b184be323e9d | -20.2533 | -55.5172 | 2025-09-22 03:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 1c4cf3db-f7a3-36c6-9e75-6475115b0beb | -22.8326 | -50.5973 | 2025-09-22 03:20:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.8 |
| be14d389-28f7-3c53-831a-3607d9a5a6a9 | -11.8812 | -64.9513 | 2025-09-22 03:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 930dde5c-a859-3e3a-b4d5-687eb33b236a | -20.2537 | -55.4959 | 2025-09-22 03:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 98.0 |
| f185a2f8-2eff-334e-9ab8-a6c72ae692d9 | -22.832 | -50.6203 | 2025-09-22 03:20:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.3 |
| 6186d79e-6dd3-3260-a148-a6ab67883625 | -16.0163 | -59.4633 | 2025-09-22 03:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| fc8dadd9-ec32-3fe4-bae9-b7968c62c557 | -20.274 | -55.4927 | 2025-09-22 03:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 83.7 |
| e143f6b6-b0b9-34a1-bab0-e73371938621 | -10.3572 | -46.0585 | 2025-09-22 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 916d10c6-3b36-3433-8cc2-20937a259724 | -15.9969 | -59.4651 | 2025-09-22 03:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fdf6cafa-a32b-370e-a869-847386fe964a | -20.2537 | -55.4959 | 2025-09-22 03:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 51a9e309-2c3b-3f92-9d6b-24e5fc2b51d4 | -11.8814 | -64.9323 | 2025-09-22 03:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 203cb184-11eb-35d3-854f-f633fe5e890a | -11.8626 | -64.9332 | 2025-09-22 03:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 974d15fc-aa5a-3625-9997-3b35c9cd38b1 | -15.1739 | -49.4335 | 2025-09-22 03:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| d5cedee1-fd30-3b9e-9622-0f1b5251f95d | -15.1934 | -49.4304 | 2025-09-22 03:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| fcec606b-6c48-3160-a0c9-b714a0294eec | -15.9594 | -59.3687 | 2025-09-22 03:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| eca8f73b-0ded-3119-9d49-6d3f2738425c | -15.9591 | -59.3887 | 2025-09-22 03:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3df6e10b-c74d-3920-b947-da327e9c04f5 | -15.8412 | -59.5199 | 2025-09-22 03:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 563ab2b5-9bed-3c06-ae65-63c8687a8573 | -15.9969 | -59.4651 | 2025-09-22 03:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 68935f6f-c5dc-3a2e-96a5-5d5889bab97e | -20.2533 | -55.5172 | 2025-09-22 03:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 84.1 |
| c5a7de7e-86be-3396-ba56-a48f9770a8e2 | -15.8412 | -59.5199 | 2025-09-22 03:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f509c27e-b24f-387c-b653-0ae26ac61418 | -15.9594 | -59.3687 | 2025-09-22 03:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 98dcb931-9a93-37d9-ba78-afdf0501d99f | -20.2537 | -55.4959 | 2025-09-22 03:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 9a7b7e18-297e-331b-9546-51bcdab3b0c3 | -20.274 | -55.4927 | 2025-09-22 03:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 6d6a45bb-ca97-32f8-a2e8-4ce0933cb11f | -15.1709 | -49.5882 | 2025-09-22 03:40:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 3a430371-a3e2-395d-88b4-0a2c026afd88 | -15.8414 | -59.4999 | 2025-09-22 03:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 7c0d4f9a-7010-306f-82f0-38a7867365a3 | -20.2735 | -55.5141 | 2025-09-22 03:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 1df804b7-f2f9-3f30-badf-352bdaa95e99 | -15.9591 | -59.3887 | 2025-09-22 03:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 629265e8-c1cd-32e7-91f7-7c5cad549ede | -16.0163 | -59.4633 | 2025-09-22 03:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 6cc7dc18-64d7-3804-b4b5-43e3c14f898d | -6.31734 | -35.06652 | 2025-09-22 03:47:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b307860a-3cb8-3cd3-942d-6d59ae19c56d | -5.56638 | -42.12849 | 2025-09-22 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 168d1d60-93bc-3fe5-9e44-91fc53b02b6a | -5.33226 | -44.1791 | 2025-09-22 03:47:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63692de7-0fe7-3eed-888c-b1da7caa9ac0 | -5.57051 | -42.12915 | 2025-09-22 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 543962b6-a97e-3f94-bf0b-b6d8c8195384 | -6.45349 | -45.67937 | 2025-09-22 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d668c9b-238f-3586-99a6-e951b5479179 | -5.56575 | -42.1322 | 2025-09-22 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b0c1f037-cc5e-37a9-9c6a-90975468669b | -5.1089 | -46.16317 | 2025-09-22 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README9.md)
