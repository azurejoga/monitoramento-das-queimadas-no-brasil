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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfeadca9-6a53-366d-83c3-3fb1d03a703d | -9.71893 | -48.33785 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 598b1d7d-f067-3f02-bdbc-18dca2eff885 | -12.93231 | -54.80476 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 789fe89f-a451-39a5-8c3e-fb76722286da | -12.13527 | -44.85427 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cd1844f-5d4b-3a64-a97a-22e34e9490dd | -12.23603 | -47.30989 | 2025-09-11 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0abeccf-551d-3ef8-b368-759ed420928b | -9.01383 | -49.76744 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5eeb09f-93f5-381b-9cef-6fbf3ed01cb1 | -15.23049 | -44.0453 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f6e0c2d-2581-374d-a36b-7c116b8587a4 | -12.03388 | -47.54097 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 168fa8c5-20ad-3e5b-8ce9-abb25c3aab24 | -11.40362 | -45.59887 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e5a2833-79de-3573-994a-8fe765bc23a7 | -9.68724 | -46.75789 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36b07a03-8553-31e2-9b45-2459227efaf9 | -12.88015 | -47.96025 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5908aa9-fa78-39ac-9668-be73dd38f1bd | -10.71343 | -48.30488 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42f475b6-0cc2-35f2-8ed3-60ab2eb907cb | -12.94575 | -54.81709 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b137ea7-9331-3536-b7ef-9719f94b78fd | -11.34072 | -46.48989 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f073b152-05a3-327e-8779-c2d67645c684 | -11.4751 | -43.63462 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e41d46f9-079f-3054-82ff-4d73a990f881 | -9.05215 | -46.97105 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc425d81-a04c-37ec-919a-18ac4e6ee6cc | -12.977 | -46.72547 | 2025-09-11 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1417b833-7304-30f1-bdb1-9b18431d5053 | -10.16247 | -46.17402 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca40744b-d6f5-3481-9d06-812736ce361f | -13.15407 | -45.28039 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5b5025e-4e40-3fa7-9736-35a4528c5346 | -8.58391 | -50.80125 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 384d8629-9758-33fa-be31-3ce8c04385ea | -11.03833 | -46.0485 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 76e60d12-fba6-3d38-9a04-ad7d216d73d9 | -12.9569 | -54.74623 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31575062-c392-363c-9552-ffd4a095539d | -13.15686 | -45.28453 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62176cec-1c00-3f25-8858-07ca4f3a4d7c | -12.42745 | -47.8055 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff72b659-db3c-3d88-83b6-12851d53ee21 | -13.95058 | -48.20957 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94d26020-7f66-34ac-bcac-2baf7e1cb89d | -13.9285 | -48.23652 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ae1b3a4-1ca0-3001-94e5-48678e8655e4 | -13.268 | -43.75179 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f354b7ff-4e55-3628-b23d-70a0e9b7ab9a | -11.71855 | -48.25251 | 2025-09-11 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5238a3a4-094c-3ba9-adbf-ef2bf6266182 | -12.06961 | -47.57726 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8b6d6d8-ab13-3f0c-9cb9-ba2a10fdce46 | -15.2028 | -44.04253 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0be7772-5caa-3726-bdb3-2068a46209e9 | -11.82321 | -46.74832 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef08bbe5-b364-3fbb-a059-02fec3bdd279 | -11.48445 | -49.25498 | 2025-09-11 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eb479aa-5943-35b0-b981-540655032dc1 | -13.85203 | -47.36042 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a595d5f4-b65c-3c4c-b5a2-eda94c0622b8 | -10.66726 | -48.62783 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60628ad8-793f-39aa-b094-e600122c1633 | -12.07762 | -50.99308 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0a7dda9e-6888-3f19-81b4-e40cea170ed5 | -9.15295 | -46.05849 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18c51b08-bf50-39c3-a04e-1ab8a6795a2e | -11.48552 | -43.63618 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1624c3a4-b153-3dcc-8d4c-d4e669d02313 | -9.7634 | -51.10683 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27cd1a2c-c213-3561-82df-d4d3ad87b199 | -13.9689 | -48.20525 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea7f061e-b9ce-30c7-afd4-9734edcc8cd9 | -15.20574 | -44.04145 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0aa799e9-b85c-3268-a4c6-122c0b5f97c5 | -13.28609 | -43.77492 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35b8c984-6a4d-318c-8a78-58955d1c9a9e | -12.11724 | -51.05199 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e22f7c14-2658-34f7-a255-5d920cbba287 | -9.01604 | -49.77802 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8d1213f-65d9-32e3-82a0-20004026d73c | -9.04813 | -46.9742 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0d3c2ec-eec8-3af8-8b0f-185a8d1d0607 | -12.11713 | -51.05141 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8aaabb8d-c4b5-3e2d-adb7-dbfa551a4142 | -14.71426 | -45.34354 | 2025-09-11 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d94ffa1-c3a1-36ed-a338-482254ee1390 | -12.05327 | -47.59386 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 910f1ed2-d175-35c1-8f53-c2775bc0e91c | -11.35231 | -46.52467 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4a3a226-96a3-31b5-87e8-097fac097700 | -12.39712 | -54.16683 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ae250471-bc4b-37cd-81f0-17474c8a5971 | -9.08978 | -49.8132 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2436a539-713c-3504-9869-2cc36d7105a3 | -11.40851 | -43.53325 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9aa36f4-790a-3279-b1d7-ae2da22d8dcf | -9.05937 | -47.05602 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3b735ef-6c90-39e5-98eb-1323554ecadd | -12.57183 | -43.79055 | 2025-09-11 04:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e94e7e94-54ba-3ff2-96c5-96f05ba1bb79 | -9.05155 | -46.97475 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3698fe6-5e10-3ad7-a162-513e132eb459 | -11.16933 | -45.28285 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ee03046-eb07-3f24-b5be-03b0aba502be | -14.14093 | -45.39868 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 176f89ce-7176-35e2-a2f2-a0dd76efd00b | -11.45084 | -43.58353 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a031f52-9d69-3400-b66e-a413f89d7edf | -12.92936 | -54.7529 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9140c34-9f12-368e-a7d8-c9cb7ab34102 | -12.1235 | -44.86351 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5b88770-c70b-38d6-bfd4-982804d50179 | -8.87232 | -49.56142 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08f9383e-6171-3bf4-a11a-b6ce7f375159 | -11.15936 | -45.30293 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8ffb0c1-494c-3635-a2b3-86d8921eca31 | -9.01858 | -49.76316 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 284480cb-b338-3f27-898e-caa4fb87fbf4 | -13.15742 | -45.28093 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6780c62e-3d22-3f04-9cf6-beb8cb453b0c | -11.16822 | -45.28991 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6129c5e8-7764-32c6-bdba-6c53351d2a47 | -14.22344 | -43.09295 | 2025-09-11 04:23:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3774f76c-e0d7-307c-a6ea-b9ff93185725 | -10.37692 | -50.52893 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b27db8f2-f4ea-3a59-9b95-ebacee664010 | -10.56068 | -43.66293 | 2025-09-11 04:23:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 897f7bfa-c67d-34cf-9334-d8e2a406f6ec | -9.59705 | -50.91996 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f6c7b582-c440-355e-ba25-5150217fa114 | -12.93418 | -54.81109 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a5a85b6-a593-3f3a-a64d-a51599e8746e | -11.47674 | -43.69378 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ed8bab57-46fd-33f6-9f35-7cee57cf0ca4 | -9.68268 | -46.76467 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 198a3d06-3a7c-3484-b825-da7dbc21cd69 | -13.14219 | -47.15083 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5951ea5e-5481-3b6e-9730-a608b098019a | -12.12913 | -44.87174 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dbe9b01-30f6-3577-8d64-2bc123c572d3 | -9.89058 | -50.16701 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 918368e3-1e89-388c-9891-bdcd65734d4f | -11.42476 | -43.56757 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1f617bb-99c5-39ee-8c06-a812770801bf | -11.48322 | -43.63889 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 009c9b85-f317-3a41-b607-dd57eae0e9b5 | -11.65033 | -46.91507 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67256aec-c19c-31e8-b814-1495236f9dab | -14.13421 | -45.3976 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2c7b2d3-d0e7-3503-8737-bde174787ebb | -11.38371 | -43.52655 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 692cf5c5-c336-367f-bc7e-d4fb9df3717c | -14.56454 | -48.74846 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76cd0d18-c213-3026-99b5-0b29b7c9fab4 | -10.31828 | -48.79706 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7365ee75-3acd-3aec-acdd-64471c4619a5 | -9.05408 | -47.06693 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cd78475-fb91-33b1-86cb-209456c57a8d | -10.66658 | -48.63195 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 380c4291-3b62-37fc-9089-5e724068593f | -11.77128 | -46.48368 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00265fca-7781-3844-8e5f-ec79688aec51 | -9.75704 | -47.84591 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5fcb123-9f32-3dcf-ab85-658c040158ae | -12.85978 | -52.94838 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cfaa5a69-a468-3544-8644-650da90c0b16 | -9.03252 | -49.77578 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 770ee481-96d2-306b-94d5-e034b6d9202f | -12.85638 | -47.96085 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25608503-c95d-3cd7-a79d-9787ed0612c8 | -11.3843 | -43.52267 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08a0025d-8860-32e3-ae7f-db8a35bea23a | -11.4352 | -43.5692 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e50eb289-7e91-3098-9994-d34275909218 | -11.44736 | -43.583 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a71fc5c0-d6ba-32bf-b401-8b9585e0574c | -14.38909 | -47.30644 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e8ed4fa-e237-3101-b221-c1f620e111ae | -9.12493 | -46.99428 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1160fa07-f613-3b49-9bc0-292000952b3a | -11.77285 | -46.51673 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a378999-ce27-3932-bb6a-8f5d94f7d0ad | -13.98101 | -48.23864 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58ae39f0-7095-3f09-8e84-05832dead5eb | -10.77578 | -46.00234 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 21b47c48-30a4-3545-8f1f-9c261a78bd0f | -11.02922 | -45.05728 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 627c48e7-b834-382f-82d4-1bf04eefffa0 | -10.06525 | -50.38211 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdc1a6d5-fcf8-3217-a247-42b76bc4cbea | -15.21812 | -44.05583 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4548a3e8-b68f-38ef-8e33-dfd1874c0cdb | -10.31399 | -48.80036 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ff50561b-46dd-36e3-966e-6aee538f889f | -15.22166 | -44.05639 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README61.md)
