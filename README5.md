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
| 8163f962-c2ad-338b-a221-afacb31b9c4d | -8.2171 | -45.484402 | 2026-09-28 00:33:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a0d0767-797a-30ba-9c97-b8d8e7c0beca | -9.0776 | -49.883499 | 2026-09-28 00:33:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22c0a21a-d0e9-37a5-b282-c301c0b09948 | -12.1551 | -50.355 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bdf8a96-4092-32d4-8a6f-ae4e88dae975 | -11.4309 | -44.9384 | 2026-09-28 00:33:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae500171-469c-31c8-a44f-f8daf6f383a2 | -13.9869 | -53.996498 | 2026-09-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5ce5ced-a3cf-3232-b373-7cbdfd630fb7 | -6.6929 | -45.583 | 2026-09-28 00:33:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31d1a385-834e-3f36-8c9a-5ec3d450ad9f | -14.7169 | -45.571201 | 2026-09-28 00:33:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0818eb9-96e6-351b-8103-22e2d0b3284d | -11.4405 | -44.935799 | 2026-09-28 00:33:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa96b1f0-bb27-31a4-8a5d-6c5839a71d01 | -3.2004 | -51.041199 | 2026-09-28 00:33:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2235d916-e3c2-3ae1-a344-7432a29f1c8f | -11.2103 | -44.764702 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e7bc2ae-a8d1-3aee-a4f7-ac2e17bae1f1 | -18.6649 | -41.462502 | 2026-09-28 00:33:00 | METOP-B | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6ee14832-865b-3253-8284-7d873243cbdc | -15.1698 | -46.158699 | 2026-09-28 00:33:00 | METOP-B | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fb3f8f20-2c14-3f72-ad46-1d1c5dfd0b9d | -9.9624 | -45.353802 | 2026-09-28 00:33:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f4912fb7-0539-3ec5-9d3b-e56e28fa2007 | -10.0035 | -50.127998 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b3c2a4d-2c8e-3514-ac67-1878f7d5ea9b | -13.0734 | -47.4361 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 563d03bb-8e58-39f0-9c7e-9b996976980f | -15.1167 | -53.8895 | 2026-09-28 00:33:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 790135d3-c680-353a-95c0-ea2bceb1a29e | -15.1569 | -43.608398 | 2026-09-28 00:33:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 15c4ea7f-d8b1-30e8-a435-040dd2dd511e | -7.7106 | -54.775501 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36670db4-abc6-3a56-928d-b13c9fa38f9e | -17.8916 | -45.064499 | 2026-09-28 00:33:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c0093566-9725-3f7f-8483-e859e35f9410 | -11.2161 | -44.7869 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 650c7d83-b361-308a-ab79-892d3276695d | -13.2028 | -48.327801 | 2026-09-28 00:33:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdae2997-648b-3201-bd23-2bfb7aae79e3 | -2.0608 | -56.867401 | 2026-09-28 00:33:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| feaf3f8b-f8a4-361e-81f2-2feae0e14310 | -11.2123 | -44.8116 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| af89216f-04b3-3ea6-b987-a203baa78163 | -1.7709 | -53.775299 | 2026-09-28 00:33:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 583fd52d-7eb6-3ce7-b7e2-d9e4701303b5 | -7.4979 | -55.02 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e328aa2e-d7fd-3ea2-94a9-582d34df5abf | -3.2723 | -54.257702 | 2026-09-28 00:33:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a326738-9e11-3401-b850-62bb3e3c1742 | -2.7244 | -54.205898 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6da5f5b3-c7d9-3d18-bff9-80719e9e1795 | -12.1431 | -50.348 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b731d3c-32c2-33cc-8d81-c5590899afd7 | -9.9816 | -50.165699 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27e9484f-cd74-34e8-9b8e-68d05956cd89 | -11.0855 | -51.333599 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fb6369ee-9d3c-31f6-aa6e-30c0c5c1748f | -3.4489 | -56.487499 | 2026-09-28 00:33:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c4983de-4e59-3111-81b5-6b81d83989f5 | -9.9889 | -50.153198 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d57a9bf-f14f-3a6a-9d4a-3757b6bf8400 | -10.2202 | -49.998402 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ea62d95-7ea3-3ec4-888d-e96b762b644a | -4.0366 | -54.218899 | 2026-09-28 00:33:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d1924ca-374a-3ca6-b5e4-bdc3c19dbacb | -3.2271 | -54.330898 | 2026-09-28 00:33:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36d50993-09dc-314a-bc78-96211c07224a | -2.8608 | -49.630199 | 2026-09-28 00:33:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c1deb9c-c3dc-32ee-8145-a7ea43898372 | -6.6506 | -55.102402 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 005ab537-7951-31b6-9c19-8c39d62ff03e | -11.1776 | -44.797298 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f1152c09-29c8-3e0e-a7aa-37312854ee90 | -2.2676 | -57.007401 | 2026-09-28 00:33:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cfb12a77-31bb-3b91-8995-bfbe8cfdf026 | -14.4837 | -53.6366 | 2026-09-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 954baa1d-5a8a-3d2d-816d-d46e6d71bdc7 | -13.0956 | -47.401001 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34f27ae7-0208-3e09-83f8-638df7807342 | -11.2007 | -44.7673 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3ad1b04-b6c9-341c-b4e5-27dc4219480d | -10.8158 | -60.725399 | 2026-09-28 00:33:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a067c327-37e5-3133-9952-015722a2b125 | -2.9339 | -56.580601 | 2026-09-28 00:33:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebaac30b-5c9a-3d81-9b39-911314e81208 | -15.1377 | -43.613998 | 2026-09-28 00:33:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 6997021f-bdb7-30f3-a776-59d2c4262f64 | -6.2668 | -55.456299 | 2026-09-28 00:33:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8a05db4-cbde-311a-8bb5-bc0153da6b73 | -16.4631 | -55.0718 | 2026-09-28 00:33:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 906accf0-20b5-3209-bd92-b6570c51eb8e | -2.6698 | -56.460602 | 2026-09-28 00:33:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a27b0180-013f-313f-b9e5-727034c87023 | -2.7623 | -49.4725 | 2026-09-28 00:33:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ef4c8d0-ad14-387e-86fb-c5f2dd353e3b | -11.1719 | -44.775101 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b50fc44-7098-3caf-bf4c-bbfe315fda3c | -9.9865 | -50.142899 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 599e4e56-9274-396e-93f3-3dfa25881007 | -13.6869 | -48.823101 | 2026-09-28 00:33:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b430a5d3-aacf-327e-af89-4f8f0e4ec535 | -10.4131 | -53.825901 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee421d20-0e49-3d34-b0a8-93b7afe1a2e7 | -6.6538 | -55.116199 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e0eb994-1970-3230-8b53-2bc25bcced02 | -2.9194 | -54.202099 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edacf116-bf70-34d0-866d-61a7aaaeec16 | -12.3023 | -50.278801 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2023b74f-1eda-3a58-95f3-99c7f4810dbe | -8.6625 | -48.977001 | 2026-09-28 00:33:00 | METOP-B | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7052d006-0b0b-341c-8edf-5538be7f368b | -14.4852 | -53.6436 | 2026-09-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91b78e39-4d06-3513-9954-ddab1b43d977 | -8.2227 | -45.506599 | 2026-09-28 00:33:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 239b1b18-f7de-33c7-9cdf-6d11c1c78d93 | -1.2269 | -54.100201 | 2026-09-28 00:33:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ef53f9c-db66-3af8-9aa4-1d6531ecc51b | -2.7754 | -49.484699 | 2026-09-28 00:33:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2778b0ec-5e03-3f0f-8b3c-f2eebc41e7bf | -12.595 | -51.9585 | 2026-09-28 00:33:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6a1bcdc-0f56-3c7f-ade8-8030fef21fd3 | -15.4081 | -47.9137 | 2026-09-28 00:33:00 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| feac6da0-9e37-3d44-bf6a-a9e7e11fb441 | -20.1835 | -48.5774 | 2026-09-28 00:33:00 | METOP-B | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7eea744e-4899-3f8c-819e-ea45e9b5e4cf | -10.9101 | -50.680099 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fd48eddb-bde3-342d-8597-ec55ebd5674e | -10.4213 | -53.816601 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce872f1d-6f34-3865-9e4d-085a841eeb24 | -12.3099 | -46.423 | 2026-09-28 00:33:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73510706-1980-3f65-abbd-6ff463f345a3 | -11.3094 | -55.1092 | 2026-09-28 00:33:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3f17973-a36e-3330-9465-a3a6badb23eb | -10.9123 | -50.6894 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d6e833c1-24dd-369d-b49a-0a8b71a218cf | -11.0835 | -51.3251 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ef2330b-8cea-3901-b33c-317d4ed5aa67 | -13.4654 | -48.5951 | 2026-09-28 00:33:00 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a381d0ef-b5df-34e7-bbe4-69515d2c7c3a | -11.2315 | -44.806301 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e99ec5d-7a28-3dfe-a111-f1072cbfba11 | -13.7064 | -48.818001 | 2026-09-28 00:33:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 044d452c-c405-3812-b455-2a25d55a9d84 | -3.5418 | -55.531799 | 2026-09-28 00:33:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f30b6a1-58b6-3651-9e47-e28fc8199ccd | -7.7213 | -61.245701 | 2026-09-28 00:33:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44d89cf2-108e-3dc3-a1b1-5815c75f5942 | -7.863 | -61.191399 | 2026-09-28 00:33:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96ecb268-5948-35c7-9b86-083a802e26db | -11.1987 | -44.838699 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7513cf87-2872-301b-b94e-70b07eae4921 | -13.3766 | -51.3237 | 2026-09-28 00:33:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd07874f-acde-343b-b088-f03c16fb9db6 | -2.8932 | -54.087502 | 2026-09-28 00:33:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38486e1f-a19d-344d-a435-73e8b80cb47b | -18.672701 | -41.489601 | 2026-09-28 00:33:00 | METOP-B | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd42dd1a-279f-3991-adc5-34c7a576d6b8 | -10.4001 | -53.813999 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6073afb5-efb9-3409-b039-dc6f21bab564 | -11.3427 | -54.1068 | 2026-09-28 00:33:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48ed58f9-9c0a-3baa-85ee-f786a1f52adb | -8.0388 | -54.9049 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7c80a27-756f-3bbd-be8e-21244d4d3fbf | -12.6257 | -47.3009 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82237179-e09f-3bf1-880d-0f86d76dc28f | -13.1025 | -47.428398 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59655362-58dd-332f-a27c-5e7175e49730 | -11.3329 | -54.1091 | 2026-09-28 00:33:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1885b2-ffa1-3184-912c-1b792664e4ac | -11.1891 | -44.841301 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 295f2d9f-6f8d-3aa4-9858-6e787dab39a2 | -11.0935 | -51.367802 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 984a93e6-28e9-30df-8fcd-184f199ec405 | -3.0163 | -54.2201 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a10f4c11-29e8-374c-90f6-34f1ce5de165 | -6.662 | -55.107101 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6edd396c-bcee-3788-9f16-b47716c60ef6 | -9.926 | -60.710899 | 2026-09-28 00:33:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8f0de0-dedb-3adf-93ba-72daff2ed5df | -15.1473 | -43.611198 | 2026-09-28 00:33:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 58013b84-8912-394c-8026-cf2585dd7053 | -21.521299 | -45.105099 | 2026-09-28 00:33:00 | METOP-B | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3bb98088-4d50-353a-9349-dbbb09a5c581 | -11.6774 | -44.541698 | 2026-09-28 00:33:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 86c04a85-9160-35e7-9fc8-107d4e3c49dc | -6.6823 | -45.9921 | 2026-09-28 00:33:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f82f92ac-1ff9-365d-9e0d-bca2a24e7329 | -12.1791 | -50.368801 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7c74d96-77e5-340a-8c24-9f2c2352ce4b | -3.4473 | -56.480701 | 2026-09-28 00:33:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70583374-3e12-3d51-9cd0-6381cf800fbb | -13.3746 | -51.315498 | 2026-09-28 00:33:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 31b599ee-de3f-345b-a1d9-687515f5739c | -10.4245 | -53.8307 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dff5f0d2-b6c7-3575-a2fa-22a66b35e897 | -7.8727 | -61.189301 | 2026-09-28 00:33:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
