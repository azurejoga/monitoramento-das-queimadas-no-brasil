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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c6c7a7a-33e3-3f14-b8ab-0f3a120355d7 | -12.41633 | -63.02776 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85ac4fa4-a1c9-3b85-a78a-1422729a6228 | -12.41174 | -46.62729 | 2024-10-09 04:40:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02bec135-5f92-3103-b473-cf23aaf2495f | -12.37921 | -47.67755 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cac9ca8b-e971-306e-9c09-1e19ef3e29a0 | -12.37622 | -47.67291 | 2024-10-09 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9242b952-07dc-3850-9f05-4937cb3efc66 | -12.35791 | -59.29545 | 2024-10-09 04:40:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddb1ba14-44e2-3672-a916-c4d4e87a8940 | -12.35092 | -54.15397 | 2024-10-09 04:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 976a29a8-82e8-330e-81de-a3f290011bd7 | -12.32381 | -50.94336 | 2024-10-09 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 142e1b8e-e525-3df4-9f68-10d41d1ece14 | -12.32325 | -50.94689 | 2024-10-09 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a65e20b-dd7c-38c7-8d23-996d06dc1473 | -12.31936 | -50.94989 | 2024-10-09 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb973663-edbc-3adb-b9cc-34b02f14419b | -12.3188 | -50.95343 | 2024-10-09 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ec44462-3139-3922-9032-b9f927243777 | -12.31547 | -50.95288 | 2024-10-09 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e61c2e6-bf60-34d5-9c5f-76acd2180567 | -12.31532 | -59.17361 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab7cb9af-bf11-3529-95e7-9e96ec25842f | -12.31439 | -50.93818 | 2024-10-09 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4411b7e-886c-3392-a1fd-c82bba110e12 | -12.31025 | -59.17274 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7911af27-27e0-376b-82d2-79a7979d69e7 | -12.30969 | -59.17572 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06f3c018-2dea-3a98-9f3c-fe016c1744aa | -12.30912 | -59.17871 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7db7ccdf-3ab1-3947-95f9-c88700d54658 | -12.30869 | -47.21669 | 2024-10-09 04:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3eed0ef2-0a5e-31ee-a1e2-795b67c9a3ec | -12.30502 | -47.21616 | 2024-10-09 04:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5aeb651-1705-36a8-9483-521ba938973e | -12.30405 | -59.17783 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbe64925-2f42-3dce-afa2-d07986afe6bd | -12.29474 | -57.88294 | 2024-10-09 04:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 063d3fe3-bf03-3e72-bcab-ac3a71599261 | -12.29011 | -57.88201 | 2024-10-09 04:40:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d05beb09-cb5e-38d8-a9c6-c8b6cab2dea3 | -12.22703 | -50.43878 | 2024-10-09 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9894bfa-cc58-377d-aca9-ba4285e92577 | -12.2245 | -50.43796 | 2024-10-09 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbd7eba8-29d5-3b60-ac1b-c8b5e82eedeb | -12.22276 | -58.92433 | 2024-10-09 04:40:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 009e36d2-ed92-3b24-8220-6634e53ef3f6 | -12.20628 | -46.72023 | 2024-10-09 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f1a14f3-c4f9-3084-95cd-3050885f5dba | -12.20585 | -54.2579 | 2024-10-09 04:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb1913fa-8575-374a-8590-a3be9c20a0ce | -12.20561 | -46.72483 | 2024-10-09 04:40:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7520e4dc-1b3d-3efe-bd10-3e5b018e4685 | -12.20121 | -50.58627 | 2024-10-09 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 829dc942-4c2a-3745-9cda-3a02779a6276 | -12.13339 | -63.36184 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb66dd87-7bfa-3463-867b-3055bf5b23d2 | -12.1322 | -63.36762 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe9c6cca-e5ee-3cb6-b84d-3476dda18eb4 | -12.13083 | -63.36103 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f8f8d53a-3a4f-3a9f-95f9-245e42722151 | -12.12961 | -63.36679 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 295b1326-b245-349d-857c-95b19f84e84a | -12.12684 | -63.36037 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5506dd79-b4b3-3f1c-a167-c11e7431aff9 | -12.12565 | -63.36612 | 2024-10-09 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c322d62-998f-34e9-93ae-14fd32af5b86 | -12.08487 | -48.64987 | 2024-10-09 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2d7cc34-d6ba-3ab4-89f2-fbfbea668263 | -12.02053 | -46.89019 | 2024-10-09 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 877e5546-9727-389e-ad7c-8a2f3223eba9 | -12.01764 | -51.064 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 145667a6-7b12-3727-8671-31f78a89d240 | -12.01046 | -51.04464 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55387f33-f023-3cf4-89a0-06a26e7c3714 | -12.00989 | -51.04818 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4ae1e89-7d37-3e17-a14a-7c7e21dbd1de | -12.00712 | -51.04409 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2410272b-df4f-3c49-b264-a856a109bfff | -12.00656 | -51.04764 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 228c2f5f-a439-32af-8409-39415f3b204b | -12.00379 | -51.04355 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f1aeddd-c403-3430-b812-b237e7036f5b | -12.00206 | -51.07598 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8c6d1fa-5458-3fd7-a2bf-3811535d3a47 | -12.00154 | -57.81547 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f92dbb8a-7f78-3fe7-a7b4-7b67fcdd1aaf | -12.0015 | -51.07952 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c671e0a-c6d2-361d-83dc-a6d266ad0bc9 | -12.00063 | -57.82039 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ef68b0c-344d-3c3f-a0a9-c7f36f95b64a | -12.00046 | -51.043 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80beefa7-48b5-32ba-93be-0fd5433734a7 | -12.00029 | -48.633 | 2024-10-09 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad74ecdc-76a8-3b27-8fc1-958a36e6e617 | -11.9999 | -51.04654 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79935e24-7fa2-3cd6-9f7b-db5f4e3493ef | -11.99691 | -57.81452 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65f33ad6-f43e-3c8f-8d8b-d66439495db7 | -11.99601 | -57.81941 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6592108b-97d6-3dd3-b56f-e0258f64bc16 | -11.99601 | -51.04954 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c154aed1-3501-3850-a459-4393683b11ac | -11.99544 | -51.05308 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 300df851-5691-3473-a0c6-d013e45fd350 | -11.99488 | -51.05662 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ad46fee-79c4-354d-aaac-12c72d3d8339 | -11.99429 | -51.9147 | 2024-10-09 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41d39a76-6ce9-3f4c-b0ff-a4af183f4a14 | -11.99032 | -51.91777 | 2024-10-09 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec31c4fc-b6c6-3c53-a364-744eff2791e8 | -11.98991 | -51.0449 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3423b970-f7a4-35bd-bdbd-645fc01e09cf | -11.98943 | -51.91741 | 2024-10-09 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41a62919-fc22-357d-8fee-f641b71dc672 | -11.98658 | -51.04435 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69693f2b-79ac-3bf4-a582-ffd2d266521e | -11.98605 | -51.91683 | 2024-10-09 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8511603-d3c8-31ec-af69-9de0ac6ef975 | -11.98601 | -51.04789 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 403a4e22-98bb-37a2-ba6b-b105c6dca607 | -11.98546 | -51.92049 | 2024-10-09 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38dfb1eb-bbe5-3a6b-bcc2-fa2bc4fd1374 | -11.98209 | -51.91991 | 2024-10-09 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 533139bb-ac91-3631-aabb-8076ded5aec0 | -11.98043 | -51.06152 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbed1328-5ec1-31fa-a014-eb3a98827dfd | -11.97874 | -51.07215 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 979a8e0a-36a8-3635-b4d3-15cf444748e4 | -11.97871 | -51.91934 | 2024-10-09 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64ea3f24-b954-37bd-ad8e-827fedbeb7b1 | -11.97817 | -51.07569 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebbccd59-f197-3f5f-99e3-5af98084e5d4 | -11.9771 | -51.06097 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c02423dd-8ec1-3cfc-8c60-c5a60701094f | -11.97653 | -51.06451 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 69d456b2-68ef-39e9-a74d-1d164def3578 | -11.97597 | -51.06806 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 785519ca-2f07-3fa7-9355-5535c11c2ccb | -11.97541 | -51.0716 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 797c083a-c3ad-3c9b-af79-16c111683aaa | -11.97533 | -51.91876 | 2024-10-09 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fde8b6d0-ec24-3374-8dfc-b363cfa44222 | -11.97484 | -51.07514 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7befd3c1-8196-3126-8304-f524bd349581 | -11.97264 | -51.06751 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e01637cf-5faf-3e07-be1d-179f9d6236a3 | -11.97207 | -51.07106 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9849b773-d841-3e94-92f4-4a660dda1721 | -11.97151 | -51.0746 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b445b154-9956-3438-8296-48009f19f1a4 | -11.9662 | -57.60009 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cbdb151-b60d-3dfe-9496-343038a0d126 | -11.96534 | -57.60484 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 239b5a50-f81e-307d-81fc-96a87b42d3c1 | -11.96241 | -51.91283 | 2024-10-09 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 304a1418-fbe1-30be-aa44-d416195ca463 | -11.96161 | -57.59928 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a4f9e3c-5644-3c51-814e-d4eadbbf0daa | -11.96076 | -57.60402 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f53c73fe-1fe4-3d78-9bd1-59b14a8c9754 | -11.95903 | -51.91227 | 2024-10-09 04:40:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 478ffc0a-7c8a-352a-b098-0ee8a0513287 | -11.95703 | -57.59845 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f620288-79c2-3fbf-85a2-34054bc6b4c2 | -11.91387 | -48.29905 | 2024-10-09 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bd9298f-ffb0-3f7c-b5cf-946beb287d80 | -11.91096 | -48.29464 | 2024-10-09 04:40:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45268bb5-f0b4-3677-adff-0949103b0715 | -11.90118 | -57.46579 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 909e5912-35bd-396d-b445-d412aa9fec3b | -11.90048 | -57.46805 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 959278b1-a158-300d-a621-a812aa04a712 | -11.89671 | -62.78048 | 2024-10-09 04:40:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6db7372-3531-3f1e-a966-a505b70f8435 | -11.89663 | -57.46497 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2789c2c-7a76-3301-bfab-9458da0b1639 | -11.89593 | -57.46724 | 2024-10-09 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b94680ce-3461-36bf-95d1-a4194a31580a | -11.89415 | -63.2838 | 2024-10-09 04:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66677b6b-ca25-3a60-a491-2308903a74b8 | -11.89033 | -62.77921 | 2024-10-09 04:40:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89590ec7-17ee-30ad-97df-b80910a7b9f8 | -11.88761 | -63.28227 | 2024-10-09 04:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c45ae9d-69ee-3b47-9312-eb0b2d056fe6 | -11.88643 | -63.28797 | 2024-10-09 04:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39a91a79-3127-3460-b252-615c6ed6e80e | -11.88106 | -63.28083 | 2024-10-09 04:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb2ed008-79ff-3837-abe6-5723571146c7 | -11.87387 | -63.2935 | 2024-10-09 04:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1f75832-e152-31d7-ab05-22468dd6786d | -11.86733 | -63.29198 | 2024-10-09 04:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57333a0a-fb9c-33c8-940d-e604c0df9a7d | -11.8102 | -58.51361 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfa05ca4-325b-3667-a494-4300e9a4052d | -11.79354 | -47.38442 | 2024-10-09 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5fa54194-9664-3581-b790-4fbe78d647db | -11.79292 | -47.38863 | 2024-10-09 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README146.md)
