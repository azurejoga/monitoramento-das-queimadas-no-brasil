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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07207990-9656-319e-9039-8ece6e33fa71 | -3.08743 | -53.37283 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c507f67-e03c-3875-b270-54a6bf45d59f | -3.0838 | -53.3723 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89b6d70b-ac03-32d4-ab00-954cfbeff754 | -3.08125 | -53.03028 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8c35111-10df-3026-a620-7e4cf64b669e | -3.08081 | -53.36763 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cf73296-c5e8-30d8-bb76-ef40161cc3d0 | -3.08057 | -53.03463 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b53325d-958a-3e00-8835-f5da21526d0f | -3.08017 | -53.37178 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6c4261f-f2c4-370b-b624-a67184f20ef8 | -3.08012 | -53.29914 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30d41bb7-15f1-3bcc-a5e9-74a38a14e411 | -3.07757 | -53.02969 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ef1056a-7656-3f34-8109-e710290c23c1 | -3.07718 | -53.3671 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96733515-6326-3ce3-9c97-da66553e8081 | -3.07689 | -53.03402 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 501e3fd6-a8be-33a9-a87e-5d87a1c842e0 | -3.07654 | -53.37126 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97ee892f-0934-31c4-8955-030359305a17 | -3.07355 | -53.36657 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd8a6ddf-4ef9-3721-af7d-e677c4c7fccd | -3.07321 | -53.03341 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c9a8964-cc9f-35be-8c67-fc468d019586 | -3.0663 | -53.36548 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0cb1233-9700-3998-808a-aaf87d4c7dde | -3.06566 | -53.36963 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd80f02c-ca28-3cfa-92a9-9a1d99ac281c | -3.06539 | -53.32267 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79c28785-5967-37ce-956c-c8d214ae9b8c | -3.06475 | -53.32685 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65dc07e5-7757-33cb-8e0a-74db7077b7cb | -3.06112 | -53.32629 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 627e2c07-998c-33a2-9028-3ac94906ccae | -3.05968 | -53.36023 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c94f6655-4cb8-3173-96c2-9e44584c01f0 | -3.05905 | -53.36436 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a100a4f3-7e8c-3d27-b9f0-db0a8642da33 | -3.05605 | -53.35965 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2c4cb14-af7a-3a88-baa3-8a52d61401cc | -3.05543 | -53.36379 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8af3cb5f-8145-36d1-97a5-a5dd7065436a | -3.05258 | -53.35657 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9d4d8ba-d2f8-3222-b835-8388b0c865e8 | -3.05243 | -53.35909 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13c1d680-cd28-3f72-9a53-ca07bd08712b | -3.05193 | -53.3607 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7117c6da-e0f0-337e-bc80-da6bd162b7f8 | -3.0518 | -53.36323 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19917046-1559-34a0-9b80-7c18d7ba287d | -3.05128 | -53.36483 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7210a7cc-bd78-3ac1-87e7-ec7804e9be36 | -3.04881 | -53.35851 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81c2cf0e-bf6d-34ee-b797-66d3282cd4ee | -3.04831 | -53.36013 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 749fe7ca-0996-3ceb-9751-d5b9c24d31ee | -3.04765 | -53.36427 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58a2a864-ad7f-3aaa-a020-0b64e8273eac | -3.04701 | -53.3684 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e9f1062-9656-3a6d-8dc9-9efb456263ef | -3.04693 | -53.37094 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dc229fa-4a52-3465-97ae-a8496ef2787b | -3.04636 | -53.37254 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbe847c3-bd4e-3794-a5dd-bf28da45b3a2 | -3.0463 | -53.37507 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 895c9ab7-331a-3373-a63a-fa2d38506b53 | -3.04571 | -53.37666 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9873c82c-73b3-3782-96da-f0174af9a764 | -3.04393 | -53.36626 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95323108-0a19-382e-b41a-156ab06c8e47 | -3.04338 | -53.36787 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef5a456e-acc4-333a-aa08-2903e7dcf321 | -3.0433 | -53.3704 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5d8e686-5e8f-3748-9680-f4f396cdf7cf | -3.04273 | -53.372 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c46db83f-cb1a-3a15-8d81-f8fbec7e8fbb | -3.04267 | -53.37454 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7a7b7aa-9327-372b-983b-6824f21f4a67 | -3.04208 | -53.37614 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 061b0cde-2670-3586-a166-966296405648 | -3.04205 | -53.37868 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b4c2acd-59b1-35db-8e10-a73797395937 | -3.04195 | -52.96633 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bf15f98-ae20-3a6a-b622-c16be7425b3b | -3.04143 | -53.38028 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04c7fb9c-8ae5-314b-8bd2-d2eace21a986 | -3.03975 | -53.36735 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9b57657-f76c-376f-a5d2-141ecfa44366 | -3.0391 | -53.37148 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b62e9d24-b072-30ab-9a90-cefab313f289 | -3.03846 | -53.37561 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e12d0cd8-abd5-3969-bf19-d1bc38db9e0b | -3.03781 | -53.37976 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 138c9a95-ded8-3bbc-8e4f-eacf4fa6c480 | -3.03612 | -53.36683 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82683c92-26ae-30bb-8572-5dd11606674f | -3.03548 | -53.37096 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db80307c-190f-3c83-a29c-2a3f42c0f063 | -3.03483 | -53.3751 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c81b73f-34a3-33df-99b4-812adc0a4ceb | -3.03418 | -53.37925 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 08f056ee-ed9e-3e5e-b817-f6c770aa9b16 | -3.0325 | -53.36631 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1161a33-ec4a-3702-9f99-ac5dafe99d1b | -3.03185 | -53.37045 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96647e06-44b2-349f-b65d-72e413598f22 | -3.0312 | -53.3746 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a6db19f-23d4-33a3-b313-f151bf3c6c92 | -3.03055 | -53.37875 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| be6b36a9-ba42-383c-b54d-10d431b0f0b3 | -3.02887 | -53.36578 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e86c4b39-ba9a-345a-a2a3-2800014d9e5b | -3.02757 | -53.37407 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4260c52-b3ce-3546-9316-e4b0af045a8a | -3.02692 | -53.37823 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5f5011d-a8f0-35c3-9d32-40c3790d3f5c | -2.9969 | -52.96375 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bec884e5-cabc-38cd-b3f1-631b1a2d6af7 | -2.99622 | -52.96824 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f16be8fb-961f-384d-809d-344758c272e5 | -2.9937 | -52.9699 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3945172f-a562-379f-8763-fc0c31f765fb | -2.88604 | -53.20388 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56669d86-fc67-3782-ac61-77d37844eeec | -2.87188 | -53.2233 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d878de5-0473-334e-a44f-3e7497d2e7d1 | -2.87124 | -53.22751 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a746db9e-1683-3beb-bfa6-5a2570f22a7f | -2.8706 | -53.23172 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e0db95ea-5b31-38a5-bc5a-5e105c89e0b4 | -2.86996 | -53.23592 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 903995a5-0f96-382d-852f-5adfca170153 | -2.86824 | -53.22273 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fda1d925-2386-3918-ae52-13aaa8f33041 | -2.8676 | -53.22695 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b8457a70-55f9-3e66-8cad-e348f483146f | -2.86696 | -53.23116 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fe1e5897-2ba4-3c5b-9230-d67a0a3e1119 | -2.86632 | -53.23536 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a4044dd-aa15-3247-a4a5-29a1cc394902 | -2.8646 | -53.22218 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b02e420-8ceb-3f69-810a-d3114e05335b | -2.83731 | -53.40151 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 51aaa0b7-1aad-3d47-b31f-daf9c1ef2390 | -2.83668 | -53.40565 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b0c7a6e4-18f3-3034-a76a-f06918fdb038 | -2.83307 | -53.40509 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c84c1e6-755c-33e4-a784-ce55c92e3722 | -2.83244 | -53.40922 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7fc2d6e-3115-370a-9dd2-f2ed34774024 | -2.81876 | -52.86463 | 2024-11-03 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 132762be-5a9c-332b-8178-87dd5a3c6707 | -2.81742 | -52.8734 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de8c84f1-27e7-34a7-ad05-39b2827bced0 | -2.81724 | -53.16914 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b410052-107d-3af5-81ec-2b1b403fc585 | -2.81675 | -52.87782 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f5c2a12-5448-30c1-a7ff-b53d33b7fb72 | -2.81359 | -53.16858 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99109767-146f-3696-b93b-61e900f8be03 | -2.80743 | -53.2324 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45f5b8d8-fd20-3c6d-b158-7feb88cdac58 | -2.8038 | -53.23183 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f5ece00-dc46-343b-8f5c-e7f8b10134a8 | -2.80016 | -53.23126 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 550752ef-9a45-3c12-bb96-ad96b461a903 | -2.79952 | -53.23541 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97f500f1-8f1a-3e60-9f41-4c4f3f23d447 | -2.7788 | -53.24907 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6d2a15c-4a4d-3839-99b9-78a82decd0f3 | -2.77816 | -53.25322 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 066da87f-2d67-32b8-ae2e-c833d3df67ce | -3.45331 | -53.48817 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65b2b422-0076-3950-9484-b69e0803d48a | -3.44969 | -53.48763 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6869dc50-365f-32ff-83b0-f2819404756b | -3.31362 | -52.99945 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 472d79a2-91c4-3bf7-aff5-610d7a2cde09 | -3.14127 | -52.82154 | 2024-11-03 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3c426c9-54c9-38b3-8323-e8d55f83b453 | -3.13029 | -52.91941 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 219ab168-6ac4-314e-a4de-ba33159da9cb | -3.66838 | -53.42406 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 279208c4-be46-356d-aabf-e4ff861380e6 | -3.53901 | -53.71334 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33e11314-463c-309a-9e76-68b846e461e0 | -3.93622 | -53.47358 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a302c5f8-0adc-3649-be9f-90130cac9215 | 0.03671 | -53.25538 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 282c8037-853d-3dd8-a169-de164a3892dc | -2.06677 | -53.44954 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 203552b2-4218-3e6f-a1fa-b9d78423478c | -1.56798 | -53.62197 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 845f556b-089a-3e3e-a1f4-0386b86cbd8e | -1.55247 | -53.4662 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e740ba37-770b-3a6b-8faa-a5c528a7b09a | -0.96461 | -54.06491 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README66.md)
