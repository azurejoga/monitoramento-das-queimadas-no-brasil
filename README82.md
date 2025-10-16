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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09d02d0d-c7f6-3202-89a9-ae3954acb222 | 1.82802 | -55.75469 | 2025-10-16 05:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e97d944c-4ae8-34d7-bf08-c2e8678ce610 | -4.11129 | -48.00737 | 2025-10-16 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d0b63ae-80ce-3b17-bae9-3e9017491479 | -9.22122 | -48.60806 | 2025-10-16 05:27:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c294e27-9f35-331e-9bb0-6809c07ced6e | -9.22616 | -48.60607 | 2025-10-16 05:27:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 79760c4b-fd9e-3a06-83c5-0ac5a1af50dc | -4.10337 | -48.01289 | 2025-10-16 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 678dd4c9-aae0-34d7-a34e-5f86727270cd | -4.11032 | -48.01414 | 2025-10-16 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| c2567b29-b573-3326-ab9d-2b5af47d88f5 | -3.83902 | -49.93382 | 2025-10-16 05:27:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a3e67e8-67af-3b2a-8f3e-41ee834c5237 | -4.61787 | -49.55895 | 2025-10-16 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c5f93be-4c28-3d67-991d-70384dd336b1 | -3.51326 | -52.49713 | 2025-10-16 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6dfcd1fc-8518-3304-860d-018cfeaba4db | -3.51466 | -52.49384 | 2025-10-16 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27ec7bbf-d30b-3af6-80b8-e7f37b50e2f3 | -3.8854 | -52.07568 | 2025-10-16 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3540d509-99e8-301c-a5ee-48aa3b400f37 | -4.10939 | -48.02065 | 2025-10-16 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 81ecf63f-0213-328a-a8b5-f836623cb231 | -3.51421 | -52.49692 | 2025-10-16 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c73439b6-74bd-3b6a-b33d-c99ba50b5ab3 | -10.12385 | -52.34543 | 2025-10-16 05:27:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c6a4fc2-d668-3688-a7b4-5f21f5d60464 | -4.10241 | -48.01963 | 2025-10-16 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a407f8e6-6957-3926-8a96-4970a3b00745 | -8.12007 | -55.28973 | 2025-10-16 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f5b713c-a15e-33a2-a4f1-6c293e24e8f3 | -3.88311 | -52.24385 | 2025-10-16 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e16cafc1-8700-32f3-ad5a-5d911ab6f826 | -4.29707 | -50.40326 | 2025-10-16 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f24679fe-3028-363f-8cb3-5a3bb0dc83be | -3.33265 | -53.24579 | 2025-10-16 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 670cfb0e-8b68-3121-9b36-0e754f46b91d | -3.51373 | -52.49408 | 2025-10-16 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bf2d0eda-6e7d-3fdc-9f79-525fac7cda57 | -4.28437 | -48.63018 | 2025-10-16 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f6a6b0d-96a6-3fb2-bbe6-5d3eac30ebc9 | -3.50941 | -52.4933 | 2025-10-16 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bd46f8ad-b86f-3dbc-b48e-60ce5f3776a8 | -3.07718 | -59.09366 | 2025-10-16 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e0f2b39-440a-35ba-b232-d66262b366a0 | -5.30423 | -49.5792 | 2025-10-16 05:27:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 455e2c2b-0e60-35cd-8df4-a025d77bfa7f | -5.48847 | -48.95 | 2025-10-16 05:27:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3fd16bb8-b547-3442-998a-111e11775d5f | -4.28272 | -48.59248 | 2025-10-16 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d789173d-cdb6-39be-a22c-35e693c653de | -3.87998 | -52.07504 | 2025-10-16 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 080cbddd-bf34-3a48-b674-d66e14147eb1 | -9.22921 | -48.6021 | 2025-10-16 05:27:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 59442a72-9a6e-36b7-8ffd-54a0114ff79f | -4.29771 | -50.39886 | 2025-10-16 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dd0e7249-f967-3709-b672-64753f912b92 | -3.20934 | -54.96428 | 2025-10-16 05:27:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84841662-4158-379a-8a0d-f1f277a85bab | -3.48184 | -53.45366 | 2025-10-16 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f351beb-efe2-355d-86bf-178a38bf72c7 | -3.84523 | -49.93459 | 2025-10-16 05:27:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2a6aacb-7c42-3473-b2e8-08a2be76f1e7 | -3.81608 | -54.07753 | 2025-10-16 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88e327c3-0e84-336e-917e-5b2934079d3f | -3.65596 | -51.75082 | 2025-10-16 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3447ff61-6098-325c-8c21-40639985e132 | -4.2888 | -48.62873 | 2025-10-16 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d86f2358-7d2f-359f-8b69-eb99e73cf025 | -5.30504 | -49.57353 | 2025-10-16 05:27:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ef0b053-b344-3033-8286-1a8c56976be3 | -3.87877 | -52.2362 | 2025-10-16 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5934f1bf-49ce-336f-b7bf-a38e7f21bc6f | -4.10772 | -48.03228 | 2025-10-16 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 5343d0ef-af3c-35c6-ae1f-5c286544d117 | -3.86577 | -50.05008 | 2025-10-16 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4ad6841-0931-3ba6-8edd-1450c7058473 | -3.66093 | -51.75518 | 2025-10-16 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf98ce9c-de16-33c5-aa9a-ce1cae9f0294 | -6.19052 | -52.73529 | 2025-10-16 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d98a949-cf97-39a0-a810-60906a4b7c9b | -2.6959 | -59.42863 | 2025-10-16 05:27:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7a75e2b-6dda-3ce3-99da-055a1c3e8df3 | -4.28205 | -48.62777 | 2025-10-16 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33dcb255-d065-360c-aa00-5ce4e8b2ae61 | -3.66144 | -51.75176 | 2025-10-16 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7008ee5-f688-34cc-8ced-276ffb565250 | -3.65545 | -51.75428 | 2025-10-16 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c7d9e4b-6a17-3fb5-a770-a46090d91a73 | -4.1007 | -48.03162 | 2025-10-16 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 63355c77-969a-351d-833e-f3fcadd0efcd | -3.67037 | -50.27429 | 2025-10-16 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f39272da-41b3-3e86-8ba2-755dd496ff91 | -4.10154 | -48.0257 | 2025-10-16 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2b4c1cef-d7a2-3bc6-ac1a-ff8b902a1bd3 | -4.30314 | -50.40405 | 2025-10-16 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 026a0bcd-d69e-3018-b6d5-968ac2c21e83 | -3.81897 | -54.07702 | 2025-10-16 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ab4e97a-89f2-337b-aba0-5f11632d6b8c | -3.66433 | -50.27337 | 2025-10-16 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22fc307e-ab4a-3b03-8640-d7698ee7dd9b | -4.28355 | -48.58654 | 2025-10-16 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a4c39a6-e5bd-38ea-b103-310a8ea47eb9 | -3.5363 | -52.70603 | 2025-10-16 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7793700f-1e45-394f-80a3-d204f6be3d6b | -4.12061 | -50.71717 | 2025-10-16 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 224b16a5-6a79-30a6-89ee-90757932b2a6 | -6.19584 | -52.73618 | 2025-10-16 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebd42c4f-90c9-3486-9e0f-c87c51da21de | -4.10856 | -48.02645 | 2025-10-16 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| bece5b5c-5391-3c78-b6d4-4e7edc5ceb91 | -4.28062 | -48.59029 | 2025-10-16 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 600a6cfb-31d7-3bc9-8997-e75c2653bdcb | -4.2815 | -48.58424 | 2025-10-16 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e3f337d-6168-31d3-a937-1105777cfc69 | -4.11999 | -50.72147 | 2025-10-16 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e87565a2-977d-3970-b34b-bfd4769cc2e7 | -8.11546 | -55.28908 | 2025-10-16 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef6dbfb3-2af3-35fa-87f3-f260e3e81494 | -4.30378 | -50.39962 | 2025-10-16 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 50c9676b-f365-3aca-9d44-0f45aada8137 | -3.88319 | -52.07534 | 2025-10-16 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6be228e3-e1bf-3b55-957c-47c05757ae29 | -9.22701 | -48.59916 | 2025-10-16 05:27:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ae27b2e6-c9d8-3120-9421-e4bb5f86e588 | -6.22983 | -55.63444 | 2025-10-16 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d05a74c-bc24-34e5-bca7-175cb21013db | -10.0185 | -65.05518 | 2025-10-16 05:29:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81ab2e0b-7039-3d6e-bbab-bd2a88d6235d | -9.57934 | -65.32651 | 2025-10-16 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b192f9e8-cdac-37e6-b77d-d3816ab4a7cd | -10.394 | -58.3804 | 2025-10-16 05:29:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a22014c1-6f0c-3a56-a821-9d79b530c4ff | -11.38007 | -61.21283 | 2025-10-16 05:29:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33666180-f598-3bd4-b6f2-70af6d693037 | -11.97692 | -63.12194 | 2025-10-16 05:29:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6619b236-84be-368b-af41-a628370223db | -11.76143 | -61.07309 | 2025-10-16 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67bbd7f4-a9b4-3b67-859d-5e90532b1fde | -9.55384 | -63.46631 | 2025-10-16 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2dad94d-b9a6-3862-abd7-ae4f9746037b | -12.17481 | -60.69314 | 2025-10-16 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3715785-9571-3d02-a1f0-63a6b1fec1b1 | -11.75399 | -61.07582 | 2025-10-16 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f774a93f-48ad-3468-836f-85ed3bdbda79 | -12.5953 | -62.08788 | 2025-10-16 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 071349aa-f035-34c7-8950-aaa5897fe56e | -9.92291 | -65.28802 | 2025-10-16 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbc2756f-35e8-3558-a557-9d5127730781 | -12.23697 | -63.60415 | 2025-10-16 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a687f003-458e-3d6e-b2e6-9459eb97b97c | -9.88998 | -64.249 | 2025-10-16 05:29:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0006954b-80b8-32b7-ab5b-c25218f33f59 | -12.70216 | -62.18954 | 2025-10-16 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c10c428d-d42f-3fb4-b0ae-0df6189ef3b4 | -9.58 | -65.32253 | 2025-10-16 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68d14018-770a-3848-b1f6-8b8193fed700 | -11.72927 | -62.29379 | 2025-10-16 05:29:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fbfa1c36-06e4-3d2d-bc55-2f0849f5b3bd | -11.87797 | -62.69122 | 2025-10-16 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 033835f7-3718-3f5b-844a-80ae9b5c58db | -9.82476 | -64.21618 | 2025-10-16 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60d82f64-3b20-319a-85e1-4c2e98fdb485 | -11.98164 | -58.06363 | 2025-10-16 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c4520f0-9d72-3d4f-977e-5bcff13a6b26 | -12.60394 | -56.51118 | 2025-10-16 05:29:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60de0a0d-4d0e-35f8-b481-954a54fd912a | -11.75743 | -61.07636 | 2025-10-16 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b395f4d4-f28f-3eab-a20e-56ee6fd280a0 | -11.81957 | -57.94464 | 2025-10-16 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e3bf830-4de0-3f07-b05d-23ff0a779cc1 | -11.97759 | -58.06308 | 2025-10-16 05:29:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 12d2f7d4-40ec-32e9-b429-8b20d89b6574 | -10.39788 | -58.38096 | 2025-10-16 05:29:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24a44581-61bd-3e91-96b5-b501eb8f312b | -12.23034 | -63.60306 | 2025-10-16 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 128872ca-ca3e-385c-abd2-ccfbd243c22b | -11.75799 | -61.07256 | 2025-10-16 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e629efa-10c4-3310-a6b1-c05890231f70 | -11.37723 | -61.20856 | 2025-10-16 05:29:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43f47905-26a3-3b90-9415-6ace1e275680 | -12.60814 | -62.07132 | 2025-10-16 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf9e6fdb-15b8-3357-8f73-d117484150bc | -12.35511 | -60.57283 | 2025-10-16 05:29:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c85d0818-fa6c-3114-9d8a-f7aefd2fc0e0 | -11.75455 | -61.07203 | 2025-10-16 05:29:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12cee032-7aa5-31b6-922c-c132d3fe7e59 | -13.36516 | -61.34131 | 2025-10-16 05:29:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e35495f8-6df3-3b69-9d97-4db3e947b383 | -11.86088 | -62.73542 | 2025-10-16 05:29:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72b8153d-eb8d-3d1c-bc69-54ae3ac1ca98 | -12.14078 | -61.53016 | 2025-10-16 05:29:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dd1c11e-a916-3d26-9b5d-c5ec6deb4e21 | -11.07735 | -57.88076 | 2025-10-16 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f7b116c-9718-3f52-8509-940951654d87 | -9.89058 | -64.24535 | 2025-10-16 05:29:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e459a879-59dc-385a-8ecb-e8dea2e97158 | -10.77442 | -62.08147 | 2025-10-16 05:29:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README83.md)
