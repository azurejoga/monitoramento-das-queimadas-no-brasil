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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f9a6767-977c-31fc-aa22-1e15685a1379 | -10.38491 | -49.44016 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47655b59-e356-3732-b6f5-acd74009f6f7 | -11.82043 | -47.50549 | 2026-06-04 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8469be8-b4d1-3a12-80c7-6f2e22b0d424 | -14.29558 | -49.14649 | 2026-06-04 04:44:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0351cc4e-952b-35b4-bd92-d0c4e732589c | -12.22176 | -57.28005 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2246c454-4b18-39a7-ad62-0c625ddeb7d3 | -9.92716 | -48.00959 | 2026-06-04 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f6505ef-2cb4-33b0-9d4e-911c9d2fac76 | -12.23142 | -57.28198 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d257675c-5936-376c-acdd-c7592f4eeea4 | -11.88399 | -57.83168 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cad11333-7d5d-3e8e-9ea6-4efe8d9b1b63 | -10.13888 | -52.12973 | 2026-06-04 04:44:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 379c812c-f8e3-3df6-be24-fb6dc8dd87f0 | -14.05007 | -46.34301 | 2026-06-04 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 514e7c34-dc2b-30e9-a354-4785c6de924c | -12.43582 | -58.40952 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4263f187-42af-351a-bce3-62410cdd5165 | -9.37549 | -50.54458 | 2026-06-04 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fff7868-99a6-3ec9-9a55-647a6adc68af | -10.57302 | -57.32322 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96ce943d-dfce-3860-8a10-abd2b44ad544 | -11.78849 | -52.51472 | 2026-06-04 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a52b577-3c9c-324c-bb16-371705b6bb71 | -15.23843 | -48.56684 | 2026-06-04 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2498af4b-3cb4-33b8-ba48-3c1b32d7b992 | -14.08041 | -53.38332 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 285cacfd-69b3-3db7-9e67-c8163a27fd6e | -10.22078 | -48.07378 | 2026-06-04 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 475db1fd-0d64-3c61-bad1-b892141990c0 | -12.22659 | -57.28101 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 435597d1-fb99-3340-94c9-8d6945c02c7a | -10.53509 | -46.61901 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b47871e-27e6-30cc-a8d5-dfb828e575b3 | -12.73586 | -54.1937 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 319ea9ec-7caf-3cd6-a79c-f7ae22850154 | -10.61331 | -46.69837 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2034e410-17a0-37d1-9cfe-72ba7b55c265 | -10.56696 | -57.32249 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9e2ee36-5c4a-32d8-8e3f-31e57bd539cb | -12.30736 | -47.90484 | 2026-06-04 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 714834fa-cf9d-3e3c-af50-6f49763bb30a | -11.78196 | -52.50924 | 2026-06-04 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c760174-107c-3bec-a734-4b9ee3cddc39 | -11.66784 | -54.58539 | 2026-06-04 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0833209f-8614-38a5-81ff-3c578d78839d | -12.55625 | -48.35142 | 2026-06-04 04:44:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7772881b-fafa-3d3b-985c-ad182a6d5561 | -12.2121 | -57.27812 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 65156017-9134-322e-a57e-87e0c8c99aa2 | -12.45517 | -58.47657 | 2026-06-04 04:44:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d8fa432d-2d4b-3ca3-a4ed-e1cc0aca2b1b | -14.09237 | -59.39619 | 2026-06-04 04:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68e25c21-b3da-31ec-9f60-eabacb0af546 | -14.08333 | -53.38843 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 176caf5c-c0fd-33fc-bc67-de012b1bce94 | -10.98784 | -47.07602 | 2026-06-04 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 408c8b02-c19a-3ecb-b49a-f47df1d0a13b | -12.2075 | -57.28687 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9c1b44a8-554a-306c-af29-9f5f9eead04f | -14.77177 | -52.67044 | 2026-06-04 04:44:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e38028d8-0ad6-343b-ba8a-6e2078a8c40e | -14.08506 | -59.37704 | 2026-06-04 04:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4d8d501-65b5-3b2b-bc88-45af6be3e4dd | -14.07965 | -53.38776 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 313e56ca-4bd8-3f86-86d9-8b55102ba5bc | -14.09306 | -59.39277 | 2026-06-04 04:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4649f144-5843-3598-b11b-466cbb469f60 | -12.43974 | -58.41705 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfccbbd7-48c2-3058-b4a3-0d93af6709ae | -9.5304 | -47.75738 | 2026-06-04 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae66e55a-2031-3498-a7ed-ee4c16ec73f9 | -10.8642 | -53.74871 | 2026-06-04 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c88f5b6-6d54-38ed-88d7-9c8ba34aff37 | -11.62652 | -55.1865 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b101436d-28f3-3c1c-a67f-0622be2e4485 | -9.62841 | -48.8817 | 2026-06-04 04:44:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 568600cc-d054-3ecb-a6aa-6c0507380e01 | -10.81857 | -56.59163 | 2026-06-04 04:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94f7e986-c3d3-3fad-880b-e0b8ba687f39 | -9.4681 | -46.05896 | 2026-06-04 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a0ed9a7-046c-3520-a825-05d51dcf4ee0 | -14.07597 | -53.38708 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f68cec5-cb8c-31d0-a25b-e44cb21ea97b | -11.48396 | -52.91335 | 2026-06-04 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ec42f5f-bcb1-3d02-836d-5f137fbe33b5 | -12.21233 | -57.28786 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d2638d95-ae99-3350-8650-b7a240612796 | -9.37266 | -50.54029 | 2026-06-04 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83691cb1-da29-32fd-92e1-35d285534111 | -10.81783 | -56.59343 | 2026-06-04 04:44:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d597eaa-a6f4-3f76-956e-e4f49f5a5141 | -14.76755 | -52.67383 | 2026-06-04 04:44:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d613ef44-4a03-3e25-aa7d-977c5572d84c | -14.05003 | -53.40526 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f73a298-a918-30df-85c2-a736a2812e31 | -12.21795 | -57.27375 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f0b1d5d7-dc7f-30a1-a8be-f18e0eaaacfd | -14.16358 | -58.98758 | 2026-06-04 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 492d70ff-e11e-372a-b0da-1599a7b07ba0 | -9.68466 | -47.05028 | 2026-06-04 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a97a5bf-452c-3d88-abef-b60a3e58be61 | -10.35777 | -48.13249 | 2026-06-04 04:44:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b0cdeae-0e6f-3d65-9409-7b281f0c37b8 | -13.51357 | -54.31438 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c37ff36a-7976-3f51-b678-a6110223498a | -11.5439 | -52.78685 | 2026-06-04 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dde7e4a3-8d94-3379-8735-590d1fd086a2 | -11.80009 | -52.51241 | 2026-06-04 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80afe215-11c5-3f07-8a2a-b60359d811d2 | -10.56322 | -46.62687 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21ae36a4-5346-3b41-827a-f1c5e403f295 | -14.0877 | -59.39163 | 2026-06-04 04:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc31d222-b6fa-36a2-bb0c-56a0819f7853 | -11.04734 | -49.61663 | 2026-06-04 04:44:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf932c57-25f8-3892-9e11-7fee11076cee | -11.16654 | -49.2457 | 2026-06-04 04:44:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 219749ff-c828-30b1-bd14-3d389fc93510 | -9.51496 | -50.26402 | 2026-06-04 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9a140ba-db59-3972-affc-b912c39a49f8 | -9.92437 | -48.0055 | 2026-06-04 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94ebef3d-779c-39b5-923c-1c5c478f50bd | -12.46219 | -58.46826 | 2026-06-04 04:44:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 126e1fc4-83a6-303b-ba79-64de4c9266b8 | -11.01336 | -47.47583 | 2026-06-04 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99221db9-1286-39b0-879b-0c47605653c3 | -12.31133 | -47.90167 | 2026-06-04 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be762138-437f-3de0-a2a9-a43734348dc5 | -14.09272 | -58.88305 | 2026-06-04 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f206a74-b844-3cf4-ba47-6a2552235652 | -15.49346 | -55.73693 | 2026-06-04 04:44:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3543664-7ecd-3ebb-ac24-dd3f79aa34c2 | -12.31473 | -47.90219 | 2026-06-04 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d56c3cad-80d0-3c81-9f11-6b6b493690fc | -10.90187 | -54.13366 | 2026-06-04 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e564255-fc11-3c72-97a0-d61d27a3662c | -11.62156 | -55.18972 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a0b7e63-45c2-33a6-a143-9b2e4562f0ec | -12.23348 | -57.27115 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 384696f0-0826-3da4-93dd-7b8f238fde65 | -11.26142 | -48.35826 | 2026-06-04 04:44:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 747b3dfc-83e9-3008-92a9-611a54540041 | -12.223 | -57.28436 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| b4cecc46-f0f8-3ac1-a963-1c3f4ba5b91f | -11.78921 | -52.51051 | 2026-06-04 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fae234b2-3993-3906-9250-93ec03144eaa | -13.51256 | -54.31578 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92c24c1c-6ccb-30b1-8624-d0091b09429b | -12.73979 | -54.19443 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3db3e67-dc97-33a8-b99d-dfd5839e708b | -12.4377 | -58.39991 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9c76c02-3566-3422-a487-674b167df335 | -11.54759 | -52.78748 | 2026-06-04 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 81128005-6281-325d-b433-258f53aacaab | -14.78936 | -50.63908 | 2026-06-04 04:44:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 246eda0b-1a37-3a36-8aeb-963362d5e59a | -9.92547 | -47.99837 | 2026-06-04 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f31f724d-b366-3117-9ce5-e294dbef85b1 | -11.54021 | -52.78624 | 2026-06-04 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b94c0d1-25e3-35f8-9b17-43fa93ed2192 | -12.45577 | -58.47347 | 2026-06-04 04:44:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dcedb33c-d040-3638-82a2-dbca16cf785b | -9.51555 | -50.26036 | 2026-06-04 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81492606-3831-342c-ab0e-4685b39ebfe0 | -10.86027 | -53.74799 | 2026-06-04 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77e22ac2-5df6-39fc-9560-adb66fc88799 | -14.09374 | -59.38937 | 2026-06-04 04:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc739c1e-8fcc-3a40-b22e-4f5a14e5d339 | -11.77834 | -52.50861 | 2026-06-04 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bee28b18-8c53-3023-bbda-f9c519ddbea1 | -14.08257 | -53.39287 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a1d7475-791e-3971-a71e-ea910b861129 | -11.88285 | -57.8376 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8e938e4-b4eb-36b5-a4df-603622e5e6fc | -13.96051 | -46.18671 | 2026-06-04 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd2fba66-8102-3dd5-b131-fb10dfa1a3d6 | -12.22555 | -57.28649 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f96fd31a-7461-3974-92eb-7d6889e9aea3 | -12.43457 | -58.41591 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25a88e19-7dfc-384c-a51d-1811c9fdf307 | -10.25905 | -52.07995 | 2026-06-04 04:44:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be6722e9-675c-3746-aefb-1e6f7efea7a1 | -12.3034 | -47.908 | 2026-06-04 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fbc688d6-86f8-3eae-9c3a-42061a6a9c8e | -12.46679 | -58.47248 | 2026-06-04 04:44:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f00d1ec-2322-39cb-83ba-16d21190e38c | -14.09042 | -59.37818 | 2026-06-04 04:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6b44132-7f15-3596-ace5-7e06e0266310 | -10.90249 | -54.1301 | 2026-06-04 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d18c04b1-21b5-36ed-8bb1-76e48a7465ce | -10.9798 | -45.09803 | 2026-06-04 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 920ae7f6-dd65-3ad5-ae88-12ad9c3c9876 | -11.73848 | -47.45101 | 2026-06-04 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb0bee5e-5ca3-3739-9dc5-9e3af9c33474 | -10.13903 | -49.15819 | 2026-06-04 04:44:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b1e3a67-c1e8-37d4-b7cd-7387bfbcd677 | -9.38842 | -48.62086 | 2026-06-04 04:44:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README9.md)
