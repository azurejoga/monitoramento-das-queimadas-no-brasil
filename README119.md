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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5067a80-446f-3b69-8ad6-e1ce60e68799 | -7.68639 | -44.89208 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 69f2d554-ffa4-34a5-a275-0ef7e083fef5 | -9.35926 | -46.8227 | 2026-09-28 16:26:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 06d4924a-bffd-3bad-9867-277ad65b8c9b | -7.25179 | -43.35585 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1f68d93e-182d-3a3c-91f9-76d5ba8c9513 | -9.75252 | -48.20121 | 2026-09-28 16:26:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3f88988e-545c-3344-9bbc-94da47b5e1cd | -9.33537 | -46.53549 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f05b359-475a-39d7-94f3-4812bf3ef55e | -8.57865 | -45.09417 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e445c5f2-4eaf-36da-ba30-349480872b8c | -9.96898 | -50.15621 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8b58c55d-6927-3800-b6d3-ceacf3d9c9cf | -7.70951 | -44.9283 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d423276b-152a-3f70-9322-fb5dd032deba | -9.98047 | -50.16636 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2f27185d-4107-3d7e-8d32-e2db0d5d341c | -7.21741 | -46.06094 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a26abb92-9246-3174-9e57-7ea7f98064de | -10.07351 | -40.0302 | 2026-09-28 16:26:00 | NOAA-20 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 869bd9f0-fdb3-364a-8483-0a51097f1bed | -3.69087 | -42.19746 | 2026-09-28 16:26:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| b3607494-7302-3f5a-882e-ae950d5c966c | -8.03635 | -42.8457 | 2026-09-28 16:26:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 6c245fae-3488-3395-b46c-9d85694f1bd7 | -5.73461 | -45.05482 | 2026-09-28 16:26:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 1689296e-1607-3ecc-a068-493fcae10429 | -9.0732 | -49.86844 | 2026-09-28 16:26:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| fd5fcd50-e694-3bac-b049-ed7f4b2e00e2 | -5.6901 | -43.21416 | 2026-09-28 16:26:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ac03b3d8-9adf-3140-85a4-aacc7e4d3040 | -10.99098 | -50.69942 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 40.5 |
| c5325cd7-832e-3ba2-8787-d844a0c3469d | -4.37619 | -40.60846 | 2026-09-28 16:26:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 01f72d2e-28c5-3dd9-8a24-59ab96ff482c | -9.99011 | -50.12428 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 867df58e-b1e0-3ca6-99ff-244e3872d140 | -7.68443 | -44.80592 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 165bcff0-1ddd-300f-81e7-5482db5b72f0 | -10.90028 | -50.70132 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9b898050-a3a1-3753-9bf3-8e6db75c5c48 | -9.49274 | -46.35725 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 07878b80-2f0f-3a46-a4dc-64978f5f1e58 | -10.89987 | -50.69808 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3535a0ff-cc70-34cf-aa08-93a5c1a0f4b5 | -9.52052 | -46.37067 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| eea8565f-faad-3995-b13e-08bfd0805994 | -7.70253 | -44.92933 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| db2facb3-e4db-3809-ab53-bedafd5fca82 | -10.94902 | -50.66204 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 45bc8e08-c9ca-379f-b456-50948834d6dd | -7.26002 | -43.36534 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c4cf662a-e48a-3467-bdb4-49e686972da2 | -10.70719 | -44.43778 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a62f0807-52e4-3e74-8788-9e6b0dec3601 | -10.65051 | -50.70983 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f76f8d2d-04ed-3da8-8552-4c0cf60ca563 | -5.03636 | -39.89839 | 2026-09-28 16:26:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5c9533b0-6585-3c28-bcab-ba0bd9d2e64a | -7.43265 | -55.63889 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8f1fffed-0595-39e5-ae07-87530bc9df47 | -9.9993 | -50.11725 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1c55b78a-29f0-392c-8f8b-4894b2802f6b | -7.34249 | -38.71818 | 2026-09-28 16:26:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 13bcb997-b937-301a-9071-e52bdc1d6dc2 | -7.46624 | -44.5818 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 6456df8d-eca7-362d-bf13-30ab3fe540a9 | -6.16885 | -52.81879 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 41061b06-3c9b-3ef4-a1c8-f1b072f94a9a | -6.75372 | -43.04585 | 2026-09-28 16:26:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| bb8109db-3e04-3dcf-acdb-9d2696dc1f1c | -8.73164 | -44.90497 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 93c4d1dd-ff6e-3cea-9c02-71557afeafec | -8.9738 | -44.15715 | 2026-09-28 16:26:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 57c644de-018a-3167-835a-4c346ab73914 | -10.20709 | -49.99311 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5a13b54c-38ee-3b8e-bf8f-43e3e9691261 | -11.02627 | -49.70695 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 89f6af27-ef42-3855-96d9-ffa938f8b9d7 | -11.13157 | -50.08119 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7797d774-e692-3d92-888f-cf2393ea4a15 | -10.00006 | -50.11612 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 551c89cf-bf20-3b9c-b54e-eeb6fd454f8d | -10.94455 | -43.88599 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b7496fd9-3464-34c5-ac5a-ed1b1a619d94 | -10.95258 | -43.89267 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c4907701-d8e5-3cf1-adeb-57ee9ccd8871 | -8.04113 | -39.56344 | 2026-09-28 16:26:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| eb74b266-9361-31ef-ac49-0c6df2bd4493 | -10.20419 | -49.99817 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b260fa9e-4d07-3451-a2f6-196ce6d07d59 | -4.09223 | -42.95258 | 2026-09-28 16:26:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ed1091be-b4fe-33b9-a16a-4bbac9e66422 | -5.51745 | -45.57031 | 2026-09-28 16:26:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 678694f9-ada5-3f1d-8505-18ebc3373999 | -9.4948 | -46.35468 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 82b175d4-6c2a-3d1d-a3da-932192dc71ec | -7.75947 | -37.62147 | 2026-09-28 16:26:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| bad74267-54d6-395e-8049-49cbf5a33160 | -6.79117 | -39.80865 | 2026-09-28 16:26:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| d15cac2b-f1da-3133-ad0b-d6bcc8569d49 | -10.25214 | -44.60989 | 2026-09-28 16:26:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 3c15505e-3f63-3be1-82cf-682b13b42a7f | -9.59892 | -49.64225 | 2026-09-28 16:26:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3e3ca67f-2cda-3080-b8d5-13fbcc77e176 | -9.02822 | -50.80325 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 73f536f9-eb76-34cc-8f48-166a0c1832b6 | -9.8053 | -45.71139 | 2026-09-28 16:26:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c541fecb-2207-3621-b5cc-eb115c485f9b | -10.6843 | -44.45335 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| f37eccba-9075-3384-8e18-916764bf6882 | -11.46613 | -49.74389 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 63cfe612-5f76-3d48-9c8a-60c935adaae2 | -10.95545 | -50.67105 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d91dfb49-73b5-3c9e-8ce8-7a3165dfc14a | -10.21337 | -49.99119 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9618ca8f-cd1b-37fa-8b1a-23d5aa93d2dd | -11.17957 | -50.62805 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 27bdb699-b9c0-3d92-a4bb-37d09fefca94 | -7.34321 | -38.72268 | 2026-09-28 16:26:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 9eedf6eb-4887-3236-93d6-b666caeb1786 | -9.78198 | -45.97789 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1b331855-8d09-39c3-b49b-8f62c9689400 | -6.31283 | -43.60699 | 2026-09-28 16:26:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 3ef7e6c7-aeee-35b8-b7e5-1f3c71172b78 | -9.08985 | -49.88246 | 2026-09-28 16:26:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 32efd0fc-e831-3568-ae66-33340f330828 | -9.83074 | -45.26515 | 2026-09-28 16:26:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 3a05f2b9-0838-389f-b9de-5738f6693769 | -6.8154 | -45.05861 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5670111f-0de7-3d9a-abf2-d195d2a50a7a | -10.71658 | -44.42826 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3920ab03-1c98-3e5a-8b5d-76ba933d2d14 | -6.69887 | -45.67398 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 4409bcbe-85f8-31f8-a62c-4b2950802bbf | -7.41836 | -37.67665 | 2026-09-28 16:26:00 | NOAA-20 | ÁGUA BRANCA | PARAÍBA | Brasil | 2500106 | 25 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 6148cf51-4774-39af-8329-ce898aa3fb8d | -11.16456 | -48.17775 | 2026-09-28 16:26:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9b0ed3b8-53c8-3870-889c-007ee45acb5e | -10.88815 | -50.68973 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2a01dbbc-3167-397c-9e1f-b59ac69e2424 | -7.76096 | -54.78041 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 73c19108-50dd-3441-85f9-cf688b3a3e5f | -8.67377 | -45.34747 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ac65316d-a31a-3018-bfd2-ee77606f7cba | -6.16432 | -52.82767 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 62cc0ec0-dc56-37c1-939b-bd73c18ebc53 | -9.01981 | -42.70823 | 2026-09-28 16:26:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7e5c4813-214d-319f-a439-85ec03306b73 | -10.12134 | -50.18943 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3689de9a-c744-3308-bc6b-ade42efd1901 | -7.3198 | -55.00414 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 750570b8-b274-3f49-8ac7-cb3a0a285f2c | -11.15603 | -50.072 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8afa5bff-2e33-3482-a9fc-d8d1deee10e4 | -3.97693 | -40.11136 | 2026-09-28 16:26:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d0a42c38-bb85-3109-bdd5-ea8af63cfa6d | -5.52884 | -37.0424 | 2026-09-28 16:26:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 890d789f-d021-3f1d-970a-f4f6664970e2 | -6.72268 | -45.58743 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ffc60d2-1f80-351a-a5a0-207b3f5e0a02 | -9.51216 | -46.36691 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 09aaae97-2f4b-3de0-a848-40ee07759b40 | -6.89248 | -52.48343 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0e137101-bc76-338d-aca7-6a8c77acff9a | -10.1273 | -50.19736 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4265a04c-e4a4-3cbd-8c93-ebc3e9f5f8bf | -7.51801 | -44.578 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 33d380b7-1c82-3a8d-b590-fae67cbe00de | -3.97164 | -41.52627 | 2026-09-28 16:26:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 06640caa-4f42-3b15-9663-1e2d54f00a49 | -7.59071 | -44.78457 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 53ad461a-11de-34f8-a31f-82661282187b | -10.01213 | -45.17546 | 2026-09-28 16:26:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1ccd7d24-a63c-335c-822c-df3d90b24369 | -10.5955 | -50.56524 | 2026-09-28 16:26:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2f895a18-7b30-3fae-8622-fc7022ec8f2c | -9.94794 | -49.36757 | 2026-09-28 16:26:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 83d4218d-9d83-30ed-9906-bbd1e1ba89bb | -9.50043 | -46.35623 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 83367a29-d983-3a03-b6ec-f0db2c9de55d | -7.69405 | -44.87154 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 777c08c6-f920-3559-9a26-b51577013df8 | -7.63464 | -44.61094 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a14c2f43-af5a-3f26-b505-6eb995ada74f | -10.29138 | -49.96183 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| be4f45c4-9f1a-3b4f-baea-ee9beebbcd61 | -4.21074 | -42.95145 | 2026-09-28 16:26:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef54f870-e07b-3f11-a7b1-93e64799c33a | -8.58162 | -45.08968 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7ea5367b-2fe9-3aac-b910-d0e7e18d0350 | -6.39936 | -48.2934 | 2026-09-28 16:26:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1bd28b45-968a-3be8-b7f1-d902e2d56eed | -10.11936 | -45.14354 | 2026-09-28 16:26:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 40639d63-c403-3c0b-a648-882c74332ebf | -10.92776 | -50.70767 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 682b4790-735a-38ac-9ab5-59c924b6b65e | -8.36808 | -45.40287 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |


[Clique aqui para ver as próximas entradas](README120.md)
