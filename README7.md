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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84846eab-a64d-38d3-8972-a9f5e9763752 | -3.2768 | -53.8199 | 2026-10-03 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 119d0848-9ea0-3e60-bba7-fc83d0f75e97 | -11.0067 | -59.1381 | 2026-10-03 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e2a6b3ef-c8c2-3a2b-a9e4-77ed97961bf3 | -10.9879 | -59.1393 | 2026-10-03 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| fa13fdae-b977-3d80-a7c0-615165386790 | -3.7137 | -50.6674 | 2026-10-03 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 67092835-13e4-38f3-89fc-d7e7a4850d03 | -3.1483 | -53.7426 | 2026-10-03 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| fd475a11-34be-35da-aaa7-e0de4b96b3be | -11.7187 | -43.4148 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1ec3d13c-d2ba-3187-8277-73a1a83793ef | -11.7935 | -43.5215 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 186dca1b-2046-3594-8d34-eb5562cdde08 | -11.4507 | -43.3854 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 21cb6b64-fb14-32fa-84eb-959e4963bb1c | -2.9042 | -45.3944 | 2026-10-03 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 1b39a181-2180-33d5-93d5-5d3679dc0248 | -2.9082 | -54.0907 | 2026-10-03 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 0695358e-f3cb-36be-90fd-c4449677fa6d | -3.2952 | -53.8194 | 2026-10-03 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 160b603b-1157-3813-9312-65dd6646b99e | -6.9295 | -49.6325 | 2026-10-03 00:40:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| f77025d1-182d-38ad-aa20-fbd4bc500c1e | -2.9041 | -45.4168 | 2026-10-03 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 103.7 |
| ebe96b04-b316-373e-8265-eae9b2509a0c | -11.4887 | -43.4032 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 1fcc9170-c0c0-34ba-9a15-815afee447c7 | 1.8037 | -55.5854 | 2026-10-03 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| cad75d21-88bb-3c93-aade-7dada75c7fbd | -3.2951 | -53.8395 | 2026-10-03 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c678ebf2-46bd-3e81-82f4-e722bf5f5c25 | -1.2107 | -47.7735 | 2026-10-03 00:40:00 | GOES-19 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b33ec97a-405e-3459-b5e3-fbf34d9b5e23 | -9.6637 | -40.5819 | 2026-10-03 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 39.9 |
| 0a751dcc-02e6-36ee-8b94-906229f391a6 | -6.7401 | -44.1371 | 2026-10-03 00:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 9374ab98-3e56-380e-822d-f2ad440768e4 | -5.6134 | -44.3876 | 2026-10-03 00:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e73ec86b-a503-3638-a0a3-2c6909e8b19e | -3.1299 | -53.7431 | 2026-10-03 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 207.6 |
| d93a6f8d-d6ab-3a6f-8b0c-6f9f71f74d82 | -13.5365 | -44.1044 | 2026-10-03 00:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| a083e48e-b447-3a2e-b5b2-1839775307ba | 1.7854 | -55.5856 | 2026-10-03 00:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 50954360-2794-3cbe-9b85-41e24f3bb909 | -12.8676 | -44.6878 | 2026-10-03 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 9ec77150-58aa-398e-ab87-b863cae6ace0 | -2.9265 | -54.1104 | 2026-10-03 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 7a09f676-9f06-3d69-a11c-0d43ca33f787 | -2.8856 | -45.395 | 2026-10-03 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 414b2cb9-fda7-3112-8947-5a1c4cdc6a98 | -10.9881 | -59.1197 | 2026-10-03 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 4a42adfc-ddc3-3386-b74e-e48c8fc435b2 | -3.4093 | -52.8436 | 2026-10-03 00:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| d97fe963-731b-3516-8464-bb5e6aa57eb8 | -3.2767 | -53.84 | 2026-10-03 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 7fe59d18-7e13-36aa-9dfe-52b85d41af73 | -11.8123 | -43.5422 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| d90611d9-14cb-3251-9efa-62f3a6f57372 | -11.4695 | -43.4062 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| a1daf2c0-8496-32ca-ab94-50c1904cdbc7 | -5.7376 | -45.1533 | 2026-10-03 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 655847d4-a7b5-3f7d-8365-30f76efb5dab | -2.8897 | -54.1313 | 2026-10-03 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 136db095-5c07-3001-8075-ade3fdaa6b58 | -5.9569 | -43.67 | 2026-10-03 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 5d0314e5-8c3c-3662-bb6c-56474cef3985 | -5.7563 | -45.152 | 2026-10-03 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 5cd42037-9cb5-3b70-a10f-d72036afb3e0 | -5.9384 | -43.6482 | 2026-10-03 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 0c6ba417-e3d2-376f-8327-34cdeae68759 | -11.8127 | -43.5184 | 2026-10-03 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 71866f48-7118-36f0-ba41-bcae09d1a599 | -5.9571 | -43.6467 | 2026-10-03 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 3bdde6f5-b4ae-3cc3-963d-dade44b2b45d | -4.4507 | -47.9112 | 2026-10-03 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9f988281-7e58-3d9b-9f8e-fd2ebcf10285 | -11.7169 | -43.5098 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 9fcbb761-57da-3ffe-b140-ed0c2ddb4578 | -11.7174 | -43.4861 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| d124277e-682c-3307-83a9-98b98c62db2a | -11.6391 | -43.5692 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 02fe888f-6bd1-3f26-8b87-a7c496002dbd | -2.8898 | -54.1112 | 2026-10-03 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 622915cd-34ad-3ca8-a0ec-244f5f5b6d03 | -3.2952 | -53.8194 | 2026-10-03 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 68f650ca-90fd-3e8c-86eb-da95cfee15ba | -5.6134 | -44.3876 | 2026-10-03 00:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| fa03be26-2c9c-3235-bfa9-752a42e0f4bc | -2.8856 | -45.395 | 2026-10-03 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| f1a35a35-0988-3894-b653-34540f7f2861 | -2.8897 | -54.1313 | 2026-10-03 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 35094910-d612-3176-8605-eabef1f29f6b | -11.4315 | -43.3884 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 07c8fdfe-aee6-3fc4-911b-016ec217dfb4 | -11.4695 | -43.4062 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| fb276dd6-f690-34ab-b498-56c3fbcba29c | 1.7854 | -55.6054 | 2026-10-03 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2c59b0ec-b679-3910-b0dd-8f4a78f0ca2f | -4.7434 | -43.2679 | 2026-10-03 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 7f1b3fb1-3891-3290-ba39-c55bd406a0df | -2.8897 | -54.1514 | 2026-10-03 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| ee2d5db7-6828-3c3d-8010-11fb4107c124 | -9.6637 | -40.5819 | 2026-10-03 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 06934e4a-4cd7-30d4-b706-908af9c74906 | -4.4506 | -47.9329 | 2026-10-03 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 6d7fb4cd-a530-3b7c-ae37-f92fe6d53878 | -11.8123 | -43.5422 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| ad7667e1-38e2-3e6e-80b2-09958a5c01a2 | -11.793 | -43.5452 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 004d7262-d926-3df5-8caf-875e51e87c3d | -3.1839 | -54.0839 | 2026-10-03 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6acd8730-04ae-3c8e-84c1-e5cb42849a0d | -5.7355 | -43.2916 | 2026-10-03 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| d6e15565-5e7a-3dff-8404-abf33aa303f4 | 1.8037 | -55.5854 | 2026-10-03 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| c956a6e0-fe4a-3ec0-90ea-8ce31f4f8379 | -5.9569 | -43.67 | 2026-10-03 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 928ff4a0-f8f2-3d49-960b-0c0b8330923e | -4.5706 | -46.5907 | 2026-10-03 00:50:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 43.2 |
| c56e2138-abd9-38fa-ae51-616aa6d2c8c6 | -2.9266 | -54.0903 | 2026-10-03 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 7db171ce-2009-3bb2-9388-6df9dbf6dc4d | -2.9042 | -45.3944 | 2026-10-03 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| dc7d4a02-db7b-37a8-82be-1cdcd09482fa | -11.7187 | -43.4148 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 5f902360-dd16-3e1d-8cb1-2a8a0a3f435c | -3.0192 | -53.887 | 2026-10-03 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 6c12ba1d-161b-3006-b63a-1c7306cd398d | -2.9265 | -54.1104 | 2026-10-03 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 36b1d785-4602-33dc-a0b4-ac44ebcc1c05 | -5.7357 | -43.2682 | 2026-10-03 00:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 05bc873a-a081-3552-8af4-29df2e9f1329 | -6.7401 | -44.1371 | 2026-10-03 00:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9803d65f-0ce8-38bd-8e51-fe17bd6800ec | -3.2768 | -53.8199 | 2026-10-03 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8507371d-1d35-36ba-a7fe-cc1d8982a07c | -3.4093 | -52.8233 | 2026-10-03 00:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 8d1c856f-a053-339d-ae42-1cade4bc4292 | -2.9082 | -54.0907 | 2026-10-03 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 1188c222-e17b-33c7-b362-485d8f284afc | -5.7376 | -45.1533 | 2026-10-03 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| d11d0f98-bf8f-3f59-bc14-ab10bd57d06d | -2.8855 | -45.4175 | 2026-10-03 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 0f67f121-1745-3328-a5d7-1a31fcd5a0ab | -6.8394 | -59.2836 | 2026-10-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 17ed09e0-20cf-3e96-9180-94b5ef920816 | -5.9571 | -43.6467 | 2026-10-03 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 85300550-4c9e-3658-9a31-77369c41ad78 | 1.7854 | -55.5856 | 2026-10-03 00:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 3fbcb28a-b775-3939-9f7c-dfefbc8efd0c | -5.6136 | -44.3647 | 2026-10-03 00:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 185f6fc5-8708-340e-83ed-58ae94a95a58 | -6.8579 | -59.2829 | 2026-10-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 38d92316-a6ba-3f0c-8079-104b7a03077d | -11.4887 | -43.4032 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| f123e044-4b38-369c-9b47-88308f4f111c | -5.9384 | -43.6482 | 2026-10-03 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 42d9b277-8f5f-3854-b80e-ff8f07fd5314 | -3.2767 | -53.84 | 2026-10-03 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e6bba843-f8b7-365f-b357-8a8e3564fef3 | -11.4507 | -43.3854 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 007363a3-038e-335b-8818-353da4f65838 | -11.4123 | -43.3913 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 64de7b03-fde8-318d-93b2-7349a18bdbcd | -12.9592 | -41.1904 | 2026-10-03 00:50:00 | GOES-19 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 72.1 |
| cdd8e42a-db85-3594-ae1d-278110348706 | -5.9381 | -43.6714 | 2026-10-03 00:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 85733541-2ba2-361a-bdae-3064974960b3 | -2.9041 | -45.4168 | 2026-10-03 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| f7519472-27dc-3aaf-9910-16d2d4057e4d | -10.9881 | -59.1197 | 2026-10-03 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 9a263022-7e61-339a-a6b0-1d03618bbce0 | -3.2951 | -53.8395 | 2026-10-03 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6553c1e6-4582-34d6-a442-4e8b4c5d59c4 | -6.8393 | -59.3029 | 2026-10-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| fe01710f-7a5c-3149-ae38-11c377d47a49 | -13.5365 | -44.1044 | 2026-10-03 00:50:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 15155320-04c0-3c28-84d5-37a64ccf3243 | -11.7935 | -43.5215 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| c53d8b01-e23d-38c9-9a14-960ef86d9255 | -11.8127 | -43.5184 | 2026-10-03 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ffd7d29a-d450-3670-82f1-8b6c9023ef5a | -10.9879 | -59.1393 | 2026-10-03 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 135.6 |
| b1874717-b860-3387-88cc-d2d77aa9feaf | -6.8578 | -59.3022 | 2026-10-03 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 41908a39-814d-3a10-b0b1-037ba5ccce16 | -0.9123 | -47.901001 | 2026-10-03 00:52:00 | METOP-C | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15f6e60a-493b-3603-afc7-a4c2c57875b1 | -3.1138 | -50.2766 | 2026-10-03 00:52:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c519802-dbae-34f8-812b-b755e2f4308b | -6.0784 | -53.300999 | 2026-10-03 00:52:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 728e34aa-b00d-38d0-a99a-b5f0858100e2 | -3.1897 | -54.099998 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 553d0f1c-7f07-3156-b354-8d0fa1d61eb0 | -6.74 | -44.1437 | 2026-10-03 00:52:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 235615a3-2a66-3f38-b5f5-00a4e99bae90 | -5.7338 | -43.2784 | 2026-10-03 00:52:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
