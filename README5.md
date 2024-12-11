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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 264d33f2-09f3-3168-9355-5ec1163f8303 | -6.9158 | -43.5185 | 2024-12-11 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 285.9 |
| d80bc8cb-9d42-3442-a8f3-e1842a534643 | -9.8592 | -35.9753 | 2024-12-11 00:50:00 | GOES-16 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 61.6 |
| b4b669c9-0a46-3bd7-adc8-71ab29ef0189 | -9.8404 | -35.9515 | 2024-12-11 00:50:00 | GOES-16 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 96.7 |
| aa8afe83-846e-346d-983c-72af42c0984b | -9.8399 | -35.9787 | 2024-12-11 00:50:00 | GOES-16 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 96.0 |
| 8eee2ad7-1618-3b46-8213-eb99991451f0 | -6.9783 | -42.9741 | 2024-12-11 00:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| a65f3323-74f4-39ed-bf7d-aed127f3d1cc | -6.8784 | -43.4986 | 2024-12-11 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e16cf29c-f45f-3338-855d-0a4f7cc26995 | -18.0062 | -52.9861 | 2024-12-11 00:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 18c4834a-dcea-3527-98ae-ffe4817f7a01 | -18.1192 | -40.1311 | 2024-12-11 00:50:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 237.8 |
| d822bfd1-d5b6-3c51-bdfc-23d0662a3d7b | -2.8196 | -53.0629 | 2024-12-11 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 0da70778-eaac-33a8-ac13-390c703e4b72 | -18.0261 | -52.9829 | 2024-12-11 00:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 96.2 |
| faa123c1-4111-37f7-adba-497e277d6bc8 | -3.1133 | -53.2381 | 2024-12-11 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| fbe9ef91-20ae-3091-bc13-f6faea68db5f | -11.1295 | -54.6391 | 2024-12-11 00:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 5fb82295-f4d0-3235-9e6a-612de6a91c97 | -6.897 | -43.5202 | 2024-12-11 00:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 466.8 |
| dd955339-b23d-31cd-9ebb-e487bc2fcdb0 | -18.0067 | -52.9645 | 2024-12-11 00:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d48a4e35-cd1e-3efa-a075-04597aac6488 | -3.2351 | -42.4353 | 2024-12-11 00:50:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 47b2f541-f19b-330d-9081-194e4a68ffcb | -11.1106 | -54.6408 | 2024-12-11 00:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.8 |
| fd47c460-0536-3922-9610-b641e3f0cd13 | -18.0266 | -52.9614 | 2024-12-11 00:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c7dee186-d7fd-3708-9172-edcd1e839ad2 | -6.1366 | -42.5544 | 2024-12-11 01:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| 24ce5c72-1d29-32c0-b742-efc84b574f3f | -2.9666 | -53.1201 | 2024-12-11 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| fcc694ea-00dd-35a1-bd64-7ff7b3ec8b04 | -6.9594 | -42.9759 | 2024-12-11 01:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 87c073a2-ce7e-3b15-989e-b88c2510ef77 | -6.1178 | -42.5559 | 2024-12-11 01:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 8ace5148-2e22-3301-9d89-e40b3ff0fee4 | -6.118 | -42.5323 | 2024-12-11 01:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 0b215359-71f0-3944-9cae-c3aeace5d359 | -6.897 | -43.5202 | 2024-12-11 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 452.6 |
| f76426e1-f646-3a16-8be5-0ce9cf5e2cfe | 3.2362 | -61.1982 | 2024-12-11 01:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d1281706-47ff-39b4-96e4-a2f19d6ed5b7 | 2.7444 | -60.657 | 2024-12-11 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9214e3fa-27e1-32b3-b4e2-8118d273fce5 | -6.9158 | -43.5185 | 2024-12-11 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 251.4 |
| 36d4ce7b-3517-3f4b-a208-8c2a83d7702a | -6.9783 | -42.9741 | 2024-12-11 01:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| e47fe677-edd6-37b6-b4d5-374b7335ab4f | 2.7444 | -60.6381 | 2024-12-11 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 36388b2a-215c-377e-a8c6-4b7c4e5ae0c8 | -6.9161 | -43.4952 | 2024-12-11 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 239.9 |
| 2879ee7a-6fa1-39ba-bc3b-ab604be6c4e0 | -18.0261 | -52.9829 | 2024-12-11 01:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| a72bb80a-4941-3a3d-8205-c55495309d42 | -18.0266 | -52.9614 | 2024-12-11 01:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| efe2484b-2a15-350f-a673-e0309d1301f9 | -18.0062 | -52.9861 | 2024-12-11 01:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d70e70dc-e5f6-3f2e-b4df-3f6dff08d1db | -2.8196 | -53.0629 | 2024-12-11 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 93e63177-bd83-3d88-b380-60e9cad138e2 | -3.2351 | -42.4353 | 2024-12-11 01:00:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e7f202db-ba2f-3b43-9fd2-19be9ec909a2 | 2.7627 | -60.6378 | 2024-12-11 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 116.0 |
| bd9e3834-fc8a-3bf8-b4fe-ef64095836bc | -6.8972 | -43.4969 | 2024-12-11 01:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 414.2 |
| b8853c62-10cb-3a3c-b1b1-3972ee5384af | -18.1192 | -40.1311 | 2024-12-11 01:00:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 169.8 |
| 1baedd8c-9c67-32a1-8891-9f9159ee93a9 | -3.8165 | -52.3813 | 2024-12-11 01:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| d2da1191-cf32-3ca5-ae67-d38a5be9e0e8 | -6.1368 | -42.5307 | 2024-12-11 01:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| bd5ba8e2-8b78-3c78-9d57-b62051baa653 | -6.9592 | -42.9994 | 2024-12-11 01:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 216.6 |
| 8e597f7d-0245-3d67-afe4-4b252a76dd2d | -6.9403 | -43.0012 | 2024-12-11 01:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 12815cb9-f34f-3151-a7e4-864bb0ac505f | -6.978 | -42.9977 | 2024-12-11 01:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 182.6 |
| befd65c6-e9e3-30bd-a49c-add207ca546e | -15.0865 | -59.6487 | 2024-12-11 01:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 255c4490-60f5-33c7-a85b-3501e345c39e | -18.0067 | -52.9645 | 2024-12-11 01:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 001486e5-83fa-38a8-9fd7-136b6811150c | -10.09 | -36.33 | 2024-12-11 01:00:00 | MSG-03 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 37c6168c-5853-355f-9297-2720cbece41b | -6.97 | -42.99 | 2024-12-11 01:00:00 | MSG-03 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4d0ce55d-5495-3e66-b509-5d3848742126 | -10.09 | -36.29 | 2024-12-11 01:00:00 | MSG-03 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a992ce0-770e-32b6-be43-05ae1bee0a5c | -6.95 | -42.99 | 2024-12-11 01:00:00 | MSG-03 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 50649594-7784-3111-a701-0a62b6890496 | -11.1295 | -54.6391 | 2024-12-11 01:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 16ba3c3f-0e03-3395-b80b-7c0f31758118 | -6.9594 | -42.9759 | 2024-12-11 01:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| f0b03c40-df73-3813-8e59-2f27457ff94f | -11.1109 | -54.6204 | 2024-12-11 01:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 29f830e6-1fc4-37fb-86e7-29d832ba38c9 | -6.9783 | -42.9741 | 2024-12-11 01:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| a3a11733-e8c7-327f-9f02-a9ed325debe5 | -6.9161 | -43.4952 | 2024-12-11 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 245.7 |
| 35d7c989-5cfd-3772-8a37-e55824fd0bed | -6.897 | -43.5202 | 2024-12-11 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 400.2 |
| b7d4beb8-7499-3dfd-a2c4-831821219171 | -2.9666 | -53.1201 | 2024-12-11 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| c753f8ee-0a62-3e69-bdd3-648a4b4358fb | -18.0261 | -52.9829 | 2024-12-11 01:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| d1b4cedc-8f80-31e7-9f09-1bf4e84c1624 | -6.118 | -42.5323 | 2024-12-11 01:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| 01ab7caa-abd8-36c2-b066-712b123e9a4b | -6.1366 | -42.5544 | 2024-12-11 01:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 2108ee35-f3c3-3dbb-9971-dfb87be8a623 | -3.2351 | -42.4353 | 2024-12-11 01:10:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 0537c764-8686-3849-baa2-1b676f2acae6 | -6.1368 | -42.5307 | 2024-12-11 01:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 118.8 |
| 80eeff8c-15cb-308b-aac9-5a17139430b9 | -6.9403 | -43.0012 | 2024-12-11 01:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 3018c828-4ea7-34e8-943f-36f6f94d500a | -11.1106 | -54.6408 | 2024-12-11 01:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 4323439d-d19d-3c35-8a1f-6b79556ef324 | 2.7444 | -60.657 | 2024-12-11 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 80.4 |
| b57ede31-fba3-32fc-8904-c6a796af82b6 | -6.1178 | -42.5559 | 2024-12-11 01:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 0d367908-853c-37df-b143-3893e90c02af | -6.9592 | -42.9994 | 2024-12-11 01:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 226.3 |
| 2939e2a2-688d-382f-8f86-636efd39d5ae | 2.7627 | -60.6378 | 2024-12-11 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 110.9 |
| eb9541cb-ccf2-304d-8e72-ba850137b383 | -6.978 | -42.9977 | 2024-12-11 01:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 192.6 |
| fb7cd612-bb05-3204-96d9-987f7134176a | -6.9158 | -43.5185 | 2024-12-11 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 302.3 |
| 149ad087-c073-38a0-9cec-b1787a50edd9 | 2.7444 | -60.6381 | 2024-12-11 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 149.9 |
| baaa9086-8b40-3b1f-a78a-58165545318c | -2.8196 | -53.0629 | 2024-12-11 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 7849dfe8-50f1-3358-9627-d918cc7de378 | -3.8165 | -52.3813 | 2024-12-11 01:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| dc82b4ad-458b-3ef4-b5fb-5bf398c15a56 | -11.1104 | -54.6612 | 2024-12-11 01:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 96749f0e-f587-3fc7-b8ad-b307f8018985 | -6.8972 | -43.4969 | 2024-12-11 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 322.8 |
| 2db8f5c1-87ff-366f-876f-8e6a8ce6fa83 | 2.7533 | -60.641201 | 2024-12-11 01:10:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b5a5e61a-4505-389e-93c2-e905f19ecfb9 | -12.5484 | -58.349201 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c051074c-9dfd-3a01-b504-dcc854d167f9 | -12.5371 | -58.344501 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4329584f-9a57-3480-8cda-0fcb923f081e | -11.1081 | -54.621101 | 2024-12-11 01:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b19fcbbe-6dfb-3648-8dad-bd2593aa9a25 | -12.5339 | -58.330502 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1890430-79ae-3737-80be-d5e935a9683b | 2.7549 | -60.634102 | 2024-12-11 01:10:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 30f507db-9736-3a25-81e7-2b9264864417 | -2.9629 | -53.111198 | 2024-12-11 01:10:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db6df2e2-232b-30a0-875a-7d59308a9b7c | 3.226 | -60.737999 | 2024-12-11 01:10:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dbdc3eca-1a88-3735-9391-6cf4027ce619 | -12.5535 | -58.325901 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 73831a61-b763-309d-9d78-f23273ede45d | -15.9706 | -57.153801 | 2024-12-11 01:10:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e45c4e5f-1696-30d4-93f2-ccd18951419b | -11.1202 | -54.6283 | 2024-12-11 01:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d4d43e8-0043-396e-9eaf-4b59cf6740be | -17.7404 | -54.2061 | 2024-12-11 01:10:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7ee80513-68f9-302d-9b7f-4855f723acc0 | 3.228 | -61.188702 | 2024-12-11 01:10:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 88e73403-27fd-3119-904f-5491d61a5b6e | -2.9531 | -53.1134 | 2024-12-11 01:10:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81dc77fb-e28d-383c-ab72-1fac615589d9 | -14.2855 | -57.454899 | 2024-12-11 01:10:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c58ce0b-d884-35fb-ac7a-ad1625302be8 | -12.5386 | -58.351501 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 29fb5d1f-a856-3568-817a-fb057ac6d603 | -12.5614 | -58.360901 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a61df26-d608-38db-b46b-eefb0f774d27 | -12.5582 | -58.346901 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ec7e11e-4ba8-3d58-b4d0-6bdbfbf96e54 | -12.5665 | -58.3377 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e693677-fc11-3847-8d6d-145da5eb37fe | -11.1179 | -54.618698 | 2024-12-11 01:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad012569-c1ce-3a3e-9a73-fd9b84af2a96 | -3.1068 | -53.243801 | 2024-12-11 01:10:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dcdf405-505b-3a59-9cad-8b5771d21c15 | -11.6625 | -58.258801 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f318a5d-b507-311c-a158-3034c89ac5b5 | -12.5355 | -58.337502 | 2024-12-11 01:10:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a0533639-7eb0-3e96-ab7b-c366418eb6a5 | -11.1225 | -54.638 | 2024-12-11 01:10:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80292c69-9de8-3880-b724-cff0529ad8d6 | -3.0935 | -53.230499 | 2024-12-11 01:10:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdba3bf5-a866-30d2-aaba-59221db5e6d5 | 2.569 | -60.682499 | 2024-12-11 01:10:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 405627f1-dd1d-33e9-9256-e92942fa5fc0 | -18.012501 | -52.965801 | 2024-12-11 01:10:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
