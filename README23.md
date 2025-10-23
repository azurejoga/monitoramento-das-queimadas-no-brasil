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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b41a4d31-3f9f-303e-af06-938830c2a2f6 | -11.7933 | -47.06846 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20cbade7-251e-31c4-9933-9299916948f3 | -12.15859 | -48.0596 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a848ed9c-0374-396d-8af9-74d23c6f2112 | -12.31868 | -47.83745 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 038b7ea5-620f-3e5f-9ce6-836117f5f94f | -14.21374 | -44.5202 | 2025-10-23 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37ac4b36-6a72-3618-87c5-4b6c62fe530f | -11.24885 | -49.87418 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc5544cc-4ade-3bd7-bc33-dde17177381b | -15.13901 | -50.11784 | 2025-10-23 04:38:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be7c4afa-3a7a-3a0a-a089-37318585e40a | -10.53631 | -47.99 | 2025-10-23 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4546bcbb-04f5-31b7-b1de-cb848f5e0158 | -9.97494 | -47.08748 | 2025-10-23 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dfa5366e-3d43-32d9-bba8-84f63b1c4217 | -16.30165 | -45.87717 | 2025-10-23 04:38:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 019fdfc9-1847-338f-b9cd-fcd19785cbc0 | -11.80068 | -49.41158 | 2025-10-23 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bcff77e-b55e-3030-91b7-267bf6341ebe | -14.87519 | -59.63202 | 2025-10-23 04:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12f80d0b-0e3c-3ff9-a46b-6446a55b0ba5 | -12.77759 | -47.38328 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e940e983-8f06-3e5a-b7f0-14d4ed6441db | -13.90302 | -48.37331 | 2025-10-23 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 21c21f73-3658-3c8e-a7c8-0df9a73f5eec | -11.61045 | -48.53775 | 2025-10-23 04:38:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 914a5beb-b348-388d-a9a5-803afd9ebcfa | -15.5842 | -45.90617 | 2025-10-23 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 04c7beb8-3460-3a3c-a4e9-d70b6d62690f | -10.90946 | -50.11325 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35586004-2a5d-3f49-a2b1-f95865cbb72b | -12.27854 | -47.45534 | 2025-10-23 04:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2eeea2c6-6751-3b3d-8b42-fdef43d908d9 | -11.35658 | -44.88477 | 2025-10-23 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ed1611e-f8d4-3fd8-b10e-5ae30e44e118 | -11.01332 | -47.56974 | 2025-10-23 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9cd651c4-bc5f-35d4-8fed-17f0b5d442fb | -16.17797 | -50.8539 | 2025-10-23 04:38:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5f31558-d602-388e-bbb5-c720da1c3885 | -10.90888 | -50.11686 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13ed1308-082d-38ae-89c4-a682f6239368 | -12.78729 | -48.57563 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3681da3-1748-3a4b-90e6-b7ecde9b2d6b | -11.01113 | -47.67388 | 2025-10-23 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dc058a5-0ab7-37a7-8844-486d59b9bfde | -12.13263 | -62.9739 | 2025-10-23 04:38:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe2bc88b-7eb9-38b3-a026-9124a290e822 | -10.66193 | -47.33936 | 2025-10-23 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4723b793-667b-316b-9ac8-1f47dedbb190 | -11.27603 | -49.7909 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4c199f4-272b-346c-832f-9607522f9720 | -16.49988 | -49.74259 | 2025-10-23 04:38:00 | NPP-375D | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3cf6073-b9d9-3aac-8fdb-8c5df429f9d1 | -13.56842 | -50.62709 | 2025-10-23 04:38:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fad5bdb-19ce-37b5-831f-a6200660812e | -13.30033 | -47.47734 | 2025-10-23 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9a4e079-778f-33bf-bd3c-b672e48154fc | -12.7018 | -48.83977 | 2025-10-23 04:38:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d931c364-1f3d-3312-81fe-02e3c11223b6 | -12.12571 | -62.9723 | 2025-10-23 04:38:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3794c11-70fd-388d-998f-ec44a4b55ca2 | -13.90697 | -48.3701 | 2025-10-23 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbf2afe3-173e-3435-8dc9-4c3b8906317f | -12.68318 | -48.63929 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96187b29-94f1-3b9f-b43b-5c6dc652ce6d | -10.63683 | -42.30369 | 2025-10-23 04:38:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e9b5683c-fcc5-38de-ad6d-107c20d6b6b0 | -10.58201 | -48.60139 | 2025-10-23 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44a11635-322f-3bc3-8eb5-ced020aa9a52 | -11.05741 | -45.39742 | 2025-10-23 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b2e3c98-ea4a-3f93-839a-79f41fc41917 | -12.28538 | -47.45646 | 2025-10-23 04:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df673da8-e9ae-3f97-9d82-9a487d542566 | -15.60308 | -48.05634 | 2025-10-23 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a693ace5-8654-324a-9289-703b6d9ee315 | -9.97378 | -47.0722 | 2025-10-23 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bb9e8f5-8154-3880-9eae-35e596b6f224 | -12.0007 | -46.7819 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ee526a42-3401-3dd8-a97b-b8da3b8fe6ee | -10.63816 | -42.30583 | 2025-10-23 04:38:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aa8dd485-db5c-3110-b4db-d9c310f7e6a5 | -12.13254 | -62.96705 | 2025-10-23 04:38:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4923a324-35fc-3c24-8afc-b3bc220e0f0d | -12.02066 | -46.74446 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2df197a2-e371-3ecf-9d75-a147e3d13b89 | -11.27269 | -49.79035 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7fdca8a-e88d-35c8-91d3-c644d1dd4940 | -12.6776 | -48.63112 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05d0506c-2d36-3b48-a8bd-16122beee5c3 | -11.05926 | -45.39542 | 2025-10-23 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 079bfcce-d873-3305-896a-5e835e640076 | -12.01715 | -46.74393 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe138133-2abe-377e-85a0-1d11d89ab2af | -11.35737 | -49.79702 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2074ec02-148e-34a9-a712-5b6b5217b944 | -12.13405 | -62.96715 | 2025-10-23 04:38:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c4e6f43-9ffc-37b7-9e25-7ae1f5111855 | -13.29974 | -47.48132 | 2025-10-23 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 064ba9a0-2c58-3c9b-9271-909683039e8c | -15.58482 | -49.06593 | 2025-10-23 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8237ad7d-f5cc-3042-b818-8d80122e6249 | -11.34713 | -51.44677 | 2025-10-23 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 200dbab5-d5f4-320f-8681-d8aefec69d6c | -10.39382 | -47.10578 | 2025-10-23 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a99432c7-51e2-3eef-9e23-c46a85694bd3 | -15.91791 | -48.32236 | 2025-10-23 04:38:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0e761dad-8515-387f-bf8c-96855dac1eda | -13.65578 | -48.64298 | 2025-10-23 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 046df14e-b8c3-3ba8-b5e8-5ab2eb72fc88 | -10.2987 | -47.79514 | 2025-10-23 04:38:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5eff9446-5092-3761-a3bb-f59903551cb9 | -15.58655 | -49.06635 | 2025-10-23 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1950b0a5-6fee-3f0b-afa6-233b2c80fb44 | -11.53852 | -52.24017 | 2025-10-23 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d3d5c6b-12bc-343a-b2bd-06f1f218c48c | -11.95796 | -47.84614 | 2025-10-23 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 421bd09a-9a2e-342b-8ec4-8adb2035df51 | -11.14038 | -44.93309 | 2025-10-23 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9eb06873-dfab-3eee-bb56-ab448d9f816a | -12.13109 | -62.97375 | 2025-10-23 04:38:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d111b93-e7ca-370c-90df-7e44c714588f | -9.97775 | -47.06905 | 2025-10-23 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 755198bd-8acb-3c4a-91f1-23d9b28c8c08 | -11.00273 | -47.79516 | 2025-10-23 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fabacc4-e03b-3729-bd4c-90664ee665f0 | -16.51807 | -51.40415 | 2025-10-23 04:38:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9cf1ff22-fc39-374b-baef-1792984a49cf | -12.28196 | -47.45591 | 2025-10-23 04:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7485e75-129f-332c-9aa8-cb66b6755796 | -14.67237 | -52.34403 | 2025-10-23 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7964d675-64b7-3f3e-9f7b-2006cc7367c0 | -16.08039 | -51.40844 | 2025-10-23 04:38:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57360fa4-a726-306f-a181-ca413153164c | -13.12857 | -48.24389 | 2025-10-23 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcfcfe16-ca87-33ad-a8b2-36455292fbac | -15.10676 | -48.5273 | 2025-10-23 04:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8ffdcad-1dc9-384f-840f-2cebb8435a45 | -15.59627 | -45.90326 | 2025-10-23 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4b98422-0fef-39d2-9f8c-7fa7f181385e | -12.67537 | -48.62343 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d713f3ec-43b2-39a6-90cb-955c3409b659 | -14.26548 | -46.29922 | 2025-10-23 04:38:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdd37ef4-0558-3de3-8f1c-e4266152f04b | -11.80101 | -45.18225 | 2025-10-23 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c93b21c-244e-33fd-8bc5-74522a0fe9bb | -16.30165 | -45.87718 | 2025-10-23 04:38:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c0519da-9aab-3a20-9f1f-d1314a2a3c5e | -14.90168 | -46.24482 | 2025-10-23 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08bac02b-b64f-3bfb-8895-e22ebb3f7c57 | -12.00188 | -46.77403 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb6ed4fd-9ceb-310e-8c1a-42db50c4663f | -13.12465 | -48.24701 | 2025-10-23 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bddbcfa9-da69-3bda-9ea4-e97e398ac499 | -11.35908 | -49.78635 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 148534a9-797d-335f-971f-b845ef1a0c87 | -13.59791 | -43.47321 | 2025-10-23 04:38:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 679159ce-5f3a-36ba-9de1-11abb4aa159e | -13.31048 | -48.66947 | 2025-10-23 04:38:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a3c4bfc-fa91-3ceb-82cb-5360ba66f427 | -13.79136 | -52.7732 | 2025-10-23 04:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0f49fd2-89f3-37ea-8445-122a1fe928f9 | -9.9949 | -49.15095 | 2025-10-23 04:38:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a07952a-73a7-3e26-8a11-69011aaf6fe2 | -14.87397 | -57.26663 | 2025-10-23 04:38:00 | NPP-375D | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b807dbba-93a4-3306-ab87-c9bb1f1c4262 | -12.00011 | -46.78581 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d9a52c44-4834-372a-9d3e-6ebd5f71d995 | -12.01364 | -46.7434 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c07b6add-803d-3054-a346-e18ec58355d1 | -11.95852 | -47.84249 | 2025-10-23 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d4bff9d-5a7f-3d03-8eda-2f6eaefc8499 | -11.35794 | -49.79346 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2ad0ac9d-7a83-3f7b-b490-c24c037dfa9b | -12.24566 | -49.59327 | 2025-10-23 04:38:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d459ec89-1d3c-3592-9b69-c28c88fd3543 | -10.91341 | -50.1102 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5750d693-24ed-32ae-a796-ade9218e3686 | -14.69313 | -52.8137 | 2025-10-23 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4624e84-8b0b-3fa8-b3f3-f42385a7f4b3 | -10.91619 | -50.11436 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 00fc88f7-e693-37ea-a4a6-802e5b5a70c9 | -9.99602 | -49.14391 | 2025-10-23 04:38:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 936593cb-db3d-3d35-8808-02c0cfe9ff3a | -9.80208 | -48.20687 | 2025-10-23 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46de266f-6d2d-39dc-9c57-abc39f6959ac | -16.51111 | -51.46737 | 2025-10-23 04:38:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06944360-ac0d-3e17-bbe4-708605e51932 | -12.7845 | -48.5715 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 44e1876d-79af-3b79-a850-460c6c79fee1 | -11.36123 | -49.78648 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5991e22c-0767-35d2-881d-ff76792ea682 | -12.00954 | -46.74684 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a48ed3d-5895-3cfe-a183-6ed6f06a3c9a | -11.05555 | -45.39491 | 2025-10-23 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d6b2dd6-81d1-373c-abb0-f7f4321bd14b | -12.68318 | -48.6393 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 640f0952-5a01-3979-b746-cc1cbefc751f | -16.07588 | -51.40818 | 2025-10-23 04:38:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README24.md)
