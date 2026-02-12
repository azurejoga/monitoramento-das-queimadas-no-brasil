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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 775fd3e0-18dc-3acb-ba3c-5205feed0c29 | -9.23149 | -53.20036 | 2026-02-12 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 61da70a7-53a6-32b2-b0bd-522280ea1b19 | -16.17036 | -58.24083 | 2026-02-12 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 46678698-d3bf-3578-899e-8812096fb32a | -19.09571 | -56.06519 | 2026-02-12 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ccfb1572-b66e-3262-903f-9e5e041216a9 | -20.56039 | -54.65582 | 2026-02-12 04:42:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cb2daf4d-8900-3f24-bdeb-22bc84377cdc | -16.25999 | -60.03195 | 2026-02-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c47f5fb-a16b-3929-99d5-a0d09742dd14 | -16.16295 | -58.23987 | 2026-02-12 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 70735eaa-8fd6-3cc0-b2fd-0bd29f19eca9 | -16.16556 | -58.23968 | 2026-02-12 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2808ca62-2184-3211-b0f0-128efb2228c9 | -16.16776 | -58.241 | 2026-02-12 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d55228a4-0b4f-3c3f-9577-81e3094b3778 | -17.31122 | -44.92886 | 2026-02-12 04:42:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b936219-e4c5-3294-870b-35e44a652f2e | -19.09245 | -56.06604 | 2026-02-12 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e1cfb908-39f2-3322-b0d4-5284f95a8ab3 | -16.25926 | -60.03545 | 2026-02-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25aa8514-859b-3820-bc4d-41fde6140b45 | -19.09644 | -56.06686 | 2026-02-12 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7d543214-8675-3ba4-bc82-e71b67198d61 | -22.69502 | -53.9517 | 2026-02-12 04:44:00 | NPP-375D | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0b8fc4b9-1816-3239-bf9d-316311e9c46e | -26.80578 | -52.07953 | 2026-02-12 04:44:00 | NPP-375D | PASSOS MAIA | SANTA CATARINA | Brasil | 4212270 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 18d24560-d2c6-326b-990c-90793093120f | -22.78166 | -53.27368 | 2026-02-12 04:44:00 | NPP-375D | PORTO RICO | PARANÁ | Brasil | 4120200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0d6d9e87-f210-338c-9997-0ff7664038cb | -25.05092 | -49.24039 | 2026-02-12 04:44:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 00b965bf-0cc7-3271-9bc6-b7b7dac8dc92 | -28.61886 | -50.43513 | 2026-02-12 04:44:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a823b7f9-04c1-3808-86e8-76b749f90512 | -28.85424 | -50.57976 | 2026-02-12 04:44:00 | NPP-375D | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d0cb2390-f437-3cdd-a274-7034cc9aa85b | -25.1707 | -49.40181 | 2026-02-12 04:44:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 39e08bec-839c-3e49-92a2-46cc82284a68 | -21.17507 | -56.50294 | 2026-02-12 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a99bd29-5171-3c84-a8b3-4dc3c7da3e94 | -27.92157 | -50.73284 | 2026-02-12 04:44:00 | NPP-375D | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dc238325-f83a-3d6f-8862-b299e3a16c4c | -25.18292 | -50.70264 | 2026-02-12 04:44:00 | NPP-375D | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 61ee12ba-e5df-3105-80bb-b0a3d811f37f | -27.09986 | -50.52791 | 2026-02-12 04:44:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e9cf8e49-df76-35e9-904e-708faba94c5d | -21.17902 | -56.50384 | 2026-02-12 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44603d4b-ed78-3de7-9bcd-5f1a36f67501 | -25.04732 | -49.23986 | 2026-02-12 04:44:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1dcccd46-1308-39fe-be5b-becc548b67be | -22.69571 | -53.94765 | 2026-02-12 04:44:00 | NPP-375D | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 48e7d5ab-9bfe-3461-824b-0ca53049ea77 | -21.17597 | -56.50539 | 2026-02-12 04:44:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e35fe076-9db8-3444-b206-1b910e4f1094 | -28.6224 | -50.43576 | 2026-02-12 04:44:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| baea46a0-7d85-3146-8eae-71503fd370e0 | -22.65939 | -50.6657 | 2026-02-12 04:44:00 | NPP-375D | MARACAÍ | SÃO PAULO | Brasil | 3528809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| df28a960-50b4-308f-8543-6d86ce9a7879 | -31.06298 | -52.59558 | 2026-02-12 04:46:00 | NPP-375D | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 64edd537-1ac4-3c50-8b0a-5b5e29e849e2 | -29.6846 | -51.08498 | 2026-02-12 04:46:00 | NPP-375D | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| db6654d4-0949-3c90-bdc8-799dcfb46191 | -29.11283 | -51.47669 | 2026-02-12 04:46:00 | NPP-375D | PINTO BANDEIRA | RIO GRANDE DO SUL | Brasil | 4314548 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 924b9ea5-2a74-3fd5-9e19-e4093d5402df | -29.21261 | -50.84039 | 2026-02-12 04:46:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 15cddcdf-41fe-3994-9c46-a56b76f8f398 | -30.29478 | -50.92403 | 2026-02-12 04:46:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| c4fd2cfa-ba05-30ca-9ab1-dc526f3b5710 | -29.55616 | -56.74939 | 2026-02-12 04:46:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| 583f6dd6-76af-3f51-8318-82fc9dc16a5f | 3.38922 | -60.6366 | 2026-02-12 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 991b7329-5626-3794-9e5b-4b5a74d627d1 | 3.08436 | -60.82404 | 2026-02-12 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4e097ad-f9e5-3db6-b797-8e8b5d3f0a9d | 3.08711 | -60.70195 | 2026-02-12 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 103cd415-9e96-3e7d-b16d-407513e3ffd4 | 3.08756 | -60.70497 | 2026-02-12 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 533f6d1f-95d0-3770-8a0a-0824e6bff08b | 1.34773 | -60.04301 | 2026-02-12 04:57:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 82ae1cb3-5bdc-36b4-9d23-0df84e80055d | 3.07541 | -60.83489 | 2026-02-12 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7185ddf8-c8ad-3e5b-be03-38ec7f0ae557 | 3.3841 | -60.63736 | 2026-02-12 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6c4514a-9e14-3043-bd68-944328b24938 | 3.08481 | -60.82713 | 2026-02-12 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bea3a802-fbe0-3114-a2ff-329f5fc08bb2 | 3.08802 | -60.70799 | 2026-02-12 04:57:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03c87460-6de7-3e3e-bc40-36ca56426aed | -10.11871 | -42.17157 | 2026-02-12 04:59:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 878768ed-4d2b-38f2-8467-2bbd0a1da9b0 | -10.11944 | -42.16544 | 2026-02-12 04:59:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| be84984f-891a-39ba-b1f3-f7493653d1b2 | -16.16672 | -58.24048 | 2026-02-12 05:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| edffe3ae-1321-3fa4-b478-7806ce24a0a9 | -16.16334 | -58.23987 | 2026-02-12 05:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 82029bbc-3418-3fbd-ade1-52473ce92600 | -23.41515 | -55.24246 | 2026-02-12 05:03:00 | NOAA-20 | CORONEL SAPUCAIA | MATO GROSSO DO SUL | Brasil | 5003157 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eff47b0d-6501-38fb-9524-e5fe8bd775bf | -21.96599 | -56.78056 | 2026-02-12 05:03:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e9867d9-e49d-3bfc-b663-4f4bb96fca65 | -22.69699 | -53.94723 | 2026-02-12 05:03:00 | NOAA-20 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3da9f11-f982-393a-9108-f5474a76901c | -20.55979 | -54.65799 | 2026-02-12 05:03:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cebc4077-24ec-35df-9696-14b4eed93952 | -25.047 | -49.2397 | 2026-02-12 05:03:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 657fde76-c7de-346f-9f95-d8cc60593125 | -21.97049 | -56.77349 | 2026-02-12 05:03:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 57ebc745-ea1c-3bb5-86ec-1e961fa24fb8 | -21.17456 | -56.50224 | 2026-02-12 05:03:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a3f27559-2ebe-3d91-9c54-7739fd9dd251 | -21.96656 | -56.77674 | 2026-02-12 05:03:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bcd6b1e-d52d-3d1d-9cad-f985338558c1 | -22.69634 | -53.95216 | 2026-02-12 05:03:00 | NOAA-20 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c9a30fc5-6885-3a34-a816-de8cad8cafad | -25.04669 | -49.2429 | 2026-02-12 05:03:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c80a71e3-67ce-3e52-8350-357635ae9dfe | -19.09329 | -56.06605 | 2026-02-12 05:03:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b1444005-d053-3e61-b95f-ec9035d50a37 | -29.55604 | -56.7513 | 2026-02-12 05:05:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| fd8127bf-f527-35da-9b10-740279829b9c | -29.68538 | -51.08776 | 2026-02-12 05:05:00 | NOAA-20 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| f7de8430-fb09-3160-a622-71f07e14a003 | -29.68594 | -51.08164 | 2026-02-12 05:05:00 | NOAA-20 | CAMPO BOM | RIO GRANDE DO SUL | Brasil | 4303905 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 884177e4-3208-3a74-9680-622cde8b67db | -28.62291 | -50.43521 | 2026-02-12 05:05:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4033d971-c84b-3957-b3dc-ca09a3d128ae | -28.62262 | -50.43851 | 2026-02-12 05:05:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 56f5aeca-e151-39a4-b51c-0d0f2712d3f4 | -27.10248 | -50.53009 | 2026-02-12 05:05:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9d41978d-0479-3f8f-b7c0-d84e2b158fb7 | -27.09889 | -50.53106 | 2026-02-12 05:05:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a44794dd-6ac7-3531-8cda-f01ee4a0e879 | -29.68245 | -51.08152 | 2026-02-12 05:05:00 | NOAA-20 | CAMPO BOM | RIO GRANDE DO SUL | Brasil | 4303905 | 43 | 33 | nan | nan | nan | Pampa | 4.5 |
| 61c8b312-350e-37d1-999d-02bcced1434d | -29.55665 | -56.74669 | 2026-02-12 05:05:00 | NOAA-20 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| a7cea8df-93b2-3848-9bed-04ddcc73b93f | -28.61786 | -50.4346 | 2026-02-12 05:05:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 28dedb11-32e7-3a26-899b-2822648f0157 | 2.9964 | -61.1367 | 2026-02-12 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| faf4b3ad-1724-3126-bb4f-185d3801fb05 | 3.08186 | -60.8234 | 2026-02-12 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f01da96-8f2a-3412-80fe-e690431df43f | 3.08615 | -60.70339 | 2026-02-12 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60427dd8-9269-3ce4-a3bd-60e71bd0caa0 | 3.25146 | -61.34586 | 2026-02-12 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a273736-84f7-3803-907d-c3089c2b35d8 | 3.22709 | -61.19411 | 2026-02-12 05:46:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6a8aa4d-1f66-34cc-914a-4a98575d58a2 | 0.09191 | -60.56816 | 2026-02-12 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fedc2530-d0d6-3069-b392-c0b06d8f8cb3 | -21.17418 | -56.50063 | 2026-02-12 05:54:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8ca8c61-1f5b-3464-9230-59c811ec9b49 | -11.26284 | -38.47302 | 2026-02-12 05:57:00 | AQUA_M-M | NOVA SOURE | BAHIA | Brasil | 2922904 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7a0caba9-c9d6-3f8b-9533-e0c120d0f332 | -10.11529 | -42.16089 | 2026-02-12 05:57:00 | AQUA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| d82029c8-a16e-3c85-989f-6c553e229236 | 2.98937 | -61.14116 | 2026-02-12 06:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc767707-4944-3853-8341-7d0f2d65edd9 | 2.99573 | -61.14411 | 2026-02-12 06:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3c193176-402c-3485-bbc8-f576edef2bc1 | 2.99289 | -61.13897 | 2026-02-12 06:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9c1169e-6125-3297-9fee-2cb679833baf | 3.32543 | -61.02658 | 2026-02-12 06:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f8b4cfd-ba9e-3e73-883b-ae4033f9ca89 | 2.9872 | -61.13993 | 2026-02-12 06:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd52cd57-553b-3b9f-97b8-50ebf06accac | 2.99506 | -61.14021 | 2026-02-12 06:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 458ed28f-bda6-3ef5-9a50-1531176fd831 | 2.99353 | -61.14288 | 2026-02-12 06:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2de30fe-26af-343b-827e-c45fdef5f369 | 3.3261 | -61.03049 | 2026-02-12 06:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c7f63bf-e762-3b36-8994-801b4ad5e395 | 2.9887 | -61.13726 | 2026-02-12 06:16:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0f2b96e-5823-30d1-b3d4-b1e162defe25 | 2.99763 | -61.14097 | 2026-02-12 12:48:00 | TERRA_M-T | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 14.2 |
| bb741a5a-1fb1-3f8b-b325-64747e8556b2 | -18.54321 | -55.05007 | 2026-02-12 12:55:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| fd6feaca-59ac-386f-afad-5870bc422ffb | -25.28543 | -54.22552 | 2026-02-12 12:57:00 | TERRA_M-T | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 45.7 |
| d41fec2e-9cb0-32f2-a293-fabd168e5a1d | -25.7739 | -49.3409 | 2026-02-12 14:20:00 | GOES-19 | MANDIRITUBA | PARANÁ | Brasil | 4114302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |


