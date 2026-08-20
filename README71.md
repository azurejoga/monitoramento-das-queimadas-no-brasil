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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aebb0e9c-0998-3b4b-a62a-79f94774c277 | -18.0311 | -44.61819 | 2026-08-20 11:36:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 363b9f11-1564-32e4-879c-25d9468d6ca0 | -14.44826 | -45.62225 | 2026-08-20 11:36:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 717a92d6-8b2c-3b55-ac9a-7310db2417f1 | -17.21289 | -47.71494 | 2026-08-20 11:36:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4ae0c40e-f21c-3011-a050-d11bf11de8d5 | -12.85377 | -48.42793 | 2026-08-20 11:36:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 3e111c04-4749-30f6-9b3c-569b1d927c69 | -21.87842 | -46.56513 | 2026-08-20 11:38:00 | TERRA_M-M | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 1491999e-3073-3f53-8e9b-878fc2e48c1f | -21.63835 | -46.3715 | 2026-08-20 11:38:00 | TERRA_M-M | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| f31ed8ed-e214-3c53-9900-f4758a9b7ab1 | -21.29516 | -45.09279 | 2026-08-20 11:38:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 435d63ba-e28f-3c9c-ae7c-c019e56a2cf2 | -21.8771 | -46.57467 | 2026-08-20 11:38:00 | TERRA_M-M | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 75fe41af-fab2-34fd-85b6-781ac253975e | -21.2938 | -45.1032 | 2026-08-20 11:38:00 | TERRA_M-M | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| cda7703e-6937-380c-bd64-a62e051c6ec7 | -22.77725 | -47.5139 | 2026-08-20 11:38:00 | TERRA_M-M | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 7a11b762-4228-3364-8885-eca65c57f39e | -22.77589 | -47.52344 | 2026-08-20 11:38:00 | TERRA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 01c008ce-cac3-348c-8f56-f25f6b7cb4a1 | -20.60809 | -44.94427 | 2026-08-20 11:38:00 | TERRA_M-M | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0f42e8a2-aff4-374b-baa6-4055da4d8821 | -21.64513 | -46.05635 | 2026-08-20 11:38:00 | TERRA_M-M | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| f15a0e71-af52-33dd-9e9a-1232719a3800 | -7.2628 | -49.8853 | 2026-08-20 11:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 217.1 |
| 8c4cc41a-bd77-3632-aceb-0c330df31114 | -7.2441 | -49.8867 | 2026-08-20 11:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 682561d7-9f32-365e-83c2-bbc29b2b464e | -7.2628 | -49.8853 | 2026-08-20 11:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| b67788a5-2563-3be6-b12c-aa2bf56e6940 | -7.2441 | -49.8867 | 2026-08-20 11:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 09a7ead5-18a0-3ee5-ba86-e93872c40d12 | -11.3989 | -46.3759 | 2026-08-20 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 7ac5e79f-8abd-3588-9a1f-efb57c0db97f | -11.3797 | -46.3784 | 2026-08-20 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 6d35cdaa-c608-3d76-a05d-84c65bbec6b2 | -7.2628 | -49.8853 | 2026-08-20 12:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| f553fd0d-c9ce-3767-b692-4073362b4b19 | -11.3989 | -46.3759 | 2026-08-20 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 328bc1c5-1714-3b0b-9b37-066334ec279a | -7.2441 | -49.8867 | 2026-08-20 12:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ffa25dbc-6cb9-391c-a032-b6f2fad8704a | -6.2353 | -55.4118 | 2026-08-20 12:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 562ac0af-2e72-3fa1-887a-d1cd886b42c4 | -11.4418 | -47.2461 | 2026-08-20 12:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| b16ae98a-cc48-391c-b157-5f8d9d93a1bb | -11.3797 | -46.3784 | 2026-08-20 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 3e5560d7-263f-3355-a634-88517f1da2fc | -11.3989 | -46.3759 | 2026-08-20 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 53ef7fa1-e74c-365d-8b21-8edcda204f36 | -11.3989 | -46.3759 | 2026-08-20 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 3de37e11-cbd8-3776-a7b2-94ef2c637b19 | -6.2353 | -55.4118 | 2026-08-20 12:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| ee988892-3188-3f5e-b685-a2ca9d138a2c | -11.4418 | -47.2461 | 2026-08-20 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 183.6 |
| 3d84f1da-c5df-3b69-a15e-08a430907019 | -18.0285 | -44.6113 | 2026-08-20 12:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 9014766f-27e8-3b36-b422-b4b4594ae187 | -11.4227 | -47.2486 | 2026-08-20 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e1cd8299-0370-3013-9148-97bace7e32f1 | -6.2353 | -55.4118 | 2026-08-20 12:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| daf6dc3f-d477-3999-aebb-47635cea8f89 | -18.0285 | -44.6113 | 2026-08-20 12:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 5db83b82-a941-3f89-9d34-bc2df9fa8736 | -6.5829 | -58.9851 | 2026-08-20 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 03f8da19-59f0-3fca-bdce-9f189e6e74be | -6.2353 | -55.4118 | 2026-08-20 12:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| d56eccf9-5f73-36d8-93bc-be6f765fbec7 | -11.3989 | -46.3759 | 2026-08-20 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 6f44940a-8842-3c11-ae1b-0db297c7f5d0 | -18.0285 | -44.6113 | 2026-08-20 12:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 71b443ad-8c00-3108-b3ce-4d3a77b638ac | -11.3989 | -46.3759 | 2026-08-20 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 247.1 |
| e5c91352-fcf2-3695-8530-9c7a5e4b842d | -18.0285 | -44.6113 | 2026-08-20 12:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 160.1 |
| a17e4f99-4933-3018-97d3-a7fd21126ab0 | -14.715 | -47.1387 | 2026-08-20 12:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 917d0053-dff3-3d8b-b8db-45906f52ee54 | -6.2353 | -55.4118 | 2026-08-20 12:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| ea8c4e7a-2799-3ba3-bfa5-4367c0d14f27 | -11.4418 | -47.2461 | 2026-08-20 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| f3183a0d-89b9-3260-9063-d47f69609a76 | -6.5829 | -58.9851 | 2026-08-20 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 531ab8b7-a2a2-3a62-9863-3c4744656980 | -6.5829 | -58.9851 | 2026-08-20 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| b2e18140-025e-3017-a8f8-702690348ae8 | -6.2353 | -55.4118 | 2026-08-20 13:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| ad98a456-f6f0-3aae-8ce7-84c6d5cdf8d9 | -14.715 | -47.1387 | 2026-08-20 13:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 1c9c3677-897d-3d8c-84d9-f96bdf198b63 | -11.4418 | -47.2461 | 2026-08-20 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 24699e7b-69ff-3e2f-94f9-408f9e62a1f4 | -18.0285 | -44.6113 | 2026-08-20 13:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 083f65a7-befc-36fc-bbfa-d5fc7ba0526e | -5.8088 | -55.7095 | 2026-08-20 13:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 0c6467c8-93e0-36b0-8b93-e62da11c5d72 | -6.5829 | -58.9851 | 2026-08-20 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| ee29c37c-6e57-3e24-bb68-32c70a034264 | -5.8088 | -55.7095 | 2026-08-20 13:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 5906c9e8-8cdd-32d5-88a2-1bbd3294a8c6 | -11.2191 | -55.0382 | 2026-08-20 13:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| cf1477c5-dbfa-322e-8a71-c31775741f9f | -9.2071 | -59.771 | 2026-08-20 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d5bf0fad-42e5-3ace-91b0-af2f5cfffe86 | -18.0285 | -44.6113 | 2026-08-20 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 84a7d82f-a88f-3df4-9b57-2bd945c80d35 | -5.8087 | -55.7293 | 2026-08-20 13:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| b6b7d24f-a030-38e0-92c0-c129c189dc77 | -5.7904 | -55.7103 | 2026-08-20 13:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 4e87ae75-94f0-33b2-9c74-7b0160e53464 | -10.3897 | -61.2118 | 2026-08-20 13:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 7316b6b0-0593-3e07-af14-aca81b667949 | -11.4227 | -47.2486 | 2026-08-20 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 65ca9d5c-b330-3f27-8540-8096f5a82f29 | -7.2441 | -49.8867 | 2026-08-20 13:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1047bd66-7da8-3266-8150-7d706dbaa835 | -11.2189 | -55.0585 | 2026-08-20 13:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 547bc039-c336-3935-a17a-6e38e367c67d | -11.3989 | -46.3759 | 2026-08-20 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 89692292-e5d8-38fb-8f5d-2c374cd796e1 | -6.2353 | -55.4118 | 2026-08-20 13:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 40ca0987-99d8-3ee2-ae2a-7c88cb6a6084 | -11.4418 | -47.2461 | 2026-08-20 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 7fe10e9c-e2ab-3edf-9cfa-ea5acf65a9ea | -11.3989 | -46.3759 | 2026-08-20 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 2eb8af74-1dcd-3100-bc79-114613ee183f | -6.5829 | -58.9851 | 2026-08-20 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 5aacc513-ca17-3dca-a4b1-dddabfe9c645 | -6.583 | -58.9658 | 2026-08-20 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f52d596f-6e83-32a4-99f2-8f95b2216fa0 | -6.4391 | -52.7343 | 2026-08-20 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c16904e5-d617-3646-aee9-0acd5da9e3c9 | -10.4084 | -61.2108 | 2026-08-20 13:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| db7239d4-4667-3b22-9fde-4d33440173e3 | -11.4227 | -47.2486 | 2026-08-20 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 0a753f11-0036-3140-9b0a-4bae08203346 | -11.2191 | -55.0382 | 2026-08-20 13:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| e79ef0fe-0ed8-3959-93ed-edb0abd4a9ab | -6.2353 | -55.4118 | 2026-08-20 13:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| dfd402a0-f10f-35b1-b493-8b88160dd620 | -8.3292 | -46.5077 | 2026-08-20 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 9883b516-c6a3-386d-9620-a09de61764a2 | -5.7904 | -55.7103 | 2026-08-20 13:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 301cf446-f31a-35da-be2f-709b13c0e64a | -10.3898 | -61.1925 | 2026-08-20 13:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d0099f32-3cf6-3093-a12a-45d21bd2a710 | -9.2071 | -59.771 | 2026-08-20 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| b6603832-cd2c-313d-993a-f8dcb4dfed44 | -18.0285 | -44.6113 | 2026-08-20 13:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 186.2 |
| d7983052-0956-321d-bf7d-71bd49d1095d | -5.8088 | -55.7095 | 2026-08-20 13:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| de720962-bde3-36b1-995f-441f5ccd1b91 | -15.7151 | -47.8036 | 2026-08-20 13:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 42158861-a2ad-31f4-a157-4797d3bd6289 | -5.8087 | -55.7293 | 2026-08-20 13:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 654b5b6e-5134-39d9-a0c6-21d7d905ef23 | -10.3897 | -61.2118 | 2026-08-20 13:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| ae53ec2a-429d-3a34-86b5-86083005cf3d | -11.4418 | -47.2461 | 2026-08-20 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 32d5280e-5306-3e07-ad66-3d95ad8f6954 | -11.1939 | -53.9993 | 2026-08-20 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 3af4581c-3cb4-36fd-9ce3-2afb9fc17513 | -11.5812 | -50.5476 | 2026-08-20 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| b03ee6a3-410a-33aa-abc9-7ca5cf6bc493 | -18.0285 | -44.6113 | 2026-08-20 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 199.9 |
| c9fdecb6-e3eb-3065-afb3-f5c3c1661239 | -11.3797 | -46.3784 | 2026-08-20 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| bac45ee8-a209-3faf-a5a1-b732709b6ca5 | -5.8088 | -55.7095 | 2026-08-20 13:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 194.0 |
| 3bc856fa-34d7-3813-b4fc-2a1870d2308c | -5.7904 | -55.7103 | 2026-08-20 13:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 224c9cdb-65e2-37cb-b559-b6fe1edae7b6 | -10.3898 | -61.1925 | 2026-08-20 13:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 993a5528-1895-3bd6-95ed-89b64b105241 | -6.4392 | -52.7138 | 2026-08-20 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| a0d849db-1b9f-3cd1-9c33-4206dca9d01e | -11.4227 | -47.2486 | 2026-08-20 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 12fc2089-ad26-3bd1-98ac-296b79d17cbd | -11.4418 | -47.2461 | 2026-08-20 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 625a3e25-078c-3b95-b6fe-6956b46d3610 | -9.2258 | -59.77 | 2026-08-20 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 6b4729b5-106a-362a-9bf1-195e39d8d069 | -15.7151 | -47.8036 | 2026-08-20 13:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 9df47e73-f932-3a17-a874-baa14e58307d | -7.0217 | -45.9103 | 2026-08-20 13:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 5ea8d45f-908c-397f-8c4c-4954fd287c8f | -7.022 | -45.8878 | 2026-08-20 13:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| bdedf9f1-849c-3b09-8a5e-cd511299b9cd | -6.583 | -58.9658 | 2026-08-20 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 2aa28985-7104-3945-b15c-fcf88b95be5a | -15.7153 | -53.7641 | 2026-08-20 13:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e35357e4-de36-3c56-86a4-637ee567db37 | -6.5829 | -58.9851 | 2026-08-20 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| efbf24cf-d047-3f65-9265-205b8b5a8fc1 | -6.4391 | -52.7343 | 2026-08-20 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 9edecef0-a2fa-3fc5-af31-4184e0f7f3f5 | -7.344 | -55.6741 | 2026-08-20 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |


[Clique aqui para ver as próximas entradas](README72.md)
