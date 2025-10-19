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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a0dbeff-2908-3e47-9f62-3a7e64aca5d1 | -3.08888 | -49.22289 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 289bf3be-cfc9-39b7-bffd-6be4f3a2e9ad | -3.51758 | -49.94147 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e014926a-06d7-324f-a488-2e2b9801dd82 | -2.12955 | -47.39969 | 2025-10-19 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51f8541f-8505-3df4-8664-ca7b176acd03 | -2.70071 | -49.5501 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d70ffb4-2998-3132-9540-cc35de73e999 | -4.77528 | -45.89298 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4335eba2-4fd9-3447-a0a5-e6082d94523c | -3.5233 | -51.6628 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23c2b749-a5ec-3aeb-8917-2c6bd7f08b86 | -3.82062 | -48.65208 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b583d7db-50d9-36f1-a867-6d535fbad996 | -4.27493 | -48.57256 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05ff6cbb-be8b-3f9b-8133-7f7e66d46d03 | -2.81468 | -54.38693 | 2025-10-19 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a4a2047-7309-30c4-8f03-2f37edeb4ca0 | -2.43748 | -48.6202 | 2025-10-19 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4832a08f-e87a-3810-8e2b-fc4011319d1e | -4.78742 | -45.29729 | 2025-10-19 04:29:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a01ef59c-fa0e-3b9f-84ae-2f3146a405f8 | -2.70134 | -49.54613 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7e5421b-0b6d-3613-bda3-871e95a71377 | -3.37787 | -52.79782 | 2025-10-19 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31fe6719-a08d-386d-9a7d-f8f268ab3a85 | -5.47762 | -43.0289 | 2025-10-19 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13ec9963-304e-3f4b-9bb9-c7d8e2734013 | -4.27262 | -48.87877 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89f9dcf3-9834-3070-be64-bc39ee2c985d | -4.41204 | -49.76491 | 2025-10-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86437c59-065e-3d20-967d-bf0407e42b2e | -3.86453 | -49.81447 | 2025-10-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c0c906f-5350-3ced-8c09-6e070b6592e9 | -3.81472 | -51.32456 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffb72986-2e5d-3cbd-9177-9548933b3189 | -4.22607 | -50.62753 | 2025-10-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d543f15-fcca-3424-adf5-cced87f46025 | -4.23904 | -44.6908 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b009da60-0f05-3f37-898c-70f5ecb366e3 | -4.97408 | -44.61224 | 2025-10-19 04:29:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2769d169-516b-363a-955f-ef1d0302ab95 | -1.42549 | -49.09737 | 2025-10-19 04:29:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e6a499c-2750-3224-8095-3f497c8dbba7 | -3.10131 | -51.29388 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f96b597-9a08-3fcc-ba5e-3891577f63c4 | -4.85774 | -44.59183 | 2025-10-19 04:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b78949e6-cb63-38b2-b06c-e32c41a894a6 | -4.5859 | -46.29925 | 2025-10-19 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 325c9bf7-17a4-3f74-9c2d-3b2852871271 | -4.58978 | -46.29627 | 2025-10-19 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 999cc392-9eae-3820-a68f-97f58315e08d | -5.12303 | -43.12646 | 2025-10-19 04:29:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e70ee876-47c0-3a7d-856c-fadc2c662806 | -2.69844 | -49.5416 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa7fb641-24a9-3ea8-a5c1-d92caefb40e9 | -4.91616 | -45.70785 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02e95977-a619-32f4-97b9-f71bf8c11b4b | -4.23136 | -44.68608 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eca65630-0b3a-39e0-959e-46bd0c9fec32 | -5.45711 | -43.30019 | 2025-10-19 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5df8e198-9659-3f49-8b8a-b925abdc9028 | -4.30206 | -49.66 | 2025-10-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00957ca3-0ba9-3e1b-a210-920fb040fd14 | -2.69593 | -49.55748 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8dc90c4a-5f15-39e5-8305-e9a91ea82cbe | -4.06782 | -45.21554 | 2025-10-19 04:29:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8a05569-d067-35f3-b7c8-2908e36240d7 | -3.07214 | -49.2163 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d23cd74-df95-310f-bd1e-3685671ae190 | -4.22336 | -48.35639 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4bd5a4e-05d8-3b9e-83a0-05cdfb39d97e | -4.16147 | -51.09734 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 727f446f-1133-3953-9c30-0482345544c4 | -4.31215 | -43.01987 | 2025-10-19 04:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3d3c2e6-2d47-3e65-84df-2ec6307c2479 | -2.68369 | -49.5433 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23d807b2-a638-3e4b-a418-bc9c34441353 | -2.69491 | -49.54103 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a853e65b-3b12-3c08-b77d-2190a8effaf4 | -4.75748 | -45.42161 | 2025-10-19 04:29:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1268509c-145d-3ce7-b521-6ff7be333d7d | -2.85842 | -50.74058 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a717ab7-819c-3632-bcad-8d92eb08aa25 | -5.21609 | -43.74175 | 2025-10-19 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2928d8b1-6c63-3c0b-b019-aae7dc8ca765 | -3.03302 | -47.80886 | 2025-10-19 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c661ea85-d780-3f2f-abaa-e48ba501206c | -3.3943 | -54.06903 | 2025-10-19 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a0e19c9-8b36-30c4-a043-fdd6363d7ca2 | -3.45363 | -50.09661 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e89abd3-4c1f-34f3-a271-6766d6885d97 | -3.04206 | -40.1137 | 2025-10-19 04:29:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e695493-9524-3119-a8d9-9ae26bbca0a3 | -2.74173 | -49.38642 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 998af971-542f-3e7c-ac80-cdd06669e641 | -4.24022 | -44.68302 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be9165f5-785b-3c7b-9083-b15f25f91d77 | -3.35082 | -45.45101 | 2025-10-19 04:29:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f61c12aa-4fb4-31c9-89a0-d5068e813bbc | -2.44474 | -49.36228 | 2025-10-19 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c91802b-f406-39f0-bea6-248694f7cb2c | -2.86959 | -50.71926 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 08b9eb55-d146-3f99-b7a7-2c3b657cb20b | -4.842 | -42.74797 | 2025-10-19 04:29:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bac9b0b7-ab99-34f7-828e-3daada750fe8 | -1.48927 | -48.98829 | 2025-10-19 04:29:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7883325c-eafd-3ad3-9ee3-b179891ec8c0 | -4.30144 | -49.66388 | 2025-10-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0322a31c-7b63-3dbe-a913-a64ff1ec1611 | -4.24372 | -44.68356 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85db554c-872d-338e-b7b4-6c86362913a3 | -2.25251 | -51.91449 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ebf005f6-7c8e-3da6-a184-777ce274b74a | -2.96814 | -47.89917 | 2025-10-19 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8905caf-8a47-30d0-9437-df94ff28b5ee | -3.14092 | -50.24694 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db4c5bed-8bc0-3424-802f-53029d24aaa5 | -2.59313 | -49.49711 | 2025-10-19 04:29:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4217de40-1b96-3f4e-a4f3-65278078f3fd | -3.52312 | -49.9299 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57143fdb-e125-35ff-9c56-2399daaccfcd | -4.91972 | -45.98483 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1e26447-1100-3767-8819-4de78b3a2cce | -2.25193 | -51.9181 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 815b69c6-c8b6-3751-9e43-af1954272103 | -2.72685 | -48.34465 | 2025-10-19 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a112e6ce-6ab0-3946-b7f5-cf0b0a49a9e8 | -4.85421 | -44.59125 | 2025-10-19 04:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4df4ba86-a732-33c5-9f47-724d498c64c9 | -2.15313 | -51.96148 | 2025-10-19 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50032b73-4248-3b59-9707-40156867c6e9 | -4.3077 | -48.0635 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f11aab64-e7ec-3648-9e99-5f5353b6cbf1 | -3.81703 | -52.14352 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87783678-c8f3-30d8-a888-fee910af1928 | -16.7635 | -42.7714 | 2025-10-19 04:30:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 216.6 |
| ca44438a-d1cc-3579-bcd7-9ea5367f25ec | -16.7641 | -42.7467 | 2025-10-19 04:30:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 90.3 |
| d4e3cda7-adcc-3f1e-a737-ae8d37d25d3d | -16.7628 | -42.7961 | 2025-10-19 04:30:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 8056f734-0ca6-3da7-8a4f-bbb984ed8dea | -16.7435 | -42.7761 | 2025-10-19 04:30:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 451f15be-7f62-35d0-be04-c918b4e73ea4 | -12.4686 | -45.4232 | 2025-10-19 04:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 9d9614e6-441d-3b91-99ac-ab78a76385f6 | -8.6032 | -40.1834 | 2025-10-19 04:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 66.0 |
| c3ead9e8-cafa-3c12-a6ba-b4ab8148400b | -10.8891 | -46.0814 | 2025-10-19 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 2eec0849-18c8-3ed7-96d7-2e064a0d0dd1 | -16.7834 | -42.7668 | 2025-10-19 04:30:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| e2f95b0c-08cb-3a86-8188-d8131cdb7466 | -11.65381 | -47.31449 | 2025-10-19 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c692cecd-15eb-3fd0-a12d-82904aaf2ea8 | -6.37013 | -45.7542 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9f3f394-6053-35be-8538-4109d0b72438 | -7.40963 | -44.80727 | 2025-10-19 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6aa8fdbb-6042-3773-83af-958f12b25db2 | -5.43383 | -47.69127 | 2025-10-19 04:32:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db796830-98f4-3acb-bf29-f02d10bdf965 | -9.89548 | -47.65623 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bc125e8-5b45-34c9-9ca7-9ed4f02e6d79 | -6.72806 | -46.31995 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6a7ac797-29de-3e84-90f3-e5211c66b6c7 | -5.35245 | -47.21537 | 2025-10-19 04:32:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd23dc6a-1fdb-388a-9bfa-a3b5ff2f6031 | -5.05047 | -49.64928 | 2025-10-19 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d7708b6-6fdc-391f-9d43-018f966f6ce8 | -5.10105 | -47.79752 | 2025-10-19 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23e8b7a3-b1d0-306b-a99c-d258792f8967 | -9.69047 | -48.93827 | 2025-10-19 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25793044-ef06-31c3-8653-78265db7c53e | -5.43844 | -45.36676 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20117822-e6c2-3f7d-8bdc-4fa3d244cd68 | -9.22849 | -46.06648 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 90cee0a7-398d-3158-892d-2a805baa2c94 | -9.75826 | -43.9593 | 2025-10-19 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f2934df-ecf2-3c9a-b49f-167870d58046 | -8.25155 | -44.00639 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 920b7713-376c-3414-a26e-66fb79abe7a3 | -8.58235 | -44.5859 | 2025-10-19 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f60fbd09-ccce-3d0a-9fee-bf5467dcc973 | -7.04823 | -41.82402 | 2025-10-19 04:32:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 767e8852-98c4-3401-8263-02fcbe84bc0e | -5.37325 | -45.95105 | 2025-10-19 04:32:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c0809aa-2899-32ef-a76c-eaf56a9ef1de | -8.43114 | -49.58656 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62b99103-af11-3c7c-8b06-76a6b30a4be7 | -5.88071 | -42.76967 | 2025-10-19 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 45ec7b7d-b8f9-33e4-8777-dad574435071 | -5.55475 | -44.95376 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3072a23c-dba1-3b8d-ac2a-2d16bea022c5 | -12.01541 | -46.48414 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9d87cd4-575c-3a1b-a851-2b78ccc8a6de | -9.61838 | -48.60059 | 2025-10-19 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83c378cb-4461-3cd0-93d5-af3191109e14 | -10.94845 | -47.56589 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e49ace73-14b2-31a7-809e-fe2867c57b18 | -7.46361 | -42.74678 | 2025-10-19 04:32:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README42.md)
