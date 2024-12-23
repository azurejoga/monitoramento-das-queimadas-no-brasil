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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eea2998d-85d4-373a-a3f9-3b6e271f41f4 | -3.90326 | -47.00107 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd8fa868-b5b9-38ec-8770-60f91092092e | -9.18238 | -35.51376 | 2024-12-23 04:08:00 | NOAA-21 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 32e6dc4b-770f-3b62-9c22-f4a3cba7fb29 | -2.68864 | -42.69998 | 2024-12-23 04:08:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7354fcdc-2b5a-31ef-9006-62dd767c5ba0 | -3.09612 | -54.60684 | 2024-12-23 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f4c6858d-95f5-31f1-ae9e-85737d1276fb | -3.50763 | -47.1992 | 2024-12-23 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 26b0d80e-e0f6-3ecf-a668-1bb103556a3e | -4.05193 | -38.79151 | 2024-12-23 04:08:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b79dfed0-eb14-3c69-bfa9-e7907a1efd30 | -4.09746 | -45.30532 | 2024-12-23 04:08:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 82db7157-8d3f-30b6-ae3b-25bd4d4d1468 | -3.75195 | -43.48091 | 2024-12-23 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc1329a6-2a89-368c-a699-09607d6cd09f | -7.92515 | -35.19171 | 2024-12-23 04:08:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 6f2e647b-ac20-3e35-8296-6c5e4f3850da | -3.90258 | -47.00517 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e1f385f-d04f-3c96-82e8-f674a47e1bd2 | -4.15406 | -43.64497 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fc72c4c-2110-3d88-84f6-77eda651f567 | -2.79416 | -46.75345 | 2024-12-23 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adcec212-8853-3123-8861-765167e87c2f | -3.50828 | -47.19514 | 2024-12-23 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 65c55050-2b47-3bfe-9855-24aca29e5003 | -4.08383 | -46.80076 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 467a6e03-f59f-3c9b-a807-93a46f0a5f18 | -5.06102 | -44.23457 | 2024-12-23 04:08:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 513bdd2d-e43e-3f97-a01e-cbc6fef70159 | -4.08319 | -46.80471 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d408eec4-a9ee-3f26-ab6c-d7f951bc8cdf | -3.08583 | -46.56246 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02199011-d661-3ced-be63-b1b2b512913e | -3.91859 | -46.93493 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e21ff67-f185-3502-bab4-5995f82a27c1 | -1.19128 | -46.66701 | 2024-12-23 04:08:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe0bb7a4-0c03-3067-b0a4-8f78f02a6fed | -4.04612 | -47.03164 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c9a887e-b469-3dc1-a3bc-670f30cbe53e | -5.80907 | -39.07869 | 2024-12-23 04:08:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8d7559a7-1dea-3977-b8c1-48ef1e85e974 | -4.44669 | -45.93092 | 2024-12-23 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eb4ee157-cc6e-3e05-9cde-ada14de1e585 | -2.70693 | -45.56845 | 2024-12-23 04:08:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c0f5c54-9535-3ed4-92cd-4faef9c48bae | -1.6662 | -52.06136 | 2024-12-23 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4d6498ad-f4cb-3344-b297-421f77057565 | -2.42678 | -48.59616 | 2024-12-23 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d6ae804-135b-3733-ad64-59823efc99ba | -4.1844 | -43.63392 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 759016bd-43ad-3b60-bd5d-ed7faff53ebc | -4.1022 | -46.81992 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dcfc600-ed34-3a97-8baf-03e2ac92129e | -3.64271 | -40.47324 | 2024-12-23 04:08:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cf23f60a-caaa-3f3c-963a-9dd9e83cef1b | -3.575 | -40.97403 | 2024-12-23 04:08:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0638ce0-b43c-36b2-bdf4-60a5a30ca205 | -3.98176 | -46.0429 | 2024-12-23 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3fdb208d-7b4c-3679-91f2-a39db2029ef2 | -4.86993 | -37.82249 | 2024-12-23 04:08:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1f048e10-da85-31c8-871a-8c3835e2a43f | -4.08448 | -46.7968 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98d298c1-9cb5-3147-bbab-fef856002569 | -6.00573 | -45.42215 | 2024-12-23 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0d2d01c-c6b5-3ccb-8c0b-de84ff979e77 | -4.37084 | -46.27103 | 2024-12-23 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0630cf77-b9be-3639-8411-15f886b5fd50 | -4.18379 | -43.63778 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 098ea76c-0ab5-3393-bc20-3e7bdc37bf1c | -5.82578 | -35.48253 | 2024-12-23 04:08:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ded3042b-5b06-326a-ae00-fba62eb3fefd | 0.06231 | -51.10702 | 2024-12-23 04:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a49d15f8-728d-367a-bf67-6425a414909b | -6.93834 | -43.53598 | 2024-12-23 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2838601f-8cd0-36d5-b63f-742c4474c449 | -4.01601 | -47.05534 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 935762a0-acca-31d0-a69f-770915b0fd50 | -4.33144 | -44.19473 | 2024-12-23 04:08:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88135b06-bd78-39fd-8a67-21649da97eac | -7.92452 | -35.19627 | 2024-12-23 04:08:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 9094afb4-bfac-3255-9240-3c3bb9f62bc2 | -3.83831 | -46.68695 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d63943a-54a2-34d0-b889-b00691d32576 | -3.78544 | -47.11075 | 2024-12-23 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76bdedd9-6626-399f-997a-39fa4509de6d | -7.8361 | -35.22433 | 2024-12-23 04:08:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| ab81be1e-7c30-36a6-b2c7-c6bc3caf367d | -4.00899 | -46.33727 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc20945e-447f-31dc-a1fb-509f26e565c9 | -3.83892 | -46.68325 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b2fb9b6-395c-3f0d-aee4-5347a6559798 | -4.06243 | -44.10455 | 2024-12-23 04:08:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad063a90-a38f-3043-8125-919e497e68ea | -8.2623 | -35.57346 | 2024-12-23 04:08:00 | NOAA-21 | GRAVATÁ | PERNAMBUCO | Brasil | 2606408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 76d26d94-9501-3053-8985-8e5e8a0dd906 | -5.80965 | -39.07481 | 2024-12-23 04:08:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0349909-4980-3185-a5c2-6b7aa9f7a6ea | -2.55181 | -46.94003 | 2024-12-23 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdee8ac9-da8d-333a-8cd1-9e66a51c8e5b | -5.82205 | -35.47773 | 2024-12-23 04:08:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 20d9ecc9-6ccc-332c-a967-10b1dfc6ed3d | -2.81727 | -45.93319 | 2024-12-23 04:08:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d905fbd5-e228-32a0-9a60-a49d1349dbb0 | -3.87903 | -47.28078 | 2024-12-23 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e56e67a9-f689-30fa-9027-d94b1ea25c03 | -4.03191 | -50.05833 | 2024-12-23 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0d20f02-5bcb-3373-9b4a-b3965e16d082 | -2.71019 | -42.71838 | 2024-12-23 04:08:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e63c57a2-259d-34e2-a4e0-b710b6d4cb16 | -4.23281 | -43.78813 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef7270bd-b568-387a-84cc-fa2f81e90ebc | -7.00598 | -39.74291 | 2024-12-23 04:08:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5db24b48-6c0c-32cf-8830-ec8896c93e78 | -3.8369 | -41.56099 | 2024-12-23 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f0dabeeb-7e36-36ab-950f-63774c696228 | -3.54244 | -43.58784 | 2024-12-23 04:08:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a9b9ccb1-1204-3012-804f-3e7c8d5cb018 | -4.14935 | -43.65213 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 210a952b-eb08-3398-929b-42bd776dc2d8 | -4.55437 | -42.91842 | 2024-12-23 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5243d3cf-bdcb-3d67-8127-5d49a79284a0 | -4.04124 | -47.03484 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73558768-4b7c-39ce-acaa-44ab6c3f7c4a | -3.91666 | -46.89421 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61c0b529-e319-37ed-affa-12b08cc2050a | -4.18075 | -43.65702 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72e2a2d7-3148-35b3-96b2-058ac5701140 | -2.5908 | -46.86195 | 2024-12-23 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9977147a-f883-3ee4-9b67-a14296217f0b | -3.874 | -47.28429 | 2024-12-23 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eaa811a-0898-3489-9190-02e4b1c45bd5 | -4.43453 | -46.31787 | 2024-12-23 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15a5d463-a578-349d-baa3-dfaa5d425bc6 | -3.95112 | -46.41136 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a943b998-670e-3bb8-ae94-848b863d787d | -4.15632 | -43.65322 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1e160294-9e98-30d1-82ce-e3364ce50cc8 | -3.98301 | -46.34277 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30cf320a-5f0b-35df-9cc8-ca27e1351af0 | -4.06388 | -47.08372 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 792f40c2-02e1-30ad-a14a-8755448d6c59 | -1.62911 | -45.84645 | 2024-12-23 04:08:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64a813bb-edbb-382d-8462-8eee359f3f03 | -6.91004 | -43.53896 | 2024-12-23 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d9e333ea-172e-3c83-a67d-18e53323b80b | -4.02617 | -46.91521 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f1f2d4b-48fc-3815-aa0e-03a6cebaed38 | -2.68581 | -42.69578 | 2024-12-23 04:08:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4685d532-af77-33a6-b792-9fb87475b6dc | -4.03207 | -50.05578 | 2024-12-23 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0042df1a-89e4-3dcb-8d35-fc561799bb40 | -3.83953 | -46.67955 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75bba3ed-87d9-3125-aec7-0c75a3107ca0 | -4.07901 | -46.80398 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e309799-ebdd-3f6e-bd66-0ab433451fb5 | -6.63601 | -46.6477 | 2024-12-23 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 031078e3-27ed-3e58-8bc6-cbdaebe3a438 | -4.17438 | -43.65208 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f059d805-dfd2-3256-b8ff-15b68edcffd0 | -5.3568 | -46.22328 | 2024-12-23 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd07fb20-bdc0-394f-890d-8c1fa51b0a3c | -4.1756 | -43.64438 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e93e060e-4eb1-3116-bbec-f9144ada22fa | -2.27048 | -46.39647 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aaa9d179-9e5c-351d-9235-d22e48f83fdb | -0.20501 | -51.6057 | 2024-12-23 04:08:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7434d8a3-f0a1-3586-8cea-13e41d565764 | -3.01096 | -48.12121 | 2024-12-23 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9aedbc0f-5063-3dd5-a2c8-6e5c295272a8 | -4.01893 | -47.06418 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a92e4a4e-79e8-3d4e-9ab0-e3a9c49e3ea6 | -4.44752 | -45.92581 | 2024-12-23 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5464e672-c22f-35ce-8b19-cf48e52450b1 | -5.45251 | -44.81522 | 2024-12-23 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6623b30-0c75-3f53-919a-5066373905b9 | -2.26692 | -46.39196 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e752be08-97d9-3bd7-a2e8-b61ecec8e472 | -2.81324 | -45.93258 | 2024-12-23 04:08:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68eaed7e-eb8d-391b-adf6-adf7edad894d | -3.88999 | -47.02832 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 815357d4-2ea9-34bd-bb7d-d42f5e30dc35 | -2.11438 | -45.49955 | 2024-12-23 04:08:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03f738b5-4af6-38bc-9679-ce5b1ff712ac | -3.98244 | -46.34636 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2758ca85-1e6d-35ea-8ec4-efe98f33b231 | -3.80129 | -46.72073 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| cdee3f6c-15ab-3a78-ab09-dd3fb396aa6c | -3.79742 | -46.85484 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f81bb105-6b8a-35b4-b9d0-58c5491f4768 | -3.92281 | -46.93567 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c926f00e-26bf-3f8a-b7d0-a4ef85e67ede | -4.09913 | -46.62891 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f184da3a-22bf-317a-86a1-209768a02a94 | -7.389 | -35.27185 | 2024-12-23 04:08:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| d5c842a1-d043-3fa3-9ac1-7539eaf5fdfe | -3.89655 | -44.05506 | 2024-12-23 04:08:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e00e0383-313f-38af-bf27-638cc85b361c | -3.35195 | -47.10791 | 2024-12-23 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README7.md)
