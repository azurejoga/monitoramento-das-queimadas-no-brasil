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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ee195d2-3609-303f-b21c-a0bcea63a5ac | -15.59708 | -48.33131 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fafecf8d-a19e-3124-a337-eee95e15bbae | -10.61424 | -53.98184 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| af717ce2-29bd-361c-898c-18b7245db9bf | -18.52114 | -50.3302 | 2026-09-22 05:25:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a016b130-5854-3387-bdc2-486e3a28f613 | -9.30112 | -58.91635 | 2026-09-22 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce1c039b-c459-3519-ae91-293ff4615495 | -8.60197 | -54.62969 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8521a41-a76f-3901-86b3-01b64bbccabd | -11.4028 | -46.77072 | 2026-09-22 05:25:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38c63dcc-9665-3609-ac09-146b37419d81 | -8.25779 | -55.29411 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 581a5ab8-509d-3e07-92b5-c2f117591c94 | -10.60046 | -53.99476 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4dd2821-b83d-3d7d-959d-53ff1b2e5750 | -8.2456 | -55.2562 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6910718e-3e7a-3915-a40d-da44c0885568 | -15.44042 | -48.46982 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6aa1095-83e7-3572-828f-ca88939e7f98 | -16.84627 | -56.7857 | 2026-09-22 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 24dda006-6922-3a31-b359-a9d58617db8e | -8.61591 | -54.63615 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e207d86f-6102-3324-ad39-dbc519093141 | -9.12776 | -58.89196 | 2026-09-22 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cafdb18-f22d-3626-bd19-2478b1dbcf2b | -11.44643 | -47.33363 | 2026-09-22 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40534fab-3933-3017-9a41-0e5df8c8e724 | -8.61654 | -54.63194 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c25c7a4-d21a-34c2-a9cb-3b71f6ce6429 | -9.24516 | -57.15558 | 2026-09-22 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63a13046-df0f-3dd1-bf79-eb4a6a04cf5a | -9.87813 | -55.85986 | 2026-09-22 05:25:00 | NPP-375D | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bdec731-b43f-3d29-97d4-4cad71d35dfa | -8.26009 | -55.30248 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb0e69f5-1bc2-305e-ad1f-ec1de972db1c | -8.60511 | -54.60851 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85195366-5975-3d1a-b354-cb81aa1f0fbd | -11.10799 | -48.31749 | 2026-09-22 05:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55740b9c-ea88-3156-bc60-0fd0851cb577 | -9.8773 | -55.72406 | 2026-09-22 05:25:00 | NPP-375D | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a091198-5331-3ab5-a96d-bcd806f7b350 | -10.68905 | -48.72004 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 318520b0-678f-3e53-b7d2-77d7a1e17a81 | -9.88597 | -48.45261 | 2026-09-22 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5ab2344-ba7c-3cdb-92dc-9a90d9a9aff7 | -10.69467 | -48.71997 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38e74688-e0a5-324b-b280-7a0b50ce6211 | -7.69373 | -61.54166 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84b42be5-f1d6-3c58-b808-21c3fcd82e2e | -8.26202 | -55.26669 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fb23272-8340-3778-81bf-ec0e3161408f | -11.41242 | -46.79737 | 2026-09-22 05:25:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fa53fb7d-d73d-33f6-b21a-33c8b031d9b5 | -10.69505 | -48.71695 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01553fb0-198a-31da-9a2f-6eaab1218f3d | -15.65387 | -52.68973 | 2026-09-22 05:25:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e3e6e1e-42ad-3dae-8824-e7d6e4ad9246 | -9.67625 | -54.33665 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67c4ffc6-bf22-3c1b-b045-528f40833f7f | -9.88525 | -48.45115 | 2026-09-22 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 738a528e-d94a-3468-b58c-ed0739a1076a | -15.44341 | -48.44265 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 87605955-2441-31a8-9c8d-772d39fca4dd | -9.97001 | -50.25981 | 2026-09-22 05:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f04dd078-5646-3d5f-9b48-c5a9ef89644d | -9.69235 | -54.82671 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c491717-2c35-3ba7-90ed-558822f26e4d | -8.91432 | -50.92649 | 2026-09-22 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a3f9047d-b165-3586-90c5-60bb3b8d9fe4 | -8.6026 | -54.62546 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1859c57d-f49a-3696-9c62-06344acfcf8f | -10.38316 | -54.39912 | 2026-09-22 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cd1f675e-5a79-3cdc-8d2c-a65a405919ed | -9.28503 | -60.61433 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f96b26b9-6ab8-310a-9f84-d9bb47a5a7bb | -9.02367 | -60.36277 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 996bd810-c0c7-3b04-a7ba-b93b5264da1a | -11.41948 | -47.35196 | 2026-09-22 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8cc59b7d-fdd0-3853-bcbb-45f2c779a0d8 | -10.46688 | -46.28976 | 2026-09-22 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01ebfa45-f938-3867-b6b6-3dc7dae327af | -10.60821 | -53.99585 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0b778f5b-ed1a-322d-a2a9-106753589d11 | -10.47393 | -46.28561 | 2026-09-22 05:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 379343e2-45c0-3cfc-be4e-7136ab3da607 | -10.26063 | -49.98319 | 2026-09-22 05:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 61d48405-5aff-30cf-9116-2fd5453707ac | -15.44586 | -48.47525 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9eb1403-713f-35d1-8d8f-827422f32807 | -9.5537 | -47.95038 | 2026-09-22 05:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c2a4ab1-f751-3043-b55f-2e51dd403278 | -21.46514 | -48.67627 | 2026-09-22 05:25:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f2bce04-d2a5-3e90-a74d-1ebbe7deeb08 | -11.10658 | -48.32873 | 2026-09-22 05:25:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5696669-8b85-3dad-869d-dbc23eb493f3 | -10.61352 | -53.98672 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| bf007d84-a154-3057-a65b-6877175cac41 | -16.99131 | -56.44859 | 2026-09-22 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 86d4d956-fa85-3991-9f47-2f84ed328862 | -9.0313 | -60.36006 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d723028-177b-33c0-8af2-714fcc00c177 | -7.6975 | -61.54229 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99157be6-95e2-3225-9deb-5165e983d390 | -15.59756 | -48.32699 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d582090-3a06-3bf0-a723-25b449f9bee0 | -9.27819 | -60.63359 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c2baa3a-9d85-3128-b787-a7f85d628ba0 | -9.66877 | -54.33543 | 2026-09-22 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec1960fe-937d-3700-93e9-3eeb4538b698 | -11.10038 | -48.33205 | 2026-09-22 05:25:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a2623bf5-dc6a-31de-b93c-e74967467fc5 | -10.5973 | -53.98935 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd6d7f9f-70f1-3fc9-b2e5-a7bc55250464 | -10.85209 | -50.15364 | 2026-09-22 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f2dc385-5155-3124-a1e1-4ecce250cc4f | -9.01382 | -57.11946 | 2026-09-22 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 333caa36-ca78-35ae-9377-928b03579399 | -15.445 | -48.48298 | 2026-09-22 05:25:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fcf2763d-0032-3c83-b03f-90aaf7584426 | -10.61038 | -53.98801 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| c8d4534c-53c2-3526-8b6d-7298432b4f56 | -9.51806 | -58.87125 | 2026-09-22 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 199c2461-83ff-3941-947e-b6a7bbb89800 | -10.5864 | -53.98276 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a2df14a-f90b-33b6-887c-25445f26d6f3 | -9.89589 | -57.05672 | 2026-09-22 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68137380-01a8-3196-982c-8006b758a2bc | -10.45789 | -51.3409 | 2026-09-22 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fcfd366-9a7b-365d-8569-3716575788e6 | -21.46178 | -48.67547 | 2026-09-22 05:25:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 69fa6f78-9d1a-3776-b4fc-39dc229394db | -10.69542 | -48.71397 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32e512a5-e17a-3dd7-b50a-3341816ffa59 | -18.52237 | -50.31889 | 2026-09-22 05:25:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 56323590-880b-3fa8-963c-466f344fe9f9 | -9.12834 | -58.88838 | 2026-09-22 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7038fa2a-b295-33b3-9069-a61318a09ee8 | -8.92731 | -50.90072 | 2026-09-22 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa6f97c0-8ace-30c1-be09-55677f72632f | -16.84986 | -56.78626 | 2026-09-22 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 15f366ea-14d0-3737-bda5-5beb201e2987 | -10.90729 | -47.38109 | 2026-09-22 05:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac37ffaf-8872-3177-aa0f-e920861fd232 | -8.26051 | -55.30147 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f437cbe-9040-336f-b56f-a6d8ccf3ac16 | -10.6065 | -53.98744 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 2cb346ef-caaf-34ac-b6e5-beb1855ccb50 | -9.93667 | -57.51165 | 2026-09-22 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4778df3-7242-39f7-a9a9-ec30342fc3b5 | -18.04258 | -50.9268 | 2026-09-22 05:25:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ae16e246-cc78-3db1-a534-bb4fa79e249a | -11.43972 | -47.33786 | 2026-09-22 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 774ffb01-51cd-3efa-a02f-d1ee01799189 | -10.41873 | -53.79374 | 2026-09-22 05:25:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e31828e-4c1a-39f4-abbd-d6a6b44253e3 | -10.45479 | -51.27138 | 2026-09-22 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a7dc839-7362-356c-9ce4-52d54cfd2ead | -7.45773 | -61.38067 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 424cc73d-66a3-3c46-aa28-64019179011b | -8.23905 | -55.27538 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddd34789-c98a-35c5-b67f-91d89b8a0f8c | -7.69448 | -61.53708 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fa66e0a-4384-3dac-8ae0-adb5972380e4 | -8.62572 | -54.62034 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e1e1226-173b-3de9-8ba7-ef6ca7e63f69 | -10.61175 | -53.97826 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| cd115c02-909a-3da9-a52e-89942f5624c5 | -10.69041 | -48.71078 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df414b30-b7dc-3bb2-9859-ba0567e812a6 | -9.27732 | -60.61711 | 2026-09-22 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19d3d4cd-1721-3343-9711-fb20f6189f75 | -9.59364 | -47.77695 | 2026-09-22 05:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c292fe0e-7fc9-365f-aeb4-cf097b4c51b1 | -10.59802 | -53.98448 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df90b689-4a45-34e1-b476-1096d1442e25 | -18.51605 | -50.32576 | 2026-09-22 05:25:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6db8f573-d86a-3da7-8a8d-45c87a6515e9 | -10.6128 | -53.99158 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| b59fe147-d33c-375b-9f0d-1e34d55367ba | -10.68908 | -48.7209 | 2026-09-22 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7a8deae2-8c8f-3d85-9a78-88249f15a01b | -8.26422 | -55.2991 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05d5e3be-69e0-393c-a5f3-4a4fc6435f53 | -8.26755 | -55.30252 | 2026-09-22 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7dd870de-03af-337e-86db-cd105f6db09f | -8.61906 | -54.61499 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa69088f-7f0f-39be-8e3e-ea1545a97ddc | -8.62509 | -54.62457 | 2026-09-22 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fb5b47c-da74-3a3d-88aa-f6e7cf0d2304 | -10.59945 | -53.97472 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a6477f8b-fbdd-39d0-8122-1b94f100268a | -10.61036 | -53.98129 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 7a1d02f6-3bf4-3e88-9fbc-955479e0eaf9 | -10.60718 | -53.98258 | 2026-09-22 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 60cabd6c-dfac-3c6d-bff5-141ec6834c87 | -18.51991 | -50.34169 | 2026-09-22 05:25:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 8a7c1462-dbc1-329c-b44f-3b37d0ebad9e | -10.4733 | -51.29594 | 2026-09-22 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README100.md)
