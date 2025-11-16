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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8b1b260-7500-3e83-97db-64758b6976e1 | -4.62625 | -47.4067 | 2025-11-16 05:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c4a9d269-aa24-3be1-bed0-08149e409a23 | -7.23069 | -47.98071 | 2025-11-16 05:25:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac0b275d-27ce-35c8-a8bc-661326c23e67 | -7.22226 | -47.97985 | 2025-11-16 05:25:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db9f3508-ef33-3b50-87b8-87bd8c036bd3 | -5.12961 | -55.96417 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d46b7a44-78f0-3fa5-8c75-333dc02c969b | -4.73441 | -46.38464 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 542541b7-1f71-30a8-a64f-4ca97035a1d4 | -4.25058 | -50.04908 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1bd028f-2b5c-3f0b-b9d1-a8798dec80f2 | -2.58987 | -51.82859 | 2025-11-16 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6f0606d6-ec8c-348c-821c-27ce6cc72bb1 | -6.1388 | -48.0495 | 2025-11-16 05:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43a198aa-53b4-36cf-ad32-85d431581c95 | -1.80645 | -54.65556 | 2025-11-16 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dabe04e-7d2c-3b9e-84ff-def9aa225f53 | -2.80368 | -52.9655 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06440108-5205-360a-be3c-994783eb5d9b | -1.22247 | -55.83366 | 2025-11-16 05:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26da7763-7e83-3e9c-896b-61205bd52d6e | -2.89037 | -53.28482 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 22e92bd8-317d-3b15-893e-3c6695974a63 | -3.49407 | -54.04211 | 2025-11-16 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b1b8d79-f497-30b3-9eb8-1141c0905461 | -4.74162 | -46.38544 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| df41c0d6-2d79-3f02-90f5-179a957ade56 | -3.86452 | -54.35559 | 2025-11-16 05:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59e3ede7-fdab-3044-87f0-9cbb1a30d80e | -0.88073 | -48.08348 | 2025-11-16 05:25:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c3a85e26-2c40-37f0-8159-c04314af8242 | -3.08188 | -52.9178 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fc8487e-0b14-3bb1-b810-0fa5eb052ec1 | -2.58496 | -51.8278 | 2025-11-16 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e76a70cf-7b1c-3913-b40c-24eb61df9867 | -2.86894 | -51.47076 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9966577-bc09-33a9-afbe-83f879d95a34 | -2.86849 | -51.47371 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05196575-6dc7-3471-b382-4c585b5de03a | -2.96903 | -53.22014 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc2831f9-d0ca-37ec-b6d6-061eb0be4817 | -1.3223 | -54.21906 | 2025-11-16 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6025acc-d679-3a92-99bd-004869684c22 | -4.65855 | -46.74496 | 2025-11-16 05:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f65f033d-95d6-3622-b0d6-a37b3caa0351 | -4.68576 | -46.5261 | 2025-11-16 05:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f114123-9d78-3f87-9a15-a76cbc4ced64 | -1.3496 | -54.6084 | 2025-11-16 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d14d05af-c1ce-388e-b4cd-3016341007ae | -7.72002 | -47.28854 | 2025-11-16 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3feb48c-cfff-3549-a85b-4fef8f8c0534 | -4.67558 | -50.3688 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d6d561e-21af-335d-bec4-3a213532b33f | -0.87536 | -48.084 | 2025-11-16 05:25:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9189edf-9628-3a62-9284-3eb100b73a08 | -0.95548 | -52.34006 | 2025-11-16 05:25:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f413b0c0-9435-3224-a75c-98fadb102ad6 | -2.52673 | -47.80913 | 2025-11-16 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c4b048d3-d61c-3ac0-a3d5-87d20a3eb24a | -6.81602 | -48.79152 | 2025-11-16 05:25:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 171ac80f-4727-34c1-8d80-aae6e7d45d03 | -4.11426 | -50.05782 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f713fbd-7bdf-30f6-9c2b-1b39765f6781 | -1.32003 | -55.38639 | 2025-11-16 05:25:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be79a55c-46ac-3003-bb13-854ce9ff5b00 | -4.67 | -50.36787 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88e08d82-e87f-371f-90fe-dca8d50751ba | -1.85002 | -56.37582 | 2025-11-16 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ed159d6-ba39-3d77-89e6-8fb686ba084b | -2.52517 | -47.81961 | 2025-11-16 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| c8419fbf-5559-32c3-b8e5-5cf4d5a36014 | -3.4661 | -50.11869 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cefa7510-c1be-3835-8bec-f06134cd38c8 | -5.12755 | -55.96097 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3b2712f-c56d-31eb-afe6-06ed54762af4 | -2.68704 | -49.0719 | 2025-11-16 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bde5982-ed24-3cb0-a8c5-5faa9263887e | -2.85594 | -51.28058 | 2025-11-16 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf131139-dc6a-3b57-b61b-12a97bb49f6e | -3.4156 | -52.36332 | 2025-11-16 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0e05991-7f98-338d-8922-aa72721ccc22 | -3.39519 | -50.1826 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 32d647fc-8d33-3e9b-9709-3b67c5a41bcd | -1.87755 | -50.95146 | 2025-11-16 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37053de1-6d47-317c-8bc4-ee0681d5662a | -3.035 | -54.59613 | 2025-11-16 05:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8d0c9e6-5451-3fb6-b87d-a5868c97417f | -4.50098 | -50.79473 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ded41f5-83c3-3524-b70f-012754d795c2 | -7.22398 | -47.97955 | 2025-11-16 05:25:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bdd4a43-3f46-38bb-811c-80e15ce5c116 | -3.54475 | -55.48843 | 2025-11-16 05:25:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02ae9db6-2306-3a09-bef8-dbe45be929f5 | -4.15844 | -50.22733 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 173eb915-5e96-3933-a872-2c79d46d9b12 | -2.89416 | -53.28988 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f034a389-ba53-3dfc-98df-94bb2c671ba3 | -3.20877 | -51.58312 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43bdf791-5d19-3066-a54e-4df9a4b09edd | -5.13199 | -55.97432 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d356d1ed-f7be-3cce-a4dc-2cf20df3c0b4 | -3.54864 | -55.48903 | 2025-11-16 05:25:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dba9f93f-c78f-33d5-9f02-9d48ed1da826 | -2.96688 | -53.21862 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c36eee7-d1f5-3b21-b2e8-efd7d2fa3ce8 | -5.48974 | -46.91605 | 2025-11-16 05:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 14357886-3ab1-3518-8a50-de86c7e0768a | -3.2075 | -51.58511 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c1f1a78-cd49-3aeb-ae56-e9cfa51e3f64 | -3.33118 | -50.26957 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c2a286c-1bf0-3b87-b3da-a2ebd6691934 | -1.3485 | -54.60581 | 2025-11-16 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4746f34-d046-3624-8c1f-b161eb81f9b6 | -7.21551 | -47.97898 | 2025-11-16 05:25:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10423641-1489-398b-8e41-66d001c987e9 | -2.7998 | -52.96028 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ee0c352-7a8d-3b09-a1ca-2ffea8479454 | -3.32958 | -50.28045 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6a2d7b4-cd63-33f1-b94f-3570f0a1b61e | -3.4898 | -54.04142 | 2025-11-16 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ea08dd7-7078-3b8b-bcf1-1781381fa171 | -3.28693 | -53.82835 | 2025-11-16 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 375b9064-9042-3a2f-a064-9ec4fc05c7a6 | -4.50251 | -50.11573 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29f64eba-8396-3907-9143-ee17ee216f4a | -5.12542 | -55.97536 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bbbc5c6-8bbe-3fab-ae27-1d218a8f23a2 | -5.12813 | -55.97373 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ea1abcc-2152-3513-b4fe-1573b822c9f2 | -4.05047 | -54.83895 | 2025-11-16 05:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38fef74f-a10e-3772-9251-dec1f9deea50 | -4.80395 | -48.33976 | 2025-11-16 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f037002d-d24f-371e-a71f-aefbae7e94f7 | -2.13712 | -56.68488 | 2025-11-16 05:25:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1a07f792-ff9f-3c6a-a964-0a90dd057ba5 | -3.49347 | -54.04616 | 2025-11-16 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 566da3af-0e18-3c85-ad71-14325c88a431 | -3.39575 | -50.17891 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca0b40d6-ac5a-351f-a322-8ed3d6527acb | -5.49411 | -46.9157 | 2025-11-16 05:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3552c674-eacf-3aba-83c7-ed07d4d15b69 | -2.41547 | -53.94445 | 2025-11-16 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1445ed03-6f9d-3b30-a5f4-6f2692e8eeaa | -6.14966 | -48.04596 | 2025-11-16 05:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed4482ee-752c-3fc6-a879-3e75cabbc8a1 | -4.01383 | -48.80658 | 2025-11-16 05:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e9ab8d4-a813-37be-bba5-8f2a3e0a20ac | -5.12427 | -55.97313 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f749fcc-570a-3c22-8bbb-7831f0ce145f | -3.28326 | -53.82346 | 2025-11-16 05:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6c9acde-2600-32c9-8e15-edf4e8a9ad04 | -3.2758 | -52.99407 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08b58e02-019f-393e-baf3-7943aa7b0b62 | -1.57142 | -55.37965 | 2025-11-16 05:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 668e6db1-239e-3418-900b-537dd498fcc5 | -1.32176 | -54.22256 | 2025-11-16 05:25:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bb315bc-bafc-3bee-8cc0-3509688d3d60 | -2.31702 | -57.01237 | 2025-11-16 05:25:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9b52c37-667b-3ee4-8d09-4bdf9c7e56e0 | -4.65953 | -46.7382 | 2025-11-16 05:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e559bcea-379c-33c9-a5ed-af7286d7c2d7 | -2.88625 | -51.42532 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de950d11-6bfe-3ab3-bbcd-d506d501b2bb | -4.69844 | -46.31531 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 873180f0-70c0-36b6-befa-5f8c50034600 | -4.7323 | -46.38571 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6212606d-7b4b-347c-91da-25c7afd1aefe | -3.82016 | -49.1114 | 2025-11-16 05:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80e4d969-a5c3-340d-b0ca-9314e718153b | -7.26564 | -48.02841 | 2025-11-16 05:25:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 155b23e4-aa84-3a73-80b5-b662a86d783e | -2.88535 | -51.43119 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad1d92f9-c8fb-3fd3-90c5-e90414cc61ec | -7.71672 | -47.28739 | 2025-11-16 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d96809e7-f588-3741-8e37-8e58d53a6fa9 | -7.71285 | -47.28844 | 2025-11-16 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56edd827-f0b0-380f-bcd0-ea05d7a550c5 | -2.46962 | -48.86026 | 2025-11-16 05:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6d76251-6102-36e0-ad20-d4842dda3ab8 | -3.37961 | -50.13451 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 736567d7-7396-3a66-a8f0-4296208976d6 | -7.27234 | -48.02951 | 2025-11-16 05:25:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 658ec4a2-eff7-3407-94e5-4ac60afb1567 | -2.5172 | -47.8175 | 2025-11-16 05:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b9084c71-f9aa-347b-ab19-c424af268f2c | -4.1086 | -50.0569 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23f276cc-ecbd-3c06-9419-94a0ab3d0376 | -4.69123 | -46.31439 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 297129df-b509-365f-9cc8-5838e6464d99 | -2.89483 | -53.2855 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6cd95482-8145-3f16-b1c4-779059f1523e | -2.93539 | -49.34793 | 2025-11-16 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ff2ec74-cb58-375a-a98f-bdab915b01ec | -3.93222 | -47.05521 | 2025-11-16 05:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8d0c567-e9b8-354a-8188-f9675f956dee | -3.20707 | -51.58804 | 2025-11-16 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8cedf165-3544-3431-a5ee-a07d4ba09c39 | -4.73543 | -46.37735 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README63.md)
