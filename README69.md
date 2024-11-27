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
| 7cbb168c-2f89-3fbd-b12f-00608b93a9dd | -1.34849 | -54.63081 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46a30cdf-1685-308b-9f1c-d8166bd81b19 | -2.82276 | -46.83154 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50c47dee-6bcf-3111-989d-7821e03f97f0 | -1.91782 | -53.00608 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a864ea6e-3a7b-3054-95a9-436680cb2bb7 | -3.50787 | -50.4595 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d16cf53-2b35-3d57-bee5-c9801db717a9 | -5.00489 | -44.86129 | 2024-11-27 04:42:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c417cd14-6b6f-31a6-a11a-d491ab29e7ef | -2.94199 | -49.12764 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfb2a507-7872-34b1-824b-d886a4931d40 | -5.56169 | -45.38225 | 2024-11-27 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63270ed2-4302-3bee-bf39-a7483a4c8420 | -1.36859 | -52.12456 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7af0bbc1-9006-32e7-a960-3a39c67a8e34 | -2.43786 | -50.41476 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7fe2a18f-35d3-35f4-af11-464da8fb7d1d | -2.46764 | -48.79424 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f878ab39-acf7-346e-a72f-367aacbb1d19 | -1.7681 | -53.6204 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69e0a3f6-d623-39ed-b347-8cd070941a34 | -3.97372 | -46.73722 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce54f301-2b95-3402-8070-d5ee2e5edccb | 0.94501 | -50.73586 | 2024-11-27 04:42:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4be2c6ee-0f87-3bad-8d90-dfcef08c9967 | -3.53539 | -50.45675 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7b081b0-8a82-3a38-b6ea-2c81518d1673 | -4.08505 | -49.33639 | 2024-11-27 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a104b64b-90e6-3410-94db-39d176e5e0ff | -3.10877 | -53.26058 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 36a6e646-c654-3f71-835c-0a5f25e5a2e8 | -3.16859 | -48.4325 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| b55ce924-a319-3304-93ed-398b4df2fc9b | -4.30837 | -48.07971 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e3a2964-94e4-38d1-8cf3-976295bced12 | -2.5867 | -54.05909 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 52ede772-3c2b-3f4b-85c0-50d1671ddc3f | -4.22104 | -50.89265 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b8009fe3-66f9-395c-b7b8-bf1404ca3890 | -1.73453 | -55.44665 | 2024-11-27 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b4ddbc9-3969-3f24-b3e9-cd2adc24f682 | -2.30807 | -51.32285 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2415821c-d7da-3307-b82b-e737b9ea7929 | -2.59709 | -53.97182 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 78ef21b3-da2f-33c6-8e7d-429ba4b4e1fe | -2.80193 | -52.47771 | 2024-11-27 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccb7cd1b-9e05-347f-83cc-0a0a777685f2 | -4.21235 | -48.6607 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 998bccdd-3763-3fa0-b93e-a9ebc4bba24f | -1.763 | -53.62865 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fda4688-d6d8-3edf-a1bb-5ceb33a0fdce | 1.9502 | -60.85547 | 2024-11-27 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66a2b524-1c51-3e03-9531-fd0f59ab9461 | -3.54128 | -50.39781 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2397131-d127-3ccf-9a63-c9e70a4b45e8 | -3.70552 | -51.80363 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a2536bf-7244-336f-b433-255f7e2723cb | -3.06043 | -53.28661 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80e98ef3-78bd-3685-b004-dc637c4be419 | -3.72006 | -50.18955 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c79623f-e740-3eee-937d-e4d1650e46fd | -4.35409 | -48.12993 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f59556e-b625-379e-9c41-7794e1455f1b | -4.3537 | -48.08642 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40266be1-aa0c-365b-9370-41e113217a56 | -1.63696 | -52.49373 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dad0683-073f-3c58-ac64-298206c2ab92 | -4.49864 | -50.44613 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd0aed35-71ef-3b35-af26-d7500c7eec21 | -4.1913 | -48.41169 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5af0944a-254a-346d-b0fa-16409462375e | -2.83864 | -46.82528 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 43163a24-7542-3ef9-8fc0-842b66aff5a1 | -3.45746 | -50.84343 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df98d820-b031-36c4-bcff-e22db57bf6a4 | -1.58951 | -51.27317 | 2024-11-27 04:42:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83e951b0-6b01-381c-8d61-2ba58d7d8013 | -2.69973 | -48.65471 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21e87792-8e1b-3930-995e-ac076917073e | -3.97549 | -48.08164 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ef57e3b-e983-3d81-9fd8-8d29f90ffb9a | -3.11777 | -53.11204 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74eb769c-82fb-3a15-8a32-b0e3721f1560 | -2.714 | -46.26007 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c16668da-ab7a-30f9-a56a-eef6fff054af | -2.38474 | -48.51813 | 2024-11-27 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d47135f-5e53-3f6e-8a2c-0e3e53780c8c | -3.07438 | -50.9461 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df3b08aa-e1fb-35cd-9d1e-e5ea3cdaf776 | -2.26324 | -53.68054 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90ad7a99-f853-3860-9e2d-289ca09e485a | -2.98512 | -49.59111 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87150cff-fafc-3705-a3ae-6b42424f2c03 | -3.97784 | -48.06627 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f94c22e-288a-310e-aeb1-5d1845bbc26b | -3.098 | -53.2589 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4339c771-8bcd-3d35-8eb3-d0ed5d40dd59 | -3.1131 | -54.13433 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98882ed2-fed1-3e8e-a9cc-9f098b2c5130 | -0.2393 | -53.76454 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32f147ad-ed3e-3f46-9296-53644823c6c3 | -1.69936 | -52.76633 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97748e6f-88a5-3cef-9335-a6d682dbb3a1 | -1.78693 | -52.73827 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| edb2cf35-9042-3767-b6f4-0a972899ad8b | -4.1977 | -50.69442 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9274f22e-9991-3bd1-a280-0c04dc259c64 | -4.23846 | -48.67233 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3460074f-62ca-3a37-a4e7-8adc19400173 | -0.27789 | -49.84733 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4045e88b-96d0-3af3-95d9-200bd297fd26 | -3.29204 | -51.15925 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf7bdd2f-e344-3b8d-8dde-7c945f0fe120 | -3.46572 | -50.25218 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a65efe7-d051-3a7d-a777-557ef085f800 | -3.97526 | -46.65115 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ae7259bd-34f5-3e9b-bf49-0ad8e109c3e2 | -2.69747 | -51.8735 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8fb0fc2-7320-38f4-aac1-e4e786e42adc | -5.66434 | -46.42303 | 2024-11-27 04:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 290f62b5-0bd9-3976-be0e-a7c473c65c43 | -3.52996 | -52.152 | 2024-11-27 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ec2a2390-347a-31bc-8b9f-fe8f72c39f28 | -1.55548 | -52.78256 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b35fa9c-6882-382a-aba5-0a2afb6f93b6 | -1.69289 | -52.62208 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb28cb6e-be11-385e-8493-9dec84ab3c76 | -2.56311 | -48.20207 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c1ee5f9-bfa1-3c92-b296-d9d8152ac738 | -4.21866 | -46.44616 | 2024-11-27 04:42:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 519b698e-1117-3e20-9d32-dd27a6b56765 | -4.149 | -43.80783 | 2024-11-27 04:42:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c7f69d05-738d-3819-a7a4-2dae3d83839c | -1.51443 | -52.21687 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 219084a8-d1c5-3096-8a0e-442d5be2565b | -2.65942 | -51.71855 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07e1ee52-1b7b-3493-a64b-eee23c4056b1 | -3.15581 | -51.07684 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d13b6e9a-bb1f-3ecc-8261-2afc27dd454c | -3.50511 | -53.80362 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efbe7c02-0271-3a0c-aa88-1b2f16358c26 | -4.19385 | -50.69734 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bba74349-b345-3e41-8d5d-5d8f1cbb4c27 | -3.24123 | -50.14634 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 823a93bc-2b21-38e4-9ce3-a86dbb3ab4c2 | -3.50475 | -49.46188 | 2024-11-27 04:42:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8196255e-fb32-31da-a81d-8953cb1cc268 | -3.49243 | -50.45005 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eac0b8c8-6efd-396a-958d-9f850bcd4b86 | -5.31633 | -43.07172 | 2024-11-27 04:42:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| baa4316b-31f3-36eb-acd6-47faab0a8a38 | -1.55904 | -52.78312 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e9142a0-7d1f-3774-9db6-fcb013e86df6 | 1.95358 | -60.8528 | 2024-11-27 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 715c71a0-e921-3893-8e50-7e153bd0eeaa | -3.22771 | -54.17182 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c6b52f6-6df0-312e-ab9e-84f7085779c5 | -3.14599 | -48.53374 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f40a043-d885-3913-b053-7e492be4f9be | -3.24453 | -50.14685 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b70759b0-ec02-312a-8ba6-b438452e057b | -1.67805 | -52.44255 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8a262ded-0131-3f2f-bcd8-f8a28463c8ee | -1.30675 | -51.73498 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5bb3f07-3e2d-31c3-9341-b9c68cecfd41 | -4.21423 | -54.37612 | 2024-11-27 04:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b0b80ac-81f7-3391-acef-21d776901593 | -0.9951 | -51.73312 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d3e1e76-6a63-3589-b8e2-091f4544ff70 | -1.38911 | -53.62081 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03172e11-7b2a-350d-9b96-3d34f34dde02 | -4.17466 | -48.451 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ecf59a11-5287-371c-ae8c-83c23f599c6a | -4.4147 | -48.59749 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27d20d8e-c9c7-3137-8046-75ae87e5d287 | -4.2366 | -41.92833 | 2024-11-27 04:42:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4375dcda-0d6f-3278-88fd-5db02648ab33 | -3.2782 | -48.56152 | 2024-11-27 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e71b1159-1986-3096-a353-763fcecbcc82 | -4.30356 | -48.18093 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bd6b5fd-7eb3-3c2c-9dfb-ba0705f63a19 | -3.49234 | -53.81643 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39ab1bfa-9ccf-3dc6-baaf-6c9f9156484f | -3.94734 | -46.9118 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad77d7db-b1af-3eed-8346-88ab35eeed31 | -1.79048 | -52.73883 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de8bafc2-b882-3a84-bf1f-c3648d5eba40 | -4.57377 | -49.68472 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad03812b-e7f7-322e-af2e-7b41b439f31e | -1.89951 | -53.02845 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a240bf4e-fd69-3b20-869c-979b1a750067 | -0.48267 | -48.6328 | 2024-11-27 04:42:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5e3c4a6-6068-31f1-a23a-f859e7a9c384 | -3.11906 | -50.29584 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 080f48de-d179-38fe-a252-4ee05a47345c | -1.19562 | -53.88443 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f72f16bc-8c19-3dab-978b-982c6f63b548 | -5.32116 | -43.0724 | 2024-11-27 04:42:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README70.md)
