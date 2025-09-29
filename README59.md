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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9619b28c-c04a-3049-9d7e-b633c5771f46 | -8.57554 | -50.91536 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab8b56d6-fd3f-3c31-a482-6fefe29edcab | -4.97581 | -44.50179 | 2025-09-29 04:57:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 774fda96-5c2f-38c8-b55f-4c2f4ea991c0 | -10.79723 | -46.6797 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d55762ff-c876-3092-9dca-beb9cbfd75b3 | -10.80977 | -46.66282 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b4aa4d9-381c-3d57-af07-072a4f96aed7 | -8.2773 | -45.50502 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c41350de-4eb8-3ec5-9140-6c6eb0211d57 | -7.15406 | -45.49707 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c5547fc-f895-3ab8-a81b-a44e37a8cabb | -6.61591 | -44.94037 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c664aaa0-1bca-3c8c-991d-6e970b47cfa8 | -8.27773 | -45.50172 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 97121979-b0c6-37eb-a6f7-358a9cbf22ce | -5.16716 | -45.01462 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 75b817c1-2981-3793-bf8b-afd4b0b08d44 | -3.50418 | -52.46719 | 2025-09-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efafe3e5-0928-3131-b58d-0c5c4f23cda1 | -9.46673 | -52.00878 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f39f7571-9451-3f28-b7e9-09427a84daef | -11.48958 | -43.21045 | 2025-09-29 04:57:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b7205427-a984-3f12-8410-37ea64af14ba | -10.79172 | -46.68212 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78ef090c-cc57-3ac8-8097-31bac74de1ff | -6.8094 | -45.98455 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9579d16-1c75-3eb7-be44-45006bae609a | -10.46126 | -48.1988 | 2025-09-29 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 95c6f675-9e04-3e39-af97-ba9551342bf0 | -7.58192 | -44.80046 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6989f87-2d89-31e4-888e-fe23ddd9f4c6 | -6.466 | -43.93998 | 2025-09-29 04:57:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6107bd14-f399-3fb4-8961-df9ead51b7ef | -7.22953 | -44.78611 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| a3fe74d7-135d-3969-997f-78d9afeedc12 | -7.86518 | -41.06031 | 2025-09-29 04:57:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2308e192-e960-31ec-aee7-ee5a6c5a1e02 | -4.05482 | -49.31776 | 2025-09-29 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cfe1081-9523-3e9c-a317-dd13d7cf470e | -11.45222 | -45.00341 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7497ef91-3d78-336a-aa5a-de869b09d6d3 | -7.89694 | -44.59101 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34868e42-cb6c-38d2-9b77-65bd4b905cae | -6.31234 | -43.45121 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc99e93d-9af5-3583-ae89-bb3a2e2b0f22 | -9.10454 | -45.85051 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0739e551-e237-35f8-af8d-880baf948600 | -5.71465 | -42.86273 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 36174174-4b4d-3051-81f0-15d6507180d5 | -6.06099 | -42.48532 | 2025-09-29 04:57:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ade567cb-08c2-3d04-8d4a-8800683c1eae | -9.46024 | -45.49665 | 2025-09-29 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1300c583-73c0-39e4-9133-9452c3b570b6 | -11.2726 | -47.19725 | 2025-09-29 04:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 42e7efae-2621-3b62-a3c4-ff313a59e771 | -5.16764 | -45.01124 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb6d4cd5-8d62-34b0-a60f-e04c1c3944be | -7.8039 | -46.89732 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6bcca108-e984-3299-86b5-0caca753a4fb | -8.2959 | -45.48781 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bbf047a7-6ebc-3008-949b-94629a872c02 | -3.30837 | -51.66753 | 2025-09-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48e7e56c-0f1e-3233-aa4b-09560f8c5ff7 | -4.76883 | -46.59603 | 2025-09-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 616b7d66-78a3-3d47-b4e5-c73a78d5119c | -11.20739 | -47.74686 | 2025-09-29 04:57:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 86e134f2-4fd3-3320-a634-801eb0aa2eee | -3.82821 | -53.48692 | 2025-09-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c413b788-578e-31e4-ab92-f5a813c11c0c | -6.57391 | -43.40887 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c4313ecf-6002-313d-8f18-36d7b8dde0ba | -7.81931 | -46.99777 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d328a333-be14-3e4e-b68b-a5dc1f226c61 | -10.81971 | -47.93789 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69150895-d596-3454-a2af-5cf46f45f2b6 | -5.7172 | -42.84455 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 53026e47-cf74-3920-af2c-61cd1a986f24 | -4.69058 | -50.47714 | 2025-09-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 710d747a-5b0b-34fa-991e-38667268b2f5 | -4.30775 | -48.09266 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 631b0e1f-b3a4-3ce8-baeb-b52094a65095 | -7.58773 | -44.80143 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f67f7cd-e4ba-367f-bcd0-76360e9762b8 | -11.42169 | -44.91405 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 40af31ee-7036-3f88-9dd2-a3a51a9eb8f6 | -9.05656 | -46.71417 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 76cedf5f-3d2e-331d-9354-9dfa2fb60d33 | -9.08236 | -47.63273 | 2025-09-29 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3faa1955-512d-3f89-9905-876d428cf97e | -8.86364 | -46.59566 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a0edf83-3f00-3099-87be-f431bd4d5b6f | -8.81872 | -46.19664 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79d908ba-cbc9-32be-b6e3-33d96bde53af | -6.83552 | -44.82945 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62ed0bc6-d734-356d-a538-5d6888d4045d | -9.16137 | -50.55822 | 2025-09-29 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ed184cf-a3ef-3097-bea3-da47a4f6b3ce | -10.45212 | -50.85489 | 2025-09-29 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7699ec01-d73f-3d1e-ac33-1361a0862f64 | -10.81487 | -46.66367 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0c6cd00-4ad5-3cff-834b-acb583886394 | -10.82506 | -47.93373 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ba29d07-27b2-38db-9f46-49e1db8d85a9 | -8.29739 | -45.47649 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8a4f336-3998-32e6-936a-1d60a93a621d | -11.42171 | -44.90907 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6b5cc398-f6cb-3876-92d6-2580c27b82b7 | -11.36637 | -45.07318 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3d4fde6-da3f-311f-8fff-ccb567a0c766 | -5.7398 | -42.8616 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c09ba8f9-14be-34a1-8274-4d71eb5fa658 | -3.94558 | -49.13149 | 2025-09-29 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0eda855e-686c-3488-9caf-cc6925636eb1 | -7.73543 | -46.96796 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 858f9701-dc88-3318-afce-986919eb8df5 | -9.64341 | -48.12209 | 2025-09-29 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f99de121-64bc-30b0-941c-c6c25be73b25 | -8.15095 | -46.34335 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01910558-daf3-36fc-bdf1-ecace795cad7 | -7.1115 | -45.53416 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c59f433-5f59-379e-93d2-eed866308174 | -5.09436 | -45.48634 | 2025-09-29 04:57:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0cb5bb3-5828-39f1-b047-0d3a0a89bdab | -8.29844 | -45.50979 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 13e0399b-daec-319c-9bf1-2f435d0f0923 | -7.21498 | -44.76882 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebc7c035-5b2e-3a64-9561-6fd4a0915754 | -6.82844 | -44.8338 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2abc6717-44f2-32bb-a636-6ee9bf52d509 | -6.50194 | -44.11876 | 2025-09-29 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cde4f1a-ff79-348f-a8cf-8119f0c20f10 | -9.0558 | -46.71969 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9f6b3062-9000-3c4c-a967-e4d7237ed902 | -6.1481 | -42.80983 | 2025-09-29 04:57:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5b820c0f-6921-3732-85a1-db787bc72691 | -11.44257 | -45.03517 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08eb00df-40c4-3dc4-baf5-8f477470290f | -8.38655 | -47.99595 | 2025-09-29 04:57:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3f0c26a-cefb-3af3-a64d-79a13157a391 | -4.40357 | -44.07992 | 2025-09-29 04:57:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dea3c4c6-4dd7-3f73-9404-5ca7a95dbdf8 | -10.79882 | -48.9127 | 2025-09-29 04:57:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea11ffc3-b7e0-37b3-94bb-26db343b812c | -7.46798 | -46.29146 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a81e0a8f-cbe4-3fa6-9f96-8b1e7ef89c76 | -9.77321 | -46.18724 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b64a38bd-af11-3538-8d0f-1a3ecd3315ec | -6.11014 | -41.82834 | 2025-09-29 04:57:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e426db90-ac53-325c-ba2c-b662a25b71fc | -3.34518 | -49.22512 | 2025-09-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0269994c-e218-3d40-89fc-83ffc5f4bcdf | -11.45856 | -44.99938 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3972b65e-6ab1-3924-9b70-f47ce1d48068 | -9.41484 | -54.71687 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95cd301d-821b-3ab9-857a-af05402fc2c7 | -7.49659 | -44.30319 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f9f50a2-8b53-3498-b74a-42e621766bfb | -10.81919 | -46.67058 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c3a9ccf-42e6-3bff-a3a0-634a867221b3 | -9.40079 | -54.69339 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11fda8c7-d23f-3d02-b76c-0862476d372f | -8.71618 | -47.98435 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c26daa0c-f87e-3ea4-9722-47dc7d64d3f6 | -10.81055 | -46.65665 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cad4d57-04e1-35ee-821c-a6ebc6a9b58d | -8.27338 | -45.4934 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0568b39c-22be-3391-9c33-6dfa60edc537 | -6.06867 | -42.4761 | 2025-09-29 04:57:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6ef1b9d0-3503-3c23-8036-6d5df9c8292d | -8.29401 | -45.50217 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 2a8e8877-65cd-3b8a-b06f-d84f65f01186 | -7.22305 | -44.79248 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 56876945-e5e0-365e-8d03-bb5c245cd666 | -6.62181 | -44.93769 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b92dece-935d-327a-878b-b26482ae9e94 | -8.30559 | -45.49691 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 433051f6-1329-312e-9674-70541b072d4d | -7.80984 | -46.99543 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 083f63df-66cb-341e-bf2a-41a8289edeb9 | -8.27602 | -45.51481 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 877a3316-dfce-3518-a1bd-4db183a6acc7 | -5.74023 | -42.86185 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 82f4f452-e9dc-3f97-9bc3-9db6210996a1 | -10.40776 | -48.14492 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c0dab08-69c7-38b0-9e3b-411526559caf | -3.48394 | -51.59934 | 2025-09-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12dd3f3b-875d-3953-9607-ff97686afdfd | -8.16219 | -46.33606 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5dd964a-1a54-3645-8d37-9d503d27409e | -6.61825 | -44.93789 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 219edac3-e850-36dd-949f-7d412df8f4d7 | -10.45695 | -48.19711 | 2025-09-29 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96a25a4b-d7fa-36e6-bed3-3934817206d6 | -3.35675 | -49.78856 | 2025-09-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ea12138-bef8-330e-af46-071b49e492c0 | -9.40798 | -54.71231 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc2058b9-029b-333f-abd8-9e9d78105e94 | -11.40502 | -44.90108 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README60.md)
