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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4e19a3b-d1ae-376b-9dbe-092fb03433ff | -10.3577 | -48.05189 | 2025-10-17 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 633b9469-a620-3c5a-b548-60d4eb840747 | -14.66761 | -47.40477 | 2025-10-17 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72257c11-c06c-3b69-936e-bc03c2b18573 | -9.02881 | -46.62344 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3688ae9-e4ab-38e7-b413-1d5005421670 | -9.04272 | -47.91674 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f1759e4c-f2fe-3352-9102-22e0049d3fb0 | -13.43342 | -47.95604 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 074bc4a0-f0b2-3de8-8d0e-149e028fac94 | -10.28343 | -44.05324 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 215a0eeb-eef4-3273-8865-c83446d6e86a | -10.2869 | -44.02652 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| faa66814-54b5-3fb9-9877-5c4ad63b1ff0 | -8.52262 | -44.57882 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55529922-8a22-378f-b4c4-cd553098bcf4 | -10.24623 | -46.72161 | 2025-10-17 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85c6b698-e8da-3159-a6e9-692e855a897c | -9.29397 | -46.90567 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31a9b160-409e-325f-afec-d9d8ac6b0373 | -8.90978 | -48.88049 | 2025-10-17 04:51:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35bb4eb7-1646-3c90-bcc7-3bd1ae02634a | -13.39032 | -47.20886 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a2389a9-3ce5-3a0f-85b4-e2b1db03f223 | -9.06141 | -48.84702 | 2025-10-17 04:51:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 967b249b-6ead-3b40-8360-324d0dda0665 | -10.10208 | -44.61374 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60965828-0956-33c3-a4f8-d16946c38f1c | -10.11961 | -52.34648 | 2025-10-17 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2e95c61-094b-314d-8eaa-c965f7099fd6 | -11.40095 | -44.20004 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e30aabf-2864-3c6f-b078-8c631fea413d | -9.8888 | -47.67791 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd979a13-fa0f-336d-bf12-3012d5b361ba | -14.23786 | -54.89819 | 2025-10-17 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 00e90311-df02-3057-acca-56fde26c8e6f | -8.26189 | -44.07353 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7c4614a-ea20-3cad-bc51-fd933b99793b | -10.00492 | -56.11513 | 2025-10-17 04:51:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dc4d6e0-6043-380e-a043-ebce641cfc2d | -10.97487 | -47.90935 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8065296-1dfd-36c5-8484-ad309a3dfb5e | -8.33578 | -46.23888 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1450f14-c4b6-3918-9185-4719b95140ba | -8.3791 | -46.24889 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eba1f944-8df4-3721-ba5c-19154547dc89 | -8.82135 | -47.30412 | 2025-10-17 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 85330930-69ec-306a-9f42-c2850a2b99dc | -9.43764 | -47.90166 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12a54733-74d7-3569-950a-a64da1a68b3e | -10.28372 | -44.04239 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3cbeb326-b2db-3a94-b6fd-dee2beacc344 | -12.41354 | -51.30016 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d9e8ea13-796d-3545-8d9b-25e71791e502 | -9.87882 | -47.67832 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a427593-e9bc-3b17-b82a-c39df385b3f2 | -9.1302 | -46.63524 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bf7ecdf-571e-3b46-8cb9-6b9698a5cf0d | -8.70157 | -46.97707 | 2025-10-17 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 049ed9da-01d7-3bcc-84fc-3f2730644c8d | -13.37337 | -43.59448 | 2025-10-17 04:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63906140-da86-3210-a06e-b554752bd25e | -8.45079 | -46.24748 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09d38cd5-c05f-36b0-95ac-c1e51f7d6dd0 | -11.48417 | -44.18921 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 251fb23c-b772-32a2-afa1-eb8274b146d8 | -13.39333 | -47.21814 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f04863ed-1893-3ad7-a037-01d799260efd | -9.28523 | -46.90975 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ebcc825-7c7a-3b39-a187-a003d29bdc07 | -10.36693 | -51.57332 | 2025-10-17 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdb84a69-aa63-385b-b8cc-97b2d20bd2fe | -9.14387 | -46.6551 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 007069c4-f87a-3b40-a92b-500dba9de093 | -8.83805 | -45.97934 | 2025-10-17 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd08596f-41c4-313f-8362-dddacede57ea | -11.39526 | -44.20498 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2efaa222-8a74-30ab-be3a-43038b81a14d | -11.5456 | -49.92258 | 2025-10-17 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57cba147-29b6-3e3d-b08e-12ecc23dfa5b | -10.28046 | -44.03753 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd6db893-320a-35cf-a304-afe90430f950 | -11.46765 | -44.04169 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 460e8552-4df9-3225-a523-0d8fdb700668 | -8.39704 | -46.24102 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d25a4c00-6b96-350f-b250-e74a60881a45 | -12.17029 | -45.05785 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2d32d7b-ee9c-3ea4-8aab-cf2ddc3536b1 | -9.24473 | -44.3809 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58bbc80b-b4a8-385f-98b0-6315fcb174f5 | -9.83248 | -58.06885 | 2025-10-17 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6626799-944f-355d-894e-681652fe0cdf | -9.98736 | -47.0087 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0b5d2e6a-907d-33a7-be10-7300391ef092 | -11.45691 | -44.0461 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0af5fba8-c6cd-33ec-8f2f-e7ac26d28859 | -13.44391 | -47.9677 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5250de78-4b35-3bb2-bb0d-2e7da39216a9 | -10.26749 | -44.0512 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0cd8189-50ce-30b5-903f-0b3489aa9dbe | -8.05646 | -48.17026 | 2025-10-17 04:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f17ee66-047b-3ba8-b23f-2b2a27c849b3 | -12.45828 | -44.63487 | 2025-10-17 04:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f259e93c-864c-342f-9a00-092c7b74db8f | -8.45606 | -44.1755 | 2025-10-17 04:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 8ebba9eb-9198-3d49-bb83-e90b8ae82be5 | -12.41916 | -51.30849 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| a0ba099a-e5d3-3128-8a36-2121d154ee17 | -10.50509 | -43.40639 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c41e4801-7609-3d6d-9142-22dfa2a8d3f1 | -10.05419 | -43.86412 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53d199bf-eef4-3669-bae7-6524b8188b77 | -12.71577 | -48.63736 | 2025-10-17 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| da0281a0-014e-3f9f-b08f-b46746ee4280 | -8.16277 | -46.06692 | 2025-10-17 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cfbc36e-0d34-3943-b7cc-df265f558fef | -11.44948 | -44.18442 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63bb19eb-0ddd-3384-bd6f-f7d7669f27b9 | -10.4992 | -43.41142 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c64da625-055c-35cd-bbf9-a6777d44b6ac | -9.13727 | -46.64359 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3032920-47b4-34fc-b831-de2acec57ecb | -9.71287 | -44.55348 | 2025-10-17 04:51:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 06a808ea-0c0b-3dd9-914f-541f4c7d7945 | -9.83206 | -58.07076 | 2025-10-17 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da1cf0b4-3a55-3671-be18-8f7ebe0a14ab | -9.88396 | -49.29216 | 2025-10-17 04:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a935563e-2d32-3858-8ae6-6188de716859 | -10.29358 | -44.04364 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 0289da99-4f3b-35c9-a936-940d02a2418b | -9.96393 | -49.80861 | 2025-10-17 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 306e767f-767f-38a8-8896-411d8ec00f26 | -13.23993 | -47.11057 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b4993298-eb46-326e-94f2-755f7f2e7ca2 | -10.14845 | -44.5302 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09919ae3-f3f7-3e45-aa2d-fb5279830106 | -12.16614 | -45.06543 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a8cdc70-17e6-3889-8586-07ea0fe5a11b | -8.39449 | -46.22941 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19d02f3e-f172-3d0f-acfe-a1e641523629 | -12.44385 | -51.30499 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4660e0f9-c765-344b-ade0-fcf2f3d76f88 | -15.04438 | -47.30964 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c307bb9-295d-36c1-9f1a-25e25f1b6067 | -9.30223 | -46.93317 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 13337d98-620a-3c17-b9f3-1b8671f8d35b | -12.41298 | -51.30379 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 46f77367-a0f6-3758-9c38-c6336182c9dd | -14.3369 | -51.44474 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c22ece79-ebf9-372d-b14d-33e013ed3391 | -11.51319 | -48.23064 | 2025-10-17 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20021e00-782e-386c-9afe-0432eab5f33a | -12.60646 | -56.51014 | 2025-10-17 04:51:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1e41d4a-c568-3c58-be12-efee54e7e391 | -9.18007 | -47.71485 | 2025-10-17 04:51:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1f4592c-b0a9-33b9-a099-838ab23bd006 | -10.12016 | -52.34297 | 2025-10-17 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84918264-7d20-32a9-badf-2aadbd6a3947 | -11.40218 | -44.22871 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9939c67c-defd-3114-a434-0ba56c54e8e4 | -8.45903 | -46.24868 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22a67de4-7160-3214-b1bc-6219391eb420 | -9.50878 | -47.26825 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3418a3fb-a26d-3db7-947f-2debb7d1097c | -12.42308 | -51.3054 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6dcd97ab-5887-3d0e-837f-fec59641dce8 | -10.1061 | -44.63077 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ebf684b-57c2-3654-8f1f-c9942db38cc1 | -9.54789 | -54.58711 | 2025-10-17 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42d97fe8-3708-3331-9384-af6f2b0c85ef | -12.44639 | -54.5048 | 2025-10-17 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fafd1ac-dd49-38f4-a9ea-5a38f4048808 | -10.26428 | -44.04654 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1cfe9b54-5302-3649-8fbe-c57d415923e3 | -10.10855 | -56.77166 | 2025-10-17 04:51:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 78414a38-6d84-3ffc-929a-d79e3e7bde33 | -10.14108 | -44.58498 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cbf381b7-ce40-3d04-bc6b-fd1676fa5045 | -9.24755 | -44.36065 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 743bfbdc-5a28-326e-9755-b1548c91103c | -11.9572 | -45.35891 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 926cf112-e704-388d-9ba3-b500f5dad51d | -10.14228 | -44.54019 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5edd86c2-cb8d-3a91-a3e6-885a114ae130 | -11.58018 | -48.56145 | 2025-10-17 04:51:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d741f02-b152-3735-9576-1f0d88ffc550 | -8.08249 | -46.66481 | 2025-10-17 04:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42610166-6e3f-3642-99d1-37ddad5803a0 | -11.47676 | -45.09053 | 2025-10-17 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2be241fe-0766-3f42-8634-9bb72f0b3ad3 | -13.12843 | -43.68481 | 2025-10-17 04:51:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 432a0df8-c3f7-3962-ba9b-3c897dbd40af | -8.36993 | -46.25434 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62b6d26b-5eb9-378a-aafa-cfc005b7d3f9 | -12.92889 | -48.59805 | 2025-10-17 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94b7d212-efb9-3909-a3a3-71e201204b30 | -10.95137 | -49.78003 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b015024-dcd8-3252-9c28-5fbc28cfb784 | -9.25299 | -44.35631 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README90.md)
