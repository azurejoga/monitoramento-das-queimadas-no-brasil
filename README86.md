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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3af1c34c-32dd-3bae-87eb-555b8ec98fd9 | -7.9797 | -44.2962 | 2026-08-31 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 137.1 |
| fb5486e7-caa6-30eb-9fd6-03edbc8cc4b3 | -11.9186 | -45.0685 | 2026-08-31 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| b02175c1-fb2b-3477-828b-ec5cafc6cc83 | -11.9378 | -45.0656 | 2026-08-31 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 8ca3dd40-6c9c-3fc7-944f-c61bb85ef299 | -14.1652 | -52.7847 | 2026-08-31 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| c964538e-9924-31bc-99c2-377a9ab54071 | -18.2704 | -52.6851 | 2026-08-31 13:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 1eee6ba2-2ad1-3b51-ad77-121b9810ac5a | -5.5647 | -60.2312 | 2026-08-31 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 224.4 |
| 31182006-3f51-3b4c-bd35-f1e5ec4e9366 | -11.4828 | -58.5159 | 2026-08-31 13:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| dbe6e52e-ff94-3489-9cac-f295c60d972f | -14.5868 | -54.1153 | 2026-08-31 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e3c9a18e-1a38-309b-92c0-2c5f4a8db74c | -6.6221 | -58.5771 | 2026-08-31 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 7fb74eef-320c-38d0-9b47-19f6b766371c | -11.3419 | -45.2212 | 2026-08-31 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d329eae5-ed70-338e-8022-2a5d4c8848be | -11.2294 | -45.099 | 2026-08-31 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 085efbfe-fadd-32fa-bb0a-ee73a1794acc | -5.8692 | -52.0868 | 2026-08-31 13:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| de0752b2-44c9-3b4c-9e7b-6c7fb48f7e15 | -7.9605 | -44.3212 | 2026-08-31 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 264.0 |
| 5b7ab681-f648-3c99-aa02-c0fe3ff728ac | -5.2548 | -55.8907 | 2026-08-31 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| b155bf34-5aed-3c3f-bd50-f2638018aa1a | -11.3232 | -45.2009 | 2026-08-31 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| af5a523f-ed83-39b9-8f9a-90a7372b6afe | -14.1459 | -52.7871 | 2026-08-31 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 9b9cf5d0-4abe-318d-9608-cdcdf90ba5a2 | -10.1531 | -45.7438 | 2026-08-31 13:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| cfe2b065-36a9-3178-a1c1-bad2bbb79cdd | -11.5275 | -45.5392 | 2026-08-31 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 4b3f4d9f-b00d-3017-9378-95d8b2fc11c5 | -11.3423 | -45.1982 | 2026-08-31 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 664a8b47-cf6b-34bb-90d6-5f5f5e806f82 | -10.8624 | -45.3789 | 2026-08-31 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 532f6a88-48ba-33ce-981b-5e098a2e5327 | -7.1123 | -42.7727 | 2026-08-31 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 4a783d43-5da6-33f8-8a29-1f8e0fe28309 | -5.2547 | -55.9105 | 2026-08-31 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 03423b75-4a19-3a31-bdab-cbbf2d2b617e | -11.1634 | -50.5727 | 2026-08-31 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 4801f5c2-6519-3022-9617-16324ca4180c | -11.2482 | -45.1194 | 2026-08-31 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a750997b-b2a0-31e6-be2b-ee47a12bf1d9 | -6.1109 | -57.684 | 2026-08-31 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| b4733726-f4c8-316b-b318-1cb7b68086ea | -11.5475 | -45.4906 | 2026-08-31 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 260.1 |
| 02405c23-b7b7-3e9e-9501-7a3a00d84e11 | -19.154 | -57.3978 | 2026-08-31 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 198.2 |
| 55f537ff-d32a-31da-b844-cea7d63d04cd | -11.5283 | -45.4933 | 2026-08-31 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 376.5 |
| 10c854fb-03d0-3626-8b28-d4f2d95e8f3b | -8.1537 | -45.4677 | 2026-08-31 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| a32d6047-6239-314f-b2ac-c0ab509d58d6 | -10.7596 | -54.0384 | 2026-08-31 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 53061819-884b-3b50-a11f-78aaa9e40cce | -19.114 | -57.4031 | 2026-08-31 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.0 |
| a0f84f5c-fbec-3617-af35-e1370dff0462 | -7.9239 | -44.2327 | 2026-08-31 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 8b4519b9-78da-3d80-96c1-eeed3ad83908 | -11.3767 | -45.423 | 2026-08-31 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.0 |
| f20eb5c5-dbd9-3612-9707-437bd8064687 | -7.5843 | -61.3803 | 2026-08-31 13:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 25ff1cff-e35e-3a3c-b1cd-3c4b69baded3 | -8.7442 | -46.4437 | 2026-08-31 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 219.4 |
| 50e0df75-fc2b-3877-8192-62f3881e068c | -10.7407 | -54.0401 | 2026-08-31 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| a37069dc-63de-3ca4-8f5a-487a72be5f28 | -14.4007 | -52.5226 | 2026-08-31 13:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 01628fbe-64be-3158-8387-e0cd6ee452ce | -6.9367 | -55.636 | 2026-08-31 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 66d06fc0-b488-3521-bd2a-0763d79ec6c0 | -6.6036 | -58.5972 | 2026-08-31 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 417.4 |
| 10f4a14b-e8f3-3c33-a608-069c24d46812 | -11.2506 | -53.9941 | 2026-08-31 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 354664a3-da42-38ab-be11-dc89edc4af29 | -7.3119 | -60.5706 | 2026-08-31 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e67d7d7a-953c-3909-a28c-2e41fb472999 | -11.1824 | -50.5706 | 2026-08-31 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| d7d7bf41-ae7e-3604-98c4-417c6efc5bfd | -5.5831 | -60.2307 | 2026-08-31 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 356.3 |
| f0965aac-918d-3cd8-a133-399ed3e296a4 | -7.9236 | -44.2558 | 2026-08-31 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| c1cf83ea-c58c-3695-aad9-c8ccb05f2881 | -7.98 | -44.32 | 2026-08-31 13:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6eb240a6-ed53-33b5-90be-8043bf308dfd | -7.95 | -44.31 | 2026-08-31 13:15:00 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 808b5788-5b7e-3b1b-9705-097b6a0f6ab1 | -18.2695 | -52.7284 | 2026-08-31 13:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 0e6dae14-5bd5-3821-9d1e-9d74c648a339 | -7.1126 | -42.749 | 2026-08-31 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| dee21ceb-74b8-3d3e-81c3-526f658ab614 | -14.2796 | -52.8547 | 2026-08-31 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 2d3882ff-5c1d-3273-a73e-08b35119c729 | -11.3236 | -45.1778 | 2026-08-31 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 3d18091c-b031-3880-9b7b-773c2cf8de6f | -11.9186 | -45.0685 | 2026-08-31 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 6f6cdda3-0a06-36f1-8484-082688387466 | -10.8433 | -45.3815 | 2026-08-31 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 84af7dd5-5786-39d3-b578-aeb67c17f143 | -10.3394 | -49.9547 | 2026-08-31 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 96ac4299-86c7-3259-b89c-4ee962588373 | -14.2792 | -52.8758 | 2026-08-31 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| ecf9bd05-0744-3973-93cd-5c0b84f03c48 | -11.1634 | -50.5727 | 2026-08-31 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 93cd471f-4e7d-322b-a9a5-a1033e279519 | -7.3119 | -60.5706 | 2026-08-31 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b4376a35-78dc-3e7c-8cef-4376228438c2 | -9.8015 | -46.4629 | 2026-08-31 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| a37425be-7316-3640-98fe-df965ae44d85 | -6.1295 | -57.6637 | 2026-08-31 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| dbc04c2f-7d73-3d4e-bd35-f4603ca3772f | -12.9032 | -45.8382 | 2026-08-31 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b78548bd-db2b-3403-b4de-f581fa470847 | -11.5475 | -45.4906 | 2026-08-31 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 0f4de873-8d92-312f-9672-7d80b2e42d26 | -7.9236 | -44.2558 | 2026-08-31 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| bc348ed8-6194-31ff-af95-dccc6eab54f9 | -7.3118 | -60.5897 | 2026-08-31 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| d68b908c-a66e-3436-97aa-6f2b0904bb57 | -11.1821 | -50.592 | 2026-08-31 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 3c51f3e3-126a-3623-9ffa-455c4b9d2f2c | -5.5647 | -60.2312 | 2026-08-31 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 1ae93591-d81d-3d11-9653-813f8f69d23f | -11.2294 | -45.099 | 2026-08-31 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 18aeb7bb-178c-393e-bbda-e38d71a78a20 | -10.8212 | -50.6732 | 2026-08-31 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| bdda7297-2d04-34f6-87de-0ebfab37c7b2 | -8.7989 | -62.5095 | 2026-08-31 13:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 52033f36-febb-3462-ad61-e01f34e9a8e0 | -14.1459 | -52.7871 | 2026-08-31 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 308997a8-c5e0-3a2d-9fe8-f87548042f85 | -14.4201 | -52.5201 | 2026-08-31 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 688cfe50-6bb2-3d20-ae5f-a47e5fa7fb1b | -6.9177 | -55.6967 | 2026-08-31 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 4a529e60-9ebf-39f4-a81a-be25070c4479 | -7.9605 | -44.3212 | 2026-08-31 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.1 |
| c4b3a8c3-383b-3264-b169-599c6a93dad0 | -11.3423 | -45.1982 | 2026-08-31 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| e0cf131f-e797-37da-ace2-11aac357c46d | -11.5283 | -45.4933 | 2026-08-31 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 9be59bef-37ac-3320-a0ae-378b17606b8d | -8.1672 | -54.9246 | 2026-08-31 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| c0d3c45b-77ea-34d7-861c-12125b651884 | -11.2506 | -53.9941 | 2026-08-31 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 4425df78-b09a-35da-9c3e-42862408354b | -6.1109 | -57.684 | 2026-08-31 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| ca1c2031-bf3f-33c1-95c4-a5612d7b3896 | -14.4394 | -52.5176 | 2026-08-31 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 4da266bc-3044-3966-97f2-b30b3e715dc9 | -10.8624 | -45.3789 | 2026-08-31 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 535f2c52-dc09-3d01-a1e6-3e2d542a92d1 | -11.9378 | -45.0656 | 2026-08-31 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 3b7e4316-d585-33e0-aec2-2050974a68b0 | -10.7407 | -54.0401 | 2026-08-31 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 05b6b7ac-c62c-3d66-934f-10670076f4fd | -5.2548 | -55.8907 | 2026-08-31 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 19a5aa2c-380a-3fe9-9fff-aa26a845269b | -19.154 | -57.3978 | 2026-08-31 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 226.4 |
| e11087e2-6dc7-38e3-a8cb-7c806e57eb27 | -5.5832 | -60.2116 | 2026-08-31 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b7ee1c8d-9b21-3407-80bf-4f766330ae13 | -7.5843 | -61.3803 | 2026-08-31 13:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c3234f15-f134-3f4e-886b-43d1367b3f87 | -18.2904 | -52.6818 | 2026-08-31 13:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 664d7388-03e0-3317-9e8c-6f1286cb6cd3 | -11.1824 | -50.5706 | 2026-08-31 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| bf69201d-e2ab-3f7b-81d1-ca1f0ccb7065 | -6.6036 | -58.5972 | 2026-08-31 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 537.3 |
| aa867363-9d07-3161-9369-73f26d1d32f5 | -7.6253 | -55.2787 | 2026-08-31 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ea4fe898-20f3-3a47-9c2a-09d931601b36 | -19.1344 | -57.3797 | 2026-08-31 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 191.0 |
| 119ab180-b333-3c11-be59-6838291aecaf | -8.7439 | -46.4661 | 2026-08-31 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 8d82d9f6-9574-3eee-a5c7-32a5185b7a4a | -5.2547 | -55.9105 | 2026-08-31 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| b6926640-b6ba-3cf0-b2a2-631e1c229379 | -7.9797 | -44.2962 | 2026-08-31 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 408c9db9-fd73-37dd-ae4e-d5f2ab0dbe97 | -6.9367 | -55.636 | 2026-08-31 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| a08efb52-68fc-317e-8d7b-461662e1fccd | -10.7596 | -54.0384 | 2026-08-31 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 3499412d-b2ad-3e8c-aa2e-f18e0eb879d5 | -14.5868 | -54.1153 | 2026-08-31 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 9085402f-c86a-3d89-a950-d9364eef7013 | -11.3232 | -45.2009 | 2026-08-31 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 47acfbe8-6701-3397-9f3a-d8ca1ad263d5 | -11.4828 | -58.5159 | 2026-08-31 13:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 3bb0232d-e28a-3b1e-8e58-a39414c13c0a | -10.7459 | -47.9757 | 2026-08-31 13:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 25300a9f-db84-3876-9e0e-125c89644dc6 | -6.6035 | -58.6166 | 2026-08-31 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 154.2 |
| 7d4d0343-4839-399c-9a02-8a95439e2972 | -10.8541 | -48.3587 | 2026-08-31 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |


[Clique aqui para ver as próximas entradas](README87.md)
