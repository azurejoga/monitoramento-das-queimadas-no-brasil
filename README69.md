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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7c89036-ca33-3b27-85d4-7c7873d9f9a7 | -8.06044 | -67.25256 | 2026-10-04 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32e7ddba-10a3-3a43-a3c0-ceb7dad0f644 | -8.57147 | -67.00897 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c64bb130-1c39-3e30-b816-7da00e82cbb2 | -8.3525 | -62.82864 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a485412-68d6-35d4-a127-45a0f074be46 | -8.51819 | -67.1143 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a62ed23-4f6f-3eda-992e-273fc4fa91a6 | -9.89693 | -65.01054 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e949cd8-203a-3f8e-9b10-17b2f5db5b39 | -9.08899 | -61.16005 | 2026-10-04 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 13359a52-bfc9-304f-bb1d-a6a32451404e | -8.57584 | -67.00508 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5797e6e2-a128-394a-b17e-2df0bedb1161 | -9.91817 | -65.04701 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0dc4c7b-581b-34e5-8e48-baa222689423 | -8.51068 | -62.6366 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a63310b7-e069-3203-9b27-a7c0235605d2 | -9.05001 | -65.4281 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a462da8e-dd8e-32bc-8432-f4b0a1c7f7cb | -8.35177 | -62.83411 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 421d4511-9d5d-39e8-91cf-b1f201581567 | -9.02006 | -65.70515 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48e17b37-5de9-3b2f-bce2-b6586d8d55e7 | -8.51883 | -67.10989 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb9d7d75-5ab2-375f-9127-e70766985f81 | -9.29629 | -67.54935 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a8ba760-8182-3421-ac69-15bfd98d99ab | -8.57518 | -67.00953 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e134e46d-ddfd-3749-b30c-53de3e626946 | -9.92472 | -65.0313 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94acf880-2602-3682-aaac-2a98ad3e25a3 | -8.58065 | -66.81634 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| caf59f19-0250-31c8-bd57-3a9a270b6fd8 | -9.90925 | -65.01653 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92392250-39c1-3123-a2c8-082c0cbdebdb | -9.40289 | -65.90247 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71673cba-57bc-32d1-b7b2-0744300fb0a0 | -9.09496 | -65.73057 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9b5a623-2f3f-3075-a708-b0346e8e1bce | -9.91557 | -65.03416 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 237d0a6a-ba6c-3f64-8167-42c1b2e325a3 | -8.60145 | -66.8054 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b6dba4b9-6708-32c1-9b8c-88fc70cb24f9 | -8.90252 | -67.45335 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82f5a132-a58b-3e16-a101-2f9b96d6b9cc | -9.89586 | -67.27952 | 2026-10-04 06:01:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecf3a133-7101-3752-8d52-1a2488152d4d | -9.88715 | -67.28733 | 2026-10-04 06:01:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e72e0696-f759-3f3a-950f-23923cb1c1e0 | -8.54557 | -67.15877 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d624ff9b-d497-38af-8e6f-0d0c272653f7 | -8.3945 | -70.11126 | 2026-10-04 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21d54a62-8931-3f4f-b97f-9c45137b2f2c | -9.92359 | -65.03947 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08266c84-e825-3bb3-b20a-6128758e909c | -9.13163 | -65.94292 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bb994e1-7324-3564-ad78-0b3effda4046 | -8.59317 | -67.1374 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1535bc19-8373-3afb-9139-619f59dc4f12 | -9.25144 | -60.33311 | 2026-10-04 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eaec5f79-ac42-3d6e-8148-863abef4a4ff | -9.91501 | -65.03825 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e2aeb4a-19e4-365f-a185-0a3543cefe78 | -8.05555 | -72.43741 | 2026-10-04 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b839617b-7249-3fde-b7ef-50641da0fe8a | -9.01853 | -65.68639 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff249bbf-ca30-30eb-9086-f8fe994eef69 | -9.69247 | -66.39614 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 636382c6-fba7-3300-90ac-10963bd38c0f | -8.5145 | -67.11375 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ea99036-2bc7-3d4b-9980-03a2b9ca9eea | -8.35104 | -62.83957 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b5270f13-3094-34b1-8b2c-48be8ba2d733 | -9.91411 | -65.01304 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acaa671e-f684-3b00-bf45-50199eff8112 | -9.56857 | -66.30827 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2145601a-873d-32ac-a7af-1b54645780fa | -9.03927 | -65.424 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ad00077-97b2-31dc-a1b9-3fbdf5739986 | -8.76712 | -69.34611 | 2026-10-04 06:01:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dabb2120-fa62-3a64-a140-8b18c7e4f5c9 | -10.27028 | -63.83379 | 2026-10-04 06:01:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 47ec8fa5-4c4f-3956-b4e4-bebcf38f4cca | -9.91445 | -65.04233 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4abc258d-c0d3-3d28-a2ad-4a0baa8ed127 | -9.36668 | -60.31144 | 2026-10-04 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13c19a62-97b7-3d2b-b0e4-5407bae722ba | -9.89086 | -67.28789 | 2026-10-04 06:01:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ec14bcf-c8e1-3583-91a4-392ec230b523 | -8.88717 | -66.8923 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42f9a7de-90ba-35af-ae51-fb8cd8efe1ba | -9.91072 | -65.03762 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70d19601-e166-3661-9b50-453f483d0081 | -9.92302 | -65.04354 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5397e5db-e911-3ec2-b324-ec4360cd17df | -10.9955 | -59.14527 | 2026-10-04 06:01:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0f17d140-1fe8-39ad-ba9a-88f183281e21 | -7.49765 | -69.99586 | 2026-10-04 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a0f072f-f729-3aa6-aadb-d08b62659505 | -9.05465 | -65.42496 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88532b9f-5410-36d6-bb0e-673cefe8fb03 | -8.01757 | -72.43513 | 2026-10-04 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0dd9f2f0-5e32-3ae9-8c42-a665be467d3f | -8.52252 | -67.11044 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea4e8d4d-636f-3b58-806a-22d8adc51512 | -9.12877 | -65.46638 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a7f90f8-0fe9-38f3-bdf0-d17afb57f218 | -9.46457 | -64.32828 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7246effd-dead-3e67-9a35-31ffed1453f0 | -9.16261 | -68.26477 | 2026-10-04 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b0dd83a-f9a4-3b47-9d71-aab51364d39a | -8.55988 | -67.06182 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f633b460-1e6a-3d82-a225-6c5774c54daf | -8.57623 | -66.82035 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b56f618-b472-36fb-92ae-da1548308d34 | -8.34616 | -62.83885 | 2026-10-04 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86a06d4b-0adb-3798-9d24-887742f400cf | -9.12715 | -65.94582 | 2026-10-04 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d93769ea-dd55-3ec5-ba44-b16dabbebc69 | -12.13765 | -63.17674 | 2026-10-04 06:03:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 120273cc-0e90-3f0a-a9a0-16d0251a6241 | -10.62101 | -67.92462 | 2026-10-04 06:03:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| db683765-ab65-3320-8a68-9ec6d6f29c4c | -12.13299 | -63.17146 | 2026-10-04 06:03:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 032ddfc0-92ea-34e2-b1c9-85bc5d9e9725 | -13.04009 | -62.32787 | 2026-10-04 06:03:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1af80798-f994-30d6-a466-d5a8a2bdecb9 | -12.16135 | -60.74572 | 2026-10-04 06:03:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4324af18-f6cd-353f-b157-958704e5df07 | -10.72776 | -69.41434 | 2026-10-04 06:03:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ab5efb0-eb11-31ae-aadb-18753dba7332 | -12.13371 | -63.16553 | 2026-10-04 06:03:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64cc30c7-2ddc-3df6-b231-e8b4a7a3926e | -11.05511 | -62.57297 | 2026-10-04 06:03:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f72abea-5d22-361c-9e94-9467efa37132 | -12.76055 | -62.08128 | 2026-10-04 06:03:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2b5c314-f12b-3144-b9c1-063ea9067f0e | -12.13335 | -63.16851 | 2026-10-04 06:03:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd9d7c91-3138-3b14-b0be-78a640d5fef7 | -13.5037 | -61.13152 | 2026-10-04 06:03:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e950094f-4c61-3b07-803d-0ea0ca823dd3 | -12.13766 | -63.17512 | 2026-10-04 06:03:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d210279-c324-3922-a756-34c06088917d | -11.04994 | -62.57234 | 2026-10-04 06:03:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d68155f-8b36-3567-a284-5a6445339338 | -12.77034 | -62.04593 | 2026-10-04 06:03:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 087e9281-6fa5-34c9-ada7-c4b9c5097f23 | -13.50321 | -61.13581 | 2026-10-04 06:03:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a6f2ec0-6099-38c8-91a5-2da1d5c9d3fd | -12.13338 | -63.17017 | 2026-10-04 06:03:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4ee41bb-d3e4-3f58-a06e-1e5746275c58 | -12.16085 | -60.75006 | 2026-10-04 06:03:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3379c851-3366-36b7-83ad-00a5ed8205d7 | -12.88714 | -61.71946 | 2026-10-04 06:03:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3a952db-5622-3962-9a5c-48503b028c47 | -12.1373 | -63.17807 | 2026-10-04 06:03:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa2c0159-c46a-3936-b722-96d9e83860ad | -10.49371 | -68.02713 | 2026-10-04 06:03:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 576e16ff-0b7e-3605-a661-e56cb596ba5e | -12.13376 | -63.1672 | 2026-10-04 06:03:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20b51e2b-2aa9-3989-b409-c45e304421d2 | -12.77077 | -62.04231 | 2026-10-04 06:03:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5b817db-0452-3063-bd64-0cb0f4851c4f | -13.04051 | -62.32439 | 2026-10-04 06:03:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39d448aa-6581-3015-86e6-cdee5e8a774f | -12.8867 | -61.72327 | 2026-10-04 06:03:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a39277b3-49b7-3319-a0a2-f3e4a4ebbc6b | -12.7712 | -62.03868 | 2026-10-04 06:03:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9af2896-a896-3d42-bd73-5e128c4807a0 | -12.13262 | -63.17605 | 2026-10-04 06:03:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc832218-ae67-3d28-a3fc-735d9290bec2 | -12.13727 | -63.1797 | 2026-10-04 06:03:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1414fa30-0be4-3765-9d2e-f372c8c2a8dc | -4.28 | -50.26 | 2026-10-04 06:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f619d464-4da2-3728-9142-27a52cc15a91 | -4.28 | -50.32 | 2026-10-04 06:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33d84f7e-e24b-33b9-83c3-c51da4464487 | 2.87044 | -60.54985 | 2026-10-04 06:35:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 983483b7-18b5-3efc-a5ea-114cf8cc94c4 | 2.87633 | -60.54179 | 2026-10-04 06:35:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac68b22c-5729-3ac5-9ed0-c55d1a9a03e6 | 2.86334 | -60.55111 | 2026-10-04 06:35:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ca61892d-f522-3ac0-bd6c-1b339af8d575 | 2.87386 | -60.54396 | 2026-10-04 06:35:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e935270-f293-359f-ae50-a26c8115110e | 2.86456 | -60.55794 | 2026-10-04 06:35:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 99c0bb0e-53e8-365b-a95d-47aca7e29dd3 | 2.87164 | -60.55665 | 2026-10-04 06:35:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 99f93576-3364-3feb-94d0-c4d22a262644 | 2.86793 | -60.55203 | 2026-10-04 06:35:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 867eec2d-d93f-3411-89dd-b20d64f52551 | 2.86923 | -60.54305 | 2026-10-04 06:35:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 359b57c5-4b6f-3331-acd1-0628c33813b8 | 2.86084 | -60.55334 | 2026-10-04 06:35:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c2b8b2af-dbd4-3ec3-a777-d5f2573fe7d9 | 2.86677 | -60.54526 | 2026-10-04 06:35:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3e7fa8d-0907-3dfb-bcb8-d92da38a94e2 | -8.3433 | -62.83187 | 2026-10-04 06:37:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README70.md)
