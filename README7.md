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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e10f00d-048f-3227-9d36-953d1bc75c62 | -7.49812 | -45.83875 | 2026-08-01 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 108d68c6-b595-396b-a0c8-752c6d85a6a8 | -9.90821 | -45.74874 | 2026-08-01 03:36:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 733b1967-9908-32ff-b5b5-8a64fbf4b090 | -10.65481 | -45.17949 | 2026-08-01 03:36:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00b9da10-e60b-3687-9dbe-8ad272aa075b | -11.9358 | -43.43886 | 2026-08-01 03:36:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b78c334a-e6d1-3e58-9780-c8716a0a8454 | -12.30061 | -43.72733 | 2026-08-01 03:36:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c079e397-8894-3fea-b5d7-a90a9a4f3938 | -12.60741 | -44.60928 | 2026-08-01 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fffd06cc-b918-3d4d-b580-0493a35e8b9f | -12.59891 | -44.62131 | 2026-08-01 03:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9e67caf-47ca-3046-9cbe-a647fe965274 | -7.50428 | -45.84644 | 2026-08-01 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 095243f4-24bb-35c8-aea5-0fa00c5192d9 | -7.64593 | -45.04672 | 2026-08-01 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c40c01a-853e-33ba-a9ec-700247a5b970 | -12.59803 | -44.62582 | 2026-08-01 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bc21424-4f43-3e2d-9ec2-4f2a3caa0c4f | -7.6458 | -45.0576 | 2026-08-01 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a397d1ee-10d0-34eb-ab71-75b523202707 | -7.54672 | -43.99126 | 2026-08-01 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77231d1d-994c-37f7-977e-66130ed27152 | -8.33874 | -45.98774 | 2026-08-01 03:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05ee3b5e-68ca-368b-a9da-d1038222a7a1 | -14.08224 | -46.25417 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| aaa78096-ef04-3276-ab77-e5ae18689012 | -14.08446 | -46.28419 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 74fecb67-e3c2-3eda-8874-9ca04545f685 | -14.08292 | -46.28253 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 425cfb04-b940-33db-8707-d51be330fab0 | -19.19462 | -49.62273 | 2026-08-01 03:38:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df6afbe5-16bf-3426-91ad-0bda07cbd584 | -14.34576 | -48.04179 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e41f95cd-a01d-357a-88ac-e0f49c175311 | -17.89418 | -44.30734 | 2026-08-01 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4a5b091-3af3-36c7-b491-21deb59a1003 | -18.50723 | -42.89503 | 2026-08-01 03:38:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 268e027f-2389-3a45-83fb-cdfbacf6dcc0 | -14.06719 | -46.2629 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5c7aa8fc-da02-3f66-ab4b-591dba3e2253 | -14.07632 | -46.26062 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1c5b61ba-417b-34ad-a5b8-240582d33923 | -14.07927 | -46.27755 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3a2042e2-b50d-3144-bb5c-939e585f4b39 | -14.07177 | -46.28157 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8b8016bd-1539-3020-b95e-0016b7688843 | -14.07694 | -46.24791 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 32776a5a-c2d2-3706-9172-14af11b924a4 | -17.89347 | -44.31076 | 2026-08-01 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b06e1d6-5891-3a0d-b021-c2228fc3f89f | -14.07701 | -46.28799 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5002581a-387d-37b3-9a21-4db61cf617fc | -14.06998 | -46.2593 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 18ed6cc0-94e2-361e-8967-1b6a2ce96993 | -15.0306 | -39.41736 | 2026-08-01 03:38:00 | NOAA-20 | JUSSARI | BAHIA | Brasil | 2918555 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c37587a1-2abd-3167-aa57-f25e59ae8327 | -14.08152 | -46.26715 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c73b6283-dd06-3b69-aaab-2614013fb189 | -14.06911 | -46.28526 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c161ab0c-a8fb-3631-a4a2-947eaba80918 | -15.44697 | -41.38501 | 2026-08-01 03:38:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 548fa63c-7633-3f06-8d3d-d4e5a9bf7a56 | -14.40839 | -48.04658 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 638509e3-afe3-3a0d-b67a-6951a1013eba | -17.05119 | -45.87858 | 2026-08-01 03:38:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a3beb1c9-f7af-3970-9cca-4a9e7e1e1e74 | -15.02392 | -47.05333 | 2026-08-01 03:38:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e1223c1-301e-37a4-bde3-110809107de3 | -14.33831 | -48.04255 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb682141-c67b-35e4-a661-9cc5c3d53c06 | -15.52181 | -42.65279 | 2026-08-01 03:38:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 24ce654d-0a49-3b96-af4b-2714771546f1 | -14.08132 | -46.23748 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4f37362b-ef58-32a9-b019-997d9750aa83 | -14.0713 | -46.2748 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| abd0cea2-e45c-3bef-afd9-7a45f0b2228b | -14.0729 | -46.27637 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2e0fb914-188a-3ff2-98ba-a9d66b6468bd | -14.06881 | -46.26471 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a2bbfd7e-8e7c-3109-9878-8d89fc18de39 | -14.0758 | -46.25336 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| e624e647-802c-39c1-a9e2-398dc0e8d5c0 | -14.07622 | -46.23053 | 2026-08-01 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16ab0940-8901-3cb1-a2b6-e7f73a1c86b5 | -14.08182 | -46.2878 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 37445e09-6f34-3564-812f-2918f203ce8b | -14.07239 | -46.26962 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fc8f27b6-5bad-3e29-8311-1a636090f033 | -14.33696 | -48.03963 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 541d9436-60ce-3929-a857-9691b046116e | -17.04705 | -45.03379 | 2026-08-01 03:38:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3eb708f6-9f62-34f7-a425-c1a6235faa01 | -14.08335 | -46.24884 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 59d728c6-e803-3540-9858-ec7d54c63d79 | -14.07986 | -46.26552 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c0d24210-2a25-34dc-a553-a9230553f658 | -17.05308 | -45.8698 | 2026-08-01 03:38:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 425fc98b-5e85-38bc-8bb1-960d9981a9e1 | -14.08217 | -46.29478 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0e2f7a1e-50ad-3f60-b6f0-2efccc35f0b8 | -14.07993 | -46.24393 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 08e17e1d-c12a-38cc-ae4c-8458ef7b3876 | -14.07814 | -46.28275 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 99142a82-c057-3951-bcaf-c56fa5d3f7fd | -17.8994 | -44.30857 | 2026-08-01 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcf02660-7c02-3c68-a39b-f54889b650d5 | -14.07304 | -46.23503 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf1057f1-97e8-3423-b314-d8fb133479ab | -15.64296 | -46.4406 | 2026-08-01 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c085ea4-a19c-3bff-80cf-cad039e7f255 | -16.04314 | -48.53085 | 2026-08-01 03:38:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b0a7a11-a549-3956-a053-867efe7d749a | -13.95312 | -47.83083 | 2026-08-01 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e28ffbc3-7950-354d-a9e6-0db0371de1e5 | -14.07063 | -46.28683 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9aaaced8-4a60-36fa-97ad-fccb94f05db2 | -14.07951 | -46.23562 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52a13db6-0811-321a-8772-6014e27e41df | -14.07181 | -46.24091 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 383e8767-a129-3397-98d8-eca679813eb2 | -14.08071 | -46.2931 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d8b8fd9b-6008-3ea3-a970-c01f1a9d351a | -14.07515 | -46.26598 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 11fe38c6-6823-37b1-9d3f-f5ad71f03107 | -14.35149 | -48.03994 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ab0557d6-3579-3550-ab09-a7d6a3d4ba79 | -14.06952 | -46.2518 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c6306ce2-5260-32f8-a38b-d64a0a9da7fe | -14.33958 | -48.03678 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b65fd710-9d06-32dc-9be3-e6d6534cabd1 | -14.3469 | -48.0366 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5158e5e6-8657-399f-9d08-9f6ba56dee0d | -14.07586 | -46.2933 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 93d4cdf2-efd2-3a71-8cb6-78f2b5ee425c | -15.44791 | -41.38012 | 2026-08-01 03:38:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| dd21bc46-7866-3d7c-ba7b-2e020e1024a0 | -14.4152 | -48.04874 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 523cd458-bb65-32dc-9390-d194dec8563c | -14.06604 | -46.26835 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3a78f827-3890-3f42-94fa-14740943909f | -14.08074 | -46.22978 | 2026-08-01 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0593cdb6-685b-3c89-9ffc-acea8a1fe852 | -14.0735 | -46.26434 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6e527522-77a9-3f95-abe7-007d915ca213 | -14.07021 | -46.28 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 94b4764e-dd76-3556-a2e0-1b0cb1dc1a14 | -17.05214 | -45.87418 | 2026-08-01 03:38:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 829a807d-10e1-33af-85a7-49e8866b4f76 | -14.08103 | -46.25996 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6d56c7a2-0a1f-3118-976c-7101675c81cb | -13.9559 | -47.82457 | 2026-08-01 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 938cf979-f02b-3aa1-ac6e-0986977fcd3e | -17.0479 | -45.02986 | 2026-08-01 03:38:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45aca860-5fab-3f48-b32d-cbd2680b025d | -14.33839 | -48.03332 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cdbcb90b-3235-32ce-824d-825c8ca513ef | -19.90996 | -42.24776 | 2026-08-01 03:38:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e547fb05-ffb6-3a4e-944c-012ca204c18a | -20.03013 | -40.2492 | 2026-08-01 03:38:00 | NOAA-20 | FUNDÃO | ESPÍRITO SANTO | Brasil | 3202207 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 051a6517-ac98-35a0-827d-34ad8968d889 | -14.07548 | -46.28643 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 55a7d08c-a9ff-3e9e-979f-6260412af6cf | -20.2677 | -44.52435 | 2026-08-01 03:38:00 | NOAA-20 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0d3770ea-cbfc-3a10-8d50-e546cbb0b3bb | -14.07118 | -46.2538 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6ce757f8-f720-3ec9-90d3-68c9507d2d6e | -14.07875 | -46.27084 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c9eca5b2-e9a2-32d6-ac28-a1595bede23b | -14.3296 | -48.03992 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 778277ef-bd3f-3570-939c-f3ae80410460 | -14.08331 | -46.28948 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 20ce54b2-1a60-3f4f-a577-dc40894c6c55 | -14.08105 | -46.29997 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d37665dd-87c2-3aa7-8b75-b12fb9333081 | -18.87017 | -41.98708 | 2026-08-01 03:38:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0d4a2ad5-87ad-3c2f-ad22-eded2965ef64 | -14.35263 | -48.0349 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d53d6283-691c-3a57-8399-d748c58bb491 | -14.068 | -46.29052 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 923e23a1-1211-32b9-a34a-9b1e49198d51 | -14.08768 | -46.23866 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8d6db232-435c-3122-950b-9baa9f3e0640 | -14.07751 | -46.2551 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| a05482d1-da75-3e3b-a752-7e3e47c14ad2 | -14.33223 | -48.03703 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32671e24-7039-3e24-b390-6cae4d3c1228 | -14.34184 | -48.05977 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 405861f8-473d-3234-ad41-89305cdf2632 | -14.34118 | -48.05328 | 2026-08-01 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c94532a-8ca8-38dd-a74e-45f1a72556d1 | -14.08259 | -46.23164 | 2026-08-01 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a57cc1dd-230a-39aa-b3eb-d0f387f11ac8 | -14.07437 | -46.29173 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 959b738f-fae8-3fef-956d-01c24983de07 | -14.07869 | -46.24965 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 653c802c-c09e-3253-843c-45ec54185b49 | -14.07326 | -46.29703 | 2026-08-01 03:38:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |


[Clique aqui para ver as próximas entradas](README8.md)
