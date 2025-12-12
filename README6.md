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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8659f17-e2d3-366f-9530-886e856bec44 | -2.148 | -45.645901 | 2025-12-12 00:55:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a319379-ab0e-3eb4-a3cd-9a5b2355c982 | -3.2358 | -47.462002 | 2025-12-12 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cf4f1f7-af6d-3162-860e-1d12a2291d79 | -3.6302 | -45.369099 | 2025-12-12 00:55:00 | METOP-C | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c1c2177-34f8-3b99-9bd2-1fefe1892b98 | -23.304199 | -45.637798 | 2025-12-12 00:55:00 | METOP-C | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0558ffe1-308e-32fb-beff-82101acd11cc | -12.4233 | -58.016201 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b619dc8b-7129-3e00-9023-049016a1786e | -12.419 | -58.044998 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 315ad79d-c3cc-39cd-83b9-5f63b683ae17 | -3.6205 | -45.371399 | 2025-12-12 00:55:00 | METOP-C | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 00963940-e6d6-3d98-aedb-b6d45e8ebaf1 | -2.2167 | -45.3745 | 2025-12-12 00:55:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fca5da95-03bc-32da-a9c8-fe52f315cf67 | -3.4767 | -50.8634 | 2025-12-12 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3cd147-43c3-32f4-9ba9-b79af09c57a7 | -4.3442 | -45.7752 | 2025-12-12 00:55:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b349b278-5260-36eb-bb69-c86ab04232fb | -2.2111 | -45.394299 | 2025-12-12 00:55:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d39b711f-2b41-3145-adb9-feb37598f082 | -3.6261 | -45.352299 | 2025-12-12 00:55:00 | METOP-C | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ed4c114-1bce-3395-9a37-818b72495888 | -4.3405 | -45.759899 | 2025-12-12 00:55:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 54deb9b5-91e1-38fb-80b6-ed9bc9c9426a | -6.1184 | -41.278599 | 2025-12-12 00:55:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ba8f1561-4563-399a-9f10-8524d95721da | -12.4358 | -58.027599 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bca36cda-2605-3b9f-b2b9-1cae249291ef | -12.426 | -58.029598 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6a2ad833-49df-3221-91dd-acd852695944 | -3.6693 | -45.787899 | 2025-12-12 00:55:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2775d49c-036a-34f3-b955-c73d3a35b736 | -2.225 | -45.409698 | 2025-12-12 00:55:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08e9daf5-a1f6-346d-90d2-099ecf212a5c | -3.8707 | -50.9604 | 2025-12-12 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe27cb43-514b-345d-b9ac-7c173aeed8a4 | -3.0754 | -45.793999 | 2025-12-12 00:55:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb9ab5d2-887a-3168-afc4-cc4a96147842 | -6.1205 | -41.246799 | 2025-12-12 00:55:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| debbc0fb-27f6-3a6c-99b5-8905e6e28685 | -6.1109 | -41.249298 | 2025-12-12 00:55:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ea5218f2-e12a-3e2f-b71d-7cf107e69bac | -4.7427 | -49.789799 | 2025-12-12 00:55:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 841003df-cbd2-3c88-acda-ed567a36d4f9 | -12.4287 | -58.042999 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9aa187b3-481b-3742-b913-713818acff55 | -12.4109 | -58.004799 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e2a0dd7-4b92-3baa-932b-0a094bd1f74b | -2.2306 | -45.389801 | 2025-12-12 00:55:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f263311-f49a-3d00-8caf-0830350e0928 | -3.237 | -42.0802 | 2025-12-12 01:00:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 8e09b1d1-de85-341d-840d-7fc9d36552ce | -3.6479 | -45.387 | 2025-12-12 01:00:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 90.6 |
| a87d2ca2-364d-31b5-8b85-78b6bddfddb1 | -6.1308 | -41.2633 | 2025-12-12 01:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| b0c8f29d-8124-3ea9-b049-634669cbd84c | -3.0696 | -45.7917 | 2025-12-12 01:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 118.6 |
| b9e45ddb-93f9-3e9f-ac38-edb371da08df | -8.0324 | -43.1022 | 2025-12-12 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| b97a5ecd-5c3c-368c-a1d7-cb3e1d94f021 | -3.2371 | -42.0565 | 2025-12-12 01:00:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 7f458786-85ad-36ac-9912-52eb709877f5 | -12.3943 | -58.0506 | 2025-12-12 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 1aa6cc2c-4108-33da-b3c3-9b2b748b4ada | -2.4923 | -51.8027 | 2025-12-12 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 49e95607-e99f-3119-bbc0-1ad7bbac49c7 | -8.0327 | -43.0786 | 2025-12-12 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 1807f481-92c5-3d92-a346-9d47bf8d7f15 | -12.3946 | -58.0307 | 2025-12-12 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 29281689-f30c-3c70-b5e6-3c81eac5b4ec | -3.6107 | -45.3887 | 2025-12-12 01:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 107.3 |
| bce6271f-730f-3cb0-b24d-bd8f7d581dda | -4.7263 | -43.0588 | 2025-12-12 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| a90952b9-0f06-3483-9fd2-9bbf6f7dcd28 | -6.1306 | -41.2875 | 2025-12-12 01:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 5786d5f9-8a4b-3356-a9c9-0123fce0f6c1 | -3.9511 | -41.5186 | 2025-12-12 01:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| a70c386e-6b8e-39e8-814f-acc2d89ed2b6 | -4.745 | -43.0576 | 2025-12-12 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| cf09ec6f-2a84-3327-9fdb-655f076d8cd3 | -2.2356 | -45.3929 | 2025-12-12 01:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 5ad4e89b-7514-3ffe-9bb4-574782a36734 | -4.7448 | -43.081 | 2025-12-12 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 5a547081-f419-354e-b185-e74c1b7878b1 | -12.4133 | -58.049 | 2025-12-12 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 242.3 |
| 487871b3-068c-3cff-b14e-69dd1ac886ca | -2.487 | -47.7692 | 2025-12-12 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 612d7121-2203-3318-bc49-1875ad07b205 | -4.334 | -45.78 | 2025-12-12 01:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 229f09d0-d36f-3cd3-bcc4-0529021752cd | -2.2355 | -45.4154 | 2025-12-12 01:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| b451cd9d-6132-33c8-8033-b6ba4d1b7529 | -2.4183 | -51.9278 | 2025-12-12 01:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 6f6ef743-25d4-37f4-92d6-22c98479e5cd | -8.0513 | -43.1001 | 2025-12-12 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 7e5a88ef-d3f8-3fcb-b605-8d14d2a3ffa1 | -12.4323 | -58.0475 | 2025-12-12 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 04cbff2c-7a37-33a0-883f-60bd873762ce | -10.119 | -36.4956 | 2025-12-12 01:00:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 86.7 |
| 9f935be0-5bd4-3e8a-8ab5-b8d4df02cc78 | -12.4325 | -58.0276 | 2025-12-12 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 9f92652c-490a-396d-ab04-93695e12f760 | -2.4367 | -51.9274 | 2025-12-12 01:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8c04d2fd-3481-3869-ac8e-f5ba051d7405 | -3.6292 | -45.4103 | 2025-12-12 01:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 233.3 |
| 5840e35d-a876-359c-9e24-d6c74b289259 | -3.6106 | -45.4112 | 2025-12-12 01:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 03ed99f9-4856-3e92-b283-6e5e1bdf2683 | -6.1117 | -41.2892 | 2025-12-12 01:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 41ff9f0f-27ec-393b-9967-bd811e4c9ad6 | -3.6294 | -45.3653 | 2025-12-12 01:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 5e45cef2-31b1-37d7-8a14-a2041963d38a | -2.217 | -45.3935 | 2025-12-12 01:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b01a2c75-c12f-396d-a72b-702511fe5de5 | -3.0511 | -45.7924 | 2025-12-12 01:00:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 98.6 |
| ba9a6b8a-cc4b-3afe-a178-a8433882c483 | -3.6293 | -45.3878 | 2025-12-12 01:00:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 562.5 |
| 12cac54f-919d-363c-bd04-88ed939106e8 | -8.0135 | -43.1042 | 2025-12-12 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| f46a9fe2-c8af-3141-9459-218555a2a071 | -4.3856 | -43.6381 | 2025-12-12 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| fa75992c-63ad-3dcb-ab78-4a3c125f41ff | -2.5108 | -51.8023 | 2025-12-12 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 8d3aca62-bedf-395f-98fb-a822d8963b65 | -12.4135 | -58.0292 | 2025-12-12 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 280.8 |
| a20f0182-bf0e-3ebe-be5a-3e603b885026 | -4.7261 | -43.0822 | 2025-12-12 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 3dee28de-adbc-3001-8c1e-8a73d0b57da5 | -2.4183 | -51.9484 | 2025-12-12 01:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 11073790-935b-373b-ab5d-ee4a13714043 | -2.2169 | -45.4159 | 2025-12-12 01:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 8a0d5b7a-5a6d-3697-ad5d-99e4ee14807d | -8.0324 | -43.1022 | 2025-12-12 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 245.7 |
| 64876481-f84d-3824-8159-f965a71766b4 | -12.4135 | -58.0292 | 2025-12-12 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 273.6 |
| eaae4abc-3342-394f-b3d8-af925036ebb8 | -12.4133 | -58.049 | 2025-12-12 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 230.4 |
| 11f1abf7-d4cd-3a9b-8645-6c27d1fdfc81 | -9.6598 | -36.361 | 2025-12-12 01:10:00 | GOES-19 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 91.3 |
| a070a76c-7dd9-3462-a28a-bbd85a9da5d7 | -3.9511 | -41.5186 | 2025-12-12 01:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 8083f83a-bfc6-34df-8079-f7bb4558ae93 | -12.3943 | -58.0506 | 2025-12-12 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 2799a05d-e950-3a4d-b2ce-4b3dca994071 | -3.0696 | -45.7917 | 2025-12-12 01:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 116.0 |
| f324b1a2-dee7-39ec-9fbb-67a0c7e011a6 | -3.0695 | -45.814 | 2025-12-12 01:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b9fbd486-a438-3a58-9029-7281ab27ee48 | -8.0327 | -43.0786 | 2025-12-12 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 8fb5601b-9d5d-369c-b2bd-0d4e2fe7eac4 | -3.0511 | -45.7924 | 2025-12-12 01:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| c71c8a9f-372a-3adf-b207-038a1baf8662 | -12.3946 | -58.0307 | 2025-12-12 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 134.9 |
| e35e6fd1-d62f-3f9a-bd97-659265d00576 | -3.6293 | -45.3878 | 2025-12-12 01:10:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 12a3e9d0-3c85-31cc-a8b2-62d03df2431f | -2.4183 | -51.9278 | 2025-12-12 01:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 4e696576-1baf-3d0d-b32d-067c17cc254e | -2.4367 | -51.9274 | 2025-12-12 01:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| a54dae6c-c5fe-3330-935f-046da6b90d16 | -3.237 | -42.0802 | 2025-12-12 01:10:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 4b476ea4-98eb-372d-9c74-94b3ddf3a1f4 | -12.4323 | -58.0475 | 2025-12-12 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 138.0 |
| f1ebc5a5-8d0b-3d0a-b4d4-b023e69403df | -2.487 | -47.7692 | 2025-12-12 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 9e344724-e7cf-36ad-86a9-ce7c612d155b | -4.3856 | -43.6381 | 2025-12-12 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a4b5d3c9-fd35-3a92-ba7a-39f4d1018548 | -2.217 | -45.3935 | 2025-12-12 01:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7f8b0eee-2ceb-32e6-a6b4-dc2c9ddd9d6d | -8.0513 | -43.1001 | 2025-12-12 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 067d65fd-6653-30bc-ad2d-a22564ad1686 | -3.9699 | -41.5176 | 2025-12-12 01:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 66077c1e-70ff-30ce-9be5-51361ee1b942 | -12.4325 | -58.0276 | 2025-12-12 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 164.3 |
| cafffcf2-d1bc-3168-b691-d4b6bde217f0 | -6.1306 | -41.2875 | 2025-12-12 01:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 7ebc4f5d-f4e0-32c7-8270-f0a740069984 | -3.6479 | -45.387 | 2025-12-12 01:20:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 97db2953-0e21-3350-8885-090480a90c18 | -3.6293 | -45.3878 | 2025-12-12 01:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 7caa44e9-b9ca-362f-8784-e5d9fed55125 | -12.3943 | -58.0506 | 2025-12-12 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d1a78f3e-d650-32f0-aac4-d339b2a21bc3 | -3.0695 | -45.814 | 2025-12-12 01:20:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c14a061e-8ed0-3d9c-b54e-009a759df621 | -8.0513 | -43.1001 | 2025-12-12 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.8 |
| d163c069-1537-3f0a-81a6-5f6e435a50d5 | -12.4325 | -58.0276 | 2025-12-12 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 138bf156-7a48-3d82-b9a5-4dffd2a7d104 | -3.237 | -42.0802 | 2025-12-12 01:20:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 37ed7724-7553-3e43-94b5-e891374afa8f | -8.0324 | -43.1022 | 2025-12-12 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 202.3 |
| 9984c80d-8531-3ba5-8d45-cd0c3e342779 | -12.4133 | -58.049 | 2025-12-12 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 196.3 |
| 22fe2993-dc23-3692-a91d-ffdb41384978 | -2.1018 | -53.4223 | 2025-12-12 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |


[Clique aqui para ver as próximas entradas](README7.md)
