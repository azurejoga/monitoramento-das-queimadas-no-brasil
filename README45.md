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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b2b95b7-0f6d-3599-8bc5-151c33693ba7 | -2.67859 | -46.84387 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4ac6c2-8f3d-3463-9a7d-bc1055e12bad | -2.1144 | -48.39205 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b25799f-9404-3c8e-8518-c40fd8c0b78f | -2.5709 | -47.57026 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f238262f-6dbf-3030-a878-d3ccafe6a85b | -2.36184 | -48.5304 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9df28090-1d71-34b3-a533-c3be2f553497 | -6.98613 | -39.65974 | 2024-11-17 04:29:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| df81052f-259d-36d2-afa6-1ec6c0804ec6 | -3.52861 | -50.24448 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2457c238-4715-341b-9c73-fe0d47a78dca | -2.13953 | -48.76137 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 441c3b47-0c41-3ef0-a0a1-ac5d0b966c9f | -4.19257 | -48.23035 | 2024-11-17 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 739d12f5-4f0e-3c46-aea0-d74d627b1d64 | -2.25432 | -48.32556 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee92b452-352e-37ed-b93f-ceece245d617 | -2.91116 | -46.85528 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2ff0d65-bc44-3aa1-9a76-41ca3d4a3a02 | -3.85645 | -46.6326 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c0ff318-fc3d-3320-b632-75dd86f223c7 | -4.1177 | -46.93882 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6a34b70-7a6c-3e02-b3ee-86b3593c7187 | -3.8949 | -50.07824 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf58a2af-32bd-3f89-8246-9887c4a4ad0e | -3.66406 | -50.20538 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3b5ad33-0615-385a-a6ea-8ba295322ec5 | -3.19165 | -46.53946 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 383e3cec-42c9-337b-94d8-608669678e2d | -3.58171 | -50.52539 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 868b27c9-55e4-3d54-9b65-03d765e83a94 | -2.0852 | -48.5318 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e59c91c7-9bf7-37f6-8a3e-db2e5048f951 | -3.84765 | -46.64543 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3e864a7-5fe4-313e-a0e9-25b966477e96 | -3.58467 | -50.53025 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0278ae33-1b2d-3ec7-a69f-281bf131e91c | -4.21427 | -50.69197 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51b39ecd-d69c-3257-a473-5846bf89ab21 | -4.06815 | -46.08448 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 986a35c5-cde2-342b-a98e-99672abf75a5 | -3.29871 | -45.51258 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5112ccb-592a-3cea-9b6f-4d4cabeda1cb | -0.95955 | -52.41711 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8936c5d3-d893-3182-a5c2-0c0a964f7d49 | -3.97333 | -46.71081 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df9869ad-20d2-3bbe-88e8-ef345e39621f | -2.71817 | -47.906 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbcda05c-3264-392b-b209-c3cffbc87236 | -3.94852 | -46.71758 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c72fdd7e-5c65-31f1-a877-51aac8d84a3d | -7.31423 | -45.27284 | 2024-11-17 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dea4b358-eefd-3bb2-9b7b-074ca76f6b33 | -0.83255 | -52.34454 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18b184c1-7541-3d3d-a3e5-6e5e20b6403f | -2.54193 | -46.32837 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6428df1-51f4-3f81-90a2-e201534eff95 | -5.39541 | -42.77063 | 2024-11-17 04:29:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b265547e-acf5-3b84-a50c-d838e26defcf | -5.85791 | -46.45354 | 2024-11-17 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a63e5ad-5c7e-31f8-b11b-549a8674f553 | -2.59736 | -47.55314 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f520e5d-ce38-3145-bfd0-380b3e419c32 | -4.70322 | -44.46759 | 2024-11-17 04:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9919a988-dbbd-31d6-bca9-e5710fd98478 | -2.21946 | -50.78173 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b53291c5-92b1-33b1-9a4e-72657b7f9d7f | -2.62019 | -46.02349 | 2024-11-17 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b07ea5dc-616e-3ab0-8ce4-d72e2c590484 | -2.83648 | -46.66045 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c70128ac-ac5b-370f-8263-3b4e477bc896 | -2.64078 | -46.82384 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 135831ff-bfeb-3738-a37d-7db13de5b3ef | -2.41202 | -54.62363 | 2024-11-17 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 190af1ac-3980-3aa0-8057-d3f3da5a6660 | -3.4629 | -52.19428 | 2024-11-17 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51d3b2f7-4dc6-3bbb-ae19-f36359ed69c0 | -2.10127 | -46.53869 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c17eccfb-1798-3c7c-a753-3eb629029147 | -3.25182 | -46.54524 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2f4513c-bf62-308d-922a-c9f3d1c0449a | -2.65816 | -46.2153 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| db1794b8-6a6f-3f15-847b-1d7b07294fd1 | -2.67589 | -46.86104 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4de30cec-5465-3ceb-90da-91b37d1f3105 | -2.63777 | -46.56276 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1f198c7-d7db-3801-8242-8b13f086e5e2 | -3.78868 | -46.67529 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9274223b-3913-3b83-8dab-2888ce866db3 | -3.96725 | -46.70632 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 191473c2-599d-310b-8ccf-f12cf0f60938 | -2.15375 | -50.20477 | 2024-11-17 04:29:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7542c8b3-01d7-3bbd-a8ca-2b114de59fe7 | -5.54633 | -46.47152 | 2024-11-17 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63031d28-e3e2-3009-93b8-5870fbe8c731 | -4.0379 | -45.47095 | 2024-11-17 04:29:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fa07bd9-edef-3d24-9452-5fb1471c8317 | -2.64263 | -46.53174 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ba642bb-dce4-330e-87b6-9fbc4d33e6d2 | -4.27128 | -48.2069 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a08da60d-9705-3b14-b9a1-cc081fe2fa22 | -4.00632 | -47.43236 | 2024-11-17 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e28f647-8b04-3270-92f1-ec4b58d51069 | -4.47721 | -48.10764 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 94266587-4750-3f4d-860b-60818bb9a4c0 | -4.39054 | -45.2765 | 2024-11-17 04:29:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66a37614-fbbd-3042-92ec-1367d1f0faba | -3.21772 | -42.08837 | 2024-11-17 04:29:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f903dce5-a390-39d7-acb8-d33af0f5a152 | -1.32549 | -51.87205 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 70e7ee30-ad1a-32ae-b14b-ab61376096e1 | -2.60344 | -47.55762 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4b05e5d6-4eda-3d73-9d5a-47c61591e58b | -3.11898 | -45.89862 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bc1e257-87d5-3dad-b1a9-030ebbfdf520 | -3.09677 | -45.97466 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f7d24a4-6449-3a3c-be4f-ca8062949610 | -0.40174 | -51.62706 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 008dd8de-648d-326a-b1b0-b8fb285b86fb | -2.17904 | -48.44278 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a8a21c1-3a9f-32e0-82bc-dc119e72e55e | -4.74294 | -48.12494 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d484484a-a4e5-39a5-b0cc-ca5afd20a899 | -3.81205 | -46.91566 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 216e5b75-2646-30f9-b027-3f6a25119a17 | -3.90183 | -46.14587 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c7c7885-ee68-36e5-a7ad-9db2f98e6f7d | -4.10934 | -46.90571 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaf5ef1f-342e-39af-a7d7-6f047267f859 | -4.10988 | -46.90226 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a668acc-5640-33c6-a84d-8e144ec7ceaa | -2.66653 | -46.85607 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ea541b9-1832-3ac9-bba0-e44fa5c11935 | -2.64246 | -46.83465 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d0c28a5-6523-3020-a0ce-c2091f37481b | -2.20311 | -46.3004 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99cb889a-1ab7-361f-b4ce-838e1ec87ced | -3.56851 | -51.64785 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2f922e3-4598-3a13-aceb-2619ec2513d3 | -1.71598 | -46.67873 | 2024-11-17 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46d301c7-87a7-3b69-9439-bfa4458e88dc | -4.10043 | -46.87603 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc530140-a1ec-39f0-a0e4-673b103e16e3 | -4.31012 | -48.60636 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41b2275c-a1c9-37ce-9262-a35b066a5950 | -2.36584 | -46.17292 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d22a9baa-82cb-3fb5-b504-162e7ff0bf7c | -5.71261 | -41.6474 | 2024-11-17 04:29:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9b50a31f-afeb-3f76-9d1c-764c16d78650 | -3.88069 | -46.60794 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d428c62-66d8-3846-8478-f1b9b27f40ac | -3.11516 | -45.98831 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e83a19f4-c45e-343d-af89-bede22b5b66d | -2.16312 | -46.40374 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6409c821-64a9-38d7-93d8-f054d00f7f2b | -0.78206 | -49.47743 | 2024-11-17 04:29:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49955e8e-8822-3ec4-81e6-bc5e59148157 | -2.35697 | -47.11669 | 2024-11-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a5e9f7a-d32a-31dd-85d2-8133884c99c1 | -1.37021 | -47.25437 | 2024-11-17 04:29:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d95f372c-1790-334e-b8dc-03d7f1d65179 | -2.81556 | -46.66426 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cc744512-5160-3e74-b74f-0a40c9f5c884 | -1.51739 | -55.3724 | 2024-11-17 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7432999e-cf2e-3c71-9a4b-a3dc9115f35f | -4.74403 | -48.11799 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62c28f7d-cf3f-3189-862b-fb0992df50c1 | -3.3441 | -46.30394 | 2024-11-17 04:29:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e9deb13-7375-34c4-affe-c8dc0f42d6a0 | -4.73962 | -48.12441 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1609638-5261-3c33-a77d-9c8a9bdca2fa | -4.30715 | -45.99022 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6284c110-51d1-3774-b704-ec0f8d9ce3b9 | -4.23138 | -50.68027 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7019b0cb-e23e-33e7-87c5-53a41eab181b | -2.15834 | -48.90807 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f51101dc-6e6f-3dd4-b14b-69d1fb3cfb36 | -4.22786 | -50.67693 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ad781d6-dcb2-31e0-8c0a-e0f70ced424c | -2.58524 | -47.56541 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 85651c16-f75f-3353-86ab-972f651535bd | -3.09622 | -45.97818 | 2024-11-17 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1973056c-5f63-3e47-a12c-5fd446010c5c | -3.89601 | -49.98212 | 2024-11-17 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9bdedf5-f29c-3ea0-9906-c0af0a474153 | -4.03769 | -45.8826 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f736be9-c6e1-33cc-a72f-f2c18d660139 | -3.96285 | -46.71273 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87ce8136-28be-3a04-9a1a-c4f49078263c | -2.02949 | -48.96877 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed55c7a4-fb98-3ece-b237-b7d80e4c0db0 | -2.09994 | -48.29779 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 757b7b76-8b35-3514-ab03-960451f70fb5 | -3.89177 | -46.62386 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03803109-a2fa-30a1-abc5-2cf45eb34f02 | -4.28235 | -48.20149 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab4688b3-575d-3ed6-bd5e-399e39613f3d | -2.1847 | -48.40676 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README46.md)
