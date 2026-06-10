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
| bba797b1-13c8-37f0-9552-257c470d7cfd | -3.50202 | -48.03782 | 2026-06-10 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a692b583-7d41-3bf1-ab08-821f67a4f5cb | -3.50652 | -48.03392 | 2026-06-10 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 62c06613-15f8-3921-b9cd-30d77b010dbe | -3.49375 | -48.03872 | 2026-06-10 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33d3ee84-c4b9-320a-b726-c05e54312f95 | -3.49752 | -48.03926 | 2026-06-10 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 142a217d-1a22-30e6-9db6-7d979c5eed30 | -3.50578 | -48.0384 | 2026-06-10 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03546187-9ea8-348a-85c9-b6ed47150da9 | -3.50275 | -48.03337 | 2026-06-10 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e475c066-66f1-39a0-9bdb-f655bc5940ef | -3.50128 | -48.03984 | 2026-06-10 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8155c261-d0fc-3661-a39b-be61b5e141f5 | -3.50504 | -48.04043 | 2026-06-10 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5eb2ae39-400a-3de1-9c7b-562c9858b7b2 | -3.6129 | -43.13536 | 2026-06-10 04:27:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2c65110-0bcb-3b57-837b-e0ab75c75383 | -3.76174 | -47.50389 | 2026-06-10 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21becf52-0f16-3d85-b46a-1cb40786e5db | -4.95667 | -37.53781 | 2026-06-10 04:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 565e76b8-2aea-3bef-a99c-690fa9fbc652 | -9.22251 | -48.56653 | 2026-06-10 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9818ffaf-d59a-3904-b6cb-9af34a11f3bc | -6.39186 | -44.17417 | 2026-06-10 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7afeea72-364b-3469-a5dc-ca70042d7b10 | -7.10163 | -46.51934 | 2026-06-10 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ed6e4df0-8725-3f6a-bf47-5608056b7247 | -9.74726 | -47.8816 | 2026-06-10 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fbd0aa2-718f-39ee-9e40-cc11c3c7ca9b | -4.42988 | -47.73156 | 2026-06-10 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbc2fc7b-4c4b-3a52-807d-77622c1feba7 | -9.30098 | -45.47345 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 08a88a42-0830-3c12-b2ac-59f52c4d4f2b | -9.30653 | -45.48152 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52f972a4-639a-3659-8d8d-4c64d8959075 | -9.22183 | -48.57062 | 2026-06-10 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a60f265a-6567-3e11-a90c-16a4167166b5 | -9.1416 | -47.98752 | 2026-06-10 04:29:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55a95394-d446-3e4a-a017-be4345d307b2 | -5.9314 | -43.48509 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ddd4a576-73c8-37ee-b381-ac1e261b13b0 | -5.83044 | -43.59446 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 89a95a10-0b41-3ab3-b48e-afccee0e62a1 | -5.79984 | -45.11447 | 2026-06-10 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 674499c0-2986-3fb2-a802-321ce1369c81 | -9.29821 | -45.46942 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4f3e46f6-a22d-31e8-8caa-3b1302c87203 | -7.72413 | -44.16468 | 2026-06-10 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2dcae25-12c9-3419-a769-c7cfa54da687 | -8.97647 | -47.98137 | 2026-06-10 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63555089-d58d-3371-8050-5767f1ef404c | -10.70304 | -44.7898 | 2026-06-10 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77e0f5db-5799-3fad-a6ce-9232814f1ef3 | -9.31929 | -45.48716 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 8ac4e1c2-7297-35af-9e29-d7143c4106df | -8.29566 | -48.23597 | 2026-06-10 04:29:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ce01514-8d8f-342c-8ca3-1e81f7d3b9d4 | -9.34165 | -49.15018 | 2026-06-10 04:29:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c847fd3-5239-34ad-9dd6-bd4d1f7b6fcd | -9.08353 | -50.60103 | 2026-06-10 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5275d5de-f270-35df-a410-923923132af9 | -5.30037 | -47.24384 | 2026-06-10 04:29:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dc0acd4-9a52-3c3a-a07f-4ce0fb0ab453 | -6.39746 | -44.17178 | 2026-06-10 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c58d8d6a-c94f-30aa-b83a-e99b581f9acd | -7.67347 | -55.00936 | 2026-06-10 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6eb7ffe0-efb1-3d60-acb7-11e87ceae5b2 | -6.56875 | -47.91241 | 2026-06-10 04:29:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3c985aa-fe2b-3ce2-badf-ec4a278693a6 | -7.1028 | -46.51208 | 2026-06-10 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| dd5a3232-c382-3d2e-9640-f84986536273 | -9.31652 | -45.48312 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 2bdbf711-1a5a-3a80-b157-593bfdab6807 | -7.7568 | -47.58361 | 2026-06-10 04:29:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32a2f2c5-c34e-3be4-897e-608f63a303f4 | -8.29634 | -48.23187 | 2026-06-10 04:29:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28d51c75-89ba-3209-b665-94dd9309bed7 | -5.0419 | -43.26374 | 2026-06-10 04:29:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 514ac7c0-4956-3d47-9944-db9fe0f3e503 | -9.44112 | -47.63987 | 2026-06-10 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7b63662-8bac-3b33-b58e-4632d0ee5da9 | -9.29488 | -45.46889 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 92ee7fd3-c932-3508-b75a-76bce669fb48 | -9.31874 | -45.49066 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68305f66-70c1-31a0-a5e6-d58dbcbea5a1 | -9.11285 | -47.9628 | 2026-06-10 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03ec474b-00b1-36e3-8470-1f9f764e720e | -5.93535 | -43.48202 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5194893a-b173-3f2e-9dc8-f0d624abfb2d | -7.0994 | -46.51154 | 2026-06-10 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad3ba59c-cf42-3950-a7d4-02c064695e48 | -6.95728 | -44.55375 | 2026-06-10 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e4a29460-636f-365d-b786-5ac348122f0d | -7.99133 | -46.04966 | 2026-06-10 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1190446e-3aca-303a-b052-f2c230f9c17b | -10.66631 | -44.46491 | 2026-06-10 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46296331-7bc8-33e0-9cc2-a93d61daa4f8 | -9.32262 | -45.48769 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 36ada2a6-c7f2-3532-9fed-d692ffd0dd10 | -8.97998 | -47.98193 | 2026-06-10 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1492e01-0d33-36bd-8d44-da663fd2c3da | -9.29433 | -45.47239 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f9cb1e6-04c6-37cd-b5ba-556fafd2b09e | -9.30043 | -45.47695 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 477b38fe-5011-3a10-98bb-5f287b94e9e7 | -9.07949 | -50.60028 | 2026-06-10 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f0acc9d-38cd-32a5-9b0a-e50989e94e4d | -5.94154 | -43.46459 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa06c0d4-1d2c-388e-8c6c-4db12453e8f1 | -9.31439 | -48.97492 | 2026-06-10 04:29:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84c6c2a9-629a-33dc-93b7-8bd41a0fc58b | -5.72885 | -49.09719 | 2026-06-10 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16b4d3ce-a560-3516-b443-e7779c5fcbd0 | -4.57285 | -48.02575 | 2026-06-10 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71699fe6-2972-3123-bf95-4e21770228a3 | -9.12923 | -49.65488 | 2026-06-10 04:29:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dea51208-1b61-330d-a25c-3e0abc88402b | -7.15914 | -44.06626 | 2026-06-10 04:29:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7559667-32e6-3a10-a03a-9f978fee3dc2 | -5.84055 | -43.48619 | 2026-06-10 04:29:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87440eb9-0bc6-34fa-8b5b-02c4cb6b7669 | -9.7479 | -47.87775 | 2026-06-10 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6bad1d2-96f6-3c25-aee2-983bc8eef0ce | -7.34978 | -45.04062 | 2026-06-10 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e14c4d83-f10c-3fca-902e-2a2fa48e5324 | -5.76328 | -46.04398 | 2026-06-10 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a7240f5-8409-30c7-87d6-de841f5d37f0 | -7.16194 | -44.07032 | 2026-06-10 04:29:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f97a03c8-bf19-3f70-8b99-c1138e4b45e3 | -9.77404 | -49.75165 | 2026-06-10 04:29:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b4e9c8c-b904-35c9-be25-ad07f3453a3d | -9.14188 | -47.98363 | 2026-06-10 04:29:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 71ba69f5-a9fa-326b-bce7-ee0bc9e2b5e3 | -7.09882 | -46.51517 | 2026-06-10 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0781fa7-c5ed-352a-8a18-d84ed25e5b17 | -5.73273 | -49.0978 | 2026-06-10 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1870edaf-9caf-3c6b-94bb-2855b448856d | -7.91137 | -47.08204 | 2026-06-10 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32f7c6ae-3dc0-342c-b849-4828867b48d9 | -9.14226 | -47.98359 | 2026-06-10 04:29:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8e59ca38-888f-3c3b-a299-c50b83a26386 | -8.44264 | -49.70931 | 2026-06-10 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acea03fa-acb7-345b-9e96-286b1828b4e1 | -5.41586 | -43.90285 | 2026-06-10 04:29:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e09b2acd-6e15-3eeb-8bb0-3af3ded0dd31 | -9.75074 | -47.88216 | 2026-06-10 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6fdcc4c-7107-3474-a0df-6fefdd37ba4b | -9.30376 | -45.47749 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 738c022c-41d9-3a11-bed4-9d0c1a1aa1e4 | -9.31541 | -45.49012 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fac45152-b015-3ba0-a42d-20fac4f6e264 | -9.31146 | -48.96994 | 2026-06-10 04:29:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 326c8ca3-a02c-389f-845a-46dfaa3e4099 | -7.09824 | -46.5188 | 2026-06-10 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8401e4b2-c0e5-3ba6-88bd-1633f8e14025 | -7.98798 | -46.04913 | 2026-06-10 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8653cb4-da84-3d56-800c-d4c241e2bd16 | -6.86361 | -45.03838 | 2026-06-10 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58e403c1-3c0c-3b00-ad89-c0cbf0817e0a | -9.31042 | -45.47855 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| fcdc6e81-f550-3ec3-9961-44325707db0b | -7.71915 | -44.56919 | 2026-06-10 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38fc0a51-162e-3ccd-9f8a-fc4a25f6e5d0 | -6.44191 | -44.57953 | 2026-06-10 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caf05afb-996a-3045-a857-5d5ed1df7803 | -8.99842 | -45.73649 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 667d3fbb-bc72-3158-aaaf-65845d05eea6 | -9.44458 | -47.64043 | 2026-06-10 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 740718ea-ddbf-3da4-9b2b-4f6226b55a50 | -5.93196 | -43.48151 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca07da36-a89e-3d0f-b0cc-d224df1ed3b2 | -5.82425 | -43.58986 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 713e5e44-0809-3e9b-835a-33b91f44e1e0 | -8.29923 | -48.2366 | 2026-06-10 04:29:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b610007-adf9-3820-9084-d67888fe3adb | -9.31319 | -45.48259 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6590352a-1352-32ea-b59a-67c292e2bd34 | -9.32207 | -45.49119 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9df24a47-5a03-3deb-8061-16d08d7fd2bc | -9.14168 | -49.83859 | 2026-06-10 04:29:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cd4fee9-0157-3ef2-bc08-b5dbe09e580b | -5.93084 | -43.48868 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d0f7d660-7b4b-3363-b46c-51e1eca16677 | -9.31597 | -45.48663 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 1457a173-15bf-3173-9e00-bb79419fe839 | -7.26784 | -46.81168 | 2026-06-10 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9759078a-8bc2-3897-ad2b-bcd4712969cd | -9.31985 | -45.48366 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 6ca9bd44-bd2e-383e-a266-13a6d0a793dd | -7.98742 | -46.05265 | 2026-06-10 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 196cd8a3-c785-33f1-9650-28e383a02c11 | -9.29766 | -45.47292 | 2026-06-10 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a41561f7-a8f3-334f-bb11-dabb7549a293 | -7.30137 | -43.56134 | 2026-06-10 04:29:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 26703048-8645-3ec2-afe8-aa19dad6944f | -7.90794 | -47.08151 | 2026-06-10 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdbaf93f-7d97-3717-855f-4ca986b4d913 | -5.93422 | -43.48919 | 2026-06-10 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README7.md)
