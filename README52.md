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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e9f5ab6-b620-3560-ba32-3a1772d5a99b | -10.77532 | -69.33672 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 873c9d2c-27d1-361f-bdc9-079fb057387e | -10.75619 | -69.41579 | 2024-10-31 06:08:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 612d2482-4e8f-3c9a-8f9f-352a14d52b5d | -10.71389 | -69.45222 | 2024-10-31 06:08:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cfdf4dd-0d13-3bd0-a988-416e81ad86e9 | -10.6885 | -64.99848 | 2024-10-31 06:08:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bb22126-8874-34ee-84cc-288e9229edd7 | -10.68784 | -65.00355 | 2024-10-31 06:08:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f55af53b-46f2-35e5-92b5-9eb3c12005bf | -10.6844 | -64.99262 | 2024-10-31 06:08:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 104122cf-ee44-310b-b39f-7d0478cf8556 | -10.68373 | -64.99776 | 2024-10-31 06:08:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a1a3971d-a464-361d-9a7f-26cf8ae63312 | -10.68 | -68.8114 | 2024-10-31 06:08:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5ae28cb-3239-3e08-a02e-c63bbcd1d9ee | -10.63526 | -69.01795 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01fc25ad-1518-3e8e-ae8c-5ff9122c170f | -10.633 | -69.01902 | 2024-10-31 06:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 588ccfdb-11b1-3415-89d9-08b781da2c67 | -10.59396 | -67.79618 | 2024-10-31 06:08:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da1da51b-8819-3005-bd9f-03b690cd5588 | -10.59206 | -67.79734 | 2024-10-31 06:08:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ac4fbb3-9d63-3644-8371-fe61cb7fc647 | -10.58926 | -67.80065 | 2024-10-31 06:08:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1325be3-8ea5-3eff-a5dd-e9d3a924ac44 | -10.5881 | -67.79677 | 2024-10-31 06:08:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45d5d87d-bb70-38d8-a14a-52de62ba7abf | -10.49055 | -67.89986 | 2024-10-31 06:08:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60793b67-129b-3433-8049-978cc5e16e68 | -10.4166 | -68.39474 | 2024-10-31 06:08:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcea5fc1-c0f6-33f6-9b25-afcbde84a4cb | -10.27834 | -68.04668 | 2024-10-31 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6e65da8-273c-3188-8d78-e2052461a669 | -10.15626 | -68.33458 | 2024-10-31 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de17eddc-62d8-31f5-a0a1-c4eb13c311fd | -10.0994 | -68.37875 | 2024-10-31 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6752572-08ce-36d3-899d-eac3b4895e46 | -10.09873 | -68.38342 | 2024-10-31 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86b0f540-f6a4-337d-88ce-bd419dcc9d58 | -10.0956 | -68.37821 | 2024-10-31 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bd9664b-f7eb-3e88-a101-2704f311f90c | -10.09494 | -68.38287 | 2024-10-31 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 757ca725-37bc-32bd-a819-1564a96588ad | -10.05435 | -68.53226 | 2024-10-31 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66514531-98e3-391f-bddf-0693099962c2 | -10.05407 | -68.53477 | 2024-10-31 06:08:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c000b521-7b82-3ac7-9fd4-8f9c67218f4e | -12.43545 | -63.27006 | 2024-10-31 06:10:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| ee99d0db-bb20-3100-b76b-012cd1346e79 | -12.43322 | -63.2834 | 2024-10-31 06:10:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 24204769-bb17-313d-95f9-4772c32ac68c | -12.42482 | -63.26826 | 2024-10-31 06:10:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a2e0dacd-cc4d-3ad7-97bd-44112b7928d3 | -12.42258 | -63.28159 | 2024-10-31 06:10:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 854bc61f-8466-3040-840d-1f54d822e6d2 | -12.32327 | -63.58327 | 2024-10-31 06:10:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 39d7092e-a88e-3c1f-859d-873ca784d605 | -10.69214 | -64.9835 | 2024-10-31 06:10:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b496cdb8-83f5-36ba-891e-062f95356c2b | -10.68885 | -65.00276 | 2024-10-31 06:10:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 30a01f9e-f454-38ff-8589-e3cddd09c84e | -19.63118 | -56.68898 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 31.7 |
| fb21a10f-58e4-3388-ba1d-b2936717c5f9 | -19.62948 | -56.70231 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 842cdd6d-8c21-3a4a-bab5-2963859aa711 | -19.62778 | -56.71561 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 23.1 |
| 987e1942-db5c-38fe-b69f-7bbccdaa0078 | -19.61899 | -56.70087 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 31aa08cc-f265-39e6-93f0-3a437c037f89 | -19.61731 | -56.71418 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 40.1 |
| fc94e99f-6f02-3975-92b6-9c571f2ce621 | -19.61562 | -56.72745 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 123.9 |
| d3ed12a1-6fb0-3bc1-b4f9-282e61c0bf98 | -19.61394 | -56.74069 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 9c5691c1-23c1-3b41-9427-4bfd5e3f9d4d | -19.61226 | -56.75391 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 67933188-672d-3dcc-a711-31e8906c3f81 | -19.60851 | -56.69944 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 35.9 |
| 26f5458f-cd52-3a12-90a6-29e700a09797 | -19.60683 | -56.71274 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 40.7 |
| 34f5d2cb-7ecc-3427-a33e-826eb5e48bdd | -19.60515 | -56.72601 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 173.0 |
| d50a35d1-fe2f-31ad-84a0-7f0df03302ff | -19.60348 | -56.73925 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 904.8 |
| ff5ec78d-78d5-3b13-ace0-d3277b8d42f8 | -19.60181 | -56.75247 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 770.2 |
| 567f98b8-f217-340c-85db-7f886ceddc85 | -19.60015 | -56.76567 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 38.1 |
| e5d033e9-6e2c-3581-8eb4-797157b2bc38 | -19.59635 | -56.7113 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.5 |
| 29630da2-bb6f-3b2d-88c7-5d63c52ef2fc | -19.59469 | -56.72457 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 170.3 |
| 960436b6-0a7b-3ad8-bcf6-2a2dce70e0c1 | -19.59303 | -56.73781 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 170.4 |
| 05d43e96-7310-3dc4-ad0f-c48b1ce7ee56 | -19.59137 | -56.75103 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 124.1 |
| f51658a4-6869-3f14-9211-f40042b3f709 | -19.58697 | -56.61472 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| ae33e5cd-58ab-34fb-a9a7-daeb395fd5c0 | -19.58587 | -56.70986 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 46bd3710-8511-3495-b29c-0370e3ea16bd | -19.58422 | -56.72313 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 64b6866a-faca-3c3c-96da-a5ff9f604dc3 | -19.58257 | -56.73637 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 25.6 |
| 24bd9475-128f-384c-a085-cdbf931ff23c | -19.5754 | -56.70842 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 29.7 |
| 94023b03-50ad-313b-9073-05db065778ff | -19.57054 | -56.70092 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 0c563aa0-a16e-3d8f-b706-bed380ebe0d7 | -19.56882 | -56.71418 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 32.0 |
| 93c21e62-2b03-38d5-b9cd-cea890a96886 | -19.56492 | -56.70698 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 47.1 |
| 35f74beb-72f3-3532-8771-69e01447bc22 | -19.55835 | -56.71275 | 2024-10-31 06:12:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.4 |
| c016ee6b-1530-3178-94bf-98d0cf944eac | -19.53741 | -56.70987 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.9 |
| 4b6047f9-eae8-38c6-8be2-25dd3c5b9cb9 | -19.53572 | -56.72311 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 228.9 |
| 9a17bb6c-3ed0-34d7-8032-fc1ba5c37e84 | -19.52694 | -56.70844 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 49cacfcb-3d8c-3750-a5ea-0a3cdee543ad | -19.52526 | -56.72167 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.8 |
| 36d50bcb-441c-3adc-836b-ab61dbb29bfb | -19.51052 | -56.58374 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.7 |
| bbf5870e-d955-3545-a8c1-71b4e1b7ae65 | -19.50884 | -56.59723 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 98f8cfd5-48c0-3df7-854e-0ab0ca879ca4 | -19.50767 | -56.6923 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 907dc9e9-0fbd-3373-bb69-679c0da1d7e0 | -19.50601 | -56.70557 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| f4e180d3-4d88-38a5-bba1-079a421754d7 | -19.50163 | -56.56878 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.3 |
| f5448894-dc41-3a1a-9623-266cb298f439 | -19.49996 | -56.58229 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.5 |
| ce2f09fe-6330-3376-abaf-e8297bad89f7 | -19.4983 | -56.59578 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.3 |
| d34fb93c-acbd-3da2-846b-77923288f631 | -19.49554 | -56.70414 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.1 |
| b1211e9b-98b8-3cf3-8b6f-e2fe5b7ba9e7 | -19.49389 | -56.71738 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.8 |
| bd49b4ac-4049-30c9-baad-9a5cdd1db584 | -19.48343 | -56.71593 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 8252f155-e05c-3730-be1f-525749df8702 | -19.47879 | -56.61492 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.4 |
| 6db60926-ad01-30ca-9f52-ec298dad8352 | -19.47534 | -56.64168 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.0 |
| f840232d-1ecf-3266-aaa3-baa5d94e57a8 | -18.25872 | -55.95687 | 2024-10-31 06:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 0d2d73a4-1322-3c69-93c2-b8a180c6843f | -17.27268 | -57.49759 | 2024-10-31 06:12:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.0 |
| 878ded08-6156-3e7e-911b-fc52c5365c3d | -16.92291 | -57.65435 | 2024-10-31 06:12:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 9ed3693a-2687-307c-a488-77405b0b1eb5 | -9.94574 | -68.62229 | 2024-10-31 06:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 906a251e-c181-3767-9855-428772539de0 | -9.94523 | -68.62621 | 2024-10-31 06:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63708ad8-eb75-39a5-b547-a80b5f90b876 | -9.33594 | -68.77428 | 2024-10-31 06:31:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 170cb826-47aa-33d5-860e-c400f70ba4ae | -8.62508 | -69.71986 | 2024-10-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3346a8ea-32e9-39ed-95da-cd05e421b28f | -8.62466 | -69.72301 | 2024-10-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11881089-7eaf-3625-ae25-e0ef67c95a1d | -8.62423 | -69.72612 | 2024-10-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e600e4df-4b5d-317c-9741-0c346fa1c9ea | -8.61945 | -69.72229 | 2024-10-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d1696ae-7d3c-3ac3-a65b-7dc114780e8b | -8.61903 | -69.72542 | 2024-10-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8910b95-ac96-3774-93a9-40898c36b640 | -8.61817 | -69.73172 | 2024-10-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3010292-3a8e-34d8-8da4-0e7154a16349 | -8.11284 | -71.32602 | 2024-10-31 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0d74f75-f6c3-32b0-b849-dc966324313b | -8.06939 | -70.88319 | 2024-10-31 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fa0e79f-e909-3185-a77e-8df2bfddea9c | -8.0687 | -70.88831 | 2024-10-31 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9afdb39a-d579-3739-8648-05fa2678c708 | -8.06831 | -70.88582 | 2024-10-31 06:31:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed815a25-2af4-3fd0-8e0a-4c4627077e8f | -7.84425 | -70.12698 | 2024-10-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4898b3c-1574-3ed8-baf3-eebcd9fc566f | -7.83885 | -70.12923 | 2024-10-31 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63b2429c-26b5-3f2e-8ea7-9d99de557ddf | -7.02477 | -71.79727 | 2024-10-31 06:31:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b461afbb-3f15-3f62-b61a-d372ea2dd430 | -10.75773 | -69.41767 | 2024-10-31 06:31:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a930530d-510c-3c29-b1a3-9bc1a3562992 | -10.63446 | -69.01889 | 2024-10-31 06:31:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93815b49-de25-3727-9a6a-47448722f4c0 | -10.63397 | -69.02275 | 2024-10-31 06:31:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 771ac85c-c59d-3784-b077-79140d85ddc7 | -10.09492 | -68.38274 | 2024-10-31 06:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79a0d596-e01d-39a8-a41a-89e21923af0e | -10.09459 | -68.38326 | 2024-10-31 06:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31277118-fa36-3ab8-9462-5389d1e828d1 | -10.09442 | -68.38688 | 2024-10-31 06:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea85ca1c-78b8-3f91-b7da-6d752683f4f8 | -10.09405 | -68.38738 | 2024-10-31 06:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README53.md)
