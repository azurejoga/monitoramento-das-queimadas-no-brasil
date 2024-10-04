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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fcf0bca-0c76-3c4d-9520-262141ef4533 | -17.1574 | -57.3993 | 2024-10-04 03:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 96eaefb4-32a1-35df-b688-b9f54d911c55 | -17.1577 | -57.3787 | 2024-10-04 03:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| dd4f7c73-212f-32e3-99e9-1d25736233f3 | -17.1771 | -57.3969 | 2024-10-04 03:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| c4040c59-78dd-352c-8d8c-442e962896a8 | -17.7508 | -43.8079 | 2024-10-04 03:16:44 | GOES-16 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 2201a298-115e-361e-b43c-a7cc1ea38995 | -18.8613 | -43.5837 | 2024-10-04 03:16:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.3 |
| 818adbbb-aeba-37d8-acd6-0e6a25600d3b | -18.9081 | -42.0315 | 2024-10-04 03:16:50 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.1 |
| 78da9c4d-3f69-33e7-b865-91c0fb66c5a5 | -19.0344 | -43.1944 | 2024-10-04 03:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.6 |
| 407d6b53-fd97-3e79-b314-98eb27d2aa1f | -19.3159 | -42.5976 | 2024-10-04 03:16:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 127.4 |
| fdbc55b1-ea51-30a4-9962-cbac444804e3 | -19.3167 | -42.5724 | 2024-10-04 03:16:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.7 |
| e80b43cc-a485-3347-babe-bb8b2a97ba39 | -19.3363 | -42.592 | 2024-10-04 03:16:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.2 |
| 7c1e56a3-ecf8-356d-90fd-6a5ff859ed94 | -19.5104 | -42.8691 | 2024-10-04 03:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| a667e166-c0a6-39b6-9ce7-8ac8b8e0556b | -19.8516 | -42.3738 | 2024-10-04 03:16:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 140.5 |
| 4c46a025-3a69-3af7-85ad-1a205e5c2655 | -19.8524 | -42.3484 | 2024-10-04 03:16:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| 69b48bc2-731c-3900-bf95-a893108b1631 | -20.121 | -43.5219 | 2024-10-04 03:16:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.9 |
| eb10ca92-934c-3bf9-9955-520a2319e9dc | -20.1416 | -43.5162 | 2024-10-04 03:16:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |
| 5c750eb1-da4c-3efd-86fd-1a8fe5697025 | -19.01398 | -43.18106 | 2024-10-04 03:17:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 012c53af-11f7-3945-b3b9-a683ccc0bae0 | -19.01285 | -43.18616 | 2024-10-04 03:17:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| eb63f825-7f47-3bb5-b917-f350e0932433 | -18.9742 | -43.20605 | 2024-10-04 03:17:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 217d08f0-528c-369b-8225-a03d46d38dab | -18.97317 | -43.21077 | 2024-10-04 03:17:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d9fdbd93-7dfe-3f9d-8d80-254004349795 | -18.97159 | -43.20407 | 2024-10-04 03:17:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 68795445-804b-33d3-bcc1-22adbb82ca28 | -18.97112 | -43.2202 | 2024-10-04 03:17:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 038abaf4-5f37-3c32-a874-4f646f9709fe | -18.97051 | -43.20885 | 2024-10-04 03:17:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0291f310-f041-3590-a264-be6c8b7c0e84 | -19.4322 | -43.06974 | 2024-10-04 03:17:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d330af61-c0a9-398f-a4b6-6a14e7b202d5 | -19.43135 | -43.06862 | 2024-10-04 03:17:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 14fb4292-7b33-3ff7-80e5-8693746596e7 | -19.32304 | -42.59772 | 2024-10-04 03:17:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.8 |
| 5901413d-67e6-3254-9e24-24e03bcf220c | -19.32214 | -42.60193 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 03ae2d75-c146-33d6-a9c1-94ce071cf92e | -19.32119 | -42.60635 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| ed0f46ca-5455-31cd-9d6c-5f975b938c93 | -19.32012 | -42.59247 | 2024-10-04 03:17:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| 0a9f6b09-7e77-352e-a753-7f341896afee | -19.31929 | -42.59619 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| e9891888-7e9a-329f-9144-7adf02153e75 | -19.31833 | -42.60052 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| cd1e334a-c551-3614-8497-d98ce96d668a | -19.31826 | -42.59233 | 2024-10-04 03:17:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.8 |
| 04f4aee6-6f9e-3541-b2ec-125afea77a83 | -19.31744 | -42.59612 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.8 |
| 037b4e1c-3e6f-3849-8335-91e7f3f80d08 | -19.31731 | -42.6051 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 570ff14d-7ca7-3999-99ac-bca68936f864 | -19.31649 | -42.60054 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| e705d569-d081-3791-8099-6bd43ba0eb2d | -19.3155 | -42.60519 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| c0ba0a49-2f53-34fb-b018-9d0a120c4012 | -19.31452 | -42.59089 | 2024-10-04 03:17:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 0a7a18cf-d40e-3978-9167-35190142a414 | -19.31366 | -42.59474 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| d321443d-4c8c-39ad-b351-dfb8c686b3ec | -19.31268 | -42.59916 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 8236e5f8-3e95-30af-b4e7-edc0d07d9a5d | -19.31265 | -42.59075 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 77ac7deb-74c7-3e97-b848-c0e95b8d6af7 | -19.3118 | -42.59474 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| a05224b5-d680-3cd6-bb34-25a5505c92b7 | -19.30883 | -42.58973 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 39969c28-6d85-36cb-8e45-b4b5939bbeed | -19.30793 | -42.59374 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 80472f63-963a-3fea-aebd-0b83af4481c4 | -19.30692 | -42.58979 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 9b5c626d-c315-3ed2-a368-6e3fe87f7263 | -19.30605 | -42.59381 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 29871450-4157-364c-bd26-0cbb69913a88 | -19.30541 | -42.57839 | 2024-10-04 03:17:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a4394217-7f08-3282-a27a-5d0f253105d9 | -19.3034 | -42.57862 | 2024-10-04 03:17:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c1483489-944f-35b3-974b-bcc59592e1a6 | -19.30303 | -42.58905 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e66a75a3-fedb-3bdf-b0c9-49b6bbdf4694 | -19.30215 | -42.59298 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5575350b-7828-3d39-8c22-e64dc73cfc28 | -19.30108 | -42.58932 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4ee3e859-6017-33f2-9d2e-ffe556a55702 | -19.30026 | -42.59312 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 71bd94b5-218a-3db2-a19e-d530abd78e57 | -19.29948 | -42.57831 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 16fdb6d4-aae2-33a2-aa7c-a38e509af52b | -19.29671 | -42.5821 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b1bd9c72-0747-3ac7-a5b2-a724eb04b297 | -19.29088 | -42.58159 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 25793cd1-ed1e-3fbd-9f7b-6f7929b0b5d7 | -19.29011 | -42.58512 | 2024-10-04 03:17:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| df399465-c000-39ed-942d-29eb7ac0fe9f | -19.28642 | -42.87926 | 2024-10-04 03:17:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a6dae787-4128-373a-bf1d-7c9aed084133 | -19.28555 | -42.88315 | 2024-10-04 03:17:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 0e6031c0-017e-3a33-a7e7-5186b153521b | -19.28464 | -42.88726 | 2024-10-04 03:17:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 3e5d9bc2-6974-3d88-8098-fff0a2f4acfa | -19.28073 | -42.8776 | 2024-10-04 03:17:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a15518fb-4867-3e0b-9795-1e0ac1e6cb68 | -19.27563 | -42.87327 | 2024-10-04 03:17:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8e8d4a4b-ed5b-398a-a0dc-837055e448e5 | -19.27482 | -42.87691 | 2024-10-04 03:17:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 18b5d6cb-989e-360d-97d1-ad7543551b1e | -19.27399 | -42.88062 | 2024-10-04 03:17:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 091fcf9c-9a92-3300-a8c9-e6d3412a66b5 | -19.2708 | -42.8678 | 2024-10-04 03:17:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 680297e9-5295-31fe-9286-03da2eba9671 | -19.26396 | -42.87131 | 2024-10-04 03:17:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bb831471-f0f2-3978-9a4a-cbeee80f3b12 | -18.85575 | -42.91413 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 62fab0ca-ee5a-3ae2-a76c-4292555df299 | -18.85461 | -42.91928 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 941d4baf-cfae-3416-a825-aef8f73817ce | -18.85108 | -42.90758 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 173643e7-7767-3aa2-be38-6caf72e7b753 | -18.85011 | -42.91193 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1519909b-958b-3510-a58f-c55a0c7a0cea | -18.84905 | -42.91675 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 86702c40-64fd-30e7-b3a4-395e1b739680 | -18.8451 | -42.90694 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| d834dfcd-855f-34fa-86bf-cac08982bf9e | -18.8443 | -42.91055 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 1161f096-246c-315e-9da8-d1713ad55d40 | -18.84335 | -42.91485 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| c322055c-b161-3738-bcb6-c8d4b03e0058 | -18.83826 | -42.91022 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| c39d040c-433d-3b33-bbdd-82b085409132 | -18.83734 | -42.91433 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 0b7eff9b-76e4-35ae-9c74-5f165754f794 | -18.83635 | -42.9188 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| c1620387-bd65-3d60-91ce-3f15e33ab36f | -18.835 | -42.9802 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 83826d1a-9cd8-3c0b-b3a9-ba453f43a48b | -18.834 | -42.98472 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 21e84380-1c4f-33f4-8491-cc4203ed85b7 | -18.83302 | -42.98911 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5c49a58b-c99d-3079-9186-d0f5548afc7e | -18.83032 | -42.91838 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9a534e8c-1f34-3bc0-b353-2050ffd14094 | -18.82928 | -42.92307 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3e39fff1-da39-3f0c-85f7-ff6ab8e36271 | -18.82927 | -42.9783 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 90c83249-465c-3ba7-b96f-6ab9d9fa3a36 | -18.82829 | -42.98271 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| bac84949-bc1b-328c-8185-24233065e3d1 | -18.8273 | -42.98716 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8a5dec4a-e0b6-3a8b-8ddb-c67abb2499cc | -18.82629 | -42.99173 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 134bca02-186f-34c2-861d-6a7f098ad9b4 | -18.82046 | -42.9903 | 2024-10-04 03:17:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 5786486a-2318-3636-8f04-e5a28845f488 | -18.3035 | -42.17294 | 2024-10-04 03:17:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 19698362-601a-360c-8ef6-94b4d8c2d626 | -18.3012 | -42.16838 | 2024-10-04 03:17:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 812d707c-7b6b-33a4-9333-1a9e78581e6b | -18.3005 | -42.17152 | 2024-10-04 03:17:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 07274d10-32e0-3d44-8eb5-870c3b25ce4e | -18.29871 | -42.16769 | 2024-10-04 03:17:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 227d1492-5f80-3ef4-8305-97bcc13c24d9 | -18.29806 | -42.17073 | 2024-10-04 03:17:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cbb6e356-394b-3ce6-b2ae-1687aa97dfdf | -18.29069 | -42.15002 | 2024-10-04 03:17:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0d49ac0c-acb9-366e-b372-a3e79ddea4e2 | -18.28989 | -42.15377 | 2024-10-04 03:17:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b0c068fb-239e-3fc0-9d8f-730ba715f093 | -18.57791 | -43.0472 | 2024-10-04 03:17:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c4ec0c01-512f-3a57-a519-6928b6a172d0 | -18.57493 | -43.04527 | 2024-10-04 03:17:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f552dad6-32af-37d7-ab08-10bf4306c20d | -18.57396 | -43.04977 | 2024-10-04 03:17:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b376c7b1-a4c8-38d6-9a2c-bd9c202de97d | -18.57202 | -43.04581 | 2024-10-04 03:17:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 146a17fc-3553-3d95-8a44-27eb4ce37516 | -18.57102 | -43.05027 | 2024-10-04 03:17:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8105e1ee-cd74-31d9-a6bf-c8c29d07ca5d | -18.08583 | -42.59871 | 2024-10-04 03:17:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 87f5b10c-0229-3833-b6c5-05795095f3a9 | -18.08495 | -42.60281 | 2024-10-04 03:17:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 6d62a411-e98b-3da4-91aa-c7cfc9c8fc27 | -18.08005 | -42.59731 | 2024-10-04 03:17:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a54db96b-bad3-399c-8f90-2daff9d0070e | -18.07918 | -42.60135 | 2024-10-04 03:17:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |


[Clique aqui para ver as próximas entradas](README50.md)
