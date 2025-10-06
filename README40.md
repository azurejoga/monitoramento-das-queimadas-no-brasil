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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef035fbc-5f45-3ed8-8ca3-40b6a6544606 | -13.30026 | -48.07935 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 44ae70d9-34a4-3860-aae5-a0533c8d8ec5 | -11.44374 | -43.48853 | 2025-10-06 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 574c759b-9cb2-375f-b248-499b8a62bd6a | -11.50391 | -54.47292 | 2025-10-06 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ad350934-09e5-3398-9f7b-8c1b2ded372e | -14.54724 | -46.96 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a31cec25-3014-326a-9098-f69e4ed97a23 | -13.0533 | -47.91599 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d4aa2b1-7b21-3f12-9fed-80ac3189e4bf | -14.94796 | -46.82882 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4326b348-39f1-3766-bf91-c88375c59a7a | -13.31953 | -47.1669 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14ccae96-59be-3cf0-a1b5-a8f3606aed0f | -11.63201 | -45.07557 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fef6cbb5-897f-378b-841e-c81676a211f8 | -9.68109 | -48.21086 | 2025-10-06 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f6592e5-883e-395e-9591-f8356aac32fc | -14.65516 | -48.35748 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a05305e-4ad4-3b91-a0d9-179c02e8a1bd | -14.9764 | -54.82958 | 2025-10-06 04:27:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65a6688f-c8d1-3815-b5f6-d7e7d407c5b6 | -11.81335 | -45.10154 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c37fb061-52c2-35ad-aab3-1053d18477f0 | -10.28656 | -50.28055 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab671ec2-c075-3faf-9c0b-fb8797dcb45e | -15.92727 | -48.62058 | 2025-10-06 04:27:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ebdc9aa2-8ff9-3cfa-bb08-f2c15206b0cf | -9.91597 | -49.23458 | 2025-10-06 04:27:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c025319e-b16c-352a-bd42-1c8ef7455b32 | -15.87415 | -46.25607 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b7f5621-702f-347d-80aa-7007223f7d2a | -16.00788 | -50.84745 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e0862c0-b667-3244-8db6-3552abf9163f | -12.22324 | -44.2421 | 2025-10-06 04:27:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4210593-57fb-3583-a3fc-26f3b3bb7144 | -9.61616 | -57.20296 | 2025-10-06 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7f8006a-982e-3fd0-ad0b-ed9530b80008 | -12.57837 | -46.74615 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 326cd335-5945-365d-9e7d-f6c29636d367 | -11.15867 | -47.93336 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 294b210b-b821-3822-991f-367285440b62 | -10.41868 | -50.34009 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 791552e9-7e81-3228-b61e-b76aab25a558 | -14.95511 | -49.98578 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1efe064e-23fc-3962-9333-d9afeaaec75b | -9.685 | -48.20782 | 2025-10-06 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f36bb37-a3f2-3a40-adee-5549ada2f50f | -12.82067 | -46.85062 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c87031dd-688d-3c8d-b3aa-ed4c2d5de162 | -16.03631 | -50.95398 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5153ca9-cd22-339a-babe-7fe23a948bc5 | -9.33981 | -54.51828 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1d6edaf-79e0-3b2a-b468-e4d94e240ce1 | -11.11102 | -47.19866 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72ceeaa4-2e10-375b-a370-e58984eadd14 | -11.11487 | -47.19569 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f97a3f72-73b7-323d-a120-b36b87999068 | -10.76462 | -49.69964 | 2025-10-06 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0a913b81-fb63-3fcb-8d00-8830593a0176 | -16.00443 | -50.84688 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b836c713-6cd2-3dfa-a5f1-00017c4311b6 | -10.2687 | -44.95446 | 2025-10-06 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eab71e90-b0d5-393c-ab17-3f1266486025 | -9.91222 | -49.9566 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e4ea3ea-18d3-3d97-9c97-e279ff328946 | -14.65734 | -48.36509 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32c092c5-5f4b-3c2e-84ea-88a67ab0433c | -14.99204 | -49.97257 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fd538e4-6e7e-38be-b317-07c44bd5e723 | -11.71627 | -44.30752 | 2025-10-06 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12df5b67-64d3-3dcf-88dc-2f787ccdb545 | -12.41584 | -51.11277 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3c9a5ef-ce2a-3a72-bf6d-b5caf6d9e3fd | -11.11157 | -47.19516 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fbe99e0-5a8e-339f-a129-df6eeb577a4d | -12.98711 | -51.04348 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 995bc014-9697-3cc5-90d4-6d8f29d292e1 | -11.82264 | -44.89247 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b8596cb-b7b6-38d8-a87f-7cbc79e7a1b1 | -10.01792 | -48.29864 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6900c88a-167a-3e10-b6bb-a4762effc5fd | -13.27743 | -47.17515 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f03a73e1-ad0c-38d2-a8bf-b14630b34cfd | -10.37201 | -48.14864 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d47e3c9-2d5b-36bb-b2fc-33e42cac498b | -10.36812 | -48.15166 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 241e6a15-735f-3b2c-9c03-2c816d3ce792 | -9.61953 | -57.20301 | 2025-10-06 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05a58c2b-3528-3b28-aab4-0aaadffc3832 | -13.69237 | -47.32898 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4eb77288-e75d-3a80-b14b-f7e5d390ed34 | -15.62237 | -52.51907 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e180e479-b071-3c5d-b306-7b8fcf5c2e48 | -13.24993 | -48.46203 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ad35cdc-4f42-32ee-a976-1d7cdabbe0c7 | -14.66136 | -48.27496 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0efe13a-d6e8-3646-95fa-5618241f3dab | -13.37893 | -47.59775 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e5a72a1-7835-3652-9d69-c54b87027c53 | -15.62819 | -52.52999 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7813b96-5e0c-318c-acf4-d18149b63875 | -12.948 | -54.7275 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6bc24c34-42c4-35ef-90db-e277df19666a | -15.58226 | -52.44007 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 636e9718-e2db-336f-97c9-d41d6b2024f2 | -13.25922 | -48.48903 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c8d4955-e958-316d-98d7-f4e18a8110cd | -14.89616 | -51.50272 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 002ff9dd-f726-3e52-b543-909073ebc79a | -15.99047 | -50.92969 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 803f6fd0-32dc-38c1-8d5e-16d57e406006 | -8.62099 | -54.97075 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d1a94994-38d5-3859-992e-ff4a89f2e5a9 | -14.71507 | -48.36373 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07b6d115-d05e-3072-8c70-c28b910e2591 | -10.61958 | -48.66611 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3794fd2b-7b2a-3687-b793-a954101e35b6 | -10.58002 | -51.59569 | 2025-10-06 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac2ec9b2-7629-3d6f-9f8c-eee11fc2cde9 | -14.56655 | -46.66989 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71f5c913-f637-3d15-8a43-de14a2876986 | -10.37487 | -51.90242 | 2025-10-06 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d2cb2d0-e8d2-3640-8510-e436521470cb | -10.47754 | -49.08737 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83fd3ac6-2876-3548-b871-aa4a9a975eef | -11.75452 | -46.8195 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16e487c5-3855-323d-b05e-a07d9f5a7c56 | -14.1164 | -46.93328 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75c79b4a-adf3-3869-8348-296a87f7bfe3 | -14.66065 | -48.36563 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25e82a00-217c-3847-b4cb-5ad40e52284f | -10.36909 | -47.996 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb0a7e77-6de3-3b9f-96aa-6f6b329edf53 | -12.81853 | -50.52712 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01d3f9f6-c6be-3f72-9ddf-ce65f47ae73a | -10.09374 | -46.91402 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8fbc7580-77ca-3585-a1a9-fb861a2b2428 | -10.69112 | -48.04806 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09fbd290-4de8-3938-bdc0-b249869f4863 | -14.70955 | -48.37735 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9d3fc18-7ca8-31ce-a878-f337f268e82e | -8.62202 | -54.96503 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74c89a71-d8b2-3014-b7ed-9f02f9ec92ef | -15.7371 | -46.2589 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c785d44a-46ac-39c0-9376-445ba9291417 | -9.67815 | -49.94507 | 2025-10-06 04:27:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80ac1e30-b678-3e9c-a00f-4caf58110ed9 | -11.91253 | -46.22629 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac579070-101f-346c-9339-00410b21efd7 | -11.18385 | -49.99728 | 2025-10-06 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d80396d-634a-3bee-b730-58bb745922d3 | -14.92235 | -46.86184 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb56dc4b-d2e3-3a4f-8fd7-c00483136da3 | -14.8719 | -51.50428 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2277625f-b80b-34d7-af1f-450e3989afd6 | -14.62124 | -52.53799 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3340198e-877c-3415-959f-a587859c251d | -16.03065 | -51.03076 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cce75288-526c-365d-921e-ac6647fb1e75 | -11.11762 | -47.19971 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ce2045f-1b33-31b2-adf7-4dc061529794 | -14.93826 | -47.1371 | 2025-10-06 04:27:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bc5d2ef-928c-38cc-980f-0bae67f2ba6d | -14.68373 | -48.36945 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7078cdce-40f2-3714-b586-9e094912b996 | -11.06188 | -47.7705 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c6fdcd1-2f7f-3ce8-b16f-fee32f951735 | -13.05055 | -47.91194 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5aebc5f1-bce5-3dcd-a8c0-d59d1101cfe7 | -10.61564 | -48.66922 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6d5102a-004b-316d-8c06-689d9ecc22be | -11.70971 | -45.4214 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21a9d151-9af4-3371-9611-980e3eb64a87 | -14.60909 | -52.49574 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 388147f1-8fb9-3bdc-99bd-d71852c6bd88 | -13.3855 | -47.55524 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a401d811-38c2-3f18-96b6-aa609eab7676 | -12.94352 | -54.72658 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1949b016-8653-3f28-b96f-519897ebfdc9 | -13.12103 | -48.00635 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f58a07fe-7774-30cf-b5d3-03ab59b9c270 | -14.68702 | -48.37 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7c4ac59-895a-3ae4-9f6f-512752a3e989 | -11.23148 | -47.77258 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b26c5f0c-0794-3205-bc8d-01e51baca402 | -15.92671 | -48.62415 | 2025-10-06 04:27:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8daf468c-2568-3d74-8d5d-3f104229c141 | -15.20828 | -56.81142 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c706314c-bccb-32b0-adfa-380e561e4dc0 | -16.0161 | -50.84082 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a2a2647-4e02-3279-b665-82901dfda10d | -9.27553 | -51.80167 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4f3b0fc-4a1c-3383-9a13-c7cdc08ff149 | -14.66339 | -48.36971 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 985f72b5-a199-3490-8c64-16ee6befe049 | -15.51387 | -46.84087 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39ed0f30-5af8-30f4-949b-3fa9648fb66c | -11.02369 | -46.53018 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |


[Clique aqui para ver as próximas entradas](README41.md)
