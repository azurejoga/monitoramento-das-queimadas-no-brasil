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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69902142-6c08-30c0-b746-052c037e1cea | -10.56585 | -47.89395 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2da1b777-80d8-3138-974d-dc876d0b1920 | -6.29384 | -44.70424 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41d3045f-328a-3526-99f6-be75a056ed95 | -6.56116 | -41.59328 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 11742649-1130-3b4a-912b-3bede36ea5ae | -12.63436 | -45.08149 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a122f56d-cb2a-3a53-8f4f-1b39f74f0ff4 | -7.81896 | -46.46281 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b64bd85d-d097-3080-9188-6c7123118b71 | -11.02883 | -44.64747 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| babd3331-a510-392e-b25a-98767b26e249 | -10.58067 | -49.79502 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb12060e-1206-3497-b986-fda242901dcc | -6.18218 | -43.74372 | 2025-10-28 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 351491f8-61d9-33ed-84fa-38424ff17ed9 | -7.65713 | -38.509 | 2025-10-28 04:14:00 | NOAA-21 | SANTA INÊS | PARAÍBA | Brasil | 2513356 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 90a5e40a-ae6a-30ad-8128-b714e781dda5 | -7.74323 | -45.32512 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a1a1f70-264b-3f05-9c04-e0cf5e448314 | -10.9185 | -50.26653 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b4c32cf-657c-3f17-8b04-f2dcae8ac73f | -6.49186 | -42.22277 | 2025-10-28 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 480d4cfc-5725-349b-a6d7-6e0d67670a10 | -9.93264 | -44.17512 | 2025-10-28 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ffde2f5-fa1f-348c-b47a-3e3b5340fc3e | -7.97527 | -45.52066 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10c22820-48c3-322e-beef-809899e77458 | -12.54902 | -44.93326 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cfe42217-5dd3-3cf5-9f05-768b79325897 | -7.83698 | -46.39745 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fb125390-1483-3b90-9d1b-51f63d7e0aef | -10.57926 | -49.80296 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f85f399-4085-3e66-89cb-34005fd9d5c9 | -7.85196 | -46.39578 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c2ec7e3c-bda8-3552-82f2-0d12c20b5b65 | -6.68993 | -42.04244 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 7b0ad583-087b-31d8-8520-2a7736926e77 | -7.45661 | -47.15802 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aea265d8-7ee0-30ee-9e5e-4e713ca44c37 | -12.39748 | -47.40741 | 2025-10-28 04:14:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc446c9f-1686-35b0-a412-27fe429ba586 | -10.29958 | -47.20461 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3e7100f-b90d-3b03-9c7c-416732f035c3 | -8.04697 | -41.10968 | 2025-10-28 04:14:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 05c9e398-44ea-3b42-81a5-f67df778f51e | -6.84653 | -50.11618 | 2025-10-28 04:14:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bed36121-0d8f-365a-bd73-099cf8af02d9 | -10.76422 | -44.74901 | 2025-10-28 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 80051b8d-6138-3c64-9f89-41e68443fdb6 | -10.87452 | -48.62785 | 2025-10-28 04:14:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ba795939-e951-384e-85b8-7bff6ef70e48 | -7.41666 | -44.64851 | 2025-10-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ab9e49e-d69f-3503-b204-2efa08fecb1c | -7.07423 | -44.94038 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2546af9f-b243-3612-97d3-3aceb3b1de78 | -8.16332 | -42.8278 | 2025-10-28 04:14:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 53006165-9492-3720-ac3f-73970a06957a | -5.63109 | -47.61723 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e59c6e38-9894-3105-a12d-1bb65f211eac | -12.6178 | -45.07877 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 065a2289-366b-3361-bde7-c8c9c60c9e83 | -6.62479 | -44.62605 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd2ac3de-0622-3e23-92be-aaed98000442 | -8.2108 | -43.80806 | 2025-10-28 04:14:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5d58b722-30a3-334f-b606-f9a08dddcf06 | -6.2667 | -41.83195 | 2025-10-28 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7981853a-c940-3f16-be70-d72a6ce2f96b | -12.19827 | -47.16824 | 2025-10-28 04:14:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e19f31f0-8468-35f5-8077-78cf0816799d | -5.67093 | -47.82344 | 2025-10-28 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1c50272-7a51-36cb-921e-45d383c223e1 | -12.21805 | -46.52915 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33f4453f-50c6-36c5-8366-4237fdcd1a6f | -6.49016 | -42.21178 | 2025-10-28 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| af93f4fc-3e83-3966-8fbe-a10ed297dece | -10.30096 | -47.17404 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3972425a-9bdf-3501-8894-9e479169f87d | -10.93052 | -47.60887 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5363decf-db22-3b43-83bb-a50e12c707f2 | -7.89532 | -45.70734 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37fd18b0-d293-3ca3-82c0-1909df7ec29e | -6.16786 | -43.09951 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bff1a650-4543-3c59-b14e-5764fcd7a043 | -10.23548 | -52.14763 | 2025-10-28 04:14:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d84409a8-8f31-30b0-92a8-5296e87d38e9 | -7.35664 | -47.63842 | 2025-10-28 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c09dc46-5d41-33bf-9ebb-e1c087008d5b | -9.95642 | -47.08022 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 243b80fb-dd46-382d-a6ea-44d7a59c43b2 | -12.20523 | -46.50321 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 790730de-c722-3172-82ec-62855dda58c1 | -6.16126 | -43.09848 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9d3861e-42ed-3aae-8fa2-1972b5d6cd34 | -7.97458 | -46.75141 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| f558a01a-ecf2-3cb6-b87f-59bcf26c6793 | -12.26147 | -51.33309 | 2025-10-28 04:14:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5cf09e11-1a8a-3606-b242-d3c33112f9d2 | -6.58483 | -42.69577 | 2025-10-28 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa7b9069-3214-34ff-a315-091c7ab39cba | -9.45871 | -46.86415 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3142c357-97ac-3381-a49e-ef1710d8fba2 | -6.17038 | -46.09246 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3156f0cc-550f-31a8-b379-9d43359e37b9 | -7.97599 | -46.74286 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b2dc0140-8ba1-38aa-9299-390c323d19e3 | -10.36004 | -47.16159 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24d34a7b-9fa9-3a6d-85d2-45e64b4d628a | -8.57094 | -47.02848 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e651bfc-e05c-30db-8c98-dd74795ff1c0 | -12.61836 | -45.07522 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e8a28ae-7a62-37aa-b8d4-2c41dc59c845 | -6.18574 | -44.87256 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5276e3f1-8eab-317f-a830-a3387f3c3c39 | -10.7725 | -44.76114 | 2025-10-28 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ab40b93-6c17-30c6-91be-8a18c75f8847 | -7.07304 | -44.9478 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1995ebc7-8051-3ca0-80d0-722c972a348f | -13.44814 | -44.10124 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7ec8a121-c03d-3dc6-bb82-0b260baa581a | -9.27391 | -45.5736 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e4af2879-c8a8-3fd1-aa06-51894adc4f0b | -7.81126 | -46.4874 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f455ca9b-bff0-35ff-8e3b-32df2b07757e | -10.9965 | -50.36236 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f10c8056-e3d3-34b5-be92-6b070a519c94 | -5.46824 | -47.2631 | 2025-10-28 04:14:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4b291855-4260-3b67-b7ee-175ca80ea32e | -9.54233 | -46.97193 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b49df1b4-3bd4-3c6a-ae41-89f909b72457 | -7.97811 | -46.72994 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d03c0d8b-4af3-3361-ab85-77d69b952cef | -9.95713 | -47.07598 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 991b3a4d-fc15-3faa-9021-55e230a8b745 | -12.59741 | -46.827 | 2025-10-28 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 346bf68d-8cc0-3318-88ab-1f54d8e126dd | -6.28528 | -44.71413 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b00a4490-b8d8-3fc6-8d6c-928b57e775f9 | -8.30513 | -46.81919 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 443a997f-e1a5-36af-9562-f04a17a2b7c5 | -10.99292 | -50.35734 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09524b24-e2ff-3578-bd63-f68c6761eecd | -7.25529 | -44.99618 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de3b2741-cec6-310a-9acc-b48de1e34f55 | -12.06067 | -47.81681 | 2025-10-28 04:14:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fc8268a-76fe-3c2c-b6cf-f7e02028b1a7 | -6.64801 | -43.3805 | 2025-10-28 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a7be40af-4efa-324f-a757-45b3bffb9d66 | -9.26488 | -45.56448 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95acd3a8-d980-324f-8686-3c9c30ed5aba | -10.67574 | -47.27259 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65f944a7-8417-39cf-9f18-a6cd85c892c9 | -5.48443 | -47.74659 | 2025-10-28 04:14:00 | NOAA-21 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d69827b9-ea73-3808-a55e-14ccc0245e3c | -12.08937 | -45.67915 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b74e905a-2472-3b95-a4fc-d43c7f6baea8 | -8.5686 | -44.95931 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b552401c-4d1b-347f-95a4-9fd83de9b872 | -10.91493 | -50.26155 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa7490e8-eecd-3fb0-a4c0-a7ff80382e8e | -7.26252 | -45.01626 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b145783-0092-370b-b467-e3cd7905be9a | -6.59514 | -42.65139 | 2025-10-28 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6c3b6a01-a0a2-3d43-8aac-2726b165eba6 | -8.18723 | -45.71121 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22a915b1-4ed2-3efb-9316-b49d7c4279a3 | -8.34292 | -46.88644 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45818b71-d6de-32a3-9930-08b219829d3e | -8.16823 | -47.01234 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11a3e9e0-3e1e-3aab-ae18-e35d9c10d092 | -10.55999 | -49.78807 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87b7a5de-880f-3c4a-b831-b9e8d5e8bafb | -9.96442 | -47.09902 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 81fcdd82-17c9-350a-b98f-d106d26c4b8d | -10.21908 | -49.84911 | 2025-10-28 04:14:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd1d21ff-befb-36fd-8a00-61f271a9df1a | -7.29967 | -45.06764 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a7ea59c4-7076-3763-8f4e-d06c4244cf14 | -7.4521 | -47.16197 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7b871ea-03f2-33d5-a9bb-7874b55b8441 | -7.96111 | -45.49896 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 961781b1-d828-37c6-8f08-fb6f62e98803 | -11.64327 | -48.52834 | 2025-10-28 04:14:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 131e5d84-98ef-30f2-8451-0e7cbf38e3f1 | -12.82364 | -47.72773 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| adefe5dd-1a3c-328e-a342-7d1830e6925b | -7.46863 | -47.15525 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fb517b9-ddb9-3abe-a57d-d185c57f7412 | -10.58418 | -49.79974 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 94b24556-29cd-3ecf-ad8d-44d48d3cce7e | -10.55242 | -45.05287 | 2025-10-28 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7ba4641-62fa-30d7-86fe-3232d58a1922 | -7.93994 | -45.54236 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23288d1d-3a83-3851-ab75-f56aaf473f62 | -7.16622 | -47.33645 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2d1fbd6-dde1-3895-85a7-e90e5c50e7bc | -10.5816 | -48.00537 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cf15180-68d9-39b4-8d5e-e8c45c801823 | -10.561 | -49.78337 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README36.md)
