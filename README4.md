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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb94d591-2a23-3d05-b151-c369c792c45e | -12.7054 | -63.0798 | 2024-10-02 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 160007a1-4a15-3b25-912d-a286b0004cbd | -12.8593 | -62.7826 | 2024-10-02 00:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 0a1a8c04-dd48-335b-ae32-de5809133048 | -12.8782 | -62.7815 | 2024-10-02 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 646f9875-2990-3935-9445-be8a7c68b41e | -12.8784 | -62.7622 | 2024-10-02 00:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 6f7d5c89-7121-374d-9b66-2a50c020b369 | -13.2173 | -48.624 | 2024-10-02 00:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 60b6bad6-d321-331c-8b3d-1646c36c3da5 | -13.2177 | -48.6019 | 2024-10-02 00:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 81e07608-b478-39a0-8da2-d88a94d8a5bc | -12.9167 | -62.7022 | 2024-10-02 00:26:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.0 |
| c6a2aa22-7f33-3fbb-84b7-e0278da78d50 | -12.9357 | -62.701 | 2024-10-02 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 211.8 |
| 4383e7ad-c63e-317a-a81b-66894b3a20ff | -12.9358 | -62.6818 | 2024-10-02 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 245.6 |
| ebb943ac-cd40-3a3a-9c3d-04d901f42753 | -12.9546 | -62.6999 | 2024-10-02 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 190.6 |
| 06e09e29-355c-34d8-b4ef-699feb0e3a82 | -12.9548 | -62.6806 | 2024-10-02 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 372.1 |
| e5fd9a39-8eb9-35fd-80b7-c73f459e5bdd | -12.955 | -62.6613 | 2024-10-02 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 74887d90-568d-3a5a-aac5-a3ed25a05775 | -13.5965 | -51.1367 | 2024-10-02 00:26:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 01a19173-c7eb-3946-8d0a-c8b044a6548d | -14.7986 | -48.7628 | 2024-10-02 00:26:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 864fbc76-d0c3-3dda-8cd8-a04c25049a26 | -14.9351 | -57.9432 | 2024-10-02 00:26:30 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 3e710ae9-97ef-3f84-9fb7-69f226196299 | -15.3708 | -55.8431 | 2024-10-02 00:26:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 6485bbb1-0070-31f8-b864-ebb8f22f386f | -15.3902 | -55.8409 | 2024-10-02 00:26:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 1f53148f-f271-3cc5-845d-6e31bddfe4ed | -16.6108 | -57.3398 | 2024-10-02 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.0 |
| 01d9e6c5-ded9-3efd-a359-39df65ca3121 | -16.6303 | -57.3376 | 2024-10-02 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.6 |
| 340ebebc-c32b-39d9-a8b3-0cf305da9f84 | -16.6306 | -57.3171 | 2024-10-02 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.4 |
| 2b4e0e2e-af6c-3378-a491-040589f58bd7 | -16.6499 | -57.3353 | 2024-10-02 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.3 |
| b9d8c6d1-c663-36ba-bb12-f9771538b26e | -16.6688 | -57.374 | 2024-10-02 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.5 |
| 96e195b9-51d0-3e84-a267-4d791facef77 | -16.6884 | -57.3718 | 2024-10-02 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 2d98c929-2047-3f7c-9aec-c1fbdc8ef744 | -16.6887 | -57.3513 | 2024-10-02 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| bd9de308-0645-353c-9545-c9c939b3ca47 | -16.7063 | -57.4718 | 2024-10-02 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.7 |
| 54775fa5-b2a6-32af-85ea-0ee81846ed6d | -16.7079 | -57.3696 | 2024-10-02 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 2483a525-b235-3059-a471-386f7b4235ea | -16.7082 | -57.3491 | 2024-10-02 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.8 |
| d43f65d0-d95c-3849-a9ae-7d0c77ad3aea | -16.7265 | -57.4287 | 2024-10-02 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 858532e5-a8aa-3c93-a056-da315196588f | -16.7269 | -57.4083 | 2024-10-02 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| aa9fb52d-a4ae-31e9-aee8-de1343becf53 | -16.7452 | -57.4878 | 2024-10-02 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 840be9f1-4682-3f25-a920-fd2cb02da352 | -16.7461 | -57.4265 | 2024-10-02 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.8 |
| 5c558940-b94f-3c49-b7e7-5ecaccbad66d | -16.766 | -57.4038 | 2024-10-02 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.9 |
| cc603b66-737c-36fc-bb33-3c4e87f6d3ea | -16.7663 | -57.3833 | 2024-10-02 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 3f4e8324-5e64-3015-9a18-250792365384 | -16.7666 | -57.3628 | 2024-10-02 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 9a93010b-8671-31b8-aff0-d6a927f2b8e7 | -16.7862 | -57.3606 | 2024-10-02 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 99e64887-7324-34a3-8c83-fc4e468ca84e | -16.8292 | -55.9152 | 2024-10-02 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 127.2 |
| eeabc543-6bd7-3469-9027-39ee793a0057 | -16.8295 | -55.8945 | 2024-10-02 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 169.3 |
| 5cca9738-2685-3b14-8551-621018c28665 | -16.8299 | -55.8737 | 2024-10-02 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| ba332daf-978a-3ac2-872d-b11b78768e1a | -16.8234 | -57.4789 | 2024-10-02 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| 8b0361ed-bf43-31ea-8b62-9d3bd2798cc2 | -16.8238 | -57.4584 | 2024-10-02 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.7 |
| 85b3a9b4-3009-37ee-a6e3-f11d50938553 | -16.8488 | -55.9128 | 2024-10-02 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 8d5f5db3-5d57-39d4-bfcf-95d3091df9c1 | -16.8491 | -55.892 | 2024-10-02 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 129.9 |
| 527c6638-2b01-3a5d-829f-bc1fef7704f6 | -16.8386 | -57.7628 | 2024-10-02 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.7 |
| 6d987d5e-be18-3c57-941f-23950bc98991 | -16.8684 | -55.9103 | 2024-10-02 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 75796b39-d531-352b-b13c-3b522d0e4dd3 | -16.8695 | -55.848 | 2024-10-02 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 08f6f0f6-3bb9-3abf-b682-aa9fdfc7fcac | -17.0612 | -56.0931 | 2024-10-02 00:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| fa0b0dea-86ef-340e-b31f-b9f584e0a7fe | -17.0705 | -56.7114 | 2024-10-02 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 629e8610-b0ec-3b9c-bc30-e45db370c50f | -17.0709 | -56.6908 | 2024-10-02 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 00bf0815-5fb1-370a-925f-e5d3794db0a7 | -17.0902 | -56.709 | 2024-10-02 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 326c54c8-5e1d-3659-9ae2-194775999548 | -17.0905 | -56.6884 | 2024-10-02 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 5ab781fe-a1b3-32e5-b88f-ae46f950653b | -17.1577 | -56.1844 | 2024-10-02 00:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.8 |
| b17f4792-17a3-3983-a6da-4499f4f86425 | -17.1581 | -56.1637 | 2024-10-02 00:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 123.9 |
| 6959232a-dd4f-31b5-9a33-3f5b60883b02 | -17.1971 | -56.1795 | 2024-10-02 00:26:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 4e0fabc8-57eb-340b-a2cb-d36a08a02d29 | -17.1974 | -56.1587 | 2024-10-02 00:26:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 39aa74d9-f6b5-3b97-a19c-749a376024d9 | -17.196 | -56.2417 | 2024-10-02 00:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| d2cf7a34-ca16-38ff-89c4-eed59d45f8a3 | -17.1964 | -56.2209 | 2024-10-02 00:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 120.8 |
| 9498d5cb-c378-38d2-aaf7-3d02e5ae6a91 | -17.1967 | -56.2002 | 2024-10-02 00:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| ded0870f-c0e3-38f0-8cad-bf1b776fec0f | -19.2317 | -46.8687 | 2024-10-02 00:26:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 302f4b91-f3bd-3201-a8b6-358fd811ab22 | -19.2323 | -46.8452 | 2024-10-02 00:26:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 126.2 |
| c3f549ab-0e72-30fc-88b1-10cc92740495 | -19.2519 | -46.8641 | 2024-10-02 00:26:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 132.6 |
| f3b53827-0224-3c8a-8afe-bf079edbe039 | -19.2526 | -46.8406 | 2024-10-02 00:26:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 114.0 |
| b6f2f961-798b-3e71-8cbb-5c790ba51cf1 | -19.7824 | -41.9894 | 2024-10-02 00:26:54 | GOES-16 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.1 |
| 48ed78fb-2e7b-3f00-8a37-7d87c5184782 | -25.002001 | -48.793301 | 2024-10-02 00:26:55 | METOP-B | TUNAS DO PARANÁ | PARANÁ | Brasil | 4127882 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ccbebcfc-44ae-3243-bfb5-50f99cab2fd3 | -19.9921 | -55.4728 | 2024-10-02 00:26:57 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 74.8 |
| eab0e059-b778-31c9-9dc9-384fceb45301 | -20.0424 | -55.9738 | 2024-10-02 00:26:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 90c544f8-2c36-3f03-b9d0-49e7c61f96fe | -20.5266 | -46.2783 | 2024-10-02 00:26:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 23071689-dc99-3c0e-84e5-2693c5160cd9 | -21.4175 | -50.9759 | 2024-10-02 00:27:04 | GOES-16 | BENTO DE ABREU | SÃO PAULO | Brasil | 3506201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| 000177d9-41b4-3a07-ad03-8ce42a2cf104 | -21.3456 | -55.6841 | 2024-10-02 00:27:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 8bd9916a-270e-37b0-8645-c4ba606b801b | -21.6275 | -50.796 | 2024-10-02 00:27:05 | GOES-16 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.9 |
| 2fe9825d-2a4a-3333-b92b-c8ccc3c86404 | -22.9006 | -45.1029 | 2024-10-02 00:27:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 146.9 |
| be0efd1f-44d4-3c7d-a5cf-259f7a5fb78f | -22.9014 | -45.0779 | 2024-10-02 00:27:11 | GOES-16 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.6 |
| a1e2344d-5777-35ea-982b-e3d21601e232 | -22.9454 | -42.907001 | 2024-10-02 00:27:46 | METOP-B | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 65a30012-7c79-302e-aad1-813939c1f04d | -22.9471 | -42.9146 | 2024-10-02 00:27:46 | METOP-B | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2ae1a2f4-dddd-350d-bc7d-f80d509f027c | -22.827101 | -42.698502 | 2024-10-02 00:27:47 | METOP-B | TANGUÁ | RIO DE JANEIRO | Brasil | 3305752 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 427436e1-bb27-395b-8961-3415f7d74917 | -22.6043 | -42.165298 | 2024-10-02 00:27:49 | METOP-B | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5a19c507-08b9-337b-a081-6009b480d30f | -22.606001 | -42.173 | 2024-10-02 00:27:49 | METOP-B | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a231e3a8-d6b2-3038-8a03-6e05ee3539b3 | -22.6078 | -42.180801 | 2024-10-02 00:27:49 | METOP-B | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2ae8e940-9b95-3def-a73c-35e3ae20eb4a | -22.616501 | -42.219501 | 2024-10-02 00:27:49 | METOP-B | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 906ef4e0-e6a3-37ff-a54c-6b851674f494 | -22.927299 | -43.721699 | 2024-10-02 00:27:49 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cf172907-bab7-3690-8cb5-c88d3810a8df | -22.9289 | -43.729099 | 2024-10-02 00:27:49 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d58c69f9-9984-3abe-824d-19f649aa59ff | -23.150299 | -45.073601 | 2024-10-02 00:27:50 | METOP-B | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 805d99f2-3280-3bc1-816e-1ccd7714060a | -23.5044 | -47.216999 | 2024-10-02 00:27:51 | METOP-B | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bf63fc4c-dc30-3846-918f-acdf38896f1b | -23.506201 | -47.2262 | 2024-10-02 00:27:51 | METOP-B | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b052f04c-8919-3c35-a210-c42847467cb6 | -22.766001 | -43.785301 | 2024-10-02 00:27:52 | METOP-B | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 896ad273-0a9e-3a38-8f03-b6d15e5dabfc | -22.767599 | -43.792801 | 2024-10-02 00:27:52 | METOP-B | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e2920f37-145a-36c2-94af-bc5b60826d46 | -22.7691 | -43.800201 | 2024-10-02 00:27:52 | METOP-B | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5a0756a2-f2d0-3cb6-bdb1-60e80362e6d4 | -22.743299 | -43.775398 | 2024-10-02 00:27:52 | METOP-B | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dfa4da34-2ffd-32cc-8b68-f0b9fdcdeae4 | -23.0625 | -45.3951 | 2024-10-02 00:27:52 | METOP-B | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f4984f55-5c3b-3ece-8010-b0e912f9ae8c | -23.0641 | -45.402901 | 2024-10-02 00:27:52 | METOP-B | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 54ddee2e-8a5e-32b4-9d2f-b8a270e74b73 | -22.7831 | -44.250198 | 2024-10-02 00:27:53 | METOP-B | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 63766e92-ea93-34fe-97c3-b6f83e4ce027 | -22.7686 | -44.230301 | 2024-10-02 00:27:53 | METOP-B | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df8d6c54-3f24-3ead-abd6-e5d773993c90 | -22.7701 | -44.237701 | 2024-10-02 00:27:53 | METOP-B | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1effdba1-1358-38b7-a70e-6be55f85f7ee | -22.6639 | -43.6936 | 2024-10-02 00:27:53 | METOP-B | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6317f1f-a81e-35cb-9f3a-2c8506331f8b | -22.665501 | -43.701 | 2024-10-02 00:27:53 | METOP-B | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5cd136ca-63a5-32d2-9d49-bf921d2c6854 | -23.2815 | -46.644501 | 2024-10-02 00:27:53 | METOP-B | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ada12cbd-a2d1-3275-90be-652ff0bde64b | -23.351601 | -47.004902 | 2024-10-02 00:27:53 | METOP-B | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aee90914-81a5-356e-9e9e-fddc959f3171 | -23.3533 | -47.013901 | 2024-10-02 00:27:53 | METOP-B | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae56af7b-1f5b-3af4-b879-e95690db6789 | -23.27 | -46.6381 | 2024-10-02 00:27:53 | METOP-B | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6da95f2c-dc2b-3af9-9708-5de33bf108ba | -23.2717 | -46.646702 | 2024-10-02 00:27:53 | METOP-B | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ef7cf73f-9959-3bb8-80fd-8b5ba99db087 | -23.3297 | -46.9445 | 2024-10-02 00:27:53 | METOP-B | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README5.md)
