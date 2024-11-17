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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a360a222-99e6-3063-914c-b62b8d583b49 | -4.5517 | -47.998299 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c61a2c17-af4b-3133-88a7-5cca588cffb3 | -1.7903 | -48.445999 | 2024-11-17 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb45a10-c1a0-39c6-88e7-5a45047bfa92 | -1.8024 | -48.002399 | 2024-11-17 00:28:00 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d663df2c-3161-349a-91ca-e092a80c7156 | -4.8217 | -42.917599 | 2024-11-17 00:28:00 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ad379e2f-e566-3040-811a-f63129b04856 | -3.025 | -54.092899 | 2024-11-17 00:28:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3581e95-6ab9-31ad-8939-578dbdbfe38c | -2.6629 | -46.173401 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e3cd597a-4c90-33c3-9fc0-e1ff04548101 | -3.6555 | -50.598 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ffb3703-b557-3b00-9aaf-43ae85cf0a41 | -4.2984 | -48.062199 | 2024-11-17 00:28:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 893614bc-e981-36f1-a081-723de0c42924 | -12.2674 | -44.992001 | 2024-11-17 00:28:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4aa317c2-8642-3cc9-aee4-9dcdd1a542c2 | -4.7856 | -44.454399 | 2024-11-17 00:28:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91c83790-82ff-3bf7-b06b-d2ed33835b74 | -3.8023 | -46.511299 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c4f3b40-2c07-3ffb-ba9d-ee4f7b05c181 | -1.2526 | -47.085899 | 2024-11-17 00:28:00 | METOP-C | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c846cebf-2bbb-3891-9182-afa888b2d300 | -2.1814 | -48.2635 | 2024-11-17 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8e009c8-622f-317f-b4eb-7234ec2745b2 | -2.3394 | -47.464298 | 2024-11-17 00:28:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aabf5329-01ad-3b67-a49a-8ad77016fde7 | -2.5073 | -46.3946 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8a194bb9-8e38-343a-a238-6406bae08333 | -4.4645 | -42.934601 | 2024-11-17 00:28:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e93dd485-622b-32bc-9bb3-2717e17e0f58 | -8.4428 | -44.2061 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e5551075-d0ed-333e-9cae-729c63120c22 | -2.6219 | -46.039398 | 2024-11-17 00:28:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4259e08f-d545-331b-9cd8-b0696099c3d4 | -2.0978 | -48.394001 | 2024-11-17 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 875daa31-ae31-3c35-a3bb-bc839c8e25d6 | -4.8131 | -44.4846 | 2024-11-17 00:28:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f8b9545-f4ba-358f-8184-107996bbdcbe | -3.1321 | -45.474998 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da3cdca9-5d33-35df-ae18-4b2b4f04e9be | -7.1163 | -46.1278 | 2024-11-17 00:28:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 988a952d-bf6e-399b-a237-58f8490d2ee8 | -3.9815 | -45.850498 | 2024-11-17 00:28:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 166a4f85-d408-391b-9b2f-80ece35dea11 | -4.2939 | -48.0877 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb7a2fd0-791d-363d-9859-e4fa09e2a4c6 | -2.8053 | -46.6605 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a600c675-3879-3019-9142-79a2609d46a4 | -3.2751 | -45.1991 | 2024-11-17 00:28:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 50f0be18-94ff-3051-98e8-70dfda88fea9 | -8.4443 | -44.212898 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9d58a7ce-b2d5-30b4-b758-23647dd66403 | -4.2071 | -48.706902 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f591413-29e4-35ce-adad-c026617fd64b | -2.8575 | -46.6633 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a40d992-6db4-3b8c-bea7-b954cf4e6404 | -3.7844 | -43.917099 | 2024-11-17 00:28:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2589e15c-fcf2-338d-b7db-ac1e93fa6e1e | -2.6076 | -47.555801 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fedfbb7-6d5e-32c4-91d0-d5c639a0bce2 | -2.6302 | -46.030399 | 2024-11-17 00:28:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e1ca578-2dcb-3236-9c31-32394c400fd8 | -2.5814 | -47.576801 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82799281-617a-3669-8d90-b30fd71ef93a | -1.504 | -47.4632 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce598e5f-544a-328c-9507-25c28d72d089 | -11.1221 | -44.564899 | 2024-11-17 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 006ebb23-6352-3408-9cab-b7be72caa6ca | -4.784 | -44.447399 | 2024-11-17 00:28:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11352530-ffc8-305b-820b-888732629232 | -2.4748 | -45.442902 | 2024-11-17 00:28:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86ece3d5-a1aa-3fce-9869-21d7451cfce9 | -9.3906 | -40.314098 | 2024-11-17 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8f7fb45d-48c2-3d28-aea9-14d61d74bf0e | -4.4748 | -48.1138 | 2024-11-17 00:28:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3274130-cfcb-3d89-854b-2fb31111f384 | -1.5008 | -47.404598 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 023bb5db-40fb-3d4a-8f5c-159cdcd87f4a | -3.2019 | -46.681301 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ee16b62b-1719-3aba-b6a0-b2d9e51a3345 | -3.8505 | -46.632099 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5315aa8c-987b-3b0a-8bbd-b0efffd11de2 | -3.0427 | -45.759602 | 2024-11-17 00:28:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3ed5167-53b0-3795-b7b4-0bf90ed184d4 | -3.7827 | -43.909901 | 2024-11-17 00:28:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ac81c57-11ea-3dbe-9907-23a32a39c290 | -6.4891 | -47.507301 | 2024-11-17 00:28:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97872a17-5af9-3e63-b2f7-2a94ee116bc7 | -2.9238 | -45.421299 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 156d1a99-d99e-3aa4-8900-6624980bfddf | -2.1121 | -46.425301 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a88de1ff-5298-3a4c-98fa-6f360ef875f9 | -3.1419 | -45.472801 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28396020-c918-3759-9c2c-c48332ed8b48 | -3.2695 | -45.444199 | 2024-11-17 00:28:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 29d7d4da-2d2e-3663-ba81-cd8849112e5a | -4.1013 | -46.104099 | 2024-11-17 00:28:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a881d29-5645-3185-88e2-4638c6f583a5 | -3.6579 | -50.608501 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a930fe61-0305-39c9-a695-ff5970f06a34 | -3.5189 | -50.263699 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20bc1870-1f2f-300d-acb8-5c4663e18c6a | -3.8942 | -45.9202 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 84fac8f2-ef46-3668-a749-77edd7dd40a9 | -3.4086 | -45.870998 | 2024-11-17 00:28:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4bf6a002-4336-31f2-99f8-347a671f40e5 | -1.9616 | -48.383999 | 2024-11-17 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b950e8af-1f23-31f9-aa2f-ddeac1e051df | -3.126 | -45.8983 | 2024-11-17 00:28:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c56d6b7-8a6a-369e-8d09-b7d70ccbc646 | -0.9422 | -51.7183 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8df38d3d-74a7-369a-b1cb-222ad8f27a2c | -4.1273 | -49.358501 | 2024-11-17 00:28:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ef350dc-23b0-3164-a4c1-e9de7599b479 | -3.1097 | -45.0634 | 2024-11-17 00:28:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 03a47a90-bd7b-3945-9397-ac82d74f8b56 | -3.0685 | -45.467701 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1ba4aed0-02e7-308e-9c95-1638b619e2ee | -3.1725 | -53.245499 | 2024-11-17 00:28:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39b9f1d5-8622-33de-a988-7345efaa9fff | -4.8221 | -47.326401 | 2024-11-17 00:28:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 71dd4d5e-83af-38ab-b79f-30b3079b3ee5 | -3.3225 | -52.7733 | 2024-11-17 00:28:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5ba4b74-3c9a-31e8-a0c0-f07a99cbe6ac | -4.2854 | -46.9128 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 191a85f6-8c11-31ce-adf5-408fc04f749e | -3.0442 | -45.766399 | 2024-11-17 00:28:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2e77f29a-d03a-3dce-ad4f-23b726d2e79c | -2.3871 | -46.184799 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c2070d6d-5d21-3732-b95f-247a590be9f6 | -3.4429 | -49.104401 | 2024-11-17 00:28:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19267c0c-0cf2-370f-b617-35e28c524688 | -4.0294 | -45.4744 | 2024-11-17 00:28:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 93fb0b2b-95d9-3528-b017-cd9f55172e89 | -3.6209 | -43.167099 | 2024-11-17 00:28:00 | METOP-C | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad927c4f-7ef1-30e0-a914-3bef7e11f0e5 | -4.2296 | -41.9291 | 2024-11-17 00:28:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5ea17443-06b9-3a48-856a-ce817c0efeaf | -4.3566 | -45.867199 | 2024-11-17 00:28:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 070a04e4-0a24-391d-b31e-4d2752a00fac | -2.8252 | -45.486401 | 2024-11-17 00:28:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ccc738ed-8187-3693-99b1-b58091acca94 | -2.2686 | -47.922199 | 2024-11-17 00:28:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04f39121-6cca-387a-810e-51553b1175d1 | -3.8365 | -45.983299 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 35e30c8f-be3e-37de-9353-dc9e309ccd06 | -4.4583 | -44.0648 | 2024-11-17 00:28:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d49050f-9af5-3049-abc9-81ca12c81517 | -2.6188 | -48.555801 | 2024-11-17 00:28:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c45a4e68-9932-3314-843a-d4e331c3254e | -5.5287 | -42.939602 | 2024-11-17 00:28:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d67e271a-8824-3238-9413-f10135d0194b | -11.1605 | -45.105202 | 2024-11-17 00:28:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 02bdf83b-578d-35d3-b034-db48d975389c | -2.6768 | -46.82 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cf36157-ca2d-334e-b7ae-240d8b51a8bc | -4.1827 | -46.823799 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 87e3c463-492e-30cd-ad38-ce62138d4f02 | -1.5583 | -47.340099 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d03c94a6-26fc-3836-bff4-a72baf895d06 | -9.8636 | -47.527 | 2024-11-17 00:28:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84dee7a0-a191-308a-a7cc-f91eb369e592 | -2.8249 | -46.656101 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 403bfc22-b32b-3466-bad8-512edf39081b | 0.6193 | -51.7649 | 2024-11-17 00:28:00 | METOP-C | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 429b43f2-fa94-363e-b6fd-557caa424fac | -3.3541 | -46.083801 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c12c6f01-1ba7-3642-b2bc-dcb2187e7bdf | -4.4627 | -42.926899 | 2024-11-17 00:28:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3756d5ea-614b-384c-b703-c74b65c1a3de | -4.0424 | -44.767101 | 2024-11-17 00:28:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 67a3b47d-db1b-3ed7-868b-78bbed675a98 | -3.1732 | -46.600399 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 810a7120-f203-3590-b93a-4cce07ad5e8a | -3.5679 | -50.252998 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95ca0b7a-4281-3007-a9d4-93d4e206f2fb | -3.983 | -45.8573 | 2024-11-17 00:28:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a5cb56d-1de0-3da0-82ff-4f7f41ef2801 | -3.9481 | -46.698502 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16b69a0d-1b7e-338a-8c37-961af1cfef16 | -2.6387 | -46.157398 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 75e9cbd1-b7e5-3664-a649-cf948bcdf1a9 | -3.9383 | -46.700699 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 290deb1a-fd9e-3d7c-9952-0e8ec64b7635 | -0.1066 | -51.613998 | 2024-11-17 00:28:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 582c8734-095d-364d-99dc-b094fb422b74 | -2.9889 | -52.607601 | 2024-11-17 00:28:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dd40fc9-765e-35ca-bb8a-9aa406b5049e | -2.8151 | -46.658298 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deb86d6c-2184-3829-8f9c-0e932cd4633f | -2.6173 | -46.019001 | 2024-11-17 00:28:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e13038aa-0e19-3192-a285-e3e6a1d92165 | -2.679 | -46.198502 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c0e0bef-b0af-3c41-8146-c555f3b541eb | -1.1331 | -51.699902 | 2024-11-17 00:28:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 390883ec-a673-32ad-8280-a27114236a37 | -5.2701 | -44.901901 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
