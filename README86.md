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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87437b75-dacc-3cda-8146-065b1cb53fd5 | -9.91654 | -63.50742 | 2025-09-28 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d24988bc-00e1-3419-ac4c-2eeb1bf63da8 | -13.01313 | -49.45847 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3d4a009e-d70b-381f-8e15-eb9b22390ddf | -13.593 | -47.31513 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fbfcec52-999f-35e8-bffd-9dc950c4d116 | -11.99186 | -47.07977 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e309b2d8-c81f-37f0-8a5d-3d6ec60f9534 | -12.01808 | -63.23088 | 2025-09-28 05:18:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f59ccdf-9dbf-32fa-9450-8ce40134bf42 | -10.04728 | -50.40243 | 2025-09-28 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6700455-dc25-372a-b42e-d183d947515a | -8.62516 | -54.66288 | 2025-09-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 523adf5b-c4b3-3761-89fa-90e2c9271aa1 | -11.52017 | -54.3137 | 2025-09-28 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1eb95a9-23d6-3ae6-8847-cfd2416aa3be | -11.1504 | -54.30507 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83264a13-cb65-3c24-8b78-fe1377432751 | -12.01097 | -47.96834 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 04a9c0a4-ba82-3b4e-be78-5eda18600136 | -13.78948 | -47.91922 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| df3c7308-7f82-39b9-9e57-1335ee2fa9c1 | -12.64872 | -51.66267 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78819a1c-43cf-33fc-955d-b807990afea5 | -13.00527 | -49.45001 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6bec74a5-9110-3ebc-b66a-1134d3d9cc44 | -13.02847 | -49.45979 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 744158f8-759c-3274-9263-c147e82b733f | -12.99935 | -49.44854 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fef91a26-2142-3699-b407-ee5b28224755 | -9.64653 | -64.56651 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 576854ce-51e2-3081-808b-03acaf154dc8 | -13.34916 | -47.30291 | 2025-09-28 05:18:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88c1a71d-7ac3-3f4b-be11-3503ef5d1175 | -9.56486 | -63.20574 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bc19543-ac50-364d-9e25-888e0c3a2412 | -9.98989 | -57.81819 | 2025-09-28 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d220b40-2891-3bea-ab5f-1db2ca88865b | -12.67964 | -46.88284 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 66c0fcf9-6071-391c-964c-d9437c406aac | -11.9782 | -47.07784 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 66d9065a-d997-38b4-a7b5-2eac03dd98b2 | -13.02473 | -49.46357 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d9be9a1f-4155-3ac8-b454-c5b3ec9a3811 | -8.83361 | -45.99619 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8b756639-d5fb-30bc-901a-c83f9ec828bb | -9.76038 | -65.03379 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f0c6ea7-3b5c-3477-bae3-919d51d9ae72 | -10.97488 | -54.10218 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8a5e5a6-12db-3241-a9e6-fc246658980c | -13.71823 | -48.34302 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 336b56ef-fa35-3ff7-bb00-2fb66ad733cf | -9.78111 | -64.98541 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acc30d8a-ca7e-3b1e-89c4-d43883fa02e4 | -9.56496 | -63.20291 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a08f3ebd-455c-3ac1-9d89-e6bc901ba24c | -9.79348 | -47.82027 | 2025-09-28 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 261e2a15-f2ba-3448-99bf-0783e0e51b92 | -10.39258 | -54.26086 | 2025-09-28 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be104925-3eb9-32a4-a03b-ae4e628a3c6c | -9.59858 | -54.57272 | 2025-09-28 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20768069-4e22-3dcf-94e9-6ea3bf3222e1 | -10.45617 | -50.85388 | 2025-09-28 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfbaa3fd-6ff3-3ed8-aed7-d75b2efd89f8 | -9.10871 | -45.87833 | 2025-09-28 05:18:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4f9e5fa-1732-3519-93be-bc191cf05255 | -13.58699 | -47.31082 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 91f1ad02-d30f-33a4-ba04-858760159e8c | -11.94906 | -47.92968 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08ef47f6-dcc9-380b-b20d-ea99dca3d9fb | -9.56122 | -63.20511 | 2025-09-28 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3ab3dc8-0d11-37c5-8837-46b00a2ea716 | -8.93799 | -63.87015 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a36e640d-efd1-3a88-8c15-2163121f7424 | -11.99353 | -47.88837 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d760b425-60ee-36ea-92a2-d6a4687d6145 | -13.77838 | -47.89665 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 993f1aa7-59aa-3ead-a848-67171687b9de | -13.5937 | -47.31338 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 00cd3ff5-0338-3e27-82b1-5173bd89b9ac | -10.42664 | -64.88476 | 2025-09-28 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24db1abb-37f0-3390-bbd3-2ecccf2e3622 | -12.64475 | -51.69419 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fdd33b3-bcf8-31a2-979e-6ee405c4ff48 | -13.78817 | -47.86732 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07ff153c-c3f8-3305-a7e2-894149e10be7 | -9.75634 | -65.03305 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91b770fa-4907-3f39-b1ab-e59a6539ef8d | -10.96564 | -49.56865 | 2025-09-28 05:18:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad62cfd2-ff51-3ebd-9219-b108665978f8 | -11.48764 | -51.44911 | 2025-09-28 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03b32acb-b7b5-3f92-b177-bca2e5ab5b9a | -13.59233 | -47.32138 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9933a93-6620-38b0-b6bf-6b780f696196 | -11.98925 | -47.04054 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 10ce969f-0e51-3eba-9318-e5fbd41d78b8 | -9.64749 | -62.84676 | 2025-09-28 05:18:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 769c92db-55a0-3f1d-bccc-a5f9a0d49e22 | -9.90304 | -49.12019 | 2025-09-28 05:18:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04046d33-dcaf-34af-8808-eb5b87640256 | -12.63036 | -48.15305 | 2025-09-28 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f4ba5d5f-1368-309c-b9d0-30e7a6934b79 | -7.86409 | -63.31598 | 2025-09-28 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c74ea5d2-9fa4-356b-82b4-9b2e854dc95e | -9.91175 | -65.00877 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 333322da-5c34-365d-8cba-a1281fe2cee5 | -13.25184 | -48.45319 | 2025-09-28 05:18:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ba67032e-ded3-3425-9e8c-c0f0ab4ff14a | -13.01273 | -49.4621 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d5abcd30-8a17-3b05-bde0-9337286bf83e | -9.10522 | -45.88153 | 2025-09-28 05:18:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72af5990-8ce3-3c75-aa0d-bbf6678ce00e | -10.85517 | -47.79303 | 2025-09-28 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d9ca702-b469-3930-a774-4c09dc15cbaf | -9.40634 | -54.69549 | 2025-09-28 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32dfdca2-2406-31d7-b62c-44d7a84bfc8e | -10.17794 | -52.57213 | 2025-09-28 05:18:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac488bb6-9516-347d-828b-f6c4eaff058d | -11.9775 | -47.08419 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1f08a7aa-be67-3544-9cb4-7504da856fb3 | -13.62155 | -48.07111 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e846537f-e550-37e3-a49a-8d4f3ccf7a8b | -12.02119 | -47.93574 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a28fca6-bcd3-3520-94ff-0d63ff7d24c9 | -13.39425 | -48.16653 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 169fe5d8-5bae-32f6-920c-86bb42609dd0 | -9.51063 | -54.66423 | 2025-09-28 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8abd6c9-4661-3bf6-a9b7-1533a53be5e3 | -10.95833 | -54.09575 | 2025-09-28 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21b74587-1ee4-328e-9d47-974d0ada347d | -10.39206 | -54.26471 | 2025-09-28 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b42a949-3cc4-3738-90e8-a2d93846229d | -13.35019 | -47.29331 | 2025-09-28 05:18:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f675166-c1db-3ba1-b0c3-46d69233f89f | -9.7894 | -64.96105 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a9662dc-14c0-36a1-9233-d50dfaaedbed | -9.21624 | -46.77145 | 2025-09-28 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| be05b282-c572-30e1-9e30-4893ff885a6a | -9.91146 | -65.00504 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e083d34d-7911-35b4-a10d-0273ab08e701 | -7.86034 | -63.31536 | 2025-09-28 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57bcc8e6-f53b-3732-ae10-6e9ed92c2c83 | -10.82023 | -69.09117 | 2025-09-28 05:18:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf3912fb-1177-371a-8cec-dde4cfa1052c | -9.05362 | -46.73178 | 2025-09-28 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 70eb28e7-878e-37a9-95e2-626dd7e85c5a | -13.71769 | -48.34811 | 2025-09-28 05:18:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fcc23149-2fbb-35b6-8da9-661705a53932 | -9.91086 | -65.00864 | 2025-09-28 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c553c13-3e19-35a6-a2bf-2e6488c8426b | -10.04909 | -65.20478 | 2025-09-28 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0009457-a67b-3d5d-a771-30d90a04adc7 | -12.02185 | -47.93001 | 2025-09-28 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05be98b6-29c1-3e4a-b40e-53c3d84fa9c2 | -9.75593 | -54.93874 | 2025-09-28 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6610cfdb-8da0-3e7c-bdbb-63b0eddb5ce5 | -11.87013 | -56.87421 | 2025-09-28 05:18:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f9e1fbd-e9c1-337c-8912-00916c340211 | -9.10793 | -45.88467 | 2025-09-28 05:18:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 19781a70-f9c8-3383-a3e0-1f41055c261b | -13.785 | -47.89784 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f856574-9af6-3276-b4ca-f769552604d1 | -12.64435 | -51.6974 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e9ec5b9-7682-38dc-844f-53c2cada539f | -12.9871 | -49.44915 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c6927431-76f1-340b-8ce3-f3d7bbade9a2 | -9.1597 | -61.17085 | 2025-09-28 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a93b115-79f2-3ce8-9dba-5568a3b1db16 | -9.41487 | -54.69318 | 2025-09-28 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a5d51d4-cb5c-3a7a-8bcc-2209acf6920c | -8.4842 | -47.80865 | 2025-09-28 05:18:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 971cb8c2-e19b-30f2-8d7a-6a5bb4e7ac9c | -13.6054 | -48.10617 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f8d1d726-ee63-3402-9ce3-d8830207e7d9 | -13.58741 | -47.30676 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 734699e6-31a7-3d14-aad6-c4afa983c54e | -8.86296 | -48.56562 | 2025-09-28 05:18:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7b48eec-b407-394f-a547-96fe140f175b | -11.45772 | -59.1283 | 2025-09-28 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d7354c3-ad71-3f36-981f-ce80fe883644 | -9.67518 | -62.39174 | 2025-09-28 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c52e846-a51a-3c3a-8f88-8b6e79582c0c | -7.86485 | -63.31141 | 2025-09-28 05:18:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e43730cf-f1bd-3baf-964e-6b6a53985ada | -12.68727 | -46.87763 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8d32063d-ae82-316c-a928-4df923b1b086 | -10.04684 | -50.40595 | 2025-09-28 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dcebfe7-8bf2-303b-a638-e619c730c8ed | -9.44838 | -56.65359 | 2025-09-28 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ab1bd8d-42ac-3499-991b-d702f640e497 | -13.01601 | -49.46233 | 2025-09-28 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f646b570-db38-30d4-a702-951e4637af69 | -12.00296 | -47.04234 | 2025-09-28 05:18:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6c42c84b-a14b-3d44-9aa2-5bb5fa0524e6 | -12.894 | -47.10369 | 2025-09-28 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71051e4e-323c-351d-a2c8-3647ea329719 | -13.58636 | -47.31222 | 2025-09-28 05:18:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3dec1ffe-51ac-361c-bc2c-34670754a395 | -12.65907 | -51.66389 | 2025-09-28 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README87.md)
