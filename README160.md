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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af507a47-31af-331f-ae96-3487230c0efc | -17.04863 | -56.69525 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0f21b459-b563-3140-b15a-61cb1df0eb0f | -17.04087 | -56.70132 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 50000577-a38a-3a11-846b-98ca26215302 | -17.03756 | -56.70075 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8ef60b88-874d-3936-b58b-e175c29822a6 | -16.98284 | -56.15948 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 89b33971-b6ba-3729-8c8b-0cb1204c1d24 | -16.98008 | -56.15532 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 61476696-ab16-3429-b8ed-4c27b5a3dff0 | -16.97952 | -56.15892 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0908c5b3-ea7c-3f7b-86b8-046eeae933f6 | -16.97732 | -56.15116 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 174194ad-0d37-3027-878d-95a1d0d00fd6 | -16.97676 | -56.15477 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 592421a7-11ae-3896-a068-b9adfa2518d0 | -16.97455 | -56.58287 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1223b21b-022a-3c3f-84b8-561f7019fabf | -16.974 | -56.1506 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 77a487d9-8040-36fa-8f9e-0aab45a69f6e | -16.97399 | -56.58647 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 17781cb0-2399-331c-b8f0-22287b8f1ce1 | -16.97069 | -56.15005 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3c3a70c8-d4d8-30d4-bf50-fdfe54cb9130 | -16.97013 | -56.15366 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 14adbb2d-25d5-3361-874b-9b8d4b12492c | -16.96957 | -56.15726 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5a9d2973-0d4f-3272-8dda-548f4132fb91 | -16.96681 | -56.1531 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1614e8a8-c6a9-32a2-9135-0e0e7ef031e7 | -16.6223 | -56.01171 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 72ce6c8f-b73f-321e-8d35-3e720337c114 | -16.62174 | -56.01532 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a4c55b17-6b52-3a98-b253-11be4f0cca3a | -16.62118 | -56.01892 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 552088dd-0a7c-3c1a-a875-974f36baafe1 | -16.61843 | -56.01477 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e5ced9a0-9065-3d09-8cf6-ca4969923e57 | -16.61399 | -56.02142 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1e2d63a2-a784-30cc-8bd9-26226d0c9fd6 | -16.61069 | -56.02079 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a691a3cb-87d9-335d-a162-2f5f028a273e | -16.60682 | -56.02384 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2d5da9d8-a30e-3f92-8dca-b0eec1ed389c | -16.6035 | -56.02328 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0846f6d7-d6cb-3972-93c6-3314be2b0e8f | -16.60018 | -56.02274 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 22d1f16c-bd9f-35e9-9c3a-15cba0309af4 | -16.59855 | -55.98928 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cbcae732-be3f-364c-bfae-73046d1786ec | -16.598 | -55.99289 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c37fa5e5-86bf-39ae-8854-0b4f999156f9 | -17.04806 | -56.69885 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0c1e7ae8-764d-3e11-bed6-e40ff662fb2e | -17.04475 | -56.69828 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 08390ce5-ecca-30c2-b932-12178aec3259 | -16.93043 | -55.83955 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 78a66e1d-005d-3214-a5e6-8c1c929d254e | -16.92821 | -55.85405 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3076a473-b732-338c-8492-71582cfe4197 | -16.92766 | -55.83537 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| c5a9945b-7090-3929-87a0-a7b992718c03 | -16.92765 | -55.85769 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 727114f7-8d4c-3221-916b-cd64daa8199c | -16.9271 | -55.86131 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0d193793-09dc-3475-a3a7-2a4953490ab1 | -16.9271 | -55.839 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 6dc33a21-4c82-3d36-8e3e-8bf8b896ff36 | -16.92655 | -55.84262 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| adce18a5-8d99-307c-aacd-76eddc3725d5 | -16.92599 | -55.84624 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0aed5ca4-f321-3b89-932a-4f116e75249d | -16.92544 | -55.84988 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 37604546-e5ba-3687-a59a-fa8bea3a79d3 | -16.92489 | -55.83119 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| ad6c5507-0394-3a73-a7ad-aed1f200571c | -16.92433 | -55.85713 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fd5339f5-6724-3d28-84f5-e36035243626 | -16.92433 | -55.83482 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| d22fcc0c-5b6f-32e1-b576-152da22d4ed6 | -16.92378 | -55.83844 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 1b7463f7-9c10-363d-a084-ada38b605b49 | -16.92322 | -55.84207 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c3d1e8a4-9c38-3c3a-9714-7e9bcb9a006b | -16.92211 | -55.84932 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 510c11cc-4ac1-30ff-9394-ff230a4bc168 | -16.92156 | -55.85295 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b8834010-d415-3b4b-8700-19230d86cfac | -16.92156 | -55.83064 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 33749bcf-ca6b-3a2f-90a9-521bd616d2d3 | -16.92101 | -55.83427 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d5eb6b7b-3eec-3084-a0c3-89e95e48290b | -16.921 | -55.85658 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b59f2f64-fe06-3f06-95d4-f3c57e9a333f | -16.92045 | -55.83789 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0fd8e159-67b5-32ab-9214-d319d8296676 | -16.91935 | -55.82283 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9e520882-6b3a-30ac-9f93-1ea97b955cce | -16.91879 | -55.82646 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3d916f4d-8625-3512-9244-121c5239ea4e | -16.91824 | -55.83009 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ed307fa1-acb1-3d7b-8bef-7289d883f72e | -16.91768 | -55.83371 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 65467d9f-e9a8-3505-9324-2f6aa1291722 | -16.91602 | -55.82228 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 7ebd0f89-5684-38a2-af30-a89634b29f74 | -16.91547 | -55.8259 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 8f1dac26-4afb-341c-af43-a952bf9df64a | -16.91491 | -55.82953 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c59b5498-c96f-310e-b87c-22d60f7e97c5 | -16.91436 | -55.83316 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ff5a6ce5-ceeb-32ea-b379-16578cd07f80 | -16.91324 | -55.86273 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 81db0f97-b744-3856-be13-6fd445cfe533 | -16.91269 | -55.82172 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| c7e4e93e-5227-3797-96ba-449af5d1cd23 | -16.91214 | -55.84768 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e4b18df0-6dd8-37a0-a586-a5c3bfc2f139 | -16.91214 | -55.82535 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 79eee29d-f79c-3b21-b415-dfb333d9fe5b | -16.90991 | -55.86218 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 84a543b3-29ec-33df-88ea-567b8481c160 | -16.90936 | -55.8658 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7535c2b0-687c-3ebb-bcb4-9dd623443e17 | -16.90936 | -55.8435 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5cc8fd63-3c31-39c7-9198-2988bcbee7e4 | -16.90881 | -55.84713 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d4ff0bab-38dd-3c7a-a237-e56c37e52f61 | -16.90825 | -55.85075 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d5d65502-6a0f-3583-ab5d-092b4409d58a | -16.90659 | -55.86163 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 64b290e7-d233-35ef-a96b-1aaeba0b9b8a | -16.90603 | -55.86525 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 40db744e-0eff-389f-8663-8228e9257313 | -16.90549 | -55.84658 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 05df5adc-936c-37c5-9742-0e5bfbe087ca | -16.90493 | -55.8502 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b9929e24-a67f-3cfd-965b-fa471097a298 | -16.90382 | -55.85745 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c4ce4727-c3d7-30fc-ae14-a61d8b546a26 | -16.90326 | -55.86108 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ebd2b0cd-9b7f-3253-a4c5-4e16667c9680 | -16.90216 | -55.84602 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4bfdc82c-8a14-3200-a93d-60f7a304a764 | -16.9016 | -55.84965 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9ae33801-d0ff-3cee-9e21-166f324ba1a5 | -16.9005 | -55.8569 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 46d70b07-4a40-3a39-a40e-5594c94bac9b | -16.89994 | -55.86053 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 321eb500-e930-3cc3-886e-cbef7dc2016f | -16.89703 | -55.86005 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2f3cd415-acf0-331a-8571-f0080fe09bd1 | -16.8965 | -55.84138 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e2dfafa0-ff5b-3d8b-91b0-09ddf2c5c1b7 | -16.89373 | -55.8372 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ee83a932-5f59-340e-bc6e-1018b2b75208 | -16.8937 | -55.8595 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6a10f1d0-125d-3a1e-b192-71de32653a8f | -16.89317 | -55.84083 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 736a8c0c-57e3-368f-9e31-2aa6ad134e69 | -16.8915 | -55.85171 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b00444a9-8f8e-394b-bbc2-4a048e9ba00f | -16.89094 | -55.85533 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ede3490c-76cc-3565-90cd-d9b99f4f394f | -16.89038 | -55.85896 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9b686783-2af4-37eb-94eb-dcbcc9ee69f1 | -16.88817 | -55.85116 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b5b76bed-c1c6-384e-b8a2-cfe5a8cbec79 | -16.88761 | -55.85478 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 52ae4176-9904-38c2-92e9-80abba711400 | -16.88152 | -55.85006 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4226fe82-5b03-33fa-afda-645509c886c0 | -16.87764 | -55.85313 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 68ec7887-3f4d-372d-afe5-360514eb90ab | -16.82995 | -55.89722 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5a5e45d2-35c3-3d05-9208-19afd5183a4f | -16.77676 | -55.75927 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0d9bad18-87e3-3e84-a616-c338b0e68c8c | -16.7762 | -55.7629 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| aa68fff8-480f-3f5f-80e7-6b6236a05745 | -16.76289 | -55.7607 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 84608e4a-03d5-3887-824b-2eb42e85b621 | -16.76234 | -55.76433 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f1321825-ab51-361f-8047-be9dfc920dbf | -16.76122 | -55.77159 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5ae3a025-7c0e-3542-b89c-021e5766cb7c | -16.75789 | -55.77104 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2e7658b4-a73f-3e82-a49b-cf98ade5cdb1 | -16.69244 | -55.88647 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 90b7bfdb-853e-3b8a-866c-3e140ba5281a | -16.68968 | -55.8823 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ece87881-f7b0-35d9-8eca-4c5f2f6b2f3f | -16.68912 | -55.88592 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 94a49abf-b31c-3b1a-a13c-124f504a9762 | -16.68743 | -55.94122 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a1f7e62d-0b2e-38b8-aa13-6546c5f7b013 | -16.68691 | -55.87814 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cd1a94d2-8185-3e4a-a248-3a1e16557da2 | -16.68689 | -55.92261 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |


[Clique aqui para ver as próximas entradas](README161.md)
