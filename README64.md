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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb3314c4-5024-3e3e-9159-ef4f0a431ddb | -14.76712 | -59.65857 | 2025-08-24 05:01:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb5db162-b9b1-3488-b7af-fd61915a8206 | -11.54272 | -51.8579 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0a2b15b5-896f-3504-a148-44f543a25d4e | -14.81023 | -47.92706 | 2025-08-24 05:01:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 24c81064-f7d4-33b6-ac74-b21228fd43b9 | -16.79523 | -51.35402 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 97ec5809-5c48-34c3-b7a4-78642204d1d9 | -9.02458 | -65.71096 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9536ebd9-d3aa-36cf-928d-2a14c1702655 | -11.79567 | -48.78793 | 2025-08-24 05:01:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04a97c03-4ad0-3af4-a46d-305f60cf1ee1 | -13.49997 | -47.02986 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b45e630-2cf4-37b7-9d6c-fe1aee5e5d1e | -11.73562 | -51.70353 | 2025-08-24 05:01:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e76703a-c5fd-371d-9747-cd27f5f48bec | -9.01794 | -65.38449 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 980abbe2-fc8c-37c9-8d3d-4e29a2f67d47 | -15.29849 | -56.15255 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d58a8f0b-ecdd-3b3d-977f-2ef75de7619e | -14.29831 | -60.37835 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2910751f-a9fa-36a7-916e-3c250024b17d | -17.83961 | -50.81254 | 2025-08-24 05:01:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 866e6c69-6664-38a1-bcf0-e8002d2628fe | -13.45707 | -47.02176 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b4bcb929-c3fe-3ab5-8223-4bb3ae855fe0 | -13.05458 | -45.23497 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de48d9b8-2e8e-33a1-86b4-7d4635c2573c | -9.51838 | -60.50884 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e104756-f7d7-389d-bcb6-4daa99110bc4 | -13.68933 | -57.75654 | 2025-08-24 05:01:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 938d2f06-cbd5-39f7-aa16-a6327fa4136b | -11.51694 | -51.88046 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6b5b404-d40f-3e8a-8a31-49e2e7a8ed0d | -12.20853 | -47.11222 | 2025-08-24 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f614dec-0231-3b54-9d4c-355575440a95 | -9.04862 | -65.72503 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 262441ec-2bb9-3278-86c5-7c534687ea98 | -16.49325 | -46.75103 | 2025-08-24 05:01:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b817afc3-d8d4-3a84-9622-c6c5d46ca0b2 | -10.42107 | -64.42267 | 2025-08-24 05:01:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 34043590-080c-3680-ba9c-f7dfe955f1e0 | -14.2944 | -60.37789 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec16f150-4182-31a5-b082-74908bcaf34e | -9.02467 | -65.68801 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 908852d5-e50f-3f7a-bb20-397b3cc14f24 | -9.65333 | -59.6414 | 2025-08-24 05:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73816a2d-a44b-394d-bf8f-9ce03cbbad14 | -16.48933 | -52.56017 | 2025-08-24 05:01:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7aff7ca-6f90-39e1-a492-388cc0703028 | -14.76462 | -45.37787 | 2025-08-24 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78c04ee5-20b8-3528-a509-c0541ae66429 | -9.52443 | -60.52211 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b81e2f35-17b2-383f-857a-1a235d2d0dc3 | -13.0493 | -45.23021 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59e9b7d6-7df2-3dcf-ab48-19eae706af1f | -14.76995 | -45.38279 | 2025-08-24 05:01:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fbd53c2-3cff-3d63-b243-f398e6698095 | -9.00245 | -65.70663 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c24b8e49-9afd-3cf6-96cb-3174e44a39fb | -9.94628 | -60.1641 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7135a7fc-302f-3385-939b-f762afa51c09 | -9.01703 | -65.69548 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c990d54-4b17-34f8-85e5-83837994c9ce | -14.76967 | -59.65211 | 2025-08-24 05:01:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04869c3c-a438-3b9b-9aa8-d582e55f1f78 | -14.49819 | -53.10191 | 2025-08-24 05:01:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bb5acf8-776a-34e2-afa8-5b8021b2f29d | -9.47639 | -63.13523 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 323c8772-593f-3ca2-8e6d-f09222e199d5 | -15.64949 | -52.71743 | 2025-08-24 05:01:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3fdd5cd3-81cd-385a-84b7-6dd5dd4b3528 | -15.067 | -48.52312 | 2025-08-24 05:01:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd0af6e9-48a0-3a83-9fc4-5cb059f016a4 | -12.95058 | -46.29103 | 2025-08-24 05:01:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3da7042b-ed72-3cae-816e-e08ae7e7c30d | -12.72054 | -48.13591 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4fb9d31e-c224-34a1-a3e4-bfeabb8238d7 | -12.73137 | -48.11643 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15114ab7-fdef-3780-8ef3-8ac4f6d97409 | -16.3898 | -49.64436 | 2025-08-24 05:01:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d6196380-b0a4-38e2-8ca4-56f1b75a656a | -11.53841 | -51.86172 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bb630c5e-2640-3b2b-b0b3-d1f0f3001345 | -9.00845 | -65.70775 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72ae9cd3-f8c3-327f-a036-43e06a9e7591 | -9.32728 | -63.19215 | 2025-08-24 05:01:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d2622419-0837-364a-a360-214d1091d0ba | -18.02394 | -51.08449 | 2025-08-24 05:01:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cd9ba000-4701-3bee-87f8-36c398671959 | -15.65915 | -56.43689 | 2025-08-24 05:01:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96093dc9-8dc2-336a-aead-c1fdc90d632c | -13.03251 | -45.22392 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4dce9aa-d956-32be-a238-ed078876f882 | -16.41591 | -49.94053 | 2025-08-24 05:01:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd766ca2-aede-3e10-9ac2-5ce5c9eab419 | -9.40113 | -61.96493 | 2025-08-24 05:01:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbb58954-0a34-3250-b479-775ab22d3adf | -15.31512 | -56.15534 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9748e969-c812-3f62-8ab6-1b2c9ddfd9e1 | -13.49481 | -47.02924 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f67d9ff7-adfa-37a8-a6a5-b8dec769cb6b | -12.73526 | -48.12323 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0e1f25ba-cd23-3946-a7fc-cc3b75cce549 | -9.0238 | -65.38567 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 881f1780-4cc1-3ef0-a324-f250fa18f395 | -14.79624 | -55.90452 | 2025-08-24 05:01:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f4f3ca7-dcfd-3b40-8313-d6193f25b63b | -9.02542 | -65.70639 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1c907529-cf1c-3d74-a3b8-28c052a3ef5c | -17.60509 | -44.30065 | 2025-08-24 05:01:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 27.5 |
| e927740e-bc18-37c6-9b7f-f65426ee1b06 | -9.5248 | -60.52216 | 2025-08-24 05:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0db106af-2f31-310d-8f81-66d21a5577ae | -12.72534 | -48.12555 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2972bc7-2ced-3c8e-bec9-6b603d3a7dee | -13.47314 | -47.01869 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f51bbe08-1452-31f5-bcb8-76135319e56c | -9.00232 | -65.69718 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07fa94bc-c546-3d20-ad37-a734e93b3128 | -12.73627 | -48.12559 | 2025-08-24 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da548fda-b66c-3a02-9bad-5164dc433601 | -17.61102 | -44.29572 | 2025-08-24 05:01:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9f713dfd-27e1-399a-abc2-8a01beb57c95 | -13.38381 | -47.52767 | 2025-08-24 05:01:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25536dce-72b7-386b-aeda-ac13161cfd32 | -14.80526 | -47.92674 | 2025-08-24 05:01:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 778420a4-45ab-39ab-88d1-855d4d1a4d17 | -15.30897 | -56.17268 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a548550b-34f1-331f-b3f8-b9c9cfda2971 | -12.99122 | -45.22701 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5dca741-0520-3b0f-b174-0350ebc4b18e | -9.03662 | -65.72283 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01924d66-9e83-3635-902d-ed94c1300249 | -8.99941 | -63.63263 | 2025-08-24 05:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 740ab8c6-318b-303a-8773-1483fdf87354 | -12.2035 | -47.11155 | 2025-08-24 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6791824-f427-3837-b832-7b397186c231 | -14.54746 | -49.11245 | 2025-08-24 05:01:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec00c3d8-7ddf-3436-b1be-f4b2ce9d7d61 | -14.80594 | -47.92109 | 2025-08-24 05:01:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 72ce24ae-0017-3a0b-908a-d0d93b7beec6 | -13.49315 | -46.90041 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 090d2f42-f93f-3d83-8c2c-dd1544a87716 | -13.04881 | -45.23428 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c650f26f-c142-35e0-8154-a1f824a711d5 | -11.53297 | -51.84775 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 058dd2fd-e76d-316f-8653-16baf6dd152c | -14.28347 | -60.37177 | 2025-08-24 05:01:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c107037-d4ea-3c0b-8ce7-6a6e61ff0089 | -15.11276 | -48.664 | 2025-08-24 05:01:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb557a18-63c3-3614-849f-956b27e771f8 | -9.00406 | -63.63684 | 2025-08-24 05:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8912c483-fe30-33c3-b0b9-c9ca928f6baf | -9.01513 | -65.69502 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2f7e291-14dd-3714-a3e7-563526927f61 | -18.39808 | -46.84291 | 2025-08-24 05:01:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 638d6567-8528-37d9-a5bd-5b5bfc90fd13 | -14.4715 | -55.94967 | 2025-08-24 05:01:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9a3eb5b-66e1-3f3c-a54d-4276fb123afc | -12.99116 | -45.2255 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 124f4a5a-c2ab-3721-9522-e034d957c194 | -15.32178 | -56.15646 | 2025-08-24 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63900c35-726d-3f25-8eb0-25d144b5a11f | -10.42045 | -64.43279 | 2025-08-24 05:01:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7c680d7b-3167-3937-aaa5-68a8fb6113d4 | -15.91197 | -52.21148 | 2025-08-24 05:01:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a87d6e8f-5151-3bf0-abaf-3618d5b9baa7 | -9.02638 | -65.71141 | 2025-08-24 05:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ab073fda-8894-3f01-bb08-d1b4885453d4 | -12.99017 | -45.23354 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 088e5d59-4bbb-3d3c-a41c-3ccd97b9a472 | -11.5317 | -51.85637 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 04180579-2c5d-3ee1-94a8-31d3ca6e8367 | -14.97912 | -50.18399 | 2025-08-24 05:01:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f314278-994e-351c-8e40-3cd7fb1882ff | -15.53479 | -54.76057 | 2025-08-24 05:01:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8032f32f-fdc3-3750-b2f0-401fd5ab869d | -12.5503 | -45.6188 | 2025-08-24 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a264702e-3c54-38d2-a4fa-2e236c6dce5a | -11.53664 | -51.84827 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f94e7c8-a93e-355a-b56a-a3eccd9e5a5a | -11.5357 | -51.90539 | 2025-08-24 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe2ca63b-9a7d-3234-9606-daab4cc236b9 | -18.39847 | -46.83907 | 2025-08-24 05:01:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0da366d-bd11-3497-9f2b-b6c13a9585fe | -16.79976 | -51.35082 | 2025-08-24 05:01:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 255593c2-2cbc-3db3-af50-23ddecf8e584 | -14.79658 | -59.6291 | 2025-08-24 05:01:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a8fae03e-a34d-38c7-89d3-d5a2d87e5c43 | -11.73626 | -51.69912 | 2025-08-24 05:01:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dfa3182-8a8b-396f-b50b-ed979ce566f2 | -13.47383 | -46.886 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cc87033-139c-344d-afe2-43f6b223dc34 | -14.7689 | -59.65646 | 2025-08-24 05:01:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f816d48-2a30-350c-99f3-686bed764c5b | -13.48829 | -46.89709 | 2025-08-24 05:01:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 562fe5d7-ef0b-32cd-831b-4a0394c3d92a | -9.45381 | -63.50515 | 2025-08-24 05:01:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README65.md)
