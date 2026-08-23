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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fc1d4ac-abd1-3d35-b00f-0836ed559a1c | -13.17361 | -51.42016 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 061520a2-4dc5-30fc-a884-1c7f1f57d260 | -10.84411 | -50.98 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| de500624-eb89-3d16-81ab-022f7aadf62e | -12.73583 | -46.45219 | 2026-08-23 04:46:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5191edd4-4039-3e73-8d29-a42c3d48e2b6 | -10.70934 | -47.74045 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c855998-edf8-370d-83ac-5738d2db5e47 | -12.84361 | -48.46346 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac5ab8a1-c559-3678-b618-6a4a50f1b38e | -7.56572 | -61.19884 | 2026-08-23 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d992d593-c487-3032-acb4-f07f34abc1cd | -10.51945 | -50.7685 | 2026-08-23 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cf4a7c8-2360-3eea-aec2-f566c87c7ec4 | -11.20233 | -55.04796 | 2026-08-23 04:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8ceced0-65aa-31c2-9851-0711711087d1 | -11.15789 | -54.01358 | 2026-08-23 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 611651b5-e2ae-3774-a716-84b9d023e891 | -8.90267 | -60.55211 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 531e5e44-8f52-31fc-a5a8-4f1fed437ded | -9.42712 | -51.61553 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35bb8885-bfe2-3b6a-b7db-05f3bafb11d3 | -8.90522 | -60.54863 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2a85e69-ac41-3142-95e0-0b5b4ad5ddcc | -9.02224 | -50.73563 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 140c4769-5ec5-3126-ac0a-bc9cc00aa610 | -9.45806 | -56.90404 | 2026-08-23 04:46:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8086e4b7-2b9b-3e2c-a8e1-29a962d26701 | -11.27893 | -50.73977 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08616205-bd14-3155-9067-e8e5517dc7d7 | -14.96894 | -52.67029 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8953fd2c-c42d-3eac-b3b0-f559ea0f2965 | -15.25134 | -52.85684 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 863bfeb1-5329-3884-b0ee-a3f9cf5c150b | -15.64009 | -55.95316 | 2026-08-23 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c99afd7-1ce3-3bef-a5a1-899503d52d17 | -12.22952 | -43.17455 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d72b928b-6e4f-35a7-98d2-e1c26d85fe4f | -13.21067 | -51.43047 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92cf35f0-8f1b-3b1a-9936-aee31bf96de5 | -8.53493 | -54.84781 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32388271-887e-3a5a-93bf-478be1b64657 | -12.73228 | -48.394 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b4fdc25-d5aa-3ebf-b78b-5f946b763652 | -8.96281 | -50.77251 | 2026-08-23 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de93973d-8afc-3be6-b7fb-90900932c943 | -13.43119 | -43.85384 | 2026-08-23 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40ef010e-1711-34e3-94dc-032c2a121638 | -9.44348 | -51.59552 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| da01de68-94dc-32b8-913c-7b20970a1e67 | -8.53277 | -54.83403 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ab08b67-c128-3ebe-b5ba-5f7e055f536b | -12.85032 | -48.4645 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7570d315-a9f6-35e9-8623-7466b086e8a3 | -16.40441 | -51.84553 | 2026-08-23 04:46:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89ba6ac4-314d-3a20-bfb1-9c522e752e7b | -16.06419 | -50.43511 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a73aefad-d764-35cd-ad95-28526780e5a8 | -10.70225 | -47.73222 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aee7b1a0-d03d-3389-b552-4ddd012bb9cd | -7.7831 | -61.43613 | 2026-08-23 04:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a565194a-26b5-3e9f-bb6f-64d4b0f9f2df | -9.17481 | -58.33445 | 2026-08-23 04:46:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 741aab9e-a603-3f78-9efe-f76fd89348e8 | -11.94549 | -45.50314 | 2026-08-23 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68eeb5c1-29d3-3aa1-afbd-cc9169a0fadb | -7.43789 | -59.7967 | 2026-08-23 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9680e9a1-5d15-38ac-8de4-83ac59fd4e92 | -9.06536 | -60.44354 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 308bb049-477e-3596-95f2-5a7c0e94e513 | -11.20731 | -55.04475 | 2026-08-23 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfec506d-e967-388a-bae9-2c593547206d | -9.85552 | -60.11034 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5de744e-1ec3-395d-8363-c8583dd0145e | -11.68217 | -54.58695 | 2026-08-23 04:46:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df147b0f-5753-3de9-9e0f-15467af560a7 | -12.23111 | -43.17287 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ac6d7396-31ba-396c-9de2-6f0227e6a1bf | -9.42563 | -51.61403 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17585b90-a03c-3147-bb85-282976df9e75 | -13.16207 | -51.42596 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d2993be5-7db5-3249-a7e7-17964452abff | -12.2904 | -43.15973 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1450d8f5-679f-33ab-b470-e337624a3b16 | -14.36651 | -51.77761 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28991d18-6c01-33d1-ae2f-84ffecb82abd | -15.04775 | -48.69515 | 2026-08-23 04:46:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 456b4e4b-9829-3ba4-bba0-ef88916975f7 | -8.53646 | -54.81264 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4174a384-747c-3b10-bd18-3735e05b9665 | -9.86102 | -60.11372 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcd8df25-8785-3007-b91c-d5fa217066e0 | -11.44222 | -44.53407 | 2026-08-23 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| caa5f622-e48e-3180-b45b-c2474ae06f93 | -9.01596 | -50.73051 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4784ce22-c945-36ca-8bf4-4c77382af07d | -8.95196 | -60.57946 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 954ae4b8-4739-3751-81b7-49553a6092e5 | -14.14792 | -48.05664 | 2026-08-23 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f65ce1e-328f-387d-a56c-e5a3fb528e5d | -11.93915 | -45.52066 | 2026-08-23 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30fe27af-bb91-3abc-a556-e7c8ee60d8eb | -11.21768 | -55.07502 | 2026-08-23 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 325abade-9c79-3f5f-bc34-c893b9debe60 | -14.13825 | -48.05128 | 2026-08-23 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f91ce00f-a22e-37fc-9338-debfe6193738 | -12.40594 | -42.89558 | 2026-08-23 04:46:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d40c6f3c-aad2-3e26-b0c8-05ba77460a1d | -8.62995 | -54.73933 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c85f14d-d3bc-3251-a873-99a51c021d63 | -13.63707 | -47.76725 | 2026-08-23 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66e08097-5209-3c21-b16c-f2f645983789 | -14.14451 | -48.05614 | 2026-08-23 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59e47082-0d44-3be8-9a14-a6a414f396b4 | -12.85311 | -48.46866 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02ffb4dd-8628-3571-a90e-c9ae7dd1962d | -10.38521 | -50.41174 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbe41379-e9d3-38ab-ade8-8d7f1e82d82c | -14.47225 | -53.01933 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f326e275-05c9-3946-a8a6-31c917fcbc32 | -12.7384 | -48.39883 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4c4279d-bfb6-3c74-a9fc-c81d6a185da7 | -12.26052 | -43.11824 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 91a150d6-e318-3bb0-952a-c66b6f999bee | -9.18651 | -59.45148 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 48e8d49f-3df4-3a3f-b92f-949e0ef0e868 | -14.31218 | -53.23136 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1393fbd7-c57b-3179-8225-e79232255d8e | -20.9245 | -57.59091 | 2026-08-23 04:49:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 378b282e-d9fb-387c-b811-4393a649ecaf | -18.72093 | -49.16109 | 2026-08-23 04:49:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1de536f-d5c2-3ed4-924f-4fd45d039d62 | -21.56799 | -45.44452 | 2026-08-23 04:49:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de306ff6-6d62-399c-a6aa-8295b948ad60 | -17.92428 | -44.3882 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb5806df-d0b2-3a33-9704-af73eebf85fc | -17.21123 | -47.52053 | 2026-08-23 04:49:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49937bc0-21cb-3ef9-9906-780323885cfa | -17.91739 | -44.40776 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a5d91f4-0ae2-3076-914f-97656bcaf752 | -18.52391 | -47.15995 | 2026-08-23 04:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22c390d8-8b7f-3c76-940e-de6e5e51ea59 | -18.54423 | -54.75367 | 2026-08-23 04:49:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a3ff8c33-9b32-32a5-8971-be5f352a7228 | -17.40636 | -48.11581 | 2026-08-23 04:49:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 813e166d-d55a-3a52-8763-e5bf080cf2b7 | -19.81841 | -46.93278 | 2026-08-23 04:49:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68e4dd72-8ba3-3b38-897f-bce8d868375e | -20.65812 | -46.56874 | 2026-08-23 04:49:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be2488fc-ab58-3bff-bbdc-5aaa4ef0623a | -19.4628 | -46.8153 | 2026-08-23 04:49:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11b19041-d152-3834-8fc5-f1b12a42b9bf | -17.75077 | -47.03411 | 2026-08-23 04:49:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0fbf2ba2-2f95-3902-b4de-d0676eb7f374 | -21.45108 | -46.14537 | 2026-08-23 04:49:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| e4d230d9-69ea-3c9f-a210-82a22cb22d55 | -17.59146 | -44.61189 | 2026-08-23 04:49:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e76ed8a-efff-3208-8f44-30b6e1b44846 | -20.67457 | -45.27136 | 2026-08-23 04:49:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3205edb0-a6c5-37f9-9b8f-2b81735fc288 | -18.04618 | -47.28267 | 2026-08-23 04:49:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36f2569f-7a87-3c59-a3b4-cfee739e5bae | -17.92777 | -44.49836 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afc92054-0c25-34d1-bf49-971d24373460 | -20.65284 | -46.57843 | 2026-08-23 04:49:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf3401fa-5f87-313a-8a46-31230f53687b | -17.93211 | -44.49865 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4065e12-16e2-39ca-8ae3-64a52059e60c | -19.80634 | -45.63863 | 2026-08-23 04:49:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26e304d0-962b-3963-8b27-f24fd4fb94af | -18.51742 | -46.60084 | 2026-08-23 04:49:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 374ea415-dbba-3f3a-a894-745872915901 | -16.44888 | -54.67756 | 2026-08-23 04:49:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02fedba1-332a-33d2-b773-3f9edc09acbf | -18.99364 | -46.32015 | 2026-08-23 04:49:00 | NPP-375D | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d6a7992e-89c2-3eb9-9b8b-bf70e4694864 | -19.81455 | -45.63979 | 2026-08-23 04:49:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d39da8b7-3dfa-33cf-817e-6b83fdd38c1b | -17.90942 | -44.50481 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa6a7710-6ac9-30bd-b389-dc75d49e0a13 | -17.79749 | -44.40286 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e645af0-bc48-3dc0-b288-63bacfd4c180 | -18.65225 | -43.57195 | 2026-08-23 04:49:00 | NPP-375D | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aad89094-1bd8-356c-a8c9-76aad697e161 | -17.88524 | -51.67045 | 2026-08-23 04:49:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d566e5a9-e538-3e1d-8dbc-d6fc9cdfe321 | -21.45922 | -46.14648 | 2026-08-23 04:49:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1dff6d82-77c2-3fe0-ab2d-a7a2378bb970 | -17.83984 | -44.46589 | 2026-08-23 04:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 651db9bb-25a7-3432-bbc9-724985c3fd8c | -20.65423 | -46.56792 | 2026-08-23 04:49:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df72a4c7-dac9-3f0a-9f92-d9404339eae8 | -21.3569 | -46.72046 | 2026-08-23 04:49:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c27b896c-efa5-3921-a65a-ceb8047c3817 | -19.65008 | -46.04853 | 2026-08-23 04:49:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4650497c-561a-3c66-81af-e339593b23e1 | -16.57593 | -51.62971 | 2026-08-23 04:49:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e580f51-37c4-37c0-a07c-dadcd92923e0 | -20.49032 | -47.12755 | 2026-08-23 04:49:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README38.md)
