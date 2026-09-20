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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d7651c2-bc8e-3d64-97c7-5c96f81bd495 | 1.15482 | -51.01417 | 2026-09-20 12:04:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c323b411-9f78-30d0-9bb8-92f96fb546b3 | -8.37292 | -47.57032 | 2026-09-20 12:04:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| b29d33e5-30e0-35cf-b34d-3c0d03498c2e | -8.64117 | -47.62257 | 2026-09-20 12:04:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 83a54ee8-fbec-36a2-a660-80be86fac3af | -9.84389 | -46.43694 | 2026-09-20 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| e861e595-434a-3fa1-9a94-69dd0a36a722 | -6.42451 | -44.97969 | 2026-09-20 12:04:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| eeb09c38-2670-38c2-94a8-1c0799d60b2d | -5.8955 | -53.64706 | 2026-09-20 12:04:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e73003be-ab89-3670-ae89-dabf7f28aa81 | -5.79255 | -51.86276 | 2026-09-20 12:04:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| f2ba4dc1-bda2-3c6b-bde5-dc8d70ba46bc | -9.83683 | -48.40531 | 2026-09-20 12:04:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 667d634f-f804-3ac3-8a22-dec133cefd2d | -3.34317 | -42.75328 | 2026-09-20 12:04:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 64018387-b12c-3e04-906f-8157830d8a28 | -4.51866 | -55.46844 | 2026-09-20 12:04:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 00773d77-1bbf-3e68-bb46-69d98509ce15 | -7.28019 | -45.54545 | 2026-09-20 12:04:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 6ff86448-ee75-30cc-b7d2-00e9968606ed | -7.32403 | -55.61919 | 2026-09-20 12:04:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b0097c1c-68c0-3bca-923a-169b4f06b226 | -9.83867 | -48.39067 | 2026-09-20 12:04:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 35.9 |
| bbd848e7-6571-3bda-8592-baa5af9d7019 | -6.55966 | -44.85657 | 2026-09-20 12:04:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| ead72da8-2c2e-3a4c-ac29-bb4bf3a68abe | -7.5962 | -46.14773 | 2026-09-20 12:04:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 15dd6537-22a9-3962-b02b-f861d88136d8 | -8.84389 | -44.92285 | 2026-09-20 12:04:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 869b368a-5801-32c3-b98c-9185cbd687f1 | -8.39153 | -47.17824 | 2026-09-20 12:04:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1695bf59-53aa-3851-b559-bcd1f163cddc | -1.4717 | -49.09016 | 2026-09-20 12:04:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 62aef6dd-c2d3-3ea1-848f-e93a9ace7288 | -3.35162 | -42.20446 | 2026-09-20 12:04:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 4316751f-7fe4-346c-8c74-db517451c473 | -7.55314 | -45.43897 | 2026-09-20 12:04:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 82588611-0945-3b45-9355-35e1fb4c0e8d | -6.92782 | -42.89507 | 2026-09-20 12:04:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| 744332b9-4e1d-36c0-a8b3-d781afce4bc6 | -5.73029 | -53.45168 | 2026-09-20 12:04:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3b47f499-c3e6-3349-b9b5-f4a45a05e8a9 | -6.75944 | -47.91729 | 2026-09-20 12:04:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e467136d-d91d-3824-91df-e47036604107 | -8.96671 | -50.84217 | 2026-09-20 12:04:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9c5b4eb0-3ebd-366b-859b-517380373ca7 | -8.37089 | -47.58644 | 2026-09-20 12:04:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 98fbaad3-a6ed-3439-838c-4d921181c898 | -8.87373 | -45.94309 | 2026-09-20 12:04:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| ed2e7ab4-bd2b-37e1-9ca2-2f467471e57b | -6.55029 | -44.93053 | 2026-09-20 12:04:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 97e6bdb7-93cd-3407-bc27-6ccd510df2a8 | -4.68815 | -46.39906 | 2026-09-20 12:04:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d87614b5-3eb3-347d-8a9a-1c27c80c490f | -8.44009 | -46.89891 | 2026-09-20 12:04:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ad284bb2-9d6e-3c9e-b343-1edee8ab3d89 | -10.35548 | -50.23607 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 60a937f6-157a-3da3-b39d-d49d6ba90d11 | -10.8705 | -50.19768 | 2026-09-20 12:06:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 5b000a0c-d606-3a42-b355-c3dcc14bbe92 | -10.26968 | -50.26412 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| e2a8b32a-6745-3bee-a326-84d3f79fb05b | -11.21555 | -48.36629 | 2026-09-20 12:06:00 | TERRA_M-T | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c6f56a51-108b-30b5-b07f-8ce85c16dc99 | -10.31768 | -50.21969 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| dea4ebe7-497e-30ee-9cfa-3c9cc4a60aa4 | -10.92276 | -48.32606 | 2026-09-20 12:06:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 843531ea-cbca-3e24-b38a-92a4639fb500 | -11.9552 | -50.10558 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f2e1b5ba-66f7-3e6d-9fe9-31f505fef039 | -10.8652 | -50.16212 | 2026-09-20 12:06:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6a70e6ab-3137-3b41-9e4b-707dfb63fa78 | -10.55084 | -46.73567 | 2026-09-20 12:06:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9b1398c5-b268-3c0a-9f06-7604c80defed | -15.87942 | -49.91347 | 2026-09-20 12:06:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 815dfe97-df7a-3a85-8192-92a796be29a9 | -10.47165 | -51.28337 | 2026-09-20 12:06:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 197.7 |
| e6bb16be-092f-3c7a-8c15-31ecac9956ac | -10.53867 | -46.39594 | 2026-09-20 12:06:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| dde11547-0830-35ee-bbb4-8ffe3378858c | -11.6956 | -47.72799 | 2026-09-20 12:06:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| eca09e1e-0745-3c37-afd1-6fa2b05d3013 | -11.45841 | -45.39022 | 2026-09-20 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| d4909810-5b85-340c-96c5-8bc1bd6a5be0 | -11.99843 | -50.013 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8d228c53-561a-3b3f-a1d4-a25e50133bd0 | -11.10969 | -54.02654 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| f47fb496-44e5-395c-8daf-4a7aaa26fb38 | -16.40518 | -54.7187 | 2026-09-20 12:06:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 77ea8aa4-c5e8-363d-baff-c51dd271acf1 | -10.3164 | -50.21366 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| f49fbaef-1817-3c59-8e10-de2f29be5b87 | -12.16771 | -47.06035 | 2026-09-20 12:06:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 422d6a0c-8858-337a-b7f6-e9052b0d026a | -10.33732 | -50.2223 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 138.7 |
| f02f279e-efe7-3804-a32b-339fd1dca9eb | -10.31336 | -50.23597 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 28d963d7-354a-3a3e-bd1d-df765892c898 | -10.92842 | -53.94171 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 49b97ee2-32f7-3261-b1b5-9c8da94adaa4 | -11.85232 | -46.8583 | 2026-09-20 12:06:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 2b411110-1799-371b-ac54-8e1b7e93abe5 | -12.14431 | -47.03725 | 2026-09-20 12:06:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 574fdf89-4311-33e1-ad7e-271cec95c507 | -12.27722 | -47.12635 | 2026-09-20 12:06:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| c4d40b73-b02d-3c4f-b711-b9445c863331 | -11.38463 | -44.24952 | 2026-09-20 12:06:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 98ebfc08-cb06-3c46-aeb1-01ed21db95e3 | -11.72326 | -54.56035 | 2026-09-20 12:06:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f3acf1b1-fbde-3e24-90f3-7995f22dc505 | -11.33121 | -47.28269 | 2026-09-20 12:06:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 55a71f15-b66b-3d56-b9fe-e05b5f4763e2 | -15.47357 | -48.42847 | 2026-09-20 12:06:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2a29d9a2-0c15-3686-99c1-c3b6ff3e50bd | -12.27791 | -47.11976 | 2026-09-20 12:06:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| acdefa8a-4ccc-38f6-a90e-e0c0e79443ab | -10.34567 | -50.23477 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| cd5a1c67-10f7-386c-9fe8-543a6a47b991 | -16.57589 | -51.62423 | 2026-09-20 12:06:00 | TERRA_M-T | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 5f2458e1-4256-3cf6-915e-0f86cf552f9f | -12.23231 | -50.17225 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 70a3a46b-f298-3abf-8449-060ed63b9fa5 | -14.04526 | -52.07998 | 2026-09-20 12:06:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c6ef11ec-b9fa-3725-8905-dedae5851db0 | -11.13062 | -49.47029 | 2026-09-20 12:06:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 346e2601-65ef-303b-99f7-7d7dfa74de3f | -12.23388 | -50.16028 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| fd709629-baf9-3b5c-a979-0d845b0d12d3 | -10.92464 | -48.31055 | 2026-09-20 12:06:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| c217e81b-fe36-3bbd-a6b0-f5b3030bc340 | -15.4593 | -48.44518 | 2026-09-20 12:06:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 38.3 |
| d36df726-9c7c-3e6e-92e6-eb81530421d0 | -11.66796 | -43.4249 | 2026-09-20 12:06:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4d4e0fb1-dfb7-3869-a5d5-262203fbe709 | -12.13142 | -47.03559 | 2026-09-20 12:06:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| e53d56ab-23b7-376c-a2cb-7e5ee2b6a1ca | -10.00208 | -50.27714 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| be8441f7-7a4c-3986-b64f-1a7c2250d0cc | -17.57778 | -44.96141 | 2026-09-20 12:06:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 139e7062-f09a-3832-953b-639535046f58 | -14.66418 | -46.6954 | 2026-09-20 12:06:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 203.0 |
| e79da932-4205-309c-92b8-f5f750a404fd | -10.33585 | -50.23347 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| bef4e754-e2e0-3620-9537-15ee3f392ccd | -10.66746 | -48.71458 | 2026-09-20 12:06:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 00dcc94d-34bf-31e5-ae4f-0e939e07b688 | -11.21286 | -54.07568 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 5a8767a9-24be-33f8-a11c-d59908f1ff25 | -10.82549 | -50.15688 | 2026-09-20 12:06:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a205963a-1c91-3b33-93dd-b4d685c9f307 | -13.31933 | -51.81249 | 2026-09-20 12:06:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7c7211ad-49ad-3f45-813f-6a1d3f912b06 | -12.48052 | -50.06315 | 2026-09-20 12:06:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| d522616e-e78e-3a2c-944a-b9fef5f3df17 | -15.88114 | -49.89899 | 2026-09-20 12:06:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e2989406-ed7d-34f3-ac42-b9e232f31c7e | -11.93473 | -49.77825 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e52c1686-79fc-37f2-8f63-e48cbee47059 | -11.77081 | -47.44769 | 2026-09-20 12:06:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 29e95f40-f5aa-39b4-980c-f8c36e421c78 | -13.87727 | -48.58582 | 2026-09-20 12:06:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 32.8 |
| ae0bc745-298a-367b-9eaf-5c35975bedf7 | -10.39005 | -48.90189 | 2026-09-20 12:06:00 | TERRA_M-T | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 72160951-619d-3bb1-894e-5cb766c0e9ce | -14.67173 | -54.46151 | 2026-09-20 12:06:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| afe94c95-2e50-3cab-bd4b-dc44a6920461 | -13.78586 | -53.09935 | 2026-09-20 12:06:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4108f866-ea5e-39b7-be45-dfa6037693e2 | -11.37531 | -51.40666 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 6ee2697b-00d0-3d3b-bcf7-60c05365042f | -11.90459 | -50.09896 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 057b0ff7-b8b6-3ff5-99b1-b7c96ee59e22 | -11.39106 | -44.24474 | 2026-09-20 12:06:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 7ca80b2c-17fe-36f3-8841-8a74ac7708be | -11.37665 | -51.39671 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6f5a24e5-c536-3ab7-8acd-71d206e88495 | -11.99681 | -50.02514 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 86da74f2-78b2-35f5-9675-c872666ed5e1 | -11.47544 | -51.48717 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 78e5d7a8-1ff0-342f-b0f8-7a5adc68b425 | -11.88219 | -50.04063 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a3c32618-1571-309e-9338-9fcf7f11022e | -10.66921 | -48.70097 | 2026-09-20 12:06:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 97b404cb-4f36-3ebc-a15b-caecb637518d | -10.86366 | -50.17356 | 2026-09-20 12:06:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 0489ec0c-ac46-30db-ba4e-7753c6802ad0 | -13.25304 | -51.74179 | 2026-09-20 12:06:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 29f5b193-f739-3739-b054-0030848e1039 | -10.27116 | -50.25302 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 211a2ca9-4833-3586-b54b-c7f4002e0853 | -11.01573 | -48.32406 | 2026-09-20 12:06:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5296b55b-7274-3a9e-9c77-d41123858ea8 | -10.57587 | -46.53191 | 2026-09-20 12:06:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 7a05ad0f-661c-3558-893e-84b9aaa1f2ed | -11.111 | -54.01751 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 2a6baef6-e2bd-3896-976d-9d1f2637450f | -10.27798 | -50.27649 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README111.md)
