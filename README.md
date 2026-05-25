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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1b94a04-9b4b-3f81-87da-6938aaef8fc9 | -11.5559 | -56.9432 | 2026-05-25 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 30ac5a9b-2061-39a3-9d03-d3c1d02a1a98 | -11.1731 | -55.910198 | 2026-05-25 00:34:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81bd3d5d-5852-389b-89be-e4aedef4ed16 | -11.9446 | -49.290199 | 2026-05-25 00:34:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cafb4dab-d26d-3220-bd8c-8e5cf95abd82 | -11.5455 | -56.921001 | 2026-05-25 00:34:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b91c199f-f7aa-3795-8757-592cdaebacf7 | -10.3984 | -49.433601 | 2026-05-25 00:34:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48a008bb-d436-31d5-8133-765a3e45cf01 | -11.5489 | -56.937099 | 2026-05-25 00:34:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea61bd5a-1023-3646-b6a2-e8451bc558e4 | -11.557 | -56.926899 | 2026-05-25 00:34:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6235873d-b92a-3455-b1b4-433e6cd4f48c | -11.9168 | -57.027599 | 2026-05-25 00:34:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6cefbbd8-6b07-3023-a1da-1d9d5f42dd21 | -11.5472 | -56.929001 | 2026-05-25 00:34:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e90991b0-0a34-3076-b7eb-b4c1efa2d46a | -11.3685 | -52.953201 | 2026-05-25 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb4a3454-25d5-3788-8ae2-b3b321737323 | -10.6447 | -49.383999 | 2026-05-25 00:34:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3fb4ba89-3ecd-30c4-aba3-bca1718222e6 | -8.7256 | -48.323601 | 2026-05-25 00:34:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b82e9681-2872-308b-b2d7-69db6005ea14 | -11.3669 | -52.945999 | 2026-05-25 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 857ba327-c406-356c-90f7-53f4db0fa0bf | -8.7224 | -48.3106 | 2026-05-25 00:34:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c793619f-dbd6-37ce-b668-82faa053afe7 | -14.7585 | -52.6674 | 2026-05-25 00:34:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 256ef50f-5b3b-334c-91ea-f860cc016efd | -11.537 | -56.9447 | 2026-05-25 01:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 8b8acb32-88aa-3413-8209-48a29f8553d8 | -11.5559 | -56.9432 | 2026-05-25 01:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 4033ff36-7696-3f0d-b141-cc532d711842 | -9.3455 | -40.2062 | 2026-05-25 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 2e9ed4e5-1385-3012-a7b0-c2434e2dd65d | -11.5559 | -56.9432 | 2026-05-25 01:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| a5130b9d-bc32-3999-9c88-deb49e8e6bfc | -4.38522 | -43.28997 | 2026-05-25 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 744f9b75-ad2d-3db9-aa46-7d7ab0c9e43f | -4.3846 | -43.29375 | 2026-05-25 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94272331-53fd-3efc-8bac-8bb4bbd8311a | -8.26591 | -43.93092 | 2026-05-25 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec8f89c6-4fb3-326b-b944-bdbb52b1809b | -11.47621 | -47.39102 | 2026-05-25 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b898e747-56dc-3c20-94f1-d71d60f8dee7 | -8.10765 | -46.90589 | 2026-05-25 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92302bfd-98d4-3f69-9ac6-84eb65902ddf | -9.48738 | -40.35028 | 2026-05-25 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 23145454-56c3-32a6-99e1-9ea70ab2c586 | -5.35208 | -45.18869 | 2026-05-25 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 28332317-b531-31d7-a3be-5e2e882c4458 | -11.47143 | -47.3897 | 2026-05-25 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 646a76d3-be40-3dac-8a3d-08ae0dc55f20 | -9.48796 | -40.34667 | 2026-05-25 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 39.7 |
| e4aa8376-de5b-3bef-b38a-e82c0bd2d10a | -8.62297 | -45.00424 | 2026-05-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5576209-0a99-30bf-b698-22d13dbcf498 | -8.72319 | -48.32289 | 2026-05-25 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7343ebad-616b-3359-8ff9-9615666bf22d | -7.73346 | -47.24263 | 2026-05-25 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48435172-2384-31f2-a060-1be14bf9d911 | -10.39928 | -49.44303 | 2026-05-25 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f038c9e-7583-377e-9683-c67a68bb97df | -10.39853 | -49.44701 | 2026-05-25 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 733a6c19-5f23-3ba9-88e5-da86bd8c42d3 | -10.39601 | -49.44212 | 2026-05-25 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9936d4e0-c479-367a-8223-409a0bce57cc | -11.30763 | -47.53939 | 2026-05-25 03:55:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af3a1eaf-bfaf-3ee0-bed6-4e08adb82d20 | -10.39446 | -49.45009 | 2026-05-25 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a08030e9-796c-3629-9044-1ae8e1bd608c | -8.72801 | -48.3272 | 2026-05-25 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0b4ff98-ea8e-350c-b44a-9ee22d8f21e0 | -7.39687 | -39.75611 | 2026-05-25 03:55:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 91698684-a9a1-3554-9a2f-2a9ecbf0e3d0 | -8.72864 | -48.32375 | 2026-05-25 03:55:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4765469c-aeae-301b-b569-4a2dd6ee9351 | -8.26183 | -43.93031 | 2026-05-25 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbeb4308-093d-3737-aa8b-e9185ce9402a | -8.10816 | -46.90306 | 2026-05-25 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f967cea-c38a-303b-a9f9-7d929326ff29 | -7.13616 | -44.06791 | 2026-05-25 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c3545ba-acab-3933-9044-68642c3487ba | -8.61862 | -45.00353 | 2026-05-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b9177bb-829f-3eed-8213-3e94a399fd3f | -9.48402 | -40.34974 | 2026-05-25 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 84160edc-be5f-3a13-884b-e56e01ef5627 | -11.37702 | -46.72535 | 2026-05-25 03:55:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e17a2d75-65b9-3f9a-b082-deaa3d7338e5 | -9.4846 | -40.34613 | 2026-05-25 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 385c4c0d-02d7-3983-8849-e33e31cd03c2 | -10.39524 | -49.44607 | 2026-05-25 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f49b536-2a9c-3935-b47d-407567c2ce14 | -8.61791 | -45.00757 | 2026-05-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42202c25-4843-3731-8913-08e07e59f854 | -8.72257 | -47.91296 | 2026-05-25 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b69adbb-da0b-387e-8ba4-f43ccd361de9 | -6.51836 | -43.68214 | 2026-05-25 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c289f12-4196-3f55-9dc6-9e1c90acb6e5 | -6.07704 | -44.01137 | 2026-05-25 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ce8ff68-89bc-3e88-922e-cf6dfa7f4f50 | -10.39777 | -49.45104 | 2026-05-25 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a63143f-868d-3297-9307-8d315dc62977 | -12.3382 | -48.22805 | 2026-05-25 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 850b256c-a6c8-3bfe-a773-94b97944ab07 | -18.10473 | -46.88847 | 2026-05-25 03:57:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 742bdc85-64ab-38fd-9e56-39c027d00cc1 | -14.76026 | -52.67851 | 2026-05-25 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba26f99e-dabc-310a-a113-94685d532b86 | -11.94688 | -49.29703 | 2026-05-25 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d48a6b24-7fe4-34f3-abf1-205a610db08d | -14.75395 | -52.67684 | 2026-05-25 03:57:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4784afe8-f3f3-326f-b04f-e00c684ea0a7 | -20.01671 | -44.2377 | 2026-05-25 03:57:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f017f742-040d-39a7-afa2-d7ba9057e4ed | -12.55818 | -48.35289 | 2026-05-25 03:57:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 962f5b79-9231-34e3-9695-a2a483cfe26b | -11.95161 | -49.3019 | 2026-05-25 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d945e916-70bc-3546-bb88-66e0e6831885 | -12.55762 | -48.35591 | 2026-05-25 03:57:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8881b4c-b121-331e-a4af-f2e84ba13db4 | -12.33878 | -48.22501 | 2026-05-25 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9325d142-b484-3c7c-815f-fae843dba21b | -17.68231 | -47.76937 | 2026-05-25 03:57:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ab08357-9ddf-3397-94c3-84e4863e96b8 | -18.09302 | -46.88171 | 2026-05-25 03:57:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1db16785-727b-3c78-b7e8-11d345183757 | -18.10056 | -46.8876 | 2026-05-25 03:57:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24306952-80e2-3c4b-893d-26d1432d4312 | -17.68092 | -47.76706 | 2026-05-25 03:57:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| eaaf5fa4-7265-311b-9067-a9029102ba55 | -11.36517 | -52.95542 | 2026-05-25 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 122136f3-8827-32ea-92f7-0cde9cfb2720 | -13.46999 | -42.49006 | 2026-05-25 03:57:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b72ca637-dbac-3993-9058-a6edef8641ba | -17.68315 | -47.76493 | 2026-05-25 03:57:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0146358-ace5-3c77-95df-32a9b2e8b51b | -12.41488 | -47.49662 | 2026-05-25 03:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78bd33e3-ad79-3623-bf41-301942de38d6 | -18.09381 | -46.87756 | 2026-05-25 03:57:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dc36194-06cd-3ecc-91da-41321dd9ba3e | -6.07774 | -44.01267 | 2026-05-25 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f91bd92-5931-3c7a-b2a3-250fc4b75de4 | -4.38206 | -43.2932 | 2026-05-25 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e964470b-cc75-3139-ad89-a023327ec00f | -4.38599 | -43.29016 | 2026-05-25 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3500a984-b57c-3c56-b37d-dd2310d1a366 | -4.38262 | -43.28965 | 2026-05-25 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 990445dd-1374-36c6-a661-75ea4fb30058 | -5.35358 | -45.18885 | 2026-05-25 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5419ec3c-ec67-3ca7-bc10-6f765c75fb1d | -6.51678 | -43.68478 | 2026-05-25 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 678cf1b4-1bdf-30a2-a914-925eeaea4aeb | -6.51734 | -43.68121 | 2026-05-25 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86afebff-22e8-369e-995d-b5e04756726c | -8.26075 | -43.93093 | 2026-05-25 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f4e8c58-1476-371e-b003-2637708c7695 | -11.47199 | -47.39051 | 2026-05-25 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4aa1eb2d-9bb5-3a65-9e09-d50a02791d1e | -7.13434 | -44.06485 | 2026-05-25 04:29:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43dc0e24-50bc-343d-8294-2b6150981d1e | -11.36712 | -52.95636 | 2026-05-25 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 54bd00e2-1fc8-30ff-aac8-b6ae99a78940 | -7.73367 | -47.24287 | 2026-05-25 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcc18b11-cc11-35b0-8a9f-e7aef3ce5dfd | -8.72133 | -48.3248 | 2026-05-25 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c88beee-d7aa-3f1a-92ff-57410ed5a416 | -8.99173 | -46.82948 | 2026-05-25 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18107f11-8907-3230-bbfb-f7652486f714 | -11.47536 | -47.39112 | 2026-05-25 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06ff126b-94f1-3d01-9753-6300bc09d56d | -8.86296 | -46.93556 | 2026-05-25 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14539097-9e51-3c38-bfcb-b6b90163c671 | -10.39617 | -49.44886 | 2026-05-25 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| edd4d632-c625-365e-805f-8ff6c6ea1aa4 | -6.98089 | -42.86544 | 2026-05-25 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de9f7a9e-8aa6-3821-b0f4-1ee9738601c6 | -8.26752 | -43.93201 | 2026-05-25 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d7555cb-05b9-3424-bd99-634b0b9dc926 | -12.30211 | -47.91109 | 2026-05-25 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85b9fd25-d136-3d66-82e8-7e339261ad92 | -11.45618 | -46.69458 | 2026-05-25 04:29:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4be19f77-0049-3aec-b6da-c5c7367ae785 | -8.9957 | -46.8264 | 2026-05-25 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 56b5bfa2-28e1-303e-941d-7f6f16b0edfa | -10.39692 | -49.4444 | 2026-05-25 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f10983d-b9b6-3cb8-84a2-28f7daae2e2d | -8.72491 | -48.32538 | 2026-05-25 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b523f091-ad3b-3b06-9a80-0418dbfafda2 | -8.61977 | -45.00495 | 2026-05-25 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05adf2ca-f377-3e5f-94ee-001ec614d480 | -8.7285 | -48.32596 | 2026-05-25 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1663b68-2246-37aa-9ef2-6ddc4e8e5384 | -11.37761 | -46.72192 | 2026-05-25 04:29:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3500229-0d27-3800-918c-a300f706efcb | -11.43838 | -52.92649 | 2026-05-25 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87f4df7c-37a5-3694-a621-6f74482ed304 | -8.72782 | -48.33004 | 2026-05-25 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
