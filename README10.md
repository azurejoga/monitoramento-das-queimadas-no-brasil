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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85c8d053-3c85-342a-af2f-fab27fca3b77 | -21.57286 | -47.78654 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 583ff9cc-92a1-3a4d-8a51-14cf93179c51 | -21.57155 | -47.77702 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 3a9dae02-f15e-31ae-863e-060c184a1a73 | -21.57023 | -47.7675 | 2024-09-29 01:02:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 89422222-6b1b-3c21-b421-dd87fd90d2e9 | -21.55048 | -45.76542 | 2024-09-29 01:02:00 | TERRA_M-M | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| b5c99985-06ee-3445-98fb-8cd6772b829f | -21.54896 | -45.75527 | 2024-09-29 01:02:00 | TERRA_M-M | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 18d7495e-d91c-347e-97d7-5be74e36cf86 | -21.51171 | -49.84774 | 2024-09-29 01:02:00 | TERRA_M-M | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 43dd743c-297b-3c3f-89e8-e8c27ed04efb | -21.32221 | -49.42263 | 2024-09-29 01:02:00 | TERRA_M-M | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 2be51c88-15b4-36f1-ac2f-05dd3327c911 | -21.13658 | -47.03193 | 2024-09-29 01:02:00 | TERRA_M-M | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 8721f6d9-465f-3417-a9f2-ddf8e532c2a1 | -21.1277 | -47.03343 | 2024-09-29 01:02:00 | TERRA_M-M | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 64be801b-bf01-3451-8078-843d3edfa74f | -20.99861 | -46.46238 | 2024-09-29 01:02:00 | TERRA_M-M | BOM JESUS DA PENHA | MINAS GERAIS | Brasil | 3107604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c3c2753f-9444-3456-84cb-c56227cbc110 | -11.06 | -52.5 | 2024-09-29 01:04:22 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15e154a2-d995-31c2-8177-c28ac00c77ee | -12.85483 | -51.14315 | 2024-09-29 01:05:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1acbd763-3024-3e3c-9efa-d4bc4efd38fd | -12.80902 | -53.99413 | 2024-09-29 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 73dfbb64-1c3f-35b5-ac74-632be4cf6e14 | -12.79974 | -54.00993 | 2024-09-29 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| ad152479-2af5-320e-a89b-962ccb31a26b | -12.79797 | -53.99558 | 2024-09-29 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| eacae010-4c53-3e74-a81a-31f1f773eaf8 | -12.78867 | -54.0113 | 2024-09-29 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.4 |
| b0cb6b9c-4284-3301-8134-07c81c986b04 | -12.78692 | -53.99696 | 2024-09-29 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 209.1 |
| 8c50c66a-a4c2-338d-b5bf-3436cbb7f41f | -12.77936 | -54.02723 | 2024-09-29 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5c90ddbb-a8e3-3279-a229-3fa679e7b96f | -12.77761 | -54.0127 | 2024-09-29 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.5 |
| ba4da308-ee71-36d9-97cb-3cb9432395eb | -12.77586 | -53.99832 | 2024-09-29 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 0ab9043b-3846-366f-bde4-819bc2970f0a | -12.76829 | -54.02866 | 2024-09-29 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 95e63648-42fd-3463-a3e3-d015f27f3851 | -12.76655 | -54.01415 | 2024-09-29 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| ef3c4315-fdaf-3aa9-9141-206493715e32 | -12.76564 | -54.02 | 2024-09-29 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8acaa049-6852-3932-a32f-dcf55135a8d6 | -12.74685 | -48.4862 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9cd420ad-59f7-3d20-964a-2944d33333a0 | -12.74556 | -48.47713 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6562b269-d3fe-3a14-80de-83d22d020ea6 | -12.71932 | -54.10026 | 2024-09-29 01:05:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 63602047-0d9a-310f-b2e8-f857262f7869 | -12.56645 | -53.51781 | 2024-09-29 01:05:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 957e0c83-42ee-3092-80db-85375673d4ba | -12.5648 | -53.50468 | 2024-09-29 01:05:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 184.5 |
| 43cb400b-2baa-332b-84d5-51cac032287b | -12.56312 | -53.49139 | 2024-09-29 01:05:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ca4d7afd-37f5-3a34-a7e9-47a87611e384 | -12.54888 | -50.6387 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 022d35ed-aaa8-326d-a72c-60cd9398ad1e | -12.53083 | -50.64128 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| d1c93451-7a98-3fcf-aacc-ec36d5002546 | -12.52957 | -50.6319 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| effd73f7-f3ed-30a9-962e-4fb9aa9ae7fa | -12.4981 | -48.61736 | 2024-09-29 01:05:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 12f5baef-f254-397c-b8c6-edaacd337599 | -12.4968 | -48.60819 | 2024-09-29 01:05:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f2f48647-5501-3abf-8539-58fd8bf09635 | -11.79229 | -47.6161 | 2024-09-29 01:05:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e9167ab2-65dd-3f3f-9025-42585f412ea9 | -11.73355 | -57.45951 | 2024-09-29 01:05:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| ca208e77-c50b-3b68-a468-368a1aac97fb | -11.73065 | -57.43386 | 2024-09-29 01:05:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 64a1e893-90a1-3ce3-8c52-e07aef1db134 | -11.72758 | -57.43927 | 2024-09-29 01:05:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 671064a0-cac0-3721-b9ed-c33164d5ced1 | -11.69922 | -46.35602 | 2024-09-29 01:05:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 05a9be7c-75b0-3218-b0b5-103e31736eb7 | -11.69398 | -49.96972 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 86ba34b0-f1c0-373c-81a8-111b9ba154ee | -11.5783 | -48.4335 | 2024-09-29 01:05:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7bdf90c7-1048-3a9d-8a07-946e90db6739 | -11.08798 | -52.49517 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b2558a81-b829-3707-8dc4-80c6eff978a8 | -11.07828 | -52.49643 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1a3dd2c3-a515-35be-a1cf-539995485d14 | -11.07684 | -52.48555 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 162.2 |
| c37583aa-c370-308f-8ad0-e706ba1b9cc3 | -11.07541 | -52.47474 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 2d3531f3-2bb3-3211-9c50-dab43fe15ffe | -11.06715 | -52.48686 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 379.6 |
| 74dd875d-6ba3-313a-aefa-ae05c1ef360d | -11.06572 | -52.476 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 57fd1564-87d6-3bad-a086-3a9413ec454d | -10.93963 | -50.11568 | 2024-09-29 01:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 77b05741-e203-3566-a2e0-993fa684e8f2 | -10.93838 | -50.10669 | 2024-09-29 01:05:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 526b2687-f7c9-34eb-a26f-67a8b5910607 | -10.78959 | -46.57339 | 2024-09-29 01:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b9eb584f-496c-37c4-a576-5bcdcde81a77 | -10.78789 | -46.56198 | 2024-09-29 01:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1407f42c-113c-3bcf-9d70-12d4ffebbdfc | -10.78613 | -46.55024 | 2024-09-29 01:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c1770a34-acf7-33f4-a134-ef851425623b | -10.74694 | -48.74381 | 2024-09-29 01:05:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 528eac44-6f3f-3e84-b862-072bc6c782b6 | -10.73796 | -48.74507 | 2024-09-29 01:05:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8a43dee0-6898-31d0-9cf6-b8489540bd55 | -10.72898 | -48.74636 | 2024-09-29 01:05:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 93cb91c4-77d2-3313-be8c-ce6b2760351c | -10.71998 | -48.74757 | 2024-09-29 01:05:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1d92be5e-467a-365a-81da-34941bf4c936 | -10.54658 | -48.0549 | 2024-09-29 01:05:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b0cf629a-6042-3531-814f-b89c5915e713 | -10.53602 | -48.04699 | 2024-09-29 01:05:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8ac29714-168a-3fc3-8c0e-b6a67d69e4d2 | -10.53574 | -49.46162 | 2024-09-29 01:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3c08634d-843c-33e6-b0c6-18125a03cc95 | -10.5346 | -48.0372 | 2024-09-29 01:05:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e205fd1b-3757-3780-baff-0656c8623cb0 | -10.53447 | -49.45263 | 2024-09-29 01:05:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8fffff31-66e3-359a-a965-d1874559a065 | -10.53184 | -46.08516 | 2024-09-29 01:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4bcf2cef-75ff-3b33-8a30-2a2b8b8ab372 | -10.52995 | -46.07261 | 2024-09-29 01:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 8b15d50b-a432-33c9-8315-8ca97687819a | -10.51958 | -46.07417 | 2024-09-29 01:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 4f3d40b9-e047-31b4-b678-d402f0398d5d | -10.51768 | -46.06172 | 2024-09-29 01:05:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 37f1f6fe-8f86-33b7-a084-d1026cc41fef | -10.4269 | -48.1883 | 2024-09-29 01:05:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cba94855-43b2-3275-a7a6-a5c194ea4b6c | -13.4579 | -48.3665 | 2024-09-29 01:05:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3f3509cd-61c2-3e9e-8d4f-8884031b17c6 | -13.45658 | -48.35728 | 2024-09-29 01:05:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dec3f901-950c-3a3f-bd9e-b9a9fda02758 | -17.7171 | -53.16635 | 2024-09-29 01:05:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 41.4 |
| eeb51913-d02b-3511-86e7-edae811eced5 | -15.64383 | -47.22907 | 2024-09-29 01:05:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 399198ac-de84-3b33-8f8c-4391d3ee6dbd | -9.95529 | -44.03285 | 2024-09-29 01:05:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 81167096-e985-34c7-8d1b-e2f283722eec | -9.95244 | -44.04004 | 2024-09-29 01:05:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7c3adcf4-34dd-3044-9e65-fdbb88dd6572 | -9.94019 | -44.04214 | 2024-09-29 01:05:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 670393d6-36d8-36d9-a7eb-4cd814129837 | -9.03401 | -40.5765 | 2024-09-29 01:05:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 5c018d14-27e7-3479-9e81-2d26913068b7 | -19.07146 | -50.87355 | 2024-09-29 01:05:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| adae5d2d-a5b4-371b-adaa-7c6783c235a7 | -19.05253 | -42.96156 | 2024-09-29 01:05:00 | TERRA_M-M | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| 2687c88c-7eed-3dd5-a4b5-49769d796d6c | -18.94287 | -42.10539 | 2024-09-29 01:05:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 01868012-3590-3fec-9dc6-e17f3c9ed34e | -18.93978 | -42.08731 | 2024-09-29 01:05:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| cf15533d-9be5-3f87-8c2c-1c6e73e64056 | -18.86927 | -49.14499 | 2024-09-29 01:05:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 6ee6ded2-7530-3a08-8e97-f0cc9b76074a | -18.86798 | -49.13537 | 2024-09-29 01:05:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 6256a26d-7ebf-39e8-b79a-4c149feb5e3a | -18.86026 | -49.14629 | 2024-09-29 01:05:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 33.0 |
| d78c2c06-a56f-3d30-8d34-60e74a3ae403 | -18.85898 | -49.13669 | 2024-09-29 01:05:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 28.8 |
| bac2a80a-96dc-37c9-bc0e-592c327fd7c7 | -18.80495 | -41.9135 | 2024-09-29 01:05:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 1268bc9f-1485-3dbd-858b-6591fc948820 | -18.79282 | -41.91609 | 2024-09-29 01:05:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 604a5a18-113e-3c76-bfc6-a2a18054a429 | -18.78391 | -41.93706 | 2024-09-29 01:05:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 1c87c610-5563-37a0-8831-5c5bf17db7f8 | -18.50986 | -42.23795 | 2024-09-29 01:05:00 | TERRA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 324cdc95-e0ed-36de-8950-071e4eeb05bb | -18.50198 | -42.22726 | 2024-09-29 01:05:00 | TERRA_M-M | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 1932f042-74e5-393d-91cb-8729f4abca30 | -18.35104 | -42.77844 | 2024-09-29 01:05:00 | TERRA_M-M | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| f7d94759-98e9-3e07-862c-6486e189add8 | -18.34821 | -42.76199 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 001e7bf9-57ae-3aef-8b96-0c0adba6ef52 | -18.29486 | -42.16813 | 2024-09-29 01:05:00 | TERRA_M-M | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 21eef91a-b85b-363d-8ecc-2a9680b9e736 | -18.10685 | -42.69128 | 2024-09-29 01:05:00 | TERRA_M-M | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 1fe5225b-0338-35a3-9f92-396c639363fa | -18.08882 | -43.96508 | 2024-09-29 01:05:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7ebd228c-0abf-313b-83a5-bc31ca37cee0 | -18.05645 | -44.39722 | 2024-09-29 01:05:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 29.6 |
| e2396179-dfd3-3561-95bd-0378e8df3b3e | -18.04782 | -44.3913 | 2024-09-29 01:05:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ebecf74d-8833-3d14-a5e0-cdfb6206d1e3 | -17.80227 | -44.473 | 2024-09-29 01:05:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 32699a7e-80d6-309b-9be7-9e3407e49ed9 | -17.7745 | -43.32898 | 2024-09-29 01:05:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5dcf0315-62d8-33d4-9409-f9c1966c566a | -17.76339 | -43.33129 | 2024-09-29 01:05:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 89bb994e-a2e0-3e3a-86e9-2dbc5fda5251 | -17.76089 | -43.31604 | 2024-09-29 01:05:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 292a5d82-e8c8-3f38-9fa3-c06ccc3aec44 | -17.71532 | -53.15086 | 2024-09-29 01:05:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 42.4 |
| cbb3463b-51d7-35f9-a04f-f8ae3859ae78 | -17.6653 | -53.11808 | 2024-09-29 01:05:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README11.md)
