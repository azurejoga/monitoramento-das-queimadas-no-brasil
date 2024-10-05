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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57081cd7-45a7-3beb-b96f-36ea1b500f0a | -9.58548 | -50.17945 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98656367-b069-3802-ae50-98d52791f1de | -9.58327 | -50.17196 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d36fd4c-4686-36b9-a5c5-0e7927fcbf04 | -9.58272 | -50.17545 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 755c8251-a4b7-3e27-ae17-1c379b0571d1 | -9.58217 | -50.17892 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71e41738-40a2-380f-844a-aa80f784df33 | -9.58206 | -50.07183 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68014be7-3264-37b1-8c7f-e815e9af4059 | -9.58162 | -50.18241 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 010fee12-a401-3f64-8ad7-df40ea93b3d4 | -9.58096 | -50.0788 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dd8e3e4-84aa-34ec-b85b-672c03939827 | -9.58051 | -50.16795 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98463ac5-9254-319b-968f-107290adbe75 | -9.57996 | -50.17143 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1be399c3-809b-3434-a4fd-f38919ba5644 | -9.57944 | -50.21777 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7df8164a-4df4-3757-9106-bb9cf47c5628 | -9.5789 | -50.22126 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e477e031-ea18-35ac-9043-098dd5c84157 | -9.57832 | -50.18188 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25e41033-c610-3af6-980c-417cde5c8301 | -9.57777 | -50.18536 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba1cb443-6be1-36f7-8176-1bc7dc7d8955 | -9.57446 | -50.18483 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42a508a0-ccfe-353c-b1c8-86141a5cebc9 | -9.57173 | -50.22368 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dca7a590-22cd-38e7-b679-1001e3825486 | -9.57118 | -50.22717 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90c9c246-98ee-3162-9aec-1ff04ed80624 | -9.56787 | -50.22664 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36c21b4e-5636-39b7-9de7-0cf2aea3454d | -9.56733 | -50.23012 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c62b3f7-6e1d-3fac-8219-1d36e5a78ced | -9.56457 | -50.22611 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14bece37-e31e-3ae9-bd63-5da97a511d3b | -9.56402 | -50.2296 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7756d0f8-f1d7-352b-bd69-e08189b17062 | -9.56291 | -50.21513 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62206ebc-4ec6-3699-b185-1ae8981592d1 | -9.56236 | -50.21861 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 053e6add-60b6-3d72-bad3-4f94ca5b3bba | -9.56181 | -50.2221 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0122d7d-df3f-34ca-94c8-41e169209854 | -9.55519 | -50.22104 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c75b210b-8935-3423-b91f-4cc1867a6927 | -9.55244 | -50.21703 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1e5bab7-a1f7-3f81-bb02-b659c9d80fb2 | -9.55189 | -50.22051 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18948557-ba97-31cd-82c3-b9f622810859 | -9.55053 | -50.0775 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c50fadae-8d44-3f2b-87b0-8426eb7e644c | -9.54722 | -50.07698 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c597bd6-525b-3c5c-930d-d1b9dd1aa96f | -9.54295 | -50.21194 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a28536b6-e3f9-3614-94a0-a71b00796bcd | -9.5424 | -50.21543 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83679e34-6dab-3096-930d-1c9677517608 | -9.50381 | -50.20211 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb435089-28d2-319d-97e9-244f5f3062bf | -9.50326 | -50.2056 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62f81c12-0085-3157-80ec-f2cd2267aa01 | -9.50105 | -50.1981 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcd7aa74-5958-3dd2-8260-11c0f8c171f0 | -9.5005 | -50.20159 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39fe4696-f9a0-33b4-81ec-5ee1a14eb9b1 | -9.49995 | -50.20507 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11cbec95-b5a8-39eb-b85a-bcbc49128f54 | -9.49774 | -50.19758 | 2024-10-05 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 707ff651-4ecb-3fce-92c3-239ec36cef89 | -10.50251 | -50.26538 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f47f4fc1-72ad-3f04-aac2-82e32f535632 | -10.48983 | -50.25977 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9eb553d-8174-393d-b60f-d4a7c7ddcb27 | -10.48652 | -50.25924 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 678f9d48-e21a-3764-a01e-284ade3bab50 | -10.5386 | -49.11536 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0a52069-ebdd-31f7-8164-700492d63398 | -10.53525 | -49.11484 | 2024-10-05 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f88dc67-ba5c-3325-9a08-84e50abff25f | -11.65102 | -50.47899 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b224fa8-6562-3b49-bdc2-6ffedc94bc74 | -10.84555 | -50.3311 | 2024-10-05 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb02fd4c-48cc-311f-bb25-b6ebb381e8ec | -12.13177 | -50.83383 | 2024-10-05 04:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0077c8af-3cb2-3dcd-9765-0d9ef66ab921 | -12.12847 | -50.83329 | 2024-10-05 04:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c47edf4-cc03-31c7-961e-5eb33118f710 | -12.1904 | -50.08899 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7514a5c5-5a6e-3a3f-9aeb-75d12629b777 | -12.10482 | -50.00651 | 2024-10-05 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b30ce652-bb90-34b1-a284-a83ded4d1481 | -12.04752 | -49.69464 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e5ccafb-d1d9-3f5a-8e64-3075a50545ca | -11.95423 | -50.1236 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d63fe3e9-23c5-327d-9a7d-06eea2da8c5f | -11.95037 | -50.12659 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d225498-3aa4-326f-858d-ea3b25773d1b | -11.94989 | -50.17352 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcabcea7-401d-347f-9533-f840b9e35888 | -11.94502 | -50.1403 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b52133f-5d81-3d3b-b410-83eec9155def | -11.94171 | -50.13978 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d02b15e6-08a2-3e22-98dc-694617ccd67d | -11.929 | -50.13412 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4adc2547-598b-3050-9509-845f85b07581 | -11.92898 | -50.11243 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ca4d4fb1-fb88-3080-8078-29828c307ce1 | -11.92843 | -50.11596 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d8f6799-9749-33c8-a583-66bfffa7b5c6 | -11.92623 | -50.13007 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53a36a54-a612-3c61-bb56-2616aad1ebad | -11.92568 | -50.13359 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 265fff5c-3992-3e7e-a64b-55aa4c2723e3 | -11.92513 | -50.13712 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34470694-8f26-3523-a12b-0d14b7a8bb42 | -11.89585 | -50.12882 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7251f2a2-9bb0-3526-9022-55036275364a | -11.8953 | -50.13234 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18669af1-f86d-343b-b3a0-d2335bca7962 | -11.88812 | -50.13481 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9459b854-837c-3279-9062-e6e262aa9894 | -11.88371 | -50.14133 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77876150-f20c-3cea-8744-895dd995f992 | -11.88316 | -50.14486 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 451f0716-73bd-3c1c-8bcf-917d063dd1e5 | -11.88261 | -50.14838 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67ecbeb0-a441-3bf0-aa99-002b87822d8e | -11.53639 | -49.64392 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adc55510-2cfb-30bd-be58-e4b0884a3a54 | -11.08012 | -49.60878 | 2024-10-05 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86136cb2-50a8-392b-8688-c7a4cd5835bb | -11.07958 | -49.61233 | 2024-10-05 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c76bae71-90c1-3dfb-9922-80fdee38c241 | -11.07625 | -49.6118 | 2024-10-05 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 287a1e75-f3bc-3918-a78f-005a8462dd00 | -10.97643 | -49.66474 | 2024-10-05 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 480971d0-6d2e-3b24-97f6-cf7b23ec56ef | -10.96907 | -50.17181 | 2024-10-05 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f705c1b6-93a6-3fe5-a1f3-cac0036a4e44 | -10.95571 | -49.57803 | 2024-10-05 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba8c3c7b-17df-3b3f-929d-00887cb71da0 | -10.95516 | -49.58158 | 2024-10-05 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1aac237-5def-3efc-bb93-85cac80c3790 | -10.93472 | -50.17323 | 2024-10-05 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1df828a1-2fbe-34ba-aa3a-a55af2b1d2be | -10.92427 | -49.69641 | 2024-10-05 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05f50b32-4393-3af8-8093-6cda0f577d23 | -10.86902 | -50.11605 | 2024-10-05 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fdebb60-6742-3037-9f6e-270a7551a5f7 | -10.81935 | -50.10816 | 2024-10-05 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9511bd0-0633-3bba-9c13-60c66dfcde86 | -10.81604 | -50.10764 | 2024-10-05 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5e9088a-ef63-3b75-b6c1-46af618c1fc3 | -13.19274 | -50.63023 | 2024-10-05 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71b10912-9a4b-32ba-be5d-2360b949ee8b | -13.19219 | -50.63377 | 2024-10-05 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73a8fe0e-11cb-3ec9-aa1c-eb05f1cde93b | -13.15535 | -51.1925 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f663278-6187-376b-aa59-f8c579211031 | -13.1548 | -51.19603 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 021db287-c64f-317a-b3ac-adafeec1ba45 | -13.15424 | -51.19956 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ee77bc7-6cd2-3e3f-9fab-0889190b5d81 | -13.15205 | -51.19195 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 745cc60c-9f9b-34a6-9c2b-638e7087a2e9 | -13.15093 | -51.19902 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a864a2d-77d6-3001-925c-98134d2677f1 | -13.14985 | -51.18435 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75e39b03-c053-362c-b939-8796d4df8d31 | -13.14929 | -51.18788 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1241f00b-1d42-3099-948f-803f2c73953a | -13.14874 | -51.19141 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63096bb8-ec29-33be-a0ba-9c00761af5b8 | -13.14818 | -51.19494 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 555bffdf-db3b-3518-9428-c35e41411811 | -13.14762 | -51.19847 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc87fe14-afa0-30c6-89f0-ef1fa56b4cde | -13.14654 | -51.1838 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65f41dbf-7e95-3233-9ae2-df2448b1a74e | -13.14598 | -51.18733 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6b55fca-72a7-356a-a607-96e2537f3b63 | -13.14542 | -51.19086 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 573d2703-80a3-3a66-9888-03a01bb3e4fa | -13.14487 | -51.19439 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32db935f-df47-35c1-816b-3072f9b227e7 | -13.14323 | -51.18325 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0439c5d-196e-3ae5-b06c-a19251c7a1c0 | -13.14271 | -51.16512 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b09b562a-242d-36e2-b6a3-8d5ff396cfc3 | -13.14156 | -51.19385 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e420dcf-86b2-316f-aa9a-e1d0a2b2ae8b | -13.13995 | -51.16105 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7eb2b4c-c4be-356f-90be-ca50d7abff9b | -13.1394 | -51.16458 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 975fec21-a391-3ad6-83c9-a6382e31a2cd | -13.13936 | -51.18624 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README104.md)
