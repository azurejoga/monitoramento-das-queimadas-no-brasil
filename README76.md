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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd412223-8353-37e1-a295-f63545de164a | -10.83469 | -45.33199 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c6bd102f-f2b5-3adc-8f78-ea815b7bdcff | -7.61807 | -44.86655 | 2026-08-30 11:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 1896b349-83f2-3fe3-9cd2-bac73c43d21c | -6.87474 | -41.66428 | 2026-08-30 11:32:00 | TERRA_M-M | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 3aeee013-aba8-32ce-a25f-56418855c2ef | -7.10198 | -42.21636 | 2026-08-30 11:32:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a5182961-da4b-3298-8173-5d76c6e94d13 | -10.83334 | -45.34116 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 6f231353-b435-367b-b1ba-a491522a1d4a | -10.82687 | -45.31545 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d91565b4-98dc-3ecb-909d-87d8887b93e5 | -7.6194 | -44.85742 | 2026-08-30 11:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 220fd2af-bb89-34fc-8578-c32790c1e1ab | -6.87207 | -41.68354 | 2026-08-30 11:32:00 | TERRA_M-M | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| e94ae253-06b0-3e80-aed3-861f8a54a58f | -6.62697 | -43.73908 | 2026-08-30 11:32:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 342d5b6b-bd0b-3dee-a102-978d65d3b450 | -6.81876 | -45.5434 | 2026-08-30 11:32:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 457be966-57c5-3ff7-abef-d807fbbd0a02 | -7.94143 | -44.29562 | 2026-08-30 11:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2be584f2-47ce-39b3-b963-73be2c673f26 | -11.53956 | -45.48882 | 2026-08-30 11:32:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 55562c22-4bf4-3460-beeb-b0f5617627d6 | -11.48283 | -45.05644 | 2026-08-30 11:32:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 42c05a39-c59b-3453-b78d-7b01c4e96fcf | -7.62206 | -44.83915 | 2026-08-30 11:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| d1a53d3c-7c38-3450-ad02-45068f631f18 | -7.40918 | -44.27391 | 2026-08-30 11:32:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 6c62931e-24a1-37fc-be67-d2a97f3da613 | -7.31867 | -45.34031 | 2026-08-30 11:32:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5c49940c-5cf3-3dfd-b557-4b840f1ffa6b | -7.09937 | -42.23487 | 2026-08-30 11:32:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fd1bfd75-31ad-318e-99bf-5435fa98d45a | -10.14507 | -45.68924 | 2026-08-30 11:32:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 855889c0-d74f-3b9c-8246-84f01358b612 | -7.41048 | -44.26495 | 2026-08-30 11:32:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ae8d731-5ef7-3c64-93c8-2b6c0b286a15 | -7.10067 | -42.22562 | 2026-08-30 11:32:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 26070dbd-5711-3f38-90b1-11f9fe41cd16 | -11.2115 | -45.08144 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 41be6570-06f4-3261-ba7e-042453df46e2 | -10.81662 | -45.32329 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 46703924-730b-3708-a27a-125c3528a3b9 | -10.49197 | -42.41325 | 2026-08-30 11:32:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| f499ea72-47fb-3e15-b3fa-292e45ad0b19 | -11.53823 | -45.49799 | 2026-08-30 11:32:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 96837729-db83-3c5d-8699-7c6fc735b300 | -10.81795 | -45.31414 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| ef65eb91-9142-3a85-8e3a-edf6ae34f460 | -10.82422 | -45.33376 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 68c61176-de24-3a65-9442-84d0aeb90e38 | -7.94528 | -44.26897 | 2026-08-30 11:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| b248382e-254d-3f89-90c6-1a133d48fedd | -8.14546 | -45.48293 | 2026-08-30 11:32:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| c73acbb2-7a6f-3503-ba9b-947352cc0047 | -10.77958 | -45.32721 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ae9f50e-9a6b-3006-830a-e3873a126c4b | -11.21281 | -45.07237 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 21df03dc-bd2e-3147-a62b-79a3d1b243f0 | -10.7787 | -44.8861 | 2026-08-30 11:32:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| ab1e519c-ee33-3628-aee1-189f3dad4be2 | -7.11497 | -42.18963 | 2026-08-30 11:32:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d917f0ff-c506-3bad-8852-606d76567d02 | -6.34632 | -44.09432 | 2026-08-30 11:32:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 73b55cd9-512a-3e83-b596-431491c534bc | -11.27838 | -45.3194 | 2026-08-30 11:32:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b4be5aea-49cc-3546-9627-5685de1cd9ee | -10.77497 | -50.63353 | 2026-08-30 11:32:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c9ac9fca-a215-3d07-943a-3c58bb172724 | -5.51603 | -39.87199 | 2026-08-30 11:32:00 | TERRA_M-M | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 7574f802-e10b-3691-96ba-cae46ce20c2e | -10.15274 | -45.69995 | 2026-08-30 11:32:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2f0941b0-ae89-347b-8d8a-20709d74922e | -7.61176 | -44.84694 | 2026-08-30 11:32:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| eaa5dfdc-c799-352d-83e4-056e50b94445 | -9.78795 | -46.41663 | 2026-08-30 11:32:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4b18e72b-e838-3120-aca7-51e66641a283 | -10.14366 | -45.69873 | 2026-08-30 11:32:00 | TERRA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 6d985b85-5982-3fca-8827-dd4580093dfe | -12.92326 | -45.86924 | 2026-08-30 11:34:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 58afaec1-1a35-3c2a-ac70-e6891ae37ae2 | -18.46143 | -44.90451 | 2026-08-30 11:34:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 65fdc08d-2cae-3942-b9e5-06cd520af2fa | -12.90264 | -45.88507 | 2026-08-30 11:34:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d8ae6b58-c1f9-3bd6-95ac-41e25c437568 | -13.64256 | -45.55146 | 2026-08-30 11:34:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f4241508-c0bf-324b-9f2b-4a5db9a1b277 | -12.91918 | -45.89704 | 2026-08-30 11:34:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e6dc39e1-6585-3e04-b4a8-2b9eef736992 | -11.81588 | -51.02361 | 2026-08-30 11:34:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| db7fd520-ec63-341f-a252-3d91b3da8904 | -14.15467 | -52.7953 | 2026-08-30 11:34:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9450aa59-a507-38ad-9460-1999a4ed26c1 | -11.4993 | -46.95218 | 2026-08-30 11:34:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2ad84df5-dca2-36a9-b482-e7c3e8af34c3 | -14.23848 | -42.23012 | 2026-08-30 11:34:00 | TERRA_M-M | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 929cf921-9246-30b4-a6d3-fedb90614307 | -12.07442 | -42.5389 | 2026-08-30 11:34:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 271f3b36-8c21-39b8-b59b-bfa284ef3604 | -12.92813 | -45.8984 | 2026-08-30 11:34:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 712e61f6-dc49-3e5e-8759-0b31134432d7 | -21.34615 | -46.07944 | 2026-08-30 11:34:00 | TERRA_M-M | AREADO | MINAS GERAIS | Brasil | 3104304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d9d8c40e-9cc8-335c-8723-8e04e7d81502 | -14.15024 | -52.78746 | 2026-08-30 11:34:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 6ef02d17-8daf-39c8-9d31-f73b28f00f72 | -12.78104 | -46.46012 | 2026-08-30 11:34:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 169172dc-9189-329f-8497-b84a7bfe065a | -13.28853 | -43.29343 | 2026-08-30 11:34:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 9d7b3308-b5c1-315e-9d85-ddef96d8d6f5 | -14.15025 | -52.81991 | 2026-08-30 11:34:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 14e5c7e5-b44f-3424-abb7-64d76b178e0b | -12.36729 | -48.19041 | 2026-08-30 11:34:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 99ce6476-abad-3439-b3a6-c151449f84e0 | -12.904 | -45.87581 | 2026-08-30 11:34:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 25e7a3ee-9251-3a54-a954-3f47d0624166 | -13.28721 | -43.30309 | 2026-08-30 11:34:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 96e67bba-01b4-388f-bf96-c8a908366d87 | -11.68806 | -47.61586 | 2026-08-30 11:34:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 46f91f8f-9efb-3d8c-b230-766fd33e4473 | -16.34481 | -50.97935 | 2026-08-30 11:34:00 | TERRA_M-M | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 0dc0ab0b-6758-38e2-a74d-ba0a91bb6f41 | -12.92462 | -45.85996 | 2026-08-30 11:34:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 986a6aa9-18a2-3ab4-929a-3a6e921eff25 | -14.42717 | -52.5383 | 2026-08-30 11:34:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 30f1e5b1-c1f0-3322-808d-a7ab6eb1bd59 | -17.28428 | -46.01019 | 2026-08-30 11:34:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4db69998-1a43-38f0-ad9f-e2b31aceebb0 | -12.89505 | -45.87446 | 2026-08-30 11:34:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c7c593cf-11ea-391a-bcd4-cd6da26a46e5 | -18.47172 | -44.89625 | 2026-08-30 11:34:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 13dc1624-64ce-37c4-a161-efd50efd7c88 | -18.47041 | -44.90582 | 2026-08-30 11:34:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 449a3f12-9ec8-35ed-945e-1322bf038071 | -13.31725 | -42.39817 | 2026-08-30 11:34:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 5bcc92a9-8d72-3cff-aa3f-5a467a4c5e31 | -21.35503 | -46.08086 | 2026-08-30 11:34:00 | TERRA_M-M | AREADO | MINAS GERAIS | Brasil | 3104304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 587648ec-e4a3-355d-9efb-2d084a9ff445 | -14.14598 | -52.81216 | 2026-08-30 11:34:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 5e999b8e-3d58-394a-81a6-3fd1d0327b39 | -13.64125 | -45.56057 | 2026-08-30 11:34:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f97fc68f-99b8-366e-925f-57ecc0cf9c54 | -22.99661 | -46.51868 | 2026-08-30 11:36:00 | TERRA_M-M | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9b002f97-609f-3177-b4c2-b8dd92140720 | -22.99795 | -46.50908 | 2026-08-30 11:36:00 | TERRA_M-M | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| 028a36af-1f39-38c3-ac84-1b7f115516ae | -22.41544 | -47.62209 | 2026-08-30 11:36:00 | TERRA_M-M | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 07763e4c-3e1c-38ac-8999-60da98f92c53 | -7.9425 | -44.2538 | 2026-08-30 11:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| d02b1c73-24c1-3de1-ac68-81cbfc223b24 | -7.9611 | -44.275 | 2026-08-30 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 6d1e9b11-c8d5-3e2b-9d4a-e207242976a6 | -14.1649 | -52.8058 | 2026-08-30 11:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| c9463df4-a04a-3b93-ad74-12e96fceea74 | -7.9422 | -44.277 | 2026-08-30 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 769f8a8e-24dc-3bcf-ade6-7a791cee4d7b | -4.9604 | -55.8424 | 2026-08-30 11:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a0c16322-76d1-3084-a1b8-f3e1c61e1723 | -14.1456 | -52.8082 | 2026-08-30 11:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 34ff9ce0-6aef-3a62-9def-f43722e5e7f1 | -11.8211 | -51.0322 | 2026-08-30 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 3ffdce29-73d1-35f2-a303-49aea2ab4bc4 | -11.8021 | -51.0343 | 2026-08-30 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 0a3bbf32-ef0a-33f4-8435-b2c509a6d2af | -7.9611 | -44.275 | 2026-08-30 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 193.2 |
| b8c0f666-0e10-31aa-aa26-9233d0593b05 | -14.1456 | -52.8082 | 2026-08-30 11:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 8da54ea0-7d2b-36f2-93ce-4b60cc1d25bd | -10.1348 | -45.7006 | 2026-08-30 11:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 92b34ca9-c132-3638-b874-f51c455af56e | -7.9425 | -44.2538 | 2026-08-30 11:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 3c74da32-bb87-3c92-a4d7-14fadd411f25 | -14.1649 | -52.8058 | 2026-08-30 11:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 7df68af7-980a-338a-bd89-2bde1ea23b73 | -4.9604 | -55.8424 | 2026-08-30 11:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 9696877b-a44e-39e1-89ad-76a659f443cb | -10.1538 | -45.6982 | 2026-08-30 11:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 1a0c6084-2a2d-3e25-be4f-b9440f6834e7 | -6.861 | -41.6772 | 2026-08-30 11:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 0c9a7bb2-23f2-39ef-822b-c57ca53e2f12 | -7.9422 | -44.277 | 2026-08-30 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 282.2 |
| db452c1b-c1b7-36de-961c-3f092bdad56e | -11.8211 | -51.0322 | 2026-08-30 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| cadb2097-30b3-3674-893f-9b546c52e4bc | -6.8613 | -41.6532 | 2026-08-30 11:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| bec3b963-a025-39f4-b3b8-92d95cedac1e | -7.5136 | -55.3251 | 2026-08-30 12:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 46103722-a8b3-3f7e-b790-161b438f8cd9 | -12.9405 | -45.9011 | 2026-08-30 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| d26d8b2c-8f20-3bbc-8a6e-b47a5c30f6e1 | -10.1538 | -45.6982 | 2026-08-30 12:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 051528cc-1356-399e-bcee-480f18e48624 | -14.1456 | -52.8082 | 2026-08-30 12:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| d7111d3d-ba25-3504-94a1-c8012d75ce62 | -14.4197 | -52.5413 | 2026-08-30 12:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e5a22f09-6661-3630-bd33-3b6471193fd0 | -12.9216 | -45.8812 | 2026-08-30 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| b31590d9-ca99-3b3a-8f0a-261a3012da6b | -10.1348 | -45.7006 | 2026-08-30 12:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |


[Clique aqui para ver as próximas entradas](README77.md)
