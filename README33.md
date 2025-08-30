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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21947f9f-baf1-396c-9893-f6932e1e0115 | -11.86842 | -46.43002 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8a331c6-4b7b-37cc-9bee-d278f0865e1c | -14.00179 | -44.5391 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a91200e0-1a6b-3d54-a104-d01e3cace2e9 | -14.04009 | -44.51754 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e83b5ac2-c9fe-32c0-9872-164d63b38fb1 | -12.92808 | -48.12036 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0fc38aa-39c8-39cf-9e19-0d9327578c68 | -11.8448 | -46.38649 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6a61dbfd-0983-35b0-9593-45e06460871c | -13.6615 | -46.92393 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 997ec0a9-f36c-3066-b680-8d1c85036003 | -14.45904 | -52.02113 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6df6c04-699f-3602-9cea-28c138615621 | -13.9801 | -46.32325 | 2025-08-30 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e756666-a846-33f1-950c-e7d20828fac3 | -15.16678 | -52.32967 | 2025-08-30 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae5e9e25-2603-3251-9371-cdf23d3fc7b9 | -9.95887 | -46.34942 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 162ffb6e-b4c5-3bc3-a52f-91efcb9439e9 | -13.37771 | -47.01884 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0c75383c-e8ca-3a8c-8fea-7583ebc4ac28 | -9.70328 | -47.05436 | 2025-08-30 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6579d804-1ab8-3296-b0d5-cdf6536f6ba1 | -11.31537 | -43.64212 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a4b335f-5654-321c-b53f-80f091b452fb | -13.57079 | -46.91597 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3423803c-534d-3680-b3f0-0f429dc9b220 | -13.58239 | -46.90701 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d8223b8-754f-3ec3-a595-f5edf57401d5 | -11.40528 | -46.90487 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6315fbcc-8c25-36f0-afa0-3540059532a6 | -14.04294 | -44.49825 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| be3047f1-659d-33a2-aad1-702f9cd64f66 | -11.57546 | -46.34611 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52295415-17d2-356b-88fe-180165d0d933 | -13.50292 | -46.93727 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d017ceea-ce4c-38a6-8dbc-1814b5971eb7 | -11.86565 | -46.44759 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 440f1da2-62be-3b98-9e98-146f57760fe2 | -13.37052 | -47.0213 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b68a0dd-e188-32b1-ad1b-4d1fdf207f41 | -11.09992 | -44.74331 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8668c5b1-10a8-33de-9759-afd5174f972c | -12.69665 | -48.13945 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a923e53-3c8b-31cb-80b1-6834be890579 | -12.56789 | -44.80386 | 2025-08-30 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 432cdc6f-ad98-3e5e-8bef-bde486ed9602 | -11.86242 | -46.38214 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c9c078b-9075-3d5f-a83d-8982e7db8696 | -11.32691 | -43.61209 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24212167-192c-3c89-86a5-908b0c5d8495 | -14.50178 | -52.99535 | 2025-08-30 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 501cc132-68e8-3f85-a99c-8019d868590b | -13.46406 | -46.96732 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cb19d75-cece-3813-9ddb-b690084f760e | -8.55527 | -51.30935 | 2025-08-30 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 64572765-fb39-38f6-a52a-8dfcd371819f | -13.37098 | -46.99599 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cdc0c544-f05a-3446-b8e9-c8ce5d946cc1 | -12.92649 | -48.10872 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0184730b-f39b-3034-b7ea-9a2f19299794 | -11.31077 | -43.64931 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ef4e4e5-218e-3fb5-b66c-cea947317853 | -14.00192 | -44.58587 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 494aad23-de35-3e74-bc75-8dcc553559ff | -10.98962 | -46.84426 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20743010-6110-3e4e-a936-a8b30a022178 | -13.59567 | -46.88739 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e23b0a30-3d9e-3b6a-93d5-67c54572673d | -13.55195 | -46.94919 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1ea0201-e7a2-350d-af1d-5d8d3233bff1 | -11.3177 | -43.6504 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c4b156b-1801-3327-bff5-76754df6bc84 | -13.46082 | -46.94489 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2298cdb-8019-3331-aeda-801e3c5bc427 | -13.41221 | -46.95156 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84226d2e-11a0-33da-a645-48e0f2a0d01d | -10.07749 | -58.35971 | 2025-08-30 04:21:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 885db040-03ce-3b38-a2f0-2eb68dc6b19a | -11.08447 | -45.13092 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b23a6f77-b60b-3a21-ab6b-8f4070bae5f1 | -16.04957 | -49.04111 | 2025-08-30 04:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e3ff6849-17ed-3963-8702-9ee4619274d9 | -15.17327 | -48.02419 | 2025-08-30 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01739358-261b-350a-b175-daef1ca42a1e | -14.49987 | -52.05129 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86fda9a4-7d9b-3c14-9b99-c18d84ce1e02 | -9.58255 | -54.48056 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 903d1651-c47c-3972-89a4-72fb25390381 | -13.56966 | -46.92307 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d5e7e55-b819-350d-a0f3-3cdc815dbfa0 | -13.9985 | -44.58533 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f241b97-bc4e-3f1e-a84d-526730735ef0 | -11.30541 | -43.5649 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6028530-a3d5-33dd-9c5a-ff263bda4a86 | -11.57216 | -46.34557 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20614e00-2394-3fa3-98a0-2579898aa181 | -11.33614 | -43.5977 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 01d7f3ea-e76c-317c-bbc4-60d68248138e | -10.70786 | -47.07347 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e138fb93-337e-31e1-b724-cd0740303558 | -12.82925 | -48.12318 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d690b40-1885-3f42-81a7-83a6ecaa8c58 | -10.99598 | -46.95123 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49816e2b-56be-3c43-a32c-82ba6ebf87f6 | -12.82372 | -48.11427 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fecd605-2640-32c9-8a86-16777a81e35f | -13.60709 | -48.15724 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a486009d-cdc5-3fd6-b396-edde30f62553 | -14.0059 | -44.58263 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 960597fc-780b-39d7-a6aa-1f6be49c2e7e | -11.57931 | -46.36472 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94f542f5-4ca0-3f50-a6a9-9fb915be42eb | -14.04351 | -44.49439 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d0d5fdff-4c6a-3a4d-8d67-8d6286e0dc22 | -13.49796 | -46.83859 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f383516-d202-3166-9823-9057c755ed1f | -13.38289 | -46.96501 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3b8b3d57-1289-3b9e-b578-696e1ddc1dfd | -14.04066 | -44.51368 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b30ea489-e2a9-3ef8-b1ba-91f366a6f661 | -11.30255 | -43.58449 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8b715e88-0862-350a-99b9-173f714b6269 | -10.93568 | -47.43084 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75c3303e-be22-324b-93c8-12698b8754ba | -13.39379 | -47.00326 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 83dc06ad-2bf7-38d0-b680-f6757205ab1f | -13.66206 | -46.92039 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3c36b359-d08f-35e6-ae79-078edfd4ab5a | -14.31481 | -51.86889 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27259670-9171-31af-a664-a46b88369eea | -13.35911 | -46.87762 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70f3fbdd-4751-39d9-889d-ba2dfee3de86 | -11.85252 | -46.38053 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 112acddc-884f-34fc-bf8e-dfc7e683b10d | -14.02356 | -44.55805 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| aa8261ce-4dff-3010-bc8b-d9acabf2fdde | -10.64758 | -48.65117 | 2025-08-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ce499f7-1f34-3534-b777-839eddb60010 | -11.91731 | -46.70205 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ef58141-a6a9-33ea-bbb0-912294ab4182 | -12.65391 | -48.18643 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62131afd-74bc-3551-b7ae-a84efe2d2586 | -11.31656 | -43.65813 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cb041b94-725e-3588-a3f1-afda4f39b735 | -10.02186 | -48.08171 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a279402f-a66a-3c6b-9dff-6a9ebaa637c4 | -9.14895 | -59.56433 | 2025-08-30 04:21:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fdef5d2e-f5e3-3ed8-8d56-9456864f866c | -11.92175 | -46.69552 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1746ad12-c090-3081-8a9c-01febd09855c | -11.93337 | -46.68653 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b30b9e1-1fad-3ea7-9fca-6d6cd3c2a2fe | -13.53817 | -46.95044 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3ac5836-140e-3493-a224-f98d8137f506 | -12.65732 | -48.18701 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5170fd0a-7977-36c4-b258-24b286ab0c43 | -11.86952 | -46.42301 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 59eb887f-cf24-3a30-9768-fb28d9d983e2 | -11.41413 | -46.91359 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c5884ae-0c0f-30a3-bf2d-cff9e2e547a4 | -13.36823 | -46.99189 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e82614c6-0d1b-39c1-a094-5f380fa904ef | -13.59511 | -46.89093 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d223628-7ba7-35c2-a417-b6b092ef700f | -11.41109 | -48.95423 | 2025-08-30 04:21:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99ead590-7b9b-3bae-a848-9e22e2c9f01b | -12.93116 | -48.14426 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10d14835-636a-34d3-9ff9-1be492eaf810 | -10.17676 | -46.58397 | 2025-08-30 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b37780d-949e-369b-9743-da0f02b86acf | -13.37179 | -46.88337 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b65abb7a-0f4c-3195-924c-8f05de122b55 | -12.89755 | -48.88148 | 2025-08-30 04:21:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11ba2a8a-9c4a-38b6-96d1-980e2739c0d0 | -14.59626 | -54.54136 | 2025-08-30 04:21:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0f66633-a45d-34c8-8f55-e71524245188 | -11.87837 | -46.38842 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 14275d5c-6a93-31b0-b8f4-cb5d1f23ef66 | -12.33095 | -45.29177 | 2025-08-30 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23a118db-b87f-3564-af30-c8971bd21940 | -14.50731 | -52.05648 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 856f3a02-2274-3771-9308-65abca60025e | -9.69992 | -47.05381 | 2025-08-30 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d69913e8-fb51-38ed-bf3a-61512cdb5462 | -11.84921 | -46.38 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf8775f5-3ae7-3f11-9f42-6ff5dc26ccc0 | -11.48733 | -48.29241 | 2025-08-30 04:21:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c59754fe-c45e-33a2-9239-30a92a841db0 | -13.4365 | -46.94832 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45964250-c4a6-358d-a07e-063ff568d84f | -14.34439 | -51.88927 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e78c1331-78eb-3614-a7cc-187a52286d56 | -9.49182 | -45.40584 | 2025-08-30 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc576750-deea-3a9b-9cb7-b652f3ebb5fd | -10.99239 | -46.84837 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4189212d-8e99-340a-89a8-8eadae088d19 | -10.02691 | -48.09459 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README34.md)
