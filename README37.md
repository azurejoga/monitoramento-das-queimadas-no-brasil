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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e91ac3c-4afe-3f94-94f7-c0cd4d5e7563 | -1.60266 | -52.25943 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0409ac4d-2280-3402-886e-608ad45e9f39 | -3.24094 | -54.23436 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 723afb9c-0ae7-3754-ade3-86eb63b9c7de | -2.0902 | -50.34613 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2b62748-156c-3a21-b9a1-444dee49f49b | -3.7502 | -44.56878 | 2024-11-22 04:36:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a45612f-3a31-3e36-aabb-8d2ce9b3dd7e | -0.81136 | -51.59739 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36cc7dbb-c5e9-3648-ae16-97475c9cbe35 | -4.00836 | -43.24937 | 2024-11-22 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7a3b17f-1a72-3fff-a6b5-495013cd7fb3 | -3.29134 | -49.1922 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b4861442-5fbd-3476-b2cd-4b6535c67c22 | -3.90116 | -40.97586 | 2024-11-22 04:36:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 39f4cd97-0f4b-3dba-855f-196557c878fe | -4.02303 | -43.98804 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73cbdf9d-8d65-3eac-89b4-363759a48c86 | -2.19151 | -48.56133 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d3701c8-cdec-3d56-a766-100253d2e34e | -4.57569 | -48.01978 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f02897f1-d2f2-3eb3-b54f-4e66c7ad8a71 | -3.76077 | -46.11643 | 2024-11-22 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aada62d-f316-38a3-9b0d-8887d3236b03 | -1.42772 | -46.01617 | 2024-11-22 04:36:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38086280-4b88-36f8-8c49-5c230c855bf7 | -4.62772 | -44.23003 | 2024-11-22 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6612dd76-efa7-3700-927c-e111acf4fa0e | -1.24395 | -51.75142 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c81f0ca3-22f1-3192-9ea9-15d293659db3 | -0.67265 | -52.33516 | 2024-11-22 04:36:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08823df4-1a8d-360b-9e69-9ae76fbdfd09 | -2.69661 | -46.84871 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4a50015-1848-392e-9355-f505c050caea | -1.22692 | -51.73985 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 298d31b9-d61d-3828-b505-49370d4f0ca9 | -2.22671 | -48.38052 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7afe255-1bc7-3629-b841-117c89642e4b | -2.4035 | -46.02675 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a27990af-5652-3835-93eb-bc75f9c2fbd0 | -1.24799 | -53.36583 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0bde46a-a7a9-3a9f-be82-ff27dc8d6241 | -1.73246 | -52.71728 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7ae899f4-4249-3e7c-b7c7-61666c76357e | -0.00143 | -51.24744 | 2024-11-22 04:36:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87779d55-cc03-3401-9fec-663ea1a7b940 | -4.74971 | -48.08274 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37a7d62a-badd-383e-9f42-d3b6edbccf42 | -3.66417 | -51.56987 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f6b9495-2273-3fcc-bee5-98eb2aae7d9b | -3.13155 | -45.90437 | 2024-11-22 04:36:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8c9447b-6bca-3c5a-ad0a-4cde6e97b535 | -4.36541 | -48.49651 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| daf78a6d-02a0-3bcb-afc3-660c5a178686 | -5.77767 | -46.4327 | 2024-11-22 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef709ae9-14b0-3c81-846d-ca60d577532b | -2.50202 | -51.96132 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67d50f88-ebe2-3825-bf1e-6989b523a5f7 | -2.70728 | -46.23684 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0aa63bc9-e78b-3ed0-a0e1-948f01db1009 | -3.24191 | -54.25432 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 53729459-4492-3602-8ea3-114912de7ef8 | -2.62458 | -48.18186 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d47ecbf3-bee6-3369-9f06-a723abf90b2a | -5.44424 | -45.58751 | 2024-11-22 04:36:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cd978c7-b3b5-3e0b-a80d-6832e5869df2 | -2.95371 | -48.33603 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1334255d-f511-32f0-a535-a1710386a923 | -1.63237 | -52.6647 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 56102e79-00f8-336c-a5b9-2720041c9401 | -4.05192 | -53.92361 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9526518f-75b4-3d53-85c4-567446a434cd | -4.2897 | -48.24366 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1535498a-1967-3e0b-b6a2-ce8dc6f34bc6 | -3.00733 | -51.30478 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f53fd3c8-c669-38a2-b7ab-22abd1473dc7 | -1.5407 | -55.52356 | 2024-11-22 04:36:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2383068e-6765-34d5-8a65-8cca6b5bf447 | -2.95015 | -53.72109 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81688d5c-91b1-361b-892d-5906a031fb4f | -1.30509 | -51.74203 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83d66556-9940-3483-aab0-5d7a8b9d6887 | -2.14073 | -53.77466 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f147b76-8941-3629-b4cf-0ff8fd7ef21d | -3.14437 | -53.13724 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40ebb596-ce4f-3ebf-8405-fa6a22d9605f | -3.84737 | -52.35395 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0418ac83-c0cc-3993-b3cc-0300f622de42 | -3.32295 | -54.09757 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| db59ff0d-ebc1-3f16-8943-edb4ab1b60ea | -3.25574 | -54.24843 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e65bf6e1-7381-3224-aa79-1f1e2ca41f14 | -3.50441 | -53.79865 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdacae00-d127-38ce-a47d-522ea52add52 | -1.42557 | -51.11863 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| baacf605-0cc2-37e5-8091-a998c5b8bf9b | -2.751 | -54.09908 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3767a5d1-3b80-351f-81d9-c583a0215cea | -2.6179 | -54.01626 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6944070a-4b2a-36d1-97d8-7fcfe9d245fd | -2.21028 | -50.69328 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c68d3d31-b508-3b1c-9d59-d2ed539c922a | -1.9442 | -49.52304 | 2024-11-22 04:36:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afe4ede5-722a-392e-b546-d9c1212683b9 | -1.25389 | -51.75607 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 73707142-41b3-3733-89fc-f7ce4e01ddf3 | -4.56056 | -48.53025 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f1dabd9-cbc2-37b2-9740-5dd87b48b244 | -1.15802 | -53.3806 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07e6ccf1-b9a3-3867-84d4-485d0c9a8a04 | -2.83827 | -51.82411 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 000c8813-e523-3d25-b109-6eca9ca81c1d | -2.70196 | -46.08644 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a15f2260-fcf6-3561-90df-4220f366946f | -1.09671 | -47.50536 | 2024-11-22 04:36:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6413a5a8-8dd7-37a2-a8d5-394bb659c3d5 | -2.69739 | -46.25483 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3688ada7-82ed-3638-9d1d-ab3da1928f20 | -2.21879 | -53.73407 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d232d973-1646-33ea-8902-8228521dd43d | -4.40746 | -44.11985 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d4f4a3c-21b6-3853-9434-08a9b0dfbe3d | -3.84438 | -52.34905 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1d4bc6b-634c-354d-874c-eb3aa4f80ca8 | -1.91465 | -46.44559 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b7d7877-125b-3148-bca9-df08c0e194d6 | -1.59413 | -50.44503 | 2024-11-22 04:36:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daba0382-75b0-3c56-835f-918cfa4b0754 | -1.27286 | -52.98191 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 08cdfbcd-15d3-38a9-825f-ea5e3edbddc6 | -3.46351 | -45.91059 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b18ac2cb-965b-387c-8b3f-1c04ae7a0c50 | -3.5027 | -54.72082 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73809424-6cfb-30a7-9e04-57e4ca9d0404 | -2.21115 | -50.40232 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14d9938a-1d52-3098-b0f3-1aeaf433bdea | -2.55153 | -46.54122 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b42d0f8f-ebaa-3a27-9cea-13a4e4e50774 | -3.23579 | -54.25756 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| ad1efc8a-1008-3dc3-96f2-28db8d7c5a1d | -3.04345 | -54.8505 | 2024-11-22 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c4c59eb-3096-3464-a52d-a5618e1a7829 | -1.79238 | -53.6377 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bb513207-3f08-3c6d-b7b8-2efddd072bde | -2.94002 | -48.01247 | 2024-11-22 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3fccd91-78d8-3f98-aa42-4de406e0e639 | -3.22217 | -54.23549 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 283ea552-fd0c-308e-87cd-2c45ca817d2e | -5.47905 | -44.85526 | 2024-11-22 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2dd6f21-85b6-3281-a331-4cd560d30af2 | -1.71785 | -52.48624 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 36c8b9d3-987f-35b1-b913-fbe588328c33 | -1.71404 | -52.48564 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2d8e605c-3e50-3f40-a611-219cf317025a | -1.10081 | -53.18819 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8401f5b-457b-3473-a89b-0bd1964f2ba7 | -2.21194 | -49.86984 | 2024-11-22 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68689ae9-1423-3e9b-b50d-d2864bcaa2ef | -3.85405 | -52.35937 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 39ff26e2-7bcd-3774-b6e4-b9bef17ee132 | -4.68879 | -40.69042 | 2024-11-22 04:36:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1af2fd1a-6115-374a-a49f-08a481e8dc3d | -3.31291 | -52.86232 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ef662f0-1db7-3ad2-8850-b6f33c4b6593 | -1.91383 | -53.34641 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ffd5b22-ad4a-311a-9a45-814f5f81e8e1 | -2.7027 | -46.22047 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe978d21-7501-3407-aea1-fc83cf4c84ef | -1.21155 | -51.74185 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4483b2fb-34fb-36dc-afad-98a47a4009f9 | -3.28758 | -53.85141 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c08353f-a57e-37a4-9b8d-b7215f87d78a | -3.75062 | -52.32661 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 187ad759-a756-3a4a-b2ec-4b27f368da6c | -3.08273 | -45.77394 | 2024-11-22 04:36:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e057ae2-4f15-3146-bb02-d19b009c8749 | -1.0617 | -48.7643 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4b3073b-aebf-39c6-9d8c-7ac01862b2f7 | -6.38161 | -47.14232 | 2024-11-22 04:36:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d497b90-7c49-3f6d-8f3c-aed2412b183a | -5.95283 | -48.0547 | 2024-11-22 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfd07ce7-d3a0-337b-bdd5-9b277714efc0 | -3.1492 | -48.10849 | 2024-11-22 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 772ad94a-2765-3a63-b14a-cf8b340f61d9 | -0.81746 | -47.18422 | 2024-11-22 04:36:00 | NOAA-20 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e4b21c1-be25-3e0e-b422-47efc2e04e68 | -3.2342 | -54.24918 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b7a94298-057a-301c-8a0c-78a508d26da8 | -3.23468 | -54.23749 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| ffd1e8a0-9b8e-36a9-b2d3-25b0d88ea8c7 | -2.43559 | -46.54253 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a6c7e14-0b9d-34e3-b663-a3f66071dfd9 | -2.69616 | -46.07763 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88dfc832-337c-3ca1-9e65-04c4a9f608c4 | -2.81767 | -54.02882 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4b00fcc-7385-3c88-91dc-2b019e6a7090 | -0.81183 | -51.78878 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0bbba026-f01e-3158-9b99-41bee2c0db5a | -2.89184 | -48.2771 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README38.md)
