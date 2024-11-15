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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e56aa63e-330d-371f-bc26-06afc0afe565 | -15.70973 | -59.11116 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c637672a-d66a-3478-8733-e0dcdc668ac2 | -17.5952 | -57.47564 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 77a0caa3-ef3a-3490-a939-0778e39bc3b3 | -17.70495 | -57.52381 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 59aa848b-e939-3538-a5f0-4c362c4dd4f1 | -17.69644 | -57.52327 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a5299b5d-05fc-30f0-853a-2b77b86df23f | -17.59697 | -57.46357 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 6c5f79cc-af2f-302d-bafe-376c3fb74d4d | -17.60706 | -57.55026 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f9dbc617-1b03-3ed3-866d-25076978ceb1 | -15.9175 | -59.2816 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 736555bc-6c9d-3ed6-8944-499a99ca65b7 | -17.59821 | -57.46257 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| e42617f5-66e4-38e9-9412-dc87bf11eee4 | -17.58165 | -57.56782 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 4268415e-0a37-3849-b1c2-273749e3bfa3 | -17.25074 | -57.46194 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 893c4383-f813-35c8-a1d6-286b6b012a60 | -17.72642 | -57.49836 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| acb41260-3806-34b7-8be1-6cd0801630ab | -15.85782 | -59.29353 | 2024-11-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92f100ee-ccba-392d-85cd-0d6338f57193 | -17.58738 | -57.56353 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 1516557e-281b-34a4-8c51-da905f5a378e | -15.40932 | -58.61701 | 2024-11-15 05:12:00 | NOAA-20 | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b030976-8c80-34e7-9bf2-8d496026f606 | -16.95214 | -57.63517 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 8400606b-fca8-3d64-a1a2-75a68a9a5fce | -15.40599 | -58.61649 | 2024-11-15 05:12:00 | NOAA-20 | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7c12f80-992e-31e9-b2ec-a5949ada1e8b | -17.59242 | -57.47815 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 664e98f1-e86a-3261-98ae-0a626f2c7a6a | -17.58242 | -57.46542 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 478924c3-cac8-3819-ab47-199b9a2609e8 | -17.2942 | -57.46802 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 799c46ca-2045-3590-9595-76d8cd644ea5 | -17.59883 | -57.48327 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0cf60707-16ad-3626-8d9a-f527e7dec028 | -17.562 | -57.53202 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 70934c35-6474-3cc7-b57a-161fce2d20c4 | -17.70327 | -57.56052 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9a58371a-7b19-3a3e-bff0-efa7ffb3e818 | -17.69454 | -57.54684 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 487c08fa-e286-3372-a14d-5958dd5b5a3d | -17.29569 | -57.30764 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 465c8adf-6a33-38bb-95cd-68212df37747 | -16.02262 | -59.39067 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d792863b-6de7-3e6c-9629-9d8dde3cb95c | -17.63257 | -57.54607 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 1b101364-9af7-35bd-97a4-db05f0435fc7 | -16.94525 | -57.63409 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 89c82862-a312-3039-8c49-4a29e9a68c01 | -15.15914 | -59.71912 | 2024-11-15 05:12:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce909dca-9110-3b7a-acdd-f8c72a8fe61c | -17.25594 | -57.47502 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| d7c3c530-3565-37ea-be01-6f024038eb59 | -17.56489 | -57.53657 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 0278075e-aa17-34cc-9772-7794e89169bf | -17.25305 | -57.47048 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 3705f3d0-7579-3382-a091-c66b3b1b84cc | -15.89094 | -59.27704 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c75329a4-54f8-3b26-b669-20a0c6d656bf | -17.56606 | -57.52856 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| b2ae0134-add9-38c8-b1bc-3820c00a1b89 | -15.30876 | -56.52043 | 2024-11-15 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96425358-1554-3d3d-8f09-baa3f278251f | -17.57412 | -57.57072 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 53e5c0c6-201f-33f4-b4aa-74e5fa697b67 | -17.57013 | -57.5251 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| f8b7b859-a147-3e75-89ff-66b9ef81540b | -17.64708 | -57.44545 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 820b60dc-51f9-31b8-98e3-03b8d77fe509 | -17.24785 | -57.45739 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| d376f2c8-7103-3e4f-9ae6-aa3c325b0a06 | -16.07215 | -59.70294 | 2024-11-15 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6d50dc1-583e-3887-8c9e-ad3affd7c2bd | -17.29014 | -57.47149 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 28f32444-8d26-3eb8-aa1a-f4165a6ba577 | -17.57529 | -57.56274 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 864211d9-2529-31fc-9a01-520716bdc600 | -17.59257 | -57.55207 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3eee0c16-3050-3288-976e-04c48def9ed7 | -17.25481 | -57.45849 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 5f55031f-91b1-367c-aed1-c2f79cf648d3 | -17.58518 | -57.54385 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fec15e36-a3cc-3bb5-a632-767b853e27b2 | -17.58645 | -57.48661 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 226893f1-a75b-34bf-a423-938c1047b188 | -17.61807 | -57.5479 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| be5f93a4-db61-3b1b-828e-45cabc214638 | -17.5868 | -57.56753 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| 5846f481-a78f-3c46-ab57-ac660f38239c | -17.58956 | -57.49828 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2cab89b0-03f8-3354-9734-0ca41152749e | -17.58219 | -57.57498 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| e8961300-9af7-3bf0-9f99-0980743c4ef1 | -17.63489 | -57.55464 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c749363e-7a63-351c-8723-dfbe23a4273c | -17.61401 | -57.55135 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 53fb691b-b85d-3579-804e-54239e295172 | -17.70036 | -57.55597 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| f791153d-0f8e-3f92-b868-adf0d1a69b13 | -17.25477 | -57.48299 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3cad0e94-0a2b-3c72-996e-e993eb86039f | -17.58994 | -57.48716 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ce692ad9-d4a8-3eff-8272-0c7af0644402 | -17.58283 | -57.55983 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 1dbe4938-d27b-32a0-a86f-bd55f948051d | -17.62561 | -57.54498 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b7ea57eb-464b-3097-a2fa-b60dd2317ef1 | -17.70094 | -57.55195 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| be56aba3-7970-3075-8979-f91420e2184c | -17.63605 | -57.54662 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| f3bb9dee-9458-30a5-9855-aae4b34643bd | -17.57935 | -57.55929 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 9017ce6b-101c-3e60-a907-e295db00b74c | -17.6465 | -57.44949 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1b5b971c-a241-3ae7-a923-199c506a6a69 | -17.23972 | -57.46431 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| a018819b-ced4-3663-9868-91c8b56e9b57 | -17.57759 | -57.57127 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 6a65562f-300d-3f79-85b1-95d88765e014 | -17.29768 | -57.46857 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 188d7a52-9419-343f-a8ea-7e441f5b47d5 | -17.23741 | -57.45576 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 382e0d98-d33d-35c2-aa12-00f812a2dd2d | -16.02318 | -59.38711 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ca6fa81-59fb-3980-a1be-a866de76a34b | -17.26001 | -57.47157 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 78f5be98-c9e7-3976-95b4-e544b468c439 | -19.77522 | -55.4139 | 2024-11-15 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 7ef52447-7412-3f68-afa1-e7dc4de9bf0a | -17.27337 | -57.48928 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3ee20378-11fe-3e04-b779-bf437a0f6468 | -17.5701 | -57.54966 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| 2fef48c6-35b9-37ff-972a-6a1768fd734a | -17.29161 | -57.31115 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5a2c2610-b088-3b01-8845-bef5f487d147 | -17.59028 | -57.56807 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| 38017e37-aab1-3e0a-9166-68a3e0a41126 | -17.63199 | -57.55008 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d21c0cef-cff4-3035-b297-8b14c8a0b2e5 | -17.57779 | -57.4482 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 58043440-5fa7-3260-9612-d3af7cb9b48b | -17.59547 | -57.55662 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9a674829-2d86-3ed8-a5c0-88c209c0a1f2 | -15.29337 | -56.52649 | 2024-11-15 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fdff2387-d2b7-3893-bca5-c747c026628b | -17.71131 | -57.50422 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 66a34e45-65f0-34f8-b8a4-54b689bc9878 | -17.72293 | -57.49781 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1488ebfd-1497-38e6-a4b3-88fe66329e43 | -17.5817 | -57.54329 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2cda00ba-7a14-300a-ac98-5cb0e24e69f6 | -17.70844 | -57.52436 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 86796925-ada4-3418-8457-63e9f7a35656 | -17.57893 | -57.46487 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f8a40ed4-3ba7-3ef4-8acb-ea11f02bb94d | -20.38514 | -55.69252 | 2024-11-15 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef35ccb7-aaea-302f-bd34-3943ee7890db | -17.57298 | -57.5542 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 6e227c85-9999-3413-a3a5-4c84187832fc | -17.27217 | -57.47275 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 48876ecf-8889-32d4-9745-b7f1d85fe1c0 | -17.56258 | -57.52802 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 4ff2662a-63b0-3635-895c-ae27e9bd0dda | -17.58658 | -57.41237 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 62210acc-4ac8-3370-b0f8-e9c1170ad94a | -17.57533 | -57.5382 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f4a83b51-305f-3bf4-bd6a-ecf75e5a8363 | -15.89425 | -59.27761 | 2024-11-15 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29223de8-62e1-3650-a6d1-d8e3750e21ed | -21.07832 | -47.48511 | 2024-11-15 05:12:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 914aea78-28b9-324b-9dfd-deb6fc40d927 | -15.29692 | -56.52706 | 2024-11-15 05:12:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2794f4b-e818-31c4-afa9-47880ff7b04b | -17.58817 | -57.4992 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6bf13ab4-aae9-3b0d-9e00-64c5b22401c8 | -17.56837 | -57.53711 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 225aa14c-0051-3ecb-863c-22066dba1273 | -18.02909 | -57.34774 | 2024-11-15 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8137a63e-d3ca-3af1-971a-13c64593f40a | -17.24089 | -57.45631 | 2024-11-15 05:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| cde43879-4861-3ad7-be9e-ae3f67102506 | -17.5839 | -57.56298 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| e8a2ca30-ac66-30a1-8113-575631080178 | -17.63141 | -57.55409 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 41cf7dee-aa9e-3e84-8062-f34d16360f85 | -17.5772 | -57.45223 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2365a8f9-51d3-3659-ae91-3f2bcc648e59 | -17.69119 | -57.53477 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 214e7f0c-9cb1-3b4c-b00d-32ee735948b6 | -17.67261 | -57.54006 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0499d7c5-6cd5-352a-910a-088fce9b4a5a | -17.69803 | -57.54739 | 2024-11-15 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 58bd733b-a2e9-3361-a888-842aaebcd829 | -15.42493 | -59.04285 | 2024-11-15 05:12:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README31.md)
