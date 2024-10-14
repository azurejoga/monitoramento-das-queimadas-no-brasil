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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62b206bb-b580-3dc3-8cf6-df491ef9c876 | -5.11415 | -44.9347 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f21a423d-89c9-34fe-8ad8-4c13787d093f | -5.0571 | -45.14596 | 2024-10-14 04:19:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 241fd557-80bd-3608-ad34-53b416006657 | -5.05655 | -45.14943 | 2024-10-14 04:19:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eec9996a-becb-3150-a807-ecaf64eb6203 | -4.99564 | -45.46982 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b55d0b6b-6c8b-30a1-9c4b-1d6cca89fd44 | -4.97038 | -45.62904 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6620e3de-b93c-38b2-9dd3-a0e932350c5b | -4.9676 | -45.62494 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40e31d26-b1de-35cb-86a1-ccbe596a9702 | -4.96703 | -45.62851 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23cad735-851b-3b02-9fb3-88ed4de5338c | -4.9556 | -45.76548 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87d2ec55-f2a6-3d3e-9e9a-9551adb589f8 | -4.95224 | -45.76493 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9329c1b8-3cba-3c8b-82bf-7c140b940753 | -4.95109 | -45.77216 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf31c318-1b8c-35c3-aeaa-efd23ff96533 | -4.94219 | -44.79794 | 2024-10-14 04:19:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcc4bf7a-9ee3-3668-8160-a51d79e9bd91 | -4.93503 | -44.80038 | 2024-10-14 04:19:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14ea4683-6139-310d-ba6b-16125493087f | -4.91734 | -45.83265 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f9e7f10-a636-3d00-8a36-64a7037651bd | -4.90707 | -46.00542 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d855892d-a1e7-3586-b487-21351ec06db2 | -4.90649 | -46.00908 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d96818fc-6cb4-3a75-94a5-767277f91b2f | -4.90486 | -45.69526 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c77a7dde-e878-31f2-b5bd-1f950f01e644 | -4.9031 | -46.00859 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0fa11c1-6e93-31dc-a90e-21acac9de81e | -4.90251 | -46.01225 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 714c7b60-9fa0-3b3d-a4ea-b789a5ee6666 | -4.88449 | -45.35503 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aaaea9a-c7ad-3688-be34-80c8d191d1b9 | -4.87674 | -45.97826 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ca251ab-5c3f-3216-8bcd-e52049e94db3 | -4.87616 | -45.98187 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b82edf1-0df4-33b2-b0e4-32ec0fa8b9dc | -4.84473 | -45.84344 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fde1937-959c-3156-99ed-8280172cc138 | -4.84415 | -45.84704 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae1c7985-f12b-3df7-be4e-a65202713654 | -4.83907 | -45.85734 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c564940-3b2f-315c-aca4-dd7414fe2da5 | -4.83644 | -45.78698 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b6c4bf8-7466-3ec6-acbd-60a625270a97 | -4.83587 | -45.79055 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b2f0092-8773-3e1e-8210-fe05fd114ef8 | -4.8357 | -45.85683 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 86cf8add-a07d-38b8-bf48-217a83d449d1 | -4.8353 | -45.79412 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 785331ea-1c58-38fd-b074-6769a80e5a21 | -4.83308 | -45.78641 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8280340-dccb-3242-9b72-961867637bab | -4.83251 | -45.78997 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28ee0ba8-5c2f-30b4-a4dd-33cf73e8b1b6 | -4.83195 | -45.79354 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89af7e05-6132-37a3-bec1-597ec90ff2a2 | -4.82916 | -45.7894 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08e656c1-1f6d-3bab-abb6-f95ff04ec898 | -4.8074 | -45.75295 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8536b82-ede9-3a04-9e82-0f4de7fb79cc | -4.80683 | -45.75654 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a348775-f1af-3a34-b55d-05db761d4ade | -4.80347 | -45.75597 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8c79b7f-a631-3e8a-b471-37e788ce3ba3 | -4.78031 | -45.79292 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5431b924-b883-3a62-84c4-5f3a14e0b91e | -4.77973 | -45.79651 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 875cf064-4894-30aa-b0df-ea204a85f594 | -4.72484 | -46.13762 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ccaa637-de48-3d57-971c-ac826c6cb4f4 | -4.72143 | -46.13711 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58f1c5ae-2022-34d9-b39c-5426e6c50c06 | -4.71905 | -46.15184 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e00239e4-0a9d-32a4-a6d7-953bc9a9837c | -4.71846 | -46.1555 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3f06eda9-493a-31fd-9e0a-482629573c7e | -4.71787 | -46.15915 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bdc4932-41ff-30af-a27f-70897663a8a6 | -4.71565 | -46.15128 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 842628bd-5377-3f8c-93a6-20ee0fb3d46c | -4.71506 | -46.15493 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c80b194d-a08b-3371-984c-1aca626965f3 | -4.71486 | -46.1509 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4e1c8ad-dfda-3d44-a2b5-4d65e54d3488 | -4.71428 | -46.15456 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8b16254-5049-35dc-b523-fbf7619b2ca9 | -4.66101 | -45.71503 | 2024-10-14 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9d978bf-e3d8-3cfb-b680-163ae1b4b77c | -4.65764 | -45.71453 | 2024-10-14 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10449ec2-665c-3272-af8e-b452e6cfc42f | -4.65428 | -45.71403 | 2024-10-14 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7ef3cb0-5d27-38d4-8aac-04c24337d983 | -4.65034 | -45.71711 | 2024-10-14 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f9dbf01-ba46-395b-b84c-debea68aeabc | -4.64698 | -45.71661 | 2024-10-14 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e570913a-807e-30b1-bf9e-fdabe104cfaa | -4.64081 | -45.71205 | 2024-10-14 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 531bd2c6-65c8-321b-b296-5798cdfada83 | -4.63561 | -44.86259 | 2024-10-14 04:19:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0aa74cbb-7962-3efc-bafd-1a34032f0d22 | -4.6323 | -44.86208 | 2024-10-14 04:19:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bdd47b13-94b7-343f-9ee5-3ecc4f35150a | -4.629 | -44.86156 | 2024-10-14 04:19:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7718310e-e5ca-3b67-b4c6-eff29977ae25 | -4.62569 | -44.86105 | 2024-10-14 04:19:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4383744-017b-3a33-a8e1-530045ab73fe | -4.62514 | -44.86451 | 2024-10-14 04:19:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1b238f2-1054-3618-b05b-8a085d31b328 | -4.62238 | -44.86054 | 2024-10-14 04:19:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa55cbf6-64fe-32fa-b03c-56b6fb08783a | -4.62222 | -46.07607 | 2024-10-14 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac597b98-b3b3-352b-90ee-cf797e6a2bb0 | -4.58599 | -45.68862 | 2024-10-14 04:19:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0712994c-03dd-385a-b446-977075a452a4 | -4.58541 | -45.69222 | 2024-10-14 04:19:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b93d1698-2c66-36f9-868b-4b778c111f21 | -6.40236 | -45.95437 | 2024-10-14 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c13a5c9-1d56-3bb8-bd35-3bdea0276d60 | -6.3119 | -45.09019 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67025137-7bdd-31b8-a1b2-599d0a78582a | -5.32284 | -45.29543 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02ec02e8-574c-3c6b-858f-6023286ce337 | -5.30627 | -45.22849 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5810ff82-ad54-37c3-8904-fc40bb23fd97 | -5.30344 | -44.96508 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77c44632-9eef-3f3b-b4bf-f89ea6f5d6b9 | -5.30239 | -45.23146 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a131f970-f7d7-3c65-b699-0021f536ae2b | -5.2899 | -45.13694 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3e5ab55-63a0-37f3-aab2-4685fc02c04a | -5.28935 | -45.14042 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97a082a1-9d9e-3aee-a2c8-88a29e011a4c | -5.28373 | -45.60596 | 2024-10-14 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cdda16fa-ac3d-34d8-af83-f596c37c8578 | -5.28317 | -45.6095 | 2024-10-14 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d96116d-f9c0-3515-84bf-774866b101ec | -5.27684 | -45.71391 | 2024-10-14 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e54c4b79-0299-3a5a-a63d-dac912ba7f5b | -5.26109 | -45.51196 | 2024-10-14 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43dca1d4-d454-324d-929c-6f069cefe65f | -5.23964 | -45.11127 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1b5a18d-f097-33c6-982d-d3cc54873476 | -5.23909 | -45.11475 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b5f0445-7fef-3b2a-834c-d2373121cc0f | -5.23633 | -45.11076 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| feeb8f59-e614-3b21-9f5a-0d524cce0bd2 | -5.23578 | -45.11423 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75394e64-6cf7-3bc2-bcfa-79412e948370 | -5.21635 | -45.58104 | 2024-10-14 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32a84641-2d16-3e18-91b1-bea2fd9d2222 | -5.20599 | -44.84993 | 2024-10-14 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e68d48b-97d8-39c7-9d23-60bde167c1ed | -5.16251 | -45.38425 | 2024-10-14 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6b6cfd8b-7c8c-3c6b-bb13-20fc8b1d253d | -5.16196 | -45.38777 | 2024-10-14 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 88830abe-5690-31a8-a687-2d8a96a125b7 | -5.07699 | -45.81749 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0458735c-ca9c-310d-abe8-5a3bab3a9c1e | -5.07185 | -45.87178 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3f80dd02-dbd4-3281-a8e0-621c8ad088c0 | -5.07148 | -45.7653 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2710d22-feb3-3fc5-9768-06092a4000d0 | -5.07128 | -45.87537 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d257544-ed48-3192-b48e-9e264cde6146 | -5.06848 | -45.87125 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 69b0a70c-6784-3ee1-898f-adbf76c4ff3f | -5.06813 | -45.76476 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dae7f686-89ca-3140-95fc-fe7309d2d0f2 | -5.06791 | -45.87484 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7be8b9b9-a31c-3ef3-aa05-76968942a951 | -5.06756 | -45.76835 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dcb05f2-8599-3a02-ae8d-a5bb91d95bdf | -5.36536 | -46.05898 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acc52640-38b8-3f84-9bf6-181d6e513c08 | -5.35839 | -46.12482 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2eb1623c-0d1c-31a9-a302-bfe3ed6eba1b | -5.29715 | -46.3785 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2504a63-713e-3854-9961-f844f4a96c83 | -5.29374 | -46.37797 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffdb71b2-3875-3034-8711-b19d20fa4dce | -5.29315 | -46.38165 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dedef6aa-1da4-3b1a-9662-392f8ffcad02 | -5.29044 | -46.35477 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6816dbab-83a1-3d3a-82d0-4d38f07485b3 | -5.28704 | -46.35419 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6bb733a-c23a-3f77-a6bd-3acc4ea0df70 | -5.28644 | -46.35791 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 812a7f7c-6313-3e62-b4d0-639f77f62da6 | -5.28585 | -46.36162 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0aa86bf-a040-3e80-9e1a-959506aa0fc0 | -5.28304 | -46.35733 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e14762d-f74c-3854-97f1-24c8a018f3a8 | -5.28185 | -46.36475 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README44.md)
