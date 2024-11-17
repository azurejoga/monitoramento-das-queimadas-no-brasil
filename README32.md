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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2fc48bd-c868-3c73-a61b-4ce178c9126d | -4.36901 | -43.00946 | 2024-11-17 04:06:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20df06a5-d72c-3d46-bb2e-b08fe2009831 | -3.17019 | -46.60154 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d0baec4-9c50-3dfa-a295-3bae19825476 | -2.66681 | -46.19972 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a0ab58f-4ca3-3e6b-ad69-1cd5affa5a2c | -3.6952 | -50.11458 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 877af9ef-3f06-3c43-96cd-d07352c37eb6 | -7.13324 | -46.63777 | 2024-11-17 04:06:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c4aed31-afd0-3605-9799-b6540355962d | -2.07527 | -46.4789 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50ad66b0-080f-397d-89f9-4da678fcd8d3 | -2.65168 | -46.2131 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58939f04-0b85-346c-ba01-22fc867f194f | -3.34258 | -53.31456 | 2024-11-17 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 61226240-c441-30d0-a543-f3abcd316c0d | -3.69035 | -50.11021 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 639be4e4-62a6-3c42-874c-16a2cedf290b | -3.79364 | -46.02232 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20efa11f-20ee-3601-9234-40ad813061fb | -3.56941 | -50.26044 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 47aafbaa-144a-3176-9003-8e78193767d5 | -4.68491 | -49.62938 | 2024-11-17 04:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0416bcd6-2c33-328e-81d9-11f45e7950fc | -2.0768 | -48.53271 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c7e14ab3-6346-34cf-8bf2-997105b1d7e9 | -2.67386 | -46.20796 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12ac2524-2da8-3b1b-a2d2-332bdde68be2 | -4.55651 | -48.01579 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b0113774-110f-3e2f-a05a-923e27e80ed0 | -3.69463 | -50.11794 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b72ea3b3-764f-34e3-b74a-596474b0fb3c | -3.69319 | -43.51336 | 2024-11-17 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13e621f7-ce8e-3ca6-a587-202b5a49464c | -4.03681 | -45.47512 | 2024-11-17 04:06:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9025f7ee-2212-38e4-9a71-6ae9b142cf61 | -8.13068 | -41.12723 | 2024-11-17 04:06:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 4d6d47b8-9add-3c72-83f7-27dd37e61e6b | -2.00812 | -47.46141 | 2024-11-17 04:06:00 | NPP-375D | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ebd7fa7a-ad36-3acb-8ced-5ac0d770b3b6 | -3.09638 | -45.9706 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f5ed211-78fc-35bc-9353-c5c48299ccc5 | -4.34216 | -46.80222 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfd10403-95f8-3231-87b2-3c78486bb10f | -2.60106 | -51.79777 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 850ecba9-a27c-34d5-a358-63db68fbd047 | -2.59861 | -47.56576 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d703fa6-3486-305c-9f8c-beacf3173462 | -4.40565 | -43.57203 | 2024-11-17 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d55f6802-01b4-3866-afb8-0cb5048fe7f2 | -4.72791 | -46.84174 | 2024-11-17 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 933e7d46-e414-3951-9fb9-e2e8b2941385 | -4.72791 | -43.25112 | 2024-11-17 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 862072e9-d4bf-3fbe-afe0-e5f8af7b4f3e | -2.46048 | -45.61217 | 2024-11-17 04:06:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d41c812e-dd1c-3ba3-94d5-3efe47760fda | -2.6728 | -46.21667 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a1bac5d1-712d-396a-9776-367b8591e4db | -2.67525 | -46.20112 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da606a8f-c18a-3200-a6e5-c703dfd20305 | -2.58467 | -47.56353 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 81d1577c-9b3f-3185-aec8-62d630204a45 | -2.35172 | -45.6953 | 2024-11-17 04:06:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 674b06d2-0730-3be4-ac21-11bba2db19be | -6.52486 | -41.44153 | 2024-11-17 04:06:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f6c05168-3fe8-3b34-b159-429c57619511 | -3.69937 | -47.68157 | 2024-11-17 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1dd0bc30-4f5d-3bf0-a330-c1c3ab75542b | -5.5132 | -37.87834 | 2024-11-17 04:06:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eef49844-ae25-37cc-95e5-adf511b14a10 | -3.632 | -50.22242 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06fced20-88ce-3c13-bf2f-300dbfe0cccc | -4.04746 | -44.76805 | 2024-11-17 04:06:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0900fee1-b3fa-326f-850b-ac571955d5d6 | -3.49676 | -43.78729 | 2024-11-17 04:06:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 8fb5e8b3-966b-381d-a815-3007b698e9c8 | -1.20375 | -51.77383 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| da238cdc-4572-37ce-94dd-7ca65804b97a | -1.1095 | -52.31728 | 2024-11-17 04:06:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb0638ad-2fc5-3d2e-896d-d70445387bfc | -0.94196 | -51.64159 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f594251e-df1f-3f50-ad41-16782e7432f8 | -3.5211 | -50.24508 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94ddadd3-cbe5-31b7-ab10-c90d5a16bae5 | -0.95297 | -52.41964 | 2024-11-17 04:06:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9acab642-dd4d-38c4-9c9f-bf6d89e635b5 | -6.69552 | -44.70499 | 2024-11-17 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9436da3-cc08-36b9-9416-748ffb5a6004 | -2.67289 | -46.18869 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3554882e-31f8-3d47-8616-1933fc573451 | -3.29423 | -43.16609 | 2024-11-17 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f4a1345-5794-3885-bc5e-ef220a0028f7 | -6.64436 | -37.08157 | 2024-11-17 04:06:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7e793031-0da5-3155-a0a1-3e4d5a792596 | -3.51812 | -50.26291 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56437146-0ee4-3328-844a-52f59857163c | -4.73971 | -48.12238 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 196d8930-b4c7-3fdb-b74f-d3fcd8450131 | -3.18337 | -53.24611 | 2024-11-17 04:06:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 085cf54b-cc60-3535-bfd5-453f1262d2df | -3.58106 | -50.51886 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e58951d-2c39-3fa3-acef-b38285aefec6 | -4.48053 | -48.11063 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| af6325ba-fa55-3f1e-809c-f41aeb18f252 | -1.9125 | -46.57013 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| b1840d6a-b370-3c8f-8234-888e039c96fe | -3.19631 | -45.76332 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fe839b1-925a-386d-aab9-c9efdb9a38b8 | -2.23103 | -53.61343 | 2024-11-17 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 33d021f7-aa86-3bac-8ecf-988265baf868 | -4.51696 | -42.9514 | 2024-11-17 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d8f467f-9d48-32b9-a3ed-4ab9779573ae | -3.58403 | -50.53501 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7415840b-fe41-3fd5-ad36-db4fc720c59d | -3.78301 | -46.03551 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc0e07e4-74b2-35a6-8ed6-258ebfa992ff | -5.46209 | -42.14883 | 2024-11-17 04:06:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf28e856-a5ab-3dcf-945e-fe19918d0163 | -4.37148 | -48.09114 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc18da93-96aa-31b9-a09e-af14c7ace38d | -6.47687 | -47.51113 | 2024-11-17 04:06:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9049f215-2fb2-3b29-8c85-40f181d778ef | -5.33579 | -40.89243 | 2024-11-17 04:06:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| be93c885-ab5c-36ee-8578-faaaaac30e79 | -4.08568 | -40.87688 | 2024-11-17 04:06:00 | NPP-375D | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8670efac-7d5d-30bb-88e0-274a893eab00 | -6.88242 | -44.77175 | 2024-11-17 04:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f977c087-c0d5-3984-908e-5ad375904440 | -4.59556 | -44.57966 | 2024-11-17 04:06:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf86020e-0546-3224-8fab-66799fe91cda | -2.6667 | -46.19881 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a67a1abf-29c7-3bed-bc68-44093e22cc97 | -3.52548 | -50.25294 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 685b2e00-b91b-3d74-8a1e-3edeb1a6a273 | -3.09756 | -45.96326 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 665972f4-67eb-39ce-9f16-ce2b0029ff90 | -2.6559 | -46.21383 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d10dac1a-a036-38a5-b2fb-3119cfac6c19 | -5.13394 | -45.11311 | 2024-11-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 582a7337-3fff-34d4-a0f4-156f3a73a7b4 | -2.62313 | -48.57023 | 2024-11-17 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 69ce95d5-a4d4-3c80-935d-dc9b1b35943e | -2.67415 | -46.18005 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7eb2e018-8c6c-3904-8006-245d72c100a8 | -2.58853 | -47.56902 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d64ef354-a282-3a73-b2c0-58c98a61e10f | -2.21469 | -47.22274 | 2024-11-17 04:06:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| bd318dc0-a13c-3540-9b55-f1207e756dc5 | -4.37145 | -40.58875 | 2024-11-17 04:06:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a8168a29-4bcc-3939-bbd7-a0687628923c | -3.62381 | -43.16085 | 2024-11-17 04:06:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8dd05b7-29fd-3370-bddb-ed55c841eb9d | -3.32761 | -50.49448 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fe9364b-bcef-3d69-a790-e16356445f4c | -2.59474 | -47.56025 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d91c5b90-1b68-3bea-ae8d-f19db59b011e | -6.39802 | -44.74147 | 2024-11-17 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1abda8b9-b884-3731-98ee-476833cd6edd | -4.453 | -44.54712 | 2024-11-17 04:06:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9947fb4-c1ab-3286-a5b2-5dc763362d94 | -3.01906 | -45.40132 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a4a2131-13cf-325c-b045-a95faac4d0c9 | -3.03817 | -47.9859 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 90a7c3af-243a-31b2-a9e5-fa35b61c901d | -4.51636 | -42.95515 | 2024-11-17 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cae4b0c-1ba0-3b2f-a566-b3db7d2ff5c5 | -2.60833 | -46.1861 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0f0921-9886-3060-a415-a9642ec0450c | -5.31868 | -45.44752 | 2024-11-17 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43c99166-0f2f-3e5b-98ca-7f8a082b2e5d | -4.05197 | -44.7641 | 2024-11-17 04:06:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7efada6-130b-32fd-8cff-e9cab43768ca | -6.94525 | -42.8213 | 2024-11-17 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 32f7cff9-1e59-35c1-9fc0-14ce47e941a7 | -2.20398 | -46.04474 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8e365f18-17cc-3d20-b59e-100e5c42c26f | -6.48628 | -47.50834 | 2024-11-17 04:06:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08208863-5324-3047-aab4-b3142c1c4344 | -2.57492 | -49.08029 | 2024-11-17 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13372e16-f063-3743-a4fb-bd2ad80978fc | -3.0094 | -45.42425 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| defd96f3-55b6-3699-b12c-fdcc00856739 | -3.20912 | -46.47183 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57f93ada-ac96-3380-b666-9fe85f69aaa3 | -2.03407 | -46.37548 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c92ca285-3b5c-321e-97c4-35f0372b4c52 | -3.41968 | -46.13314 | 2024-11-17 04:06:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ae04ad8-dcc4-3fd4-ae3d-41c5a043c9d2 | -2.60187 | -51.79307 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9eca6226-05d6-396c-9e3e-057c6cddc42c | -3.0054 | -45.42361 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 70f90e76-824a-3180-9079-2c5ce476efcf | -5.17772 | -46.17229 | 2024-11-17 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bc43cdf-6c3e-340a-9a27-57ef1afe94c4 | -7.27553 | -45.79533 | 2024-11-17 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dae7bc1d-9845-3e64-a580-139e97597995 | -4.33473 | -43.04663 | 2024-11-17 04:06:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5162ffb-4f07-3f3e-bc7f-7cdeb460c2ba | -2.67157 | -46.19561 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README33.md)
