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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b1a4cd3-f76b-3e72-8ce7-b83fd3438d71 | -16.5756 | -58.23808 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 67cf5bef-841e-3e67-b7ba-2099c0d12cd1 | -16.5739 | -58.2263 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 03295f71-fab9-3e42-a7f7-efae9858e57b | -16.57277 | -58.23378 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| acc63678-422a-3b8a-b7f4-1ea4cf215533 | -16.57051 | -58.24876 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2ce997ef-0ecd-3782-a0b6-93a2b8112177 | -16.56318 | -58.25139 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 74287721-01d9-3820-9d94-1fe22ab0b148 | -15.86353 | -58.24845 | 2024-10-02 05:12:00 | NPP-375D | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a465a66-e62a-3f78-a587-aec6671a7dce | -15.38279 | -58.15473 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c77f26a-6cca-3b45-b3df-3fcd0312f682 | -15.37941 | -58.15425 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9551e056-ba24-311b-92a8-857d6d0a837d | -15.37884 | -58.15801 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eaa3f291-d060-3b47-80ef-6f54bfc6e5da | -15.37603 | -58.15379 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a81479a-eb6d-3f65-a4d2-5e67bf0bc117 | -15.37546 | -58.15752 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb25a796-23ca-33b7-918a-c38e2561d34f | -15.37208 | -58.15701 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c851b25a-17de-39bd-aaee-e7accf0ff851 | -15.35972 | -58.1702 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88144329-4cb9-3816-b7ce-d8e7d3d62f02 | -15.28266 | -58.19191 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93aabb4a-dabb-3b13-a866-cc2ec9a60bdb | -15.2793 | -58.19133 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23c092ca-d2b8-3e11-bf3b-d8e35afa1e9a | -15.2765 | -58.18707 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 84fb72cd-2d92-35c8-8fff-fee9db99dfb6 | -15.27314 | -58.18646 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 301864a3-9ed0-3f35-b109-64ea7574ed11 | -15.26978 | -58.18588 | 2024-10-02 05:12:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee68153e-f964-3694-b066-1b09bfb1bffb | -16.8131 | -58.42442 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9e25b135-6e47-3cb8-9361-e5a5c528dc86 | -17.04101 | -58.3919 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c1146265-dfca-336d-b347-be4950b798a5 | -17.03763 | -58.39134 | 2024-10-02 05:12:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 53853bb8-7168-32e2-a313-7ceadc5c9cc1 | -12.32651 | -59.21808 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cd3ccab-55e8-3992-a17c-74f6365aca87 | -12.32595 | -59.22163 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a49e839-3023-35e7-9a17-65d6a76c0656 | -12.32261 | -59.22109 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 619885a8-d8cd-3e65-812b-988d2063459b | -12.23414 | -59.23931 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b9ade01-e113-3f8b-a419-e326579d1dce | -12.23358 | -59.24286 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ef1939a-92f6-3534-86fe-714e3f547409 | -12.22967 | -59.24587 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35995071-b94a-3dc6-840a-6cd2aebbef78 | -11.02302 | -59.20223 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a8fee9a-64aa-3994-a50b-5150affa73e9 | -10.98138 | -58.96943 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b7d690e-771b-3b65-899d-9c709c009da4 | -12.16795 | -59.73554 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9643198c-6b5b-384a-94ab-26ae1423fdfb | -12.15568 | -59.72606 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c4d10c0-dd91-3b6b-9d44-67fd623bedba | -12.1539 | -59.88601 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdf3a3de-f7a3-3b00-b001-10ef6e39a446 | -12.15274 | -59.74416 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2dd7d0f-69cc-3d93-a420-c63d31758b15 | -12.15053 | -59.88547 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60a66e3c-239d-36ae-b64f-b906a99215ba | -12.14997 | -59.73997 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3d6e23c-8081-3208-b0fe-303c35dee6bf | -12.14821 | -59.75084 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 474b8d0f-7343-3576-baae-349f7f914de1 | -12.1472 | -59.73581 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f411f914-e38d-3ceb-9bfe-e7e99c3603a9 | -12.14715 | -59.88491 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02a59e32-0b7e-39d3-928d-d776da98b338 | -12.14703 | -59.75808 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc4f150c-96ed-3e68-9354-717bfe9d49cf | -12.14656 | -59.88854 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 228d7289-f55b-35c6-a530-d89d279585d2 | -12.14485 | -59.75027 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b4f6776-ed66-3602-b9d0-a34267d77a2a | -12.14426 | -59.75389 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c788ba1b-1203-3548-95a0-6faa53d90bae | -12.14319 | -59.88799 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54ba0892-b37e-307a-a148-a4c84606c562 | -12.1426 | -59.89163 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d862212-c479-3143-9ffd-4deaa93e393d | -12.13982 | -59.88743 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a7372642-2702-37d1-8919-3b76c773f4a8 | -12.13922 | -59.89108 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6334a37c-7192-304b-979a-53dae3771f44 | -12.13807 | -59.76445 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb26c635-cdbf-3716-ae14-ea06ad7bcefe | -12.13471 | -59.76387 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 842f1863-c048-3b72-ba24-f65fa472d052 | -12.13413 | -59.76751 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6050e28c-539b-39b5-9218-d0750d5d98fa | -12.13076 | -59.76694 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f22ff32d-69c4-3e87-a46f-fc32e03c7e5b | -12.12682 | -59.77 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee96dcd1-178c-3bb7-a60a-ff44836a4a85 | -12.12624 | -59.77363 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1afffb80-acdc-39e9-8074-3c4131e2df37 | -12.12565 | -59.77726 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 484639d6-a8c2-3f18-9a39-e98ef8935bb3 | -12.12507 | -59.7809 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be1289b2-33cd-3df7-b368-6c982bbbfde4 | -12.12448 | -59.78453 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aecb6972-3b6b-3cde-b3fe-a4d9b8866861 | -12.12112 | -59.78396 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89c7cd23-68d9-3bba-9f86-450cb4dc24f4 | -12.12053 | -59.7876 | 2024-10-02 05:12:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 607c0107-3295-381f-8a32-295f854cd811 | -12.35755 | -59.29601 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b83ebc89-63d7-3edc-b14f-5ad48d3151a7 | -12.34811 | -59.29079 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98f09659-7a92-33ea-8a9a-e4a0fc482cc5 | -12.34672 | -59.21394 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48f1d470-4591-3de6-9579-8c6df65240f0 | -12.34421 | -59.2938 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e91b55fe-2934-3f5a-bb69-de3ffabbe17b | -12.34395 | -59.20984 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 318de18c-20c3-3db5-88a8-08ea99eb5b23 | -12.34338 | -59.21339 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6d57210-c472-3d86-b2ee-eded92c88c8a | -12.34282 | -59.21694 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f9f8f0a-87f2-341e-bf67-a1cbb13be8c6 | -12.34225 | -59.2205 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d55e4a2b-bfe5-388d-be8a-086abca97ec1 | -12.34062 | -59.20929 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4f07e5a-1890-34e7-bf16-6e44e06e0567 | -12.34005 | -59.21284 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1d27ae5-694b-3348-a397-e902ab502318 | -12.3386 | -59.30748 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dd57c10-ca2a-3307-933f-365b03b8b120 | -12.33764 | -59.21261 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 606b7405-71cb-3b36-9af5-2b06e0a31ebc | -12.33318 | -59.21917 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da4719b5-e79b-3f7b-9bda-435a8096c930 | -13.1464 | -59.80046 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceb72711-aaae-364c-b2be-162569a07764 | -13.14465 | -59.81132 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49f9ea5b-a1f7-31f7-9a52-6b893b018eed | -13.14188 | -59.80714 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98734454-5601-34d5-81c5-8761c4c8524e | -13.04068 | -59.86836 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f037d495-82ca-360b-b3d0-d631b2746f8e | -13.14975 | -59.80102 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1e9de29-b07a-3624-aeea-e2ce6b64538b | -13.03732 | -59.8678 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52934afc-b112-3d30-81e1-efa4643c0a17 | -13.03396 | -59.86724 | 2024-10-02 05:12:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a70a666-23f7-3c72-b98a-36970db09134 | -14.49802 | -59.62364 | 2024-10-02 05:12:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 696e08c8-7abf-3deb-be11-3830fa41005b | -14.79594 | -59.42653 | 2024-10-02 05:12:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af2ed695-0d1f-3fd1-b4e1-e4c873a7ce15 | -14.79369 | -59.42651 | 2024-10-02 05:12:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c4b5684-1c66-3f16-8eb2-23d0ce89020c | -14.7898 | -59.42952 | 2024-10-02 05:12:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26ceeae8-10f2-334e-b4db-d41cf9a2a2ad | -14.18386 | -60.25315 | 2024-10-02 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ea97b9a-5ea5-3c02-9cd8-66107c79ea06 | -14.1805 | -60.25257 | 2024-10-02 05:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3dad1db-742f-3e62-b130-ec8c8bddfb1f | -15.74689 | -59.57311 | 2024-10-02 05:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbdf06f3-ece1-3727-99b0-e77dc2036fe3 | -12.30759 | -60.75843 | 2024-10-02 05:12:00 | NPP-375D | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 213ad25d-3988-3858-b883-1c42176da988 | -12.23014 | -60.63513 | 2024-10-02 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e394c9d-8a89-391c-919c-fc628fcde54a | -12.13928 | -60.76612 | 2024-10-02 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d12a7eb3-ee90-3965-afad-f952ffd38f6c | -12.13865 | -60.76995 | 2024-10-02 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c46f3211-4f40-30ec-a583-ab2c83dbd8d8 | -12.00303 | -61.08543 | 2024-10-02 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff01eb64-5aac-3e4a-a0f0-1f4fcdcaa59e | -11.99953 | -61.08483 | 2024-10-02 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d945f3fc-13cd-3a94-bef2-e11cbea409eb | -11.90545 | -60.29511 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb4db8bf-c272-32e0-a809-5b2c7985b698 | -11.24699 | -60.47861 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e510c96e-febf-327d-8641-6fe6f3205a79 | -11.24416 | -60.47426 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 019ac1d8-fc0b-3e63-9a3b-976a4fce4684 | -11.24354 | -60.47806 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 811ac17f-9a32-35bd-8591-e04de6fa408a | -11.24194 | -60.46615 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a459dd0e-31b8-330d-af34-6b98586ea262 | -11.24132 | -60.46992 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 183cf8c4-1387-3dfc-91e7-4e44cc99e7b8 | -11.2407 | -60.47373 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9925b68-c03d-35fe-938f-1f74361d32e8 | -11.23848 | -60.4656 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c054305-c54b-3a81-a87c-0932dce5917a | -11.23786 | -60.46937 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e9e7da1-ea7b-3c8d-8006-17f3beb8b346 | -11.2344 | -60.46885 | 2024-10-02 05:12:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README156.md)
