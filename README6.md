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
| 84382a4b-b810-3b61-af95-6f7d7803d0cc | -9.00145 | -47.44339 | 2025-07-04 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c780771-aed6-3322-8612-048b4e483cbd | -11.92673 | -45.38016 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 718600f2-4a21-300d-8134-9c16f91a3c5f | -13.44978 | -47.82082 | 2025-07-04 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b272a8d-82b0-32f2-bac2-468b3cc0bc71 | -8.85632 | -47.95511 | 2025-07-04 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b86adb00-0f48-34a3-bba2-592fa8357bf7 | -10.24993 | -47.67698 | 2025-07-04 03:49:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8537cdc5-5ee8-332e-af65-fd8f9aff675e | -9.79787 | -47.74615 | 2025-07-04 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f5555ce-3f96-3f40-a096-ce14f921e91d | -10.25295 | -48.15031 | 2025-07-04 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc4cbb9b-8487-3d99-a975-d5bb4b93c3b4 | -8.44745 | -49.63451 | 2025-07-04 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c7a49ad2-ff81-36f2-9678-caadeae308ad | -8.32752 | -46.29214 | 2025-07-04 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0ecbc8b-ee7c-3c61-a759-90741c8ada8a | -7.0985 | -49.16877 | 2025-07-04 03:49:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 32e0a612-fc21-3718-864e-e659733abb1f | -9.47708 | -40.2687 | 2025-07-04 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 69544fb2-7865-3277-8181-8a71b2139960 | -8.58734 | -48.20889 | 2025-07-04 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 06757b79-a713-3d67-ad54-4d53c38de10e | -11.86479 | -44.86783 | 2025-07-04 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4b085fc-27cc-3961-a3ac-943dedb41604 | -11.92408 | -45.39466 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 852bbb63-6278-3c0c-961f-772c73935669 | -7.94526 | -44.84918 | 2025-07-04 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fed261a0-4397-3b65-8d90-7bba1a54efbd | -13.69695 | -47.74859 | 2025-07-04 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b2cd60e-78ba-392a-87c3-ac1d08ee3f12 | -7.22442 | -43.09991 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f270dd90-0744-3aa4-8ac4-d2350ae9ad4e | -6.84988 | -43.30907 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eb8b8240-8aae-3f88-b3cf-c224d4fb68b0 | -8.99642 | -47.44642 | 2025-07-04 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57da8d69-5281-39ef-89d7-4195330f1cfa | -6.8831 | -43.21874 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4ead5380-8382-34c4-b9b2-a6aaa367db9e | -7.00017 | -43.54069 | 2025-07-04 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c5a595f-f64e-3b1f-aca2-dba88e9b37dc | -6.91078 | -44.00187 | 2025-07-04 03:49:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7e0ab71-19ba-3156-b624-cbab5d5f8f17 | -11.44967 | -45.11707 | 2025-07-04 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 152b6467-696f-3feb-9081-85e845076e94 | -8.99519 | -47.44606 | 2025-07-04 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0af87c23-5340-3fe5-a37b-7d464c81c08b | -11.46626 | -47.30235 | 2025-07-04 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b42568b1-babe-3119-a003-1babb5ac2176 | -10.6504 | -44.49113 | 2025-07-04 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c72b4b82-1c68-30e9-b879-f1ebf37104aa | -7.23299 | -43.10135 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f222fbe7-97f0-3d35-af45-1e718a9092ce | -11.54168 | -47.8671 | 2025-07-04 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6dcfde90-c094-3e2e-94a9-3082acce7dc2 | -10.64754 | -44.48155 | 2025-07-04 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f689f255-07d5-323c-a284-3f1f4ff5d094 | -7.95002 | -44.84797 | 2025-07-04 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7ef19ec-d94b-3501-b770-9fcc2fff2889 | -8.2151 | -44.93877 | 2025-07-04 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 135a951f-0218-38c0-bca2-da0005fa841c | -10.34552 | -47.29452 | 2025-07-04 03:49:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 681c2e7b-0052-306e-9315-48ac70ee7aa7 | -7.23007 | -43.09255 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 13ef6593-3373-3bd0-b173-87e72368fade | -7.23367 | -43.09732 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d88a91ff-18eb-341d-a317-943fc1812e78 | -12.42876 | -43.72535 | 2025-07-04 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 13d1b4f1-aa22-38e5-be6d-1a164d7ae2f2 | -7.07777 | -43.21991 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a2ef8e99-28f5-3d56-bb68-989e66c6a057 | -9.00265 | -47.44375 | 2025-07-04 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 982e86ed-3529-33f7-8c33-6f936fc6a1ad | -11.92585 | -45.38496 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e303c616-8178-3638-bbc7-86573d1cc5a8 | -12.92777 | -47.14481 | 2025-07-04 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27bf84fd-c6c5-3de1-84c8-59dc36e2c245 | -11.8664 | -44.85905 | 2025-07-04 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 976d3191-c933-3b2a-b7da-d3964c882082 | -11.93241 | -45.40126 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 345792a9-ea68-332a-849c-a98d63ee98f0 | -10.25218 | -48.15439 | 2025-07-04 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1542e39-3962-38f3-9663-b100d64d0292 | -6.99941 | -43.54509 | 2025-07-04 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 77f9557b-dc02-3cf0-9cf8-5c0984ec8046 | -13.23937 | -48.03133 | 2025-07-04 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12417504-b5f2-3931-afdf-93518762faa6 | -12.42942 | -43.72161 | 2025-07-04 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdb4ee77-2c94-392b-9f63-8309c8243fc4 | -7.07706 | -43.22405 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5332909-48a6-3984-a1e0-0041dac966e7 | -10.87464 | -49.54723 | 2025-07-04 03:49:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a14ca50-3bd5-3ac4-a1b1-65764b84c263 | -7.84576 | -44.21578 | 2025-07-04 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 820c6859-4c7c-3c1c-9077-dfcc88d9ac7a | -11.54098 | -47.87069 | 2025-07-04 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5808e51f-5ebd-3d69-ba26-55790337fbc0 | -11.93045 | -45.38584 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a8c62bf-4064-3130-a21f-68edf4065d73 | -7.91154 | -44.53859 | 2025-07-04 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9c29854-6ff6-3fce-a122-7e595a4034eb | -12.20267 | -50.93867 | 2025-07-04 03:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6d60b36-f614-3277-9575-cce17d8ebec8 | -6.80322 | -44.75649 | 2025-07-04 03:49:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24470854-2bf0-3abe-9ebb-424b8e06fda9 | -9.79861 | -47.7423 | 2025-07-04 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3537802d-574e-3833-8674-1ee2cdfe0f9f | -12.20918 | -50.94004 | 2025-07-04 03:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8e1e66d-2c26-358a-a8dd-fc513a691fa9 | -12.20724 | -50.94442 | 2025-07-04 03:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbd6eb98-6832-3c8b-800b-ecca6385ee4e | -11.86034 | -44.86701 | 2025-07-04 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45fa8b2a-949f-3528-9920-eee3d41fb7cc | -7.65808 | -44.34534 | 2025-07-04 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8b15a2c4-12f6-3a47-a42d-c85414ab24af | -10.24494 | -47.67609 | 2025-07-04 03:49:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffe107a0-cd94-3f36-a76f-3ff7910afdb6 | -11.93504 | -45.38683 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5244a83f-210b-3cba-bc7b-fd9321eed40e | -11.49534 | -48.07632 | 2025-07-04 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b53e38c7-1fd0-364c-80a1-11560065e85c | -10.24444 | -47.67576 | 2025-07-04 03:49:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71b7634b-b51b-3386-8af1-b2123ec28b1f | -12.16327 | -45.52947 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9c055fd-2652-3855-9c0f-68f05a136789 | -11.54102 | -43.24696 | 2025-07-04 03:49:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0831d1ff-05c6-33ba-b68b-2aedfb85f71f | -8.30437 | -49.07546 | 2025-07-04 03:49:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e66b76b-382c-3899-a4ba-cec400bb701b | -13.23858 | -48.03531 | 2025-07-04 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cd31ec6-43f9-3ae0-adfe-45655a8dc175 | -8.24086 | -43.74746 | 2025-07-04 03:49:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| be5e44a4-1ad9-303f-934d-70bb950e41cb | -7.94392 | -43.34142 | 2025-07-04 03:49:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d7a836cb-e398-33b9-bba8-2b19232b47d4 | -10.59421 | -49.45699 | 2025-07-04 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 27085567-53a7-3159-99ab-0d920f540c17 | -6.88815 | -43.2153 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d2242da7-42f3-3439-8113-c573f0ac656b | -6.91535 | -44.00266 | 2025-07-04 03:49:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dffa39e-13f8-3152-83fe-2f14dd77f922 | -6.72463 | -44.33488 | 2025-07-04 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9e65bbc-77e8-368f-86f7-5a6b0c27b8c2 | -7.07847 | -43.21578 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8643e23e-96fc-3102-9376-d1c57bf1cc6b | -11.00667 | -42.79536 | 2025-07-04 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd7f6839-d6c1-3b13-8a3e-1ba6405a8391 | -2.93887 | -40.09955 | 2025-07-04 03:49:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13fa6f4a-8865-3e38-8c1a-6683d8c10bb3 | -10.55523 | -49.13837 | 2025-07-04 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8c941d27-1e2f-3789-aaad-75aec5c3e76e | -7.94527 | -44.84703 | 2025-07-04 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78a73103-2fb6-3ad8-a3b2-d199f10086dd | -11.92034 | -45.38902 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f8f4006e-d992-3d08-abf1-1dbdc0915051 | -8.32809 | -46.28897 | 2025-07-04 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de97e0cf-fbdf-3553-86d1-cce1836a876f | -11.92692 | -45.40524 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61a16e6a-fd2e-3ae9-8e98-20ef3c119bdd | -7.96504 | -45.93812 | 2025-07-04 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc505ae2-2551-32a5-87f1-1b4d83fcf6f2 | -11.91744 | -45.37885 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2a57e72-547b-3371-976c-6c0199fffc71 | -6.99865 | -43.54946 | 2025-07-04 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f064537d-72b5-3f99-9534-e1d9d57441a7 | -8.49112 | -49.8588 | 2025-07-04 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af3fa9c0-23e0-3d6c-8570-2f3f3db5607a | -11.52801 | -48.95674 | 2025-07-04 03:49:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6721fcf-6d4e-3254-bf5f-ca294caf4930 | -7.8412 | -44.21496 | 2025-07-04 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 518c6196-177a-3441-8b5c-a8b1b743da31 | -12.57541 | -48.88277 | 2025-07-04 03:49:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ac03d0a-5f70-387d-aea9-e50c38fbd0a1 | -10.98886 | -44.50031 | 2025-07-04 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61ebad33-6969-37e4-a118-6fe6e4710854 | -11.93131 | -45.38111 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e77f8243-fce0-3bb1-a31e-d99b9666abdd | -11.93328 | -45.39646 | 2025-07-04 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ed0d682-6917-33c4-839a-576ed8e0b912 | -11.47407 | -47.92185 | 2025-07-04 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71a47861-6984-37a3-946a-cb8f68eac581 | -6.71993 | -44.33411 | 2025-07-04 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af4cdecc-b6cc-3538-a2d9-569211d75da1 | -7.09748 | -49.17426 | 2025-07-04 03:49:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 27.8 |
| e8f6554d-c76d-3032-9230-2e83e5721091 | -11.86561 | -44.86337 | 2025-07-04 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c44e05f-3c85-39c3-b40d-bf07507f6b0a | -7.30505 | -45.36631 | 2025-07-04 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d2f0c66-6aec-301d-80e7-e6b7fc52dbd3 | -7.22939 | -43.09657 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| c1388a25-f5c0-3ffc-89af-b5037a0cb924 | -6.7231 | -44.33219 | 2025-07-04 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81742f59-4311-3423-ac94-17db61b271b3 | -7.22083 | -43.09514 | 2025-07-04 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c9e49521-1076-3133-bfcb-a0f6dd200757 | -7.19557 | -43.42968 | 2025-07-04 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| be6c838d-4b8f-3d3d-9043-4f1c1b101ec6 | -11.45423 | -45.11793 | 2025-07-04 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README7.md)
