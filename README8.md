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
| a40043ba-6a40-375c-8508-2eb9952a5d90 | -5.475 | -43.0774 | 2025-09-27 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 371.9 |
| 5a34f652-882e-3b5d-9069-812b6963b2d8 | -15.0267 | -47.1307 | 2025-09-27 01:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 303cf706-c975-37b0-8061-40fafc442181 | -22.5582 | -48.6038 | 2025-09-27 01:00:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 267.3 |
| f362fe72-e126-3c42-8e29-8770936fdf27 | -5.7961 | -42.8182 | 2025-09-27 01:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| bba23ec8-7536-3220-a483-73d324385adb | -10.2598 | -50.2624 | 2025-09-27 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 181c5ef4-c376-3941-af05-244f11071354 | -5.4562 | -43.0788 | 2025-09-27 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| a6a9f666-9bd8-3119-8bbe-22172fde9587 | -22.5575 | -48.6273 | 2025-09-27 01:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| cc1b6f1d-e617-3eab-9669-adf823b3c3ad | -10.222 | -50.2662 | 2025-09-27 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| c4dfed52-3c4e-3abc-8883-8163d3d8e95f | -10.2409 | -50.2643 | 2025-09-27 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| e2266c9a-5656-32a5-ac69-2b7478d37143 | -5.0676 | -44.8581 | 2025-09-27 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| af96becf-801d-3d3e-ad76-de463ac12cbd | -10.2412 | -50.2429 | 2025-09-27 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 025070eb-e842-30a9-96f4-dc22ce016e61 | -22.5575 | -48.6273 | 2025-09-27 01:10:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.0 |
| c8eacd65-4350-3044-bed2-5e1a22826678 | -22.5792 | -48.5986 | 2025-09-27 01:10:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 164.2 |
| 1a852ada-4275-305b-8334-bf33f48a9596 | -10.2409 | -50.2643 | 2025-09-27 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| fe887a54-ef24-3b78-aa0a-82deaf00544f | -14.8253 | -45.6282 | 2025-09-27 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b2e18057-7ac7-30c3-b600-75e2d026c896 | -6.8854 | -35.0666 | 2025-09-27 01:10:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 93.9 |
| 7d66e9c2-1849-3430-87d0-f27b67f6b3e1 | -5.5243 | -43.8647 | 2025-09-27 01:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| b1d5239f-290e-3d1e-b313-4222136075ff | -6.9236 | -35.0617 | 2025-09-27 01:10:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| a46eaacd-b99c-389f-a278-90a8e32ab95e | -5.5241 | -43.8878 | 2025-09-27 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 38fac343-744a-3b18-9e61-53e235aaa759 | -15.0457 | -47.1502 | 2025-09-27 01:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 75347209-937d-349e-a3f5-f59e21bfec34 | -5.5056 | -43.866 | 2025-09-27 01:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| f0bd81f4-0a1a-3c8d-ac63-a0600db93c33 | -5.7961 | -42.8182 | 2025-09-27 01:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 45d9fb25-b147-3e8a-b059-79ec43df779d | -18.39 | -51.7528 | 2025-09-27 01:10:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 8a57f3fc-dbaf-36a2-8385-c0315d09b21a | -22.5582 | -48.6038 | 2025-09-27 01:10:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 131.7 |
| e7ca4b8a-d815-3b13-ac8a-71083de15783 | -5.0862 | -44.857 | 2025-09-27 01:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 22686d0d-09f7-36ea-b5f3-190852ac6dcf | -5.0676 | -44.8581 | 2025-09-27 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c93f858f-43b7-3f32-ad8f-f469fac45e40 | -15.0267 | -47.1307 | 2025-09-27 01:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 637bbc6b-054d-36bd-940a-d87e0f4069a3 | -18.41 | -51.7494 | 2025-09-27 01:10:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 8ac4eaff-820d-3baa-900a-4eafc1a41ab8 | -22.5799 | -48.575 | 2025-09-27 01:10:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.2 |
| bd085317-284c-3a33-b635-83bd95d332f8 | -6.9042 | -35.0916 | 2025-09-27 01:10:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |
| def328dc-0d68-3e35-8417-0e34e70446f4 | -14.8448 | -45.6246 | 2025-09-27 01:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 2927df29-df62-32bc-b9d0-7b6ed555e0fb | -15.0462 | -47.1274 | 2025-09-27 01:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| f6f4a2a4-d9b9-3dc1-b052-12924f8f6534 | -10.222 | -50.2662 | 2025-09-27 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 127d1595-b255-3929-8c4a-d1409e03081a | -6.9045 | -35.0641 | 2025-09-27 01:10:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 202.9 |
| 41b1712e-3d2f-3ca0-a037-fa756c0abafc | -5.5243 | -43.8647 | 2025-09-27 01:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 238178f2-3cf8-346d-8949-41274d15519c | -12.2834 | -44.0332 | 2025-09-27 01:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 41701536-5013-3757-9c26-547c38cf25ea | -22.5792 | -48.5986 | 2025-09-27 01:20:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 191.2 |
| dd6024e5-ea22-38a9-b5b8-cf022a183ac2 | -6.8854 | -35.0666 | 2025-09-27 01:20:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 85.9 |
| 31d1c231-171e-3900-9bde-80788e62511f | -14.8454 | -45.6013 | 2025-09-27 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| adac0b00-af82-3468-88de-5d84709fac0c | -18.39 | -51.7528 | 2025-09-27 01:20:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 16ad6685-600d-33fa-bc33-3627c3fd9ddf | -10.2409 | -50.2643 | 2025-09-27 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 3082833b-1937-3894-a4b6-6730b881d869 | -5.5056 | -43.866 | 2025-09-27 01:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| c96c1ab7-ff6b-3a73-8582-254c21c6bc82 | -14.8448 | -45.6246 | 2025-09-27 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e0704d23-9e45-3c5f-adec-803fdcdf4cff | -5.4752 | -43.054 | 2025-09-27 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 607252e4-f3ad-3bc4-9734-b6b6824f9192 | -6.9042 | -35.0916 | 2025-09-27 01:20:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 112.1 |
| afeea495-21bd-3b7d-a3d5-398af7f3ab1a | -5.0676 | -44.8581 | 2025-09-27 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 982c2b03-f3c2-3df8-bd2a-e04cb419dbfb | -22.5799 | -48.575 | 2025-09-27 01:20:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.2 |
| a35e8c85-f267-31bf-a38c-94e077f83eb6 | -5.4562 | -43.0788 | 2025-09-27 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| a47cae98-6555-3457-887d-1fad1f3d80f8 | -5.475 | -43.0774 | 2025-09-27 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 6c58d8d1-51d1-3cd4-a5f7-ae987ed42fb6 | -10.2412 | -50.2429 | 2025-09-27 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 2f098201-4a4c-31f5-a4d3-f4ae2dfd3a2c | -5.5241 | -43.8878 | 2025-09-27 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 92df344c-4f86-356b-834b-1473798618a2 | -15.0462 | -47.1274 | 2025-09-27 01:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 47b5c904-8da7-3e0f-9b6d-d5fde01f6876 | -14.8253 | -45.6282 | 2025-09-27 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 79f00445-26a7-3318-84fc-db9b5c5df669 | -22.6009 | -48.5698 | 2025-09-27 01:20:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.0 |
| 6409d9c4-c721-3a37-a51a-ccd0f4301f6b | -5.0862 | -44.857 | 2025-09-27 01:20:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 05ffbce6-c76a-3105-916a-91383c831c52 | -22.5582 | -48.6038 | 2025-09-27 01:20:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 178.7 |
| 50e5c1bc-6261-307c-b54a-90dec7d5b94e | -5.7961 | -42.8182 | 2025-09-27 01:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 4223b130-5345-385f-9e9d-b461dfe6c75e | -12.2636 | -44.0599 | 2025-09-27 01:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 8d6e21b5-be04-3298-bfd1-84e0a8bccd7a | -5.4937 | -43.0761 | 2025-09-27 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| a70ddb68-8bcf-344a-9a9a-11ba65e99f87 | -18.41 | -51.7494 | 2025-09-27 01:20:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 31b16d19-7ed0-3ba6-a7f6-ea9198d959fd | -12.2829 | -44.0568 | 2025-09-27 01:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 197.3 |
| f4dcc1ab-95ca-3970-9032-254b0038e16e | -6.9045 | -35.0641 | 2025-09-27 01:20:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 159.8 |
| 0a6e7738-ea57-3d4d-a2e9-1c0522a47946 | -22.5575 | -48.6273 | 2025-09-27 01:20:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.4 |
| 8915d934-b2a4-3736-9f57-feacd737bafb | -5.5241 | -43.8878 | 2025-09-27 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 5143571d-3a13-3a6a-be7e-571a8aff1ed2 | -22.7271 | -51.3948 | 2025-09-27 01:30:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 120.0 |
| 9c84b0e4-d9ab-39ff-8045-361edff6590f | -5.4748 | -43.1009 | 2025-09-27 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 81a1c823-f8b9-3964-a49d-661e2ead9d58 | -5.5243 | -43.8647 | 2025-09-27 01:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| ffe52a46-fd6f-3467-b369-fef645ff8554 | -9.6159 | -47.5741 | 2025-09-27 01:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| f24238a1-7c36-3fdf-9a19-3f428d28ac8c | -18.3244 | -57.112 | 2025-09-27 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 35295768-cef8-3b31-a043-63c52796287f | -15.2756 | -46.4468 | 2025-09-27 01:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 1b498042-f245-3c92-9ef2-7eb8d50e3333 | -6.9045 | -35.0641 | 2025-09-27 01:30:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 101.2 |
| 73529450-2ce3-3955-8902-8504a6ef3cec | -5.0862 | -44.857 | 2025-09-27 01:30:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| e31718c2-6929-3a32-928e-8cc7176a1366 | -5.475 | -43.0774 | 2025-09-27 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 447.7 |
| a1ed03de-bebe-36dd-b803-e7c6a7eb58c5 | -18.41 | -51.7494 | 2025-09-27 01:30:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ef1cbb83-7d36-33be-a093-e401a702b76b | -18.39 | -51.7528 | 2025-09-27 01:30:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 5ebe5bc4-4a18-3ac2-9175-146e8e490e4b | -14.8448 | -45.6246 | 2025-09-27 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4514843e-160b-3574-92e9-b9d03512e46e | -5.0676 | -44.8581 | 2025-09-27 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 282c0caa-91a9-370c-9af6-ccb048960977 | -5.494 | -43.0526 | 2025-09-27 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 8e9de46a-d105-3879-9d61-72ba8c6c0011 | -10.2412 | -50.2429 | 2025-09-27 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a3c7e956-2f21-3d23-b146-6e96422a4639 | -5.4937 | -43.0761 | 2025-09-27 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 5dba53d5-bae7-3a19-b257-e81345138f64 | -5.4565 | -43.0554 | 2025-09-27 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 13bead43-49e7-3cb7-8c83-5fd54484f3b1 | -5.4752 | -43.054 | 2025-09-27 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 257.2 |
| a359a0cf-f08e-3e64-91f4-bbfe653f8ef3 | -7.1571 | -45.5158 | 2025-09-27 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 756b47ff-a297-3d4c-b6f2-4a6efdfa81fc | -5.7961 | -42.8182 | 2025-09-27 01:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| ce5d2d30-2d94-3336-bc2e-e410c02abd7a | -5.8149 | -42.8167 | 2025-09-27 01:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| ca048977-4616-3d96-8200-78bc12d87cd4 | -5.4562 | -43.0788 | 2025-09-27 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| bf824db5-0a34-3714-bc24-d43dc8c0b7ba | -5.5056 | -43.866 | 2025-09-27 01:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 763a0451-a611-326d-8705-66f917dde8b0 | -22.5799 | -48.575 | 2025-09-27 01:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.7 |
| 43b93c41-0e22-3d81-a182-dde8193b896e | -18.39 | -51.7528 | 2025-09-27 01:40:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 7aa36f1d-cc75-3509-a3ad-326f9b12a4e0 | -22.5785 | -48.6222 | 2025-09-27 01:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.4 |
| 62977bd3-6743-359f-808d-53f840bf4478 | -5.475 | -43.0774 | 2025-09-27 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 225.6 |
| d99fbe0a-f85c-3c52-bec6-398f03f72992 | -5.5056 | -43.866 | 2025-09-27 01:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| b1f10a91-fc1f-31b9-85c9-3eaf27e62915 | -22.7271 | -51.3948 | 2025-09-27 01:40:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| 5c0f8af2-283a-317f-91cf-9b1207c16784 | -5.0676 | -44.8581 | 2025-09-27 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| ed321157-a6f0-33a7-9932-fb1049afa40a | -9.0583 | -45.5085 | 2025-09-27 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| e9d43abc-16de-3a29-bd0d-426dd52e1af8 | -9.0587 | -45.4858 | 2025-09-27 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| b063d653-15ca-3f3a-b40b-e976495a2422 | -12.2636 | -44.0599 | 2025-09-27 01:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 22336a01-2a04-31ef-9135-49e94082822f | -22.6009 | -48.5698 | 2025-09-27 01:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.7 |
| 9f9768ba-3534-3c7f-a244-1a40b2e9ddb6 | -14.8253 | -45.6282 | 2025-09-27 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| cd428b62-7eed-3e2f-b081-532169a9cafc | -22.5792 | -48.5986 | 2025-09-27 01:40:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 190.9 |


[Clique aqui para ver as próximas entradas](README9.md)
