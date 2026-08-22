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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee0695b4-542d-3ee2-b66b-b4442d702cbe | -12.8076 | -48.40203 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c0d3309-4a7f-3d66-9fb2-8383e6d18070 | -9.165 | -59.45929 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8a766029-6739-3b27-a626-c174a07d0852 | -6.77472 | -58.65677 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5dde7ee5-786f-3503-8108-49be6d94c601 | -10.80996 | -50.97612 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 46b7561b-aada-3bc3-8897-2c46ef7b796d | -12.26013 | -43.17499 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 56bc8250-9866-3c2a-b84f-b356f588bf19 | -9.1811 | -59.44529 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bc387cd9-3117-37e9-a3ec-12cb656617d1 | -9.15851 | -59.45806 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| cad4e022-8baf-3af4-8291-52b1d3442cec | -6.81495 | -59.66082 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1bb4da71-6b90-39ad-a8c8-23896aaaae6c | -6.80017 | -59.66446 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2f11047-56be-3a3c-8b65-9aee6464f85d | -9.17586 | -57.00088 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d280128c-31d7-3ac1-83de-54d0a1d69039 | -11.45489 | -47.55305 | 2026-08-22 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b43057c-cb23-3258-8bd7-a046225ddd0d | -8.97007 | -50.75506 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9419981-8616-3ffe-a495-9e374defc2bd | -8.5373 | -54.83092 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6c468c05-fd6b-38ca-9fc4-2f0b0a1aa8d6 | -8.534 | -55.33352 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 040efc83-79f0-3c5e-baed-726da9cee924 | -6.94112 | -59.31893 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 861369c5-675e-38d7-b484-4e54fa4b7bd1 | -9.17462 | -59.44407 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6e1355cc-371e-3c4b-b995-db8f77685eb0 | -11.83749 | -51.95995 | 2026-08-22 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dec2f942-9a68-35df-afd7-54cf980dd587 | -6.15862 | -53.70359 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0a6665a-2650-35db-8660-e7be067cf990 | -9.16395 | -59.46478 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c363b8ee-4538-37dd-a617-493ac54de3c0 | -12.10117 | -56.3171 | 2026-08-22 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5eba1f29-4d0a-3968-8e23-a4fe539b3dfa | -12.2617 | -43.13448 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3dfe3313-bb51-331e-b9d9-780fbc94c234 | -6.94888 | -59.31422 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30384f8f-e38f-325e-84c3-ac6fa9d8bc5a | -6.76311 | -58.67991 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a14c4e35-0bdb-35ba-977c-f14ab0e0060f | -6.81075 | -59.38747 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8bfbff51-bee3-3656-bfd1-74f8c96e9786 | -12.27384 | -43.16198 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 21a2ef5f-439a-32a1-bd27-db81a453ba21 | -10.24267 | -50.36385 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd63f516-339b-3362-a081-c9c635d4d740 | -6.89203 | -59.03167 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0ea5b13-c051-3fc9-91b7-e12feee369f4 | -12.72357 | -48.4169 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e4125a2-f8ce-3577-9b94-31d690779302 | -6.8499 | -59.43751 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3545096a-24dd-3870-b5eb-85c8b90fc71e | -6.80105 | -58.62203 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a82e59f-3328-3b8e-aa18-28342e74350c | -6.66554 | -56.33976 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eea78c28-732e-3e17-802b-7b9ef9da8ac4 | -6.09284 | -59.95207 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 233ca1b0-0b90-36b2-99ee-9004222c43d6 | -12.7667 | -48.40248 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c18e2ade-c709-3dd5-a761-de9b0b1ebb5f | -6.25783 | -55.41562 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c89cba3c-fb89-3860-ac74-a0def7a9c121 | -10.93895 | -49.59952 | 2026-08-22 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 743770f8-03fd-375d-baac-23d39e65b72a | -12.84678 | -48.45558 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d394fa0-93bd-3cde-8f06-4d4628c16ffc | -7.69476 | -46.15441 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47725627-8e40-3c08-b7e8-66df2fe78ceb | -8.53437 | -54.81919 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9304bd3e-9199-3862-a1ff-2181b47e97b8 | -11.33638 | -44.95931 | 2026-08-22 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e540798-81a6-3bf7-ac02-2fc8f8efbf5b | -10.29915 | -48.21714 | 2026-08-22 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92b89378-d430-3f85-b13b-2b15a12b5d85 | -8.09186 | -51.67134 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5936bf7e-9096-309a-8ebb-95e582fc38b2 | -8.8917 | -60.54402 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0703adbf-980f-392a-a7c0-41718b4be9a4 | -6.43303 | -54.95698 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b4e095c-9cf7-3704-ab77-5763871cc3b2 | -12.5535 | -54.77053 | 2026-08-22 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e63ed743-4fcf-30a9-85a6-f57ca4e231d4 | -6.61355 | -56.37264 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cce878d6-a5bd-3ec2-a198-2144e464cfde | -13.08657 | -43.33475 | 2026-08-22 04:27:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b35d63a-e1b2-314c-8a29-187cf50ed71a | -8.6326 | -54.73743 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a7225b40-58d3-3a1a-879b-5bc3c5bd99ac | -6.9165 | -60.0722 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb030e63-545a-3197-8076-28b8ebea96d3 | -12.66651 | -47.80691 | 2026-08-22 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ab77ad7-6cea-337e-bbf4-7f02538f22f1 | -8.09782 | -50.03334 | 2026-08-22 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf29e9e8-bffc-32e1-b789-dcabef58b402 | -6.23446 | -55.4251 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64b753a7-e9b4-3318-9e9d-6dfc038c394d | -6.00193 | -57.81409 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 30c5ea64-0741-3f3c-95f1-4ce3c43d7ebe | -9.17358 | -59.44954 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 58eee4d9-2550-3e36-827a-4b350296dec8 | -11.1054 | -49.88834 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38fa6e02-8dca-36e2-ae77-b88cc53a0e7a | -7.63986 | -42.72827 | 2026-08-22 04:27:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3d3269b9-0389-333a-80c1-389486839557 | -9.21791 | -59.76765 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e487e7e1-9a8a-3699-b266-0800a4a72dfe | -6.76142 | -58.65228 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1d6808b9-8897-3d93-a675-80e15157470c | -9.05502 | -57.07061 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26dcac47-53c4-3ca8-8c12-7bff5028586f | -6.25591 | -55.39501 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 04864ef0-3d0d-3094-9d9c-ef662ad302af | -6.80393 | -59.42325 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 78e794ce-0666-3841-890c-fde5cf7db6ef | -9.04926 | -50.86413 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82972686-c3df-355e-b82a-3a8d1bd3f661 | -8.18564 | -54.9782 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9eda7422-3fad-3f4c-b9b2-ce5d9194df8f | -14.01917 | -46.21507 | 2026-08-22 04:27:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 205ef40f-a0c8-3948-b7ca-5ea56a4ba717 | -9.11744 | -60.33775 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e2704e27-331e-332a-a615-0847c7575b37 | -8.27236 | -46.35246 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01a352b3-c605-3ce2-8af1-01df69975676 | -10.94347 | -50.29259 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 344cb529-2a91-3989-ad11-4827cd347956 | -7.47622 | -45.14674 | 2026-08-22 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb50e5c2-22ca-3541-a8be-80a85438c597 | -6.99894 | -48.02881 | 2026-08-22 04:27:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 63994ed0-39a3-3596-b8f0-c5108bc23ed4 | -9.16882 | -57.00779 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3d70301-3440-307f-ae9c-c13de0683806 | -12.84346 | -48.455 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42c6b4c6-d4e4-36d3-b7d0-bbb8f6820af2 | -6.81966 | -59.41363 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a9f6b321-4385-3f38-bb4b-85b6b1c0cdeb | -10.90144 | -50.24066 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8891ccb-66ae-3c30-8c04-917b14033b45 | -6.905 | -58.99883 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b15fafe4-f462-3ae0-b35b-93a542786d9b | -11.50369 | -46.64462 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73156f3f-8a64-31fd-a5d6-2021ffdf32e3 | -9.00479 | -50.71798 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ab07c3b-ebbf-326b-86be-ef7474eb6ec7 | -8.2229 | -55.02795 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e29b32b9-4e17-3ee3-bae7-99433b0a266c | -6.89592 | -55.71456 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3a11951-de4f-3e8a-bc97-a0201f6ff535 | -6.48521 | -51.5985 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9edb2a66-a4e8-3ac1-accb-d2b85e1ff508 | -8.17444 | -54.98355 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34a631f1-09f1-3a0d-bb7d-0f86bda77633 | -6.77374 | -58.662 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 39b1e0d9-9ea4-3404-9de8-ac1bfb6a9118 | -6.81677 | -59.41466 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3389cf66-5976-3fa9-a7d2-a506487331dd | -6.88233 | -59.41265 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 80cb9300-b99a-3f76-99f3-2960818f0216 | -6.79377 | -59.44 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f0ef13f4-4776-37d4-8361-fb5eae03c326 | -10.79305 | -50.98682 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 60873c0f-e5a6-349f-bc46-3be97ca16577 | -6.0889 | -59.9627 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a1d7b24-846a-3c6a-9501-69cef0e0d4d7 | -12.72734 | -46.46212 | 2026-08-22 04:27:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 71c91a21-ec9f-34d7-ba51-ccb5700085b1 | -11.16186 | -54.0291 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fc85389c-5357-3b5c-affa-af72883060cd | -9.05569 | -57.06697 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75797c48-41a3-3756-ac95-83a24f57aa4f | -13.40382 | -54.3681 | 2026-08-22 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f88c5de7-98e6-326f-a3e3-8dfaa8312211 | -7.02161 | -59.55164 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f1cfca4-82d1-3840-8fed-16b44c03a4a0 | -8.58699 | -54.74952 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 802abd4b-27dc-342e-b258-97a47204287b | -6.75793 | -58.67553 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e3a30a55-d1ab-3774-8d4c-003a7d1de99e | -11.17028 | -54.00787 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c14dbfa3-8f3c-3556-8d34-487a55ba68dd | -9.18649 | -59.45107 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0301868e-c420-3fed-bb5a-7d21b081a927 | -10.79673 | -50.98745 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 5f92297c-1067-387e-9573-ed07c3ffc48a | -9.192 | -59.45869 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| abc5404e-8314-3f55-bea3-8bc4a6c88aed | -12.27249 | -43.1717 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| be5fab8d-9c27-3abf-aae1-ef677cbee342 | -10.96325 | -51.41473 | 2026-08-22 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8aa41455-64c7-3001-9bfb-e5f366886b2f | -6.37231 | -54.94318 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e055701-b6b7-36ed-a28a-312ba2d74d92 | -8.03124 | -51.80012 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README24.md)
