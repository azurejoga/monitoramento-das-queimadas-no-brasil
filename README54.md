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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed5931fb-6958-3c98-9e2c-7c55746cb7dd | -11.37786 | -46.83161 | 2026-09-12 06:16:00 | AQUA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 893933cb-c921-3049-9de0-ea8627963f97 | -11.18468 | -42.78297 | 2026-09-12 06:16:00 | AQUA_M-M | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 77f98b1e-350b-3db0-8d63-e986cb446047 | -12.1298 | -48.95733 | 2026-09-12 06:16:00 | AQUA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 9100cc32-b87a-3313-a295-201e9fdeb135 | -11.79779 | -46.37507 | 2026-09-12 06:16:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2e31083e-2e0b-39c3-90f1-3b6b0de88c37 | -11.37657 | -46.82389 | 2026-09-12 06:16:00 | AQUA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| db033556-bf08-3975-8cfe-7970014142ff | -10.54807 | -45.218 | 2026-09-12 06:16:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 38bb09ea-b78a-3381-bae8-50f426f41f11 | -10.5481 | -45.21122 | 2026-09-12 06:16:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c644e524-2aa7-3932-a4c5-d36ac949d575 | -8.75467 | -72.76794 | 2026-09-12 06:16:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6415a5f9-7231-350e-a38e-5586675bf29f | -9.48602 | -68.83955 | 2026-09-12 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ead33f84-8e74-3d7a-8a21-17177ab2a9e7 | -9.79467 | -65.05006 | 2026-09-12 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 31996cc8-88ef-3f49-88f6-f697a85da442 | -9.53266 | -67.16766 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c512fcb5-e29d-32b6-a3d6-5586dafcae73 | -9.49966 | -68.49706 | 2026-09-12 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 42e837df-3c18-328d-b62f-2a26dc18f5f8 | -8.74564 | -71.00138 | 2026-09-12 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 488753a3-d08e-3e92-9a58-8a8e92df9bc8 | -9.15794 | -68.24934 | 2026-09-12 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 291604b4-e59a-32b8-8210-92fe46f3fb69 | -10.43465 | -67.92188 | 2026-09-12 06:16:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2e3291d-412f-3d6a-9d42-b1d638f2d543 | -7.79677 | -72.48199 | 2026-09-12 06:16:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89abf57f-9ffc-3da0-b97d-d4d4cb9a61eb | -7.86434 | -72.81528 | 2026-09-12 06:16:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44760d55-08ff-3c49-a3f6-ef85e619e7c0 | -8.60139 | -72.75138 | 2026-09-12 06:16:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 756f490e-35ce-3bb2-a463-8aa35ae01f29 | -9.28304 | -71.93279 | 2026-09-12 06:16:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a88dc75-be6b-3484-b1a0-db89f5bad711 | -9.1883 | -68.21775 | 2026-09-12 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d25f3f33-0f23-3a1f-ab5e-68f1040de48f | -9.16238 | -71.84905 | 2026-09-12 06:16:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c424bd59-1b2a-3163-9ddc-aef067f6c1bf | -10.28379 | -68.75218 | 2026-09-12 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a4ffb96-554b-3783-8e9d-14a90b8f9db4 | -8.60685 | -72.71576 | 2026-09-12 06:16:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e6ae466-37e0-3337-bf12-800e8ffa7873 | -8.44984 | -72.98557 | 2026-09-12 06:16:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 467845ea-5067-3dd2-81e9-799fa7d44497 | -9.456 | -65.34831 | 2026-09-12 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19807dd8-12ce-3cf2-8781-5275d8ed2eb9 | -8.93827 | -72.74855 | 2026-09-12 06:16:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f32b0e83-4dc7-32da-be36-06b3f7a27dc3 | -9.31593 | -68.77901 | 2026-09-12 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f694e3e-d372-3dac-8c8e-db35ec11a2b2 | -9.41815 | -68.90797 | 2026-09-12 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8656c1e-e05f-3346-878b-9d6d9c141d2d | -9.02882 | -65.41557 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa0d3728-25b3-3055-841c-85088a62fb6b | -9.47208 | -67.09821 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f06723ad-bd4a-39eb-837f-aca064e0e8c0 | -9.31237 | -68.77474 | 2026-09-12 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe9838f7-29f6-3891-bc76-23ca4d3e26d4 | -9.47161 | -67.10089 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e112bc89-a683-377e-a031-02c4b5dda597 | -9.30154 | -68.30437 | 2026-09-12 06:16:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c56723df-734a-3e0b-8a4d-def79e38126a | -9.47223 | -67.09619 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 381348e2-0547-3439-b37e-56f500debc1f | -9.50018 | -68.4932 | 2026-09-12 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4f7a325-64f3-382c-b32b-2cc20f5370a1 | -9.1675 | -68.24267 | 2026-09-12 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb75c914-b799-38b6-87c9-ed7242f8874d | -10.212 | -69.05681 | 2026-09-12 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 273d2445-76d6-3d4f-be1b-61276ceb5696 | -9.17562 | -68.21576 | 2026-09-12 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8923c754-818c-3b39-b7b3-222d9b5dd411 | -8.98323 | -70.60725 | 2026-09-12 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 109efea7-64be-314f-b258-bfbcc0b6e647 | -9.49548 | -68.49647 | 2026-09-12 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa72a4a3-0aab-320c-b1f9-ecde6fc7da2f | -12.15803 | -64.14262 | 2026-09-12 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ecde1117-8257-3d54-9ce7-be9e6005f614 | -9.18886 | -68.21377 | 2026-09-12 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4da4c91-9276-3428-a566-ba6b514587d2 | -12.15319 | -64.13363 | 2026-09-12 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 734c721a-00e1-30e8-9845-f6b0948387de | -10.27233 | -68.27816 | 2026-09-12 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5268d4ac-9be4-3121-8cb5-803f1c8de961 | -10.2708 | -68.28006 | 2026-09-12 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28441495-bc06-3c36-97c5-4d2ef45d3fc2 | -10.53884 | -68.01667 | 2026-09-12 06:16:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43a2da86-40b8-3922-bbf0-f27aa2509f2d | -8.85689 | -71.44928 | 2026-09-12 06:16:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db5dc855-de3c-34cf-898c-fdeda6ec515b | -12.15221 | -64.1419 | 2026-09-12 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d1a90d7c-fba9-3893-813b-f88e81477956 | -8.85747 | -71.44536 | 2026-09-12 06:16:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a8636e7-9d3c-38f8-a688-b874eed27e83 | -8.99138 | -65.42263 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50ad04fb-9dad-3ad6-94d8-1b3f738f9d8b | -10.28433 | -68.74834 | 2026-09-12 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7eab19a6-05b3-3689-911c-7fe7327f9bd4 | -9.31645 | -68.77534 | 2026-09-12 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 413440d8-1c9f-3f01-a2e3-37d607ef7df2 | -9.46816 | -67.09276 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7628d2b0-acf0-3a52-b548-be98ce164832 | -8.8465 | -71.36775 | 2026-09-12 06:16:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0da4a6d3-0de2-3b75-b2c7-81a9eefd0a8f | -12.15901 | -64.13435 | 2026-09-12 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb83cac7-a755-3c43-8ebf-7248a9beaad6 | -10.20794 | -69.0562 | 2026-09-12 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad2f54ce-d59e-3263-9cb6-d711a160e2b7 | -8.85411 | -71.36488 | 2026-09-12 06:16:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a075871a-d52d-372a-bde6-8ebeea262952 | -8.07578 | -72.38535 | 2026-09-12 06:16:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e846c2d2-c6d5-31f0-b316-4a5460ce1785 | -9.18826 | -71.88797 | 2026-09-12 06:16:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f61da4ce-cbb7-32ff-b059-1598ada376f2 | -9.52809 | -67.167 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 405c5b33-75e3-3b57-a154-482f40711d53 | -9.93665 | -68.70538 | 2026-09-12 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cafb7353-3994-3c62-a8ac-8b2435e03abd | -7.79062 | -72.47739 | 2026-09-12 06:16:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c337db59-fcb2-3e05-b5f9-1bb5cdfa725d | -8.0528 | -72.51402 | 2026-09-12 06:16:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83ba5ae4-cd35-3eac-8b1b-7a3c6f5aef5a | -8.98687 | -70.60781 | 2026-09-12 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55da7c8e-b7d0-35ae-acc0-a80443957c5c | -12.15754 | -64.14673 | 2026-09-12 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6ffc7925-9896-32c0-9daa-bf979fd25d4a | -8.88116 | -70.84329 | 2026-09-12 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb350ffd-c379-3165-9379-0d8a45841a27 | -9.46765 | -67.09548 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e95e77e-bcce-3ffb-a3b7-ad907b966117 | -7.69375 | -73.06144 | 2026-09-12 06:16:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 663223a3-f0e4-3ae8-a4c2-6b24228ffa62 | -9.18351 | -68.22105 | 2026-09-12 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7642c9c-7b73-3189-8383-4b51275866bd | -8.88771 | -71.28851 | 2026-09-12 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f67a7084-a737-3a7f-8687-91e63f465a3d | -9.34019 | -68.2737 | 2026-09-12 06:16:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 690198f7-dbde-3907-a8df-fbf0be7ac06d | -8.97655 | -70.60186 | 2026-09-12 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8eb219f6-3fe1-3336-869f-1026d6c74ab6 | -9.03567 | -65.42405 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f81a4c9-3f35-31eb-8780-d850eb69418f | -8.82226 | -71.80274 | 2026-09-12 06:16:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f1d0ba1-3c0a-31d2-aef5-98d76a333823 | -10.28025 | -68.86744 | 2026-09-12 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee6ac207-191a-39af-a619-57c608b2474e | -10.27911 | -68.75538 | 2026-09-12 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3ba5d30-4d22-3fbc-a04d-46fd70087ecf | -9.1931 | -68.21439 | 2026-09-12 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 888e1e57-6644-33e2-855b-d08a56ccec25 | -8.75207 | -72.76788 | 2026-09-12 06:16:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06fb3662-234b-3262-8153-46c907ed390d | -9.8004 | -65.04748 | 2026-09-12 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb84a672-8c97-3929-9796-ca7581e21020 | -8.76481 | -72.79141 | 2026-09-12 06:16:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2042495d-a225-3a63-91fb-013973c9d981 | -9.30575 | -68.30502 | 2026-09-12 06:16:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d151de8-a4ea-3709-afe2-5edb413de133 | -10.02993 | -68.56487 | 2026-09-12 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c153be8-a87b-3148-ab2a-8593cdab30fc | -8.7544 | -70.81741 | 2026-09-12 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 694bec8c-56d1-31f8-aff5-9cc4091104eb | -9.47274 | -67.09346 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a668186d-7fd2-3425-946a-c393d01d78e2 | -12.15852 | -64.1385 | 2026-09-12 06:16:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c465687-fb50-39e5-bff3-15f4a9d9ae34 | -9.1595 | -71.84471 | 2026-09-12 06:16:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56d22736-3504-3d23-b01e-b9f1f2acd668 | -8.5975 | -72.75443 | 2026-09-12 06:16:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37a0462c-76da-3392-9e14-da4821fc7d54 | -9.2521 | -68.22485 | 2026-09-12 06:16:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aced88e1-6bda-3ce3-90fe-f53e8f845472 | -8.85013 | -71.078 | 2026-09-12 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2a38a73-e014-3f3e-884b-9290bc7c9f92 | -9.50403 | -69.03373 | 2026-09-12 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73dd018c-52ac-3031-b88a-8ee473fcd41c | -9.17984 | -68.21644 | 2026-09-12 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37d055d9-91d6-3c9d-b0f1-bb915ba622f4 | -8.86039 | -71.44981 | 2026-09-12 06:16:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cf2f289-51c6-356e-92f8-2434496c8dcb | -9.45642 | -65.3451 | 2026-09-12 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5853bab6-d998-33c3-ab56-f4fcbff09451 | -8.21225 | -72.54198 | 2026-09-12 06:16:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c622950-06dd-336d-8fff-f765cbe353f6 | -9.4762 | -67.10154 | 2026-09-12 06:16:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72289dac-f370-3873-81a0-e4f2f2e58cd5 | -8.75861 | -70.81377 | 2026-09-12 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 74358dca-eacd-3df7-934f-63a2e5c15bd0 | -7.39075 | -73.28435 | 2026-09-12 06:16:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b017baf1-be84-3963-a1c0-66dc1390b7af | -8.75799 | -70.81795 | 2026-09-12 06:16:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a41d354-b6a3-338d-8177-d19ae5f66820 | -10.43482 | -67.92071 | 2026-09-12 06:16:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea48930b-dc40-3d93-b32e-27b6e00e5556 | -9.09097 | -68.69432 | 2026-09-12 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README55.md)
