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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8754f165-2402-3875-81f2-809650098699 | -4.3571 | -45.277699 | 2024-11-24 00:25:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fd0dd85b-cd3f-3a39-981a-62d1f77b011d | -4.1101 | -49.500999 | 2024-11-24 00:25:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dad4debc-6a55-34e0-b8ef-4d08add3b0fa | -3.7625 | -44.041302 | 2024-11-24 00:25:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea117243-33d1-3498-94d5-84472833af4d | -4.1983 | -45.349098 | 2024-11-24 00:25:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 302f9308-841f-3bcf-b42c-8b33ca6b52f4 | -2.6002 | -45.658199 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6659d01-a1c7-36a3-84d0-005dc12c2bb0 | -4.4787 | -46.077 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dcd1f79f-37d2-3d17-a1f8-b22926c2494f | -4.372 | -48.5578 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c1d15e7-351f-3d22-9ccf-1dec91dfebff | -0.8097 | -51.589298 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45a5bbfb-a197-38ba-ad47-6e1b8c4a4dcc | -3.866 | -47.0508 | 2024-11-24 00:25:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8616414-f8ee-3862-9174-0ff78ca54448 | -1.4625 | -51.103699 | 2024-11-24 00:25:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 402bd6bc-b4d8-3233-beea-ba880ddb3681 | -2.2635 | -50.451801 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 412fcaa0-19fa-30e7-a4e2-f3087280ffec | -3.4938 | -49.922001 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59560227-2cf9-3179-b9b9-68560a6b06aa | -1.2171 | -53.676201 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfeb615d-68f1-3d0e-b3f6-d9093f852f21 | -3.9458 | -50.193401 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba0ee5c8-574f-3e90-b60c-531d1685b9cb | -3.9556 | -50.191299 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14907a34-b40f-33f4-be66-62ac2920f49b | -2.914 | -45.363899 | 2024-11-24 00:25:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d38ae10c-050c-308b-9b99-829dcb350e70 | -4.2577 | -48.690701 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e19a6337-88d5-3190-a299-9cba0bfbe5e2 | -1.2907 | -51.7141 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f4897c7-5e64-312e-9afc-f9b470bbedb0 | -2.2651 | -50.4589 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50e769ea-0127-3e3c-9726-caf6237d0dfc | -3.704 | -47.608601 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 271877d8-df79-3f8d-8a96-43d74cc73e04 | -1.0467 | -51.727699 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| da474972-d94a-3751-a515-84b9e12dd687 | -1.2059 | -51.748901 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffa7b0a4-4894-310a-9c6c-1104f9e2329e | -1.448 | -53.3773 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b68665eb-0369-347f-82e2-a3c47d839981 | -2.4941 | -46.0956 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 000f5450-0ce1-381a-ae7a-5541666e3dcb | -4.2374 | -44.625 | 2024-11-24 00:25:00 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bfe0328e-4acc-3d9a-a480-e55d5bd0351b | -4.368 | -48.494202 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1bb6bd3-b881-3e16-aea6-be4b77093db8 | -3.5377 | -50.762901 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f25a601-a1e5-3d67-b306-33d900cd360e | -4.4088 | -49.6395 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 103b544c-4ee3-31fa-bce2-0eb793ba47c4 | -4.4869 | -47.106899 | 2024-11-24 00:25:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2b91c32-5ece-3769-88dd-42d1ac5f08f7 | -2.5877 | -46.551498 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76151f13-8ee3-3c9d-aa5c-c1a7ca3e6744 | -2.7023 | -46.2407 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3b74b1e9-4464-3711-a81a-b3c0d7064626 | -1.2123 | -51.7314 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30bbff71-ee2e-31ce-98ca-ebfd465c69c8 | -1.5968 | -52.573399 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e7384cf-e834-38f4-8eb5-ce96f8374db1 | -3.3963 | -50.314301 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 170172cf-980c-3d0f-832d-6539470a7b44 | -4.3736 | -48.564701 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7b08d1a-a2c4-3639-8df0-a67ce55bd833 | -0.9499 | -51.709099 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5ead5dc2-5f5e-3d64-b2f9-80d3c01a4c50 | -2.9159 | -45.372501 | 2024-11-24 00:25:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88ebcf37-0964-354e-acef-f70748a30e4f | -1.2601 | -51.761101 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b3ae1c7-902f-39cd-829e-f89716b17c1c | -2.822 | -54.014301 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae96612c-2f76-39e5-b3d3-fcb7653bacac | -2.7113 | -46.2799 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d4535c6f-c70a-3902-859a-8e3add2acd06 | -2.177 | -48.923401 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f955041-e75a-3299-a495-7410b9c951c3 | -3.4954 | -49.929001 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d35bc260-8ee6-3a66-a253-5a19cfe0ace4 | -2.7041 | -46.2486 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 557e03e9-2305-3edf-918f-dde9ac0a23d8 | -0.3755 | -51.536499 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0ba7f274-1f04-3a54-baee-12f96579dd38 | -5.1173 | -46.1647 | 2024-11-24 00:25:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9d0e32e-a8f2-354d-a131-a816fabd48cb | -4.2365 | -48.688202 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 277d0721-58e3-3c8b-b592-4f1e34f91dac | -2.9267 | -46.682499 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28a8e04b-8a9f-3df3-b12b-ed79d5e5e051 | -1.255 | -51.737999 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ee067e0-5c93-3fd6-83c7-f7743f796a0a | -4.6389 | -48.8283 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e283dee-fbaa-3b67-a038-d9de1ef46ccf | -3.0522 | -52.739201 | 2024-11-24 00:25:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 421a86b7-897a-34c3-927d-75b92d276eb5 | -1.2438 | -53.383202 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b510d536-54cb-30c4-a46a-2e05085ef361 | -3.9505 | -45.9757 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 02615a92-35cc-3d33-9913-44cbe60253c2 | -2.4252 | -49.018501 | 2024-11-24 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 756adadf-a1c7-397a-93cb-0e1274735c8d | -2.2608 | -51.082199 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b27fad31-647b-3043-a66c-76446373da86 | -2.5548 | -46.542801 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2953a15-5ed2-3663-ae67-673a8be7a642 | -2.5983 | -45.649799 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab75e1a6-b1c7-351b-84a0-47a9a493e7e8 | -1.489 | -54.064301 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33de42a0-9589-3d00-aa4c-e2f324b2ea4a | -2.6516 | -46.2439 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8930d0-e652-3253-b00e-34d9fc00d99f | -5.0631 | -42.5592 | 2024-11-24 00:25:00 | METOP-B | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8f980ed2-2ec5-3aaa-8c94-f03e3a8212ba | -2.6449 | -46.848 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25a19a0e-1f58-3ba7-9ade-bd0146b18687 | -2.9591 | -45.7864 | 2024-11-24 00:25:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 39dc6723-130f-3807-9798-52470dcb6091 | -2.1548 | -50.6101 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 343caa9b-b688-3a33-a032-355e3b494820 | -5.1473 | -44.5494 | 2024-11-24 00:25:00 | METOP-B | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 008064b2-76bb-3167-a942-855a661a9c12 | -3.5731 | -41.9506 | 2024-11-24 00:25:00 | METOP-B | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5c79ba33-6224-316e-a7c4-d00c1c21dee5 | -3.7024 | -47.601601 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7064dbe-4777-3285-95ad-1dd60c965115 | -1.6377 | -53.306499 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de21e38e-9dec-38d7-a94e-08e3d010bbde | -1.4243 | -53.362999 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45bce8c2-1825-34b7-93f4-3171b38f3ff8 | -2.623 | -46.208801 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd596799-614f-39d7-95dc-a38116e4e86e | -1.3057 | -51.734901 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a09696ad-bb6b-38a8-b378-76ae45f40500 | -4.0814 | -46.819698 | 2024-11-24 00:25:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e12a3b7a-1a93-3166-b317-8f95ea75887c | -3.9888 | -47.727901 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b9c3695-3755-3032-9bfd-c51495552165 | -1.12 | -53.381302 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5401c13-60d1-3b3d-9550-b5d663bde823 | -4.9958 | -42.929199 | 2024-11-24 00:25:00 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9bdd02fc-8a39-39e1-8cb8-b4b2f6d05c18 | -0.2837 | -51.494598 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a4e4f3ee-b487-3689-b8f6-811366da66f8 | -4.6291 | -48.830399 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7da14b64-c308-3b61-9afb-c5ec50c3d031 | -2.709 | -46.089401 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9d55bbc-ef33-3217-915a-2b7457dd6003 | -2.6727 | -46.156101 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82f3da8e-7a89-30ed-869a-63737865b005 | -1.6156 | -54.4007 | 2024-11-24 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 673364c1-6bdd-3da1-af92-e996e50421fb | -2.6934 | -46.201302 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e8833fae-dce3-3eac-bd53-39b15611ab0e | -5.0604 | -43.689098 | 2024-11-24 00:25:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9a6a928-04aa-3282-b3d1-8a61cffd0a88 | -1.2261 | -51.7929 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e43243f-3960-36bb-9938-2dc77807cddb | -0.0464 | -50.807899 | 2024-11-24 00:25:00 | METOP-B | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 757796e4-b629-38d1-8921-68df4de25c4a | -2.5729 | -45.628899 | 2024-11-24 00:25:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ecfede4-9dc2-3a32-9649-f62e8aa32a19 | -4.2356 | -48.638302 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5e644a1-a83b-3684-90f4-8cde0f0bd594 | -5.1017 | -43.161201 | 2024-11-24 00:25:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28291a1f-338c-3635-abee-3fd526a4833a | -2.4512 | -53.6842 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b409fbc3-3557-3144-a14e-8fb2b0d36842 | -3.266 | -53.796501 | 2024-11-24 00:25:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dab74ece-113b-3673-b7f0-a8ebf1b65ce8 | -4.0478 | -45.277199 | 2024-11-24 00:25:00 | METOP-B | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fadfcfe9-e0a5-376c-8af4-8d99e105c718 | -2.6899 | -46.276501 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 385b8805-d164-368d-950b-21d156481f12 | -0.9597 | -51.706902 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3a238b89-8bb5-3cb7-bfd8-34053fb7717d | -2.1993 | -50.533001 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cec06173-b972-34ae-a9e6-b508aa97fbda | -4.218 | -50.3983 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bfe6864-3930-3ff3-ad09-3d46ae3dd0b3 | -1.4522 | -53.396 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88eae3cd-ce90-3157-a2b9-091fc4fcb163 | -6.6851 | -48.858799 | 2024-11-24 00:25:00 | METOP-B | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e590a089-7220-319b-b326-0c7126639a45 | -2.6605 | -46.5994 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01d9fd73-6d9c-344d-8ced-ffb589ba6a77 | -5.5535 | -45.325401 | 2024-11-24 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f60484d-c576-3b78-974b-1c22b685aa34 | -4.1142 | -49.427502 | 2024-11-24 00:25:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7221d000-4227-3138-9a9c-0120dac5b53e | -1.6987 | -48.7216 | 2024-11-24 00:25:00 | METOP-B | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b2e24b7-7947-3500-9b5d-c1aaee4a4fa5 | -3.5969 | -47.499802 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e291a602-4127-3c82-b45e-369b9317c798 | -4.4143 | -44.099098 | 2024-11-24 00:25:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
