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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1227a65e-87bd-3061-b6f9-69f3cf328b90 | -11.80623 | -46.82174 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90ef5c80-8c5f-374a-a050-bd2cdd1416fe | -12.57736 | -48.15984 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab6916b2-8bd0-34a3-8273-1af420d299c7 | -11.86848 | -44.95468 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 195fe41f-6be2-39db-9fbe-dee4b0a9fbb6 | -14.86978 | -48.14778 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| def61841-1379-32d3-a828-8e3162ebb084 | -13.33708 | -47.19209 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a82b75f5-16d5-3094-b55b-b7065ee379de | -10.82635 | -47.98583 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dc98947-8b3b-3ba5-bf7f-733af2de959d | -13.28827 | -47.5857 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 21305a9c-8faa-33af-9b2f-7a709efbbb87 | -12.82808 | -48.32967 | 2025-10-05 03:55:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0aa308eb-b672-36b3-9770-24fbbeea0b58 | -13.5842 | -48.16175 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c409b347-cb34-3498-ae09-28361286e213 | -15.98406 | -50.86129 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7c826fa9-365e-34e6-8b06-24803ed5b081 | -14.94966 | -46.84847 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2924a29e-e86f-3bb5-9dff-e20c2219a436 | -11.22592 | -47.74316 | 2025-10-05 03:55:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33eefccf-8bec-3556-8f06-f0c5ae398e9a | -13.72251 | -51.46023 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e26b73ab-5034-3de2-96cb-f315094e5d0e | -13.0764 | -47.89851 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 13771907-2764-3a03-b756-52a18c0d61e8 | -14.6974 | -48.34612 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b97da2a8-3fbd-304f-abf7-b8fe7b31a6cf | -13.35084 | -48.05957 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dd9d25df-2124-38e0-bfe4-8a10cb8e6fd4 | -10.94668 | -47.05087 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2a0cc04-c6d5-303e-89eb-8fb45d5d77f0 | -15.13435 | -45.75985 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 474f0924-2b41-37a8-ae95-6251ee60fcc1 | -10.743 | -47.8933 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09d5a57f-d3d7-3c81-be6c-0b8cd912b97a | -15.23877 | -49.31048 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4dcf2a3c-1466-32b4-86a0-c512940a8551 | -15.936 | -48.99477 | 2025-10-05 03:55:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b374538-3577-3ffc-80af-d532260e4ddc | -13.94132 | -48.18396 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ca1960c-c804-34aa-bd12-7f98229db5b0 | -13.86069 | -43.98935 | 2025-10-05 03:55:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1eaff0b-4805-3d3d-a094-4af85b550f57 | -11.52756 | -47.67857 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0d9852f8-8ec2-3380-998f-ab79e7bd485e | -12.7695 | -48.82237 | 2025-10-05 03:55:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2e82105-027f-3110-9b86-8f440be94d60 | -11.01636 | -46.6972 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08cb5420-e358-346a-8759-df61729447bd | -12.98188 | -46.84015 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb093206-19b8-3554-bcd8-be57061e08f0 | -11.07039 | -47.69342 | 2025-10-05 03:55:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e063993-4d2b-3eb4-bae7-766943c463ab | -13.09919 | -47.83161 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 14fa79ad-2f09-3fee-88cf-096970c5f91d | -12.65313 | -46.98971 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63d1c4fe-16d2-396f-9eaa-f3314ea6e128 | -16.02692 | -50.95025 | 2025-10-05 03:55:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8919f61a-1b1e-3d46-8851-296a9815bbd2 | -15.23457 | -49.31001 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc3ea7c0-0686-3e6e-96d4-3e7ab021c28e | -13.2713 | -47.6221 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a3d62ac-b5af-3b36-854c-3d1aa1122857 | -13.14206 | -47.96289 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 280b0160-23da-319d-9353-351cc63c4a3f | -12.90401 | -47.31799 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1499612-ba66-374f-b990-7504a7b81b3f | -13.71687 | -47.35537 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a312f6c-f6d3-387f-9499-04665d6208fd | -13.12997 | -50.87839 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9fb24e97-a11b-3e34-bfa6-6fc0af5f6257 | -12.41953 | -45.15273 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25685b78-4b04-3db9-a267-92a869066e51 | -12.29339 | -45.35295 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edc0b914-9a5e-31db-8376-6732bf7bafc3 | -14.99361 | -49.98375 | 2025-10-05 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1de95fa2-a44c-33ed-8c2f-4fb32005213b | -11.81368 | -45.07026 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28298d79-b800-3e55-8f9d-2510303e026b | -13.70274 | -47.35334 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e65b038f-285c-3b04-a4cd-b44b5afee679 | -15.20348 | -46.38364 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3aedbbd-949d-3d92-8816-13a27e79ccef | -14.69126 | -48.3515 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca314a4b-212b-3b2d-b9d1-20e001393023 | -11.8336 | -45.0787 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e4135ffe-d929-3b99-a530-e30fcffc22e2 | -15.38707 | -47.94862 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e90a2ea2-7b4e-3c67-adbd-afb1046f4a11 | -12.12078 | -50.90727 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b94c718f-b8f1-35f0-938d-8e811b834769 | -13.48001 | -47.27958 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 284aad67-5608-32ad-af06-5ee498609f56 | -16.35867 | -51.46218 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48def1c4-9dd1-3943-a2f4-a4fcf1a3bff6 | -11.70873 | -44.30227 | 2025-10-05 03:55:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9d0ca42-58ce-3643-b37d-5c93e7643630 | -13.2499 | -47.20737 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ca0f900-f81e-3a72-a56b-615d34c6bcaa | -13.50822 | -47.28379 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 03cb5589-d86c-3cf4-be53-51716e2d624a | -14.33888 | -47.6686 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e77c942-581a-3f96-ac45-0b10e5c1f739 | -11.45718 | -51.51826 | 2025-10-05 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3be72c9a-c68a-3241-903a-0253e16dc3be | -13.30645 | -48.12742 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bebc04c9-b1a4-3824-b72e-2b968b8f4a07 | -14.32959 | -47.66602 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29a7b717-4b45-3c15-8996-5159974e79d7 | -13.26333 | -47.81857 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 112dee7b-5e67-37c0-948c-e8061f702ef6 | -15.98947 | -50.92059 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c842d2a-b892-3d1c-ae5c-158aae3af965 | -13.31791 | -48.07121 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 21f8d03e-a232-3f1c-893a-aa865207657f | -13.74199 | -48.07299 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f4dc492-fbb6-37fe-acc8-14843ba3b674 | -13.52667 | -47.28854 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55ff4db8-5162-32d6-8027-adb34ece4f22 | -13.36072 | -48.06135 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 035352d6-889e-3a65-a848-e1eb22c9071b | -13.68769 | -48.0552 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aea34594-7de8-3095-8052-1484681f0deb | -13.24941 | -48.47631 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 596872ee-135e-33ef-9392-faa1e1bfffdc | -15.3972 | -47.9533 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4c55e8c6-4607-34f1-b040-cbed86e62ba2 | -16.34076 | -47.09264 | 2025-10-05 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5f3c4ce-df45-3084-ab67-8b03ba2584b5 | -12.07642 | -45.15306 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34183f3a-89a4-31ff-acaf-d2e5db8809dc | -14.00846 | -48.21341 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 66cf47f7-3639-386e-a45f-aceb285b5ee0 | -14.66924 | -48.28293 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff96f622-1a0f-351b-a519-e1d5d000641f | -11.86439 | -44.95379 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9cc3a1c-03bb-34ee-a553-582113a5193a | -11.10196 | -47.74353 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a02d92a-15d9-3037-8268-ea386e2945e0 | -15.77583 | -49.0968 | 2025-10-05 03:55:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48b68cbf-2f4f-3cf8-8489-fa68809230fe | -12.60294 | -48.13485 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f56c116b-d8a7-3de9-b8aa-cf6c96265c48 | -14.66779 | -48.30458 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fae27846-b8ff-3e5c-bffa-03d1645f57c2 | -12.60518 | -48.12308 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 230c2b25-ad29-3658-bcd4-2578ffb39cdb | -14.4591 | -46.33857 | 2025-10-05 03:55:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24e6f774-0362-3272-97a2-20cb60fc50e5 | -13.73977 | -47.96759 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f4e0df2-8ea7-3239-97f8-267958a7bd50 | -13.73854 | -51.2647 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15cfc4d3-dc8c-3f4f-956c-48736f759b0f | -15.31735 | -46.30959 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89d7e1dc-a693-351b-a9d4-ce26801f4194 | -13.67721 | -47.72276 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9b73666-b548-3dd0-8712-84cd07b7efb7 | -13.30148 | -47.56857 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cd951aa-7afb-3c56-bb63-2cbdde0cc50a | -13.31681 | -48.07686 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e3ee2fe2-1414-353b-9481-6735a7feb4d3 | -14.92694 | -46.92221 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ee0cea6-228b-374c-9a05-961827169b57 | -11.48184 | -44.97289 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b0f3dfe-6ba2-370f-b0de-6f4e6117e939 | -15.50423 | -46.86238 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1ebe864-accf-31c8-99e9-e6b94116dcf6 | -16.12382 | -53.97979 | 2025-10-05 03:55:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0012bbe9-c697-3db8-8387-9e9821039de1 | -13.29359 | -47.81821 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b460d187-cdcc-39d6-8c63-2f58d5055772 | -14.6827 | -48.26608 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1059ee52-d0b0-33ac-82e7-18bbe234a340 | -15.31175 | -47.32284 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcb55d6f-2d74-3c2a-af9c-6833894866d1 | -15.30296 | -47.95327 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91776e54-b5fc-396b-a0f8-004b975e7a50 | -14.67201 | -48.36256 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4cfb3f7f-af48-39e3-967e-203dcbc7a546 | -10.94183 | -47.07719 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 211f2d33-aefa-3bd4-88cf-bc0fdbe2f8d8 | -11.01728 | -46.6922 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4153bdfe-f7e1-33b3-b5a3-0ccf8c194472 | -14.69012 | -48.30558 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d01a8da3-44e7-3d91-ba68-95007157ded5 | -12.81375 | -46.85494 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9515edf3-714e-3522-a43f-c4bef896493a | -11.70386 | -47.50946 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c682bbd-8219-32da-a7a3-4d9b35fdfe1c | -15.9856 | -50.9229 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f02bcf87-d04e-3797-839c-b0d03ed2621b | -15.23227 | -49.29492 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8472a334-0501-3e1d-adb2-818227e5e1aa | -12.9663 | -50.99817 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c5af04f-0cd0-345a-a661-1c2a078a022e | -15.29146 | -47.33056 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README54.md)
