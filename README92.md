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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd97ea9c-409a-3e8a-817c-1d7683fb82d2 | -11.44547 | -47.17852 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbc7df1c-dc11-35df-85a5-5492a4c01073 | -7.66969 | -47.28676 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6089406-a8a2-3bf5-9b7e-ff4619882d00 | -6.05881 | -44.6198 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89db77cf-86b8-321f-b790-7f866e8549e3 | -4.85639 | -45.66724 | 2025-10-03 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62f6b009-1f05-31d2-b854-fd2202e9bdcf | -7.75455 | -46.24712 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d688947b-b693-3f96-9572-8c61df94e58e | -11.91145 | -46.75231 | 2025-10-03 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf0f1796-c93a-34f7-b717-60a1259f12ca | -9.12919 | -45.92619 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0219a7a-a02d-399d-8f31-3290c0e272e0 | -5.6398 | -43.90219 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 754e113c-3c4a-3344-88ca-bee84deef404 | -11.62974 | -47.99088 | 2025-10-03 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 12fe65c7-862d-3950-afaa-2b010d4e4433 | -11.53479 | -49.82046 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50dd38f9-9a66-386c-90f0-aca1e6bd9c50 | -9.34719 | -45.91825 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78076bdd-9586-35ab-b67c-d92345502354 | -6.68812 | -42.83263 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c1c918d8-096d-3af1-8e73-764d9f239887 | -5.48935 | -52.13388 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9d3a089-25f6-3552-9a94-41b1933aed27 | -8.61143 | -54.96584 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 188df6d0-068f-3633-910b-e5a0d72c34bc | -10.89776 | -46.72858 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb60921b-0e9b-3813-9f01-1f640998a272 | -6.66224 | -42.78485 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d9ea5093-980c-3b2a-b4ec-1bfde2fa1170 | -5.54553 | -44.64803 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 339d95b2-824b-328c-b390-68e636f5a06c | -7.78586 | -42.56621 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9efbb12c-1b04-3a4d-b343-d23f1d1eaf60 | -6.74093 | -44.57934 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 151a1ffd-662d-3f09-89ee-dab9c37492e0 | -5.64611 | -49.12909 | 2025-10-03 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 311bd4c1-dec8-33e0-8e27-389541f8dffd | -10.20485 | -43.05937 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 68e3b8e6-bfa0-3fdd-abfc-002e9b89c029 | -5.81038 | -43.81716 | 2025-10-03 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9ed7ee37-37df-3548-a5b9-59813831e0c0 | -7.78532 | -42.56997 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 32a7a684-bbb3-34cc-8898-6b4d2badcf6b | -11.79859 | -47.9335 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ab34ea9-71fa-3275-880c-70493ba63977 | -11.14705 | -43.38193 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 25c400bd-a6d7-37ea-adce-6234cac6044d | -7.78063 | -42.57316 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 413342db-34c0-36e3-b5af-a8307a2f1b9c | -11.84618 | -44.95269 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b6edaa7-e5bd-38f4-8657-2e442b32187e | -7.00207 | -44.50704 | 2025-10-03 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f17fa7bf-bfeb-3d05-85ef-1557d05ca462 | -4.6679 | -45.80298 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 866e5be9-4f62-383e-b09e-2da78e079952 | -9.76266 | -46.22871 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 212c2796-b5c8-30a5-8090-02e9a24e48a5 | -9.93054 | -43.59156 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfb37329-db20-3ccf-ace8-ab331cbed04c | -10.86067 | -47.25119 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| baeae3b1-2526-3de7-9ff1-1b8519e45c22 | -6.29646 | -45.91423 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03dd9446-ad2c-3a26-bd41-85b1b9174df4 | -5.83905 | -48.87173 | 2025-10-03 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78adf303-12b0-3f33-8d02-377f211051da | -7.72868 | -46.23188 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66bd0409-579d-3fca-8946-3fdc5165a2d8 | -7.75286 | -46.25824 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1e730b6b-842c-3dcc-955d-1968fcdf3cb9 | -5.38734 | -48.95457 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9321b662-657c-322f-8701-62b7b1dabad9 | -11.32061 | -49.01395 | 2025-10-03 04:32:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82747340-40ae-3e4e-881a-b3fbb1fae21c | -11.12059 | -43.39061 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a00e9990-0047-3fc8-8bcf-a01351c76fd2 | -6.79285 | -45.5746 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce072af8-bd99-357a-b783-a80574f9a60e | -9.62281 | -48.19313 | 2025-10-03 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5d496b9-f589-3fc7-9069-37c64c244819 | -11.56889 | -47.65779 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 900d557c-a986-3378-ba4d-1a49b15a1864 | -5.83709 | -45.80371 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 964da703-8714-3aff-bca5-a7929aa8d44e | -7.44817 | -46.98546 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38c961f4-982a-3af0-ab79-9aa9e98f1876 | -11.4664 | -44.96203 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 996f97ad-be87-3fe1-9472-5c16ce0af36d | -9.94626 | -43.73623 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f8af8d2f-98b7-3dcf-a04b-9835bb5f1d4e | -7.20028 | -45.38867 | 2025-10-03 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e60312f0-8f65-3113-9a7e-d1af671e0aec | -9.90079 | -47.71917 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 532c1035-1129-338b-97e7-246d84a071f2 | -11.11226 | -43.19371 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 83f9d9ae-925c-3db2-b9b2-e4369033b0be | -7.78117 | -42.56937 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 9170b15d-392d-3dde-8846-39f9ead4f6c9 | -7.75628 | -46.2357 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3edcb0f-5084-3dfc-a691-52a01ae2cf30 | -8.53974 | -50.15438 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 151313e2-3f8b-3fb0-91f3-d0cdcd21ba9a | -8.88502 | -46.59429 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddfe8cef-68f1-307a-babf-544f37f8c427 | -10.54192 | -43.64444 | 2025-10-03 04:32:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0273d6a1-c3e8-3999-a3d0-7561170abd97 | -11.13413 | -47.19895 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49b36b09-3b40-3e67-92c9-48a99ae32a09 | -11.91174 | -46.28262 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13d38240-f947-3a66-a4ff-7cfc897a86d1 | -9.04372 | -46.67495 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8d8459c-3fbf-37ca-b408-663ee503260f | -4.95576 | -45.77197 | 2025-10-03 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b1061df-d81b-323b-b183-cc563dc6fbe6 | -5.64553 | -49.13271 | 2025-10-03 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04699873-d381-38b3-a9e4-ad4d82d625df | -10.98542 | -46.67936 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 24b88d59-8a08-33b9-b84a-f5afd3a217f8 | -8.71454 | -47.13493 | 2025-10-03 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 006682fa-d5d8-3050-85e2-2ec09719a03b | -9.90356 | -47.72323 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b0d2d44-9618-34d1-9769-18409ff940bd | -11.13209 | -43.39869 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 77167fcb-e083-3830-9b95-6132f2e57e85 | -8.17645 | -47.0154 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25e5a104-8448-3f55-8f02-5c8e411bceb0 | -6.34718 | -43.40703 | 2025-10-03 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c5878942-272a-32d7-849e-aa57edd23aec | -11.07853 | -47.86797 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6167487-7961-3e84-9339-ffd92421c1cb | -11.05632 | -47.79505 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de06f1fb-317d-3be5-b4b6-4daabac700e7 | -11.55155 | -47.65879 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 731dc53a-4cd1-3545-9839-0a886f5d1492 | -7.4233 | -40.07257 | 2025-10-03 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5134c088-ca64-35aa-9884-83b1d943a6e8 | -10.89948 | -46.71724 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a841b0d0-6dc2-38ee-9d5b-0b1f8ad5e816 | -8.61591 | -54.96668 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97a873fd-094e-3a89-8ad9-d21c6a7f4d9f | -11.59185 | -47.66508 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8b1bdcb3-73e7-3850-8479-5d468435cfc6 | -11.49539 | -44.99997 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 533fcce0-7200-339f-814d-e411cdb9cada | -7.79218 | -42.55169 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 82d93b9d-ff06-3b63-8230-7f134fe80431 | -7.70103 | -48.08244 | 2025-10-03 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d287274a-a53b-37af-a3cb-827e97a69ae7 | -6.23018 | -44.24912 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3bd821b-0efa-3f49-90bf-e68e2c95715c | -7.31575 | -47.29206 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da944f80-feee-372e-b1be-ac58911f9954 | -7.89021 | -47.35333 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82249b54-9940-3901-986e-67215727f473 | -9.58649 | -43.32505 | 2025-10-03 04:32:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6cd2c909-4169-3b8c-98aa-e19bea116862 | -7.31659 | -42.88361 | 2025-10-03 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 14953e5a-a990-3f3b-a551-284f666f31fe | -9.34412 | -45.721 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f862ca37-c68f-33eb-80b7-8257e5ce29d3 | -7.77159 | -42.5173 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 39d9b911-93c4-390a-a00d-d223f8154ac6 | -6.07081 | -44.61322 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f7bb9e8-f991-3146-9639-45fa7fa8a82b | -6.41448 | -43.84074 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90b09bcb-941b-32b9-bdc5-dd422a53d31a | -9.89364 | -43.70764 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b69a5e93-c071-3744-bc4f-829297b9881d | -11.8142 | -45.03992 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4e8d908-1988-3b7d-ab89-0ada3f6f6a3e | -11.4696 | -45.0192 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 707f3a0f-8e5d-3641-b5e4-b79d1959c6d0 | -11.10009 | -47.81664 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb5de3db-0c6b-3d63-bc75-6a0aa881a799 | -10.59037 | -48.71332 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f654b3cb-c52d-30b7-ac32-ac8caa6ec2b0 | -11.77118 | -46.83084 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5f64c74-ee31-38a4-afa0-c62a80c79b04 | -11.16125 | -47.18053 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aae32abe-441d-3b32-9b5a-6ba6c22a9ceb | -11.05075 | -47.80891 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e5e93bd-02d9-3544-ab43-5746a5a3a9de | -5.4073 | -41.32727 | 2025-10-03 04:32:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 42351355-0f8c-3e35-a393-3c20cb858802 | -4.66563 | -45.79521 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a45e052c-4ebb-3d22-af49-ccd7ce26bd7b | -7.76657 | -42.58266 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b3a028c7-a681-3a6c-abfc-c5d8b27b8684 | -11.78177 | -46.82401 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a966a710-4908-386f-a738-3ac9e2cbe532 | -8.25134 | -50.57327 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ceda542-d271-3444-8570-4aa60acdb4c1 | -7.74887 | -46.23859 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11f527ad-c4bb-32b0-8227-2e33bddbacf5 | -7.75082 | -44.79825 | 2025-10-03 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d7d4b12-1639-3bb8-86f1-08c8eea42b4e | -7.78694 | -42.55868 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README93.md)
