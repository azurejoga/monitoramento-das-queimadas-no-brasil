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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4729aa12-a385-36b3-b4b9-da64d4593288 | -17.86481 | -57.57394 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 97f2331f-2805-3601-a941-fc988c89e9c3 | -17.86452 | -57.57109 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 531acf26-7a4f-3f18-a787-009da61d8057 | -17.86333 | -57.52925 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.4 |
| df567ee6-de5a-31ee-b58c-2054d6cb139f | -17.86262 | -57.57261 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| d8fcec0f-61d7-3819-a687-02bf035d6075 | -17.86046 | -57.53163 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| e8c679f3-f525-389c-be6a-d6bda18fb32e | -17.86013 | -57.52848 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| fd726abd-e752-3fb5-924e-1b523c5a538f | -17.85943 | -57.57505 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 99e61c17-92ef-3458-b74d-3390c018bda7 | -17.85756 | -57.57662 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| eb200ee0-5997-3af4-867e-b3a98ef90c87 | -17.85723 | -57.57352 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 8b629f02-e158-3e75-ab2d-25dc08b0f27c | -17.85575 | -57.53919 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 8e234be1-0725-39c6-a73c-0929c2ac912b | -17.85543 | -57.53606 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 690844a8-41c2-3c17-80a0-344bede238c6 | -17.85405 | -57.57615 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 1d306b60-dbc1-366a-a6b5-bcab942af3fc | -17.85038 | -57.5403 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| d09d9b8e-8244-32d9-8cb1-e9bb792820b8 | -17.84399 | -57.55299 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 4cc0af1f-c57c-3583-8381-48bd522611e9 | -17.83701 | -57.25409 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 36a86c9c-4c52-3123-81b2-1c19774346c9 | -16.76189 | -56.73917 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 54e100c6-435e-3d76-a83f-5fd2e2e65644 | -16.75647 | -56.73669 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 515e2ced-17b6-36f1-aac7-8569a09ba791 | -17.18386 | -56.73997 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.5 |
| ad1bf9b2-b53d-3110-b93c-a8d8753dab17 | -17.18351 | -56.73687 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.3 |
| b3644807-e203-39ea-b974-3708c9b0f4b3 | -17.16829 | -56.78593 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.4 |
| 0079bfb0-610e-3867-8bf5-2b7bd21079f0 | -17.16795 | -56.78281 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.7 |
| ce304163-7cf0-3727-9c3e-9b979a7f19fd | -17.07656 | -56.87465 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| af080718-1630-30fe-a458-12dad5589e0c | -17.07177 | -56.87836 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f6511586-3b95-3f36-ade3-8872aec029a0 | -17.07141 | -56.8752 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e7bd3eb4-0df9-3494-8ed9-be8bbb8d1edb | -17.0433 | -56.85606 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 34fb41d9-2b0d-393e-84ab-2d4667747cb2 | -17.04075 | -56.85688 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 257ee8db-fc85-325f-b983-0c98918f4aa5 | -17.03817 | -56.85664 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7e6b8f7b-069a-3401-b79f-22e50b1029cf | -17.03562 | -56.85746 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2fbce8f6-6ff0-3374-bb29-11d18ddb1763 | -17.02536 | -56.85861 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| d3b1702b-775b-3fc4-b135-dc6a82f2d95e | -17.02023 | -56.85919 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| e8980c71-3e8b-33a1-809c-ee173e58e8d6 | -17.01438 | -56.85353 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| c573580c-dcc6-3535-9811-97ece4efd67c | -17.01402 | -56.85038 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| d64556d2-44d7-3c64-bf03-4c7e7c4ee313 | -17.01366 | -56.84724 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 9e5c2762-ee2d-34a7-a54e-c1016f39654d | -16.97496 | -56.82623 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 40e6f717-f269-3832-917c-7c3626c21e3f | -16.96984 | -56.8268 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| e150b914-b922-3fa5-bc57-23f613d56f6a | -16.96472 | -56.82739 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| c13f6d40-1a3d-3a57-a135-d4c87955dfa1 | -16.96437 | -56.82427 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| e0e8fb53-f074-3c8b-8ba3-eb11a8b952ec | -16.95926 | -56.82486 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 46e79281-d9ef-3c4c-beba-c0d65ee52c2a | -17.70878 | -57.48843 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 46fc7163-001a-3b95-9ed7-595f55a55ebb | -17.70262 | -57.48192 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 1457ce52-67d4-3659-8cda-8fd6b0556182 | -17.69723 | -57.48249 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 5ff17dd2-6b97-3594-8afb-7d791d03d8f1 | -17.69684 | -57.47894 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 5ffeb1e9-416f-3397-9bab-c2d9dac7e6a5 | -17.69145 | -57.47952 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| f30fb379-8493-3808-bc26-b88b4eaf5d68 | -17.69107 | -57.47598 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| f3734c21-7604-36d3-a576-5e6ccacc8cfb | -17.68029 | -57.47715 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 162.4 |
| 20c32d47-4516-3f59-a87e-4963606f39e6 | -17.67991 | -57.47362 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 8632a0fc-b833-3177-a831-e87ecd34f3d0 | -17.6749 | -57.47773 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 162.4 |
| 28858c21-083e-318a-ad7a-cf5210cebf4f | -17.66502 | -57.43599 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 61dd7243-36a1-3f1d-bb52-8dc82e4c9aeb | -17.66427 | -57.42896 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 8b81e09b-b9c3-3a33-b489-fa2675761524 | -17.66352 | -57.42193 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 83da27cf-82fa-3963-a857-894872f7b525 | -17.66187 | -57.45768 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| bfd0d9a0-800f-3850-9a0a-e9b1a91a0761 | -17.66039 | -57.4436 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 7c5f9d9b-728a-3fb7-8e0c-ad2cf57fb673 | -17.66002 | -57.44009 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| fb96e884-a73f-3f86-a6e4-0132d194c020 | -17.31135 | -57.47033 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 63e42320-1cb0-3331-9318-47ded55c6e42 | -17.26424 | -57.51564 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 49f07cd8-7a10-3c3f-b10d-5a285415aa4d | -17.26386 | -57.51213 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| cdbaf7b5-1cdd-35d2-8934-ac031c933411 | -17.25886 | -57.51622 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| d4efea41-04e9-3b01-9c17-4bf467edde41 | -17.25235 | -57.50629 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 0a1291c8-5c65-38c2-b166-e73e20c67db0 | -17.2516 | -57.49929 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 21335a25-ec75-3f75-9e91-95fecb4659a8 | -17.25122 | -57.49579 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 13ce46f0-240b-3c0a-8113-c40b95af1a22 | -17.24623 | -57.49987 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7ca4bd37-6075-3fba-9851-e01dbcb132fc | -17.81697 | -57.50599 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 4a31b268-5f9b-3e51-82ff-831bf3d30a16 | -17.81194 | -57.51014 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 1bc60108-7265-3973-904a-233964e77bd9 | -17.78451 | -57.50946 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.4 |
| a22775ba-5ac2-3dd0-9228-281ebcffc3fc | -17.78413 | -57.50591 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| d8f525be-8458-3a6f-a402-ca271accca80 | -17.78409 | -57.35254 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.7 |
| d781ab53-3f7c-349c-b0c1-5961c82bee6b | -17.77948 | -57.51361 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 6521d2bc-2092-3ca5-b0ed-d6cddb5bf383 | -17.7791 | -57.51005 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 4f286463-05f1-3e69-a3f6-adc0287f2cf7 | -17.76604 | -57.48985 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| e2c22d7b-88f2-3e0c-9c58-1ec430a9dc42 | -17.76527 | -57.3793 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 05d398a1-7da5-3480-9fcd-475be494435c | -17.76176 | -57.50111 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| d4b1051a-7569-3bcf-8b1e-ff6c17c4a986 | -17.76139 | -57.49755 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 90b5a526-7999-3e00-b124-51382ea158f2 | -17.76092 | -57.51527 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.5 |
| 31248dc5-447a-3f0f-91a5-06d7b358c710 | -17.75991 | -57.37989 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 34605001-4f4a-3256-a7fb-4126d548930f | -17.75933 | -57.50102 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.8 |
| 6320c0b1-dc94-3db0-9006-924caf11d02c | -17.75314 | -57.49448 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 94c02524-86e9-3d12-a649-f35d7e9c7fa4 | -17.75021 | -57.49516 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 179f7725-3f43-3680-b3bf-075d02220d19 | -17.74518 | -57.49931 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 414f6e5b-4eac-36b8-acf0-7cdcaacaeced | -17.74273 | -57.49918 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 133.0 |
| 63d41deb-a3f0-3a57-ab05-27c5d6c15a75 | -17.74234 | -57.49562 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 7477ffc7-20b1-303b-b9d3-41d2cd782957 | -17.74194 | -57.49208 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 90007bc4-5a97-3a1c-8825-15fbf88cbb35 | -17.74155 | -57.48853 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| e40c3d7c-3885-366b-b07b-e0e702aeff08 | -17.74051 | -57.50702 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 160.8 |
| 23e42f42-8d19-3e0a-a6b0-47eb90004b76 | -17.74014 | -57.50346 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 37ad30ba-19bd-3cbe-bc3f-ba49586ff420 | -17.73977 | -57.49989 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 26f1d794-927f-3a01-995f-e073dac3ffb1 | -17.73941 | -57.49633 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.5 |
| c5fdca1e-b96e-34a2-b017-2871e2aa0a1f | -17.73904 | -57.49277 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.5 |
| c3a78f5b-695a-3ba9-8b3e-d5bf03611ec4 | -17.73867 | -57.48922 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 0144c31f-897b-3026-8b06-fe26b27b96bb | -17.73811 | -57.50687 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| a830b879-ac6e-30fe-95c9-10993428150c | -17.73772 | -57.50331 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| c06df28f-67b0-36b0-9476-d94251a9ca84 | -17.73721 | -57.47503 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| b0daeabe-7af3-3399-bfaa-6024349a610c | -17.73693 | -57.49619 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 0a91cf3e-bbe5-3ceb-9a42-8d0865adf0f1 | -17.73459 | -57.47492 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 67681f47-4d96-3d12-8b12-b1ff8bc2eae2 | -17.73115 | -57.49322 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 27f64868-6aad-348f-bae0-c51033307197 | -17.73076 | -57.48967 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.3 |
| 82901873-11f7-3c10-beb3-c449af53679f | -17.703 | -57.48545 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| d633f213-909e-3d85-aa5a-cbaa4ae2f48d | -17.69646 | -57.47541 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| f71e15de-7483-309e-9f7b-dc32ab5e02b8 | -17.68968 | -57.36256 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 7412b7cb-6ff3-3cd5-8572-5393c33aea60 | -17.68666 | -57.33481 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| b0f021fe-11e6-313f-b32f-7f56e0c3e4c0 | -17.68568 | -57.47656 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |


[Clique aqui para ver as próximas entradas](README137.md)
