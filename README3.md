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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebe555fc-6398-3d89-802d-1048c59b50de | -20.13421 | -46.85174 | 2026-01-11 03:21:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6c89f1c-9fdd-3999-871a-7e2f97079c99 | -22.89281 | -43.65862 | 2026-01-11 03:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f6d0e1cd-c125-3fde-8703-4f9a0ce1089e | -18.70594 | -40.00666 | 2026-01-11 03:21:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 42a373c6-dd83-3ae8-8ce0-71a2ac2928b9 | -20.23592 | -46.4958 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4c5d22cc-f636-3194-80fa-99e61b1e7c75 | -20.23633 | -46.49434 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6f40cbcb-57fa-3665-b355-6717ccd65103 | -20.24621 | -46.51305 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5c5d4b5-f650-3ddb-9af8-2da9736bbdd4 | -20.24256 | -46.49827 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1cf327f7-ad91-3864-b302-d45b6b2bb6e6 | -20.23803 | -46.48756 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 868d0370-7f97-36ba-954a-5b758ed41fea | -22.89672 | -43.6595 | 2026-01-11 03:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1068e79f-7cca-3483-945d-b69f4924cb25 | -0.27161 | -48.78591 | 2026-01-11 04:06:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8e93bbac-5001-33c7-b113-dd2af8fa67fc | 0.72676 | -51.41801 | 2026-01-11 04:06:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b77b65bf-fb9f-35f8-98a1-8fff77a4b86d | -0.27209 | -48.78289 | 2026-01-11 04:06:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 605f4cb8-af5f-32df-965e-01fd949ee5d7 | 0.72747 | -51.41796 | 2026-01-11 04:06:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca1fc44c-b21e-3426-905c-497fdbd76794 | 0.73293 | -51.41698 | 2026-01-11 04:06:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c940511-b4bd-3bad-bfe6-4a87a45aceac | -0.27113 | -48.78893 | 2026-01-11 04:06:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 06e74739-77cb-35d4-84c7-f50267c48172 | -0.08783 | -51.27864 | 2026-01-11 04:06:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 53145a87-b31b-3eeb-894b-7611865d9dbd | 0.72672 | -51.41326 | 2026-01-11 04:06:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 121fdd08-05e3-3759-9eea-a3cfb2a6e36c | -5.28578 | -45.82696 | 2026-01-11 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a76ba139-fa05-3b05-89f8-b83e119eb0f4 | -5.24996 | -37.50283 | 2026-01-11 04:08:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3fe8052c-23a9-35fe-96ff-238e50995ba8 | -4.65371 | -45.79948 | 2026-01-11 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 521d6287-41c0-30fc-adae-29e8fac768a1 | -5.48269 | -45.43554 | 2026-01-11 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c3cfbeb-1b46-3a4e-95aa-c940903ad8dd | -4.81429 | -37.75505 | 2026-01-11 04:08:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 430f4b32-d159-3314-8c2b-4aa1197f5b40 | -6.64164 | -46.54066 | 2026-01-11 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1a9eec4-f537-3a3f-b06c-f915e06d1a6b | -1.2662 | -45.73978 | 2026-01-11 04:08:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b72bacf2-a558-3ee7-a866-b6dadb5b0bfe | -3.6785 | -42.06087 | 2026-01-11 04:08:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3aed9d2e-3644-358c-9006-ba3e9a9bd104 | -1.65302 | -45.90863 | 2026-01-11 04:08:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 289377c4-7c60-3c08-b1e3-27d494fcec0d | -6.31234 | -43.81397 | 2026-01-11 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 286e6897-bbcc-3877-bfd7-8ec42c244dd9 | -5.49753 | -42.15583 | 2026-01-11 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1ff8293c-5a2e-3789-85fe-28b417644dfe | -2.87193 | -45.21117 | 2026-01-11 04:08:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 223c2eb4-6c5a-32b5-b0d5-2efeffc51b3d | -2.89167 | -45.22244 | 2026-01-11 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca9e9146-3008-3cf4-b28e-6220d0aaca5f | -3.35833 | -50.19015 | 2026-01-11 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cee4f299-ffd8-3fe8-8295-5f83301e98db | -2.86807 | -45.21055 | 2026-01-11 04:08:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4abb991f-959b-3458-a23a-a2ce9fea2422 | -8.49624 | -39.92921 | 2026-01-11 04:08:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c0d37d51-159c-3508-b95c-4166ed329f0a | -3.55816 | -43.65813 | 2026-01-11 04:08:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82ee1048-70f3-3ef8-9953-4106597285d4 | -5.01794 | -41.87325 | 2026-01-11 04:08:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6269a4cb-d835-35bd-873d-c8760e81dc7e | -5.49975 | -42.1633 | 2026-01-11 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| be00d138-a2d1-31fa-958e-3ad79954a333 | -5.52752 | -42.85043 | 2026-01-11 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 840cbfa6-1625-385f-ae97-6da5ec34d758 | -3.35887 | -50.18681 | 2026-01-11 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37e7ed96-7f45-3f48-8110-c1b08a26c0b8 | -5.83747 | -35.64344 | 2026-01-11 04:08:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c06c33ca-8223-39ac-8694-163a8a70827d | -5.29428 | -43.74126 | 2026-01-11 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 767e4a41-8074-3448-8216-599b4f07e8b5 | -5.01518 | -41.86927 | 2026-01-11 04:08:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 54d2977c-ed08-3644-9565-1606044f6424 | -8.2044 | -46.08755 | 2026-01-11 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bae9122-85f0-3b6e-9277-1d511c650f3b | -9.32131 | -37.32027 | 2026-01-11 04:08:00 | NOAA-21 | POÇO DAS TRINCHEIRAS | ALAGOAS | Brasil | 2707206 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 113fec28-7f59-35e1-b7ac-1fa9f4078742 | -7.4929 | -45.57901 | 2026-01-11 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 943f2482-30c4-3bc8-921e-ac5ecf168fe9 | -4.68606 | -41.23483 | 2026-01-11 04:08:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7832081d-3b7e-35be-a46e-cddf61a4567d | -2.19066 | -52.01433 | 2026-01-11 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f9660e2e-2b8c-3c53-b07c-1cbc63114cb0 | -4.50276 | -46.10534 | 2026-01-11 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f9f05ec-7969-3156-ac49-0a18286ee694 | -3.91113 | -40.84182 | 2026-01-11 04:08:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f775a357-e010-3c02-ab2e-2615d132b10c | -6.6432 | -44.68967 | 2026-01-11 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25d2ff56-b7dd-3a90-aa5c-d2504f82ec2f | -4.96061 | -43.00178 | 2026-01-11 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7701b698-d9a8-306e-aed7-3f6dab7cdc86 | -4.81608 | -45.23333 | 2026-01-11 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26d1d997-6053-36f7-9e59-8598a88f18c8 | -5.28966 | -45.82755 | 2026-01-11 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f937b41a-f109-3601-a781-8babe585444f | -5.49506 | -40.73967 | 2026-01-11 04:08:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3352074f-8f91-3bd5-8515-c509dc72c242 | -5.15116 | -40.95908 | 2026-01-11 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8558187e-798f-3140-bf8d-ea5536994d50 | -3.55465 | -43.65756 | 2026-01-11 04:08:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0968805-3c98-32ec-aceb-55a2a8f6b577 | -4.86652 | -37.63338 | 2026-01-11 04:08:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fe2bf7b6-efbe-3e9c-b507-3daf4bd1bd29 | -5.49698 | -42.15931 | 2026-01-11 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| df216acf-98bf-34b7-a943-0813f1203e62 | -4.40699 | -40.69358 | 2026-01-11 04:08:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d94ba2b-a99f-312c-8db2-ae42d67babd6 | -0.96758 | -46.96585 | 2026-01-11 04:08:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab5f9585-85c9-34d9-bb72-c435964b82f5 | -9.97681 | -36.36462 | 2026-01-11 04:08:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5e7874ff-c074-3818-8768-2a0a8a8ca347 | -2.87009 | -45.20919 | 2026-01-11 04:08:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a4a0aea-4ad7-3719-bc59-0dec4fbfdff4 | -5.46169 | -45.28299 | 2026-01-11 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 44532ff4-2dee-3902-98cd-46d1db023efe | -5.10477 | -37.59357 | 2026-01-11 04:08:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 090158c6-f03b-39c0-81d1-48d7e687b720 | -6.02272 | -44.54886 | 2026-01-11 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f148f597-be54-3155-a880-c511dcfa31d3 | -2.18517 | -52.01067 | 2026-01-11 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e0303e60-0ddd-3235-bdb8-b01ce781d8cd | -4.95955 | -43.00117 | 2026-01-11 04:08:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d4c7c57-3696-3e2a-89ee-2fa87f8f9ebe | -4.14344 | -38.27223 | 2026-01-11 04:08:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2f2d2789-a060-3a94-b035-cb935a34289a | -9.97453 | -36.36634 | 2026-01-11 04:08:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 4d010a87-4a5a-345f-bd66-bbe62fba6248 | -5.84174 | -35.64406 | 2026-01-11 04:08:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 93112db7-8608-38e6-a56b-8a62c9dddc05 | -4.66097 | -40.41727 | 2026-01-11 04:08:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ab92b7e-28ed-3389-b9ff-439998e15a54 | -4.70708 | -44.48186 | 2026-01-11 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf1a433e-3c3c-3156-ab7a-8b6a49c34cbb | -8.16419 | -44.46303 | 2026-01-11 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81616755-d82d-3d71-b73c-52dd88f0d298 | -2.87001 | -45.23384 | 2026-01-11 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1be1dc6f-3bdc-3b52-b061-9c7529fa185e | -5.5302 | -42.84704 | 2026-01-11 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 899cc94f-0c57-37ef-8d03-e7d3fbc94212 | -5.52962 | -42.85061 | 2026-01-11 04:08:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c9922a28-c228-36d9-943a-931ad30f307e | -7.49216 | -45.58344 | 2026-01-11 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74bc6d62-dea5-3c0a-9e3c-7016c36a3c64 | -5.49643 | -42.16278 | 2026-01-11 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 60bbbda6-c4e7-34ff-8c0a-bbdba1322b4a | -5.76508 | -43.92059 | 2026-01-11 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30a9cc0a-ca8c-3681-8655-676852b9d264 | -2.1913 | -52.01169 | 2026-01-11 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c5195616-b17b-3d7c-9e96-ddd4cf53d5f2 | -2.87159 | -45.22422 | 2026-01-11 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9e456a3-2a73-31b6-8ace-f5fac236c3f4 | -1.05792 | -47.13329 | 2026-01-11 04:08:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd92844a-b924-324d-92a2-e212ef164954 | -3.55113 | -43.657 | 2026-01-11 04:08:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4b2355f-5043-3dcd-807b-971eeb8ed2a2 | -9.97622 | -36.36876 | 2026-01-11 04:08:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 17e52db1-9778-3e7c-8301-03c9aa89aad1 | -3.55879 | -43.65422 | 2026-01-11 04:08:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdbb4cdd-c019-30d8-8159-6c8c2d6e06a0 | -3.64348 | -42.02311 | 2026-01-11 04:08:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 815e9ce0-de57-34e5-b980-618855f44a6c | -4.6506 | -45.79409 | 2026-01-11 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d127b26-914c-3f9d-91d0-1e6ad303669b | -1.65244 | -45.91232 | 2026-01-11 04:08:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21a4234e-9e2c-3675-8aa8-3e3a1996a692 | -2.52245 | -43.26192 | 2026-01-11 04:08:00 | NOAA-21 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ba4023d7-6304-3d02-b272-a35d628e6b91 | -3.94032 | -40.69824 | 2026-01-11 04:08:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c902fe9b-415a-30fa-a899-bb8e694d4dc4 | -3.93701 | -40.69773 | 2026-01-11 04:08:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f3a3d34e-f3d8-3e9b-adc2-596cdc0d8592 | -4.44131 | -38.93084 | 2026-01-11 04:08:00 | NOAA-21 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9cbceb47-9a33-3f9c-a9d8-1e835000e968 | -5.49837 | -40.74018 | 2026-01-11 04:08:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dbf85cd1-6186-374e-af5c-cd234a39fb2e | -2.61957 | -43.10004 | 2026-01-11 04:08:00 | NOAA-21 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dce6f172-31c3-33cc-89b3-9b98494e1751 | -6.68725 | -44.70509 | 2026-01-11 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74164bd6-345e-3b0c-bd5b-fde9cbf70b12 | -5.5003 | -42.15983 | 2026-01-11 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6e29b702-635b-3ce2-a67c-a5207432d5f6 | -3.55753 | -43.66204 | 2026-01-11 04:08:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03786aa9-9094-35db-ba6c-b2d573074565 | -7.59958 | -45.8903 | 2026-01-11 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 300f677b-5ecb-3af7-a013-ca1eeb05f233 | -4.66179 | -40.89305 | 2026-01-11 04:08:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fe925ad3-0029-39a5-b268-a84c2891d2ac | -5.24621 | -37.50227 | 2026-01-11 04:08:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 857039b3-2734-3457-833a-8f19e6e425c0 | -4.92341 | -37.40863 | 2026-01-11 04:08:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
