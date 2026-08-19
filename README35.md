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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a37b0e13-b692-3318-9109-863f9c9666cc | -6.88915 | -59.0392 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a0fd086a-59ba-3c74-aaf3-f6bf0d6244ba | -5.13909 | -56.27824 | 2026-08-19 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 445138fc-47d6-381d-a790-8878b5d01397 | -8.04465 | -50.11049 | 2026-08-19 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a96e9f3-f939-3427-b64e-2480e303a60f | -6.00456 | -57.86643 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 31074957-5caa-359d-8765-1c1d7939cf95 | -6.34766 | -54.90599 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b3ef000-2920-3adb-ad95-16a68fca69ed | -6.886 | -59.05673 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf45d3be-280e-3432-b015-f6e5601ba7f4 | -5.99668 | -57.84579 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84b87eb8-fe04-3e4c-bf37-8cd5213c55eb | -6.98837 | -48.05138 | 2026-08-19 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| caecdd6b-9b16-348d-ba23-d8124693116b | -6.13778 | -57.87524 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b36d17d-7486-3e24-9e54-040c39b17615 | -6.0141 | -57.84486 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 156453d2-bbb6-314c-8dd6-97cc4021675c | -5.73351 | -44.50767 | 2026-08-19 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f9967be-4023-3b18-b71c-e47b19b094ac | -6.10032 | -57.86786 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f77e6a5e-c448-329b-a1b2-a39ba6a0c80a | -5.49393 | -60.1368 | 2026-08-19 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17e8cf32-31d5-3092-8f98-56c379488c2b | -6.06746 | -45.36488 | 2026-08-19 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afc8f701-5239-3563-a3ae-5079515da41d | -6.16186 | -47.75687 | 2026-08-19 04:38:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fb62d3f-35f0-3a2a-a0f9-6382d5e89282 | -7.21751 | -43.28907 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0f722c7d-d973-3010-b05d-8d58306cc2e1 | -6.64408 | -51.30767 | 2026-08-19 04:38:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8412ebfc-7d33-37cc-9b2c-2113575bfd84 | -6.02059 | -57.80789 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ba875c2-b16e-3c69-bb99-302055d9d266 | -6.63048 | -59.07764 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74db69d4-c078-359f-97bc-7222d1031598 | -7.18936 | -43.45678 | 2026-08-19 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bb9425ae-f046-328a-a7b8-35bd3c5546ed | -6.26894 | -55.97184 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45c370d2-748c-3916-81b0-01fb05e5b851 | -5.90783 | -43.62125 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b824f85-fabe-3773-b82a-74ee3338df3e | -6.84819 | -58.99488 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7c0e956-3f71-334b-b160-5c3bf0aa13b7 | -8.36498 | -46.34517 | 2026-08-19 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca7eed8a-f1f0-30c5-a699-cc3e563fdd17 | -6.08681 | -57.91159 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 19530bdc-af1e-3fbb-92e1-a800a6784fb4 | -6.4045 | -46.63729 | 2026-08-19 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b6fa1cd-8a64-3849-a194-3188038a9c97 | -6.7502 | -59.17979 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6bd08f9-facd-3950-b6f1-d61158935cfa | -5.13857 | -56.28122 | 2026-08-19 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bacc378c-d4da-3807-9d57-adf21f7b4482 | -7.55237 | -55.56106 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21aff276-2839-3ccb-a334-d544e1cbb54d | -8.35977 | -46.35603 | 2026-08-19 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c89e0dc6-49fc-3e05-999b-4d33010d15db | -4.2721 | -48.18967 | 2026-08-19 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3ac33fc-7803-3883-bf94-854b77d21024 | -6.80942 | -59.44689 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 642ceeb6-2828-3f37-aab2-dad6a719d326 | -7.62673 | -45.71419 | 2026-08-19 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44e6ade8-170e-37ae-9028-efb61b9a6b70 | -2.77014 | -48.57513 | 2026-08-19 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 795ab0a6-3deb-364c-bf75-8b4407fa2d2a | -7.94423 | -44.63845 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| da324fb0-2d13-3a96-a8b2-d64229a204e8 | -6.99411 | -59.05221 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7fbddee-206c-363c-af22-fd34d94ac54c | -6.14067 | -57.89103 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d158b368-48f7-3930-af03-4b1edc950c4c | -4.70441 | -47.15502 | 2026-08-19 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2dc2494-d4fe-39b6-b329-b64fdd3a65cb | -6.35019 | -54.89425 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b11530b-3270-3787-a477-6852188f9b7b | -6.34938 | -54.8989 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64f30791-d210-3952-a782-de2dcfd47984 | -8.17936 | -44.4355 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7d9714b6-faec-36e3-91a1-c8476612118b | -6.80332 | -59.44584 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7e7f1ff-8c7b-3122-a5b5-536b1ed1e58f | -6.84229 | -58.99372 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eeda2b15-767c-3f85-9984-f11efb5c1657 | -5.29607 | -49.14151 | 2026-08-19 04:38:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96b8ea56-2be3-3ec1-be63-7a7bf09a4c3d | -6.88655 | -56.43796 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b4a9e7f-de2f-35e7-bd35-e7056e185176 | -6.90745 | -42.84887 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0f22325f-ce01-3dc2-8c5f-55e2fb12c689 | -6.40118 | -51.71191 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9821674-aad1-3f62-980d-044d1d6fbf05 | -6.12281 | -57.70845 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9b720ca2-1b67-3216-bcdf-7590ec7a85f5 | -6.84937 | -59.02199 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e87203d-6b17-3fce-9a79-cfd58603a2a9 | -6.8316 | -56.45885 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 227c1b2c-b68b-36d8-bd63-9c58dc6dcc32 | -7.53292 | -55.57614 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2fddf50-c152-3d23-959d-30111ff5218f | -7.94796 | -44.63899 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 02db8591-60c7-3657-bc6a-2fb48f725976 | -6.09545 | -57.86287 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9207c9c-a275-3e5d-86f5-cefa325a4a5e | -6.34857 | -54.90351 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2c1955c-d428-3ea2-a506-5f8236f56d22 | -6.01649 | -50.20237 | 2026-08-19 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6a653d5-0de1-3e51-a687-eee117fca5d2 | -5.91595 | -49.25837 | 2026-08-19 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 782880af-986e-3ea8-90a2-90622b3a9e37 | -5.43934 | -48.41418 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b05e1a19-97bd-33a8-891f-e6901a4cd1e9 | -7.28967 | -44.07676 | 2026-08-19 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 773c7fe0-1835-3d54-a32f-99f3f9a046cf | -5.43271 | -48.41312 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 7d203d00-8f6e-3241-97d6-9503fce7e512 | -7.89411 | -44.99795 | 2026-08-19 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 718468bd-57b1-3ecf-9b50-41ddc0587521 | -7.04643 | -59.84181 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6258c38-5150-3001-b2fc-a123e9d4b8ee | -6.87414 | -59.05444 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffa83db2-31b6-3b96-b12d-2e18fd92dc3d | -6.74413 | -59.17912 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a8c7a59-7e46-37b6-b076-1a47f04e5f57 | -7.12166 | -47.54881 | 2026-08-19 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b3f04dc-d6ae-3d2c-a96e-6efaf781d678 | -6.70124 | -58.9427 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9665a2b8-4e4e-362b-9255-303eb2fcf850 | -7.28266 | -49.42205 | 2026-08-19 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a92fa3e9-9fbf-3abc-830c-76d6592a4bd0 | -6.76383 | -59.15169 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58df62f3-5f18-3245-9090-0597e300e578 | -5.91939 | -43.62298 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7be6f42-a20d-3732-bc5a-59e9c1f96635 | -7.55615 | -55.56684 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 656ee83e-a633-3217-abb7-fa919b6e4948 | -6.99845 | -59.04765 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1c0f47d-cd74-340f-8937-f5613cfd6801 | -6.74432 | -59.04181 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c7bf4d1-431f-36a7-9337-bb36167d93cf | -6.83293 | -56.44907 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 118158b4-33cc-316f-b74e-93b4bd90abe4 | -8.54265 | -47.38846 | 2026-08-19 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2221a80-3000-3ca9-9e73-a6fe99f963db | -4.70718 | -47.15899 | 2026-08-19 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61ad4e2c-fefa-365a-9fa6-3f7878148f8a | -7.18279 | -43.45439 | 2026-08-19 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e9ab0055-4c95-3de9-8b4a-d440af33c40f | -6.75103 | -59.17519 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f901736e-948e-363c-ad0b-ec3934c2ce16 | -6.40662 | -54.9475 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba88cca1-374d-30d0-9cbd-5665d37f38b7 | -6.33844 | -44.07728 | 2026-08-19 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 34fd3a89-8211-3db8-aa0b-8fb093a8ad49 | -5.93016 | -46.23852 | 2026-08-19 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9e34307-1708-3c5e-940b-dc6cddbecce2 | -3.24614 | -48.80349 | 2026-08-19 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fbde5169-e858-320f-a632-c612cf98e088 | -6.64165 | -45.50913 | 2026-08-19 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bfa55981-134c-3d58-8a4c-df1ffd9d272d | -6.33624 | -54.91829 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 278dfc67-bc24-3513-99c5-8d058315852d | -6.44366 | -52.74421 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91553e30-16ae-3a4b-9ef9-8005b91be77e | -7.09678 | -55.45503 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c8bd066-cef7-3f19-87a3-d843762408d0 | -4.17847 | -49.39676 | 2026-08-19 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6286322c-ea5e-3adf-9aab-d927ecb047cb | -7.01891 | -45.90057 | 2026-08-19 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67f7dce8-41d8-3e43-ba96-e5fd75fa7b0a | -6.88245 | -59.04235 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb6978f0-6b90-30be-967d-df2d1bf8c8c3 | -6.85959 | -59.03317 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0673b5a-304a-3ed4-9fed-6c3f6e47a223 | -9.10985 | -46.04033 | 2026-08-19 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 540d930b-4b44-3a3c-803a-7d08a71064ab | -6.34776 | -54.90819 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03c79c51-59a5-3e1d-a9cb-c0377e3cfc25 | -6.69907 | -58.93529 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d1fe1014-f1df-3baa-bc14-4212042b5ec6 | -3.0558 | -46.92395 | 2026-08-19 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6382f40-a81f-3636-ba43-ac6a4c21c6d1 | -6.41277 | -54.93892 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8878a24-3017-324f-8b9e-c9ef88f4b180 | -5.43658 | -48.41018 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da9668b6-35e6-38c2-a900-d44c305e9360 | -4.70387 | -47.15847 | 2026-08-19 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a339283c-579a-355b-9113-c3d2093e1943 | -6.34844 | -54.90134 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2c960e0-54df-3b47-82cb-b6a38c45080a | -6.40787 | -46.63782 | 2026-08-19 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 79e79cf2-8b7d-3b57-932e-4d1afcc3cf83 | -6.83426 | -51.29383 | 2026-08-19 04:38:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65b9a3ea-6f1c-338f-8b82-ba487c0e41d9 | -5.42608 | -48.41208 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97485b4a-63a8-34dd-91c8-0802a779f1fa | -6.74353 | -59.04616 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README36.md)
