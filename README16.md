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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a91ca8c-3949-3838-83df-4c4940bcf8c9 | -6.82549 | -43.03965 | 2026-09-10 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 118c1dde-3352-326e-8815-4d7c81057973 | -6.16665 | -44.63973 | 2026-09-10 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e346dcfb-05d6-3b0e-874d-b6150bded436 | -6.09791 | -44.1396 | 2026-09-10 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aaf187e3-82d7-3978-bd2b-9e7b325ce10a | -6.17104 | -44.64051 | 2026-09-10 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8f5fa0a-985e-3bf2-bb5a-7e599a0636a3 | -1.47654 | -47.2743 | 2026-09-10 04:06:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e47382e3-4f11-3326-9661-e3517129d3ad | -7.04625 | -42.72681 | 2026-09-10 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a825bdf4-7ce5-3205-b1ea-6779a4f5e44c | -6.09922 | -44.13172 | 2026-09-10 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 404cdc28-e4a3-38ec-aa85-ba3e81b70ba0 | -4.00735 | -51.02709 | 2026-09-10 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c9460fb-9e73-3cf1-a5e5-fb39d4973a50 | -5.41188 | -41.83737 | 2026-09-10 04:06:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ecdcd7d8-da53-3b71-8120-3a181b2ee332 | -6.88111 | -38.30553 | 2026-09-10 04:06:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df0e2892-4729-3047-8646-cf493f33afff | -5.66197 | -44.2991 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a18d257b-a8ef-3a05-99a5-82efd90417dc | -6.26553 | -46.36654 | 2026-09-10 04:06:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adfb3d16-d565-326a-a604-81e89acff0b4 | -6.76293 | -44.57429 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4094a44-62cc-3c1d-9c69-c061e74092f3 | -6.26686 | -46.36174 | 2026-09-10 04:06:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38239d16-e673-3bc1-a191-f20ccc7785a6 | -7.10854 | -42.12825 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 11a02b5f-2cce-346c-ab9c-579c95f50a50 | -2.93194 | -50.4688 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8ca744c-d597-33ee-90e7-7e74fa4b4058 | -5.7731 | -45.07166 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd66a59c-24e7-3ff2-8ecf-473585c8db67 | -7.11743 | -42.14328 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7bf280f2-2aa6-39aa-90fd-210bb72b2c95 | -3.24753 | -47.24831 | 2026-09-10 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8b4ea6cc-8c63-31ff-a3d7-a65a6265817a | -5.69006 | -43.39653 | 2026-09-10 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| af6ab44c-4c83-3ae7-abfc-965c6054d1f9 | -6.28091 | -41.69889 | 2026-09-10 04:06:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 35312390-0285-38bd-8231-1d6be48f83dd | -6.87779 | -38.305 | 2026-09-10 04:06:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 15774e78-bbf3-3ad6-b37c-777ba1c720ae | -3.96105 | -49.01088 | 2026-09-10 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ba32635-0197-3f0b-9bb7-4c0f2763e7dc | -5.68539 | -43.39942 | 2026-09-10 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5a57d8da-c823-3084-a24a-c2f47ed07c8c | -3.26226 | -50.0865 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4ebffa1-1edc-3719-bb09-306d7ef00702 | -7.11743 | -42.12072 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5f0602f1-ab04-337e-a13a-91d47d474f17 | -6.77568 | -42.7333 | 2026-09-10 04:06:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c4343ade-79ab-3da7-864b-83253dbf1eb6 | -5.41634 | -41.8414 | 2026-09-10 04:06:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c63da93e-45fa-3616-abb6-cb1677ddb8fe | -6.75926 | -45.47566 | 2026-09-10 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bb56726-2bf0-371e-be66-ad168333d5ce | -6.82466 | -43.04467 | 2026-09-10 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 202930ab-155a-370b-8bad-6a6d224cb4cf | -6.11761 | -45.39104 | 2026-09-10 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 031fd28b-fcab-3e4a-a83c-fc4a882b8ce6 | -4.16975 | -42.43623 | 2026-09-10 04:06:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a6d138cc-0b12-3eac-8b79-5b665dc3f727 | -7.05783 | -42.70473 | 2026-09-10 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0c23e5c1-b9a2-3d92-b6d5-a2d88d6f422f | -7.04477 | -42.71219 | 2026-09-10 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4599a5b2-15a2-3ff8-965c-4052829327fd | -5.76451 | -45.09418 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2c206095-5eb8-3a8e-a932-7b40819ce95e | -5.48164 | -45.13151 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04b4447d-e220-3b75-be02-89323833766a | -7.13073 | -42.10946 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 12169d54-baac-319c-b88a-dc1719468979 | -7.10929 | -42.12386 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bbc5bc36-4495-3dc0-8e7f-0e1f6ebeb08a | -6.67196 | -43.43679 | 2026-09-10 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cec8af14-5a21-3176-b3d4-ea586b2c1534 | -6.4233 | -43.06735 | 2026-09-10 04:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fcadffe1-0729-3e5b-a2c0-07f5456da1ae | -5.14878 | -43.8494 | 2026-09-10 04:06:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92b652be-74da-3af4-aec1-cb1e78c35605 | -2.94544 | -50.47139 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45349c4d-e0a4-3e2e-9db2-6117d21edb02 | -6.26583 | -46.36745 | 2026-09-10 04:06:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b950b355-3964-32dd-a40b-4a8c86fb68fe | -6.16814 | -43.01857 | 2026-09-10 04:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dd3c69b-92e8-33c5-a2c6-a487f70028a3 | -5.76533 | -45.08945 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 4b43450d-ef4d-35be-86f8-5a079a73ba9e | -6.76799 | -44.57074 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e67eba56-7d42-367f-b504-ce1a9a684103 | -6.41935 | -43.06671 | 2026-09-10 04:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd05e33e-82ba-323f-a73c-fb615ce4cc9e | -3.54489 | -48.18314 | 2026-09-10 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c6d0e6c-3f65-395c-a33f-50f8b501ab4f | -7.12187 | -42.13951 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a29d0d60-17da-3f70-9afc-64126d65280d | -7.11077 | -42.12601 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e821a58-c197-3017-96e3-e91cbbd91229 | -3.2657 | -50.08126 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13bb9882-4fc7-3e3c-abe7-bd4079d07fda | -6.28387 | -41.70374 | 2026-09-10 04:06:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 09de7587-b524-363c-a963-c0296c386096 | -5.60995 | -44.84685 | 2026-09-10 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6df7244-c939-3552-a847-4c06f67acc18 | -5.10728 | -46.94867 | 2026-09-10 04:06:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00fe89ef-8f97-38c0-a892-bc8e660512e3 | -4.17057 | -42.43127 | 2026-09-10 04:06:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1b134366-4114-3b79-8d36-804456e566ea | -6.67261 | -43.4368 | 2026-09-10 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0284c6a0-4cd0-30e2-ba7d-8c22a5a78375 | -6.33223 | -43.7495 | 2026-09-10 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0472b5fc-a0f7-3a57-bd87-4c5df9bcc2c2 | -5.3242 | -47.47274 | 2026-09-10 04:06:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 400c3e00-de0e-3142-bc7e-7767d2ce9067 | -7.11373 | -42.12009 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 219af60b-40dc-3f45-9fc8-6c72edbc831a | -1.0991 | -48.05891 | 2026-09-10 04:06:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e03ead7-ae02-3fb7-a088-51b7d2097dbc | -4.03247 | -38.24079 | 2026-09-10 04:06:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 667627fa-75bc-3aa7-96f2-19d19d2769c9 | -3.24202 | -47.24738 | 2026-09-10 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ff00d7b-07c1-3dca-9d2d-ede9fdfd7d70 | -4.9603 | -45.14266 | 2026-09-10 04:06:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d55c6742-5e64-39cc-8785-5e7c02886d34 | -4.86117 | -47.41092 | 2026-09-10 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 17bdd97e-3e36-3446-a11d-d4e938b4f740 | -5.41561 | -41.83796 | 2026-09-10 04:06:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6a540034-63ab-3542-a34f-1d474ff6afef | -7.10193 | -42.13355 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0a7d791-0197-32cd-874b-f8227a93d980 | -3.51914 | -43.25983 | 2026-09-10 04:06:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e5356f1-f73e-3659-84e1-7eb9a70c44de | -5.55417 | -43.43644 | 2026-09-10 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 99c474c1-ed11-3a78-8768-90b31d88c201 | -6.17212 | -43.01909 | 2026-09-10 04:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c2d23d4-afed-3714-8723-e3080bb6914b | -3.96024 | -49.01559 | 2026-09-10 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cefdcdc-7177-3bc9-9eb1-35d3327f49db | -5.62879 | -45.87582 | 2026-09-10 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 421d27a9-d44d-3ea2-b4cd-ac0f47eee0cc | -5.56474 | -45.33506 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f66a9ea-205c-3d51-9d43-91b202f7316a | -5.68599 | -43.39579 | 2026-09-10 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| fa0ff807-39d2-364a-abc9-9192c61f5645 | -4.15029 | -43.10505 | 2026-09-10 04:06:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3a41628-4d3b-396c-b7b9-c8887f0b76ff | -5.60919 | -44.85133 | 2026-09-10 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a2f1e89-2c4e-3369-b37b-2e7f28e39864 | -5.10203 | -46.94781 | 2026-09-10 04:06:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e870c0f-377f-380c-a327-0f2b73d18060 | -5.76614 | -45.08477 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| a7a50158-9c94-39a9-a4a9-fb352c20910e | -7.28015 | -39.32678 | 2026-09-10 04:06:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5bb356f1-4ffd-3cf2-b070-9ba8bb31af42 | -5.38093 | -46.29798 | 2026-09-10 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 018e431e-2187-3746-b7a3-0ff10089ebe3 | -5.55888 | -43.43343 | 2026-09-10 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d13c5329-6f1c-33b7-851e-a11fffb6780a | -6.76728 | -44.57495 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba05d187-9e18-30ea-95b5-fc7bd5b815a0 | -6.16739 | -44.63543 | 2026-09-10 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 13e3d538-4a22-372a-b4fd-b56fc275a590 | -5.69066 | -43.3929 | 2026-09-10 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ec67f73b-caf2-308a-a506-2c005489b4c8 | -10.23552 | -45.21478 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b1b55c0-9a4a-36e9-91d2-a07c3c4afc2c | -7.48434 | -45.26999 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e454c6f-4477-3032-85c4-f70adb82a7cf | -12.65071 | -42.29845 | 2026-09-10 04:08:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1909aa38-cd37-3ec9-9ccc-fa75cd809a7c | -7.57585 | -45.68192 | 2026-09-10 04:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b4eae1c-f5c9-3ad7-af27-0bba65500cad | -11.21036 | -46.34599 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 086d89e9-1bfb-364d-927e-fdbb0b208731 | -11.86295 | -44.87748 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cc65818-ef5b-3230-b97a-6c5cb002fd0a | -7.97981 | -43.98611 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dea15a33-4da4-329e-bbe1-ef5134fdd229 | -10.46358 | -44.94953 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4485e8da-7a41-3a99-9849-e4c441ee3380 | -8.75995 | -46.43596 | 2026-09-10 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8c08e4e-0d8b-3440-bcec-d462a07b95b1 | -7.68499 | -44.31085 | 2026-09-10 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cfee983-1d9a-3deb-adcc-5e5d70151721 | -8.97966 | -44.97747 | 2026-09-10 04:08:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04f26c47-4ec3-34d3-9bbe-5501b0ad2e5c | -8.13245 | -41.12216 | 2026-09-10 04:08:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8b04ccac-d7cf-3d6e-b939-d58028d3ae53 | -7.51193 | -45.27093 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67324767-effe-3b35-aeb1-815298233953 | -7.51432 | -45.2571 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca95b530-46fd-38cc-884c-543ef6bb1e58 | -10.55963 | -47.73792 | 2026-09-10 04:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2564a07-54cf-3f12-a8b1-428c62e06ed7 | -8.70938 | -44.71627 | 2026-09-10 04:08:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c943c8d6-0384-36ae-8da5-2a0c22794838 | -12.86493 | -44.61357 | 2026-09-10 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README17.md)
