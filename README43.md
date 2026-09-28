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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85d4f51c-9a36-3ed2-a091-e8ee2bfbeb01 | -15.43611 | -56.06533 | 2026-09-28 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4d29ab0-b68d-3050-9da7-ea21766f7c6e | -16.00085 | -47.73896 | 2026-09-28 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b203f6ae-3dfd-33c7-bb6d-2551e106a974 | -13.45225 | -48.59844 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7dbcffad-7fb0-3af6-9d46-88915d097e14 | -14.52732 | -48.30854 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 71649376-0c55-36c8-9615-d848c3a576cb | -19.30235 | -45.45848 | 2026-09-28 04:36:00 | NOAA-21 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 346eb95d-dfd8-338f-b559-43c869da7788 | -15.16854 | -46.1484 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f0f0e7a-1ae8-3c90-993d-a5b7e505a090 | -14.08897 | -46.32224 | 2026-09-28 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97221a84-faaf-3182-a8ba-67025af23d82 | -15.16729 | -46.15767 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 298ec467-b6a0-317f-8779-4941ccbc2cd7 | -15.41247 | -47.9307 | 2026-09-28 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bb3be654-4d25-37d9-addf-4b5170330eed | -13.71844 | -48.81341 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3e7770aa-507f-3b77-9e7c-fcf9da08d38f | -17.25234 | -42.82966 | 2026-09-28 04:36:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1a464fc-32f2-3625-b3a4-a4948d84bf7d | -13.47172 | -48.60521 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67c59e16-c8fd-374c-a015-0c95f7c1fc4f | -14.5959 | -45.59423 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aad11a98-f3e3-3eeb-bb2a-c1adaecf30e9 | -17.58236 | -44.29591 | 2026-09-28 04:36:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f48d5cb-5d79-30e0-a016-add9e4aeceac | -15.1729 | -46.14444 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ebeea32d-4a0f-3d95-9514-87f9222790c8 | -14.11831 | -46.29938 | 2026-09-28 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5cd0957b-effb-3cdf-9fa4-d229699b90b0 | -15.14283 | -43.62732 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8d93daa1-db6e-3e07-bd3e-2d83f5bd3ad9 | -14.5213 | -48.3158 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b910c375-518f-3409-bc10-b1930d0381d4 | -13.68331 | -48.82266 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc231c1d-dddf-372f-b398-ea32ebbbdc3b | -15.4084 | -47.9104 | 2026-09-28 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 22adb24c-abab-3b8a-8fc9-6e8469fd1632 | -18.1026 | -44.36349 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 12c0cc07-8649-3f9e-ab68-af89f0f04efa | -12.8095 | -54.00846 | 2026-09-28 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b9bf115-4237-3ebc-b918-e628513ca422 | -18.12332 | -44.37479 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0953c37-6df6-367c-854d-9bc3eb67d357 | -14.47986 | -53.64548 | 2026-09-28 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1553359b-57f9-3296-b3fa-a7060e82ba23 | -14.71625 | -45.58059 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ebea00ec-5a13-3c0d-a9ac-50c73476aa69 | -14.52185 | -48.31211 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87ecdafb-0b72-3182-aa8b-6925410242c0 | -14.79968 | -45.96157 | 2026-09-28 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b56da07a-1aaf-364f-b8b4-d96aebd85d91 | -18.10973 | -44.37777 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 52f1dd72-c68b-3a29-bc02-ce2abf21cc97 | -22.34624 | -46.95913 | 2026-09-28 04:38:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ae61e58-6fb3-3615-adb2-15a06bfdb0c8 | -21.51996 | -45.11607 | 2026-09-28 04:38:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 39faf3cc-7123-3309-9077-ee6994ced5b1 | -21.02463 | -47.26083 | 2026-09-28 04:38:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fd699b4-4c2f-3a94-b86b-e7a2cc567e90 | -22.10488 | -46.81386 | 2026-09-28 04:38:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa0a12d5-15f7-3ed1-a47b-677d7d85b272 | -22.10132 | -46.81149 | 2026-09-28 04:38:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c27bcd90-b7c4-3fad-9a56-4239b7186f93 | -19.77253 | -50.29142 | 2026-09-28 04:38:00 | NOAA-21 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| d01eeaae-f03f-3651-a978-b33bc938719f | -20.59974 | -52.46021 | 2026-09-28 04:38:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d20b2972-302c-35f0-836d-4b30c545a717 | -21.52482 | -45.11219 | 2026-09-28 04:38:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| eb987fb1-5ebb-3d7e-9e8f-4558ec0d3a33 | -21.1409 | -48.58668 | 2026-09-28 04:38:00 | NOAA-21 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c159de83-731a-3adc-915a-69f24ff4b8b8 | -21.52048 | -45.11168 | 2026-09-28 04:38:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| b3079009-20f4-3eaf-9814-4ce171f6edd4 | -20.83657 | -57.69681 | 2026-09-28 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2bb053bc-2284-30a9-9f5c-d226a675c64c | -21.0621 | -46.94345 | 2026-09-28 04:38:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 821f78c3-79df-33ce-9279-05e6e27adac8 | -20.185 | -48.58118 | 2026-09-28 04:38:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 14095038-45ee-3065-82a1-cb031f53eaca | -20.87598 | -44.1169 | 2026-09-28 04:38:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aed0ef00-2987-3b10-a80d-8e64c3d8236b | -23.32276 | -52.31354 | 2026-09-28 04:38:00 | NOAA-21 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b4838cb2-2840-3b44-aa56-ebd2346613d6 | -21.22498 | -44.32929 | 2026-09-28 04:38:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a172f49d-1bc2-327d-885b-422d1254310f | -20.18793 | -48.58587 | 2026-09-28 04:38:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e2f08769-e658-3e6f-808d-a45d05ed6886 | -21.51614 | -45.11113 | 2026-09-28 04:38:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bb2e3cbc-436f-3d0b-ae0c-a2653938b3d3 | -23.32606 | -52.31416 | 2026-09-28 04:38:00 | NOAA-21 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 58394557-4f22-311b-aa0f-c74a4847bad0 | -20.84079 | -57.69772 | 2026-09-28 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7d941c98-6609-30a4-837f-6bfec5bf495c | -21.39092 | -48.71003 | 2026-09-28 04:38:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de31b3d9-2000-3054-8e6a-a11e159e1387 | -21.52533 | -45.10788 | 2026-09-28 04:38:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f542752a-33be-3a50-9826-a5538847f8a0 | -21.5243 | -45.11658 | 2026-09-28 04:38:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f018e857-9f3d-3148-a85f-21db85a6926a | -20.18033 | -48.5889 | 2026-09-28 04:38:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b7a3352f-4a1e-3cef-afa2-9fb2a603bca6 | -28.75557 | -55.59949 | 2026-09-28 04:40:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| cb512865-d246-3477-a90b-f24e3637c3e5 | -28.75825 | -55.60444 | 2026-09-28 04:40:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 74437210-16b9-3494-b4f3-7929d5d465ef | -28.75216 | -55.59875 | 2026-09-28 04:40:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 788925ea-748c-31ec-8f72-c74e7699ccb0 | -2.86759 | -49.63494 | 2026-09-28 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09685c81-20f7-36b7-96fb-c08d64183381 | -1.75331 | -55.2835 | 2026-09-28 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f3c702a-10d1-3035-9b09-90a5064e4229 | -1.77445 | -53.7648 | 2026-09-28 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ebf7e9f5-fce0-3c49-a24f-68af16326958 | -1.80808 | -54.87205 | 2026-09-28 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d17f3fab-5ce7-31d9-8504-8769e799af82 | 4.30795 | -60.82622 | 2026-09-28 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4d0c6a9-b0b5-39d7-b3ff-ba88f70c9f3b | -0.52988 | -49.19349 | 2026-09-28 05:08:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 295b107f-2528-3fae-816c-0f035075ed29 | -1.77056 | -53.76775 | 2026-09-28 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5790c992-f1da-333c-a53c-21b07fad2e6e | 1.67466 | -55.94276 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36f4208d-fb50-335c-81f7-062f16fac374 | -1.74131 | -57.17985 | 2026-09-28 05:08:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 46949a4a-d73e-31f4-a5ea-85e6ea38d138 | -1.27358 | -49.36838 | 2026-09-28 05:08:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95e8e76d-7230-3b7d-a9ca-39463f120faf | -1.8115 | -54.87259 | 2026-09-28 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa9f3192-26e9-3b93-b453-ef4504094ac6 | -2.27178 | -52.0157 | 2026-09-28 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 829c6c73-a512-37d9-a869-0769ee7dde7c | -1.64444 | -55.10816 | 2026-09-28 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e4e132a-bad8-3145-8990-c76fbb11458c | -1.82043 | -55.31662 | 2026-09-28 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a5fdf28-5dda-30f5-a71f-c16341fa0f38 | -2.44546 | -49.22499 | 2026-09-28 05:08:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95e5fe71-b52d-3155-8874-56ed11a5d44e | -2.77519 | -49.48495 | 2026-09-28 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a946292-c445-327a-b93f-6ef4f141e88b | -3.93881 | -42.55118 | 2026-09-28 05:08:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| c260bf2b-a877-3a73-92e8-84e0bec039f3 | 4.31214 | -60.81755 | 2026-09-28 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12a57ff8-5aca-319f-80a5-7d37d83f18c4 | -1.76722 | -53.76723 | 2026-09-28 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ca535ec-56ba-3c8a-953d-d5b28f2b0875 | -2.26841 | -52.01517 | 2026-09-28 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a97cbe53-6e76-3276-9135-34a5e3b8a879 | -1.26162 | -54.68464 | 2026-09-28 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75a78ace-aac4-3eb7-bcfc-efb79495d25b | 1.67264 | -55.92957 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad3345e1-e700-3c94-9ca3-1804f6dc89fc | -1.90815 | -52.06439 | 2026-09-28 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94548691-2e36-31c6-a2bc-c94726b52e22 | 0.28342 | -50.9096 | 2026-09-28 05:08:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 45193232-e285-3725-a151-5091f8854a55 | -1.80377 | -48.06068 | 2026-09-28 05:08:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22ffa20f-8d72-31a0-8adf-f12dd7ecb5cc | -2.7358 | -49.46501 | 2026-09-28 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec556558-10f0-3d9d-b444-d2ea4e9e1a28 | 4.3449 | -60.70869 | 2026-09-28 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2e980848-b19d-3504-8261-a89035384d87 | -3.37272 | -44.37226 | 2026-09-28 05:08:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edcfc6b3-fca3-3f40-aa23-22cfc56829d0 | -1.92666 | -52.14318 | 2026-09-28 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0d7e481-03cb-379d-8afe-ef3bfb94ccd7 | -1.78845 | -47.94447 | 2026-09-28 05:08:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a62d04c9-705c-311b-8a63-2c6b808c3232 | 0.46831 | -50.97456 | 2026-09-28 05:08:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3065fd44-5b0a-387a-8106-ea642c3a398d | -0.93855 | -47.55401 | 2026-09-28 05:08:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a562b8b-1ad0-3883-af15-61a700a073b0 | 1.67006 | -55.92377 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f77bc9b-122c-3bf1-b33f-4b70eb907c5e | -1.75391 | -55.2797 | 2026-09-28 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1e87b92-e0ad-303c-bbff-15e773e34e40 | 1.65175 | -55.90427 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 270fd4f8-ef25-3068-ae15-b315f1c58ce1 | 0.4767 | -50.93965 | 2026-09-28 05:08:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3585a5da-9a05-349d-ae0c-e1d2fb92a842 | 1.67601 | -55.95155 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b591049b-b202-3216-a358-a52444d9d452 | 1.67868 | -55.95391 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6649c8e-3699-3706-a77c-16800da39b3f | -1.76777 | -53.76375 | 2026-09-28 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 900325da-a99b-39ef-85ac-4a946b0d0640 | -2.77143 | -49.48436 | 2026-09-28 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d6820ab9-eb39-3fba-8b3b-17111152e26d | -2.98753 | -49.1024 | 2026-09-28 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82dbce40-c128-3933-8e28-4fc3c68987d7 | -1.85733 | -47.97752 | 2026-09-28 05:08:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 186918bf-03ae-3261-b2e1-928ed97d9987 | 1.67566 | -55.95889 | 2026-09-28 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6ea7580-d92f-3837-ba43-668a0ed3bbb8 | 1.26739 | -50.6874 | 2026-09-28 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6344e31c-519e-330a-9c9e-8da791a10f8b | 1.83386 | -50.86767 | 2026-09-28 05:08:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README44.md)
