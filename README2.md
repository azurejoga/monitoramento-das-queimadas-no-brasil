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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3e83168-beb3-3edc-8441-99de8f6805b9 | -22.40083 | -47.15951 | 2025-09-16 01:07:00 | TERRA_M-M | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 240dd3ab-efb9-3f70-bf9c-c8b1e4430521 | -14.90991 | -51.65645 | 2025-09-16 01:09:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 9fb5add8-d299-35a6-a49d-9755e2131752 | -11.2412 | -49.96196 | 2025-09-16 01:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 20b2188c-c6d4-3746-b7a5-6de6965ca7bc | -11.23729 | -49.93789 | 2025-09-16 01:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 44943ca8-e8e6-338b-b0c9-22fde6ee0f13 | -14.90744 | -51.64099 | 2025-09-16 01:09:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 98f78fb2-b340-3523-b11b-9d361421199c | -16.07289 | -59.4253 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 6537e202-56df-3e55-904a-e9b51eefae21 | -15.99974 | -59.25929 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 80ef5d39-0a53-3f88-98ca-228ec0807989 | -14.91972 | -51.64905 | 2025-09-16 01:09:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 44.1 |
| aae7c648-6d89-3f17-a9f6-514c99cdd861 | -16.06301 | -59.4258 | 2025-09-16 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 52bee32c-bcbb-335c-b949-433c20f551a6 | -16.00799 | -59.24692 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 40884160-c174-3024-8513-7dcc3f0118af | -16.47815 | -55.11457 | 2025-09-16 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 422d873b-7550-366a-9e16-6ada7dbced0a | -11.84787 | -57.05561 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 482518f8-5670-3c7e-92af-b7f99442d229 | -15.80584 | -53.4554 | 2025-09-16 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 42c188a4-5a6f-3884-9b2d-c4dca2426088 | -16.02158 | -59.25048 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 175cdcb1-8372-3059-a499-cd5fcb9ad768 | -16.00109 | -59.26994 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| eabfddfa-566f-3d97-bed5-f397d830030d | -19.73631 | -47.35351 | 2025-09-16 01:09:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 41.8 |
| be50c056-a816-3989-bf8f-76e688be5f7f | -14.84844 | -51.63547 | 2025-09-16 01:09:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 120.6 |
| cf4fbd52-9f45-3ede-a8df-38203457aeaa | -14.36025 | -52.92509 | 2025-09-16 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7f5df64a-d2eb-3734-a554-d905434733a7 | -16.00938 | -59.25784 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 20eb0474-ccd6-3270-a559-bcc7bea49491 | -18.90221 | -49.57142 | 2025-09-16 01:09:00 | TERRA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| dad59ab5-fe1e-3d4a-8310-b0c6ff57d7ab | -16.71205 | -54.94759 | 2025-09-16 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bf73a1c8-426b-3580-8aa2-7a77065d1c7d | -19.88533 | -48.34903 | 2025-09-16 01:09:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a3755172-c037-3e7f-8043-e7ecd643fbf5 | -10.78877 | -50.67886 | 2025-09-16 01:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ddc983ce-3fba-309a-9189-590cdafdab89 | -15.87582 | -59.39592 | 2025-09-16 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 5f5a0709-17f4-34b1-99a0-33ac0d27f847 | -11.44871 | -46.92617 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| b1f25f34-5981-3d8c-bd82-5704cc941c8a | -10.79242 | -50.6848 | 2025-09-16 01:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 9e29ca42-6b6a-329d-9d7b-cc49915f97e3 | -14.92363 | -51.66988 | 2025-09-16 01:09:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 549b6ebd-118a-3ff0-97c0-63df0a602edb | -14.92228 | -51.66445 | 2025-09-16 01:09:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| a7c76c10-5aef-3e4a-9d75-6a0b050e7666 | -16.02299 | -59.26191 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 2adcc5f4-cedb-30b4-9056-6628d986c526 | -12.76841 | -47.95002 | 2025-09-16 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 48382e40-b2c1-36ef-82a7-4c06daa501f7 | -11.41686 | -47.76615 | 2025-09-16 01:09:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 004005a3-12c9-3c5d-97c4-2661d4d8c27d | -15.79608 | -53.45715 | 2025-09-16 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| adc0c0d7-8dba-3572-8326-1c585f3aa3a6 | -16.01904 | -59.25648 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 1b6fcfaa-a19f-3940-a130-ccde86f4cd61 | -14.93354 | -51.66247 | 2025-09-16 01:09:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ffa25757-1f1a-3796-9389-b1e61a57f265 | -16.70582 | -54.96831 | 2025-09-16 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3dd2c815-320a-33cc-a80a-9c6d16c98311 | -16.07142 | -59.41356 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b67636b6-79a1-3313-a682-bed0cac61665 | -16.47675 | -55.10501 | 2025-09-16 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 23e9680b-f359-3d9e-b2dc-7884957ae2ad | -16.47954 | -55.12414 | 2025-09-16 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 50808731-e9b1-3d71-927a-21abf0c3a5cb | -13.20372 | -47.30513 | 2025-09-16 01:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| e9a90adb-4658-31ab-8d37-8afbe3c8fcff | -15.8772 | -59.40704 | 2025-09-16 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 59d3ee96-92c8-3777-84bb-94411cd37ddb | -12.64915 | -47.97818 | 2025-09-16 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| c65f9c6a-526b-3dd8-ad92-a13f7faeea06 | -11.24668 | -49.9544 | 2025-09-16 01:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| c7b12287-c9c9-325b-bf9e-f6fd0d13ad7d | -10.76256 | -50.6678 | 2025-09-16 01:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 300de638-e1b4-34ea-b80c-72351bb54da8 | -18.56067 | -49.27285 | 2025-09-16 01:09:00 | TERRA_M-M | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 2dd1e756-4c14-33cc-988c-289456eb3270 | -10.77924 | -50.68706 | 2025-09-16 01:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 1261e8ee-cef4-3344-80b5-4b63fc54e276 | -14.92118 | -51.65445 | 2025-09-16 01:09:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c19ac176-358b-3ea0-83c4-2e33c965856c | -14.87105 | -51.63148 | 2025-09-16 01:09:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 1f400e1d-c673-31a0-9653-5690928c8ae8 | -15.8386 | -53.47304 | 2025-09-16 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9c584c5a-ea48-350c-bc81-73a97e41c81c | -11.44729 | -46.933 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 818c7676-b53c-3ce0-bdf7-2ebfed44cc08 | -13.75736 | -48.77809 | 2025-09-16 01:09:00 | TERRA_M-M | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 9a6f1267-8647-3fbe-a802-2435a546c356 | -15.78426 | -52.21002 | 2025-09-16 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b55a18ef-fcf2-3bbc-a1b1-3a4f9010903f | -15.8786 | -59.41829 | 2025-09-16 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 38d23f3e-e4a1-37a1-81ab-838c31a5bd0f | -11.34513 | -50.85429 | 2025-09-16 01:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.1 |
| fedf68aa-9ea7-303a-808c-d862b27a680d | -16.70306 | -54.94923 | 2025-09-16 01:09:00 | TERRA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b0f1c22f-6acf-31b1-aa37-bfc0ff0ad689 | -16.48573 | -55.10352 | 2025-09-16 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 06e04bd8-3d8a-3fc5-9264-eadcb03227af | -16.0616 | -59.41442 | 2025-09-16 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 11d61aab-b60c-3ca9-8c93-7881039e8d9e | -10.21337 | -54.30244 | 2025-09-16 01:09:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0b2f1bcd-8034-32cc-9f06-3c36672f4d48 | -14.91237 | -51.67187 | 2025-09-16 01:09:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d23c405a-94bb-39c6-a4f7-8de130ea198b | -12.77455 | -47.98455 | 2025-09-16 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 36b6513f-546c-34b7-a956-ffef85c134f9 | -16.48712 | -55.11307 | 2025-09-16 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| f57c4af1-3fa2-3e40-a945-6e856e606451 | -15.7907 | -52.18189 | 2025-09-16 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d43ceef2-633b-3701-85e9-7bd070e89dfe | -11.41053 | -47.77458 | 2025-09-16 01:09:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 28f6b4de-4578-3a25-897c-7ed31479345a | -15.86882 | -59.41932 | 2025-09-16 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2db14561-2546-3cd8-91d9-3606f414b54f | -14.85975 | -51.63347 | 2025-09-16 01:09:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 89b437c3-df5a-3946-9cf5-d28774016366 | -14.89615 | -51.64299 | 2025-09-16 01:09:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| dfa5aa6b-08f2-3a95-9071-443c525c7344 | -16.01764 | -59.24557 | 2025-09-16 01:09:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| dbce2362-57cb-374a-b551-f1f4fc29f659 | -18.55717 | -49.25284 | 2025-09-16 01:09:00 | TERRA_M-M | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| 0c140692-9535-3c47-a7cc-f4b68480ed58 | -11.34845 | -50.87473 | 2025-09-16 01:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 166496ff-82d2-36a4-bf3d-6ffc457afb54 | -9.8715 | -48.61749 | 2025-09-16 01:09:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| a00e2b0f-e364-3fa7-87b2-a2efb1b96b0b | -16.05328 | -59.42745 | 2025-09-16 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e5b09f21-f3a6-35dd-8b94-f0c67ae38046 | -16.03363 | -59.44743 | 2025-09-16 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f4af086c-a437-39f2-bde0-a447402b0343 | -12.67471 | -47.94009 | 2025-09-16 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 94bdd622-3b91-3fdb-9f90-befa0a418d30 | -15.78708 | -53.52834 | 2025-09-16 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1d5579bd-3ae4-3fca-b3d0-af732978dc52 | -16.00288 | -59.44017 | 2025-09-16 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9eca2a00-405c-3120-a16c-9e654a6fb0b2 | -14.66528 | -52.07214 | 2025-09-16 01:09:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d399fd32-dd66-391e-8ba5-57590f103d92 | -16.00146 | -59.42888 | 2025-09-16 01:09:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| eaeccda9-67a7-396f-8eb1-cd572af9cd59 | -15.6221 | -47.36729 | 2025-09-16 01:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 32d00562-4f8e-3ba6-b935-d63891968054 | -15.82885 | -53.47477 | 2025-09-16 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 499c42ca-b2ac-365e-8017-8f5d9599fa66 | -10.79238 | -50.70029 | 2025-09-16 01:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| cb4f6e4e-410b-374f-b0ad-c1cea11660de | -3.8197 | -41.5739 | 2025-09-16 01:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 516d7bf8-9644-37d2-a5b1-9e80a1bd87cb | -15.8371 | -53.4741 | 2025-09-16 01:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 196d1368-2287-3a6e-8a0d-a16caa3a7964 | -8.5947 | -46.3471 | 2025-09-16 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 293afc1b-3458-3a87-a29d-5536c7256877 | -18.5481 | -49.2392 | 2025-09-16 01:10:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.0 |
| 4ee83097-e95f-3924-98e1-647fc2880b19 | -10.7115 | -46.488 | 2025-09-16 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 90af8664-313b-3b49-b82d-74248df9d1b5 | -3.7401 | -49.0399 | 2025-09-16 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 32d301a6-f2ec-3978-bad1-03bed85344f8 | -18.5676 | -49.2579 | 2025-09-16 01:10:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 413.1 |
| f0d9bdfa-d057-350b-80d5-a7d36f89be00 | -18.5476 | -49.2618 | 2025-09-16 01:10:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 246.1 |
| d6b0e435-2a53-357a-8a4f-d1543d69c968 | -18.5671 | -49.2805 | 2025-09-16 01:10:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.6 |
| d355b14c-fa62-321f-9ace-18656eaa22ad | -7.4503 | -46.1647 | 2025-09-16 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 938ab4fc-db27-3938-9f7b-5cc8f7816835 | -15.8176 | -53.4767 | 2025-09-16 01:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| d2693a01-c6c9-3c97-9e12-013a9bb4e313 | -3.2121 | -47.1138 | 2025-09-16 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 4ef37b15-3293-3e44-a4f8-a5fe09aba37e | -3.8228 | -44.1063 | 2025-09-16 01:10:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| bd75e79e-bb4b-39d0-a177-adcf1570ce31 | -16.0192 | -59.2427 | 2025-09-16 01:10:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 79f13a61-a535-3c1d-be37-d74a743acb61 | -3.8199 | -41.5499 | 2025-09-16 01:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| b1a2b5e5-f320-388c-9285-09d090f9f391 | -15.9998 | -59.2446 | 2025-09-16 01:10:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 72ed0ba2-1cd4-34f8-a46c-86642b37ab18 | -10.7201 | -44.7541 | 2025-09-16 01:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 141.8 |
| c697b44f-63fe-3682-a921-764d929bb831 | -10.7205 | -44.731 | 2025-09-16 01:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 066f83ba-5375-37bd-8699-6cd7fa530e61 | -10.7392 | -44.7515 | 2025-09-16 01:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 5ca7ea9b-3e04-3c17-b185-08a5d769bc71 | -18.5877 | -49.254 | 2025-09-16 01:10:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.5 |
| fbc65e7b-1f02-3645-99f0-e41b66c600e9 | -18.5682 | -49.2352 | 2025-09-16 01:10:00 | GOES-19 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 168.0 |


[Clique aqui para ver as próximas entradas](README3.md)
