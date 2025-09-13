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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ffd5700-a707-37d0-9455-c12738ed2d6a | -14.42675 | -47.33187 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 039ee46d-d549-3a52-acc0-d46fb5c3f1c2 | -12.99207 | -46.73376 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3a28bd4-30c4-30cf-aa38-919fab14702c | -11.73692 | -44.21479 | 2025-09-13 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bc8a70b-bc3c-3f58-9791-81f7b23ea6a1 | -8.05162 | -44.51844 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1eb792f6-d535-3f3e-84dd-e36353744ef0 | -14.22598 | -46.30292 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 77174d67-8624-3897-9c80-ff6295eff5c6 | -9.03355 | -47.05932 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60584df2-b8a6-36d2-8d80-aaaab3b7bba4 | -12.0921 | -44.87506 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4309ac78-0a62-3240-b882-4357021c0982 | -9.7153 | -48.32256 | 2025-09-13 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f170eb4-dc25-34f6-a5ec-a964b44aec8f | -14.2153 | -46.27934 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7ca26cfd-22a8-38a9-b187-18dd15c6a1fc | -12.11655 | -44.85096 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2bf57409-1b75-3461-8f25-be3133b42478 | -11.17845 | -51.41788 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7402d59b-b127-353a-8ad9-a0adcb02eb83 | -11.4391 | -43.67837 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24793dbd-0a02-3dfb-ab40-1079eee0c168 | -14.21176 | -46.2786 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ba47dba2-6bef-3437-9e7c-596cc883c256 | -11.86755 | -50.57398 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 48e5c42c-5aea-3a42-acad-038ddb16e16e | -9.03016 | -47.05518 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 431bdac1-816a-3e96-a568-bf444373c778 | -12.81383 | -47.98871 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a164bbd-3fc8-3d30-abda-df5fc33fcb65 | -14.20041 | -46.2806 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ad7f846b-48ac-35be-9f33-2133829e0f75 | -11.7373 | -46.61387 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 66e78d94-a322-358e-946a-635ed5315afb | -12.64171 | -44.8602 | 2025-09-13 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84690ee4-cc57-31b0-9ccc-80ef51513207 | -9.50039 | -46.42887 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d084bf94-784c-355e-be80-617b5fe167bb | -14.6122 | -46.33337 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 787c35f5-3f80-33c7-b1de-44b28ab46164 | -10.69619 | -48.6638 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 928493d0-f12d-3983-8562-c6f635202453 | -12.08896 | -44.89427 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0fc9f6b-75c6-3012-b997-7c4a493d61f6 | -11.85973 | -50.58447 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 84a1dc70-af28-3422-aade-6ceaf1496ddd | -14.43273 | -48.43257 | 2025-09-13 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09af8bf5-10f7-3773-9a25-62d16738524d | -14.34241 | -46.61341 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 311ddf65-cd0d-31a5-a8a5-f4fc32b6a8ca | -8.08877 | -44.51212 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61a46bd4-535d-32eb-8651-e868279efdae | -9.01141 | -45.77908 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b62b2ebe-f7da-3cf8-b056-e5b1417350ef | -14.19677 | -46.23765 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6fe03f30-68df-3465-a477-65951cbe452f | -10.3381 | -48.81526 | 2025-09-13 04:08:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c2ec6712-e6d5-36e1-8578-e8991ba1c399 | -11.61779 | -46.60832 | 2025-09-13 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d87ab3fd-6081-3f2c-990d-6dbf7e79e920 | -14.17194 | -46.25423 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 27548a9a-a429-37ac-bf82-74b397359f79 | -12.0967 | -47.5767 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c27cfdcc-8b10-3c1b-aa62-3a15e53cd261 | -11.85032 | -50.55953 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 654abbb0-e1b0-3e75-a616-d9f26f42706f | -10.79143 | -44.78345 | 2025-09-13 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7291a1d-908f-3c27-a715-45d86302ada0 | -12.10578 | -47.59415 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ea1779f-f80c-3495-90f1-f4453c3553e2 | -14.21309 | -46.24932 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb772a25-9831-375f-972f-b4aa0c078cb5 | -13.24875 | -43.75397 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 887bcb2e-1e0a-376b-807d-fed970cea346 | -14.28745 | -46.06813 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4f72f75-5f37-3d0b-acff-822e6391e472 | -11.74396 | -46.61987 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20865915-eb10-33cb-a304-f1354960c163 | -14.29803 | -46.06995 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5f9c961f-ec37-3bc7-a285-57ee67c07ca4 | -14.21739 | -46.2671 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ac732ef9-630a-30bd-a9ff-1f3812905c69 | -13.32853 | -43.10186 | 2025-09-13 04:08:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 77bcf4c6-088a-328b-b118-dcb0dbe24265 | -13.45371 | -51.78362 | 2025-09-13 04:08:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 573d3717-6bad-3a11-9da6-98df883b20b4 | -10.78653 | -50.54656 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 2601446f-4c22-3adf-a628-ca8d8ba58db5 | -10.16351 | -46.16324 | 2025-09-13 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86d76dfa-d183-3c39-a6ee-4fbae643ce4f | -13.13213 | -47.13098 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ce8ce09-8016-3f7b-969c-d712f2bb2ab9 | -12.10849 | -47.57885 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 406ce7da-e7b2-3c1b-9426-6fe4f11f5c43 | -10.77846 | -45.99231 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6b8d3fb-c20c-3b28-8f9d-cde1658015a7 | -9.13404 | -40.23996 | 2025-09-13 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4a4d9f84-3f40-3036-91b1-cda28587ae79 | -13.5066 | -40.5593 | 2025-09-13 04:08:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ba3f3d3e-f9eb-35d6-a78c-c072fe49e9bf | -10.38162 | -50.49021 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7452a30-6adb-3b81-af14-7981bf0d0d1e | -12.58277 | -45.7015 | 2025-09-13 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 184f768e-868e-3914-bdcc-086200792c13 | -8.40877 | -47.26479 | 2025-09-13 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d79c08ba-ace5-36ee-ab68-c6970263c52b | -12.96299 | -54.74649 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7374149-babd-3c2c-8782-b110f4ab0508 | -9.23555 | -51.24706 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 503d83f8-3767-3ecc-b8fc-31af85a28bf2 | -14.21453 | -46.26233 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9627ac7-892e-3181-92b7-330f4f1dd02c | -14.19119 | -46.27019 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ec659f43-5929-39f1-a682-12480eb31ae1 | -9.00626 | -45.76418 | 2025-09-13 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33b0e0a2-547a-3def-b81c-db17ef9f99c9 | -11.08055 | -48.43894 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5b75238-c1b6-3eed-b36a-1319c58f5e19 | -11.56514 | -50.578 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 402b5b00-665b-325d-80d6-c1a57aa54900 | -11.42576 | -45.61789 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d457abea-be22-3581-92ae-981641cb3116 | -14.28813 | -46.06404 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eebb21f7-a06f-3323-bfd9-87d9575769ce | -9.51241 | -54.68485 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 743af319-0be2-3a13-b761-a8b7129a7c4f | -9.24021 | -51.25134 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12f0b863-c7f7-30ad-abb5-f3cb7b4df87d | -9.4964 | -50.88377 | 2025-09-13 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ad93c65-69bf-3f4b-930c-bc26c58d4c56 | -11.72864 | -46.59722 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aff6a83a-a1da-3972-8198-d61938d27210 | -12.99626 | -46.75336 | 2025-09-13 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 740e6f1b-3a3b-3e43-a7d2-8edcbc0b5c05 | -9.65021 | -45.81313 | 2025-09-13 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c70040c6-d05a-3957-9507-12cee016b89a | -10.07906 | -48.18074 | 2025-09-13 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29c98c4f-50fc-33d3-a2d3-d7f83139f0fd | -11.37242 | -43.50334 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d86e388-aacb-3138-8244-0aeaecee6c0c | -9.02235 | -47.0418 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ed0012f-f271-3d69-b41f-f06ca514923a | -11.1812 | -51.43135 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a1172e98-291e-325e-a7ce-aa66b76861d2 | -14.18265 | -46.2772 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| c977572a-5dd5-34c4-8a4e-db23ca3208bd | -14.13146 | -45.37934 | 2025-09-13 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e49cbae1-0de5-3090-80e4-4a2f92174500 | -11.43612 | -43.55399 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8dc0ab8-c3f3-3929-954f-f52f51974f3b | -12.1177 | -44.84795 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 391186b2-9207-3fde-a34d-bb62e7a2aed8 | -10.50723 | -51.52922 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c61567f-dfcb-37ce-898a-e1e427650800 | -13.72789 | -45.42332 | 2025-09-13 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fdc4baf1-9aba-3956-b193-f28993ed5af5 | -14.29029 | -46.07283 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2b054be8-2b84-35b2-b15a-c44a1c07454d | -9.58717 | -40.59566 | 2025-09-13 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1a1793ba-7a49-3749-be43-171a35a8cd33 | -10.50662 | -51.53528 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d7dc685-1e4a-3eb2-bb1a-a63bde42a713 | -9.89516 | -51.8638 | 2025-09-13 04:08:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2912e0fc-6840-345a-8b6f-7289d22ab2fa | -14.17266 | -46.25003 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f8a94f60-3a04-3674-9356-ba9a0b6b5aa4 | -10.74759 | -50.49841 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6b3bfceb-02db-34f1-8665-65487d1cf795 | -11.84454 | -50.56392 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f25446b9-ff23-34e3-9220-e2f85555a681 | -7.39057 | -48.17448 | 2025-09-13 04:08:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f564d8f4-c9cd-3618-a589-d5455dbacfe7 | -14.17621 | -46.27201 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 40.4 |
| eb100dc0-992c-39df-9866-831c176d113a | -9.96708 | -50.30257 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 074771e1-d280-354f-94fd-91da56ff7fc1 | -9.82418 | -48.90635 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff38f93d-443f-34ad-923f-d72bad902860 | -15.05775 | -47.99308 | 2025-09-13 04:08:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 46fbe547-771c-3800-b002-870667a4a226 | -9.50823 | -54.67188 | 2025-09-13 04:08:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9046a52-79b0-3923-b83b-49ae2462028d | -12.80006 | -47.99657 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0dc4657a-6edf-31b2-b7f1-e8a898870c3b | -13.92312 | -48.27168 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f553cabd-1dce-3401-beb9-51e98ccfef76 | -10.37932 | -48.5787 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37063797-f964-3eb4-a5cc-afd13b87dc47 | -13.91627 | -48.27811 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4dcb4a81-05f0-3d6d-82de-a4c2db368de0 | -11.74317 | -46.62446 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f493651f-edf8-36a0-8d5c-f18291f1e8ad | -10.69837 | -48.6518 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc1f3a0c-4285-316f-aa82-1d07f94c39ac | -11.86204 | -46.76777 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3556854e-6db0-33e2-aabd-b53dfcf88f35 | -9.24092 | -51.21745 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README46.md)
