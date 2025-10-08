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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4528c869-32f5-3473-8533-13875fd62a89 | -8.5016 | -46.2669 | 2025-10-08 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 338.5 |
| 88291e4f-15ce-3611-b7a9-229a3582276b | -8.4824 | -46.2912 | 2025-10-08 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| aaeb3b7b-a0a5-3584-8d90-003b6d96dbf2 | -7.5463 | -44.3164 | 2025-10-08 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 25db0d33-5a38-37ef-8e27-72cefe8acbf0 | -11.1646 | -54.86 | 2025-10-08 13:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 34063922-5396-31be-8e9a-39a4367128b4 | -13.3245 | -48.0101 | 2025-10-08 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| da298f35-0e66-36d8-b327-0d3118d54501 | -7.7922 | -44.2229 | 2025-10-08 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 2cc23236-4526-3310-9be1-4386c4e4b609 | -12.0118 | -45.2161 | 2025-10-08 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e2f3cddb-c9b2-3cc0-b3c9-29cc2c6022a8 | -9.1716 | -49.9408 | 2025-10-08 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| d330781f-a723-379b-9b1b-b34ae63a017f | -12.5107 | -54.7345 | 2025-10-08 13:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 58b48e31-faf0-3ed5-86f6-7ee6c1462907 | -9.1713 | -49.9622 | 2025-10-08 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 21a09b11-efea-304f-9e70-249b99541e61 | -11.2629 | -50.2409 | 2025-10-08 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 2c344747-4f3a-38a6-88f3-70ed08a056f4 | -17.9224 | -57.5128 | 2025-10-08 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 702d08d8-a95d-3b73-a43e-6af958485e7a | -13.3774 | -47.2411 | 2025-10-08 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| e1fea88e-0661-353e-bb2a-ba15280cbb99 | -11.6851 | -46.382 | 2025-10-08 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| b6ae5e34-e741-36d7-b439-2bb561d49ea6 | -8.6106 | -45.102 | 2025-10-08 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 3dd745c3-bd81-3369-a030-3007e1744149 | -8.9399 | -47.3576 | 2025-10-08 14:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 42ac9577-685e-3f2e-917c-53cc45f5d96f | -14.8832 | -51.4561 | 2025-10-08 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| d1c744d4-6e20-3a0b-bdae-1b0436404cba | -14.7179 | -46.0867 | 2025-10-08 14:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 277.1 |
| 87da90bd-e2b1-3bce-9dab-21b93a0a956d | -13.3706 | -47.6013 | 2025-10-08 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| afed1a11-4883-3c23-b713-3ad926a8b850 | -12.3908 | -51.1366 | 2025-10-08 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 5006d288-1672-33d2-a502-69a6e77c039c | -13.3774 | -47.2411 | 2025-10-08 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| aa41c4f4-5c46-3078-8e17-9d3b9916f90e | -12.4916 | -54.7364 | 2025-10-08 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e3a480d5-1728-3ef6-95ab-8697102fb2c5 | -9.1713 | -49.9622 | 2025-10-08 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| db4721d3-7e70-37b9-9b88-f06e716f5290 | -12.0118 | -45.2161 | 2025-10-08 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f79b27fc-dfc4-3d6d-883b-2ca2033bfeed | -13.3245 | -48.0101 | 2025-10-08 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 712a0a0d-a9fa-3153-8afd-e0e68918b0da | -12.2688 | -49.1907 | 2025-10-08 14:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 29198179-e968-3c1c-9bf4-aade5d62536c | -12.5109 | -54.714 | 2025-10-08 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 4a8e2f0d-1748-32b0-92fb-f0ff89b8bda9 | -7.7919 | -44.246 | 2025-10-08 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 400b7c72-514e-38e7-b90f-f8665e208dbc | -13.3438 | -48.0072 | 2025-10-08 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| ddb8a73c-1234-34ae-9cd8-cae233df4c55 | -11.9519 | -46.4352 | 2025-10-08 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| f4954d45-99ad-3f4c-8915-a504ac730d0e | -17.304 | -58.0566 | 2025-10-08 14:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 52804e28-1e80-34f4-9d06-9ff9af383364 | -9.2099 | -46.8861 | 2025-10-08 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| d0e1b23a-1e4e-36ab-b6b5-30b63e0bb07a | -12.2525 | -47.8728 | 2025-10-08 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 73e75fc9-b1db-349b-985f-9b3769f0d9c4 | -7.4666 | -43.0909 | 2025-10-08 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 53729f3c-ec09-3696-8e74-251ca3aafa08 | -7.7736 | -44.2017 | 2025-10-08 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| da608fc8-7b19-3e4c-a8fb-80a9443bc319 | -9.1975 | -47.8381 | 2025-10-08 14:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 25b46b6c-93a6-369d-b667-7dd6f288c93e | -11.0451 | -50.9047 | 2025-10-08 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| abcdd1a5-ffcb-392f-b581-31489c4b5445 | -13.3778 | -47.2185 | 2025-10-08 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 888e99c0-574c-3d52-985a-34d6416875fb | -8.6295 | -45.1 | 2025-10-08 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 450.7 |
| a53e8af8-4370-3eb7-b554-fdf8be1f2fbc | -8.6106 | -45.102 | 2025-10-08 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 5f7480a1-8c3a-3151-bbc7-c968cf6c48d3 | -11.0454 | -50.8834 | 2025-10-08 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| ca33803a-569a-3c7c-9f90-11541ccb9ef7 | -14.3889 | -46.0063 | 2025-10-08 14:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| ea96e694-ece9-366d-8728-f5c6d7bb6092 | -12.4919 | -54.7158 | 2025-10-08 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6953f70b-ccac-3361-9ec0-d33cdbdb7c37 | -7.8005 | -46.7355 | 2025-10-08 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 4d3010f3-b477-3a7f-a0c6-ffd2d859774d | -7.7414 | -46.9848 | 2025-10-08 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| ad85975a-7662-3164-acdb-2cabe75f855d | -15.3979 | -48.0164 | 2025-10-08 14:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 1647d52b-f1a4-3116-a67c-76f48ecfcec3 | -9.6795 | -49.9355 | 2025-10-08 14:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 77c6f3a7-0d0e-3b99-aa94-b4c512ddd9de | -13.3018 | -47.1626 | 2025-10-08 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 194.8 |
| e2721b17-8899-34ca-abf7-967495a7c24f | -12.5107 | -54.7345 | 2025-10-08 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 3765d598-b6b2-3b7f-b71e-b68599cebd89 | -9.2096 | -46.9084 | 2025-10-08 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 3d84ace0-51e0-346c-abdd-e583f1278a77 | -8.9309 | -46.5809 | 2025-10-08 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 5fe9e462-c51f-3009-9dd4-82f36f3ed214 | -8.5207 | -46.2425 | 2025-10-08 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 259.6 |
| 6ef2ae8b-29dc-389a-b33a-400cd3ca58ea | -8.9121 | -46.5829 | 2025-10-08 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 47f5c6a1-8043-36b0-a840-45f6c306f41f | -12.3655 | -50.3049 | 2025-10-08 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 3feb89a1-1d9c-3bad-868a-ed123275dcdf | -12.5297 | -54.7326 | 2025-10-08 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| cf0f11b8-5159-3917-bc3b-f060d2e9230f | -14.9018 | -51.4965 | 2025-10-08 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| b8e6bc33-2aff-32a7-8c08-e8590378c401 | -11.785 | -45.0421 | 2025-10-08 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 6c11ffc0-a441-3dd7-a96e-bb5f3bf0dad7 | -7.2966 | -44.7761 | 2025-10-08 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| cb851f8f-5d88-3eca-8536-cbebd4f314a8 | -14.8828 | -51.4777 | 2025-10-08 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 1178e887-fb53-3800-978f-bf27123905d1 | -7.7922 | -44.2229 | 2025-10-08 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 0cdf65d0-f940-303d-afbf-5a32a8e2ac98 | -13.2855 | -48.0381 | 2025-10-08 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| b126b279-fb8e-3035-bf96-52d2df7ba658 | -13.3211 | -47.1596 | 2025-10-08 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ad4f5239-94cc-3981-ad0b-6a92ff5b2bfc | -7.4855 | -43.089 | 2025-10-08 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| eb4cc7d3-fae4-36a7-b7cb-fbda8a7b03fe | -9.1716 | -49.9408 | 2025-10-08 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6b759bf9-4b9f-3efd-afa1-70a524ca535f | -8.9306 | -46.6033 | 2025-10-08 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 841fe281-ba43-3fd5-86f6-ce03ee15cbf0 | -8.1618 | -43.323 | 2025-10-08 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| b2cd3dbd-2c19-327d-864e-65435c155012 | -13.7364 | -45.68 | 2025-10-08 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 371.6 |
| 0e516406-de7d-3ef4-9fa0-05ee4e998289 | -11.7846 | -45.0652 | 2025-10-08 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 28894ba3-063d-3d77-8f38-2da23d0f4776 | -7.4672 | -43.0438 | 2025-10-08 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 2bf54f15-8cc2-3397-bc71-76c1c3c93a13 | -11.8827 | -44.9351 | 2025-10-08 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| d807ccc4-fc42-33ab-bc97-240dc85ab3d2 | -17.9224 | -57.5128 | 2025-10-08 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.2 |
| be1b6a4e-7a47-3a9e-98f6-4e6080eb3263 | -7.7743 | -42.6103 | 2025-10-08 14:00:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| a4b10fe1-2aff-383f-9ab6-82a6545a214c | -7.7203 | -42.4023 | 2025-10-08 14:00:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 77b35db4-65d1-3141-b46c-ab0ac1da7567 | -11.9331 | -46.4153 | 2025-10-08 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 1293e321-bb4b-3c3b-bd95-58e5b3600bc8 | -9.6793 | -49.9569 | 2025-10-08 14:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 524b2618-348c-3225-901c-f3445ccc2593 | -9.5508 | -48.2182 | 2025-10-08 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 0b1c3cd8-209b-3f32-97af-71de61ebe675 | -7.793 | -44.1535 | 2025-10-08 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| f01bf28c-1a20-359c-a41b-14331c245a7c | -7.2471 | -44.1604 | 2025-10-08 14:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 466f759f-04f6-3d5a-92c3-14ff49ab99fa | -13.3048 | -48.0352 | 2025-10-08 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ae9f9931-c721-3f8b-98a0-6cffcdfc6548 | -8.5398 | -46.2181 | 2025-10-08 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 467c59ab-0428-37f3-824b-5a350b3b9ee4 | -15.321 | -46.1622 | 2025-10-08 14:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 88.1 |
| c7ba65a9-c99a-3fe6-8d60-c6abb923161c | -8.1804 | -43.3445 | 2025-10-08 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 278.9 |
| cf966f80-4e24-3a18-93dd-306cdd0954d7 | -12.3911 | -51.1153 | 2025-10-08 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 068f510a-3de2-3115-96cc-dc50cc34d92a | -11.7576 | -51.4847 | 2025-10-08 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| be679e36-c9a2-3575-a39c-ef6cc3f3ee6f | -12.1372 | -50.2682 | 2025-10-08 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 302aa7a4-634b-37f3-a1f3-eeaf28cd1683 | -8.5393 | -46.2631 | 2025-10-08 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 35c311ff-30e1-37c1-99c6-7c3066535821 | -9.1899 | -49.9818 | 2025-10-08 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| db695019-c2a8-3bd6-aeb6-355798cf6677 | -11.9523 | -46.4126 | 2025-10-08 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 6614c34d-f470-3350-8294-f1a6385e322e | -12.9816 | -46.7824 | 2025-10-08 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8aa69eee-a40f-3a7f-bffd-cf0d8475cf60 | -11.7656 | -50.932 | 2025-10-08 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0506ad1e-6441-3664-8624-d473389d1d85 | -14.7379 | -46.0601 | 2025-10-08 14:00:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 65c818c1-1171-3871-b471-066860b701f1 | -7.7924 | -44.1998 | 2025-10-08 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 7e31f567-41c7-3d15-befe-9fb222aa1ac6 | -12.0314 | -45.1901 | 2025-10-08 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| c36931f9-34bc-3b2b-b34b-b42e25b8b5c6 | -18.0394 | -44.9438 | 2025-10-08 14:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ce8a39c5-b6ee-3bad-8c9a-fd9d07f24a33 | -11.8042 | -45.0393 | 2025-10-08 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 3c0fc8b2-6d4e-3a9a-8394-cc8bbd4688fa | -11.1364 | -51.1496 | 2025-10-08 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| ab7728bd-0bd6-38bd-aaa8-1628ab6688b1 | -17.2837 | -58.0997 | 2025-10-08 14:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| aef4a9a1-a696-38c4-9109-cbefbe093c92 | -12.2333 | -47.8754 | 2025-10-08 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| c6421925-e9bf-337b-a98b-524562f7bd21 | -13.7354 | -45.7263 | 2025-10-08 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| a8eca8e2-7fce-376f-96f6-b73ee77fbdde | -12.0122 | -45.1929 | 2025-10-08 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |


[Clique aqui para ver as próximas entradas](README108.md)
