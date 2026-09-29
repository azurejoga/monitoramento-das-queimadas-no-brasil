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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3368b62-91d5-3fef-8c18-bceb6c1bc77d | -6.51876 | -54.9614 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b6407ca-9664-3e0e-9111-2a9c47e119c4 | -11.96337 | -50.92388 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dcffd1de-69d9-3b8a-aca8-59592b8517dd | -13.16771 | -48.54248 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f9cb829-215c-3259-850f-aa0db5190ad0 | -12.05527 | -50.94252 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bf72044-67a9-391f-aac4-60f5bfcbdfab | -11.43546 | -43.45497 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17308200-90de-365f-a77c-7a9295a5ee17 | -13.43617 | -48.62176 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9be3ef2e-4d9e-35ae-b889-efff5a7db701 | -12.69986 | -47.36798 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4adeb407-92d7-3211-a303-d3ecd3ac3c4b | -12.03642 | -46.50686 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10e38aad-9dbc-35da-9de5-066bf21cc477 | -12.90485 | -52.03693 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7da5bc0f-d4f4-3172-84f3-ceb3ed102375 | -8.23114 | -45.40244 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f88f9cd7-b711-31f9-a8b6-95cd46cb547f | -7.56885 | -47.36544 | 2026-09-29 04:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c741301-2688-3b19-ab85-b1e2c0ecb9b8 | -12.69058 | -47.38009 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37e21c94-9c95-3aba-bba4-2103c859bfee | -12.69726 | -47.25456 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2aaef69-0e5f-37d0-9885-1586d17e6429 | -11.39949 | -43.41849 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25a0a231-7b4c-3030-859e-d7873bfba3d8 | -13.56157 | -48.93878 | 2026-09-29 04:51:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff2c4ef4-936a-3485-af74-a0ccfb1cc0f5 | -12.01586 | -50.9324 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e1a78b45-9c7e-3f11-9b66-e9c215990068 | -9.95634 | -50.147 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 097d3d34-2c01-37c6-b3e3-c321425a650a | -12.27755 | -50.26338 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8489772-102b-3d2a-a312-2f6f25ade090 | -10.80727 | -48.723 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 500c031d-deee-39d5-84b3-a0e9e7e0d3bf | -6.91465 | -45.5936 | 2026-09-29 04:51:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 099cd033-1c8b-3a8d-ac01-1677598e27ef | -9.9519 | -50.15347 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d6592c1-27f0-322d-aaab-fbc43824015b | -12.05194 | -50.94197 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c81c280-dd0a-320c-93d3-40dce011761f | -11.17025 | -50.04261 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 493547ab-fd9f-3eb7-92d7-16f9f7ea8915 | -6.13512 | -53.0587 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18d1c998-c8a5-30f6-ade4-6372eb5ea4c1 | -7.40567 | -42.61721 | 2026-09-29 04:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c4cccb32-fda1-33fa-8834-d922f56fe3e8 | -12.03139 | -50.94222 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afb3f65b-80ef-3488-b36d-766579696ff9 | -8.73402 | -44.92709 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2893f383-9ca8-3917-b848-0c00ebdc7270 | -12.94306 | -46.64009 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d3c60fa-64ea-303c-a1ef-1136eeb1c2c0 | -11.39048 | -47.45408 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 967825b4-6b56-3d1e-b749-578ff31ac61a | -13.5581 | -48.93824 | 2026-09-29 04:51:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4378bea-8e93-3776-8fe2-01985d1b98bb | -9.79888 | -44.83418 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8a913e0-e704-367e-a5b3-5fb0e7ef1d02 | -12.9553 | -46.63706 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e071e2d9-081a-394b-92c8-d469d1d231c7 | -12.88369 | -44.81633 | 2026-09-29 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b6261e1-e2ad-3063-998d-2585ff87a449 | -19.00482 | -47.8744 | 2026-09-29 04:53:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28cd6acd-5733-3c7f-b154-cb6acf8cec7a | -15.24696 | -43.27236 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 50.2 |
| a14a07c3-7ec1-38bb-a51d-d65909bf8bde | -15.08664 | -48.3309 | 2026-09-29 04:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 347e104d-7e9a-34cd-a44d-ed28cd6c2e39 | -15.44445 | -46.14404 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 354711a4-39e5-3cbc-be13-0128c6d3309b | -16.02283 | -52.50349 | 2026-09-29 04:53:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2a9c74b-2ac1-382d-9107-e0b406736812 | -15.22232 | -46.17104 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6a531f4-1374-3063-a34c-ff92c0e3bfde | -15.89708 | -48.07124 | 2026-09-29 04:53:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d0b456d-7139-3c82-a0c7-c3d0de731501 | -15.38443 | -47.92032 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a82b3da8-9579-363c-8148-9295e1a30d7a | -17.61864 | -46.66446 | 2026-09-29 04:53:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15758b1b-6113-3b0e-8d36-b514b1d9f403 | -14.53637 | -48.30611 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96113a5a-0ac5-3c2e-82a8-f0091b1b7f96 | -15.45314 | -46.1417 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 825e5c0f-fe3c-3247-8a9e-243db9cbda07 | -14.97098 | -46.26431 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7096a77d-1db7-3ac6-92fb-bbf023bb5009 | -19.36259 | -41.50288 | 2026-09-29 04:53:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 402ddd19-d229-3a61-8d05-408f76381141 | -15.08241 | -48.33459 | 2026-09-29 04:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9828127f-3ffe-3a67-b715-95086c5b4702 | -15.45411 | -46.13442 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4066c56-1d3d-386c-aced-c80e4380b2a7 | -15.89619 | -48.06882 | 2026-09-29 04:53:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbd0f9da-d73c-3c7b-ae7d-5e166af3cb8b | -19.02987 | -46.96722 | 2026-09-29 04:53:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 333b3537-f401-3e34-9d0d-55a51995c8e8 | -15.45723 | -46.14241 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f078bffa-a03e-382b-81ef-532007297737 | -15.38584 | -47.92269 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1bae28e0-a54c-32e3-a29d-3d2b7875a5ca | -17.78883 | -47.15955 | 2026-09-29 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 561530c5-a870-3806-9762-4c5f514a1a9a | -15.17132 | -48.67812 | 2026-09-29 04:53:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10dff65b-a7ab-36fc-8adc-62670b4f1ef9 | -15.00131 | -47.86399 | 2026-09-29 04:53:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33c7cf37-327c-32db-a3ca-709f8b7ed611 | -15.17035 | -46.1344 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64ac5053-f149-319d-b05b-b9df7a3d192c | -18.76527 | -47.6158 | 2026-09-29 04:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b259279-10af-3181-a740-7dfbf352cd32 | -17.86926 | -48.61266 | 2026-09-29 04:53:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64b1aea9-2e77-3f00-b5d5-5d7b5940de87 | -15.1335 | -43.62468 | 2026-09-29 04:53:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 98b0e26c-01e8-3d8a-b9a8-cdb833d97e25 | -16.81821 | -48.99385 | 2026-09-29 04:53:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8455e2a-dcc7-35be-af7d-267fbd4e5830 | -14.21984 | -48.50719 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0ce768f-6c86-39a5-a95c-3d934dcb1cc9 | -15.73303 | -46.03082 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 265fa7ee-0365-30ab-b6cb-63a5fbce0af4 | -15.7377 | -46.02756 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2218e614-3580-3d9f-a65a-d863032e032c | -15.38943 | -47.91188 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fde401dc-cdf6-36c3-9222-59bc8a0c644d | -18.10985 | -44.35351 | 2026-09-29 04:53:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b76e62a4-1827-311e-8418-c2a45973320a | -16.33529 | -47.69553 | 2026-09-29 04:53:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4172d35-577e-3513-bf74-2da7cf05dee1 | -15.16776 | -48.67761 | 2026-09-29 04:53:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 893802cc-643b-383c-b670-5de42c3444e8 | -15.08603 | -48.33509 | 2026-09-29 04:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| baf6aba2-9f13-3b4a-b2df-ec71126a033d | -15.16985 | -46.13808 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0978824-1c09-35ba-b196-c54355ab00c6 | -14.80094 | -45.95763 | 2026-09-29 04:53:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dfdeceb-3639-3822-982b-1ee8d99c0e95 | -15.46227 | -46.13602 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4d2d8bcb-70f1-32ca-b8a5-2e8b020407a8 | -15.86848 | -40.45985 | 2026-09-29 04:53:00 | NPP-375D | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9d32019e-ca93-3372-b6ae-23db197fed3a | -15.22541 | -46.17915 | 2026-09-29 04:53:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5493ef3d-2bf2-381a-887f-f1db5d590428 | -14.09905 | -54.30254 | 2026-09-29 04:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4159d4a-e1ef-3499-889f-f8b417a91a52 | -15.34019 | -48.12129 | 2026-09-29 04:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f588f26-e57d-32d0-bb0a-adc6607fac15 | -14.21277 | -48.50602 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3325a7e7-5df2-3954-b35c-7822a57ee887 | -16.22657 | -48.06552 | 2026-09-29 04:53:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcb18bbe-09e8-361b-ac2d-c4612fee5634 | -14.79164 | -45.9497 | 2026-09-29 04:53:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dc7d4ee-9aa8-3398-8fe4-3adb483ef554 | -18.10937 | -44.35452 | 2026-09-29 04:53:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2a07ce8-f939-3535-a3df-2f2458bd1fdf | -15.3871 | -47.9137 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bcc2354-7e83-3833-9d74-915fe025d3ef | -15.38508 | -47.91581 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 528aefc6-54bb-36b0-8b19-452852dee8a9 | -18.10455 | -44.35404 | 2026-09-29 04:53:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1162b395-54f0-3c90-bbcd-c61d1afa7a8b | -15.242 | -43.27171 | 2026-09-29 04:53:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 89.7 |
| c248fe93-fa2c-3424-98a3-03e2786bab99 | -14.52325 | -48.29546 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f191ef8c-a5d7-3d03-87dd-35d99d0a1541 | -15.39206 | -47.90517 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24f49eba-44dd-3631-bf7f-7b0bdb839b5a | -18.11418 | -44.35498 | 2026-09-29 04:53:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e31750ca-996c-3ffe-a42e-69f1b260f81f | -15.83433 | -42.56247 | 2026-09-29 04:53:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 53891f6c-3ee6-3cef-93ac-19bd0e48f045 | -15.38379 | -47.92469 | 2026-09-29 04:53:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f4dd56e-295c-3f32-9c0a-20e83bc4ae5b | -15.45676 | -46.14594 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 794d333d-1072-306a-8502-44a83291b620 | -14.51606 | -48.29434 | 2026-09-29 04:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7c689bf-983f-3a86-ab5e-2307ac930e67 | -16.35601 | -42.58896 | 2026-09-29 04:53:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f88cff92-4b70-35be-9eae-ef8ce151c23c | -17.86765 | -48.61455 | 2026-09-29 04:53:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f566eaf-fbd1-3b50-a9b5-03ebcb9a4ee1 | -17.65592 | -46.53811 | 2026-09-29 04:53:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74de5b8a-acff-34a2-bd23-ed442b6bbd66 | -18.68271 | -48.62824 | 2026-09-29 04:53:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13290701-ae2c-39c1-abeb-a6bd6baf1dbf | -15.4577 | -46.13892 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dc187e0-dd05-39ad-bbd5-cf89ead11744 | -15.72836 | -46.03402 | 2026-09-29 04:53:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d581ce1c-c8f3-3bad-b782-9bb19f22b205 | -15.86887 | -40.45635 | 2026-09-29 04:53:00 | NPP-375D | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b36c24db-271b-314d-be20-bda46ca9925d | -19.1883 | -46.81218 | 2026-09-29 04:53:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a935ff8d-8142-3a97-ae29-1fbd6333db79 | -15.09304 | -53.87891 | 2026-09-29 04:53:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f8c27a7-bfef-369c-b591-5228dd4d3394 | -15.87005 | -40.45739 | 2026-09-29 04:53:00 | NPP-375D | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |


[Clique aqui para ver as próximas entradas](README51.md)
