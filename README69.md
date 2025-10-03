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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c556123-1468-349b-a007-ce6e8b6f5a31 | -11.13353 | -43.37559 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cebf3745-3282-3bdf-8373-3f4057ccd51c | -14.29007 | -45.91877 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc40a99c-0b39-3f6e-bde0-e1ca69ec76b0 | -10.93009 | -47.05021 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6928212-cde8-369a-93fe-7289e41871c3 | -13.97297 | -48.17901 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1001ff5-a49a-37f8-b9e5-26ade197334c | -10.00818 | -50.25819 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed864e5b-49cb-35fb-b09b-6c1852c3d740 | -13.48125 | -47.24587 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18076fd9-ffa7-3527-8d50-da20062191c3 | -13.27661 | -47.24272 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1ed039a-d3e5-3011-a9a5-63b1da3c763b | -12.61282 | -46.96584 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 529abb7f-8ab8-30df-bfb3-64b59d75e37b | -14.6017 | -48.24265 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f4fb0ca-0d5e-319d-99e6-403daf6b96fe | -10.93941 | -51.07431 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 288caa70-413d-3264-9818-f5bb55bd47f0 | -13.154 | -47.81933 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e173c7c-8456-350d-8feb-5a6b9d885e47 | -14.29631 | -46.03225 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84d88935-90d8-3d75-832b-176c912871b9 | -10.00836 | -50.23022 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 91550546-10af-3a72-ac74-d85dffb01539 | -14.35757 | -46.13933 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3c6f735-4c27-36be-8ab6-2f697809974b | -11.82551 | -45.0413 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd01923a-63fd-338c-9cf2-f1e10b98c5a7 | -13.76425 | -48.06648 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8f6df2ad-1df2-31ed-9491-eacafde5df33 | -13.53948 | -47.24788 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d1b8f38-8182-3631-8700-087e240fda0f | -13.31515 | -44.31123 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d501121-17a9-3844-8e69-d758e61e8f82 | -14.44155 | -46.11071 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4630aa56-e22d-3224-b209-e91ea9f260d4 | -9.44944 | -47.5839 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f4e57ecf-d83e-3c7a-8e00-ca42e217754f | -10.00402 | -48.27571 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bbd55470-d9e1-3cc7-a3e0-d16ce2d0ed1d | -10.20538 | -43.06129 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 59cd1167-b6e3-3f2a-b6f4-8587bfa8d285 | -13.7603 | -48.06571 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| db5b58b8-9f99-386e-aae3-559757560836 | -11.48685 | -45.0172 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f91fad3-663e-3563-bbb8-83d97c1b5627 | -10.00919 | -50.25278 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| de9ae4d4-490d-35de-9b95-e36ec15df31e | -10.06378 | -48.18338 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6b72cd7-7d32-39ac-a3e1-8f6d08e0b683 | -11.47531 | -44.97931 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e78fee6-3ab7-392e-9524-46678bcc4ccd | -9.93548 | -43.58471 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5be951a1-0cca-3624-b639-18e541e6902c | -9.91722 | -50.49751 | 2025-10-03 04:12:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a092152b-aae8-3848-b3c6-69df1c9dba01 | -8.75572 | -49.9269 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 683cbeec-7b00-387c-9ad9-2285b8ff6f8f | -13.96403 | -48.16045 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c436740e-9cd9-31aa-bab4-e83358fbdf2c | -14.43338 | -46.35119 | 2025-10-03 04:12:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c4bbb87-a507-38cb-a187-828706405b03 | -14.64362 | -44.73751 | 2025-10-03 04:12:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fa2d752-013d-371e-9ab8-9895a0f68d45 | -14.30166 | -47.11506 | 2025-10-03 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb08aa19-769c-3c1d-849b-73874da8f1d4 | -13.13363 | -47.89624 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 5d5e3855-60aa-3229-945f-9f69a0cb022d | -13.2482 | -47.30106 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 768705c5-ad4f-3127-a1bd-4a0b9dd4ef34 | -12.9352 | -48.43908 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2638ec12-2ffa-3b57-9cf8-1430fe2e8c48 | -11.08726 | -47.86633 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e53708ed-9fbc-3fa3-9b64-0f53b77290d8 | -15.36624 | -43.67096 | 2025-10-03 04:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4d4843d0-cce1-387f-afa6-343d4e42b6fe | -10.94176 | -46.49109 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1826e08d-2405-356c-9306-adc8524311da | -12.90881 | -47.15836 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e12ac93-f47b-32ac-9aed-7a9e8ef1a1bd | -14.46672 | -48.40128 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58a9daac-55e6-355c-863a-94e021789c1a | -13.14994 | -44.53536 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1258a5d5-e28c-3507-8639-73c1924d2d50 | -10.87675 | -46.71007 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b38496eb-cda6-3fc7-a670-39efe8c71b45 | -12.80367 | -47.02555 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf69ecf0-b1a8-3988-b21a-139b71cb1141 | -10.92228 | -46.74226 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf7a7b48-3b2f-3d18-9963-7b00e9d5a73c | -8.82813 | -46.77704 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6113b31-f9e3-319b-a954-93576f35f84c | -14.64302 | -44.74118 | 2025-10-03 04:12:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4ac515cc-efa0-34a0-af6b-8d95c6fdb7a0 | -13.33396 | -47.59826 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f743c33-5fb9-3cc2-a162-664bb4e9e7fd | -13.96286 | -48.10899 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad99e588-45b4-343b-945b-51a7e517b1c9 | -14.30029 | -45.98703 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5541ea7-13ae-3333-ae2b-e610d19b4810 | -12.53676 | -43.18661 | 2025-10-03 04:12:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13ef24e1-144c-3786-8d8f-a200c6accdd2 | -8.69576 | -47.69466 | 2025-10-03 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c0e31d3-1cc9-3d49-b48d-5203bc6b4303 | -13.5116 | -47.25102 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a16a9624-b5a8-32b4-97aa-1470c044db09 | -13.14947 | -47.89894 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40cbf582-9b84-3d04-90ea-12cb788820c6 | -11.48796 | -44.98921 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9753719c-fb8d-3c22-93db-0f655ad2a68a | -13.29879 | -46.98454 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 644731c5-7dc8-38e6-8dc1-c722921b08be | -11.09131 | -47.8672 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47863b71-2c22-3d4c-9077-47cfc88aa2ab | -12.53952 | -43.19071 | 2025-10-03 04:12:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d5a2f3d-43c8-3905-9d79-429447bb2774 | -10.64567 | -40.2239 | 2025-10-03 04:12:00 | NPP-375D | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ec1f746a-55c9-3cb1-bb05-086da480bd82 | -11.11589 | -47.86341 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d74b7d1-6c90-3f70-afbf-73675830b5cd | -13.39901 | -47.54561 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1933ad9c-75c8-3873-80e0-c4a76876bb52 | -13.78649 | -47.58126 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a174d856-a5f0-32df-bdff-0f734a6a2133 | -13.29975 | -47.26716 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b0cf4200-6337-34b2-8053-b5c5ca7429eb | -13.23733 | -48.49371 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3a6ee18-d64a-32a4-a35e-1f43e786e227 | -9.14574 | -47.63549 | 2025-10-03 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23af0266-0537-318e-ae28-c1491feae0bc | -9.44541 | -47.36947 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d09db3dd-a6d7-3612-982c-889afe676f68 | -13.12347 | -47.88436 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 161d1abf-7729-3a4b-9fa3-5e53fcfb2afb | -12.76221 | -44.89666 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 949c3b44-49ee-3de2-823f-624350f81194 | -11.16866 | -47.17815 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9d1b6c3-cc47-32fb-b8b9-2e5c806ef984 | -11.46824 | -45.01477 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb8c3ded-f762-3553-bda9-647d7ada7c84 | -10.2593 | -48.07697 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 669a80f6-eff5-3416-954c-58008133b460 | -13.19796 | -47.80046 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43122dca-7c76-3b2a-a866-d6f15bafed33 | -12.39594 | -46.51349 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46c952cf-9616-36a8-882c-27e65dfd676d | -13.77646 | -47.54832 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 36809655-1f77-38de-a7d9-d30ae6f3368f | -12.65296 | -46.95842 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60920999-69d9-3cc8-94ec-439ddd1b8c3a | -13.74867 | -47.95599 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16ef4163-ed7d-33af-a3fd-c8e4c5b3b178 | -11.90488 | -46.29586 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 945fe6e0-abcc-338b-8384-a9f0bdf6d3c9 | -11.56947 | -47.65539 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 240c9201-2485-33f6-bc72-f8fd05da6033 | -10.94176 | -51.07445 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be49783b-601e-3924-a9c9-d8dcaa8e3702 | -13.75046 | -47.9458 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e09eb701-c2ad-3b93-9ea9-e18a9a100b15 | -11.43552 | -43.88139 | 2025-10-03 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ea06a94-a19d-3abb-8e65-24e9ff634002 | -11.08249 | -47.86961 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08d101b3-ea78-3438-868d-aba8b9cd37c9 | -14.22806 | -46.09119 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc63dcdc-ea14-3358-8b31-8be8e0ad12f1 | -10.27797 | -48.06892 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddd976cd-36f7-3052-b915-e136ec9f7975 | -11.49857 | -43.50097 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03e4ba3a-13ca-3aa5-b2da-ef5b62119944 | -13.24414 | -48.50309 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d69ae90-a972-3415-a85c-18d255661353 | -14.44337 | -46.37901 | 2025-10-03 04:12:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ff96fb4-8fc4-30f7-ab40-136d57f71aeb | -12.9385 | -48.43225 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48590741-4202-38c6-9ee3-0a05a721bdd4 | -13.306 | -47.59815 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a66c682f-24da-3a05-bd2a-b963f8f5284d | -10.85518 | -45.38564 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4d08c06-fe11-32d3-845b-02434471250d | -11.83539 | -44.9391 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd231934-3203-3b70-85ba-a5c7d25b609d | -11.3116 | -47.83928 | 2025-10-03 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbbbc788-2bc7-34c8-b398-b172ac5890d2 | -14.41478 | -46.1604 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27e08035-b2ac-3316-95d3-bc01d7ecbb51 | -14.42032 | -46.0913 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67af324a-d230-34af-bad4-8d5ff4bddacd | -11.42909 | -43.49323 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f89d564-c96c-33e8-bd9b-fd71ff59df7e | -13.7433 | -47.98654 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c5ee045b-5d92-3511-987e-2eace492d7c8 | -14.35892 | -43.83776 | 2025-10-03 04:12:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94286331-cbe2-346c-b3ec-f34bbf90caf4 | -11.12405 | -47.86484 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 10a93169-7966-3e2a-8c2f-c7cae41d0e77 | -14.45626 | -46.34653 | 2025-10-03 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README70.md)
