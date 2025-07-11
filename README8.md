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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a8675d8-c926-32f9-bb15-a64dacd40027 | -10.84661 | -49.11713 | 2025-07-11 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1a1da67f-39d0-390e-9909-591ddeb1ec37 | -9.91438 | -47.82965 | 2025-07-11 03:47:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 267e9455-2aea-381b-895f-3bb4b10c0001 | -10.63439 | -45.23437 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2710d93-35bb-32e4-9c5a-1932735f6a42 | -12.47048 | -44.49915 | 2025-07-11 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e048c53a-6519-38ab-b15e-96bf4755dd86 | -10.57785 | -49.13353 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5a450dd9-25cb-32f1-9f3a-64af3814ef72 | -12.99218 | -46.27835 | 2025-07-11 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39751390-3822-3572-ac1b-c00556ac6bf1 | -21.68764 | -49.50207 | 2025-07-11 03:47:00 | NPP-375D | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| c4f1d3d7-dd2a-3aa3-8d71-31829fe06c7d | -12.05578 | -48.5463 | 2025-07-11 03:47:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af534521-2fb5-3380-b5b0-5de9da5c0129 | -9.8644 | -47.87284 | 2025-07-11 03:47:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c36d9ada-166d-3fd6-a59e-8f0282e74437 | -12.46864 | -44.494 | 2025-07-11 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c981e5a0-e981-3f27-9860-6ac987828c07 | -12.99008 | -44.86044 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd6dd54b-0c75-33b9-9702-ffba6d57c294 | -11.43868 | -45.11919 | 2025-07-11 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4f8b74c-46d5-31cc-8e7a-8ea5d66e5095 | -11.84363 | -47.50114 | 2025-07-11 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8a00cde-a971-3a5c-bcb8-721c72f14bd3 | -10.58144 | -49.1283 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 68f39067-7890-33f3-a506-298ba209b886 | -9.90475 | -47.83297 | 2025-07-11 03:47:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 60a48cb6-5163-31f8-acdc-07c1684048fc | -12.41977 | -43.49161 | 2025-07-11 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c8f2047-cba1-3dc0-80fe-f18271184ea0 | -10.67529 | -49.49769 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 5112edcb-d626-35b9-844b-1d167d3f4ea7 | -21.27019 | -48.57146 | 2025-07-11 03:47:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6c8107a-59a1-356a-8d13-a52ffd329e0e | -11.44383 | -45.12022 | 2025-07-11 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff1b9012-00fc-3ff1-b757-937fdf889e6b | -21.53472 | -49.53045 | 2025-07-11 03:47:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 55cbb16e-b301-3d05-b2d4-fe4553452ad4 | -13.15256 | -47.29565 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fc24296-15da-38d8-bbad-08317f96000a | -13.13872 | -47.30484 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fa99e3e-df53-397d-b898-5236adf448b0 | -12.66571 | -47.0946 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c5256057-68cf-37f1-9b0b-f8d60c4a6cb5 | -13.0048 | -44.86361 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b5a687c-2c0b-30f7-b9bc-875c10d9d0b6 | -10.66851 | -49.49603 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 9f71c9d4-bb22-32d7-a18d-5f014c30f646 | -10.6247 | -45.2362 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3ce91854-9adf-3f87-972a-d94c0bc9d97a | -10.87733 | -46.76352 | 2025-07-11 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64e9a63f-3cec-36f3-b952-4e54328b4273 | -10.68334 | -49.4931 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 96404a52-80f1-3a8b-b42d-fbda409b2590 | -10.84927 | -49.12283 | 2025-07-11 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b89402a9-5894-36fa-8ab0-8bca45c13ab7 | -13.16399 | -47.26871 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a329e959-7349-3477-8e78-fcf7dd780269 | -11.57489 | -47.42841 | 2025-07-11 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4d9295b-ccff-353e-8e51-145f98ab70bc | -14.39187 | -43.7727 | 2025-07-11 03:47:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c8d7c02a-b416-342d-b734-d4f3b6202b37 | -15.36731 | -47.05362 | 2025-07-11 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67ade16d-b10e-3ba6-80c6-942850714e72 | -11.32804 | -45.21783 | 2025-07-11 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78634aa1-5081-3e87-b1f9-cf6bb8b1c15b | -11.85333 | -46.75744 | 2025-07-11 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 431028a4-062e-3637-bea0-c8e920941210 | -10.63377 | -45.23759 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05ddf60b-7827-3016-9075-ad16ab2e2eaf | -13.15766 | -47.27051 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| febf8a9d-e7d0-3c8b-aba2-b411ee113f4a | -11.33262 | -45.22207 | 2025-07-11 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 503c363f-3b36-373c-bb66-84012fd66269 | -16.71813 | -49.23017 | 2025-07-11 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c8fa3b2a-c9d8-32e0-b5b4-577843b97837 | -13.13512 | -47.29315 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08e0009f-9429-36c3-bb5e-c06170da45a7 | -21.53563 | -49.52635 | 2025-07-11 03:47:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 416d0075-b690-31fa-a85a-7ba3739a7627 | -9.91538 | -47.82459 | 2025-07-11 03:47:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 39aacd9c-7312-30ad-9410-13ad09b83a73 | -12.42063 | -43.4869 | 2025-07-11 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15122f6b-9990-318c-8603-b59fadf0bf10 | -12.4077 | -45.35595 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e0fdae3-d906-3ac5-8725-c2b71c2383b8 | -10.84378 | -49.11556 | 2025-07-11 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dbcce3f3-3b3b-3d47-a1ee-058e87ce6b8c | -12.9941 | -46.2975 | 2025-07-11 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f00a980-059f-3e12-b7bf-8560c922a5cf | -16.13854 | -42.32978 | 2025-07-11 03:47:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 90dff3c2-a4fd-3148-b25f-746af2d93454 | -11.32744 | -45.22102 | 2025-07-11 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2575e32e-6239-34c3-9e2f-aad2cde66911 | -10.84259 | -49.12155 | 2025-07-11 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e8560ac0-b10c-3971-b5d6-b43334cadc2f | -12.99183 | -44.87804 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91fb174d-c7a0-3aff-ab6f-5e1f0dd00517 | -14.5623 | -48.13818 | 2025-07-11 03:47:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee1e3998-2409-39d1-baac-0e4a44b7a092 | -22.85622 | -42.98175 | 2025-07-11 03:47:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 41f08e03-4461-35d2-af9e-4270afe7cd7e | -22.0009 | -46.80479 | 2025-07-11 03:47:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 066408c5-0c6d-3d8c-9f1b-8a4acff0543f | -13.85067 | -45.85425 | 2025-07-11 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d270b56-7a4d-31a6-b030-1baae4a637f8 | -16.72418 | -49.23151 | 2025-07-11 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0007b28-094c-3b2a-b780-3b0ce858a180 | -11.84769 | -46.75611 | 2025-07-11 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9edb5366-005d-34fe-9f50-dc8bd09f4804 | -13.13446 | -47.29427 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47c8d56b-3682-33b3-a31e-a26af6716ecf | -12.99341 | -46.30105 | 2025-07-11 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a68b4a70-1a02-32fa-90a8-455927f8ffe5 | -11.82719 | -48.21306 | 2025-07-11 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7840f95-e16a-3f8f-8fe4-d7485219e0f6 | -12.06887 | -47.98415 | 2025-07-11 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fe14050-7322-345b-acef-b7fd52b39bf8 | -12.99362 | -46.27599 | 2025-07-11 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31a334be-8f57-3d81-8148-5dfaa1fc30dc | -13.13326 | -47.30227 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a7790089-0949-3411-903a-e825d81c69dc | -13.15427 | -47.28719 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c8152eb1-b501-34b3-8fa2-7023fd4d3e5a | -10.63037 | -45.22684 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a2c5121c-246c-38d4-8f38-69f87caf1bfc | -9.90704 | -47.83374 | 2025-07-11 03:47:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 2187344d-f5fb-371a-ba3e-83da69087e32 | -16.71781 | -49.23136 | 2025-07-11 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9b6dac8-4c98-393b-ab56-b9bf61b71c55 | -12.995 | -44.86141 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d223bab1-64a6-3a60-94ee-fee50ed66823 | -13.17133 | -47.29158 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ebf6098-3682-3016-8983-20fffd9ae3fb | -12.98902 | -44.86599 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bf6d3f0-cae0-3256-b91f-a5e693e6a540 | -13.13359 | -47.29871 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7365afa-26ca-3ce2-95da-e9af75cc1883 | -12.40197 | -45.358 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8392dfaf-4e4d-309c-98d9-06661c70ef8c | -9.9081 | -47.82845 | 2025-07-11 03:47:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 2a4030e9-0347-3b71-8df5-f872b4be0bed | -12.40651 | -45.36222 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f52dcd29-24b1-35e5-a740-b584836e72c4 | -12.41523 | -43.49071 | 2025-07-11 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbf0b719-cd1a-3056-bb8e-54150082d181 | -11.57401 | -47.43272 | 2025-07-11 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89ab187c-d234-3b19-bccb-e09256023353 | -10.85208 | -49.12434 | 2025-07-11 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 27e13b0e-d41d-31dc-a21c-b7943c540b51 | -16.72386 | -49.23269 | 2025-07-11 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a2c6bec-8f03-32d2-8af6-77e7319b688b | -13.15187 | -47.26962 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ccedef1-8c67-39bc-adec-1bc7c9b6d3bc | -14.20977 | -42.01805 | 2025-07-11 03:47:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 871addd8-17a8-3884-ba9e-f1a008eba68f | -10.57663 | -49.13958 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 29fdecf7-b675-341c-aca2-2e81fe58d44a | -13.00374 | -44.86918 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae9b3852-e06c-379a-8317-bf9a47dd73e4 | -12.40079 | -45.36427 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e9a5d42-23ac-3dbb-a744-1b21ced5e0e3 | -10.57912 | -49.1272 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d0e72881-14e9-35fa-9235-f3d4742aa6a5 | -9.61852 | -49.02042 | 2025-07-11 03:47:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a21b4961-5a48-388a-bf94-8e71b4e636a0 | -12.99605 | -44.85592 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79640413-5f4d-3a17-86f0-70a8821e3829 | -12.46759 | -44.49945 | 2025-07-11 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab63dbb4-b426-3dc9-af28-e1115e5b681d | -13.13809 | -47.30627 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2da6acf8-1fe2-3c1f-9ca8-f51aceb7f07a | -11.33322 | -45.21889 | 2025-07-11 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f27558a-c28a-3f41-b1a8-896d32beee7b | -12.98409 | -44.86504 | 2025-07-11 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 001d5a92-d8c2-35c9-97c3-fb9870310e9e | -11.42444 | -45.10986 | 2025-07-11 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 656e0075-2569-3627-b762-4f285d13c41a | -13.1723 | -47.28676 | 2025-07-11 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25800169-5582-3431-bb3a-85ee2f9a6d1c | -9.91207 | -47.8288 | 2025-07-11 03:47:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f33065da-951c-3019-ae7e-537e8c9c8a5d | -10.87813 | -46.75946 | 2025-07-11 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa28d5ea-648d-343b-8b42-1259f270aaa4 | -13.35928 | -47.89426 | 2025-07-11 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 251e4b3f-d32d-3ad4-a95e-264999360345 | -10.66979 | -49.49056 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 417fa45f-3b7e-39e4-9716-638744ccfd0f | -13.85127 | -45.85493 | 2025-07-11 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e88a1175-301c-34bd-9d15-ba70f0a10b43 | -10.85329 | -49.11845 | 2025-07-11 03:47:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d3ae7bc3-2cc5-329f-966f-4553ed24e884 | -23.33987 | -46.77465 | 2025-07-11 03:47:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 877692c8-d1ca-3281-88ee-51818b299cf9 | -12.99287 | -46.27478 | 2025-07-11 03:47:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3ed9a0e-ee3e-3ffa-89d9-9bd0ba813f28 | -10.6253 | -45.23294 | 2025-07-11 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README9.md)
