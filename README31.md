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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01fadb62-f5c2-371d-ab20-86355c2b08ef | -9.62378 | -48.98234 | 2024-10-15 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc274d43-6b2b-36ac-8103-a7a82a49070c | -9.62324 | -48.98534 | 2024-10-15 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 841f48f7-19fc-3988-b372-46bf0525f0f1 | -9.53382 | -48.99376 | 2024-10-15 04:02:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f210950f-b9ef-35d3-83a7-58c2391cb1bf | -3.16054 | -50.45961 | 2024-10-15 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be64e47a-9184-36a5-8280-e9012e19a1b7 | -3.15442 | -50.45862 | 2024-10-15 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc0c4626-327a-322e-ad4a-9fe725482799 | -3.15362 | -50.46326 | 2024-10-15 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 463d5d53-e595-33cf-96a7-71eb6065cc13 | -2.68247 | -49.05364 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb07afa3-fd79-310e-93da-ee56b07f67aa | -2.68184 | -49.05748 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c882f977-b947-3e3f-9ade-6d62be2d37c8 | -2.62792 | -49.27601 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad531a52-01d0-3b24-a82f-b7b38c67f277 | -2.62725 | -49.28004 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28ee5560-4306-3dce-9873-d5d12feffbcc | -2.61581 | -49.08655 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e6d7916-8ae5-396e-912c-29479eaedc5a | -2.61519 | -49.09037 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11391a87-0b45-3d5d-be87-2654e30116fd | -2.61142 | -49.11353 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 784178a8-e90b-3a6a-971d-c1c833da26ce | -2.60575 | -49.11268 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1566b54f-c079-3e45-999a-e97982a8ac7e | -2.60512 | -49.11654 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c153f903-d35e-390b-9d65-16cd8d3edf92 | -2.60311 | -49.11178 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f537f48-30e1-3286-83f4-e468335a3ff1 | -2.60245 | -49.11563 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2fbb3840-606f-362f-8912-9739b67f0605 | -2.50211 | -49.0724 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f1c3e57c-f75a-35f8-91a1-ac0f183996b8 | -2.49646 | -49.0715 | 2024-10-15 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4a66c7d4-68ec-362d-b934-89041a070fdf | -2.44207 | -50.23442 | 2024-10-15 04:02:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 74a69a2f-0102-301c-96eb-dae840b781a2 | -2.44129 | -50.23901 | 2024-10-15 04:02:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ab15440a-d614-30a4-b5bc-86c89247edb5 | -2.44094 | -50.23648 | 2024-10-15 04:02:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d528538f-ef29-3b44-bf32-90c6568540b6 | -2.4402 | -50.24105 | 2024-10-15 04:02:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 55d8992b-8400-3cae-a46e-3e31f17de8ac | -2.43597 | -50.23346 | 2024-10-15 04:02:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c011af54-c1e7-35d7-8c72-85504c3b8f47 | -2.4356 | -50.23088 | 2024-10-15 04:02:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 24c03107-cd6d-335f-a2aa-ce76f5753ec3 | -2.43518 | -50.23806 | 2024-10-15 04:02:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| aa021ab6-c18c-3a27-a07b-fe53d2c53ae3 | -2.43484 | -50.2355 | 2024-10-15 04:02:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cb5f5ec0-b13f-3d5c-8037-e766e695e1f9 | -2.43441 | -50.2426 | 2024-10-15 04:02:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 34a0922c-0b3e-3374-908e-59be0b584e2c | -2.43409 | -50.24012 | 2024-10-15 04:02:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9503f761-9cbe-3590-967c-e7aa358c2245 | -6.54707 | -49.85773 | 2024-10-15 04:02:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0c824c1-72f5-355c-a793-d16104a3ded4 | -5.26485 | -50.47107 | 2024-10-15 04:02:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80f60258-7fff-3f15-aa03-fe05775d9dc4 | -2.90546 | -51.93591 | 2024-10-15 04:02:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 910ff387-351f-33e7-92ac-c1832298e6e7 | -2.90186 | -51.94019 | 2024-10-15 04:02:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dccee287-adf8-3ad0-a495-6a37c772dbfc | -2.89771 | -51.9408 | 2024-10-15 04:02:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94985d98-7852-3c46-8cd3-ae8d38e64f5e | -3.87276 | -52.13772 | 2024-10-15 04:02:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7acc525-3d08-3aef-bea0-add077a94593 | -3.86991 | -52.27332 | 2024-10-15 04:02:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd697c82-edf3-383c-bea5-250c5934bc82 | -3.82019 | -51.86485 | 2024-10-15 04:02:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8487ba89-f848-3fba-a121-3add815e02e9 | -3.81792 | -51.9171 | 2024-10-15 04:02:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 513db39a-ff05-32e6-8ce2-86c4631e7fd5 | -3.81591 | -51.92873 | 2024-10-15 04:02:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 58d32698-a80f-3789-b682-ee82514910c4 | -3.81361 | -51.86364 | 2024-10-15 04:02:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4ea6c012-08cc-3a87-866f-a322959eb0f9 | -3.68003 | -51.1735 | 2024-10-15 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bd366e2-4c09-3bbb-a670-93503c2699ea | -5.51431 | -51.11749 | 2024-10-15 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ffbcf7fe-2eb1-3477-9a1f-5086a0c4f23b | -3.42019 | -52.73278 | 2024-10-15 04:02:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 64e97210-d5e4-30cc-bf6f-135a0bfb3802 | -3.1008 | -53.04654 | 2024-10-15 04:02:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0620e09f-e85a-3d17-ab68-5cd78f889d38 | -3.09935 | -53.03539 | 2024-10-15 04:02:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2f4d7d8-13c2-355d-9edf-3ce7147753fd | -3.09692 | -53.04954 | 2024-10-15 04:02:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 036b1bab-bcee-371c-b143-cc8d0031e757 | -3.09485 | -53.03871 | 2024-10-15 04:02:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a18e4fae-1fd1-3ab7-a6e2-26ab60461c2f | -3.09096 | -53.04154 | 2024-10-15 04:02:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8702da73-fec2-3c8c-bac0-40d4025f62e7 | -3.08767 | -53.03782 | 2024-10-15 04:02:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9522679d-df6b-3b85-966e-8b1f55beab10 | -3.82037 | -52.39733 | 2024-10-15 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 651cefdd-d603-3330-a1b2-fd90bc3d81c2 | -9.00717 | -54.50278 | 2024-10-15 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 90435b84-607a-3627-9af6-afb4e3ba907c | -9.00576 | -54.50967 | 2024-10-15 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 46c58e50-c11c-329e-b7a8-5ca5cbab22fc | -9.00267 | -54.50505 | 2024-10-15 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| afb72738-5be4-3661-9173-caa5b0078a54 | -8.98611 | -54.58848 | 2024-10-15 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 59fa5d43-228f-3c9a-ba76-ea4ba5e4c454 | -10.03615 | -54.33499 | 2024-10-15 04:04:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| fca56c07-e86d-3901-933e-216afcc28028 | -10.03577 | -54.33761 | 2024-10-15 04:04:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| de78fb0d-48c9-39c0-a316-abb1176b96b9 | -10.03485 | -54.34131 | 2024-10-15 04:04:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| beee06b4-5541-31fd-946f-02799216ac1a | -10.03454 | -54.3438 | 2024-10-15 04:04:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 76638e96-4fd9-3f1c-889b-9419d4edf69a | -10.02799 | -54.33976 | 2024-10-15 04:04:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4dee29a4-cecf-32e1-b9d6-bd9779d11e2a | -10.02769 | -54.34223 | 2024-10-15 04:04:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50555cb8-eede-365d-bed7-c291ab3f3dfd | -10.80621 | -53.89491 | 2024-10-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f57e31a4-7ff7-311e-90df-896dfebecfb8 | -10.80499 | -53.90089 | 2024-10-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b8f7e02-0035-36fd-a1d2-ef8fe149d46e | -10.9457 | -54.09431 | 2024-10-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f588b096-0f7f-3c40-8cd6-a5e693002f5f | -10.94441 | -54.10053 | 2024-10-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0ab1c5ba-d974-387d-929c-24ea9ca607ab | -10.9417 | -54.09911 | 2024-10-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a1f4c740-699d-3de0-8f96-5ace867aca2f | -10.94044 | -54.10541 | 2024-10-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| adf045e2-369a-3367-afdf-e1118ac8cb8a | -10.9377 | -54.09921 | 2024-10-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| decd3875-f51d-3a7b-bab0-1d73fce19e5b | -10.9364 | -54.10546 | 2024-10-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| eca18658-ac18-33db-9231-d55d42aa21b2 | -10.93501 | -54.09769 | 2024-10-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d047437e-2adb-361b-a845-a2ed7e2864b1 | -10.93375 | -54.10397 | 2024-10-15 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3259177c-add3-38b7-84f4-deba8bd0ef00 | -13.54457 | -43.30688 | 2024-10-15 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ed7f7778-730f-338d-8dd1-ea4ef2c935cd | -12.37891 | -42.74337 | 2024-10-15 04:04:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d1d7759-e570-3da8-92f4-df6eadc402df | -13.871 | -43.03505 | 2024-10-15 04:04:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 87bc2ace-4698-3aa8-b3bb-720a79cb055d | -13.8236 | -43.14447 | 2024-10-15 04:04:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9b7e4605-1e75-37e0-8a0c-a454c3f966f8 | -14.91924 | -43.4592 | 2024-10-15 04:04:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a14fc3d7-7d62-3e27-b7a6-4869d92fc6a3 | -15.58922 | -43.21404 | 2024-10-15 04:04:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ecc8b351-ebdb-3449-9755-423f0bfa4512 | -11.72098 | -44.57877 | 2024-10-15 04:04:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc65b3cc-9e88-3d9e-9f05-13edbb0e4c5b | -17.38679 | -42.66045 | 2024-10-15 04:04:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d2f5e85-6368-32d4-afef-7abfbde2f375 | -17.59773 | -43.19698 | 2024-10-15 04:04:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4fd7054-353e-38a6-a53a-c485dc95be97 | -11.11895 | -44.47241 | 2024-10-15 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2ae281d-d1df-334e-9217-671cf518d500 | -12.0863 | -43.89097 | 2024-10-15 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7719b0e9-cd43-3356-a347-e49434bbb945 | -11.88843 | -43.81337 | 2024-10-15 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 353e1634-05cb-356c-ba30-ebbfb680cb15 | -13.59481 | -49.78961 | 2024-10-15 04:04:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ae756f4-5c2e-3697-a383-0ceac249496a | -12.20561 | -38.24987 | 2024-10-15 04:04:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 61c69afa-e8f8-30ad-a018-485ab4976b3a | -17.42797 | -39.60831 | 2024-10-15 04:04:00 | NOAA-21 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ae0bc7ed-44b4-3d05-b569-689656123394 | -19.22412 | -40.13781 | 2024-10-15 04:04:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0c851ddb-7324-3d68-8ff9-24a1705159d3 | -19.22354 | -40.14197 | 2024-10-15 04:04:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a07353c6-1f54-3b79-bef0-a40d92853e41 | -16.12808 | -40.61063 | 2024-10-15 04:04:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c8b443a9-910a-3145-9068-a50b593db95f | -18.49406 | -41.24489 | 2024-10-15 04:04:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0b532e96-0b30-3a3c-bcfb-8fb5f656ce80 | -17.25057 | -41.96584 | 2024-10-15 04:04:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 92b03aaa-889e-3f08-9e3d-6fd7a1d28e52 | -18.10649 | -42.34572 | 2024-10-15 04:04:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5377ce11-20ea-300f-a8b7-c490e439fedf | -13.74436 | -43.58861 | 2024-10-15 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 004269e2-603a-3de0-8dca-3a39857fb169 | -15.58648 | -43.2098 | 2024-10-15 04:04:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d5632191-b6f6-3a46-aad2-f8c1022192e2 | -15.58588 | -43.21347 | 2024-10-15 04:04:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 166001cf-40eb-3d8c-acea-ff730d6b887d | -16.34914 | -43.69709 | 2024-10-15 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c14991a-7a5f-3a36-8b11-185ae77de82b | -16.18225 | -43.86063 | 2024-10-15 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4c62607-3853-3364-92fd-c465f62e6cb2 | -16.18163 | -43.86439 | 2024-10-15 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3dfcc61-420e-3504-8b04-235046794a50 | -16.17887 | -43.86005 | 2024-10-15 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68007654-f824-3373-a75f-77bf5680a1dd | -16.17825 | -43.8638 | 2024-10-15 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da001919-61fd-381c-b7e9-58d4224fafd6 | -17.28198 | -43.84354 | 2024-10-15 04:04:00 | NOAA-21 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README32.md)
