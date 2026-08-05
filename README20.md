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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be4b7dca-b9a7-3456-a87c-c0248dff4317 | -11.17534 | -54.91469 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0fe9126e-90d1-3111-b0a5-98c7fddc111d | -6.53858 | -55.15979 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e985f323-e7cc-3692-a5a6-5ba3eff6cac9 | -11.16853 | -54.90908 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 328cdb99-064a-3e29-b902-d99f2bcbed49 | -11.17662 | -54.90577 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb9252b3-9ce6-36d1-b2f3-dea1c304ad9f | -11.19283 | -54.899 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5dfc11f-6c13-3e49-95b7-451c739998d9 | -11.15528 | -50.38243 | 2026-08-05 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f472c51c-db43-3f6e-a806-e5dd7d4a6565 | -11.17081 | -54.88422 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4cc3a21-fded-381c-b024-6a6d1df9249c | -11.17352 | -54.90074 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| edef35bc-5064-3ab1-81dc-e00191075703 | -11.20192 | -54.83562 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03922bef-4c34-322d-bf71-8f44ebdb0328 | -9.49054 | -57.32604 | 2026-08-05 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e650b928-dab9-330f-ae06-5d4e331aa236 | -14.18588 | -54.40678 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96edab90-2f59-329c-81e1-9127a858a041 | -9.18452 | -58.06562 | 2026-08-05 05:23:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b1ae676-2973-36b3-8716-0263b1863f8e | -11.18336 | -54.87684 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85662dec-04b5-3b24-8b63-54ed1b55cfb8 | -9.28729 | -60.64818 | 2026-08-05 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f03e8ee0-dd2d-3996-8af7-f0f3b05485ed | -11.20273 | -54.90966 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| caacccc7-7324-3c30-b597-638c53423081 | -11.16708 | -54.88366 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 589c5034-5a72-32ef-b5c3-319c398b9bd7 | -11.20646 | -54.91021 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4152062-c134-3c97-af36-fc6c5181ad07 | -10.9155 | -50.42839 | 2026-08-05 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51600d7f-d239-3fb2-a05f-fc726e33512f | -11.17215 | -54.87521 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55982d7f-84e2-3719-affe-51960ccaacff | -6.71848 | -58.94559 | 2026-08-05 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f100e0e4-db70-354f-b52f-821bd59df288 | -11.17981 | -54.8834 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27f8f5e6-ad4f-349d-afd7-f1f086a12c30 | -11.17454 | -54.88477 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7128dd4-7f3a-3c08-8d2f-0c82e2e52cc5 | -6.57065 | -55.16079 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82800429-61b0-3d65-a798-fcbb46188670 | -6.54439 | -55.1686 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5de62d3c-675e-3148-9238-e591485f21b9 | -11.18268 | -54.88135 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a83b10d9-409c-345f-b2b3-95616be081c6 | -11.16575 | -54.89259 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cf5cdad2-731b-32df-9df6-3cfc018c7c56 | -14.18989 | -54.40729 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 570c5861-4387-3d7a-95e3-d48355f88837 | -9.28379 | -60.64759 | 2026-08-05 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc07c655-45de-39fb-abe8-36aa46b0a6f1 | -11.17843 | -54.91972 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a919af7a-8b47-3ee2-86c7-6c7fbd553cba | -6.55317 | -55.15808 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26d94ad9-3a90-3879-bb58-a51b6c839d30 | -11.18279 | -54.91582 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cf321a68-2bc8-321e-b5b7-de11efaeaea9 | -11.217 | -54.9163 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df1734d8-6738-3043-9111-068e5fa339d3 | -10.63628 | -47.48914 | 2026-08-05 05:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a8e6b94-e6be-339a-afbc-23fcbe85de42 | -6.57355 | -55.1652 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0844ed34-3596-35d8-be13-fcd5e7055de7 | -11.17894 | -54.88083 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01cf797a-df46-3e91-a8c2-8a583fab185c | -6.55146 | -55.14586 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d41306e-0559-3e90-a429-2cf020f15c56 | -14.19351 | -54.44033 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c35c6309-2ad2-3e41-aef4-b6b9e6472475 | -11.16789 | -54.91353 | 2026-08-05 05:23:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9b86f6d1-f788-377d-9fdb-01951262c862 | -14.18915 | -54.41265 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34ff63b1-b909-3345-86d3-03334928036e | -11.17598 | -54.91023 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 844b2f96-d7da-35b1-9868-c6727fefcb9e | -11.22923 | -54.85838 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22ba5ee5-806a-3a15-b184-e7b4993ad6aa | -4.05541 | -56.23136 | 2026-08-05 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74b48fa1-9b1c-3516-9c31-c000cc9d3528 | -6.56489 | -56.5218 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 896f134b-b221-36c1-9dd7-ec757e0b79a5 | -8.34808 | -45.9783 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 73dd3be8-c16f-3785-9d50-ad6e266071c3 | -17.45027 | -47.86639 | 2026-08-05 05:23:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a9451ab2-aee3-3b0a-bd7c-b7940ca18160 | -11.17917 | -54.88789 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23152a60-8571-3ce4-8785-51df20752ca8 | -14.18113 | -54.41175 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5338a51-4747-30ca-a8b0-e4c2c450cbe0 | -11.17225 | -54.90965 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cc66ff4b-474e-392c-9492-6ddd92ea8feb | -11.186 | -54.89344 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7e0bcdf-d572-3c10-ae4b-a25824eaa46f | -11.18174 | -54.86984 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e45083ba-a747-3c64-984a-208fbefe43e0 | -10.63686 | -47.48451 | 2026-08-05 05:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4f236e7-e2c0-3a2a-8c81-5a2403a3b7e1 | -11.18536 | -54.89792 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 796761d6-3644-3ecb-b224-90f6d0640612 | -11.18227 | -54.89289 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 598e7e0d-8e00-314d-9b9a-adbddccd7339 | -11.18974 | -54.89398 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 287a1f64-ff57-31dd-899a-beb1509f8b3e | -11.19102 | -54.88499 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 711fc8ea-b3e8-385e-8350-1bd878b436f5 | -6.95983 | -52.81908 | 2026-08-05 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31811016-1c00-3f92-ba85-6b889503ca91 | -11.1993 | -54.85387 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 380923bd-e652-3232-80dc-bdf12e071864 | -11.19996 | -54.84932 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9a5e02e-1aef-372c-83da-d43a2558d80a | -14.17386 | -54.4053 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c9d866d-a1c5-3626-847a-84ff9a42eb7c | -11.19038 | -54.88949 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c79de7c5-6fdc-36b4-89ee-2bf56bac3594 | -6.54557 | -55.1609 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ad1b4c6-28c6-3b31-9776-23532b361279 | -6.71116 | -58.94809 | 2026-08-05 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4958777e-26f8-32b4-90fa-1a6d0a610056 | -11.20208 | -54.91412 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c7c9da1-9f14-3f72-956c-0473cb1e8a8c | -6.53977 | -55.15201 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c871733-4d09-3668-9396-7e7c535f046a | -11.19785 | -54.89056 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee36463a-ba39-3fe2-8083-7ed922d12a2d | -17.9845 | -47.1575 | 2026-08-05 05:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 501e8f58-e645-3b3d-8035-ca30dda7d551 | -11.20566 | -54.8362 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff4feaab-1fac-30d0-887f-b1e4863d7ecb | -6.56195 | -55.14755 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afe5f8f9-6adf-3b58-b5c0-bda776ed82cd | -11.17962 | -54.87632 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d2fe804-f871-3e82-9229-f5b8b5fd17f1 | -14.19751 | -54.44082 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44657ccc-711d-360b-adfe-03c08af546ef | -11.10886 | -50.4269 | 2026-08-05 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d495b80-cb35-3f8a-a590-87b1cea08961 | -6.41997 | -55.79409 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0c5b933-379f-317c-ab53-ddff560cc292 | -9.6126 | -47.76954 | 2026-08-05 05:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43c66a37-884f-34aa-b97d-17573f091c71 | -6.55845 | -55.14698 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd20c0f9-7337-3763-a363-fa58d75e65e3 | -4.05286 | -56.23106 | 2026-08-05 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b718fa1-d43f-3148-bd24-6da9601e3959 | -8.49018 | -46.85909 | 2026-08-05 05:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25ff9da4-cbca-3f7e-9df2-8f2c33533d06 | -6.5345 | -55.16309 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bb0d754-1163-329a-84da-e5d6942cb8cd | -11.17014 | -54.88871 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1e84151-d8ad-34d4-8855-f1b6dd0ada15 | -6.55257 | -55.16197 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ac8d258-9947-38f3-8c8d-c23d180b3173 | -11.17362 | -54.87327 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f89b4779-7760-3a31-b721-217dd99a09d1 | -11.22482 | -54.86238 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e32c6c4-17f2-3dcb-a29e-c175c371a273 | -6.72243 | -58.94255 | 2026-08-05 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e359a1d-8855-371c-9176-c8be0f593697 | -6.64543 | -43.90785 | 2026-08-05 05:23:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36a646ec-1010-3470-958b-3fcb7b97782d | -10.60874 | -46.38116 | 2026-08-05 05:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fae26831-dec1-35c9-a4ed-191439593cf0 | -14.16256 | -54.3984 | 2026-08-05 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c18ca071-d5e1-310c-af0b-7da54700af0c | -11.16916 | -54.90464 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 54c22056-5ada-3cc5-aceb-0dffe7398b0a | -6.54788 | -55.16914 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93c9cc81-56dc-3cd2-a538-8356afdee661 | -11.21457 | -54.90681 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dd022eda-2932-3712-8026-1e1dca34efe0 | -10.852 | -50.33706 | 2026-08-05 05:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c998dee-8017-30c4-96d1-170c9c500848 | -11.21831 | -54.90732 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 63b40c65-2302-3931-b12a-d2c4abfe5904 | -8.3521 | -45.98886 | 2026-08-05 05:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 16da44c1-0f5c-3e25-b6a1-6663e51357b9 | -11.21019 | -54.91076 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b10923d9-9dc6-3405-8da8-425d536bcc7f | -11.17736 | -54.91709 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d3bb5c57-72ab-373e-8a14-c245f4deb720 | -6.33553 | -55.73263 | 2026-08-05 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45813ec6-ed90-3b74-ad2b-ad5c8678fea4 | -11.16163 | -54.86892 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 892388ba-3655-3db5-99c3-bfc66125f56d | -6.53799 | -55.16366 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 393390e2-fa67-32d9-aaa6-636dfbbc6108 | -11.17289 | -54.9052 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 76590d51-ec95-3794-b261-29b6df6aa437 | -6.54267 | -55.15646 | 2026-08-05 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99684056-c3f9-39c2-9747-5721ba8a5c2a | -6.10315 | -55.81353 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af84fe05-d9c4-3581-893d-6cd2b3915cb8 | -11.1811 | -54.87438 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README21.md)
