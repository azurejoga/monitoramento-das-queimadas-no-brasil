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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54a7843d-0d2f-30d4-9a60-e3348e3e4e8d | -10.7463 | -50.6172 | 2026-09-20 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 1de0944b-2130-341c-9b38-966e6fc9a267 | -11.398 | -51.418 | 2026-09-20 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 224.0 |
| c0a5856b-9772-3eec-9564-a37a1437b188 | -7.0286 | -45.2554 | 2026-09-20 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 2f3719e0-5d87-358c-9c6f-b124b4d78fd5 | -11.7823 | -49.8152 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 1ac40437-d6c0-33b1-90ba-438cc4d711a5 | -10.2598 | -50.2624 | 2026-09-20 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| fd68cb5f-9da1-3094-b350-85d1b14424ab | -11.0506 | -54.9309 | 2026-09-20 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 246.1 |
| d3251c59-1e13-3aae-8fc6-72c4a47887f9 | -14.912 | -49.9132 | 2026-09-20 14:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 0a0c9d61-fd77-309f-88dd-1b0c55c3232a | -11.0407 | -54.1772 | 2026-09-20 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 173.8 |
| 0aa5e634-8027-3fff-9a1d-e5f8eb4439fb | -13.9448 | -47.8494 | 2026-09-20 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 3bc8e503-7196-30ff-87ea-fbf4cfca9a71 | -12.2341 | -50.1703 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 0e113b4f-d666-3c4e-ab26-73eadee0e0bc | -8.4737 | -47.0053 | 2026-09-20 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 667280ba-edbd-3185-b33f-bd23e1b7b84d | -10.473 | -51.2808 | 2026-09-20 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 284389b6-f9ee-3176-bdbf-95716034460b | -8.4611 | -57.6292 | 2026-09-20 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9c2a794f-0882-3f3e-9ec0-21a50021dec3 | -3.3866 | -59.5797 | 2026-09-20 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 60674551-5e59-3f45-9958-d378ff52396f | -3.4049 | -59.5794 | 2026-09-20 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e7941919-d596-33cd-b95d-60f2c3bb417a | -6.9851 | -45.8235 | 2026-09-20 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| a4901f36-9515-3e53-93de-f09c3e43330c | -10.9665 | -49.7583 | 2026-09-20 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| f82899d2-0a35-3f34-8321-ddf9d26c18e4 | -6.4486 | -59.9717 | 2026-09-20 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 290.7 |
| 9a746eb9-3181-3043-906e-9a675aaee248 | -9.6665 | -54.3332 | 2026-09-20 14:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6e3b0694-9d53-34fe-bb58-7331d897c903 | -9.6668 | -54.3129 | 2026-09-20 14:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ce95e675-3c1b-30b1-a0e7-100a176a6b20 | -11.4541 | -45.3662 | 2026-09-20 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| af24fb15-05ac-3b87-8352-4d1eb0b594b8 | -9.2606 | -45.9164 | 2026-09-20 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 09923a76-a8da-3f2b-a48a-93c1d761ec7b | -9.0544 | -48.7469 | 2026-09-20 14:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 207.2 |
| e2ff5e08-f3c1-33dc-a60b-b9ae650bdad7 | -5.7615 | -57.5807 | 2026-09-20 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3927c5e4-51a6-3c16-abd6-4177103089d7 | -10.8672 | -56.1775 | 2026-09-20 14:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 8b9a459b-a28a-3db4-866c-dcc675db9d84 | -11.4545 | -45.3432 | 2026-09-20 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| f2d90259-547d-3d38-9583-837fcffd1486 | -3.2955 | -59.4476 | 2026-09-20 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 6779916f-d38d-3a80-a7cd-57f5a2ff8dff | -9.2563 | -46.2323 | 2026-09-20 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 0cfa7682-0473-3a5c-b9f8-4fd150abab41 | -11.782 | -49.8368 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| ff0a6beb-4b4c-3029-93c9-d4891a501b75 | -9.8397 | -46.4361 | 2026-09-20 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 397.4 |
| 5af1f168-0456-300a-849d-fee9d0214456 | -9.2676 | -48.2472 | 2026-09-20 14:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 68e06865-b11b-31b4-8ac4-b14c22038ee3 | -7.3259 | -55.6153 | 2026-09-20 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 200.4 |
| f13d8b99-a651-3f8f-8a28-bbdc1dc80807 | -6.4485 | -59.9909 | 2026-09-20 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 198.5 |
| 579459fd-f17b-3543-afae-20ec0bd2bd70 | -10.41 | -48.933 | 2026-09-20 14:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 77b3abb9-4891-38e6-97da-2989e24b48a9 | -11.9885 | -50.0277 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 9e1b4acc-38b8-3996-9bd9-f2d7b953c0b9 | -12.1524 | -47.0158 | 2026-09-20 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 0ed5d03b-e07e-3d09-9639-ffe813b9c507 | -6.737 | -55.0674 | 2026-09-20 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 09fa2b70-6d7b-320b-a2c3-bae1d2a1b4cb | -8.8825 | -45.9576 | 2026-09-20 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 318.5 |
| 928b198c-5e77-3212-8c35-5404b4276e30 | -7.0098 | -45.257 | 2026-09-20 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 17001407-638d-3d9f-b448-22c6af03397b | -8.4549 | -47.0072 | 2026-09-20 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b5ea6b1a-b859-320f-8de3-fb59bfa62590 | -12.152 | -47.0383 | 2026-09-20 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 196.2 |
| aaa2ed31-404c-3b11-8d42-a58725886d23 | -3.1261 | -61.4077 | 2026-09-20 14:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| eef06021-7f6c-347d-bc5d-09030b8c60fd | -8.0894 | -55.331 | 2026-09-20 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2c75d593-69fc-36f7-a99b-70522b7cddb5 | -7.0262 | -42.0685 | 2026-09-20 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 109.5 |
| 1adb9654-bb31-3d85-b2ec-183e117cbfd3 | -3.4428 | -59.0996 | 2026-09-20 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 8bf5a6fd-bd36-3582-9066-e021defd0177 | -9.2865 | -48.2453 | 2026-09-20 14:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 221cd230-4c0f-3247-a93d-7afaa72f436a | -12.642 | -50.9359 | 2026-09-20 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 3d8f5176-80cd-3a39-b368-0be3c7430fa8 | -8.0892 | -55.3511 | 2026-09-20 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| ef82c0c7-8660-337f-a2f0-ecb12087d592 | -9.0353 | -48.7704 | 2026-09-20 14:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 99dc15e5-706d-3d54-9820-d3479d8e399e | -7.1014 | -42.0849 | 2026-09-20 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 177e1b30-1093-3cda-915d-2a51412d4762 | -12.2344 | -50.1488 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 4f4e7968-1a52-3663-a98a-16b5942ba709 | -7.3564 | -44.4726 | 2026-09-20 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 49067d1d-68b1-3fef-a585-7bb0c0ce180e | -11.0256 | -48.3164 | 2026-09-20 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 80c1aba4-9bcc-30e6-9b20-34227855a431 | -6.4671 | -59.9711 | 2026-09-20 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 9818744b-800c-30a7-8840-2854766c547f | -11.3813 | -44.0554 | 2026-09-20 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 9295259f-6812-33e0-a989-2079d6d35d01 | -8.4797 | -57.6282 | 2026-09-20 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 837a4502-222b-3bf4-bd20-d09949aa7201 | -8.8639 | -45.937 | 2026-09-20 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 156.9 |
| d97a3423-b31e-37d5-a089-626c336dc989 | -8.754 | -44.2589 | 2026-09-20 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 9a6eebbc-add1-3bbe-8180-89fee045b2a0 | -7.5337 | -45.4141 | 2026-09-20 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 1ad2f15f-0eab-37e0-b08a-504edfd150fc | -14.9314 | -49.9103 | 2026-09-20 14:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 108faf50-d7d9-3f9b-9cfe-41de8dfca0b8 | -8.883 | -45.9124 | 2026-09-20 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| a896f5fc-2d11-3297-bb86-45d2959c67fb | -6.4301 | -59.9916 | 2026-09-20 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 6178b304-bec6-3118-acf6-2ad93db94701 | -11.041 | -54.1567 | 2026-09-20 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 209.5 |
| 0d81ff70-6787-30fa-83c6-9a43aeb415ba | -8.4922 | -47.0257 | 2026-09-20 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| be400077-6321-39f6-9021-8e5d87920486 | -12.0263 | -50.0447 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 9422e227-6063-38e4-9ade-a7f2dc2239b9 | -9.8313 | -48.4073 | 2026-09-20 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 174.6 |
| b4ea7bb9-a194-3c6c-8942-92b643d6bdf8 | -3.8255 | -40.6796 | 2026-09-20 14:40:00 | GOES-19 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 119.2 |
| c941390b-6df9-3b09-8c09-4fbca39a555f | -6.7369 | -55.0874 | 2026-09-20 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 164.0 |
| 992ea4d0-bca8-3eb4-8552-f29e8fb064c0 | -3.7856 | -60.7335 | 2026-09-20 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 8714e90b-5fc0-3167-a899-7c1fcc809216 | -11.3612 | -51.3374 | 2026-09-20 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 91d8aecd-692f-3f6b-bf15-18b6e709c412 | -6.3199 | -59.9381 | 2026-09-20 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 27244ea7-5aef-388f-871b-5563884b4454 | -9.0541 | -48.7686 | 2026-09-20 14:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 530.3 |
| 616df241-9263-3a4c-a225-fae06383c0c0 | -12.1715 | -47.0131 | 2026-09-20 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 28924b1f-de68-3a60-94f5-ba004a9148d9 | -10.9694 | -57.1881 | 2026-09-20 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 8d4dfeca-bfeb-3d64-9725-0c1a5c84f281 | -3.1079 | -61.408 | 2026-09-20 14:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 5edd09c6-332a-3bd2-9caf-b28c87c43249 | -12.1328 | -47.041 | 2026-09-20 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| e2c9dd8f-c9fa-3e9a-a27e-0101b868b01d | -8.0464 | -61.3618 | 2026-09-20 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 88baa95a-684e-3c3c-9a0c-cb88019be7e1 | -12.0072 | -50.047 | 2026-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ab533639-3fae-349a-bb6d-cd80e3774087 | -10.8367 | -50.9266 | 2026-09-20 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 261.2 |
| 0117d5e2-44b7-32f6-a8f5-05010795f8ca | -9.3609 | -48.3251 | 2026-09-20 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 4241133c-f02f-3159-8425-f0661f03b5ae | -11.4714 | -47.776 | 2026-09-20 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| f1b39cf8-d432-333c-aef2-0d15e1bd7af6 | -12.1516 | -47.0608 | 2026-09-20 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 322b4854-662b-383d-98d7-b36a4e2ef430 | -3.3492 | -59.8861 | 2026-09-20 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6f5f2127-89e5-3c42-8d83-c8a9100279f4 | -8.8827 | -45.935 | 2026-09-20 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 133.3 |
| ef07e960-295c-360b-87a8-b53341867458 | -10.8364 | -50.9479 | 2026-09-20 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 294.7 |
| 9959095e-8eb7-343b-a28b-763db28f663d | -8.1378 | -46.7933 | 2026-09-20 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| f09917c4-827a-3c52-b24e-7163e6a046bf | -8.7733 | -44.2336 | 2026-09-20 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 242.0 |
| 32dead73-b056-343d-ad7a-b3f808a2f6d3 | -2.8974 | -57.8181 | 2026-09-20 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 914c835d-553b-3365-9975-2469245f0dbe | -8.8636 | -45.9596 | 2026-09-20 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 410.1 |
| 32f97d29-1086-35f8-bc1a-24fad6f9794d | -9.0096 | -44.9209 | 2026-09-20 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 33d4ab04-d4b2-3945-a1bd-651059ab4544 | -8.9752 | -44.6722 | 2026-09-20 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 357f9324-3a9b-3026-aa1a-904cf01844ed | -9.5595 | -66.0172 | 2026-09-20 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 30fa52b6-82d0-321f-81ed-c0808f060987 | -10.8553 | -50.9459 | 2026-09-20 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 246.0 |
| 32902496-a077-300d-9387-2b2336ab7c95 | -7.5704 | -57.6766 | 2026-09-20 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| f0a7e31c-a12a-3748-a821-ebe23d64e7a7 | -8.1874 | -54.742 | 2026-09-20 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| ddc87ba1-32f7-313b-9aae-cf64e7a73fb6 | -6.3382 | -59.9566 | 2026-09-20 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 148.0 |
| fb4903e7-a1c3-3f05-9433-613028f83519 | -7.9637 | -44.0667 | 2026-09-20 14:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 66c54c36-97e6-34d8-9fa2-7dee36b44742 | -3.6945 | -60.6405 | 2026-09-20 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| a5b8ccff-be77-365a-b99a-32871153b628 | -3.6946 | -60.5835 | 2026-09-20 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 316.6 |
| 7926af62-6604-3f28-a87b-e2bf2d3abc1d | -9.2603 | -45.939 | 2026-09-20 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |


[Clique aqui para ver as próximas entradas](README131.md)
