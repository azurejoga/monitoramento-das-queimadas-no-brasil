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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5630f71a-edd9-3926-a817-d427d5119a75 | -11.71252 | -44.53687 | 2026-09-29 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9a29e35-0808-3905-bb7f-a0a3ad4d6f30 | -8.24887 | -45.44432 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c14a67d4-803d-31ca-936c-d6ca78432580 | -13.1642 | -48.54193 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6072dabc-a09b-3cdf-8eeb-d22919d1821c | -10.91157 | -43.85951 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ed36c5b-a64d-3d63-87aa-254dfca0cca7 | -11.34028 | -54.11273 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44ff40fb-9c18-3da9-b71e-fa683e960f48 | -12.79858 | -50.58771 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae0ae241-1702-3c74-aa98-658a54206395 | -10.9714 | -49.66886 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d7e4d85-a9cd-34bc-a6af-0f9687e0e3ba | -7.9885 | -43.25711 | 2026-09-29 04:51:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7c6cb553-7f46-3870-95b4-5abca6cf1660 | -7.54274 | -44.58631 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55221fe9-5137-3c9d-a0f6-4aaee04b2a26 | -7.53305 | -45.88786 | 2026-09-29 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7534321d-76a2-3e1b-8614-7401888edde3 | -12.90687 | -52.06715 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d7a0d94-5775-324b-ae0f-5e125d6e7282 | -6.31692 | -52.62687 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2e6d30f1-4db0-394b-9f0a-f684dc605320 | -9.04636 | -45.00178 | 2026-09-29 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92173a71-d9e3-33f7-8758-83708a657e73 | -7.61141 | -46.4594 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 77729e58-c792-35a7-9db0-239f25c6db88 | -8.72646 | -44.92217 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b53734bd-561f-3e36-8f10-d4a42ecf3d55 | -12.06407 | -46.46474 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 137ca92a-1c3b-3655-a36a-156dd1169013 | -12.0586 | -50.21397 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b949a38b-9924-3fcc-a842-ed8e12c0e646 | -12.72931 | -47.2687 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a13b1b8c-6e49-356a-adaa-a0c49129b42c | -6.88625 | -52.47633 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f80a06de-f5d1-335e-b22a-c515ea4fa764 | -12.77127 | -52.81151 | 2026-09-29 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f12a32f5-5854-3c34-ad87-d310f86a0992 | -7.88626 | -54.72132 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4e2f09d7-3a53-3ff2-8c93-37dbc812f66d | -12.80192 | -50.58826 | 2026-09-29 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da78ff33-faeb-3e42-96f4-e781ba346726 | -12.0525 | -50.93843 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 022937d6-ab35-3907-8ec3-542c8441d66e | -7.50529 | -44.55834 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 321faaf5-3921-3bea-b146-485911c0c58d | -11.41547 | -43.42732 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ffe3dc0-07d6-3222-abc7-faa0de6c7ada | -12.94691 | -46.64073 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| df2eb64e-0766-39a5-901d-46701284ca43 | -11.3829 | -43.4012 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4342d9cb-f4df-3f25-b863-a78c26aaef4a | -12.04308 | -50.93325 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c8cbe9ef-46eb-3e4c-ba97-0f370479c6aa | -7.50934 | -44.55909 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 765eff52-b669-3afb-80d3-373522bba3a4 | -12.07109 | -46.47065 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df7b40ea-4977-3ddf-a574-99f20083200a | -11.17539 | -44.79356 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 0f3fda56-d7cc-35b0-9db9-8ab906407c33 | -11.86126 | -47.07689 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc689a2d-7ed3-3b54-bf87-3fc10a338adf | -12.02186 | -50.9805 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74749bfd-0379-3853-9089-4018c9db8175 | -11.42012 | -43.42796 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d11a850-4083-3012-9a8b-abc1634bc6f3 | -11.85385 | -47.07573 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 062ba839-64f4-3005-addf-bbcd38617ba2 | -13.43266 | -48.62124 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6bbc8ddc-df4f-376d-8153-53e96731e1bb | -11.41017 | -43.43158 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b6c9f6f-5a09-31be-a01a-5ce09f2fe581 | -12.31932 | -50.14979 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f72b72de-84e8-3c1f-8368-d927ac64c255 | -12.31702 | -50.29528 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72c67284-548d-3fd6-979d-ac454e65cbb5 | -12.01084 | -50.94246 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b0f9f7f-6367-39da-bf03-9afc1087418b | -12.7546 | -50.67148 | 2026-09-29 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| badbd70e-8535-399c-b071-fa64dc96515d | -7.99126 | -43.25512 | 2026-09-29 04:51:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f0d6aefe-3049-3ec1-86ef-1f6b153b2ee3 | -12.0131 | -50.92832 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9699241c-3aeb-346e-860d-7e7d4ebf3e61 | -11.42682 | -43.4488 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a693147-b9dc-3e4e-b273-e0055c5a67d2 | -7.389 | -42.63447 | 2026-09-29 04:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd8469d6-ec87-360b-a9e7-500f8e981280 | -11.33213 | -54.1159 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 574e024f-05d3-35b1-9213-42b8325c48c6 | -11.98444 | -50.9418 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7c5691e2-81a1-37dd-be20-9644fd0ea3e7 | -12.28255 | -50.27512 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44d70788-55fb-3d3a-a738-a4c809041dbe | -12.87936 | -44.81577 | 2026-09-29 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 636bc8c8-3e73-3401-8f10-0f2fc9562a13 | -10.71316 | -44.42419 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 858fd94a-1e71-39c5-8385-69f569bf4412 | -13.53552 | -49.18196 | 2026-09-29 04:51:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e4a1fd50-54f6-33ab-9167-4fea1de23ba5 | -11.43945 | -43.4605 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c36ebada-b95f-3324-9f1f-f45a827fd142 | -13.92682 | -47.84859 | 2026-09-29 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 986c0a6e-0f69-3b2a-95e7-f12785e81645 | -11.89974 | -50.62336 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 182dc774-91ce-347d-babb-b30f631dd219 | -11.4514 | -43.47699 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83871cb3-70aa-39d5-895c-ed5eb6a187c6 | -13.14723 | -48.53552 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a3fb1dfb-6e35-346c-9faf-51f93185d50c | -7.5379 | -47.12151 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d79e9b1-5a2b-315c-8442-12d6551189b6 | -11.42087 | -43.45793 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9df018ec-4ffb-3a13-987f-ea19392818a7 | -13.19687 | -48.53931 | 2026-09-29 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c5f8045-f8e0-3fa5-a722-a3e5929edbd3 | -7.26417 | -45.33698 | 2026-09-29 04:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a0a137e-c94e-30f6-8a1b-19eb57c9c07a | -11.41623 | -43.45731 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ce4a7eca-06a1-3f8e-9a49-7fc5a64193eb | -11.14134 | -50.07419 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4e984961-4a1a-3e7f-943c-3ef73d3bd3bb | -11.86022 | -50.46849 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b6af508-eaa5-39de-aa85-24954aa0336b | -7.24696 | -45.25859 | 2026-09-29 04:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7227341e-281d-36f4-9dd8-cb5346b6501a | -11.33507 | -54.12099 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27478d98-9a7a-36cc-bb89-6aeb25af7454 | -8.68357 | -38.19664 | 2026-09-29 04:51:00 | NPP-375D | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c4dba8f-d354-3a37-9334-d48cc024b9e0 | -11.43081 | -43.45432 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c315c00-65ea-3645-b5c9-349d14fb4347 | -10.71573 | -44.43692 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c0c17ce-3b9a-3249-944f-21694ba54a8c | -6.20286 | -52.9087 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 922ec950-480d-31ea-80fe-945286918607 | -12.03944 | -46.50037 | 2026-09-29 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d9e7389-2c04-32f6-8531-ac2771ea8844 | -7.50998 | -55.03013 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b103c2a7-3099-31bd-9df4-52d228f16211 | -6.16498 | -52.82833 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35196fb4-cf2d-3ec0-a274-938a299a68cf | -11.54845 | -54.50085 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cfcb4c5-bee0-3019-a51a-1e3509353761 | -11.67676 | -44.54025 | 2026-09-29 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0c66de4-ab13-38f7-8cc6-65169fa33b42 | -11.61913 | -44.14865 | 2026-09-29 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b92ac37f-5864-3e3f-b854-8a9ddab4609a | -12.02473 | -50.94112 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0c6ccec-597f-383f-bcde-a67c9fcf2102 | -9.95246 | -50.14997 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86f706e7-8e47-3804-8efc-ed6d8e476118 | -13.19336 | -48.53879 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef350589-a704-3c47-9032-37397d92025d | -6.16256 | -52.9133 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3704f661-383e-3e6d-bc85-bd4f0a45e2ff | -13.48537 | -48.60818 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb396c99-818f-3009-b663-5dfe2179a88b | -14.10775 | -46.29187 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f4ec1fec-24e9-3399-9d8f-e38959692534 | -12.00775 | -50.94564 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ca84586-8643-3fe5-84af-027c204daabf | -12.66292 | -46.98422 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 34c99287-9c8c-302c-8d52-f8ea1a0a000a | -11.44076 | -43.45073 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fccf7483-1ba2-319c-9b6c-d2a0835d758a | -12.00629 | -44.92716 | 2026-09-29 04:51:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a4fa97b-d57c-3357-af43-4a39b63bb416 | -10.80385 | -48.74525 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6407339-e333-34a4-831d-3f0558b6aa7d | -12.94619 | -46.64571 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 400dc690-4d80-3b44-ac1a-a963b3409f5d | -11.43748 | -43.4751 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d9714292-6035-371f-8cb3-13555c321e38 | -12.93851 | -46.64447 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60ee6928-6a9c-3c10-8089-478ca7309b76 | -11.4335 | -43.4696 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 814fc4fa-c60f-3c2a-a557-1b31121a415a | -13.11407 | -47.40482 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c6dc96d-4553-3391-b1d1-56611bc9b3f9 | -12.71978 | -46.98961 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef9e2666-df7e-3fd3-b0fd-cae057958dbf | -7.67673 | -44.887 | 2026-09-29 04:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ffaf41d5-bc94-3e99-9148-9daa425ccddc | -12.75515 | -54.05081 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 084309fd-475c-3af7-9d31-1650620a11bf | -13.17594 | -48.55947 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4088aca1-9828-3e6f-b936-b54dc4298e57 | -12.91159 | -52.03805 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4aa1fd03-cd30-3a27-b8bf-48630845d05f | -9.67229 | -48.87116 | 2026-09-29 04:51:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b595a6b-75c3-3f11-8e68-07929d5032d0 | -11.39608 | -43.44304 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e23ec2d-11c6-329b-90e0-ec6a2b84bdd2 | -12.71057 | -46.97377 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27caf46b-a982-3fa6-a6ad-969fa476ed9f | -9.76504 | -36.97499 | 2026-09-29 04:51:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 4.4 |


[Clique aqui para ver as próximas entradas](README49.md)
