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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c21335f5-a314-3ba0-bdcf-8e9c9aef037a | -6.32299 | -55.2844 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 847592f6-8f36-3679-a07c-4ae37b200cc2 | -6.66488 | -50.93188 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb7a7832-3d23-342e-9fed-2c594db85907 | -6.36928 | -58.29385 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f391ac24-b9b4-36c5-a656-2e8173157dfe | -3.33647 | -59.8077 | 2026-09-19 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 224f27df-96b8-3607-a124-22c50b269bcd | -9.67722 | -48.3327 | 2026-09-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 395bb00e-e674-3fee-9651-9f26e500b6f0 | -5.86751 | -52.03502 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b85ed542-caa1-3ea8-8ee7-1f00ed0ace3f | -2.90151 | -54.18246 | 2026-09-19 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebfe1383-c450-3816-aa7c-9241cd672cb5 | -4.4438 | -55.00552 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c475499-31a8-32cb-a2db-a3c02f71afc4 | -8.6107 | -54.59211 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf6f39cf-f6fa-3abb-8bc1-5b698e2e0c6d | -6.97921 | -42.17982 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 395f7f76-e30c-324b-a324-15c6f3a41d9a | -7.21974 | -49.6372 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa63cdfe-363d-33d9-8968-ed0bd88c18a9 | -4.56899 | -54.90487 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69224ffb-f7a1-324f-b0a2-8a71217e0c16 | -4.06914 | -56.25036 | 2026-09-19 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb6693ea-7632-30fd-93e6-8fd03b8b0c88 | -10.58779 | -46.54386 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efce365a-989d-3eae-9f70-0a33e694e07a | -11.08183 | -48.30282 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5a1bdb1a-0965-3862-ae5c-7c7bbb71cd27 | -10.53401 | -46.73683 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9616cb14-baf7-3a6c-a87e-ef8f4a7c4bdf | -4.81905 | -42.88001 | 2026-09-19 04:57:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 370dca5f-a0f8-3c9d-a916-c58edb0f201c | -8.82666 | -44.90086 | 2026-09-19 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa9b474e-662a-348a-a44c-3db4f0b9df46 | -4.83641 | -48.2033 | 2026-09-19 04:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec216279-3448-3b26-b4f4-254fd06d6af7 | -4.59313 | -42.96157 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c062b55-2962-31e5-8806-259dcfb8d0ee | -9.04323 | -48.74966 | 2026-09-19 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73cb79b9-61cb-314b-b286-bfdf9586fe6b | -10.02708 | -51.90516 | 2026-09-19 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fe6638a-6088-3052-ae8d-2bb757b3667e | -9.03042 | -48.72725 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fdba8f99-2f9c-3cf6-b48e-e34d9dd5fefb | -10.53676 | -46.75151 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0af1e6e2-545b-345e-bf69-11e33601d037 | -6.30659 | -55.91687 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d769dd96-3ffc-307d-baef-7f3d8b6b1270 | -10.93579 | -47.85513 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56239e43-df7a-3097-be25-836c3db3d73a | -3.28727 | -53.2651 | 2026-09-19 04:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb9d1ecf-b746-326c-ae91-61791cd32d72 | -7.83154 | -55.41503 | 2026-09-19 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ded64ef9-9444-347d-ad4a-33b17af200cf | -10.46378 | -51.25766 | 2026-09-19 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32cbc406-983f-3018-a3ed-53dd25026ba0 | -3.43055 | -50.66606 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a831c5f-e0af-3240-8edf-9cc0c9469025 | -8.71824 | -44.87368 | 2026-09-19 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae3fe69a-6f7b-3132-9c39-7f4546e04c0c | -5.86811 | -52.05288 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9549ca25-37fd-3b65-b640-d23c61bd42c9 | -9.9528 | -46.54683 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52c1ed77-ca55-3695-b10c-3a8d042be1a7 | -2.63919 | -54.3093 | 2026-09-19 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4dc9944-9c10-38d8-9452-0e8cd33afa48 | -10.79834 | -46.64582 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29e0f89b-bdb4-382a-be2c-597cc3b4f689 | -11.33004 | -47.35384 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c7e6363-d10e-3ae5-a348-41cd05a84bf0 | -3.75978 | -55.96057 | 2026-09-19 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bcb3ff0-6796-31e5-80b0-d956c37bedda | -6.35246 | -51.73331 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd3797c6-5cb9-3c1a-887f-6843000a1175 | -10.52424 | -44.84827 | 2026-09-19 04:57:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c525ac3a-34b7-3094-a152-700447b28f2f | -9.71555 | -54.81534 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31b3f242-0553-393b-97f6-6e747d168905 | -3.47158 | -54.69747 | 2026-09-19 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a590b45-74db-355e-af15-d70e5ec8a584 | -9.40992 | -50.20409 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb1677b4-8ed0-3c1b-b324-c8a917c7793f | -7.37544 | -44.73195 | 2026-09-19 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a314e6be-8595-38a6-b92e-3f585f53cd98 | -4.68523 | -46.40049 | 2026-09-19 04:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1507886-becd-30c7-bb9f-9c435da5806e | -6.75964 | -59.43073 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3728676a-5ec5-3426-93ac-f6a2d660beb7 | -8.3772 | -47.2105 | 2026-09-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7596dd6-bcdf-37d6-8501-157b92394ce9 | -8.31833 | -50.91735 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86912eef-2bd2-3fcd-be4d-c36cfa577313 | -9.94403 | -45.27296 | 2026-09-19 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b17495ed-eb53-369f-9425-4c6a34bd19da | -7.59957 | -55.69728 | 2026-09-19 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6f1474d-54f3-3bc1-a086-d6f0d92dd54c | -4.56227 | -42.98235 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86930834-f7d8-3f6d-bc40-2b4b2d84ed0e | -6.7105 | -59.46053 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dabe7251-6e68-3785-aa28-c32e02638e77 | -9.75433 | -46.59879 | 2026-09-19 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9d1976e-2ecd-3968-a1f5-bacd44784fab | -4.50831 | -54.96334 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0289aebb-85b1-31e3-953a-6d3b23ffb752 | -9.47353 | -40.32207 | 2026-09-19 04:57:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8a448543-f8d6-32cc-a223-8dbc9165d24c | -10.16916 | -48.52006 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c97a5153-5650-3b9c-adca-29cf583ea537 | -7.05488 | -47.49208 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 884c75fc-f6ce-3451-8a64-4837561103ca | -9.35914 | -48.29312 | 2026-09-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e2ffba7-a7d9-3d3e-8858-d1a228810b2e | -3.36195 | -50.45585 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a0ac9e0-c0b9-343f-b763-e5342121f76e | -3.26636 | -54.26517 | 2026-09-19 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6beb6810-a47d-32b9-8561-7b56d726c936 | -7.38137 | -47.75357 | 2026-09-19 04:57:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb77c0c2-66c0-3ab9-b20d-85d5c3ff3ead | -9.95215 | -46.55159 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 20b54112-5421-3a82-bfc1-c201ae2c0d1b | -5.86316 | -52.06276 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 861cdd72-9b39-3987-b2a7-898fc784dee6 | -10.99249 | -48.32455 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9c3a351b-d43e-37f1-a946-0b263d9c17d3 | -9.74614 | -46.08511 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 725278e7-2574-3131-aa05-1626af44c526 | -8.60955 | -54.59929 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8559842-b35e-3ec2-9f08-68d8ec0be70b | -9.00842 | -44.91 | 2026-09-19 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f1ecfcc-3550-38b3-bb8a-d59d8282693c | -3.4565 | -50.61109 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4708563-01f3-3d47-8310-520c89e0be4c | -6.37368 | -58.31786 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afcfeba2-c46f-345b-9e7e-8a20e31c505f | -9.79906 | -46.09406 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ca9dc51-2358-368e-a179-ce43813e4a21 | -3.51821 | -50.80027 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7fedd73e-a0ed-3cb2-9732-f6ad332b6f51 | -3.03656 | -51.37711 | 2026-09-19 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81393311-66d4-3c02-b0ca-be82162e4bb2 | -7.61116 | -45.43173 | 2026-09-19 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e96e911-a06b-3b13-b5bb-8ee84df3015f | -9.25223 | -46.20415 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e2b5064f-5ef3-3b3a-9a54-4146e001b76c | -4.11057 | -49.06738 | 2026-09-19 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdfc7b61-199f-32ec-bfbe-ea110598fc8d | -7.06535 | -47.53586 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3a90b30c-e477-3160-bb0b-3a4b51950d31 | -10.80567 | -50.90498 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f77166a0-ee26-392b-b34f-10b52e4bd07e | -5.8793 | -44.97681 | 2026-09-19 04:57:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77f525d0-af61-3737-9b5e-d4c00b7527db | -5.88202 | -53.61493 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc6899e0-4f4c-3c6c-ae87-1e9301087ef8 | -9.93794 | -46.52378 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fd18f0a-6d63-3276-868a-dbf158ee94ab | -3.37214 | -50.45742 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cdc68a8-ce1a-3590-8347-b12bab1c4cc1 | -6.31519 | -55.2601 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62de2009-929f-3666-863d-1a409c4a552c | -6.36863 | -58.29763 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e725d1e-4cc8-394e-9faf-de31a076ad27 | -5.75494 | -57.45012 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8c70c66d-14bb-3810-a809-53cc63ed9eba | -8.9854 | -54.43265 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b299a999-e640-36d4-bbde-2214aa045568 | -10.74633 | -50.61119 | 2026-09-19 04:57:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e793a15-bf50-3519-9e4c-e9ba54c666c7 | -11.08043 | -48.28166 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6898f98b-be55-3e85-b38f-37d5c19ac7dd | -6.44318 | -59.98006 | 2026-09-19 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acfb6ec4-c32d-38b3-8385-643dc294836e | -4.55237 | -42.97383 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab892f27-6764-3c86-be0a-38223be6ca23 | -9.04296 | -48.72404 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfc5e2d3-1339-33b7-b721-3edddf3e0dba | -9.68221 | -48.3253 | 2026-09-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cd50e0e-8c25-3ab4-bc99-ac09776f8fe7 | -7.67012 | -46.12539 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4dd22b5f-3a78-31dc-af3f-085db63811f5 | -5.86479 | -51.94491 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a1ad176-5e39-3f84-ad48-12b49ef46b06 | -11.00138 | -48.35222 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 61839271-676f-3805-80c6-87e807eba43c | -2.89416 | -57.80317 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 530252a5-789b-3fda-ab9d-a252be34aa7d | -9.55478 | -46.58874 | 2026-09-19 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b805ec3-3317-3763-afe9-5b1e08c66d66 | -3.43393 | -50.66657 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32d23f51-aee6-33df-aa89-29a865b0f71c | -6.33766 | -59.96476 | 2026-09-19 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2cec36d4-1562-37c6-be7e-9c860e890f0a | -6.01401 | -53.68287 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1c1b60c-dee5-3fe0-b000-33b92f9a5569 | -3.37893 | -50.45847 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5be9d20-ec25-3b83-a783-77cef5751449 | -10.44975 | -48.67644 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README78.md)
