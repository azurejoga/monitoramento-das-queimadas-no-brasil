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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d131139-bdcf-3874-b976-dd230eb2653d | -5.79384 | -59.22493 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb709e79-2b70-376c-b2f0-cb1ccfc0074a | -10.63412 | -51.61702 | 2025-08-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c03d767-5969-3cea-a89b-1bc84288230c | -9.16686 | -59.59672 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17ed5a44-da85-393f-aa3f-0b7f3a4f8aab | -9.32875 | -48.26439 | 2025-08-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb682fbe-2d53-393f-a373-f023502b8f80 | -5.80166 | -59.2162 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ceae64ec-e82f-3be6-ac5c-12747416c0a5 | -13.41241 | -51.79609 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b08a3ccf-0afa-3464-b8eb-830df38c3f0c | -10.76395 | -48.26099 | 2025-08-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fcea1f9-b228-3bb7-a4fd-fb4d4a134a7b | -6.98155 | -44.43001 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18946cea-2402-3626-a45a-1975ff04fc46 | -12.99733 | -45.22525 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 62da0482-5c68-3998-8623-b7252f127e92 | -13.03567 | -45.23088 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74264708-c0f2-3644-ac70-a12faa227900 | -13.62748 | -48.16557 | 2025-08-24 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90d574d6-95fe-366a-8f63-0a8982b5b70a | -8.53837 | -48.8401 | 2025-08-24 04:34:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6daee26-7cd4-347a-9835-2a51de2a4978 | -11.51153 | -51.86888 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 294574be-cf1b-3614-8c1e-5f50082ec3a1 | -9.17098 | -59.59515 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bb38457-52dd-3adc-a60a-82d13eff9fb2 | -11.10764 | -44.76083 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ea895c9-b52d-3cd2-a3f8-4cad7a9fd3bd | -9.19921 | -59.47962 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c218948e-fd89-3638-8344-f0bebd41cf03 | -9.81966 | -46.42658 | 2025-08-24 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8759b718-d0ed-3a0d-ae5a-520eec656508 | -12.72618 | -48.13884 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5c66cc4-20f2-38a0-b605-222a3a86ee17 | -11.54231 | -51.85765 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6157f63-23a2-3c8c-821c-5fa36c56f379 | -9.11684 | -45.18645 | 2025-08-24 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6b4aaed-0828-3297-b689-6aa27faa507b | -7.59264 | -45.24941 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea4cbf1c-8e00-38ea-a15e-c7895431ae26 | -8.75678 | -46.73791 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58168d9f-d73b-3a13-a665-e50f569de6be | -7.70273 | -42.12754 | 2025-08-24 04:34:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f4ff3e1e-ca25-3a8b-b3c2-fa5f56a6d2ab | -9.17164 | -59.47212 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 807c8104-1c31-386a-8bf4-98a7eb2c2937 | -13.35805 | -47.50119 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c83aac55-6227-3f5d-8e62-70d9e60ce4a5 | -6.61112 | -48.04977 | 2025-08-24 04:34:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5209a93e-e6c6-398a-8296-40a668334094 | -9.51195 | -60.51605 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf348afd-7a7e-348b-bbd0-8ad3b1b6cee2 | -13.46213 | -47.0206 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cc2811f-4698-3c51-80b5-45908bb68f22 | -10.29679 | -46.74868 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f2fc986-cb50-308f-97ff-ce0f39dff359 | -11.5301 | -51.90912 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7dbbb53-a445-3625-85df-abd53b4ccc0a | -13.46391 | -44.0756 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 10f6bf1c-a5a4-3863-b2f8-72afb40b6b9b | -8.06174 | -47.31322 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03cbbcf9-0773-374d-80ef-2cdf40240113 | -8.76816 | -46.75491 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0386aaf4-afe9-390d-98c2-51df2739a57f | -8.71666 | -51.13594 | 2025-08-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b68dd80f-4e8b-39fb-ac58-c2edcf213a86 | -12.72443 | -48.10503 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5eb7a965-9495-3ac7-9ac3-593424da1762 | -9.16987 | -59.47411 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 574cefb9-6ff4-3cdd-889b-56c131a12a3b | -13.051 | -45.23317 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6edc993c-20f6-3bf1-8e79-c26db70d288b | -13.05031 | -45.23801 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40a1ebec-9848-3ea4-9cdf-9b5abbeb129f | -8.22346 | -45.10963 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50f7bff3-883e-3ff4-8dca-8d7ce1190304 | -11.53463 | -51.8604 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 00486718-7fdc-34a1-9115-08ffafc0fa8b | -9.16228 | -59.45715 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 26c9d266-d607-377a-9b26-be2e48cc8fdf | -9.03323 | -47.646 | 2025-08-24 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b919bb62-4028-336c-b326-00567a3975a4 | -8.76404 | -49.97314 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3ef3e78-7d32-3499-8a51-5acab675b141 | -8.90705 | -62.44099 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e438daa1-411f-35be-807f-ec264f0df733 | -10.41625 | -47.19216 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 728bca54-02ab-35b6-ae00-cb54e8c6c067 | -8.76511 | -49.98814 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 532e624c-2c3d-32f4-86ea-eae90e833e57 | -8.74482 | -46.72468 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cde94e6a-b3a1-395e-9b31-0180820567fd | -8.20554 | -44.42976 | 2025-08-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| caf6ffbb-4660-3cad-9095-1e21beb363ce | -10.28301 | -46.74644 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d0806b5-28fa-355c-9e7a-b877b423c1b3 | -11.54032 | -51.86958 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 120c07d3-f4cc-3e0c-8282-f0f193b81147 | -7.62375 | -45.23759 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d2c8b7d-426b-348b-ad2b-e9defc9692fe | -12.17969 | -47.20515 | 2025-08-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d8e1ead-e0f3-303e-a845-4a3684899357 | -6.4661 | -53.40098 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a865dc4-2a01-3446-ada1-81cef1fdb106 | -10.41222 | -47.17257 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6c15e6eb-cd7f-3922-b4a0-961b1c3f3cd0 | -6.43689 | -53.38012 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a3b1b1a-52a4-3e7f-9d13-4ae39fdc10fd | -9.95184 | -60.18221 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88347760-08c6-3bab-a2cb-9f18436599c8 | -8.83966 | -49.90014 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e60217c-b964-3df5-ad8b-10cd77be432a | -7.60928 | -46.25802 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3135c611-6fc2-3876-af5e-95caccf712c8 | -13.4762 | -47.02254 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb371894-9e18-3113-b2a1-1bf6c4cd2943 | -11.33585 | -47.85328 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26224cc0-acf3-35fb-b0b2-0346028c0f25 | -8.74526 | -45.45172 | 2025-08-24 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca7fb4ab-ae31-3c92-82cf-331546056232 | -11.5338 | -51.84379 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 266eced6-88ae-3d31-8463-bc88b0b70de0 | -11.18259 | -55.02364 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57792c6a-2246-3cb5-b5c4-a1c85ac92547 | -8.09338 | -46.30263 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 609ec4bb-0a36-3f84-8326-f8780cd34166 | -7.67164 | -46.24059 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a8c4880-707a-3c83-b8bc-a4b4c56bd0a7 | -13.33093 | -43.1951 | 2025-08-24 04:34:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5039540c-e72c-3f46-9061-cf437cffc76b | -7.63046 | -46.28067 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 98e79ec3-db50-3490-97e6-fef61c89999b | -8.48471 | -49.39439 | 2025-08-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f37f8b2d-db5d-36f8-b238-48d125ca2d40 | -11.32911 | -47.85238 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 428b76ba-4ef2-33c0-a050-f756cfca1edf | -11.67341 | -51.59626 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e63dcd0-8537-3ad8-a630-233d03512f17 | -9.15507 | -59.49577 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1d4d78a1-fe39-3b7d-a06b-c7e84f5e33ac | -6.46262 | -53.39664 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e8f640f-13ec-3a22-9693-beae37969b91 | -11.73223 | -51.69428 | 2025-08-24 04:34:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 730f2277-aa67-3e0e-841e-191bb0f2bf6a | -10.48198 | -46.86881 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f294ea3-09c5-3665-b199-900be3e5bab4 | -13.03499 | -45.23571 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79984b88-74c0-3855-bdc3-e26cf8171e9b | -11.5087 | -51.86423 | 2025-08-24 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0227bdf2-c50b-3e9d-b6c7-2ec0ad1fd729 | -11.18538 | -55.03236 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f32fa4c-4c1b-3ac4-a8b6-9dffd1dd5830 | -8.71316 | -51.13535 | 2025-08-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ca32ca1-9e81-3061-842a-81a72de7b7d9 | -7.138 | -44.15953 | 2025-08-24 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53cd6142-12e9-3480-998d-99d34d54d10e | -8.8776 | -62.44239 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 564979f9-28c6-3204-b04d-db3b8fc22a53 | -5.7941 | -59.22502 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05dbc492-03b4-3159-a21c-bdf9b6787eec | -13.48121 | -46.88682 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0340a6bd-d243-3bd3-919e-08df9e748473 | -11.45271 | -47.28736 | 2025-08-24 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c3ebc1d-0410-33b4-b7ae-b69a11d9e12e | -5.74823 | -57.58683 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc848724-5686-3a1d-953a-eca0df921bfa | -11.1063 | -44.77042 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1608af1a-1c2a-3160-8ccc-9dbfae939929 | -7.67107 | -46.24438 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b348d9a-2e94-3b31-a105-94720259d8d8 | -8.61248 | -62.58913 | 2025-08-24 04:34:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 56ef280c-6af4-3fab-9454-a058a2596b80 | -8.15496 | -47.30268 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a728f25-c95c-324d-b214-c951690c716b | -8.05488 | -45.00856 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1e3bf61-93c4-3109-9e8b-4f05a1b4285d | -12.551 | -45.62312 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07fb1d60-f233-3fe1-bb2e-553dfb62fceb | -12.74064 | -48.11166 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 352eece3-37ab-3a63-8dec-9971c2832706 | -12.73784 | -48.10741 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed2c0a9e-f12f-36a1-a278-1eed3938fdb8 | -9.80286 | -46.41999 | 2025-08-24 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23feb02f-468b-3fd5-bbb3-d556756b8c29 | -9.19139 | -59.61667 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 684bbab6-fc87-389f-8899-451757b6e95e | -11.70977 | -47.74297 | 2025-08-24 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bafe79c4-4d1e-3c03-9f08-41f7aedfbf2b | -8.60964 | -62.60342 | 2025-08-24 04:34:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 73e150cb-c511-3fd4-8ba2-491e06072e19 | -8.06913 | -49.65123 | 2025-08-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 068ccc10-d86c-3fe4-b860-a59819708156 | -8.7749 | -49.95989 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17e93262-33c1-3545-aeb0-eeb56c72fb78 | -9.80482 | -61.20949 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e54ba00d-3aee-366e-bf3e-7e4626cbeb23 | -13.46115 | -47.02108 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README39.md)
