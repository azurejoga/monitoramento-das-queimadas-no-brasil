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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b12dd3d2-5657-338b-8700-0ef724c4ca15 | 1.1393 | -60.5222 | 2026-01-17 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8ecf2231-4b7f-3410-bde8-6b457bf1aad4 | -11.7984 | -45.3627 | 2026-01-17 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 04876eb6-81b6-3b7a-8778-f42f9d09336c | -17.284 | -42.6479 | 2026-01-17 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e60ee158-a712-3c63-8fa7-63da1c5a1334 | -12.6553 | -46.7633 | 2026-01-17 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 271677bc-7ac1-3b13-8dfb-8b52ac3e79bc | 2.7634 | -60.315 | 2026-01-17 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 9d8667a6-7b0e-3e42-b40c-96541a111de5 | -11.8176 | -45.3599 | 2026-01-17 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ec8ce335-b21b-3151-8a32-1c1246db2e25 | 1.1393 | -60.5222 | 2026-01-17 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 16748fd1-f6c6-333b-8a24-9f24bd6e33da | -17.284 | -42.6479 | 2026-01-17 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 7574248f-5ad0-3cee-a90f-e542b8079d7c | -11.7984 | -45.3627 | 2026-01-17 00:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 882d0469-652e-3dc8-873c-fcef19a72b33 | -12.6553 | -46.7633 | 2026-01-17 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d43df0e6-8cef-376e-adfc-cc2a9f717b85 | 1.1393 | -60.5222 | 2026-01-17 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c8a04d48-0e28-32c7-a3e1-bd4fb34b71df | 2.7634 | -60.315 | 2026-01-17 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 6ac1e374-3dee-3602-b9e8-dba9a86becc4 | -11.7984 | -45.3627 | 2026-01-17 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 47841504-8027-37e1-b308-471a04643e84 | -17.284 | -42.6479 | 2026-01-17 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 3213d48a-ad2a-361f-ad22-87ade10a6472 | -11.8176 | -45.3599 | 2026-01-17 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 61cb5e0f-042b-3139-9b80-34056c8ed53f | -12.6553 | -46.7633 | 2026-01-17 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 97e06ef5-528e-3be5-a118-0f48997a777f | -11.8176 | -45.3599 | 2026-01-17 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| b1326bcd-8bbc-3294-ab03-a758bf116b5a | 1.1393 | -60.5222 | 2026-01-17 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| b35317b5-49bb-3415-8468-03cf3fe5ea2f | -11.7984 | -45.3627 | 2026-01-17 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| f126b13e-8da8-3af6-8269-3c4cb12672cf | -16.5846 | -57.787399 | 2026-01-17 01:14:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0980265a-a1d4-39bc-b2bf-cbe5072a26c3 | 2.7716 | -60.297199 | 2026-01-17 01:14:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 68ba9b49-1de3-3575-99f7-b3174198ae43 | 2.7655 | -60.324699 | 2026-01-17 01:14:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b89ff6bd-0ca1-36f7-a08e-587007014ca2 | -20.721201 | -55.137199 | 2026-01-17 01:14:00 | METOP-B | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9e625fa6-90f5-3a9e-a22a-d2ab9a442bfd | -15.4395 | -56.317799 | 2026-01-17 01:14:00 | METOP-B | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b7ed8ae0-1b89-3f64-9544-03b40f60761e | 1.1384 | -60.502899 | 2026-01-17 01:14:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2de485bb-eded-379e-b274-055ea61cd9c2 | 2.7686 | -60.310902 | 2026-01-17 01:14:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 82f743a8-e176-3646-9a05-6fffcf831b9c | -16.587099 | -57.797901 | 2026-01-17 01:14:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f8dafc0f-90b6-3c3c-89d8-c1b0911c464e | -20.7246 | -55.150299 | 2026-01-17 01:14:00 | METOP-B | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a8d816ca-3fb1-3d22-a172-848ac97cad8c | 1.1393 | -60.5222 | 2026-01-17 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 76c8f36c-5d16-30c1-822a-43a89b883b55 | -11.7984 | -45.3627 | 2026-01-17 01:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7133c26e-2ce0-3e4e-b1c2-82ca3e5362f9 | -11.8176 | -45.3599 | 2026-01-17 01:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 1bbf09c6-df6a-3b8d-9829-8bf28fdf4109 | -20.43599 | -57.8861 | 2026-01-17 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 77889cd8-4e06-30d9-93fe-76b4fca7324a | -20.72788 | -55.14931 | 2026-01-17 01:24:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 59457f57-6c4c-3b01-a1a8-50de04257f02 | -20.43188 | -57.87733 | 2026-01-17 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| fc82790e-c353-38aa-9ecd-807a847661f9 | -20.43349 | -57.8714 | 2026-01-17 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| b92701e5-80e6-35d3-b6e8-ffc83c1531c7 | -20.45618 | -57.80589 | 2026-01-17 01:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 5e1309a2-0ebf-3d1b-b7ff-38b2a6809c40 | -20.73201 | -55.17165 | 2026-01-17 01:24:00 | TERRA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 17.9 |
| e24b046a-9131-3fb1-b5d5-5a9a6448bcae | -16.58737 | -57.81031 | 2026-01-17 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.7 |
| 4caa91bd-11a3-39dc-98e0-2669489fc74b | -11.7984 | -45.3627 | 2026-01-17 01:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 64867618-b86e-3626-9383-8826e70225f0 | 2.76215 | -60.33036 | 2026-01-17 01:32:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| f5fcb497-7e3b-3dfc-a35a-c90f6f5b06ab | 2.77589 | -60.33221 | 2026-01-17 01:32:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 713c5170-3e84-34c0-922a-9dd32bf8f201 | 2.7693 | -60.32557 | 2026-01-17 01:32:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 8c5b24f2-4385-31b3-a027-11b3793d0f8f | 1.13128 | -60.51279 | 2026-01-17 01:32:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 1ac8ee8c-3f7c-39f3-9ce5-6b2b9e7b0574 | 1.1393 | -60.5222 | 2026-01-17 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.6 |
| d4d1d1df-6e28-3b7b-b986-a0e055defe96 | -5.9408 | -43.3922 | 2026-01-17 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 63.8 |
| cec47d6c-e39a-3118-9160-3840d3726a07 | -20.4289 | -57.773899 | 2026-01-17 01:53:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aa6db896-afc5-311b-9854-630e41d50dce | -20.4259 | -57.762199 | 2026-01-17 01:53:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 12cfc5ec-0566-3d99-ab38-9bb58a0e741d | -13.7058 | -55.6567 | 2026-01-17 01:53:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b1300cb-50fb-3ea6-8fbe-fceecd2ed144 | 2.7632 | -60.308601 | 2026-01-17 01:53:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b8d0ebc7-76f9-32b9-a68f-d444bf78693d | -13.6962 | -55.659401 | 2026-01-17 01:53:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 18748e83-453a-34be-878e-fbbd2f0563c9 | -13.6993 | -55.6773 | 2026-01-17 02:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 7c3c2ae2-e254-3da4-8e10-4f9a50afb29f | -15.8955 | -43.4523 | 2026-01-17 02:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 59.4 |
| cd8cce47-0560-302d-9935-bec9dc2582ea | -10.2386 | -36.2857 | 2026-01-17 02:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| a2e66e2f-ccf0-3bda-8cb9-c035b304c244 | -13.699 | -55.6977 | 2026-01-17 02:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e093fb4e-1eed-3e83-84f5-03ce3311aa8b | -10.2386 | -36.2857 | 2026-01-17 02:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 65.3 |
| c230c531-d361-3929-8630-747c55eedd7f | -13.6993 | -55.6773 | 2026-01-17 02:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 6b07b672-6c12-3ca9-9166-3d3a352f362e | -13.6801 | -55.6792 | 2026-01-17 02:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| d87f7883-d28a-3494-a39e-0abd5f41492a | -13.6996 | -55.6568 | 2026-01-17 02:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| a194e65a-d395-3fb3-b2bc-a722cd1e14f6 | -13.699 | -55.6977 | 2026-01-17 02:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 2bbba1a4-a094-350c-9382-8c20db2e1e82 | -13.6993 | -55.6773 | 2026-01-17 02:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 7b5cce01-90b9-3e95-bfcb-63f40d29c02b | -17.27367 | -42.65556 | 2026-01-17 03:08:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e44460c-ab4d-3813-a3f5-5e6ab8abb2e5 | -2.90252 | -40.44038 | 2026-01-17 03:53:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f47f1c4b-2b6d-3eb1-adfa-0a083a6cf9cc | -1.67311 | -46.70327 | 2026-01-17 03:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb802669-09e7-3431-8fda-956e628c0e6c | -1.67592 | -46.70246 | 2026-01-17 03:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e6a11f3-0c2c-32f2-9104-568157b44cdb | -3.01697 | -41.83516 | 2026-01-17 03:53:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0607aeb3-0820-3250-bcae-c390e7792d3e | -3.01247 | -41.83702 | 2026-01-17 03:53:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6990d5ae-d4c5-3159-a7b0-82a8cf878e45 | -3.01627 | -41.83762 | 2026-01-17 03:53:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| da9c8c1c-8083-3012-a9a4-c44b24fe7f1d | -3.01317 | -41.83456 | 2026-01-17 03:53:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 51ca7329-c870-3c4d-a423-a3dfee71b8a0 | -5.93182 | -43.39731 | 2026-01-17 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7bd02948-46d8-38ca-9925-6c6559fae57e | -10.45274 | -39.16354 | 2026-01-17 03:55:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aad051af-7356-30fb-aaba-410f50a666e5 | -8.42927 | -44.01823 | 2026-01-17 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83b76603-d8cf-33bb-b675-d8655b74b94d | -6.08391 | -37.3141 | 2026-01-17 03:55:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d394b6b8-8538-3e56-af7b-ed43f02a3fe2 | -5.37516 | -43.19278 | 2026-01-17 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce3a04ef-aeb6-347f-8084-b1182b103b95 | -5.13776 | -37.60302 | 2026-01-17 03:55:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8cfc6295-e083-315e-919a-8842d5ccb23f | -8.49767 | -39.92952 | 2026-01-17 03:55:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dd87c34c-f3e5-3c21-8412-88704a560baa | -6.22443 | -44.16063 | 2026-01-17 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 272d9e88-e405-3109-b171-616f9612b1e6 | -4.258 | -48.83837 | 2026-01-17 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 013821c5-91e3-3710-aac2-899205351823 | -6.55977 | -43.59288 | 2026-01-17 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a917a8f-6a41-318e-93af-d6c0102a06d3 | -7.02308 | -37.44127 | 2026-01-17 03:55:00 | NOAA-21 | SANTA TERESINHA | PARAÍBA | Brasil | 2513802 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d6b02ad5-ed5a-3497-9dea-92d23b1b8ff6 | -8.48955 | -40.66071 | 2026-01-17 03:55:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7623de52-e6ff-39d9-a4ee-48918e4497ff | -8.43449 | -44.01194 | 2026-01-17 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88bd5178-d35a-3e08-895b-a80dbfa05131 | -10.56337 | -44.31992 | 2026-01-17 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e2365c96-d48e-37cc-86ed-6ef29e05b72e | -10.53553 | -36.97794 | 2026-01-17 03:55:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cefb460b-eb7f-3d30-ab42-7afbba4faa06 | -9.50866 | -36.89249 | 2026-01-17 03:55:00 | NOAA-21 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ff7d931-880c-3d77-8bc0-e8beee71876f | -6.94171 | -45.85089 | 2026-01-17 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac985f70-a57a-3362-91a1-c00c152416c4 | -5.4363 | -44.03918 | 2026-01-17 03:55:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1c1dea2-c45c-3831-9c68-ebb35d6ea891 | -8.98142 | -48.07888 | 2026-01-17 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b4e647e-1b45-37a4-a064-4763b2e8c046 | -8.42987 | -44.01477 | 2026-01-17 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e693085a-a966-30de-9da4-52ea9e9a83b9 | -5.84424 | -37.47812 | 2026-01-17 03:55:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d2804bc8-3eca-361e-be60-cab3fc8e5534 | -8.43389 | -44.0154 | 2026-01-17 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8951f90-1e79-3b49-9b37-7f777b7ad084 | -7.2606 | -43.06277 | 2026-01-17 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 90a5669a-c5e3-3d6e-b5cc-37f2bbcc10fc | -7.1833 | -44.95387 | 2026-01-17 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc04b884-4f1d-3d81-bc19-aad0eb7d36c0 | -6.98906 | -42.86552 | 2026-01-17 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| c4be3efd-a460-345d-a039-a82dc3a8ee60 | -8.43329 | -44.01887 | 2026-01-17 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f155c3f-d62d-3e24-a29c-839927a8301d | -9.06437 | -38.22629 | 2026-01-17 03:55:00 | NOAA-21 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d9359cf-7625-3935-a49b-8810e6660040 | -6.89888 | -42.84737 | 2026-01-17 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 46dbb7fe-9489-344d-8470-d9e232c1bfa8 | -5.71558 | -44.13589 | 2026-01-17 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f03bd41-9f34-3d53-9daa-f587772d1790 | -10.45604 | -39.16406 | 2026-01-17 03:55:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8ca02481-0d52-3341-899d-b070adbae22f | -6.37992 | -43.81791 | 2026-01-17 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d03547c7-771b-34bf-ac9e-9acb948b41fd | -8.97623 | -48.07775 | 2026-01-17 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README3.md)
