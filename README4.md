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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b4e3c06-06a1-3d1c-9023-fe0f0e905b9a | -8.3211 | -44.1447 | 2026-09-25 00:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ea88bfd0-5b4f-3423-808f-8ae7642e3bf0 | -9.6298 | -43.9453 | 2026-09-25 00:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| bf5e2072-8c48-362f-a858-180cdfcd65a8 | -1.1462 | -54.0796 | 2026-09-25 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f51f9996-4cea-3df2-aecd-e29d875ab486 | -14.7149 | -46.2253 | 2026-09-25 00:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 9827d32e-0c9c-3697-aacf-28bbc022003e | -5.0697 | -56.0756 | 2026-09-25 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 23021f7f-dc5e-39fc-9193-9d52c0848d10 | -1.1461 | -54.0996 | 2026-09-25 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| a9d99850-d061-353f-98b5-0c3657424f74 | -5.7754 | -45.1053 | 2026-09-25 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 66e575de-cb2b-3e47-91e2-eda02e10345d | -8.9663 | -72.8525 | 2026-09-25 00:20:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6d932e31-feac-315c-8ee0-2a86e6fff5c8 | -9.0157 | -60.533 | 2026-09-25 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7e097491-28e5-3ddf-9395-2f892af0ff34 | -3.2314 | -46.9376 | 2026-09-25 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 258.1 |
| a888fa58-4278-3f5a-b52b-0351170db63e | -11.6757 | -50.5796 | 2026-09-25 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 80f12cf0-c60e-3057-85a4-f3c60548febb | -5.0698 | -56.0559 | 2026-09-25 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 8c1335cb-cae5-34e2-9bc7-db4bccdc0f7a | -9.0343 | -60.5321 | 2026-09-25 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 43254227-55ab-3b5f-b369-2beac3d356c3 | -4.5046 | -54.9446 | 2026-09-25 00:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| bdca23b1-91f8-300d-b987-0a6cd67e5d4c | -3.25 | -46.9369 | 2026-09-25 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 936b6106-acb4-320d-8a5f-cae7b9b1a351 | -8.34 | -44.1427 | 2026-09-25 00:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c80cda03-b775-3e1e-8f62-6542073f11be | -14.7344 | -46.2219 | 2026-09-25 00:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 22e29ae6-1112-354f-900c-2165afba35ba | -11.6564 | -50.6031 | 2026-09-25 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| fb5b6ce9-f00d-3db2-b3cb-dbdbfb1808fe | -3.2501 | -46.9149 | 2026-09-25 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| f8e3f050-957a-3369-b1b8-1dba7ceaa0ca | -7.6161 | -46.4404 | 2026-09-25 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 7c68a864-739f-3813-a677-86a6b627ebac | -9.1626 | -60.7948 | 2026-09-25 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 47cf9ce2-ca22-3687-8704-b2f988336a80 | -7.6158 | -46.4628 | 2026-09-25 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 8c152ee2-73d4-3789-9406-555a6455310e | -11.6754 | -50.601 | 2026-09-25 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 525d1557-2751-37ff-9a2b-396819f71aba | -5.786 | -43.9147 | 2026-09-25 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 162.7 |
| b53bceb8-7498-3654-a97d-a6aeda4f45fc | -10.5537 | -57.4369 | 2026-09-25 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 6c836a5c-283e-3329-bb8c-a583015770d1 | -9.6295 | -43.9686 | 2026-09-25 00:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 3b4c3711-a36e-3367-880c-cf9a2bfde800 | -5.8808 | -43.7918 | 2026-09-25 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 315cd526-d192-3e2e-be0d-dd4b8897a419 | -9.1627 | -60.7756 | 2026-09-25 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4b8c6922-86d8-3838-833e-6a82408cc6b2 | -1.2189 | -54.5592 | 2026-09-25 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a7f49845-71d4-375b-8bf4-aed7755c5928 | -5.8047 | -43.9132 | 2026-09-25 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 21e309f2-963e-3bd5-be05-19fde3458b49 | -3.2315 | -46.9156 | 2026-09-25 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 146.4 |
| a1e34aa3-a8b6-31cb-9cdd-1c45b2ace700 | -3.2315 | -46.9156 | 2026-09-25 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| facd6c05-a95f-360f-a454-b1535bdddeae | -3.2314 | -46.9376 | 2026-09-25 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 181.9 |
| f0de638b-9e64-3550-bc48-065a72bae7c2 | -11.9586 | -50.7393 | 2026-09-25 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| bb92dec2-00c8-3722-b811-4727088d4964 | -5.786 | -43.9147 | 2026-09-25 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 07fbb677-3c8f-3a0e-9ef6-fde662ee999f | -11.6199 | -50.5004 | 2026-09-25 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| fa457b61-91d8-35d5-b71e-846c8c6ebbf2 | -7.4037 | -64.3843 | 2026-09-25 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 95a6bfd0-8e2f-37c8-97bc-48f77d1446be | -7.4222 | -64.3651 | 2026-09-25 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 61345953-7598-3000-b95f-7e0586ab3166 | -9.1626 | -60.7948 | 2026-09-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 5cede16b-ad84-34ed-a5c0-7ad15ab0a7f1 | -8.34 | -44.1427 | 2026-09-25 00:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 987fc355-65b9-3b93-9171-9125f762cbda | -4.5046 | -54.9446 | 2026-09-25 00:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| b20bd103-1f4e-38f0-8d13-bf218921ca3b | -1.1461 | -54.0996 | 2026-09-25 00:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 22bce89c-faa7-3997-8366-1621aa9633d1 | -11.6757 | -50.5796 | 2026-09-25 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e025a5e7-efdb-3353-b9ae-186164a40baf | -1.2189 | -54.5592 | 2026-09-25 00:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| f0eba121-03d4-3ff5-a5ab-ee8bb25e64c8 | -5.7754 | -45.1053 | 2026-09-25 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| ffccc89d-c3de-3f6b-8fad-3389de943f3e | -12.0799 | -50.275 | 2026-09-25 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 5956c837-b27f-372a-bacd-c2f760739666 | -3.25 | -46.9369 | 2026-09-25 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 365a1d34-bc2a-35d5-a34a-36e35240d208 | -1.1462 | -54.0796 | 2026-09-25 00:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| df4beb1c-026f-3fd0-9c4d-65384d403b70 | -4.5045 | -54.9646 | 2026-09-25 00:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ba0802f0-3ef7-3328-a654-425b894f2603 | -7.4038 | -64.3656 | 2026-09-25 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 97693dd2-7aa5-324d-917f-82c11d8eaf30 | -5.8808 | -43.7918 | 2026-09-25 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| af7eb1e1-9770-36d6-8562-be200ad425aa | -11.6564 | -50.6031 | 2026-09-25 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| f0ad99ae-dc3c-3e56-8960-0ef558ef0fc4 | -3.2501 | -46.9149 | 2026-09-25 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 6e8b98fa-48d9-3b66-8adc-d3430a4f0315 | -9.1627 | -60.7756 | 2026-09-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 7b697e3f-b326-3ab0-bed2-89bebad9eff0 | -8.9663 | -72.8525 | 2026-09-25 00:30:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 41aa0989-58de-3b13-bb4e-af03868e2d92 | -9.0343 | -60.5321 | 2026-09-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 8e4a382a-0d62-3d6b-9073-f243035c7519 | -11.6009 | -50.5025 | 2026-09-25 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 594745f6-94f9-3103-8025-7fb9b50181ef | -12.0796 | -50.2966 | 2026-09-25 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 1254de6a-12d3-35e8-b8a4-c164faa91f65 | -11.6945 | -50.5988 | 2026-09-25 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| e2ac7d92-31ac-3ab3-a3d1-5b65b37bf24f | -9.6298 | -43.9453 | 2026-09-25 00:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 8bc158b7-0fd1-3937-a391-15ee527e7982 | -9.0344 | -60.5129 | 2026-09-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 057e138b-5645-31ad-808e-f0a3ec0d2993 | -8.3211 | -44.1447 | 2026-09-25 00:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 77b16ed3-33f3-338f-a94f-7203d02a48a4 | -9.0157 | -60.533 | 2026-09-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8574e7f1-724e-3457-ac02-f2f550347291 | -9.1812 | -60.7939 | 2026-09-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| c953ae43-c154-304b-9736-6504cfed880c | -5.8047 | -43.9132 | 2026-09-25 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 3bacf35a-37b1-3239-aa84-867cb15fa7af | -9.1813 | -60.7747 | 2026-09-25 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 871df5f0-a45d-3c67-9578-ed66d8e6f8d2 | -11.6754 | -50.601 | 2026-09-25 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 1d7f027c-5c46-3066-8288-132e76bba816 | -10.1574 | -46.7352 | 2026-09-25 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0c7aaeb6-2685-361f-acd5-1a9b4d921394 | -7.3854 | -64.3662 | 2026-09-25 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b07077ec-8b5d-353c-9ae6-4e153ed9a5fb | -12.0609 | -50.2773 | 2026-09-25 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 20b22190-28b9-3c21-9e63-cefbba677e4a | -3.23 | -46.93 | 2026-09-25 00:30:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 664429ae-060d-3003-8cbd-01c19bf78470 | -7.8896 | -54.7609 | 2026-09-25 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 029cdf6f-357a-3b9d-8e3c-380ab52ca2b7 | -1.1462 | -54.0796 | 2026-09-25 00:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 2a903cab-73e4-3238-95a6-d7d2b11990b1 | -7.9084 | -54.7396 | 2026-09-25 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| bf887cc4-ac04-30f9-a129-c7d04a8813ed | -12.0609 | -50.2773 | 2026-09-25 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 389.1 |
| 82f98b23-56e9-3814-b858-a76c1d5087e9 | -11.5303 | -45.3783 | 2026-09-25 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| fcbf43ee-6117-371e-a768-b2491fa218c7 | -3.2501 | -46.9149 | 2026-09-25 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 65bb3c10-5f06-3a3f-a820-06e24cae27cf | -5.786 | -43.9147 | 2026-09-25 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a37f4262-2ed3-3efa-ac50-d09a9a05a464 | -11.9586 | -50.7393 | 2026-09-25 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| d05d6420-537f-39fc-8b2b-ada362b8a8a6 | -7.4038 | -64.3656 | 2026-09-25 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 6a07230c-b852-339b-82ce-d26b2f2688ee | -11.9399 | -50.7201 | 2026-09-25 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 94bc3840-365e-390b-afe9-d20ea150b1a8 | -7.3853 | -64.3849 | 2026-09-25 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a20a2b1a-4ab7-3b68-ae03-30b3742444a2 | -6.8817 | -55.5592 | 2026-09-25 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 7f659f33-3f3f-3717-81f9-257bf0e65480 | -11.6757 | -50.5796 | 2026-09-25 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1f085107-1785-3b9d-84de-21598bec6bea | -1.1461 | -54.0996 | 2026-09-25 00:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| f9d89170-3a69-3c01-b106-152122e1e3a6 | -3.25 | -46.9369 | 2026-09-25 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 162.0 |
| e28862d4-0f65-3b85-9c68-1c3a6a525713 | -8.3211 | -44.1447 | 2026-09-25 00:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 4735771f-0260-35a4-b6d5-9bc2d471dbda | -11.6564 | -50.6031 | 2026-09-25 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 63d146e5-d597-338a-a2cc-5e582f7e9350 | -9.0158 | -60.5138 | 2026-09-25 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f1119898-b731-3702-8461-a6e73f879460 | -7.4222 | -64.3651 | 2026-09-25 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 53f57ffb-c5b7-3ba1-8468-95669e3f6529 | -9.0157 | -60.533 | 2026-09-25 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1659a908-1ca4-32b9-9263-c46ffef89869 | -11.5108 | -45.4041 | 2026-09-25 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 6dbf83ff-ce6e-3bc1-9f77-c20951eb285d | -12.0799 | -50.275 | 2026-09-25 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| d8b36ff9-cda4-3a50-8716-e0e843c9b3d7 | -7.4221 | -64.3838 | 2026-09-25 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ca9e5a9a-46ae-379f-b91e-de83a8d3b822 | -7.3854 | -64.3662 | 2026-09-25 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 1bd1be55-b1c2-3c16-af13-39c76d1fe570 | -9.1813 | -60.7747 | 2026-09-25 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| fde9c5d1-39e4-341a-9c88-881d67f37237 | -9.1626 | -60.7948 | 2026-09-25 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| d867529e-152d-3fdb-8ca3-8af76d492906 | -4.5536 | -43.6513 | 2026-09-25 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| e76dca73-cbb6-35ba-9018-85d4f2182748 | -10.4237 | -53.7809 | 2026-09-25 00:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 49fef92e-cfed-397b-bfb9-79e8f554a961 | -12.0418 | -50.2796 | 2026-09-25 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 181.2 |


[Clique aqui para ver as próximas entradas](README5.md)
