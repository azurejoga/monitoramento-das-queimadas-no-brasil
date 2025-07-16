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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ecc9088-0009-3162-b3c9-11ced213cf3d | -8.5618 | -64.19782 | 2025-07-16 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 342f3ce2-985e-3cca-90c9-da94665f166c | -8.68849 | -64.12324 | 2025-07-16 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c67e0ffc-2ef9-3b28-a117-78fb0645f61a | -9.01635 | -61.22749 | 2025-07-16 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2ebe886-a76a-3ec3-918f-7fc0b0cc744a | -11.94323 | -63.84728 | 2025-07-16 05:55:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b152c7c6-b42b-3c2a-9479-1cc8b3fd0ecf | -9.65987 | -63.22156 | 2025-07-16 05:55:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaa5a082-709a-386a-9506-fca403ac0fd8 | -9.64661 | -63.44555 | 2025-07-16 05:55:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7907b638-8c66-39a3-a94f-3a56a7774bb0 | -10.0618 | -59.10465 | 2025-07-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1192d79c-4ed7-3fe5-a679-ad993da7f91a | -10.05554 | -59.10782 | 2025-07-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34822ce2-da69-30f8-ab13-dd182c9c7d6b | -10.06078 | -59.11256 | 2025-07-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c32793d4-b103-3288-8464-157fbe21b97a | -10.05605 | -59.10381 | 2025-07-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1b9c45d-f25a-3534-a0eb-92c26986046a | -9.62665 | -67.20815 | 2025-07-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21c14f70-fbd8-36fa-b311-eb64c957fc39 | -9.65144 | -63.4421 | 2025-07-16 05:55:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38367bc1-cdec-37ed-ba0c-bd0a7fcc3e2f | -21.95975 | -57.59173 | 2025-07-16 05:57:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60a876c5-6b1c-3740-abe8-b0b875244460 | -21.95258 | -57.59099 | 2025-07-16 05:57:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b4c0668-88bc-36b1-b9ee-40685fa24369 | -6.7194 | -44.3231 | 2025-07-16 06:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ef2ca283-9be3-3120-8aeb-cd9a8707d8e4 | -13.0146 | -45.0593 | 2025-07-16 06:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 2d871aa0-600b-33e6-b3ac-e2c11438bf12 | -3.21895 | -48.9621 | 2025-07-16 06:16:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 70742f59-2372-3402-8de0-9a793fbfecd1 | -2.91941 | -48.23247 | 2025-07-16 06:16:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 23abb1ae-4e8d-3a32-9362-b9c69cd1640e | -4.02366 | -48.06133 | 2025-07-16 06:16:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 51f81705-f0d7-3fc6-8a33-1d23016ab978 | -3.38237 | -47.48877 | 2025-07-16 06:16:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ec01f519-b441-3e3a-82a1-5237f489f0aa | -3.21329 | -48.96943 | 2025-07-16 06:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c5c8deeb-2325-3008-9a4e-3daef3d121d0 | -6.72121 | -44.32302 | 2025-07-16 06:18:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 2f347188-c866-33f1-bf7b-4b22ad27d61f | -6.73303 | -44.31649 | 2025-07-16 06:18:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| ebd895ff-4f86-35c2-918e-9384af8f4525 | -11.94607 | -48.4106 | 2025-07-16 06:18:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 3714d58b-8771-38c3-b2fd-04ebc57ba0af | -6.91133 | -52.85099 | 2025-07-16 06:18:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 534dc332-61f0-329b-a5e9-f4510597ea77 | -9.7071 | -56.17807 | 2025-07-16 06:18:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| aeca2657-1f0a-34ab-95e4-950d94f048b4 | -9.70565 | -56.18751 | 2025-07-16 06:18:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 97f93c18-8fcd-3245-9154-b4b20ba7dd9b | -6.70467 | -44.32053 | 2025-07-16 06:18:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 3802623a-809b-30d9-a362-18f7d0128138 | -11.87235 | -55.44963 | 2025-07-16 06:20:00 | AQUA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 221990c2-bc64-3d1a-89c5-3e007e17d72c | -12.8809 | -49.1977 | 2025-07-16 07:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 62ca41e5-6793-3370-9673-6cceb0b1e98f | -22.0953 | -52.5818 | 2025-07-16 09:00:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| 34bb07b0-3d8f-39e4-a65a-6e2ddcf17589 | -22.1155 | -52.6 | 2025-07-16 09:00:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| b93fdf4b-8f4a-39ec-b46e-96d6c5a83536 | -22.0948 | -52.6041 | 2025-07-16 09:00:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 54.8 |
| 517664dc-f268-3da9-b396-af5606a3cf3d | -22.1161 | -52.5776 | 2025-07-16 09:00:00 | GOES-19 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 141.6 |
| b8c4cd02-c887-3bb4-a5f7-be2f97102b0c | -12.4121 | -45.3628 | 2025-07-16 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 0f1a56e5-9000-37bb-8962-764d430fd002 | -12.4121 | -45.3628 | 2025-07-16 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| ea59fce2-10f8-3184-9a49-b9c4297b41f8 | -6.6488 | -45.7388 | 2025-07-16 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 05f2de51-b05b-341d-9027-bf256bffc4c2 | -6.37536 | -44.75623 | 2025-07-16 12:08:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1a2f63b8-788e-39a9-9bdf-4fd19b2d07da | -6.12422 | -42.5332 | 2025-07-16 12:08:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| be69ff50-401f-33b3-9471-8565ba14f122 | -4.41892 | -40.58508 | 2025-07-16 12:08:00 | TERRA_M-T | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 4fa53434-0319-3089-83fb-6acd3975d0da | -5.05894 | -45.11489 | 2025-07-16 12:08:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| a6e82802-b46b-3b8f-b634-3f16478ca55d | -3.30047 | -42.52699 | 2025-07-16 12:08:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aca12c05-ee27-38b2-87b5-d182e2e3f3a4 | -5.68686 | -43.71494 | 2025-07-16 12:08:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 24dede20-3eaa-3f8f-be6f-269deea2323d | -5.45638 | -42.62474 | 2025-07-16 12:08:00 | TERRA_M-T | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 6e7154c2-6666-38ff-86ba-ce6bd63d7681 | -5.79234 | -45.08372 | 2025-07-16 12:08:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 4a212c22-4d9c-3277-a794-001f421c66a5 | -6.2035 | -37.42785 | 2025-07-16 12:08:00 | TERRA_M-T | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 889067bf-6539-380e-a355-da2dd6137476 | -6.33706 | -43.4375 | 2025-07-16 12:08:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 0fc06be9-9387-308b-9940-d767bdd71d9d | -6.34586 | -43.43873 | 2025-07-16 12:08:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| f6417e07-b188-34a8-a747-b06ac05914e7 | -5.06707 | -45.11222 | 2025-07-16 12:08:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 740bcafa-e60d-3c0c-bdc3-505eed29ccdb | -5.97445 | -43.76538 | 2025-07-16 12:08:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| fe7fc6a2-af0c-3229-8a03-3fd35d687851 | -5.91422 | -43.48121 | 2025-07-16 12:08:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ab90fe9d-64d3-313a-8905-b58df5d9803b | -5.70428 | -43.84348 | 2025-07-16 12:08:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 16d96f39-8d66-385f-8a8e-adc0485b68ee | -5.45765 | -42.61585 | 2025-07-16 12:08:00 | TERRA_M-T | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 4bb61a7e-5c6d-381c-b5c7-756dadcc02cf | -6.35947 | -43.65583 | 2025-07-16 12:08:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7158f3d5-0fad-3e7b-a406-eeb86bcb7505 | -5.06034 | -45.10523 | 2025-07-16 12:08:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| bf924e03-9f9b-3286-bca0-ae5216e67a21 | -5.70301 | -43.85233 | 2025-07-16 12:08:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 94b3bc79-2d14-3bd3-a8d7-2cb4423ea4ec | -5.7832 | -45.08242 | 2025-07-16 12:08:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4b3f5a5e-53e5-3614-b9c4-4f15a1442bb8 | -5.962 | -44.99503 | 2025-07-16 12:08:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 8329a808-e78f-3bfb-96fb-220649abf0dc | -6.13164 | -44.07983 | 2025-07-16 12:08:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 100c65e5-98b3-35b4-8707-93ad5641322a | -4.4204 | -40.57471 | 2025-07-16 12:08:00 | TERRA_M-T | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| e28ddc61-c61d-3ef3-9647-8f28f37bcd83 | -6.34713 | -43.42994 | 2025-07-16 12:08:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3b4a6d2e-5be5-37d6-b45a-7d2c673dfbca | -5.97318 | -43.77419 | 2025-07-16 12:08:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 007918a0-2f34-3b62-8b0d-24684b5e4c31 | -5.43087 | -43.1791 | 2025-07-16 12:08:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| a553fdb5-e6dd-3011-bd91-6cdfd28832a4 | -6.63165 | -39.37528 | 2025-07-16 12:08:00 | TERRA_M-T | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 51.6 |
| 05ee2153-21b7-334a-b539-e5555f83f755 | -5.68813 | -43.70615 | 2025-07-16 12:08:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5658c432-d99b-327a-8b11-41c513eac041 | -6.63342 | -39.36196 | 2025-07-16 12:08:00 | TERRA_M-T | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 40.5 |
| cfd437ca-839c-3a29-99a6-4538677f05c8 | -6.33833 | -43.42871 | 2025-07-16 12:08:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 24714ac3-d8b3-329b-9f24-a6a887dfdced | -5.91548 | -43.47243 | 2025-07-16 12:08:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d822c2c8-3ad7-3432-8bd2-a35032c43837 | -5.58103 | -46.73702 | 2025-07-16 12:08:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a5bbbaf8-3610-3774-bcc3-2208d9a0db5a | -6.37671 | -44.74703 | 2025-07-16 12:08:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d9dd3b10-424f-3695-aa94-39eb75971680 | -5.42207 | -43.17787 | 2025-07-16 12:08:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2dd40b1c-9c56-34c5-81f2-cde905fd6204 | -12.4797 | -46.9243 | 2025-07-16 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| a5d3eeb7-c292-35f6-852f-34128e71fd18 | -12.4121 | -45.3628 | 2025-07-16 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 02670528-ab23-3994-9d75-c0640be5b571 | -6.3344 | -43.4299 | 2025-07-16 12:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| a29925b8-499a-3314-89c8-13e7a9824ea4 | -6.48419 | -44.89727 | 2025-07-16 12:10:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7ac2e079-8c43-3a29-ae8f-fa8146f6cece | -9.41644 | -47.47953 | 2025-07-16 12:10:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 58d2c404-a5ef-361c-a481-4cf964ae3601 | -7.35858 | -45.66934 | 2025-07-16 12:10:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 61a7002e-e113-3e7b-b65a-75890e44fc70 | -8.25173 | -44.93313 | 2025-07-16 12:10:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 529a7cae-14da-3536-b30e-7ab3a6ce8b5b | -8.81589 | -44.54079 | 2025-07-16 12:10:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 0dec6e94-c60f-323d-86b4-8afad6bd060c | -8.75992 | -46.60385 | 2025-07-16 12:10:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e1078a9d-7005-35eb-94a2-30e4abd8a204 | -8.06972 | -43.12401 | 2025-07-16 12:10:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 9ab5daec-d853-3e11-8e93-a98f598719fd | -6.7153 | -44.32439 | 2025-07-16 12:10:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 93be260b-fc26-3a39-b1d7-856a0aaf818d | -6.67285 | -43.026 | 2025-07-16 12:10:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1adc9ef2-08b7-3310-ae38-228e36d1db92 | -6.65386 | -45.74401 | 2025-07-16 12:10:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| e7e4ad62-56ed-3939-b7f9-8b2cffa172f3 | -8.32547 | -40.16242 | 2025-07-16 12:10:00 | TERRA_M-T | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e34bcdd8-bf2c-32bd-8137-deb0ef220fa0 | -9.42721 | -47.47583 | 2025-07-16 12:10:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 62a17132-2202-3bbb-b147-2275e3e9392b | -9.13199 | -47.59277 | 2025-07-16 12:10:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 87fa62c1-2765-322f-98a5-00cd75f859a5 | -10.67616 | -42.67792 | 2025-07-16 12:10:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 5a6e31c7-ad6c-3adf-83e2-ab8ffe32905d | -6.43016 | -45.32313 | 2025-07-16 12:10:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54a3198e-8aa7-31a3-99a7-b6433419e73c | -6.69809 | -43.03857 | 2025-07-16 12:10:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c75cbde6-17ea-3e9e-8dfd-2bd03e98d6ab | -7.62688 | -46.48438 | 2025-07-16 12:10:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2caf0021-1b8b-3eb2-9c3a-0642a422cdb3 | -7.61334 | -44.4968 | 2025-07-16 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 108102ba-2441-320e-b7e7-a173a88c80e1 | -6.73174 | -44.33584 | 2025-07-16 12:10:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 2547ab4d-b713-3078-aeb3-49f61fd4d92d | -6.43663 | -44.96938 | 2025-07-16 12:10:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 41c6d3cb-4969-3341-a54b-51ea7a1da460 | -7.04985 | -43.47328 | 2025-07-16 12:10:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6beb64a1-1591-3511-a497-9956a7f2347c | -6.9795 | -42.81492 | 2025-07-16 12:10:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| a4d9e44b-86d4-3820-85b5-12fca260da67 | -7.63512 | -43.97449 | 2025-07-16 12:10:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 59dea626-18b7-367a-9758-0d0ac1ac8fde | -6.84984 | -42.74783 | 2025-07-16 12:10:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8551e5bb-e126-3cd0-8475-44c4d69bb372 | -8.24415 | -44.9227 | 2025-07-16 12:10:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 80673831-3d96-3d2f-a351-c2c8b7396a54 | -8.95287 | -49.83587 | 2025-07-16 12:10:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |


[Clique aqui para ver as próximas entradas](README27.md)
