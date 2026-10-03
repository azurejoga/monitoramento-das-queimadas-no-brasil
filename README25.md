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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bbe699a-056b-3dfc-9e5f-b2687dc48f16 | -5.10138 | -47.55693 | 2026-10-03 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a235e4a6-245b-35b2-b36d-a72accd0a81a | -5.73633 | -45.14201 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 68fc2484-9f9e-30f2-83a1-e1953c87da5c | -5.76321 | -43.9865 | 2026-10-03 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4992636c-9199-3ca9-9219-a2ebff4f00b8 | -5.74449 | -45.15475 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fc6c366a-cd7f-36a0-9f4a-7f9c686a493b | -6.31383 | -43.61601 | 2026-10-03 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| efbb0aec-3deb-3f81-a24a-e13092216190 | -10.36738 | -39.87074 | 2026-10-03 04:40:00 | NOAA-21 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 79bc6019-c895-36ed-afdd-57acd7ad4063 | -5.73871 | -45.15229 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d37dec7d-e677-3303-97c8-011dabaf9df2 | -5.25534 | -55.92638 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2c6a4b3-3f99-3727-bbdb-1730dadb38bf | -5.85369 | -53.46577 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e27d1e64-5b70-3628-9065-f25f24380a95 | -4.84823 | -49.95684 | 2026-10-03 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f77325c-0c09-31c3-8890-a2e0a10d417d | -6.88924 | -43.73748 | 2026-10-03 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0c26e11-5d37-3272-83cd-8ea2b87a9cce | -9.16779 | -61.40903 | 2026-10-03 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e3dc6608-b133-33e4-9e60-e736ddccc3ec | -6.83118 | -47.43374 | 2026-10-03 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 739afbf1-70ba-3d18-9055-d2c868c4741f | -5.85631 | -53.47809 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2001ab63-79f3-3e91-8cd1-a0595959825c | -6.21408 | -60.02215 | 2026-10-03 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0daddce-e6c5-3acf-b639-6d440b00ce80 | -9.16861 | -61.40472 | 2026-10-03 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3352be03-f683-35d0-b1ba-7e75b9d57a55 | -6.01618 | -53.54368 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b7855e8-0977-3bf6-84e3-d49f1f0d4fe8 | -7.46756 | -54.99009 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15884705-c379-337f-878a-39fc3df891d6 | -7.2813 | -47.42427 | 2026-10-03 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35e8ae52-3e6b-3e75-956d-acbad3639c65 | -5.7529 | -45.15103 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cf9a20c-0910-3cde-9eb2-0bc0e9bcf067 | -4.81389 | -49.87341 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00c7e6d4-91b9-3efa-b477-938dbbcaee68 | -4.11793 | -55.02073 | 2026-10-03 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34e7576a-cf55-307f-8d23-8d0077962668 | -4.11923 | -55.01286 | 2026-10-03 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb4c04f4-80b3-3397-960b-56eeb40ff378 | -5.36836 | -49.59029 | 2026-10-03 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 696c821f-94e5-3554-bea9-a039f75451ae | -5.9559 | -43.6454 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3afe78a3-fbc4-33e5-bcf1-739b3f3ff3c5 | -5.27443 | -43.36152 | 2026-10-03 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 418f09d1-81de-3399-8f28-f4122b579a2e | -9.46434 | -40.37603 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| a60d311c-6c3a-3abc-9e16-10475440bb6e | -6.21643 | -53.2621 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b41ee28-d1b5-3bfb-b559-14735c7de5fc | -6.00256 | -53.53249 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 436f64cd-5bb2-3868-b5e4-1164f6411d12 | -5.73994 | -45.159 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67658a61-6163-3fb9-94f5-021f03d00f24 | -5.74134 | -45.14931 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| aa542543-766c-3c7a-bd79-c46e1845344e | -4.29806 | -50.77122 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca4324bf-fe4a-3a62-a901-e74f4a711e78 | -5.74642 | -45.1534 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3fb2b0ff-2f48-3fa0-a3d8-21d177c79d53 | -6.01693 | -53.53908 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 152a19c3-0c3c-34f1-890d-320f4600dce8 | -5.76681 | -43.99088 | 2026-10-03 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efc2d4de-eb3c-3fc9-af23-25f0a6af4daa | -4.40343 | -49.97226 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2272aaf-8245-385a-b774-41965d19a255 | -4.11858 | -55.0168 | 2026-10-03 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdd2c638-ba5c-31c9-8e4c-332d0c57719f | -11.6511 | -42.41172 | 2026-10-03 04:40:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 679b7b92-d01e-32c6-827c-f7987150dc4d | -4.28117 | -50.76858 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b286b9fa-9333-3b95-9050-8c9e2f46d67d | -6.92575 | -49.62085 | 2026-10-03 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8899adcb-db3f-3b18-9b69-094a93777a96 | -5.74096 | -45.05877 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8100dc2c-2de1-3611-819c-1775907b7155 | -5.21789 | -46.02028 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55de30ed-5ea0-3427-a9bb-8c37416730bf | -4.21176 | -53.56196 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f2d45a5-0c4f-34e8-b145-f899194d975b | -5.41031 | -45.19055 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c173bb24-fc89-35cc-b07c-c02a739a7678 | -5.61794 | -44.37829 | 2026-10-03 04:40:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0dcc9e1c-a1d4-3848-ae04-7ea2e026391d | -4.78481 | -55.71515 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed3e1b7e-ab00-399f-9847-cb0a005ae1a6 | -6.31647 | -43.3397 | 2026-10-03 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d6a4b40-a1c7-3394-9a0a-b0659cce1d06 | -4.43039 | -55.75179 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 48e1da8c-3590-386c-adbf-cb0ea0bfb676 | -5.13584 | -45.57485 | 2026-10-03 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cabd2f35-0c91-3dfa-9e8a-1e8681f7f5eb | -4.40784 | -49.96581 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1414b28a-1fcb-3b46-9aba-ae5ff4d4efc6 | -4.3003 | -50.77897 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a494dd5-a48e-35ae-b5e8-c95e31fc46fb | -6.10323 | -47.65766 | 2026-10-03 04:40:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 135479cd-42db-39f8-9ba6-8c6643afea24 | -5.42772 | -49.14497 | 2026-10-03 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e08478e-e114-3ff0-8d7f-d8fbc2efdf00 | -11.71549 | -43.48808 | 2026-10-03 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 571a7803-839d-375a-9f4e-210dbbb55925 | -6.15754 | -49.48198 | 2026-10-03 04:40:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ed47b2f-45ee-3561-b14d-29e6afab95b9 | -11.203 | -54.12659 | 2026-10-03 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e0471d7-1da0-3f22-98a7-8cb215b3b7bb | -10.36715 | -39.49734 | 2026-10-03 04:40:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fab1a0e2-42c7-3eec-a1c1-201dc980787d | -4.29468 | -50.7707 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50ec6666-be7e-32a9-8fed-b97a37dedaa3 | -4.28564 | -50.78412 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a48a5b01-da89-3c58-8335-ba68e3a62217 | -5.94254 | -43.64737 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 84addafb-2066-385a-a0c5-f0b90344038d | -5.15062 | -46.04167 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1098c35f-f026-38d5-bd70-8565151563be | -3.51769 | -54.60581 | 2026-10-03 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cf7fc844-c176-392a-a880-15b1d60cfff8 | -5.99573 | -53.55046 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 302b6463-271a-3c0c-a6d5-fd4ff461b47d | -4.29182 | -50.7888 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ed70c41-f026-36a2-bdd8-4ce0c448c3ec | -4.78997 | -55.71139 | 2026-10-03 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9223e882-c2e2-3a2b-b467-f06063bf3a53 | -4.2924 | -50.78517 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d4b3753-3aa4-3240-bce1-5ba4c8c672d0 | -7.46352 | -54.98945 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f4db7e1-693a-37a7-b933-343c458bca2f | -5.60388 | -44.90459 | 2026-10-03 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d35c44bc-d414-302a-9141-1ed10f3a536b | -6.00633 | -53.53301 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddabffaf-93aa-3e72-ab29-380f940af02e | -6.9185 | -59.28099 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cd0f624-0a22-3156-a99b-d8661c51803a | -5.59925 | -44.90896 | 2026-10-03 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecfbdee1-71ff-3322-8383-1f0434d37558 | -9.46483 | -40.37222 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 65f71a63-3ec7-3572-99be-f98ee5189628 | -6.20108 | -60.02835 | 2026-10-03 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00b1582f-505a-3cb4-a63f-53ece1c4ce9e | -9.45409 | -40.36683 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 1a2eceac-da97-3c1b-9692-87db97314f63 | -5.74018 | -45.14257 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3a8e5ec5-e134-3b7a-9ebb-18f6b0bcecc5 | -5.21725 | -46.02461 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 411268b0-519e-3036-8ace-b889efbaf1fb | -4.28621 | -50.78049 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da24ec9b-f66d-32fb-8ce1-f076d0e73358 | -5.63621 | -44.36657 | 2026-10-03 04:40:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1181732a-3e30-3dd9-9b56-85eca8dfba58 | -5.74835 | -45.1553 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0f7a373a-4eff-3f67-9638-00dabe12b49d | -9.46628 | -40.36076 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 12573116-69ac-38fb-910e-12713d77cb51 | -5.19648 | -46.16348 | 2026-10-03 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4db0a6be-6be5-3f70-ab2a-b09073739236 | -4.31606 | -50.78884 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6852fb4-2ed1-32a9-9ba5-63f323d36109 | -4.30368 | -50.7795 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a653b785-5d5f-3efe-a1ea-342fce179535 | -6.05506 | -62.53231 | 2026-10-03 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13ccfda2-9bfb-32c9-a19b-3743f92f84ad | -4.29692 | -50.77845 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b675c0b2-8728-3419-adea-108daa6dc745 | -5.85711 | -53.47333 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32b5f8e2-726c-33fc-aa42-e483c68fbf7c | -3.8483 | -55.96297 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b57a43be-af47-3576-b3c7-5cfe36a39272 | -5.72284 | -43.27786 | 2026-10-03 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98949cd7-f768-321c-bbf0-e75595d0d8c9 | -3.62707 | -60.20677 | 2026-10-03 04:40:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad39e1ba-0cb2-3831-b084-a28cc926228e | -6.02331 | -43.59613 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 507a0e52-91b7-3598-98b6-bc3015218278 | -6.20469 | -53.26438 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2ba8f41-91c1-37b4-82d6-1f8b0eda0f3e | -4.26434 | -50.74379 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4dddb95-4763-3655-9c62-05f418be091e | -6.20834 | -60.021 | 2026-10-03 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f4f08d1-92bf-3360-8efb-ed1a11a1b5e3 | -5.85678 | -53.47052 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6335c18e-15d3-34c3-967a-ada99d7a5c01 | -5.89479 | -55.48848 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aeca4f46-007b-3eac-adc7-be9fc297e2e0 | -6.20908 | -60.01682 | 2026-10-03 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 245bd91e-4244-390e-8cc5-3647200dd9fb | -6.24959 | -52.68736 | 2026-10-03 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e65886fa-b748-3a10-9a9d-2a8edb514976 | -6.01995 | -53.54425 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f10788a-7134-3ac2-b274-b111e3fc1df8 | -9.46115 | -40.35614 | 2026-10-03 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f849110c-2399-39f3-bb27-29f7e52b1aa8 | -5.88138 | -49.0499 | 2026-10-03 04:40:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README26.md)
