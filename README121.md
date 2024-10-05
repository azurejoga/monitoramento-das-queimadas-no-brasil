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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a32b37d-79c8-373b-9e6a-7c135e42f929 | -16.6215 | -55.91064 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7d3c4081-3260-32e7-beb3-182c9b29bd8b | -16.82105 | -55.90388 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5e9e2846-e60c-3aef-9adc-6d0497ac6a2c | -16.81729 | -55.90316 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1f171c1a-1acb-372f-a72b-82bc2b51d4bf | -16.81644 | -55.90792 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5034a648-cee8-3273-b541-da16adeafa09 | -16.81437 | -55.89769 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 58fde627-8408-373e-be6e-c3d60cc08bf8 | -16.81352 | -55.90245 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0fb4ef26-d0f7-3fff-93d8-b130e53ba5b2 | -16.69167 | -55.88688 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| aedd0c6c-0653-3173-9c63-ef8c92376298 | -16.68864 | -55.92575 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b24eb16e-947c-3735-8561-ebaf9d93fbd3 | -16.68384 | -55.48873 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 270e2608-ad87-35c5-8090-ac101c6140f2 | -16.68307 | -55.49313 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9a86bc4d-a62f-380a-8ff1-e690eee242dc | -16.67987 | -55.90925 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 33caf3c1-853c-3ffe-b1f9-53e1ed4b4b94 | -16.67861 | -55.49685 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 529fb900-1dfc-369a-b5f8-3a4e4262e5af | -16.67567 | -55.49185 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8af56d6c-a160-31da-9b44-4f353d7dd725 | -16.67347 | -55.5481 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7c896ce7-274a-3a9b-a540-66939bb2365c | -16.67197 | -55.49125 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 45f4640b-ebde-3904-9279-89cb47aec8b4 | -16.66978 | -55.54735 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 763ea3e0-2180-324f-bbc3-af91989f984d | -16.66856 | -55.90707 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 341d9197-82d7-3722-ad7a-138f832ad08d | -16.66748 | -55.49511 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1f98c6c6-d81b-34f1-aae8-82fad711ca35 | -16.66393 | -55.91112 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e0144a7e-53e4-3654-b20b-2040a70a5336 | -16.66323 | -55.54106 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e241e7ca-daa6-334c-a236-790eaa8d494b | -16.66271 | -55.52229 | 2024-10-05 04:40:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 44d3f26d-53f9-3b65-a8c7-f87dbd72d073 | -17.15057 | -56.15388 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cbe34396-4593-3958-96fd-91fa23c1d166 | -17.15023 | -56.15056 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| faf5876e-f56c-3872-a4c2-45d4d1c24675 | -17.14846 | -56.16028 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| dbb13505-4d2d-3feb-bd60-9a5b0ca95916 | -17.14801 | -56.16851 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c848da32-955a-332e-9196-a30d1fb85afe | -17.14757 | -56.16514 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9d4f68e9-5170-32eb-ab22-cfdd49b5a33b | -17.14592 | -56.15801 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| da477e22-bf43-3404-bcde-165b23fb100d | -16.97748 | -56.58607 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 05bf5857-14d2-3aa5-b7e6-bd3b638137d4 | -16.96832 | -56.14647 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3b2bfde3-43de-3486-a443-322c24c86b6d | -16.96363 | -56.15062 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| db1b8952-7d2d-38b6-bedc-1315544cf273 | -16.95093 | -56.60046 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b6447f77-9b7a-3b33-be99-659c1b17eb1a | -16.9335 | -55.83978 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7e37e6ca-3c6b-3404-9c7f-439bdde33d85 | -16.92976 | -55.83906 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f5c2c48b-6fca-31a8-b1e0-6a8dc9e395fb | -16.92892 | -55.84378 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b482437f-57fe-3a91-8887-109891565214 | -16.92685 | -55.83363 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d6a07d93-b306-3cf9-9c19-33b50d64049f | -16.92601 | -55.83834 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bf38bc7d-f8ec-3514-a935-d25c4890c8a4 | -16.92517 | -55.84306 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1b4bf767-fe30-3d33-a2ec-13bdfb4e4193 | -16.92394 | -55.82821 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 85966687-9216-3247-b904-b9fc4ee4df38 | -16.92311 | -55.83291 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3c10a484-0b7c-3f47-8316-56eccabcbf53 | -16.92226 | -55.83764 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b08f7c47-4cb5-304a-a693-bf4ba821f526 | -16.92143 | -55.84235 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 83d1cccc-b235-332c-a730-32e945910d1e | -16.92103 | -55.8228 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2c84d942-fc3d-398a-9f03-cc9172bf42f5 | -16.9202 | -55.82748 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 39c81f09-a07d-33f7-9227-726f1a18288d | -16.91936 | -55.8322 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 423adab5-98e8-34d1-8f83-eeba683c81f0 | -16.91729 | -55.82209 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 08521df3-60f2-3a3f-bf72-0cdaced08a64 | -16.91646 | -55.82678 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8780d2a2-c9cb-3699-a8b9-21fad02e6f9f | -16.91562 | -55.83149 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 69f8deb7-5240-3a33-9040-112ff2f27070 | -16.89849 | -55.86228 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5ad5dcbc-8d05-3580-a722-4a9dca183ee6 | -16.89474 | -55.86156 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| deebc9dd-c1f0-3f5f-bd61-322692c57550 | -16.88442 | -55.85247 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a5bb2493-c1e2-3817-b7eb-c87cc0bbcd18 | -16.88434 | -55.85468 | 2024-10-05 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7738a522-9806-3903-a308-d8fdd96f7cd1 | -19.66193 | -56.45347 | 2024-10-05 04:40:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 2f9eb13e-bdeb-323d-8cb0-c07eb89aca6e | -19.66109 | -56.45818 | 2024-10-05 04:40:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| fe3c506b-4090-3c52-88e0-b38a24be3f43 | -19.65736 | -56.45743 | 2024-10-05 04:40:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| c8b1fa00-3373-39a1-89b0-bd225f9fea86 | -19.64311 | -56.49375 | 2024-10-05 04:40:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 727f0967-e0c5-3334-839e-307da8a412e2 | -19.63938 | -56.493 | 2024-10-05 04:40:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1a325bb9-7e30-3e88-b78a-033de4cfc2f8 | -18.67088 | -57.28715 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 662839d0-6b82-3a0b-93a7-5e63dab895cc | -16.43025 | -57.3702 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ad7fb785-b55f-3a37-bd38-acfd229659ee | -16.42717 | -57.40997 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bebd041b-bd71-347e-a003-3b680f6a2907 | -16.42684 | -57.36549 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 362dab97-f7d4-369b-ba02-1ee28a9cfc35 | -16.42612 | -57.36937 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 46c8ac5e-ab83-3cac-b73b-138686e6894a | -16.42343 | -57.36078 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 48a699f1-0c44-3558-ae19-9a8aa0fc3345 | -16.42303 | -57.40914 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 45f2d4bc-341f-3a1a-a38d-a91b1755fa9e | -16.41838 | -57.38794 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3b19bf73-ccac-3928-8880-95d5e0ecde95 | -16.4159 | -57.35522 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0ba8c5cd-72fb-3da7-b73e-9f1e03e6e342 | -16.41178 | -57.35438 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dd36a675-1b05-35db-92a1-d881d2dde3fc | -16.41012 | -57.38626 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2aec1e7e-9c13-337a-8c15-55ca6d902ae4 | -16.40766 | -57.35353 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| fcf613fc-0855-37bc-a868-21213b163f13 | -16.40693 | -57.35741 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e3bae819-9170-3872-9d03-3cbdb331a6f1 | -16.40526 | -57.38931 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 71933937-f713-3263-afd8-940db1354762 | -16.62672 | -57.17075 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b87de0b2-aaf2-311c-a2e2-45ff21d2f0e9 | -16.5987 | -57.25531 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 06210020-6383-3970-a7f6-99e1bc8cd900 | -16.59544 | -57.20354 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9252e390-f52f-3a6b-b383-0a3064840583 | -16.5833 | -57.17764 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f2b9c69d-e44f-3d77-bdae-59b58dc9db07 | -16.57992 | -57.17306 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 32949e7d-f476-3df7-80b7-784be998e673 | -16.57854 | -57.1806 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f5d64e48-1ee3-3fc1-8b0e-7d183f602595 | -16.57388 | -57.16008 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e318e47f-9105-3116-8155-3f82a126dead | -16.56841 | -57.16685 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| b73e0219-653b-3c15-83de-bc5f881379ab | -16.56702 | -57.17439 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b20532f7-c883-3063-a797-ed6b20e1331d | -16.56365 | -57.16982 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| dab0b5c5-78d8-3c1e-9b15-d082375c879e | -16.56202 | -57.22433 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| c68801bd-b55c-3d60-a317-030523835a93 | -16.55864 | -57.21972 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f681d151-d819-35ba-8c47-2d7a0b8bccb9 | -16.55794 | -57.22351 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6d53b459-25d2-384b-a313-dbc0ab6b47a1 | -16.55245 | -57.23027 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 64dd3700-9337-3307-94c2-dfb1287475f1 | -16.55047 | -57.21809 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 27d94c37-3d17-3579-8b12-c95a1c5a6d84 | -16.54639 | -57.21727 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| db27e8f6-feb5-366d-adac-8f638dc2531b | -16.54569 | -57.22105 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 476a860b-9906-329b-a2a8-e249fcece801 | -16.54498 | -57.22485 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 1c90327c-c8b2-32ee-b916-dfbba874606e | -16.54428 | -57.22864 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| cf5348e6-55ba-30bc-a0e4-1791a0bd3f00 | -16.5416 | -57.22023 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 01a066e8-5951-30e3-b776-f3fdf274c2c2 | -16.5409 | -57.22403 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 6438ab4c-c433-3120-bb60-5f80a90f1691 | -16.51817 | -57.25491 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 25ae7bf7-f77f-38b0-9d56-027c4c6105c5 | -16.51516 | -57.25546 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 380174e6-05a5-3086-800c-d95eca90d6fc | -16.51377 | -57.26319 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| aa886172-e8a6-31fe-a918-340081a129a3 | -16.51336 | -57.25789 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b9af6224-9cb4-30ec-bf01-396b7ad2b740 | -16.51107 | -57.2546 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| aac6d0f3-fb81-3d11-8003-78cbda59902e | -16.51037 | -57.25848 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| f4936778-ca1a-3eeb-822c-9060efcb555d | -16.50968 | -57.26235 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 0a81d564-79f2-365f-99a0-0b1db64969cd | -16.49113 | -57.29432 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b373584f-f6cc-3bbd-ba2d-9fe9d28f8ae7 | -16.47471 | -57.291 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |


[Clique aqui para ver as próximas entradas](README122.md)
