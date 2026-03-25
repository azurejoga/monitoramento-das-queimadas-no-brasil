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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f2a8af4-51db-3295-8a75-b04011f0c5ab | 0.8301 | -59.3437 | 2026-03-25 03:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 619c438d-35b4-3940-8691-57ef1ca5186d | 1.9056 | -60.2691 | 2026-03-25 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a89214d2-0c42-35ad-b64d-836da7adf791 | 1.9238 | -60.2689 | 2026-03-25 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 36b8c464-870d-35b4-802d-c815d63b79a7 | 0.8119 | -59.3629 | 2026-03-25 03:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 105.7 |
| f8541338-d9ba-324c-a1a1-c72d66a6e852 | 0.8301 | -59.3628 | 2026-03-25 03:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c2796398-e51b-3979-917f-25bc4e88c7db | -3.44852 | -40.12402 | 2026-03-25 03:28:00 | NPP-375D | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 0.1 |
| ae7db20d-07c7-3be4-9f30-aed5e7e2483e | 0.8119 | -59.3438 | 2026-03-25 03:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 99.2 |
| acf7278f-518d-35b8-80d9-3872462a376e | 1.9238 | -60.2879 | 2026-03-25 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 06ea19d6-2a21-3881-942e-b185761b1769 | 0.8301 | -59.3437 | 2026-03-25 03:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 846f7c3d-c429-3426-b7f8-0f3ca659c443 | 0.8301 | -59.3628 | 2026-03-25 03:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 18a07ae0-172b-36eb-bc0c-5b1a762ce068 | 3.8389 | -61.2816 | 2026-03-25 03:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 74ce157f-067b-3f59-807a-6eb02a2bc216 | 3.8571 | -61.3002 | 2026-03-25 03:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 2f1edc82-0ead-31c6-bc37-f9c2340e214f | 0.8119 | -59.3629 | 2026-03-25 03:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 96.9 |
| bc5a5c62-4624-3005-bdd9-5167551c2fdc | 3.8572 | -61.2813 | 2026-03-25 03:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 0c5460f1-4ae0-3a79-bae2-4a8ea3c6d72a | 1.9238 | -60.2689 | 2026-03-25 03:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 1a59505f-3b6d-31db-ab01-5139f5e69378 | -5.99815 | -35.32829 | 2026-03-25 03:30:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f137bcd8-e7b6-30cc-a59a-0a2e54d919f5 | -10.23375 | -36.99881 | 2026-03-25 03:30:00 | NPP-375D | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 22cf4be6-e2f1-3ff7-bcb8-4ac1e8f0e349 | -8.57112 | -44.28474 | 2026-03-25 03:30:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b3f31e86-0bd6-3da9-9ce6-1863a5341410 | -9.20167 | -35.97303 | 2026-03-25 03:30:00 | NPP-375D | BRANQUINHA | ALAGOAS | Brasil | 2701100 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 73091607-7ee6-3b2d-a48a-27d8d9cedd2f | -9.04218 | -37.1319 | 2026-03-25 03:30:00 | NPP-375D | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e8c52bcd-b8ce-3d57-9186-35a82a7a82cb | -10.14279 | -36.67262 | 2026-03-25 03:30:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 0.2 |
| a65687b9-a697-3c0c-a6fb-ac4c143db4d0 | -6.24988 | -35.58814 | 2026-03-25 03:30:00 | NPP-375D | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4847fb1a-8309-354c-9765-77b76eb43e06 | -10.10612 | -37.35967 | 2026-03-25 03:30:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c681b74a-0dff-39ce-9bfd-43fcd666adc8 | -11.70765 | -37.64124 | 2026-03-25 03:32:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e0e90765-8b9f-39ca-bb7d-90353974f1b4 | -11.71021 | -37.63859 | 2026-03-25 03:32:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 593772c6-776b-3d06-987d-2bed46e4057c | -10.45635 | -39.65331 | 2026-03-25 03:32:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ccae6752-2e20-3461-89c5-f7f84a44638e | -12.2456 | -38.25629 | 2026-03-25 03:32:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2769a19f-e107-337e-8ef8-fc9b1f4540dc | -17.56061 | -40.2183 | 2026-03-25 03:32:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 77cf3bdb-db63-3dd3-af2c-749f18d33e0d | -12.24473 | -38.25456 | 2026-03-25 03:32:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b62fec76-d32a-3002-982e-2b20b59693fc | -11.7084 | -37.63717 | 2026-03-25 03:32:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 825139fc-f77d-3f87-8334-68581744a9c3 | -13.12382 | -41.18959 | 2026-03-25 03:32:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| f96f7808-6af7-39b8-9c9f-cb1f01ee8a88 | -20.87113 | -43.88308 | 2026-03-25 03:34:00 | NPP-375D | CRISTIANO OTONI | MINAS GERAIS | Brasil | 3120409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5d9c9dd6-d353-35b0-b257-351a0aac3ebf | -21.67409 | -47.36716 | 2026-03-25 03:34:00 | NPP-375D | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c3207d64-ce51-33a0-ad24-1d3fd3153192 | -22.89618 | -43.58745 | 2026-03-25 03:34:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b474cc31-bd79-3c87-8161-b9189ad4db3a | -20.15308 | -43.39782 | 2026-03-25 03:34:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 08d75718-45ab-3af5-af91-9e1adf341a30 | -18.13454 | -41.3531 | 2026-03-25 03:34:00 | NPP-375D | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 77d1cf02-6ee7-3ad3-8e41-d8258df8d322 | -22.89335 | -43.58565 | 2026-03-25 03:34:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5ca57dd4-724f-3b2d-8fc1-a09e2d25fb66 | -20.18662 | -42.76129 | 2026-03-25 03:34:00 | NPP-375D | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.0 |
| 68d1c560-cf0e-3581-bba0-53de40133bce | -22.04448 | -45.43976 | 2026-03-25 03:34:00 | NPP-375D | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 24b2ee7f-84fa-31b8-92b0-54b9f37ac420 | -23.01949 | -48.45224 | 2026-03-25 03:34:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8ed6630-fc24-32be-b40d-4fbf9d3808cc | -19.7974 | -45.68721 | 2026-03-25 03:34:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb6864a4-ca21-3aef-a3fa-4bd479d23de3 | -20.43117 | -44.4065 | 2026-03-25 03:34:00 | NPP-375D | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 840b9409-9c61-3416-a814-90ff1b872c7c | -22.86832 | -45.9761 | 2026-03-25 03:34:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 68b79712-8638-3615-9991-c1987f374c92 | -22.17133 | -47.69253 | 2026-03-25 03:34:00 | NPP-375D | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| de0c6b23-2f4f-39c3-a2be-615b8c242ec3 | -19.57774 | -44.77661 | 2026-03-25 03:34:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 044e88e0-7c63-3a17-a26d-8a9e85e6fcc0 | -20.60798 | -40.4988 | 2026-03-25 03:34:00 | NPP-375D | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e350e21b-c860-3fb4-b92e-ee8c7c255d69 | -22.89841 | -43.58696 | 2026-03-25 03:34:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f0738674-8ae6-33e3-9a1d-53697ed118ba | -22.7012 | -47.63091 | 2026-03-25 03:34:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 85a2a507-332a-30d4-91b4-e8011bf56f29 | -19.92208 | -42.57262 | 2026-03-25 03:34:00 | NPP-375D | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 93877da8-d339-3389-85e4-3eccd1898488 | -22.33455 | -47.18984 | 2026-03-25 03:34:00 | NPP-375D | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55c1e102-8e9a-33d5-aead-22b206e92f7c | -22.5611 | -49.53964 | 2026-03-25 03:34:00 | NPP-375D | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 9639b274-b531-39bd-80c7-44ec8ac7deb0 | 0.8301 | -59.3437 | 2026-03-25 03:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 61a717cf-a3c1-3e78-b2c3-0c6128be5c6e | 0.8301 | -59.3628 | 2026-03-25 03:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 97.8 |
| e24507be-04e0-3fbb-8cac-38946dd14844 | 1.9411 | -60.9132 | 2026-03-25 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 143dc5e8-3f4d-3fa6-a453-4cc22ef7302a | 1.9238 | -60.2879 | 2026-03-25 03:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f4b967a8-7d68-3eee-a524-17c00c4b804c | 1.9055 | -60.2881 | 2026-03-25 03:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 1857f46b-479f-383e-894d-c44072e603a4 | 0.8119 | -59.3629 | 2026-03-25 03:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 117.0 |
| ab9000a6-c8ae-3866-9ec9-50fb920eeb89 | 0.8119 | -59.3438 | 2026-03-25 03:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 2270bab9-9a71-3a2e-b30c-7d322abf2711 | 3.8572 | -61.2813 | 2026-03-25 03:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 17c31116-16a4-33a1-bd82-b2ebe31feade | -6.24773 | -35.58771 | 2026-03-25 03:49:00 | NOAA-20 | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b19d2d0f-217f-364a-bf5d-aaf146465209 | -8.564 | -36.4306 | 2026-03-25 03:49:00 | NOAA-20 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c8051494-894a-3f65-a08f-b65b2befb3f7 | -5.99886 | -35.32624 | 2026-03-25 03:49:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 10.5 |
| ed86b63f-80af-3581-aa68-32f3d172b7b9 | -4.80824 | -38.06312 | 2026-03-25 03:49:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 334a586e-c695-3afe-9c36-b468a4b895b5 | -4.72915 | -37.8152 | 2026-03-25 03:49:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fa7708c5-f33b-33eb-8e9d-e9aaa18ee4c7 | 0.8301 | -59.3437 | 2026-03-25 03:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 35e6389d-1813-3361-85ce-0a8ba7bcf8fe | 1.9411 | -60.9132 | 2026-03-25 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 0cbd10a5-2275-3d1d-ba71-ba9aada50510 | 0.8119 | -59.3438 | 2026-03-25 03:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 20853ccc-5be6-372d-bb49-350a9932e51d | 1.9238 | -60.2879 | 2026-03-25 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 07f0d409-55f7-3f3b-b107-ffe74c08e919 | 1.9055 | -60.2881 | 2026-03-25 03:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 44.3 |
| e5a2c179-e927-3884-a11c-7b6d7efd5673 | 0.8301 | -59.3628 | 2026-03-25 03:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 89.3 |
| cc4bbe99-d32e-3ca6-918a-33b813805cc8 | 0.8119 | -59.3629 | 2026-03-25 03:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 23480407-4221-3296-99ad-e95ff2a515d8 | -12.2448 | -38.25501 | 2026-03-25 03:51:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e447a2ca-22ed-36d8-a6ce-c8aad66aa8c9 | -11.71015 | -37.63877 | 2026-03-25 03:51:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1d0772b7-94cf-38f1-91ef-2037676c4768 | -10.10372 | -37.35679 | 2026-03-25 03:51:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 611d77a2-3428-3421-a5b5-4fbfed433f53 | -11.70684 | -37.63824 | 2026-03-25 03:51:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dab2a53b-711e-3289-b39f-46eb22c0f9fa | -9.97866 | -37.91222 | 2026-03-25 03:51:00 | NOAA-20 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| afe11f02-ecf3-3e5b-8432-337dec789d0f | -11.19447 | -37.65666 | 2026-03-25 03:51:00 | NOAA-20 | PEDRINHAS | SERGIPE | Brasil | 2805109 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 030cbf58-4818-39ca-8ecf-2104c0707f2b | -10.97074 | -37.50244 | 2026-03-25 03:51:00 | NOAA-20 | SALGADO | SERGIPE | Brasil | 2806206 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 34830d66-0a9b-3d59-9f41-0e3c8db79d00 | -22.33772 | -47.18633 | 2026-03-25 03:55:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9013a9f3-db6e-36ac-9020-c25b80e84b3e | -22.06157 | -46.85455 | 2026-03-25 03:55:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9aff0a3c-8c47-36bd-b43e-df419840a50b | -22.0624 | -46.85029 | 2026-03-25 03:55:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1f070b5-575a-3c5d-8579-2b8d9a850f56 | -23.02064 | -48.4464 | 2026-03-25 03:55:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d34797cc-bba0-3ba8-bfa8-1bb7a9dcadc4 | -21.49165 | -48.77091 | 2026-03-25 03:55:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1d06223-d2e7-3575-8f99-f80c98491bd1 | 1.9055 | -60.2881 | 2026-03-25 04:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0746af6a-4a68-3541-9702-a4d3c45db3a2 | 0.8119 | -59.3629 | 2026-03-25 04:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 2350a91e-3211-374c-8c21-1f8174d0a8e8 | 0.8119 | -59.382 | 2026-03-25 04:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9f739b26-2158-3aee-9b74-b67f318fb207 | 0.8119 | -59.3438 | 2026-03-25 04:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 90b01755-59d8-335d-a39d-499bdb188f82 | 2.7247 | -61.3571 | 2026-03-25 04:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 291a6686-fd3c-36c7-9b71-ea9f5873e3a0 | 2.7065 | -61.3573 | 2026-03-25 04:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 74e07ed5-ca2f-3308-8c67-92092a5f0f1d | 1.9238 | -60.2879 | 2026-03-25 04:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 88b0c824-0eb9-36cb-a9c5-0760f81e55e2 | 0.8301 | -59.3628 | 2026-03-25 04:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 78.8 |
| cb732824-bcad-3c88-9d6d-137d92dc2206 | 2.7065 | -61.3573 | 2026-03-25 04:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 49864cd6-adac-3051-b39e-ce0c64dacc41 | 1.9238 | -60.2879 | 2026-03-25 04:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ebf270b1-ea26-3047-bce3-d34705ef4013 | 0.8119 | -59.3629 | 2026-03-25 04:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a19eb5ca-2dc1-3d03-ad23-691b89db090d | 0.8301 | -59.3628 | 2026-03-25 04:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 4843c2c6-fdc8-3398-9ddf-1e6d936002b2 | 2.7247 | -61.3571 | 2026-03-25 04:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| d97bd06e-033c-3abd-8d01-f667f17dce7f | 2.7065 | -61.3573 | 2026-03-25 04:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 3fcfb66e-6a5a-352d-bdc0-01d6a1deee2f | 0.8119 | -59.3629 | 2026-03-25 04:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 1986c439-7256-3a75-872c-bab891e1d769 | 2.7247 | -61.3571 | 2026-03-25 04:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 075e846b-f53b-3bba-abf8-08da98da6269 | 0.8119 | -59.3438 | 2026-03-25 04:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |


[Clique aqui para ver as próximas entradas](README5.md)
