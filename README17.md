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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daa2c20d-7f03-3b8b-a249-84e0687e03ac | -10.76316 | -45.95374 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49a5836f-4db3-3d89-b128-a0fc4d15392e | -7.26317 | -45.35316 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a5c7e0ac-3141-3ce2-aa3c-ad346d25ff27 | -7.19201 | -43.60912 | 2026-09-10 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2659587d-f8b2-38e7-bdfa-b79308735d8f | -10.73389 | -45.91209 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b201d550-1bb0-373d-846f-4eb8616806f1 | -7.99517 | -43.97045 | 2026-09-10 04:08:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b25f1bc-07cc-37fc-a16b-7ec7d3b4e4b3 | -7.98317 | -43.97529 | 2026-09-10 04:08:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22ae387b-8880-364f-8a87-8a551504672d | -9.71574 | -43.3964 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0523ae66-19fa-357f-9c14-2f473fab1cf4 | -7.97853 | -43.99339 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 643c52d4-ebb1-3e38-bd77-c9837387fb2d | -9.68246 | -43.44283 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3ad3c58d-1188-39d7-9d88-bcc9eaa64251 | -9.3354 | -45.64301 | 2026-09-10 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61d09d5d-1fc5-3ef9-aba6-66aaa2a2f67b | -8.97504 | -44.40133 | 2026-09-10 04:08:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd0dc4f9-ddd9-304c-bfa2-98b7afa34200 | -11.33323 | -45.78655 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f53c59a6-a5e7-3e1f-9148-d3974365c55e | -10.25416 | -45.25982 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70beeb18-0592-34eb-ac0b-21cda0752c44 | -9.33908 | -45.64817 | 2026-09-10 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc4674b4-bf93-3e31-88ac-c1e6da00d444 | -12.83435 | -44.33606 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 60130817-77f2-3345-8785-20519aa6e78c | -7.5067 | -45.27446 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c521b13-9539-3517-89bc-e9595107f739 | -13.363 | -41.33624 | 2026-09-10 04:08:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b72f9258-48fd-316d-a70a-88aa8cfe2168 | -12.37188 | -39.5877 | 2026-09-10 04:08:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2abd8c05-db97-35b9-8f38-d698fa4327e3 | -9.69548 | -43.46722 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8ae68dd6-7061-3283-af52-3c79fd1a3941 | -12.84985 | -44.33888 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2b7bde53-9a8a-3870-ba34-afef6c91289d | -12.82485 | -44.34456 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 3236cbbd-8181-36f6-931c-078d727b0177 | -8.23958 | -44.7561 | 2026-09-10 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9896455-ef7d-3c2c-ac5a-326101ced969 | -12.85072 | -44.33394 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 81c5357f-8b32-3820-af1d-a483c9e6af54 | -12.82873 | -44.34528 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| bf193341-4e43-36f7-a164-a20245db8c51 | -10.82678 | -49.45064 | 2026-09-10 04:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d2b040cd-73a1-3c71-9551-b1aadc86d8d3 | -8.74937 | -47.4851 | 2026-09-10 04:08:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6e14e38-6fbc-3568-8df2-c7b80420c0e6 | -10.23148 | -45.31401 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb900057-4fb4-3a52-b9fe-189d891d773b | -7.99176 | -43.96585 | 2026-09-10 04:08:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d31ea471-6b76-3098-8bc6-ac564881ddce | -7.9845 | -43.98333 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c89fc15-876b-3881-aeab-4fbe4f80a909 | -9.32529 | -45.63462 | 2026-09-10 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f6ccfec-3236-3360-8dfe-e7ff6c98a15e | -10.6656 | -46.06017 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af4167c9-8e1a-38df-92e1-ebe587d614cb | -9.69544 | -43.45995 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 544dbc30-ef5f-3974-96dd-ceec37b00126 | -6.49699 | -47.59401 | 2026-09-10 04:08:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 370e3548-a64e-328d-9ed0-0b7bf46dc507 | -7.48354 | -45.27456 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e285a70-e94a-3584-934f-e79ec0374a69 | -9.68675 | -48.37191 | 2026-09-10 04:08:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a768b26-56f2-3cc9-9881-54fb48ca0290 | -12.84898 | -44.34383 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 86313d2a-fb2b-3e77-9a7a-5aa14a999d00 | -10.23771 | -45.22747 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0ff4688-5f64-3319-a9a7-829ff0015b06 | -9.69462 | -43.4649 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0a41de6d-4d9e-3255-bf68-cf409351978e | -12.85459 | -44.33466 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 8c6ffc4a-d2b0-3758-a4e7-f126b603b22a | -9.71279 | -43.40363 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 94b3589f-5419-384b-aae3-139aceccda74 | -9.68977 | -48.37267 | 2026-09-10 04:08:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dea7a011-1f05-39dd-8cff-f66093ffd5c1 | -7.50829 | -45.26521 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a836de7-b5fa-37c8-9d84-cac059c81091 | -9.68201 | -43.49262 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c1a6ccb-4260-387e-9938-1ff9c2315c11 | -9.72042 | -43.39225 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| da9698a5-c195-3f1e-98fd-0fd06fe020da | -9.68327 | -43.438 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd814d13-9e19-306e-a71b-95ef50fdcd06 | -7.08354 | -44.36094 | 2026-09-10 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f55d1b7c-c5e6-38e0-b882-7a31fa1e39ce | -10.23611 | -45.18624 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 986646ef-42c5-38ff-8fa0-0d309e6f3dd5 | -8.4616 | -41.25332 | 2026-09-10 04:08:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cac7bfed-1fc0-366d-aaad-01f67653b6fc | -7.74662 | -49.20055 | 2026-09-10 04:08:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ebaa1864-dadb-349d-ac3c-a948cc60905e | -8.2553 | -42.89538 | 2026-09-10 04:08:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8e92d20c-d442-36db-a793-ac48c6e13371 | -9.30164 | -44.36196 | 2026-09-10 04:08:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 569a5fdd-08c2-3c9c-b0e8-17e1b4b70aa2 | -14.49343 | -43.81401 | 2026-09-10 04:08:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 2570dc5a-a47e-36f9-aa21-43a90ba5707d | -14.48899 | -43.81778 | 2026-09-10 04:08:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 6250f8c0-e39c-3f6d-90f5-2536851640f0 | -12.84123 | -44.34241 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a505e06c-f1ae-3e93-aa66-c2123404f442 | -9.68831 | -43.47878 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f55880ef-1baa-3f41-9a9e-76434a0b7270 | -9.76481 | -43.40993 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2663662-6cff-36ee-9fad-256a98b9cf54 | -9.5435 | -45.68896 | 2026-09-10 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e9dd187-b4de-32cf-b267-61771b014494 | -9.53506 | -45.46074 | 2026-09-10 04:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa183e83-0e2d-3742-bee3-cb8c9cac6edd | -12.783 | -44.81128 | 2026-09-10 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07267a3d-e659-3575-90f3-dd2ee211f25d | -10.76536 | -45.95679 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca5562b2-f9e5-36bf-857e-9e2ec1b88aa7 | -6.49455 | -47.59404 | 2026-09-10 04:08:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0ec787b-f030-37ec-9610-9a8f202720ca | -9.77443 | -43.44641 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1597cc79-78ec-39b0-89d5-ceb071427f5c | -9.66227 | -40.6285 | 2026-09-10 04:08:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2b419f36-c64a-3e47-bc85-9313f3f8d791 | -8.98041 | -44.99881 | 2026-09-10 04:08:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e615b33-6537-3f1c-a29e-068f23c3e1fb | -12.8266 | -44.33466 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| fc1a4489-ce81-3ab0-9540-c036229a3b1e | -8.24099 | -44.74795 | 2026-09-10 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b60d986b-d74a-3194-9301-dff0cabc2687 | -12.84511 | -44.34312 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 472e9c14-0cb2-3ebc-ae96-41442b68610e | -7.18735 | -43.61203 | 2026-09-10 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cebab9c-300a-38cd-8e43-00eb089a6a19 | -9.72124 | -43.38751 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| dffd0138-2f8a-3516-a726-d653eed012a4 | -11.43643 | -45.15124 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 010ef0fd-f356-3c1c-aa23-1f85517c8818 | -9.68793 | -43.43386 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 053e2cf3-bcd2-3832-b125-25d2dee96032 | -10.25674 | -45.23405 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1edd3a64-f912-3678-9ad8-d31f0d6d0d31 | -9.68364 | -43.48293 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7d85009e-18ab-3c47-a159-1c2701b2a7ec | -8.32205 | -45.11055 | 2026-09-10 04:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e74fc3a6-8066-3a5a-92d6-ff19c87d33a6 | -9.7805 | -43.45736 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cffcae8e-e922-3e4f-adc4-fa331a5275e5 | -7.19667 | -43.60622 | 2026-09-10 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63b1f030-8d74-3e51-a6ad-820860894b24 | -13.44122 | -43.83407 | 2026-09-10 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| ee6c1944-dcf3-3b86-ae6b-39794c7ca6c5 | -8.82349 | -46.92846 | 2026-09-10 04:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1dfd7bec-f454-3df1-a585-14a52a1cbe30 | -11.21534 | -49.94416 | 2026-09-10 04:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ef30234-e57e-34ff-ab72-aaa914fcab72 | -9.70046 | -43.40645 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b4bb3ec1-b144-3882-b65b-2d451e0af65a | -8.69132 | -47.9821 | 2026-09-10 04:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01449436-e580-3aa0-ad7e-7b86cada4832 | -12.84036 | -44.34736 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 0eed1940-4bb2-32f7-a8ef-f0ee2ef2d837 | -10.27602 | -45.22498 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8302c51c-910d-3ffa-a38c-be89c2002979 | -11.85206 | -44.86797 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68456161-c36c-3fb8-b1f4-6428d0791d06 | -11.85614 | -44.86859 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a0e26d8-61bc-3408-a7e9-2ad12920a8c6 | -10.06937 | -45.47122 | 2026-09-10 04:08:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0af63f0b-4b62-3ff1-b910-5e4e16ccacf0 | -10.26388 | -45.20361 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd78485c-0b09-3af3-86df-67566bf25864 | -7.99081 | -43.94723 | 2026-09-10 04:08:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60ec6f1e-3c01-39a5-9016-c4d4fd450124 | -13.53669 | -43.30915 | 2026-09-10 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 874e8b58-5086-3cad-8a14-444f00957bf4 | -10.75286 | -45.93418 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2054e430-26b2-37ef-bd87-a900a014eb23 | -7.50985 | -45.25617 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40664392-9f4b-3663-8930-76a81f73b73f | -10.25665 | -45.25904 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d8872f3-8546-3b07-aa9b-e9e4587547da | -11.32889 | -45.78567 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f432b011-2913-3691-840b-079087647b72 | -7.98324 | -43.99058 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23b3dae1-5f9a-3c6b-9d19-353df7838986 | -11.32963 | -45.78147 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 10afc1ba-a4c5-3d5d-889d-f9a19c501c17 | -11.33558 | -45.7479 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc820873-1456-3eac-a28a-4cc25d2b840e | -10.07966 | -46.23456 | 2026-09-10 04:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1ded57b-bd4a-3be8-a394-867c984a1b2b | -7.51274 | -45.26627 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae650256-c3a2-3abb-8678-eebd9bef1718 | -9.68387 | -43.45802 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ef66bf7f-810b-3b65-8602-ec8f2bb0f2ed | -13.53743 | -43.30487 | 2026-09-10 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README18.md)
