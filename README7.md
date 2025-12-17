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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9148cfa-a5b3-371c-a013-8d8c439dd37a | -11.4162 | -40.77506 | 2025-12-17 04:08:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 092d16ca-4b1d-39df-9ba6-10e9fa4d6238 | -12.67083 | -46.76634 | 2025-12-17 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4bc4159-0d28-33eb-9444-2e040756e2dc | -11.73523 | -44.59447 | 2025-12-17 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28400925-9d5d-3fe0-9dca-c380686d5c45 | -16.27242 | -40.08743 | 2025-12-17 04:08:00 | NPP-375D | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c81c6827-d800-356a-8d29-cc0fa441f719 | -17.00744 | -39.77964 | 2025-12-17 04:08:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dbfeedc4-09e4-3237-b354-d1003d5dfc97 | -13.38371 | -41.87621 | 2025-12-17 04:08:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d652aa6-0308-3f24-a9da-33628f79a694 | -11.97269 | -44.49205 | 2025-12-17 04:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 632e028d-d860-3afa-a88b-ad89a6a743d8 | -11.75123 | -43.30742 | 2025-12-17 04:08:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 929bcc2a-d3be-355c-a89e-c3aa851c4cd1 | -14.4407 | -44.86604 | 2025-12-17 04:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8e063ea-386f-350b-9853-df8de2805991 | -11.82482 | -43.79485 | 2025-12-17 04:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd3eae4f-95a6-3dd9-9c39-5bcd52345189 | -6.5631 | -51.1126 | 2025-12-17 04:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3ab15ea2-f405-35a2-bc70-26bf0c51c300 | -26.77305 | -53.1986 | 2025-12-17 04:12:00 | NPP-375D | MARAVILHA | SANTA CATARINA | Brasil | 4210506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0b527fe2-9fa7-3789-9947-f4c49cf293a2 | -28.28361 | -51.49581 | 2025-12-17 04:12:00 | NPP-375D | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f353a5b8-f484-3422-a8f7-1ef0559e2c99 | -28.28492 | -51.49412 | 2025-12-17 04:12:00 | NPP-375D | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1ea7525b-7815-3a11-a765-690e3b092474 | -26.77186 | -53.20406 | 2025-12-17 04:12:00 | NPP-375D | MARAVILHA | SANTA CATARINA | Brasil | 4210506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a32f9449-5399-3f69-9cac-26d0ea1ce453 | -5.3634 | -36.83941 | 2025-12-17 04:25:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6ec25d69-61ba-3820-97fd-252bb906e397 | -3.55997 | -51.123 | 2025-12-17 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8c96d1f-5188-3295-92f2-a209566dd3da | -1.42035 | -46.06599 | 2025-12-17 04:25:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96a6a6a7-b8df-39fa-8da2-efb225f631d8 | -2.48501 | -49.31719 | 2025-12-17 04:25:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09e9fffd-c159-30d9-9e6c-1bb461694785 | -5.47188 | -45.40767 | 2025-12-17 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41719f6a-4c31-3ec1-8940-823ac265cae5 | -5.57997 | -44.89336 | 2025-12-17 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88c5e9c3-2edf-33bf-84c9-6395f00dd30f | -2.67206 | -44.93882 | 2025-12-17 04:25:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 76d0dd8b-c75f-3f03-af2e-ee8d8d7c5189 | -2.8333 | -46.73249 | 2025-12-17 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3e7df9b-c97f-3466-9ae7-a3199c9c8a08 | -3.65638 | -47.5529 | 2025-12-17 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf42e86a-8382-3709-a6c4-035c063ec9b6 | -3.34397 | -41.79531 | 2025-12-17 04:25:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8489cba2-f4d2-37a7-8896-71bf4f0d30bc | -2.79078 | -51.40385 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbed0abd-eec3-37d8-803a-5e08fb11ae58 | -2.75462 | -51.57501 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57b5ccfe-f1e1-3475-8943-25146e12c598 | -2.63192 | -45.66616 | 2025-12-17 04:25:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3fc5c98-59f8-3770-97f0-b524839c61c9 | -3.32768 | -44.37627 | 2025-12-17 04:25:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a22c7c7d-b54e-3123-bd47-ddd9fa36d057 | -2.37366 | -46.39788 | 2025-12-17 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb9fa06d-5565-3895-8193-0bcd445738da | -3.20162 | -43.18636 | 2025-12-17 04:25:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4cfe62e-d629-3fbf-8318-b7adc13fd0a4 | -2.68602 | -52.07846 | 2025-12-17 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2caec85-7c7b-3e15-9aaf-292eaa6c4cc8 | -1.92239 | -45.29748 | 2025-12-17 04:25:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 116915d3-c19e-3e30-a9b5-9e9a2fc13e28 | -5.41077 | -50.7633 | 2025-12-17 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 214fd981-d993-3443-81a8-525375f4a3e1 | -3.86961 | -40.45429 | 2025-12-17 04:25:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7f608d79-ddfc-36fe-9797-46deaaec4ae2 | -2.68783 | -52.07679 | 2025-12-17 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08c2baf3-541e-3795-8b18-377576fec45c | -3.14591 | -48.15339 | 2025-12-17 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00483543-9f9c-319e-af41-76c0f9044b94 | -3.17685 | -48.02773 | 2025-12-17 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f31d4e0a-717d-30de-9b9f-b037baf71238 | -2.88684 | -53.0152 | 2025-12-17 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7d5b169-b060-31c7-a614-3439b1bc04f0 | -2.22312 | -45.71787 | 2025-12-17 04:25:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 424fa1e3-9de8-3140-8488-f26ab076ccf4 | -5.10177 | -44.79816 | 2025-12-17 04:25:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3030b0a0-96a9-3786-a11a-6a931626f5ea | -2.63137 | -45.6696 | 2025-12-17 04:25:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c21f0eac-3273-3288-a2f1-5d29d355d794 | -5.58109 | -44.88625 | 2025-12-17 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f605693-19a6-38f4-9899-9a6c1fe5f9e6 | -3.47984 | -52.96042 | 2025-12-17 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca2df9c7-6819-36c6-a620-f0d110ba6dec | -1.41758 | -46.06199 | 2025-12-17 04:25:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d91ee9b-34dc-301a-8f62-a9e207c06d31 | -3.3558 | -44.56149 | 2025-12-17 04:25:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1497d2ca-ef14-32c5-bf20-a683722cbedd | -2.62037 | -45.22424 | 2025-12-17 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 9e2870bb-b759-38dd-9029-4daa10aec72d | -3.32664 | -45.41925 | 2025-12-17 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8160127f-e6f7-3574-8a65-35b59591daa8 | -2.46765 | -48.11432 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a2b768f-6bf6-350e-8dbc-eae0e77e23ee | -2.36694 | -47.67761 | 2025-12-17 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cff268a9-e5a8-3835-85e0-d2d62daa3936 | -6.68746 | -46.66136 | 2025-12-17 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95cc502b-46cd-3d0d-b13a-7bb0bb64917c | -1.95321 | -48.45703 | 2025-12-17 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cbdac64-56a0-30a8-85a9-9a4662a00764 | -2.80065 | -47.35263 | 2025-12-17 04:25:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0c6da6d-bc37-311b-b78e-8d7e377861ce | -2.88766 | -53.01025 | 2025-12-17 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e2cfe43-baa6-3587-9c3a-5cfbfdf57b81 | -2.22562 | -51.94921 | 2025-12-17 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8700bcde-b9c9-3f98-abd8-20a8c932c846 | -3.03798 | -51.55939 | 2025-12-17 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d874c5d-f06c-3357-b66c-b4a250068591 | -1.95256 | -48.46114 | 2025-12-17 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be1b9721-e0d4-353c-8649-abb21307de52 | -1.30524 | -47.25467 | 2025-12-17 04:25:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3d2b9e4b-8597-38ff-adad-7dd7dcd72a2b | -2.69524 | -51.64088 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86a4a5d8-3f76-382e-b11f-eccf9c44022e | -2.93023 | -48.23244 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccf4c892-b5b9-30e7-ac72-a30e20e35f5b | -6.68801 | -46.6579 | 2025-12-17 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5bc5b02f-a1d3-3376-9979-82d0d4fec572 | -5.32137 | -40.55178 | 2025-12-17 04:25:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e5016d4e-5cd1-30b1-9c3d-1bd198e46c49 | -3.20915 | -50.66458 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9758353-7b58-36c4-9fac-d16118e3d2f5 | -1.91731 | -45.24393 | 2025-12-17 04:25:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 030b5f1d-8f22-3528-8f32-7f5a7fde56ec | -3.33406 | -45.41727 | 2025-12-17 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00aab4ff-3a3e-3249-9356-63df34c61a2c | -2.90315 | -45.58571 | 2025-12-17 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d24e1468-db72-3e2a-aca7-ab3cf2868587 | -2.93149 | -48.22458 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 570f6574-e178-35b8-a171-e890ad3eb5f6 | -2.4558 | -47.60236 | 2025-12-17 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e0c2fad5-05fd-3124-8ebc-8bbffd721808 | -3.14242 | -48.15284 | 2025-12-17 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 10e109c4-1ac0-3372-afcf-bac15dd292a8 | -2.92608 | -48.23583 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d69e1fa3-733d-34bf-b9cb-d829ca58f978 | -2.68338 | -52.07603 | 2025-12-17 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99596711-f059-3379-b3e0-e881d8066372 | -2.47137 | -49.0366 | 2025-12-17 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18f594b7-f98e-371d-93e6-004968dff7f4 | -2.93438 | -48.22906 | 2025-12-17 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7a8cf9f-792b-3e02-9800-c3e72cd3ce16 | -2.77365 | -54.52915 | 2025-12-17 04:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3028139-3fa9-3aa9-8217-6fb99388b2de | -3.33021 | -45.4202 | 2025-12-17 04:25:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcdc6e56-79bc-3b3b-a43c-1919f467a18d | -1.82563 | -45.58842 | 2025-12-17 04:25:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f624fe34-4a9a-37fe-9117-b952ca244201 | -2.69389 | -51.64913 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5c8178f-787e-35a0-9935-5dc58b7cd440 | -2.84004 | -46.69018 | 2025-12-17 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa329d6a-c517-3ed5-b591-5f85eb292332 | -2.3964 | -45.75914 | 2025-12-17 04:25:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5e9d1a8-9594-3163-8b7b-b48be4a64fe6 | -3.87018 | -40.4506 | 2025-12-17 04:25:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bf8ab5b5-146f-3ac0-99c8-25a0146f124a | -5.50308 | -45.12132 | 2025-12-17 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf9c14a8-ca76-3813-b720-e18ae797d3ea | -2.03258 | -46.38377 | 2025-12-17 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e57a96fb-111c-393d-a53d-7b8ba92e54a8 | -4.33387 | -39.14831 | 2025-12-17 04:25:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 92453e1e-ef34-3939-9aca-999343ff6f87 | -1.33784 | -45.81522 | 2025-12-17 04:25:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbfda7a3-3ffa-37f0-a249-7c2b946394e3 | -3.66037 | -47.5498 | 2025-12-17 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5dfe6354-851d-3715-9166-5ed057c46ce7 | -3.65011 | -46.89309 | 2025-12-17 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30a77f27-5b58-36bd-aa2b-629013ef84f8 | -1.42368 | -46.06651 | 2025-12-17 04:25:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26587b28-376f-3358-ba4f-17e1160396d6 | -3.68037 | -44.68086 | 2025-12-17 04:25:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a052aa60-ea98-3df3-a0af-42c95c5301b5 | -3.90581 | -39.93609 | 2025-12-17 04:25:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 96ebd31b-86f5-36a4-ab6f-7274094ad993 | -3.65919 | -47.5571 | 2025-12-17 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa524509-7b18-39d9-b8b3-436fb7b87996 | -3.35525 | -44.56503 | 2025-12-17 04:25:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66749ed6-fab7-3796-ae5c-06bc3928a518 | -2.69957 | -51.64161 | 2025-12-17 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d1dc922-dc07-37ff-a22d-63f12e0b1dba | -2.48511 | -47.77343 | 2025-12-17 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2be04cf-bea1-38ba-9c35-37ae42f25b55 | -4.32934 | -39.14758 | 2025-12-17 04:25:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2b981206-5e00-3880-94bc-c6478d61f91d | -3.41826 | -43.16655 | 2025-12-17 04:25:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 43d0237b-1850-3dac-a530-246dc856bac9 | -4.30255 | -45.60813 | 2025-12-17 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c51ddcd3-731d-3248-8fa1-991ce37dde46 | -5.02884 | -41.28045 | 2025-12-17 04:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 99db5b24-4a13-329d-a082-92fff637b9ff | -5.57717 | -44.8893 | 2025-12-17 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8dc85184-b4da-3ef4-9fe4-28f3c51e2e39 | -3.34404 | -50.25202 | 2025-12-17 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 609822b4-51ee-3fd9-887e-d74969966c38 | -2.57029 | -45.32561 | 2025-12-17 04:25:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README8.md)
