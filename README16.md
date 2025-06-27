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
| 410866c3-8f4f-3c27-9f3c-90258a318a34 | -13.05064 | -48.81997 | 2025-06-27 04:21:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a8e692b-631e-3f3b-bc0a-c958048e0beb | -11.67441 | -46.73333 | 2025-06-27 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6588bd0-a00c-38e5-a5b2-d8dcdaa48dd0 | -14.23905 | -45.50595 | 2025-06-27 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5af2f3d-4672-3b73-96b8-e1165d55297c | -11.68823 | -46.73198 | 2025-06-27 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d0df7c9-8273-3851-ad00-d0f1aa96f4a9 | -8.61836 | -51.583 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 47ced1d5-23fe-3e53-9ec2-66dd1bc07311 | -11.57209 | -52.10872 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 21b28049-9ed9-3bf2-a9ca-eeb9d894e827 | -11.5784 | -52.12266 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 896f20b4-1ddd-30d1-b4d4-42ce00d1fccd | -11.78142 | -55.03263 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0982252a-8708-384c-9e2f-8fa9aa777e7a | -11.584 | -44.66823 | 2025-06-27 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bd470a2-1643-33aa-b800-c113dd53f068 | -9.37249 | -47.63217 | 2025-06-27 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e49839c0-2e19-3300-a05c-83b154b23192 | -10.37165 | -51.81341 | 2025-06-27 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a4b25a7-2cb0-382f-affc-915e61004bf1 | -10.85107 | -54.03077 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48e1f093-e5fd-3960-a44e-3744ae48632e | -11.57363 | -52.10985 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| b60013fb-7474-33e1-8c52-3a2cb927cc05 | -12.76787 | -44.40107 | 2025-06-27 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebc35cad-85d9-3490-8bbe-ff1714a43c70 | -10.87927 | -49.54963 | 2025-06-27 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08f8a4d7-bfd7-3c29-ae5a-3975c72b9d0b | -11.57713 | -52.10532 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f5591e2d-54d0-33e9-a5c3-fe19ace99546 | -10.83204 | -54.05092 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 932cd1c0-4df8-31e4-9aec-379502b6e39e | -12.57974 | -57.37698 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 095e323d-af9d-306f-b2fa-c2c2efdd1e7d | -13.78444 | -54.30088 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37bcafd2-8cc4-38f5-9a06-ac22b28af03c | -14.31375 | -59.89924 | 2025-06-27 04:21:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 59ed70c7-71cc-3db1-b80d-aea8e8197dc3 | -10.77652 | -49.60303 | 2025-06-27 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f78ff89-3656-376f-9124-5249dd2e1c95 | -10.63305 | -46.69012 | 2025-06-27 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ac0f443-7eb4-3d43-8ce3-2fa85054d34d | -9.50858 | -45.42518 | 2025-06-27 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e2b3383-6f6f-36af-945e-a7157cede56c | -12.89697 | -43.7898 | 2025-06-27 04:21:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4ce666a-aefa-3775-975b-8fa234075be7 | -11.68547 | -46.7279 | 2025-06-27 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df40cc88-0bb1-3bb6-b311-795e4fb62134 | -12.01096 | -49.5225 | 2025-06-27 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e92d2d94-bd33-3d4c-85fc-490b4c9eac61 | -18.95088 | -39.90958 | 2025-06-27 04:23:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| f88327bc-c758-327b-b810-a221f690fac1 | -16.70664 | -49.35931 | 2025-06-27 04:23:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4c1f1f7-2d84-3fd1-91cf-b8961c4dd000 | -20.59966 | -45.11271 | 2025-06-27 04:23:00 | NOAA-21 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b499bd85-9573-3f92-8550-d0af597da7ab | -18.23797 | -48.34539 | 2025-06-27 04:23:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ed932ed7-9574-367d-9e4c-2b6f868c9d73 | -18.66265 | -55.75103 | 2025-06-27 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5678ade1-93b6-3aaa-8b07-2b1fc9b3270c | -21.42988 | -48.64692 | 2025-06-27 04:23:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70509bac-3c8b-3adc-847d-c37bbc4aeb82 | -20.92405 | -45.78934 | 2025-06-27 04:23:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 501534ed-15a0-36c0-93cb-dd1b5a2ca747 | -16.70728 | -49.35542 | 2025-06-27 04:23:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 451a171c-d207-37fc-8368-3627206e35bd | -22.51376 | -43.50478 | 2025-06-27 04:23:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0a1a7315-ef5a-3070-b164-c542a444d148 | -22.678 | -42.85612 | 2025-06-27 04:23:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 97c129c5-07e1-35cc-b40a-7452695af06a | -19.5791 | -49.10603 | 2025-06-27 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50f7a658-f83a-3005-92d7-31611e00b2d5 | -18.65787 | -55.74999 | 2025-06-27 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| aa2b8f96-d46d-3f4f-b24a-e0c77a442e73 | -21.10363 | -45.48617 | 2025-06-27 04:23:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7aa51eb6-56dc-3e7d-a4bd-2b913cd0f4b3 | -21.19434 | -44.93716 | 2025-06-27 04:23:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 331ee870-e7c9-3b8d-abf4-9010aef8417f | -18.44613 | -47.34985 | 2025-06-27 04:23:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 204dcc7e-b06d-3c7a-a5f0-378cbf289167 | -21.10976 | -43.81151 | 2025-06-27 04:23:00 | NOAA-21 | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 90271727-26b6-3d3b-9c73-43a2c7d86b23 | -22.90207 | -43.75233 | 2025-06-27 04:23:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1dccc8e5-10da-3aa9-b675-91cec9ebe287 | -22.78625 | -43.75523 | 2025-06-27 04:23:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e9f8934e-a117-371c-bc1c-716ee145009f | -17.45189 | -46.29356 | 2025-06-27 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 410fa900-c043-37b0-a5ac-a9d59eea02ed | -21.13307 | -47.80276 | 2025-06-27 04:23:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21d12fe6-7096-341d-a391-0e2cf88452fe | -19.68153 | -45.37902 | 2025-06-27 04:23:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c7bfa17-9b6e-3c46-b279-779a826b8825 | -18.66154 | -55.75652 | 2025-06-27 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3dd424d1-137f-378f-a94e-29adb8eaca50 | -19.57849 | -49.10977 | 2025-06-27 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9751207-ce1d-3a9c-b0f7-ed2e9331b0a3 | -22.67595 | -42.85374 | 2025-06-27 04:23:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3b750a35-a8fd-3a8d-ae92-094073b90a94 | -20.76508 | -46.77117 | 2025-06-27 04:23:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 715f9079-64d4-38be-9601-aa169b564999 | -20.47833 | -53.67715 | 2025-06-27 04:23:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 290d9479-5c5a-3f8c-ab62-099eb6aa9665 | -19.71756 | -40.35258 | 2025-06-27 04:23:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8b19a235-1013-36e0-a539-3542bfd5a1fe | -21.1802 | -43.9801 | 2025-06-27 04:23:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e95a8086-25c5-3ba0-b45f-5711a7699acc | -20.57987 | -44.57537 | 2025-06-27 04:23:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9dbee5a8-68d8-347b-9b6d-c4ead16c5496 | -20.043 | -43.53568 | 2025-06-27 04:23:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a38692a8-dfac-3ef1-af3b-e8afbf471e9b | -16.29222 | -52.93102 | 2025-06-27 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ff20df3-6bc2-320e-ab79-7907b39f4a37 | -18.42762 | -54.5588 | 2025-06-27 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd063c5f-fbd4-3acd-a312-93fbe9bfe31e | -20.70664 | -54.89008 | 2025-06-27 04:23:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d56489bb-7eed-38e6-af23-e6dab6e80fe2 | -21.11041 | -43.80652 | 2025-06-27 04:23:00 | NOAA-21 | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| db971dc2-7e65-3e49-8c47-150aaf1fc474 | -19.73693 | -54.51256 | 2025-06-27 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d99d4c7-578a-34fd-a01c-98aa5094549c | -19.57788 | -49.1135 | 2025-06-27 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94161d13-5aa4-3893-a939-37b0eb7b26a0 | -20.92348 | -45.79335 | 2025-06-27 04:23:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81a97d2e-00cd-3071-a515-a690cef9f0e9 | -16.29296 | -52.92698 | 2025-06-27 04:23:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 134e71f6-811c-3895-b182-113328c830b9 | -22.78604 | -43.75612 | 2025-06-27 04:23:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f1379cef-e8f4-3ac8-9234-c4d927c9556e | -18.75243 | -40.07677 | 2025-06-27 04:23:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 948ff7ed-a15a-3acf-9a3b-3f6c9585e27e | -19.45352 | -45.30719 | 2025-06-27 04:23:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f117a41-9ef7-3403-ae31-b984ddc5715f | -19.58183 | -49.11037 | 2025-06-27 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bbbf41d-feaa-3b93-8122-42660c7423e0 | -18.22616 | -51.71994 | 2025-06-27 04:23:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d651310-870c-3aff-b2f6-1cb05ffc51e0 | -22.50984 | -43.50383 | 2025-06-27 04:23:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 393698c2-9682-3ee9-be3f-870540ffc7ef | -18.95127 | -39.91147 | 2025-06-27 04:23:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| fa20a1c2-4009-3f95-8349-09c83e3f0a2f | -20.5961 | -45.11213 | 2025-06-27 04:23:00 | NOAA-21 | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 18a75bd3-2aba-3fe6-9f26-6b407d8ec4f0 | -17.73382 | -44.74455 | 2025-06-27 04:23:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 021d9807-92be-3902-b595-4b6391a7b87c | -20.10312 | -55.24914 | 2025-06-27 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62e04e3f-6098-37e5-9158-01207a1e503b | -19.58245 | -49.10664 | 2025-06-27 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23c970f7-ee68-3093-9c6c-c4c7c7368515 | -17.92445 | -45.5566 | 2025-06-27 04:23:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44a7f5ca-b855-3725-abe1-d1cabf73a4b8 | -20.37665 | -45.60215 | 2025-06-27 04:23:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c7a9b88-e5ee-3ecb-8638-cf07e092e75a | -20.91153 | -44.11999 | 2025-06-27 04:23:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a0df93e5-0743-3187-8815-f564532222a1 | -30.15162 | -52.02649 | 2025-06-27 04:25:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 4bb1cb69-4027-3408-95f5-bd7567313b3f | -23.40574 | -46.5586 | 2025-06-27 04:25:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| eeddf3c5-4a9a-378d-8b2b-bb5b94a7c1b9 | -30.15017 | -52.02667 | 2025-06-27 04:25:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| d34524db-ebf0-32b2-bf7b-d72c27c70cc8 | -11.5969 | -52.113 | 2025-06-27 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 14efe838-7934-30ec-a2ec-e9075bd3923a | -11.5782 | -52.094 | 2025-06-27 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 6150b88e-a1e6-38de-b95e-b8e170f0a6c9 | -6.9602 | -42.9052 | 2025-06-27 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 339.1 |
| a8e8a53b-9fde-3ea2-9568-78bae5f18ad7 | -11.559 | -52.117 | 2025-06-27 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| fa3751e8-fa6e-3c95-a9a6-52e232564172 | -11.5779 | -52.115 | 2025-06-27 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 253.0 |
| 37baf0e0-b04a-3d0e-a298-18ba78bc356e | -6.9414 | -42.907 | 2025-06-27 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 80c8a5f5-cd0b-3d56-b02c-80740cba5eca | -6.9793 | -42.8798 | 2025-06-27 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.0 |
| f8d8758b-df77-376c-8760-4cd55dd6494f | -11.5776 | -52.136 | 2025-06-27 04:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 9b047103-bb95-34b3-9d89-59144437ef21 | -6.9791 | -42.9034 | 2025-06-27 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.8 |
| ce506871-ea3f-3a3e-98b0-9c919fe89ab3 | -6.9416 | -42.8834 | 2025-06-27 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 3cc4a6f8-6dd7-3890-8881-a0a45277d053 | -6.9605 | -42.8816 | 2025-06-27 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 317.9 |
| b69e6c1e-8d96-3825-bcca-bc2e3f25f7f7 | -6.9416 | -42.8834 | 2025-06-27 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 82073dce-52ac-3ed6-b440-de1b13f083f5 | -11.5776 | -52.136 | 2025-06-27 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| be853bb8-ab61-30fe-b4fb-d8140182a73d | -11.5779 | -52.115 | 2025-06-27 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 326.3 |
| 1a335e57-5f63-3291-8da0-37388815b995 | -11.559 | -52.117 | 2025-06-27 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 8a787b2a-f89a-3e3e-9cf7-2471328ec484 | -11.5782 | -52.094 | 2025-06-27 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 7d22c21e-c9b2-32c9-adf1-9fef2a92be20 | -6.9414 | -42.907 | 2025-06-27 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 22e241ee-18d7-336f-92cb-55ba8fe6729e | -6.9605 | -42.8816 | 2025-06-27 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 264.5 |
| a61ff8d2-ec7b-30ac-ac18-a2b2b92aab82 | -6.9791 | -42.9034 | 2025-06-27 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 145.3 |


[Clique aqui para ver as próximas entradas](README17.md)
