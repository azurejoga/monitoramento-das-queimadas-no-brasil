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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ad0d696-14a0-3778-948c-4d4d8a9b095e | -3.70931 | -47.64971 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb6f8366-904b-300c-b062-5b9b15a36891 | -7.36726 | -42.45052 | 2025-10-28 04:42:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e6d55e0a-30a2-38a0-a9b2-86b747ca8232 | -1.41382 | -52.671 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc8a7f65-8b52-3660-ba21-21aec9736e0b | -7.31632 | -47.20787 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c3f4760-aa01-33fd-b372-12b5a03462dd | -6.70373 | -42.04844 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 09557074-2dfb-36ff-874a-b57194a928a7 | -7.81596 | -45.3846 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4fadd93-0961-3101-929c-49bd4236e229 | -7.00564 | -47.00308 | 2025-10-28 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01309297-4270-308f-ab73-599ae0ba5184 | -7.8927 | -45.70768 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cc42c98-b7a8-3c9b-a8bc-0d290a6c7644 | -7.80714 | -46.46444 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 208252d9-ed5a-3140-821e-a98601807ab1 | -4.96879 | -56.2748 | 2025-10-28 04:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 729a1616-74a7-3a5c-9914-9304d36d1541 | -3.23377 | -50.65132 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e26bc397-c504-3a8d-9a90-ef174843dc8d | -6.4207 | -42.33211 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f17159cc-d9ca-3ce9-ae23-8bdd51b0866f | -5.65929 | -47.83405 | 2025-10-28 04:42:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 235f2350-1459-380c-bd1f-9bc1701571c9 | -3.02246 | -45.36955 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1c800305-ec68-3473-b5aa-94688c5baae1 | -5.60707 | -47.10551 | 2025-10-28 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bd0205f-23fc-3a3c-8d0d-0f837f304fae | -7.97827 | -46.73707 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d168171a-5bb0-3ed4-8bf6-aed1447e73cf | -4.43191 | -43.44614 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4d31f41-13a6-3637-91f9-e9c5855fc8b1 | -7.95204 | -45.54498 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ffac865-ca36-3d28-ae75-3ebcbd20f12a | -7.98204 | -46.71204 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05363f16-2c4a-3fa3-b359-110c529af86e | -5.80921 | -40.81336 | 2025-10-28 04:42:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ca68ca52-c11e-38d0-a313-613ed73eb96e | -7.44656 | -45.12869 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f057e569-e247-3e75-9cd7-6420cb8526a7 | -7.15984 | -47.00506 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b2b05e5-5a6f-32a8-bf3b-e72906237c21 | -3.28926 | -50.1967 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8ddebed-5975-36f8-b6f3-50ef7cef5409 | -3.71042 | -47.6426 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a027947-5ecd-35c4-9c8d-4d42e8e819ef | -4.15993 | -46.79031 | 2025-10-28 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca4c34d6-15cd-37ea-a7b2-a49857d0168a | -7.80777 | -46.46021 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4950ce64-fb66-39e4-9cf4-97d7d974a668 | -2.74734 | -45.41318 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 39f5d7e3-0c53-3bbf-9043-11358ec41ef2 | -3.24799 | -50.03615 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcf46b13-f3f7-3ebb-9f7d-55b7573c8bfb | -4.55922 | -44.45137 | 2025-10-28 04:42:00 | NPP-375D | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2531100f-52c9-3d28-87a7-62d46b206cd6 | -4.88634 | -45.74467 | 2025-10-28 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 354f4b5a-3e28-31e7-bbc9-bcea22ec6e67 | -3.9829 | -48.98912 | 2025-10-28 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19e2db0d-2e2c-3b7e-b65a-f047fcc4ea18 | -6.24018 | -44.65701 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80450e96-741e-315e-8d87-d75a896cf12a | -4.30816 | -48.0609 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94ec89a4-24f0-30ba-8dbd-f63ccff0715a | -6.685 | -42.04436 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 55b67f9f-3cd6-3697-aadf-d81ef4b51e0d | -6.80715 | -49.35631 | 2025-10-28 04:42:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edf6df40-2bbd-336b-84af-5800175309f0 | -5.531 | -41.71407 | 2025-10-28 04:42:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ee82632a-ce01-3dcf-9f76-7a6428bde578 | -7.43233 | -47.20435 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a90be63-5678-3755-89fb-1246d095c009 | -3.33976 | -53.03528 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c8c76ce-7264-3604-a004-60f44ba03c11 | -6.68576 | -42.03918 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6cf94a49-d6aa-34a2-94f7-a2b1b68855d1 | -3.25442 | -52.91645 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8adad98d-3d35-3086-9dfa-3d5b8c60b5cf | -4.46014 | -43.23477 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 40bb767e-1ee8-3689-9bfb-4de581959631 | -8.03565 | -45.14365 | 2025-10-28 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7dd6ba55-8606-38dc-94a4-85e3369f42fc | -7.86785 | -46.40141 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 985eba59-84d8-3d72-8d85-74c2d49c4404 | -5.70413 | -43.53563 | 2025-10-28 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c01d17a-7b21-35fc-98bd-36982e4278be | -3.38348 | -50.14907 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07de392e-2037-3028-9e44-98305b0671f6 | -5.31601 | -48.36089 | 2025-10-28 04:42:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f9aa265-e4d4-3998-9915-94846559a753 | -6.69006 | -42.04118 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 23f991bc-e57b-3d4e-ae9a-60b122df5130 | -7.61175 | -46.47673 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1f15b616-d4f5-3857-9ffb-2497a4f47236 | -4.42731 | -45.8966 | 2025-10-28 04:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebc23d40-7b2e-39a2-83a7-7f7da0e797c3 | -7.60279 | -43.58318 | 2025-10-28 04:42:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 85987936-f3ad-3c5a-82d2-5d84ba9b98ea | -2.79576 | -54.8632 | 2025-10-28 04:42:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 909da10e-7c70-3e49-a59c-ceab72f4aa18 | -6.1119 | -41.72842 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ffe6b0c9-f4b8-35f2-958f-256aa2dc346a | -7.31135 | -44.10691 | 2025-10-28 04:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9d808cf-836a-3b42-88d5-01aca1aa89bb | -3.71278 | -51.82261 | 2025-10-28 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1569a58d-5822-39bc-8383-cd8e79671b34 | -7.92232 | -45.69239 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7e93c348-a3b6-3157-9c7f-2850eee46d5a | -6.49315 | -42.22767 | 2025-10-28 04:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c9f74ea5-b502-3f47-a6e3-bca7c39c0edc | -3.11492 | -51.21134 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c12a53ad-d45f-34b9-b0af-e266afabb26a | -7.44941 | -47.16269 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b297235-6f42-35e7-8db5-25098a435145 | -5.78856 | -47.71944 | 2025-10-28 04:42:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d332ce0-a49c-3f30-84a1-8549ecee0bf8 | -6.57481 | -48.76921 | 2025-10-28 04:42:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1569d9f1-3072-3cc9-b715-7da78dc2463a | -5.58829 | -47.17249 | 2025-10-28 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 322d17e7-2ee4-39a9-81af-f520d3bbfcbf | -3.2378 | -45.94932 | 2025-10-28 04:42:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf23c947-fb31-3aff-841e-a30c0ee10f93 | -6.16621 | -46.09333 | 2025-10-28 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c21fb73-871d-3987-95ad-7521b3eec7fa | -6.2823 | -44.71728 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e76190ad-dcf8-3e89-9468-934079ed08f0 | -3.39907 | -50.27258 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f47ce1a9-0d9a-3a01-afa9-0f2e1a99e9f5 | -7.07239 | -44.93728 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d93e2980-930c-3a6c-9097-eedd09632634 | -7.29215 | -45.0707 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3cf2116c-b9f5-3944-8343-49f8966dab04 | -3.53221 | -51.57705 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5d0eea2-9d4d-3d45-a397-9912bfd64a06 | -4.97524 | -47.81423 | 2025-10-28 04:42:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc96df14-1ef3-3751-92c1-a2de9e987384 | -7.9507 | -45.50053 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 150d97ca-0986-3f43-acb2-d852ff50c77e | -7.26411 | -45.01489 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c8df0276-fd24-3fe5-a3fb-eedccbc69d36 | -7.40989 | -46.99536 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30098d7d-79ce-33ff-b862-dd96416df8da | -2.30552 | -48.14517 | 2025-10-28 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f98fbdc-c3c4-3095-abb3-1910e911dbfa | -6.23926 | -42.56562 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| efd9bd7c-c967-33d6-9423-84952b6abe0f | -4.3611 | -50.52667 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 873319d5-c17b-3c8c-9c30-dae8941d5885 | -5.6065 | -47.10925 | 2025-10-28 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42856585-f214-31fe-b984-7b21548cec94 | -6.12466 | -41.70856 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 39589ca6-c07f-3a44-a777-de785087288a | -2.19836 | -56.98225 | 2025-10-28 04:42:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1cd1749-8a65-3f80-be7e-a250d1c0b7e2 | -3.70876 | -47.65325 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a62ea5f-1c1b-3fa3-a4f2-296974a455d1 | -7.96298 | -47.24088 | 2025-10-28 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e328430b-0987-39c9-9339-43aad7265985 | -6.42804 | -42.33145 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 21866a70-cf64-3fa3-9122-0ced9b453f30 | -7.26486 | -45.00983 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 480f1022-782c-3c55-ae9a-5a4a10472c7c | -3.57607 | -43.61168 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3217c29-7f95-3629-a061-4d7dc5800123 | -2.80758 | -49.14368 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd290c25-c6f3-35da-9923-fbd847991056 | -5.15422 | -45.24952 | 2025-10-28 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25ac5e27-b12c-3d3c-8031-40e111cd7800 | -5.0132 | -41.03976 | 2025-10-28 04:42:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a5c4bb27-2050-3cc1-94f5-9228c9eee2c9 | -5.03105 | -43.61317 | 2025-10-28 04:42:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bffbe9be-741a-35b9-98a1-1447ce77d157 | -4.19949 | -48.3666 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8272104d-7cfa-3701-85ae-e56094243bba | -2.75683 | -47.752 | 2025-10-28 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b857b19c-8e1d-3518-8ef3-efce90523cfe | -3.17934 | -52.49376 | 2025-10-28 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dab2fe7f-2222-36d4-b2d6-3ddad5053296 | -7.12384 | -47.02793 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bb7db29-5513-3184-9c24-52734f950032 | -7.9734 | -46.74488 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 30403daf-7c06-3d80-8d9e-da3939a4b49a | -3.46895 | -49.96496 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eca67e0e-6ceb-325d-a7bd-89c166c70909 | -8.1867 | -44.44569 | 2025-10-28 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 963ad7d8-f745-345d-be64-b5a5fe2da28e | -3.91669 | -43.32419 | 2025-10-28 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c513c49-73fc-3ee1-aec0-135c1ccf94a6 | -3.4432 | -41.85022 | 2025-10-28 04:42:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 43bd5f64-ca89-3dd5-9137-bc183aa0f35d | -7.97901 | -46.28844 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c962c29-1302-32aa-88e6-c8669d5f9cc9 | -3.57365 | -49.43518 | 2025-10-28 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c94495e1-f07a-330f-8ebd-d108f4c36c21 | -4.64969 | -48.64353 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98624cbf-91b3-396d-96fa-d851ab917bb8 | -5.03525 | -43.61382 | 2025-10-28 04:42:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README52.md)
