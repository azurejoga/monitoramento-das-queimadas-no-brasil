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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d15e5883-b83c-314a-9efb-0455ffe0c191 | -7.50607 | -45.83733 | 2026-08-01 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27e9a8fc-6a34-36da-adf7-0cd92cbe3c56 | -8.18933 | -55.43484 | 2026-08-01 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2ee81f24-054b-3446-b0fe-b390815255b5 | -6.56146 | -55.1548 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e043b897-9486-3614-a70b-d1973aade8a3 | -7.50535 | -45.84258 | 2026-08-01 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3da0db1-101b-33ac-8cae-45e2ce44f176 | -10.07735 | -60.50137 | 2026-08-01 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74acf51d-bd11-3d7f-a625-77f8764abe5a | -6.56435 | -55.15923 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58d867f0-36eb-332f-8f0f-6b00b7ad830b | -6.55739 | -55.15813 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1b90af75-bb0a-389e-92fa-842c46805b0b | -7.87058 | -61.68662 | 2026-08-01 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3572f7e1-380c-3bf9-8201-1b4a6a0a4757 | -11.22261 | -54.84195 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 838853be-6114-39dc-8187-4af7ed6839f7 | -8.34181 | -45.98863 | 2026-08-01 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caebb9bc-fd96-3d72-a576-8634fe58a59e | -6.71727 | -44.02039 | 2026-08-01 05:16:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0183937-13df-38f7-9bbc-3e415909f6b6 | -9.27674 | -60.65329 | 2026-08-01 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ffe81f8-edc8-38b0-b5be-7f6bec0a72ce | -11.1409 | -49.90424 | 2026-08-01 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb991c8e-f995-3c4f-b21f-a8c5e3af26af | -9.15847 | -48.83314 | 2026-08-01 05:16:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 611aa674-6aec-3c42-b927-b0cb25bd644a | -11.24371 | -54.85421 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3635a2a6-5f27-3651-a752-5702b9d6e1d3 | -12.24162 | -47.18526 | 2026-08-01 05:16:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09276c2c-8ce7-383e-bc5b-d47b01d62c37 | -6.54345 | -55.15598 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54ed8381-f5e6-32b7-9074-80d69f6df9e4 | -9.87858 | -48.73273 | 2026-08-01 05:16:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc2f6210-01d4-30c9-9a1d-b86e2fbd778e | -10.0817 | -49.12384 | 2026-08-01 05:16:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62c8d7f9-6a61-34be-9fea-cea0d6d675a5 | -5.31751 | -47.48272 | 2026-08-01 05:16:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49ed3641-2202-39e2-9ddb-dded4be92fa2 | -6.65143 | -43.92108 | 2026-08-01 05:16:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8b38ee5e-d8db-3962-a7d5-df0c1da5952e | -11.76962 | -50.16814 | 2026-08-01 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d31cdb1c-7673-3e58-b612-9ca2fe5356ef | -9.59377 | -48.54912 | 2026-08-01 05:16:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14b1ae4a-ea96-33b6-88e1-456fa4e05a48 | -11.23997 | -54.85367 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa548229-e0ad-3aec-ae32-f1609df360a3 | -11.24809 | -54.8502 | 2026-08-01 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 9ec57b82-69f8-3840-bc4b-226d3d8045fc | -5.28342 | -56.01729 | 2026-08-01 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 263ba285-3988-3769-92b3-94d9dccd6d37 | -9.59422 | -48.54551 | 2026-08-01 05:16:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea30a424-05e8-324f-ac74-839c99c344c0 | -6.56879 | -56.53185 | 2026-08-01 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af32a88e-e8c7-32d0-9cef-f87c64795cdd | -6.56317 | -55.16695 | 2026-08-01 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d05cd0e7-2d1d-3416-91be-306b4a3488f5 | -7.29641 | -55.31696 | 2026-08-01 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 584a872e-19c9-3627-b863-f806dc43e7da | -14.08607 | -46.29603 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c01ae662-240a-3c29-b133-e0c4db126212 | -16.04697 | -48.5292 | 2026-08-01 05:18:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09571138-2378-36d0-8bd4-8e88e9cad767 | -14.07852 | -46.26123 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 471fd5ea-5980-3d38-906c-718e6bbb5624 | -14.33472 | -48.03176 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e10e61da-3d9e-38f2-8e6b-fb6565f60fe0 | -13.16644 | -53.25718 | 2026-08-01 05:18:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b456f3f7-ae7b-3c77-bd6c-0475adb63000 | -14.08737 | -46.28395 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 171ee3d9-78f5-35f8-ad3a-844f89b51ccc | -14.08626 | -46.23055 | 2026-08-01 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d25934a-7883-39a6-a430-55466bbd096d | -14.07729 | -46.27357 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dd0a7f11-ceea-3dca-8b1d-1d1ae0d9ad88 | -14.81553 | -48.50817 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b5b0d4e-39a5-3a0a-8bf3-8e0e9ac935d6 | -14.07457 | -46.27601 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 35172dfc-92ab-3048-9f0f-612780480f7a | -13.06075 | -52.72866 | 2026-08-01 05:18:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bb11a61-09e2-366c-9f05-58d70d603c2c | -15.82931 | -48.18214 | 2026-08-01 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8e4e0569-78ec-33c2-b26f-d044b96d4dd2 | -14.06588 | -46.2936 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4e3da547-5075-3b1f-acd6-338896684c54 | -12.25034 | -59.32019 | 2026-08-01 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1daf9b8-ecaf-310b-9063-c1a940ba79f8 | -14.07324 | -46.2885 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9c2b51a4-ceb2-3e31-9164-b1363e9e7a24 | -14.41461 | -48.0413 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9965a88-d729-38d9-95ec-cbbe16280dd7 | -14.3353 | -48.03399 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41c2bc74-116c-331b-948a-b6eaa69d146e | -14.81346 | -48.50663 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a18f150f-8c40-3825-894c-2d91cdee44b6 | -14.08152 | -46.29931 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 61bc618e-c226-3030-934b-a7a2a0c8a910 | -14.08699 | -46.24498 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7adec6cc-ea65-3c8b-8279-a4438e6594c8 | -14.08808 | -46.23411 | 2026-08-01 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f82a84b-6b3c-3eda-803d-2a7e12ce928c | -14.07864 | -46.30177 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0d2a672e-ce58-3a74-a6c1-b85233038839 | -14.07042 | -46.2509 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf4d7a32-a27a-3040-96a6-c3b08dca4fa7 | -14.77203 | -48.30233 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe21bf42-0a67-3d83-9f63-0c17ab20c6c6 | -16.40469 | -53.34819 | 2026-08-01 05:18:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 660b7e9f-c4c3-35e6-8fdf-9f449c30151f | -15.81745 | -48.17676 | 2026-08-01 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb8f786e-d5d8-35de-85f7-22e828711510 | -14.08672 | -46.28997 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c39352ee-e693-3fbd-a464-4946ededd5d7 | -14.08382 | -46.25338 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ddd3e69-6c7b-3d9d-9c34-910eafe05c10 | -16.40415 | -53.35251 | 2026-08-01 05:18:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea99f0fd-013b-3078-bf8d-5902642945b2 | -14.07996 | -46.28946 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| de4205ec-7d53-34ed-b6af-823234c0cb96 | -14.08508 | -46.24163 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04c16f40-04ed-3d3b-9ba1-66bd39904f0a | -14.40852 | -48.04062 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3174d31d-5118-3ef5-b350-28bae4c49c4e | -14.33477 | -48.03894 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 011dc495-8c44-36f1-8f2e-0630d9a200fb | -14.08192 | -46.22732 | 2026-08-01 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d44271ea-7a71-31ae-a353-1c2a119cf306 | -12.19933 | -52.86469 | 2026-08-01 05:18:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee2ddff4-718a-3cfe-9bbb-3dcfba88f400 | -14.08276 | -46.287 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9512da92-4179-3bc7-8796-2a3c5f50784e | -14.07792 | -46.2673 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7794e510-51a0-3ffc-8f5a-90bb70a6a998 | -14.06721 | -46.28113 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cd9ce760-8885-3150-b98e-036cdeb314d7 | -14.08261 | -46.26469 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 28a826a7-b391-3aa1-8499-08a88cf8c412 | -14.08402 | -46.27448 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c27ad01a-b1a5-3d28-a4f1-4389f23c467c | -14.08134 | -46.23312 | 2026-08-01 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 353b366f-6858-3541-bab7-468fd5a25db4 | -14.4141 | -48.0458 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b6917a9-1d0e-3fe3-9ce5-30011dfae04a | -14.87754 | -52.76471 | 2026-08-01 05:18:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bdba9cfc-7f7c-375c-94de-964dc99ff660 | -14.08564 | -46.23636 | 2026-08-01 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 302c9e9d-4cb1-3618-8a1c-32403376e1d5 | -14.0845 | -46.24705 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55ea6aa1-8c20-3114-b5e8-5b69c74a8a6a | -14.08891 | -46.29359 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14aab145-8805-31ba-9aea-0f3924881329 | -13.95295 | -47.83272 | 2026-08-01 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d53cee37-881b-3c09-b0a0-6aeeb125b55b | -15.81773 | -48.17495 | 2026-08-01 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76f05a9b-13d4-3620-b372-3c206f3d3159 | -14.06787 | -46.27487 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7f10f048-16b4-33a7-81a4-7d8df9eace56 | -14.06853 | -46.26866 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 45901ae9-baf4-31bc-b9f6-125c5081a6d0 | -14.33941 | -48.04463 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f652241e-5d35-3211-9288-0260e229f30b | -14.07951 | -46.2297 | 2026-08-01 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbe3de15-8791-36d9-bf28-06c2d2f7ed33 | -14.08129 | -46.27701 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 353083b7-b629-3bf2-a0a7-3f0ab63276b7 | -14.81936 | -48.50769 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d9c0d29-8ff7-3a71-be21-e13652c4f5c3 | -14.08338 | -46.28084 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e5fe0f21-502c-3a8c-8a47-b7e349f09cf2 | -17.46408 | -51.7352 | 2026-08-01 05:18:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bdb63362-c653-3eb0-bce5-4c870845d07d | -14.07104 | -46.24504 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f0dc89d-6347-3c73-bc8b-9962af51d61a | -11.88738 | -57.14096 | 2026-08-01 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7111476a-17ce-391a-9f49-04e43ace06eb | -15.81793 | -48.17221 | 2026-08-01 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1ee1773-715c-3c3a-8096-6b8c21c38fec | -14.06918 | -46.26259 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 29cdc4ad-b7fc-351a-b935-9f1283605014 | -14.33419 | -48.03641 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6904e2ce-d7b3-371a-bdf1-983b9b694d9b | -14.81299 | -48.511 | 2026-08-01 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a25e283-887b-3e2d-88d3-8d74d8768ee9 | -13.95293 | -47.8332 | 2026-08-01 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43b895ca-2f7b-3161-81fa-95fb0e54c094 | -14.08197 | -46.27064 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| aca76749-d302-3e63-af7a-8481a15320a3 | -14.0739 | -46.2823 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6264383e-d520-36e0-b054-41cee585144a | -13.95347 | -47.82855 | 2026-08-01 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ae75476-58be-3bc7-a2a5-4a493279a3f3 | -13.95174 | -49.14789 | 2026-08-01 05:18:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cb5da04-0d00-3e77-8dd4-6e0495d5563d | -14.07479 | -46.29848 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 49cbfadf-de0f-3943-8962-31af59b04baa | -14.07911 | -46.25534 | 2026-08-01 05:18:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d79df786-1629-35bd-8162-5bf99b10724e | -15.82316 | -48.18161 | 2026-08-01 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README24.md)
