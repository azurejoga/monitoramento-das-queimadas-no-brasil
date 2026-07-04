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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c95b8cf-e15a-3559-b13c-97cd0396b19a | -6.88659 | -43.66285 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73470b4a-00b5-3523-93d7-07b41efad0aa | -8.75646 | -47.40437 | 2026-07-04 04:00:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd39dfe8-9f99-33ca-b834-2c698f2e85eb | -7.00447 | -42.76562 | 2026-07-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c47cb689-0a06-3b9b-99c9-c43268c0176a | -12.76404 | -44.53654 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ec910624-7175-3791-a793-7507f7cb7ab2 | -12.74071 | -44.53217 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f19344e4-bd59-394c-8a18-bb514cfab772 | -12.76191 | -44.52575 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c1e9481a-e865-35ed-bc8d-c93a0d7cb9a9 | -12.75238 | -44.53433 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| cae46c60-70aa-33c3-a85a-8b52ced09149 | -11.45177 | -46.55109 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef891ced-5b70-3a06-aa80-f6a543f7c7d8 | -10.92586 | -43.04785 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| cd5d2ea6-a777-32c2-8c24-fa01ca69cb10 | -6.66829 | -47.91406 | 2026-07-04 04:00:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9aa43b09-9645-3aea-8f8a-c7ab7ff83ad4 | -7.51189 | -49.5256 | 2026-07-04 04:00:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e83768ac-ee98-362a-a4fe-12d3daf5fd0f | -12.74496 | -44.55375 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 115a1bca-a58d-3d48-a5e6-cece57548995 | -12.75275 | -44.55515 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 52883b20-bcbc-31cf-9429-5c0aac19c77f | -12.32015 | -46.73833 | 2026-07-04 04:00:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01d0653c-8892-3983-bb92-00b9f8e43906 | -7.73538 | -44.17588 | 2026-07-04 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4f1c035-f1d3-3315-837b-35be8d2a5e9d | -7.7401 | -44.17303 | 2026-07-04 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fd7c6c7-7a58-3406-abad-9e44cc32e1c0 | -12.75928 | -44.54081 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 06533fb4-1ac6-3eab-b6d4-cd5d05d636ce | -12.7446 | -44.53289 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cd090029-630d-36fc-9045-328a910f434b | -8.45 | -51.56975 | 2026-07-04 04:00:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7764eab-0985-3b6c-800e-973845bbd478 | -10.97919 | -43.70948 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57369b38-e67b-3b47-9857-8a9db15f278e | -8.72544 | -47.84116 | 2026-07-04 04:00:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c164176c-5cbb-389f-bfc9-f52fb2df1aab | -8.07957 | -47.15889 | 2026-07-04 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be85f9eb-178c-3158-b94b-f3d9aef28890 | -6.8872 | -43.65928 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c65403a-b970-3cfd-99d6-861020bb59d2 | -6.92787 | -43.71388 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a75d5f0b-0c75-36e1-80a5-8c62f5c15303 | -12.75978 | -44.51495 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9619954-67c7-347f-b29a-932d7c731f1f | -12.74372 | -44.53792 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cf8e960c-41fa-392b-9a12-a60b274a036e | -12.76444 | -44.55731 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c79322db-9945-3a67-b83d-ae5f9bb97bd2 | -12.76833 | -44.55804 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48cdcb08-4af6-3b77-8cb3-e000cddd867b | -7.00829 | -42.78363 | 2026-07-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7c214d57-60d7-3e81-b935-59fd62367b50 | -12.75187 | -44.5602 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0455cc8-e961-3b19-921e-920c1486d8b7 | -6.8157 | -44.15229 | 2026-07-04 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 583b4536-1150-398c-a315-7327eacd1940 | -12.3486 | -47.90289 | 2026-07-04 04:00:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae6b4813-f618-3e54-bbd8-87b954825668 | -6.93251 | -43.71102 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c400683-2e70-31f4-baea-6fcd8709a250 | -12.35903 | -47.42561 | 2026-07-04 04:00:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| add45456-e9dc-3ccf-829e-9de9cdabc744 | -12.74708 | -44.56456 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b22390a-46c2-34e8-94ed-0f83b7e773b4 | -7.90458 | -48.24919 | 2026-07-04 04:00:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e36667f-79df-3b9d-8b1b-812160fc1dac | -6.89831 | -43.71626 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 76c26269-b97c-39fd-8ba9-42fc86d3edf4 | -9.04591 | -47.74402 | 2026-07-04 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22e7583e-b0ca-3f68-9b64-a9f4c905b9c4 | -12.75502 | -44.51927 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1f891724-6290-3378-b3f7-c9ac78223802 | -7.73251 | -44.16775 | 2026-07-04 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00d4f95b-c0f2-3434-ba3b-25c59a53d1d4 | -7.00309 | -42.76815 | 2026-07-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ffd6a8e3-e53a-3b45-b5f5-7382a9e9641f | -6.87987 | -43.70224 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8fc0326-d72d-3492-b640-9f0889f7e413 | -7.00609 | -42.77351 | 2026-07-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6985f924-9bfc-3f86-afd5-4936f89bce8f | -12.75878 | -44.56668 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f47ddc9-8365-3c41-b12a-ceb3c0274c9e | -11.3786 | -47.81553 | 2026-07-04 04:00:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5aa7df8f-ef97-3430-af9b-55f483ca913e | -11.45632 | -46.55182 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3790acbb-8c88-341d-8850-498e05a5f7dd | -11.45457 | -46.56166 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2230581-465b-314d-b32b-1fb3c92db50f | -7.73189 | -44.17143 | 2026-07-04 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1561c0a5-4772-31e1-b918-600b34430515 | -7.73662 | -44.16851 | 2026-07-04 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2564dd10-a9bc-33cd-a70e-ceac13c893c3 | -7.73601 | -44.17216 | 2026-07-04 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19cf6b6f-63e7-3fcc-bf4b-24421a234663 | -8.08451 | -47.16025 | 2026-07-04 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7802a58-d9f8-31e7-aaeb-92a780f38f7d | -12.74797 | -44.5595 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5de9411e-540a-3ef0-a119-a8989f18a627 | -11.50863 | -47.41171 | 2026-07-04 04:00:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8af2f73-5408-3830-ae97-9c7408c53567 | -8.03437 | -46.2364 | 2026-07-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8e3a1084-a8a3-3742-a4a4-f673c522af40 | -7.89852 | -48.25173 | 2026-07-04 04:00:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fecd6fd-b825-3331-97e0-f5e09a76b588 | -7.009 | -42.78588 | 2026-07-04 04:00:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d7572b0b-1ee5-3648-b342-95138ff10b04 | -6.88315 | -43.65865 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1502e2d-94b9-3902-8432-d50679aa8122 | -11.42416 | -46.57431 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 373f041c-d9e7-368d-aa59-6f819d6f7aeb | -12.74849 | -44.53361 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 73cc9f11-538c-3b82-b722-5523d9aa3386 | -12.76103 | -44.53078 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| abbb1e6a-db43-30a7-87d9-d1c9b51ab073 | -11.43854 | -46.5726 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d65512e0-0cdb-3e4f-bea5-463a9034e3b9 | -12.76317 | -44.54154 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 53b5c3cc-a2fe-32b9-bf76-e78924bc2bb5 | -10.92804 | -43.05729 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 62b985a0-c69f-33d7-8080-53efcf9cde2b | -10.92511 | -43.05224 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 83cff1e0-ba45-3884-afcc-fa5e391ff3a8 | -11.43938 | -46.56792 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f5afe4b-f6a5-3a78-ad64-758e17b430af | -12.75326 | -44.52932 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 774c8333-c002-3357-8494-09bd946c99ec | -7.80182 | -45.22199 | 2026-07-04 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31e9d7ea-d7b7-3588-983d-74af9e92cdd5 | -6.93537 | -43.71888 | 2026-07-04 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5f4956b-b76d-39f3-95c4-4d51e1855cd5 | -11.92205 | -43.38682 | 2026-07-04 04:00:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f907bddf-ba8a-317f-845c-523cdfde0739 | -11.5076 | -47.41288 | 2026-07-04 04:00:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56c3e691-2bef-3114-ac87-a962bc0fce0c | -12.75539 | -44.54007 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| b5aa55b7-a6cc-3ce1-a0a1-75527a6f420b | -10.92736 | -43.03906 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a2396a72-e530-38dd-b6c7-f06d762d6374 | -12.75451 | -44.54508 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 8009550e-110e-3a80-a1f8-6ff304439b51 | -9.44212 | -40.32857 | 2026-07-04 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 1e08949e-a653-3b0e-a102-c76763b5fa30 | -11.4233 | -46.57904 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ff7a1d5e-a92c-39b0-8cf8-d4675e574a92 | -8.72104 | -47.84175 | 2026-07-04 04:00:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3e587e6-bb27-3f9c-8e46-9dc73714cf64 | -11.43405 | -46.57149 | 2026-07-04 04:00:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31b8745e-951b-388c-8484-73c446e85c2d | -12.73983 | -44.5372 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ebcf285-9fe9-39ce-97d5-5511d4dbe2ed | -9.5675 | -49.11211 | 2026-07-04 04:00:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16c71d2a-8c78-3b2e-8a4b-e29d8704c92c | -12.7692 | -44.55303 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec74e7ae-474a-3041-9bec-e0fa4aa7ecec | -12.74584 | -44.5487 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5ddf104-f0ed-3592-b38b-6619145efa4d | -6.66484 | -47.91311 | 2026-07-04 04:00:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09ac9230-e063-3087-afe1-908baf09416c | -8.76567 | -37.16542 | 2026-07-04 04:00:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 26a0ab35-3425-3a1b-a65a-cd1e9dbd1754 | -12.76142 | -44.55156 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f2f4c48-c71f-38a4-8938-ef05f226b599 | -9.28083 | -40.46105 | 2026-07-04 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8b43f341-5cde-36bd-9e3e-1c9064eb8f49 | -12.75627 | -44.53506 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8d41cada-27c3-3e92-9774-b0a7f9feb5ed | -10.97959 | -43.71251 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d26c0eda-d2d3-3dd8-93d1-3a94864dd4af | -8.4483 | -51.56887 | 2026-07-04 04:00:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24331750-fee7-3af4-9e67-d33f4405b244 | -12.76054 | -44.55658 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a249d5f3-040e-32f2-9384-33e358b77977 | -12.73682 | -44.53145 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7046b550-002b-32ba-ad4a-fb6dbb9185f7 | -10.94421 | -43.05109 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cf2c0fc-facf-39ec-9f8c-83ab1d353ec3 | -10.92878 | -43.05289 | 2026-07-04 04:00:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c85a0d0c-6c79-352c-be90-c504f595ab8b | -12.75753 | -44.55083 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48584aaf-70bf-3309-92bc-eb467b3e21f6 | -9.04079 | -47.7431 | 2026-07-04 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5eb7419-6803-342c-8c1b-5a3eb39634b0 | -12.75665 | -44.55587 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c5d11c6-f381-3d60-9bf5-49e31a4bd8d0 | -7.84254 | -40.06551 | 2026-07-04 04:00:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 6d14a69b-046e-3f3c-8abe-72865a851f02 | -8.03345 | -46.24177 | 2026-07-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ad1495b5-7ef1-3aee-9fa3-36d69048f836 | -12.7589 | -44.52 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 45cf4f74-7297-310e-8adb-f49ec5df0e82 | -12.73593 | -44.5365 | 2026-07-04 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59cba994-addd-3b11-b0c0-990b3e796ba6 | -11.92127 | -43.39127 | 2026-07-04 04:00:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README10.md)
