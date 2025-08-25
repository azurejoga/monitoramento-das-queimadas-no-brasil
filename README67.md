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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cd3b778-2191-3ee8-a832-db32dfee87f6 | -9.04149 | -65.73535 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0e447f0-ae83-3aa7-8f70-29ec185bf983 | -8.70073 | -63.96399 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4f97e6d-2c37-3729-9846-2d64bc1f9879 | -6.19109 | -44.13672 | 2025-08-25 05:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3762321b-f55e-305a-b65b-4f4a869b87a0 | -9.17048 | -60.8131 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5fb1cdd-d0d2-3d92-9b9d-804adcab5741 | -10.83764 | -46.41131 | 2025-08-25 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c1c9be2-bae0-3990-a69b-0de5e679ae99 | -8.90748 | -62.41891 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 034ed7fe-b23b-32c9-bc0c-b76ec3e90036 | -8.2328 | -61.43576 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8df42130-2810-3b1e-9033-e55c0ecabef3 | -5.7971 | -59.22002 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e4310bd-4680-3ebd-b9cc-0d790cb43865 | -11.39673 | -50.68169 | 2025-08-25 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a15264d7-ba33-370d-9bfd-438aef838699 | -6.8923 | -47.92966 | 2025-08-25 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 384907f0-6a11-3d7a-a008-63cf88a5b1c3 | -9.82448 | -64.26012 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b08996ff-96cb-3d93-bf78-6e2af847ded8 | -5.79637 | -59.22439 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5cbc41df-5037-3faf-b275-afae77d60cc2 | -6.68428 | -58.86084 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b5d20c2-b954-3fd3-a757-9baeeada7443 | -7.54311 | -63.8586 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a98d2596-25b2-3483-85e3-f7708ee72933 | -5.49175 | -51.16264 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7aff6d43-9384-32ab-a711-4f847711b99a | -9.1964 | -59.47341 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f47df7cf-8012-37a7-b362-b5965cd19497 | -8.11749 | -62.87674 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ddbfe8b-8ebc-3fe3-b4b9-91d50ae99f3f | -9.21134 | -59.62919 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75ff185e-26f9-3321-a976-76edac4bcdb9 | -12.93943 | -46.31566 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9964e69-ccc1-37f0-95bd-9cf5d584cb7d | -5.74206 | -57.57559 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 676d455e-9730-3398-89d5-90a85522ff0b | -9.20079 | -60.77396 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fedddf93-25ee-34d2-9b95-92f1934fbc96 | -11.54493 | -51.91481 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a5f1ff7-35d3-35c3-bf03-3ff5c6e1b33e | -9.16033 | -60.82624 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 091bc34b-cf48-3053-935f-638e0d0aa267 | -9.20575 | -59.48347 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 644efc52-9736-3ac4-bb52-18dfce9e10a5 | -8.88827 | -62.45329 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f1cfeda-313b-3ba8-87de-a91aa81faf96 | -5.80813 | -59.22178 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db0b9854-d1a0-33dd-a140-3a32ab476368 | -9.19999 | -60.77875 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d36fe6d-b979-340b-8bfd-eaabcdf19c5f | -12.74489 | -48.14426 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| be171c33-5aa8-3c4a-8e0b-33de17a0c99d | -9.17351 | -60.81857 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 444ba880-afc0-3e0c-9f5d-4afc4e1dfe24 | -9.23914 | -60.47635 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cd0991c-597c-3d3e-b33d-31c3c506f0e8 | -6.79492 | -58.62603 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 042555fb-5359-327c-9ba5-3b89ae190f27 | -9.96402 | -60.17918 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 479f243b-e3e5-3aba-a10d-da92120cf3b6 | -7.65048 | -63.52586 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a57b0e47-d5a9-3c08-8347-aa47fa4f4124 | -9.51651 | -60.51288 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d2070ba-096d-37dd-9a54-5289af6d0dcf | -8.80036 | -47.31304 | 2025-08-25 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b22985fc-2dea-30de-8c17-6386a701dbce | -8.63293 | -62.64713 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aecaddaf-5f20-3bc5-baa4-240e7f9e9ade | -9.64271 | -59.64978 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6effdf88-b814-3e9e-9907-9d0165f57307 | -7.36031 | -57.62867 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05176b5f-bdf8-3c60-871e-36879e207cbd | -9.15146 | -59.4785 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e500998-0b37-31b4-8e56-49c65cddbf14 | -10.42299 | -64.43737 | 2025-08-25 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d0b42017-8126-3625-a5c1-3155de20282c | -8.89326 | -62.44998 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6438248e-e9ea-396e-855b-bc55e9a99471 | -8.86267 | -52.04008 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7601e397-b919-34ec-854a-87ff46466d98 | -8.62283 | -62.62785 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84091d60-0e20-3b67-a20a-a3f3679fb9e0 | -8.05907 | -49.68923 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| a0fec7b2-945f-376c-90dc-493621bfd30d | -11.93265 | -46.72675 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 755bb31b-b48a-3486-b9d7-4a4ff9b8a431 | -10.40183 | -57.68098 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41fe2fc6-69a2-372e-bd39-0626283b8b06 | -7.76226 | -47.3606 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56855543-47eb-317b-9acb-fde0a548d124 | -9.51318 | -60.55498 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56b8d2d2-1ee4-33ae-8bc9-2b5a6a6f920f | -11.61259 | -46.24357 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9ba8284-dc96-3937-bed7-9fdd0684d63a | -9.79939 | -61.20849 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc4104d9-ad4c-366c-8ad3-0145bdaf2ff0 | -4.96225 | -55.8067 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 163f088c-c578-38e1-8592-fd927a6431b3 | -12.99167 | -45.22729 | 2025-08-25 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a1b1093-359f-3b71-960a-c5fa13cd1cc5 | -6.82473 | -58.95857 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 877b823d-2e37-3b4c-9b30-cb13f9d6fcbf | -8.12116 | -62.88202 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ea4da0d-5e78-3e52-8486-fa66e193401d | -12.75932 | -48.11398 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 990d5000-3f38-338f-8090-43cd5f047617 | -9.18684 | -59.62072 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf4b2c16-5044-3ef3-9ec6-235a3330ee22 | -6.82711 | -58.95732 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2b712f2f-34c4-396b-ae16-51f71ed1a178 | -7.3648 | -57.62909 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bae1277-0ef4-345c-89b4-a036d3de46af | -13.05657 | -46.32158 | 2025-08-25 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f074a38c-17f6-3943-ab0a-c8fc8e4ee53b | -9.18058 | -59.45807 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b728cf18-fc7f-31d9-b441-74c984384999 | -5.43461 | -60.17909 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 52c7d0c5-98a0-3b65-8d8d-86b5cf6760f7 | -9.19044 | -59.44287 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83ed0748-eac4-316b-8f76-e1d05ebd9fd2 | -10.2501 | -59.10439 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| caef4906-6970-358f-a11f-e95b6b221501 | -7.67309 | -63.51627 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25020e2e-e4fd-3cbc-975d-54d22419fd86 | -10.24946 | -59.10828 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 969db188-8f08-3cae-8736-77e05ce6fa1d | -8.60705 | -62.59019 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94ae2270-2462-3f16-a9c4-dcdeafe5947c | -12.95594 | -46.33083 | 2025-08-25 05:04:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6c37f33-3825-39bb-830c-acff0921a2c9 | -8.89255 | -62.45406 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8761ca74-47d1-3ef0-9eeb-7df5986cb7ee | -9.26267 | -59.77431 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 35aa180f-384a-31e8-87b5-92acf1ade517 | -5.80566 | -59.21875 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a24fbd69-dab1-3bb6-b84f-d2b02fbe8953 | -8.89537 | -62.41253 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bc07293-59b3-340f-b707-0afcda05d3db | -7.53139 | -63.81276 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d1813aa3-358e-301a-9ea6-22137a616911 | -9.18806 | -60.82615 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ded3023-4007-369b-94ac-aa92f91805d8 | -8.60556 | -62.59864 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a3b8d53-3b6b-36da-a42f-52958a22ec17 | -9.20504 | -60.92105 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10c4e20f-795e-3588-9aa3-54ee65217dab | -10.71553 | -47.12943 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18badbac-a22c-3e7e-8abd-a8c8a63d2042 | -9.24514 | -60.4868 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a52dd299-cac2-3132-8242-cd1401ecf07f | -8.21516 | -61.3923 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0768cb4e-0e4d-3624-8999-201804766e7e | -9.18976 | -59.44697 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0ae9cab-c387-3b01-afd2-577944c47677 | -12.74568 | -48.13765 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07e2908d-f451-3ee9-bbb5-e58c03c02fdf | -6.7978 | -58.63057 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd823898-69e7-33c6-ac3f-0cb6f68aa4eb | -9.16193 | -62.3545 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1bc66a8-3dd2-37be-bb1a-185b6a4aabb5 | -9.19071 | -60.78701 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00069b84-2bcd-366e-a61e-7f477ff840a7 | -8.12721 | -62.87387 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7c3caf22-46b9-348e-955d-0e98ecdf0012 | -11.23737 | -50.40593 | 2025-08-25 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70e8f5d7-4d5a-3014-8b46-9613c78c3009 | -7.76183 | -47.36369 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91174d3c-3c19-3b97-9784-08a84ed8adce | -10.10275 | -57.76806 | 2025-08-25 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cdb2fb9-0952-3740-9c86-d183bb09520b | -9.31439 | -63.43768 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8305e000-cc11-3694-8a2a-78ba7c38e7c3 | -6.34097 | -58.18752 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1db45207-8f60-3402-9f16-2019feb1e281 | -10.71638 | -47.12247 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51b86f39-b76c-312f-85f3-51226bc11e04 | -9.16579 | -59.59153 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 765d9ee9-b80f-3b8e-89f7-78036654ce5d | -9.06467 | -65.7292 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3077b49-8621-323c-b9a1-e328eb4c4827 | -6.62941 | -58.4188 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8509582c-0039-3a19-9b0d-bb45ed512b9f | -7.32962 | -44.5364 | 2025-08-25 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d41ba03f-4f1d-3ace-b57d-79cdad87627b | -10.70493 | -50.55755 | 2025-08-25 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b066b93a-9e1d-3d66-8c92-e1fd2437bae5 | -9.1309 | -60.73022 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2f68a04-2d50-38a7-8583-31d689d992d1 | -5.79782 | -59.21568 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 061d2f7d-0b41-39fd-be4a-6ad5601ba832 | -9.20222 | -60.78898 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 691f831c-effa-37b4-abca-e577e29e6816 | -9.14363 | -60.73927 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cabce354-1681-3c99-a4d9-8181f98362e2 | -9.21276 | -60.92244 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README68.md)
