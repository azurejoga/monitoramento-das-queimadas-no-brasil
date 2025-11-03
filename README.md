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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e9f4e50-b3ee-3748-a318-7d9730411781 | -12.6813 | -50.8669 | 2025-11-03 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| b34e6ccb-037c-3dc5-bcb7-435ec93b82a5 | -9.7815 | -36.0161 | 2025-11-03 00:00:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| f44de995-3044-31b8-b24f-f830155c9f83 | -9.781 | -36.0433 | 2025-11-03 00:00:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 62.8 |
| b4cadb4c-73bd-31d6-9089-cffc66d0cb70 | -12.6809 | -50.8883 | 2025-11-03 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| d53591b8-5808-3ee5-bfb1-7b0ea5f49b62 | -5.0399 | -43.6205 | 2025-11-03 00:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 6bbdb0e1-5894-301d-a789-1a2bc9ece055 | -12.6618 | -50.8907 | 2025-11-03 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 2271c90f-dcab-3cf5-abb4-aadd1bef5891 | -12.6806 | -50.9098 | 2025-11-03 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 433268c2-97cf-345c-b226-5e46740f75d5 | -9.8003 | -36.0399 | 2025-11-03 00:00:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| 25b724fc-173d-3894-821d-8a419aafadce | -12.6427 | -50.893 | 2025-11-03 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 9d582184-0e7f-319d-9a67-9ac70e2be6a4 | -9.8008 | -36.0127 | 2025-11-03 00:00:00 | GOES-19 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 116.1 |
| e3f9b0fe-b519-331b-a9c6-6f1d686cd913 | -3.4936 | -50.319 | 2025-11-03 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| f9530f55-faf7-3ebf-ade9-e6ecd6ca7f0c | -12.408 | -46.6413 | 2025-11-03 00:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| b00d6bd0-7692-3854-9e07-a2388ae2a798 | -12.6615 | -50.9121 | 2025-11-03 00:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| e023c3da-2564-3604-9dd3-d647ea190a67 | -11.7388 | -59.3034 | 2025-11-03 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 9fc04551-f790-3d35-87ed-6301a1b18a40 | -12.6618 | -50.8907 | 2025-11-03 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 65f2d669-e770-31c7-992c-488d2f29a74f | -5.0399 | -43.6205 | 2025-11-03 00:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| e675138a-d236-3f6c-b90b-1d22933d8866 | -12.6809 | -50.8883 | 2025-11-03 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 557e892f-a984-336a-b967-ecb77699a501 | -12.6806 | -50.9098 | 2025-11-03 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 92a9519f-9d85-3d8d-a120-ab277171b77e | -12.6615 | -50.9121 | 2025-11-03 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 9bd9ce2e-05fd-3c49-a8ed-c54a2c2adff3 | -5.0212 | -43.6218 | 2025-11-03 00:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 3539fad1-0534-39e2-8122-f1015af3a595 | -3.4936 | -50.319 | 2025-11-03 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 6a9e95dd-b2f6-38be-bf21-24b083f48337 | -12.0579 | -51.7473 | 2025-11-03 00:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| c21693fb-cfa9-3609-9867-06d4b5ec5921 | -12.0773 | -51.7241 | 2025-11-03 00:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| d708f444-7b94-3af1-81cb-0debdc5e97ce | -3.4936 | -50.319 | 2025-11-03 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 8a93757b-c95d-36d6-ba98-df518db26f60 | 1.6021 | -55.667 | 2025-11-03 00:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| a4e5b0ec-b40a-39e8-9cfd-ff1ce9f316b1 | -12.0582 | -51.7262 | 2025-11-03 00:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 5a704cf3-b455-30fe-a24f-eff61de34c8a | -12.6809 | -50.8883 | 2025-11-03 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| cb28cb4b-9a09-3966-822a-b011cc5f66f5 | -5.0212 | -43.6218 | 2025-11-03 00:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 66dec872-b1cc-3795-b632-f3d4079eb757 | -5.0399 | -43.6205 | 2025-11-03 00:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 19cec6a8-4463-3eeb-b65d-abb1185ebb95 | -3.4937 | -50.298 | 2025-11-03 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| dfa11cbd-4675-3e9a-a042-ed4e11c7167d | -12.077 | -51.7452 | 2025-11-03 00:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 6c697c18-8e1e-3cc5-ac0d-609819a7aec4 | -5.0399 | -43.6205 | 2025-11-03 00:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| df8ce860-0ab6-3d31-9791-3d8de763d920 | -12.077 | -51.7452 | 2025-11-03 00:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a9401f35-afa5-3646-8331-208e3529254a | -5.0212 | -43.6218 | 2025-11-03 00:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 0241bd19-5273-3d81-ba85-b656e4e7916c | -3.4937 | -50.298 | 2025-11-03 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 700a4d90-f3e9-3049-91e2-481d159e65d4 | -3.4936 | -50.319 | 2025-11-03 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 1008099b-8878-30fa-ab27-927dea7a02d6 | -3.4752 | -50.3196 | 2025-11-03 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| afa844cf-12e6-383e-94e3-fc491a021c78 | -12.0579 | -51.7473 | 2025-11-03 00:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d37392b6-76b0-3cd5-8aeb-aedf5140e205 | 1.6205 | -55.6272 | 2025-11-03 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8e8c45ba-10be-3864-8388-f78df748baba | 1.6204 | -55.647 | 2025-11-03 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ad2f4ae1-00ca-3c13-a29c-00196a84a32e | -12.6809 | -50.8883 | 2025-11-03 00:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 3964cb35-02f2-31be-8349-688d9ff68c93 | -5.0399 | -43.6205 | 2025-11-03 00:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 9fd8385c-b794-3ff0-b70d-85b98598e202 | -5.0212 | -43.6218 | 2025-11-03 00:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 96b7dbe6-429b-3eb3-9aa6-f9200431c354 | -3.4936 | -50.319 | 2025-11-03 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 025c9286-860f-3b83-a260-dfa745b1a615 | -9.5156 | -40.3061 | 2025-11-03 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 114.6 |
| 888d794e-38d9-313b-87c7-f3aaf281b342 | -3.4937 | -50.298 | 2025-11-03 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b25d6bb0-d84c-33c6-9c9d-e8e086e6c518 | -9.5156 | -40.3061 | 2025-11-03 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 140.6 |
| 2fe51181-0807-36bb-8b81-a03bef9cfd70 | -12.6813 | -50.8669 | 2025-11-03 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 3c9d650f-9094-3936-b4b6-88e2b0ec5002 | -9.5152 | -40.331 | 2025-11-03 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.3 |
| ba22d351-a31d-33b8-b88d-0ad8860980fd | -5.0212 | -43.6218 | 2025-11-03 00:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 0ae66001-59f3-37a3-882f-d1928de4c573 | -5.0399 | -43.6205 | 2025-11-03 00:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 160.3 |
| d01beadb-ee5e-3c76-a350-65a8349630dd | -3.4936 | -50.319 | 2025-11-03 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| a7e10522-ac77-3860-a61c-22f7e9be7cc9 | -12.6813 | -50.8669 | 2025-11-03 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 01402bf5-4130-3948-8bac-a558a09c56ef | -3.4936 | -50.319 | 2025-11-03 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 49ea9dd9-28e7-3329-b828-5899b1285174 | -11.7388 | -59.3034 | 2025-11-03 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| e478d983-fca3-3e5f-94bf-00fd62776c52 | -5.0399 | -43.6205 | 2025-11-03 01:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 3475f0be-b69a-3c51-a437-f2e8b2ed7ddc | -12.6621 | -50.8693 | 2025-11-03 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 134aa9f2-a4ba-329c-a93e-149fb343188a | -5.0212 | -43.6218 | 2025-11-03 01:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9595fa40-ac44-3862-9766-2cfc96bac2fc | -9.5156 | -40.3061 | 2025-11-03 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 132.8 |
| 330c1e08-4cbe-3484-8d77-e27f83201563 | -12.408 | -46.6413 | 2025-11-03 01:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f29199c2-b0f5-3847-bb62-8154e1da8305 | -12.6809 | -50.8883 | 2025-11-03 01:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| ed2e9c82-5669-3d4b-b3f1-9caeaf01a002 | -9.5152 | -40.331 | 2025-11-03 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 2adb57d7-b1ac-31d3-ba56-acced4703bd6 | -12.6813 | -50.8669 | 2025-11-03 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 5d7221df-129a-3a6b-bfd5-548949db1e98 | -5.0212 | -43.6218 | 2025-11-03 01:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 15b15615-e8bd-3ab2-bb40-b9e4280f0c77 | -3.4936 | -50.319 | 2025-11-03 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 24e5d11d-fef4-31a7-b834-2eb848d3803e | -12.6625 | -50.8478 | 2025-11-03 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c453558a-6fd2-3a02-8e18-326eeb155d0d | -12.408 | -46.6413 | 2025-11-03 01:10:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 75276e01-a6d1-3d88-87bf-ba0e3b5195a8 | -12.6816 | -50.8455 | 2025-11-03 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f37a9373-d589-363f-a824-436c8e0734fb | -12.6621 | -50.8693 | 2025-11-03 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 18b0ba9c-f37b-35dc-a488-becdc32ccfdc | -12.7004 | -50.8646 | 2025-11-03 01:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 1adb45b4-0d2b-38a3-8ade-2206611ebfef | -11.7388 | -59.3034 | 2025-11-03 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 3805cc1d-59ab-34f0-adc0-29b60cffcdac | -5.0399 | -43.6205 | 2025-11-03 01:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 371392d7-1e02-341d-9594-754e6f498d02 | -12.6813 | -50.8669 | 2025-11-03 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 120.6 |
| a4e2c484-5562-30ba-a26e-6fe04d39e86d | -12.6816 | -50.8455 | 2025-11-03 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 66f544e0-e1b5-36b2-82d2-0cfdc20a4cf5 | -3.9147 | -44.3309 | 2025-11-03 01:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| f4269b6a-284f-36fa-935d-b96e1097ea60 | -3.9148 | -44.308 | 2025-11-03 01:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 0ab92835-52f0-3b18-92d8-cac7f08b76d4 | -3.4936 | -50.319 | 2025-11-03 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 363c0113-57e8-3a9c-94bf-716b606f0be5 | -12.6621 | -50.8693 | 2025-11-03 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| afecbb0d-9bce-310f-9cfb-2885127ae8c8 | -5.0399 | -43.6205 | 2025-11-03 01:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 7d68ef9f-41b2-3528-be38-55eb55fc475c | -5.0212 | -43.6218 | 2025-11-03 01:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 71954297-102f-32c2-b99c-ee0c4cbe754b | -3.4937 | -50.298 | 2025-11-03 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bcee5f41-f049-3d5c-9d94-77eda626e317 | -12.7004 | -50.8646 | 2025-11-03 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 1ab10c69-71e7-3a8e-a479-5032126a7b1a | -12.6625 | -50.8478 | 2025-11-03 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 8178fd0b-c7ee-38f0-ae1e-e8a4ad972b57 | -12.6621 | -50.8693 | 2025-11-03 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 0ce720e8-4a90-33fd-aa45-25ec04ff7ce2 | -3.4936 | -50.319 | 2025-11-03 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 9feefdda-a480-38d6-a146-59eddbcf7a2b | -12.6813 | -50.8669 | 2025-11-03 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 0d1f31ea-3d75-3d24-9aa6-60882e8f63b7 | -3.4752 | -50.3196 | 2025-11-03 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1d0564fb-89a6-3c70-bff5-8a030993f9cb | -5.0399 | -43.6205 | 2025-11-03 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 1bd7392a-51a0-36a4-82f9-900d63c2f8d1 | -12.6816 | -50.8455 | 2025-11-03 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e2bf21b3-ab8a-35cc-ab1b-15988e42e682 | -5.0212 | -43.6218 | 2025-11-03 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 9260b0eb-6582-3a8f-a189-4e94057728e3 | -8.76824 | -63.50803 | 2025-11-03 01:32:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 767cf624-6851-3bef-b6b4-607fa4d3672c | -10.85328 | -56.96465 | 2025-11-03 01:32:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 0f92318c-2c4b-3718-8a59-3d0df227b849 | -7.80741 | -61.34402 | 2025-11-03 01:32:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fd59d129-0fc3-33de-940b-3e26013982ce | -11.61928 | -58.28592 | 2025-11-03 01:32:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b47c13b5-f7a4-3a7a-812c-4101eb7200f7 | -12.57915 | -62.95782 | 2025-11-03 01:32:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| db143525-bf90-3e99-8f52-bf90cd6e1701 | -5.1861 | -60.3097 | 2025-11-03 01:34:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b9cf5c59-2e7d-3e51-9694-004b6816f0bb | 3.22886 | -60.7502 | 2025-11-03 01:34:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 492a9c87-2ec3-3c92-b5c5-e9be5348c9a8 | -12.6813 | -50.8669 | 2025-11-03 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| c47fb04f-5078-3576-9cdd-eb8da5eaeabb | -3.4936 | -50.319 | 2025-11-03 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 7f8ab8be-b49e-3959-9ad5-c5d2967aabe7 | -12.6621 | -50.8693 | 2025-11-03 01:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |


[Clique aqui para ver as próximas entradas](README2.md)
