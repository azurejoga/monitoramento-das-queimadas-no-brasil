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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06159462-7522-32e6-a1f9-0ee5daaa0df1 | -11.4898 | -45.09604 | 2026-09-01 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19305e8c-3192-3cdf-8195-e3a27ac82988 | -11.24997 | -45.14227 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a8cc6e6-f7f6-3c7b-950e-2f92072d5418 | -11.66937 | -47.61057 | 2026-09-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b05402e-fafd-308a-8769-5471cbf55c10 | -11.36996 | -45.23259 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ac5c359-4005-3c35-a847-f6a317345113 | -9.98702 | -46.44112 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86106d35-a06c-3dc8-b619-1082eb7f7d71 | -11.31899 | -45.17686 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f261b951-b80a-388a-b233-5451e90f5fbf | -13.27824 | -48.55212 | 2026-09-01 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 356f0506-b211-3f7e-9270-75959e4d892a | -10.32879 | -49.95101 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 501ac436-db32-35ba-a3dd-49e257cf14a4 | -10.0608 | -46.65519 | 2026-09-01 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99db6f75-4690-332e-81cb-56b6cbad668e | -10.20955 | -50.31701 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3cc0ef55-89fa-3244-bea3-9b2bd0612e07 | -11.26503 | -50.57914 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9f8efcf9-725a-3dcd-87fe-0983536d50a7 | -12.10041 | -44.98452 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae92c999-6aad-3f19-be74-f762d6b10d56 | -11.28917 | -50.59125 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 0f0d34a8-7c47-3942-9843-a108384d8017 | -11.2757 | -50.593 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1451bd3a-84a2-3baf-8ade-4798a070bf41 | -10.00796 | -46.4421 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| efcc6d7e-d7f2-30f3-bfbe-a732a2534690 | -11.27037 | -50.58605 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 17e4ead1-9f23-393d-b731-22ac6f12a8ec | -11.11064 | -51.5462 | 2026-09-01 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 129524cd-d657-34cb-85b1-8794c984daae | -8.84979 | -47.08232 | 2026-09-01 03:55:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36e3697b-3bca-3382-8094-2fd401a0f24b | -13.32348 | -51.72597 | 2026-09-01 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9dd90836-5bd7-3123-84f3-2a770341f53b | -11.28327 | -50.58889 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| a450e15a-d354-39e5-b9d6-5ce778847fe0 | -15.6665 | -45.90933 | 2026-09-01 03:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78aa9299-854e-3a81-b8f9-90d4db609e3a | -15.66632 | -48.70388 | 2026-09-01 03:57:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df7a356d-5dd8-3291-ba47-e7a31b4ddd52 | -14.39007 | -52.52306 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7474331a-9b60-3a99-97a7-69bfd1e678de | -15.06234 | -48.38697 | 2026-09-01 03:57:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6dc1f61-fbde-3bab-91f1-94bc69a4c1bf | -21.87441 | -42.03612 | 2026-09-01 03:57:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 46857f62-2490-3556-8f63-90e8ddbfb331 | -14.25453 | -52.87064 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a759e39-aa10-3ad1-9fed-6f3823099938 | -15.66713 | -47.26929 | 2026-09-01 03:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27a82bb3-27e9-3ab3-a42d-ab2cdad3595f | -21.24894 | -44.44788 | 2026-09-01 03:57:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e0f95ce4-d5eb-372f-baff-2133c9e380b8 | -17.38702 | -42.35484 | 2026-09-01 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f648f613-0fdf-3a4c-b4f1-29ee917a1b0f | -19.34034 | -41.64811 | 2026-09-01 03:57:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a24d5bc3-9f57-37a5-894f-b08f0e38edd2 | -14.25836 | -52.88621 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 712929ac-93be-3080-9c2c-2aea24faee40 | -19.39073 | -40.87248 | 2026-09-01 03:57:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c4a4e041-5cc1-312a-8f6e-1bde9f3799e1 | -16.61024 | -43.3751 | 2026-09-01 03:57:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 334a4ae4-1bed-32e4-9789-6fa208793821 | -14.27313 | -52.89755 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f0d261d-0a43-3ebc-bf8a-a8fc66f274b4 | -19.39467 | -40.86929 | 2026-09-01 03:57:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 45143cb0-a90b-31d0-9270-1b33eee38113 | -15.66668 | -45.95767 | 2026-09-01 03:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19939c2b-9029-39cd-9546-241d6b419114 | -18.25677 | -52.74285 | 2026-09-01 03:57:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c298b89b-ca91-3765-86af-33e4b292e5ca | -20.47713 | -45.68541 | 2026-09-01 03:57:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f60986c7-5008-3992-b597-55b8bdc27c54 | -19.56825 | -45.7179 | 2026-09-01 03:57:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc96ba80-1331-3b80-989c-6a47a41baa13 | -18.2517 | -52.73534 | 2026-09-01 03:57:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 858e1f11-b4ef-3348-8bcc-8f4e1a704a1c | -17.38628 | -42.35915 | 2026-09-01 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 80c3fe89-2edc-39c7-a23b-5567f9422a8c | -15.03224 | -52.76799 | 2026-09-01 03:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72cdc594-4c49-3ad5-aec9-07a1d61f417c | -14.26151 | -52.87223 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13d49d69-7c6e-3604-ba2b-165ac2cb46ab | -15.67089 | -45.91051 | 2026-09-01 03:57:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8aa11b4c-d21e-37c4-95e0-e2c54a9b5177 | -16.47399 | -47.94895 | 2026-09-01 03:57:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 38.6 |
| bec09736-dc5f-318e-8957-ac2e7dffe377 | -19.39406 | -40.87304 | 2026-09-01 03:57:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 98224ceb-fc4d-3525-8db6-686a56b4a51c | -17.3813 | -42.3669 | 2026-09-01 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82ad44fb-43c8-37ed-86db-9e82f7106c0a | -16.08574 | -48.05072 | 2026-09-01 03:57:00 | NOAA-20 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02b8efc3-c240-3bbd-a12f-93af35b35eb1 | -14.25681 | -52.87163 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e60bea5-6530-3537-84e2-137b86d18919 | -14.25376 | -52.88557 | 2026-09-01 03:57:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4012b9cb-ebd2-394b-873c-7112a62c97b8 | -15.0241 | -52.77231 | 2026-09-01 03:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e32cdb73-c13d-31c6-b5c4-6fb7d0729aa5 | -14.39151 | -52.51656 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bdca56c4-4b9b-34cd-8edc-840ef58ce0be | -17.13603 | -46.83721 | 2026-09-01 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 547990fa-65ee-3dd1-a6bb-63ee905ab9a3 | -14.46954 | -52.52163 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| dd86ead7-8cf1-362b-af6e-b5268a373259 | -18.9535 | -45.37827 | 2026-09-01 03:57:00 | NOAA-20 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 603806a3-fd69-32f1-8c3e-2917553558f5 | -17.38202 | -42.36269 | 2026-09-01 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b92d8be-306a-3adf-85d7-6e038a9b407f | -15.58953 | -46.46017 | 2026-09-01 03:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6540a03a-a6fc-3fe7-9c1e-d256a2aaf1ff | -15.63114 | -50.10809 | 2026-09-01 03:57:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e2d998b-cf6b-34ec-9502-d01631279239 | -17.14156 | -46.83332 | 2026-09-01 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 09a11180-9185-30d3-84b2-a82fa5353819 | -16.50373 | -41.74569 | 2026-09-01 03:57:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8582e803-c9fc-3009-aa65-726b9715ab05 | -17.79478 | -39.70288 | 2026-09-01 03:57:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 266499c4-3eeb-38ba-9c0f-5c40c8034f3c | -17.14062 | -46.83821 | 2026-09-01 03:57:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e6b1882-5e58-3a11-ba32-1e895a90a2a2 | -19.11466 | -39.75264 | 2026-09-01 03:57:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3aa8439e-b54c-3eba-bddc-c073e945df6a | -15.02543 | -52.76626 | 2026-09-01 03:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b47422e-2ec5-328c-b6ee-5e9cf3599d73 | -14.45684 | -52.51247 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ecf793d-7368-3def-a892-55c31365b8a5 | -14.39976 | -52.51162 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b2ab1feb-d366-33fc-9cf8-8e0d6ab60f48 | -21.24709 | -44.52153 | 2026-09-01 03:57:00 | NOAA-20 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9f6202d6-b86b-3fc0-91c9-baaa833ee13f | -17.37562 | -42.37873 | 2026-09-01 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 97f30a23-cccb-3835-a16f-97a48cda2704 | -16.30207 | -42.03483 | 2026-09-01 03:57:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a95e95e1-dc05-3f21-b2bf-8b87725a8122 | -17.3721 | -42.378 | 2026-09-01 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0054a18a-5855-34a2-a3a0-919b4013c79b | -19.39133 | -40.86874 | 2026-09-01 03:57:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f69391ec-659a-3da9-9af5-a1200a640f3a | -15.03186 | -52.76948 | 2026-09-01 03:57:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 955b6ce5-d8c6-3f89-8878-c3a77a9b6a08 | -20.16426 | -44.34957 | 2026-09-01 03:57:00 | NOAA-20 | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 504a4bd2-87ce-30f3-bf6f-3460a7cca095 | -18.00423 | -42.69293 | 2026-09-01 03:57:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a44d50db-5a1c-3038-9eb8-3bdaee7d67f4 | -14.40113 | -52.50542 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b0752c31-41f7-33b3-84f0-547c3b3c7d74 | -14.408 | -52.5067 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9e032eff-04bd-33b8-920d-9c5726802df4 | -15.29584 | -53.18959 | 2026-09-01 03:57:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6081a87a-d7ba-35f3-aea5-7bf9a8aaeeda | -14.44333 | -52.50879 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 41bdb70f-960e-3fcc-b8a2-793d3f7fbd56 | -16.3668 | -46.87851 | 2026-09-01 03:57:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d54e1d66-4a06-3fc5-901a-47ffe1d30728 | -14.43649 | -52.50737 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f9b8266-726f-3679-a981-ad2f81fe9d0c | -16.47887 | -47.95061 | 2026-09-01 03:57:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| d0fb1ec2-eb53-3178-89e3-f8c1fd0d4998 | -18.7016 | -46.59874 | 2026-09-01 03:57:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f698f9c8-1451-3128-a2bf-1fe529d92bdd | -14.4508 | -52.50935 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 794043ba-f0b4-3233-8f19-df1ec3501d9f | -14.46094 | -52.52659 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ce9f0b61-a796-3a60-aa6a-f7679d7870a1 | -15.83384 | -47.67906 | 2026-09-01 03:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a8a93808-2c6a-3e28-913d-633846b852e6 | -17.90368 | -50.64445 | 2026-09-01 03:57:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6f56384-1203-3ac1-a148-cdf7acd3656a | -20.47785 | -45.68164 | 2026-09-01 03:57:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24e749f0-5294-37f8-82a1-2ab4d9f22685 | -14.45502 | -52.52248 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 450bf56a-6677-35b2-93c5-80edca9f1651 | -15.637 | -50.10916 | 2026-09-01 03:57:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac22bda7-a21c-344e-8ef7-283b32f6d356 | -14.43718 | -52.50621 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45b0a1ff-2d61-39a0-9514-8baddb689948 | -18.30537 | -43.33694 | 2026-09-01 03:57:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e93c949-5a09-365c-a198-e8c4fcf10367 | -14.25921 | -52.89419 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d8db513-6417-3898-9921-a1503efa3eda | -19.20279 | -46.8016 | 2026-09-01 03:57:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfa70f79-d2b3-313b-a759-3de191dfcb0c | -14.45565 | -52.51796 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6364c8e8-dd16-38f9-805e-3a41778b5a37 | -16.47341 | -47.95189 | 2026-09-01 03:57:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 38.6 |
| c4aef09b-c087-3f72-b3de-4dfe03b77fe1 | -17.3898 | -42.35984 | 2026-09-01 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 205bdc7d-c71d-3254-a645-589b8e59a2e3 | -14.38017 | -52.53543 | 2026-09-01 03:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d70e48bb-c9a4-3134-b6a4-f59df1fe610e | -15.66565 | -48.7072 | 2026-09-01 03:57:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e77e9c1-69fc-3923-b85a-f141f2d3f26d | -21.86494 | -42.03044 | 2026-09-01 03:57:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dde5e49e-a779-38c7-b0e8-e5bdcbe3e393 | -14.25141 | -52.88448 | 2026-09-01 03:57:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README28.md)
