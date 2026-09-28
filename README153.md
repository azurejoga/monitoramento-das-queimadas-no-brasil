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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03efcdb4-a3f4-3b7e-a2ef-9f088fd8f366 | -7.47717 | -54.9842 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2b55d2b5-a284-33d2-8698-982be192c2f7 | -9.34886 | -46.53678 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 20adc23e-dc3b-3563-b00b-09952bb8edcf | -11.45718 | -44.92559 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0638ecfa-d412-35ca-9903-f3449c6f5bb9 | -7.68949 | -54.75117 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 80540c31-cfb6-37d9-a212-e82a82ad54eb | -6.3366 | -55.32793 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8eb6563f-2c2b-3746-8953-8a252bb5102c | -9.07429 | -49.87283 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 8a1d50e8-8de4-38cd-bffe-81d4d741f54f | -10.96584 | -50.68332 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 167a91a6-d6c4-3955-b729-80e281d05856 | -6.1974 | -53.228 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6f084104-4246-3e91-a3c8-e702f75f1212 | -11.01233 | -54.14163 | 2026-09-28 17:09:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| b7475e62-94d6-3aed-92b0-1de32caf28eb | -8.22665 | -54.7508 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f88e29f3-e750-355b-9219-9711cf3c2479 | -7.46135 | -45.80653 | 2026-09-28 17:09:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b9cf22a-37da-3dcd-85a6-46c96c36dfdf | -11.06971 | -48.89093 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3e1af029-318f-31d9-bade-18fa9a7f058a | -7.37653 | -44.76907 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 94ab6453-9bc2-3d72-a843-3d67d90a7d30 | -10.26055 | -44.6236 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e821819d-f8f4-38a5-8ddd-169410c87419 | -8.77585 | -45.82547 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4a569983-b6da-32a4-846d-ed511a949aed | -9.93292 | -50.23943 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 7a915b65-5203-3127-b706-13bc7ebb39fe | -7.74429 | -47.51759 | 2026-09-28 17:09:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 94f0602e-3571-33cc-8621-d662a914862e | -7.66944 | -49.53575 | 2026-09-28 17:09:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1e984625-f141-3fad-9913-653a65a904d6 | -7.25272 | -43.34921 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 648f4069-b94b-3c08-b3db-62efc26317e8 | -9.76822 | -44.84908 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 135de969-d702-3b45-beff-28ab7d6d82fe | -6.03422 | -49.56635 | 2026-09-28 17:09:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| abe18cb7-dac6-3bbc-9db8-926a45a3bad5 | -11.11959 | -43.32433 | 2026-09-28 17:09:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 959cc2de-f8fa-3fe3-a1d9-8534bbacb34f | -5.23033 | -48.42499 | 2026-09-28 17:09:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cf81bfc2-e362-3adf-8293-74db2e0fc114 | -7.69108 | -54.7616 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 55e32d4e-1e2c-3f82-b4e3-8c573d735e22 | -11.84648 | -50.85639 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ba97a196-5547-3819-a1a1-c7451b9798f4 | -13.50729 | -61.14299 | 2026-09-28 17:09:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| acaf64bc-1251-32f9-b444-c2e6ca215066 | -5.39135 | -45.6858 | 2026-09-28 17:09:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 16f227a8-87c8-3796-957c-629392e420fe | -9.57529 | -45.49289 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f4c0b89e-b294-332e-9e50-114bf0ebe133 | -6.13966 | -53.0628 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 33a84000-b80c-321d-a12e-fc80d8db0e5c | -10.2044 | -49.9812 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 3a2a2f14-c12c-3354-a041-74a53494e990 | -7.44088 | -55.63811 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| c57c747c-0eaf-32c5-b425-5f25d28ca813 | -10.2975 | -48.15423 | 2026-09-28 17:09:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f66cd1c4-c0d0-31a5-8fdd-26ede3460ef9 | -6.23367 | -53.03661 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dbdf528b-3022-3512-a48e-ec4c8122d41e | -6.66875 | -45.62008 | 2026-09-28 17:09:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 296edfe0-0240-34c4-8b4f-25c51fd19610 | -6.22292 | -53.23987 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 14299e3e-d7d7-3226-ae2f-05676abacec6 | -8.10181 | -44.01132 | 2026-09-28 17:09:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1d9f3b27-6867-362f-8887-d03b8e331e3a | -9.50694 | -45.76656 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8e5888f8-8017-3ed9-a851-340e48a84198 | -9.76568 | -44.83297 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 12206aaf-2d08-3d8c-88b4-0ada5266f847 | -11.96311 | -50.06449 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a8338e45-3993-34c6-8b52-1fe974ebc08b | -6.31645 | -43.61682 | 2026-09-28 17:09:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 91450d5f-61c4-37c6-a9fa-e7eaab8cff15 | -10.91321 | -50.71079 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 95657073-c39a-30d8-8a26-63b9f5defeb6 | -9.93758 | -50.24365 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9b04ee19-5c30-3b8d-9419-344de9c1ddfc | -9.78081 | -46.44185 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 524613e3-3641-3891-85bb-cba40373031d | -6.67407 | -45.62066 | 2026-09-28 17:09:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 63e2dfc7-f1e3-3a88-af91-b67265753625 | -4.85831 | -45.27279 | 2026-09-28 17:09:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d925ebf6-cfbf-377b-a9b4-f93000fbe867 | -11.12695 | -50.06727 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| cf075cc1-05e2-3d13-a146-3ecea9184125 | -9.49677 | -46.35661 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 69b87f3a-af2d-3129-ae1b-28b5809f10fd | -8.26379 | -54.70591 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| fb87ce41-b636-34b1-a5da-55631102e88a | -5.2295 | -48.42002 | 2026-09-28 17:09:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 719175d1-cb9d-3279-9c97-27f428c8ef72 | -10.81472 | -57.22625 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| eaebe196-c44e-309f-8986-709cceec2281 | -10.82587 | -57.17644 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 10ff69d5-d7ad-3e7d-a5bc-008bbb3f47fc | -11.39327 | -45.4189 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6fc480dc-38a1-3e40-9d4e-ba6d0af9c2f6 | -5.80202 | -43.63082 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d2b03f2f-bce3-31b9-bc75-f4883f3bf285 | -8.28116 | -54.70624 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 44de531e-72b6-33e3-b2bc-789be622139b | -10.91692 | -50.71016 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 66aa75e6-5935-38d3-8302-7e69b8dae01a | -11.85068 | -50.90431 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ffd7b1a0-612a-3d19-a080-f5321eae699e | -7.26194 | -43.36366 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c0636b30-1dd2-3e47-acce-6e5cc34d750a | -10.81768 | -57.19719 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| c3288e80-3f3e-3fb2-8ec0-0d2727f706f3 | -9.79866 | -44.82851 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ed64d0ac-460c-3488-9550-cf89cfeb6956 | -6.73724 | -52.32415 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3f63eea6-e0ea-311e-b3dd-08c08f69197d | -8.52891 | -64.12625 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 43f4cb75-6153-3a35-9005-4d60f4387f35 | -8.36115 | -45.39832 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 26f00f99-9b21-3fc4-952f-cf2de2463515 | -9.4996 | -46.6011 | 2026-09-28 17:09:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 5473191b-3ceb-30fe-9c1a-721529be2281 | -10.90989 | -44.6517 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d8bcb293-bebd-34a3-9ed1-49d3351dda30 | -7.90416 | -45.44706 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4423c33c-9556-36bb-a807-35e38bac257f | -5.73901 | -43.28263 | 2026-09-28 17:09:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| c4c142f8-6892-3041-bf22-380aa43c0ce9 | -10.22171 | -49.98859 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9c030b8b-7ae0-347d-8ca1-2dcd1b9f6a9b | -9.10755 | -49.89962 | 2026-09-28 17:09:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6f8781fc-3984-3c8f-b184-06cc80c65f05 | -6.16585 | -52.9028 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 017dbfde-bf8c-35fc-9781-8d73cfb41675 | -8.22576 | -45.4652 | 2026-09-28 17:09:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| a0f82094-cacb-3e77-986b-850624e4204d | -5.64282 | -43.71905 | 2026-09-28 17:09:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| eb0df396-cc63-38a9-a4b8-1a0609964b07 | -10.7025 | -44.42992 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 2b82f7eb-fc56-342c-be42-8b50830b99fe | -7.09902 | -46.45935 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 85ed139c-6a87-3c66-aa6c-183ea889b27a | -7.70229 | -46.968 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a4b5c243-f4ff-3007-beea-f141b6bfad64 | -12.21231 | -50.4371 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ac455e48-3c87-3cce-aa66-4a76ad2f0778 | -8.97034 | -44.15174 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 04ee71cc-a5d9-3246-9657-7efea3cb7678 | -7.4295 | -55.63346 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| aa64f197-ab88-3fbf-a360-56992c29a19d | -9.60051 | -49.6454 | 2026-09-28 17:09:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b5329d7c-5824-3ad3-813f-b3b0c03b27ab | -8.66494 | -45.34325 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 16313236-60fd-30e4-b4b3-aef7373c36e5 | -10.82446 | -61.42006 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| de93c3b9-825e-3a74-b4d4-79c9a7288e9a | -9.84493 | -45.20922 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 427679bf-c6cf-373c-91cc-b5a63eb7bec1 | -11.18671 | -44.8181 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 2bf26911-8be0-306b-abd5-4609fd007d84 | -11.15077 | -50.06811 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| b43872e7-e9ff-30a6-925b-770af387448b | -11.12657 | -50.05521 | 2026-09-28 17:09:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 88fe3f7b-98e0-304e-8a3f-0e1cd6f1a313 | -8.98224 | -44.15602 | 2026-09-28 17:09:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 0e1a7414-5b0c-36ad-8adc-5b67a444fd96 | -8.03839 | -54.89816 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c319ae0a-1df5-39e3-824f-3823a5c8cf93 | -12.35836 | -50.23812 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 44fa3ba7-9606-3685-b803-fa9ad59a1d83 | -12.39904 | -50.65565 | 2026-09-28 17:09:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4117dafb-96fa-3990-a618-27a1480770ea | -11.99206 | -57.60836 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e86fcf40-40ce-3553-b38d-70ff69d59b4b | -9.48718 | -46.35715 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9c76bdbb-a577-3e53-9047-3a3f082b8b07 | -11.17566 | -44.7988 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 43ac5f3c-858c-3a4e-8575-107b59102319 | -5.85477 | -53.82685 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6543e0ca-25dc-312a-9dfc-190a2f5375b6 | -9.79174 | -44.82213 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44167335-4384-3f52-920b-23592e061f73 | -10.82238 | -57.22928 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4796ef0d-139a-3462-b5fb-1a6edfef0549 | -6.73076 | -52.32959 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 41c03108-cf4f-3f5b-b0b1-16bd5ea11d1e | -12.38679 | -50.24726 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 322d8f73-fb81-32cf-831c-0403eccb4c2c | -8.64005 | -49.48285 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d7705a5e-16e8-35f5-9b31-5b4211610106 | -9.19176 | -60.42225 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 7ceeec02-fbd0-34fc-9614-e56a4fd46269 | -8.93274 | -61.495 | 2026-09-28 17:09:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 384684ca-167f-3897-a38e-43678392adcb | -10.20591 | -46.68906 | 2026-09-28 17:09:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |


[Clique aqui para ver as próximas entradas](README154.md)
