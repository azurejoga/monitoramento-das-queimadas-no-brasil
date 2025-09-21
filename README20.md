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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e99d7c9b-a3db-3306-85ec-7bb9065ca5d1 | -28.28634 | -50.37402 | 2025-09-21 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 52330472-8266-3c47-88d3-3a84aeef5267 | -28.28614 | -50.3546 | 2025-09-21 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| dd3ab127-6691-3f09-bbb5-d502c0706c73 | -28.29515 | -50.36635 | 2025-09-21 04:14:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ae0ec402-0eac-3853-8bc1-3bdd16b7b995 | -15.2783 | -56.8555 | 2025-09-21 04:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 91d9e11a-5cc3-3319-87b9-c870c98ed576 | -15.9783 | -59.4069 | 2025-09-21 04:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0811854a-3e0f-3621-bfb6-0598d5aec892 | -5.09412 | -41.13881 | 2025-09-21 04:34:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b80bcdbc-fd66-369b-84c0-33dfd3499276 | -3.30291 | -52.58871 | 2025-09-21 04:34:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cf78e618-9cbb-31f0-ac18-c924049b07f1 | -5.42353 | -43.26281 | 2025-09-21 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ce0390b-4a1f-3e22-b851-a24b8c119be6 | -2.73484 | -49.54927 | 2025-09-21 04:34:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69e855c8-125f-3c79-bb26-62c4d777ff28 | -6.08619 | -40.99997 | 2025-09-21 04:34:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 707123d0-e3fc-3717-b8a4-3f6a03f1c2b4 | -3.39309 | -44.76139 | 2025-09-21 04:34:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a79b0cb-a997-3283-881c-7ba27b4bc55a | -3.69418 | -49.5517 | 2025-09-21 04:34:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dab395e8-4206-3042-b17e-a8bd659a66ea | -3.76006 | -54.82005 | 2025-09-21 04:34:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 03c8dd4d-5a43-3148-87ad-9ef1f9237c67 | -5.42286 | -47.16161 | 2025-09-21 04:34:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 404a9f81-c9a5-387d-9412-04410c35811e | -3.84015 | -55.60242 | 2025-09-21 04:34:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f253105-f6d8-3ebf-9ff5-209e911dd606 | -3.68429 | -44.17771 | 2025-09-21 04:34:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20a92c0f-8593-39f5-8895-11e81f029c74 | -3.80541 | -47.57118 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b97f1f8-752b-3fca-9e5b-3533531f5023 | -2.74541 | -49.55094 | 2025-09-21 04:34:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b16a52c5-86bf-3e4d-bb02-5ee8f303f486 | -3.30153 | -52.58892 | 2025-09-21 04:34:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e4f8f8e4-8ec3-3aea-a363-d91eea80fb37 | -3.59411 | -47.51642 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 848eb48c-7880-39c8-92fb-f7960a367844 | -5.41983 | -43.26499 | 2025-09-21 04:34:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ef4c4bf3-b296-32f6-a4cd-206645ca69bb | -5.63194 | -45.95785 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a11f093-7d95-3222-844e-3b9b760d2914 | -2.14524 | -53.65174 | 2025-09-21 04:34:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54f60350-5476-3814-a3b5-3f98984458a0 | -3.59391 | -43.91677 | 2025-09-21 04:34:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a89eb18-eecf-3a9a-affd-f0d54d3d6706 | -4.8011 | -47.28485 | 2025-09-21 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 992af49c-d27f-362d-9d14-af09b1cb94e2 | -3.20415 | -51.59062 | 2025-09-21 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 999f3352-d263-3792-aa86-07d95446ced8 | -2.60382 | -48.13815 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7563a95a-fec6-361d-a586-4633936bd2cc | -3.60131 | -47.51401 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bedd80f-b190-3821-bd10-7dd3fd25682c | -5.5187 | -43.86951 | 2025-09-21 04:34:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f8be8344-644f-36d6-914f-bd044d77f2a5 | -5.52314 | -43.86558 | 2025-09-21 04:34:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 09817a91-8366-330f-8a77-a6a107eb3564 | -3.62683 | -47.5251 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcba4382-745d-3751-acfc-1d9107d657ec | -5.84799 | -45.89155 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e0eb046-ae11-3e47-9247-61418b84fd3d | -1.12414 | -54.14556 | 2025-09-21 04:34:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| efdd716d-c91f-3462-825d-0d256bb11729 | -3.79989 | -47.5845 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 732b6b4e-8b18-3b84-9f59-a394bbc1c380 | -3.35274 | -48.39728 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb1c29c7-94ec-3e2c-a072-ac2148680eda | -3.35387 | -48.39018 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 206cb421-a5bf-307b-ac30-6e3ae1fd4f83 | -5.34686 | -45.00919 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eea70144-74c6-3115-a6ef-8a8bca1ecf53 | -3.76095 | -54.81462 | 2025-09-21 04:34:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e8af37df-59a1-3cba-815b-0194728fe29b | -3.05064 | -50.3423 | 2025-09-21 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73aef86e-bf0b-3f0b-ac9f-015c3845b289 | -6.08751 | -41.02344 | 2025-09-21 04:34:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 942506d5-eed8-3288-860b-beab6f173476 | -4.54576 | -50.87975 | 2025-09-21 04:34:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6d5c0a8-a015-37af-9e0a-dabbaadf6daf | -5.82282 | -45.89531 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c581d04-98f9-3dc6-bd39-8310c1726e66 | -1.12005 | -54.14305 | 2025-09-21 04:34:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5d4288f-534c-3949-afb2-1166721d7e29 | -4.80164 | -47.28138 | 2025-09-21 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ca17aa2-d773-3218-867d-0b9e5e880ab5 | -5.63536 | -45.95836 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b812af4-02f2-39ae-b406-495caac49055 | -6.08609 | -41.00277 | 2025-09-21 04:34:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 39f71d85-6cbe-3337-9436-20f2024e81a1 | -4.22438 | -50.15921 | 2025-09-21 04:34:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb747bcb-3c2c-3082-b464-b84624036791 | -3.59356 | -47.51988 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a4d5203-6936-3978-8612-ff32482dc9a6 | -3.72415 | -51.32852 | 2025-09-21 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1a685ef-b37b-38c8-8b85-5be21339dc36 | -3.45447 | -47.62967 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97d2e4a8-dc1b-3d2a-b82c-949d6349d7ee | -6.3077 | -42.36296 | 2025-09-21 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 29e34b6f-c140-37aa-9352-0b084425f073 | -6.30251 | -42.36937 | 2025-09-21 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 04e1ede7-7ef4-3f0e-9fbf-967e19127c94 | -6.01233 | -44.33367 | 2025-09-21 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3fffedc-7e0c-3013-8b3f-332874ebefb5 | -3.80874 | -47.5717 | 2025-09-21 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 341255b9-45bd-37aa-90b8-261db8527b30 | -2.83216 | -48.65919 | 2025-09-21 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 133dedd3-322c-3866-8a2b-97c589f13767 | -5.08966 | -41.13817 | 2025-09-21 04:34:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2a2064f1-7c83-3982-b361-0a2ba8c60b6e | -1.75689 | -47.17816 | 2025-09-21 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d88d5f2-233b-358c-869b-abb259c3aa69 | -3.591 | -43.91372 | 2025-09-21 04:34:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 380badda-05fa-3ef3-9698-0fa89b92ac00 | -4.41615 | -47.96601 | 2025-09-21 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fc7fde8-306e-33c1-830a-633bcbbd6cf2 | -3.64847 | -58.16246 | 2025-09-21 04:34:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46741197-f7aa-3626-a98f-d6b028720ab0 | -2.60718 | -48.13868 | 2025-09-21 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48069745-0ff8-313e-af09-ecd3c84354d8 | -2.62189 | -46.84004 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1cafcef-580d-3742-b701-2e9e8e684f71 | -3.76185 | -54.80916 | 2025-09-21 04:34:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 612f4301-ee02-3007-8f26-f3cad73832ba | -3.30895 | -48.71452 | 2025-09-21 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfd6b9f3-b110-3304-a2ab-13488b191506 | -3.51272 | -49.94179 | 2025-09-21 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48418f81-0e97-3b34-ad63-268cc0d87789 | -5.53064 | -43.86682 | 2025-09-21 04:34:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eee88354-4983-367d-901b-35e31d75eaf9 | -3.65449 | -58.16347 | 2025-09-21 04:34:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e8384cb-acb9-32cc-82fb-50f9ff11df32 | -6.01868 | -44.32793 | 2025-09-21 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6da871c0-084e-3fc3-a8be-bf78406d08bc | -3.98432 | -51.05878 | 2025-09-21 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9ef8489-9092-3717-adff-ca74b041659c | -3.65057 | -58.16069 | 2025-09-21 04:34:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 31db032a-8d6b-358f-9031-1ebac227e4fb | -6.01297 | -44.32937 | 2025-09-21 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fac10f48-42e5-3883-9fa2-bcf8d0b6d985 | -4.19765 | -48.55157 | 2025-09-21 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eac0fe55-687f-399d-b1ec-83f85cc3ce57 | -5.00425 | -45.17538 | 2025-09-21 04:34:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e097bd6-51b1-3d8b-bc47-543ed3adf863 | -5.00072 | -47.28756 | 2025-09-21 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 832f13c1-bd61-3001-9c86-0849bbdbe48c | -3.2945 | -51.60228 | 2025-09-21 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5885b18-428c-3727-a47e-13337989951a | -3.84062 | -55.59958 | 2025-09-21 04:34:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c41fdf33-f2d8-3a50-bf69-a981d1ae496e | -5.52557 | -45.72131 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c91b9d19-0370-3bfa-bf7b-dc4bc2ee4330 | -3.92791 | -52.20098 | 2025-09-21 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb366c85-7c0d-37fc-a766-9366b4eb94e3 | -5.62966 | -45.94995 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1734a834-d027-3476-be67-19c080b609de | -3.75613 | -54.8139 | 2025-09-21 04:34:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ea43660-0773-3693-aaa8-089ad10e91ad | -6.30356 | -42.36203 | 2025-09-21 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5b4a1999-d732-3df6-a9ae-b10e6e2d7335 | -3.98464 | -51.06123 | 2025-09-21 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 291756de-2d40-35db-9eb5-4e439c28d93e | -5.78142 | -45.34738 | 2025-09-21 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a30f19d-c9b4-3c99-bbe7-0aaeeaaafa6f | -4.82212 | -46.00687 | 2025-09-21 04:34:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8b4dea0-f13c-3239-b98e-b7de1e235002 | -3.5185 | -47.20377 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62d24b6b-0702-3c7f-b29c-8bf744639800 | -4.51253 | -43.52107 | 2025-09-21 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 730426ec-9b2b-3743-b25e-2d104f63d67c | -5.7891 | -43.63068 | 2025-09-21 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ead76745-5fe6-3746-b14f-d8c4344b478d | -5.68169 | -41.39716 | 2025-09-21 04:34:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6c218f95-27e0-3a46-98a6-c8fe0723ab78 | -5.82567 | -45.89956 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dbc17e6-1a22-3b00-90d0-99e377b31230 | -1.11936 | -54.14475 | 2025-09-21 04:34:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ff0a540-df84-367c-af6d-279abbb69f22 | -5.63251 | -45.95416 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 97df5ad3-becc-3112-aec4-ae0c2a43141e | -3.34993 | -48.3932 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 149be700-575d-3885-b74f-32906d7c257d | -3.35331 | -48.39373 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 682903ff-0c00-3f2d-9f2a-630dfed2da15 | -3.30613 | -48.71035 | 2025-09-21 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 424e8315-bd5b-32f6-93fa-de344b94e44d | -5.63651 | -45.951 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 47b7c0a6-08b2-3215-87da-2e6b9729e83c | -5.84456 | -45.89103 | 2025-09-21 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26f2dc94-d21a-36f1-8512-7864e3e9f244 | -3.36617 | -50.39693 | 2025-09-21 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2485542b-25c2-3b4c-a681-b2dd94f5d505 | -0.99052 | -47.06142 | 2025-09-21 04:34:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e5321c8-47cc-38ed-8c6b-445ba42b88f5 | -2.61585 | -46.85679 | 2025-09-21 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36dfabb8-bec4-3823-a05b-2c8dd139ea86 | -5.24901 | -45.34081 | 2025-09-21 04:34:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README21.md)
