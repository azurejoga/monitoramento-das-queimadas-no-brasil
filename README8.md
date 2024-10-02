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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91cabdd1-5e34-32ca-b79e-b750d62258dd | -17.060499 | -56.061298 | 2024-10-02 00:30:04 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dfe0c4ce-f820-3b3c-bafe-b39dda231cd1 | -17.1078 | -56.643501 | 2024-10-02 00:30:04 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e5f4e9c-caf4-38f1-8478-dfc3991c3b46 | -17.0982 | -56.6451 | 2024-10-02 00:30:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c420792e-1b53-34c7-84a1-f4c874e2ef3e | -17.1029 | -56.673698 | 2024-10-02 00:30:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2bfdf099-843b-345d-b3ca-29bc84955104 | -17.088499 | -56.646801 | 2024-10-02 00:30:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5b35c7b8-15e5-3ed3-9ecc-bab552e133df | -17.093201 | -56.6754 | 2024-10-02 00:30:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 72975953-6f89-36f5-bca4-78b4595ba18f | -17.0979 | -56.704201 | 2024-10-02 00:30:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 13a2e4e8-fbe6-375a-be66-bc800c72dc88 | -17.0788 | -56.648499 | 2024-10-02 00:30:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 44c3da3f-8dc5-34f6-ab91-f37e9b808892 | -17.0835 | -56.677101 | 2024-10-02 00:30:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb4f5718-ab09-369b-b546-a9ae66e66e12 | -17.0882 | -56.705898 | 2024-10-02 00:30:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eead9068-99cc-333c-a5e0-db9c936acd21 | -17.069201 | -56.650101 | 2024-10-02 00:30:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aae04673-877d-3bda-bc21-e8312128ed13 | -17.059299 | -56.710899 | 2024-10-02 00:30:05 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bd5b55cf-5f1b-3260-8002-12c98588bcc3 | -16.8613 | -55.885201 | 2024-10-02 00:30:06 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cd185d08-b69d-3a0e-9f95-f25e182770f1 | -17.044901 | -56.6838 | 2024-10-02 00:30:06 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11873314-b116-31f6-a268-8987559ec6bc | -17.0497 | -56.712601 | 2024-10-02 00:30:06 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9f0a742-178b-332a-b499-0ebb8d9bac5c | -16.8776 | -55.804901 | 2024-10-02 00:30:06 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 77748f7f-8f03-35ce-8def-70fb7798d9f6 | -16.863701 | -55.781799 | 2024-10-02 00:30:06 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ffad39b6-d1a0-3a54-91fa-91e1c0b34564 | -16.867901 | -55.806599 | 2024-10-02 00:30:06 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81832aa1-88ce-3b8c-af09-33c5a5a1c458 | -16.880699 | -55.881901 | 2024-10-02 00:30:06 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ff2f7aac-dc12-3735-bb0f-cb98f397f282 | -16.854 | -55.783501 | 2024-10-02 00:30:06 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8fc81483-c33e-30a5-9ba9-0c2ac61b22c3 | -16.8582 | -55.8083 | 2024-10-02 00:30:06 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e3ff291f-e1a6-39f9-b9f8-594692f5b28f | -16.866699 | -55.858398 | 2024-10-02 00:30:06 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1ab72e6-c021-3f2d-9f12-31bfd6a6e0f0 | -16.871 | -55.883499 | 2024-10-02 00:30:06 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| af7b3051-d89b-31f8-8435-a346b9092727 | -16.875299 | -55.908798 | 2024-10-02 00:30:06 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c5cfc4dd-63f9-3a00-b1d2-9e078a8ac6ab | -16.8528 | -55.834999 | 2024-10-02 00:30:06 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9a33f6d-5363-3c59-a8dc-8cd9528bc8c3 | -16.857 | -55.8601 | 2024-10-02 00:30:06 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d463d23d-8c52-3f73-b5d3-456f61b631dc | -16.8431 | -55.8368 | 2024-10-02 00:30:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8e8ec254-970f-3a73-9bee-f6c408234234 | -16.8473 | -55.861801 | 2024-10-02 00:30:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c246945-ed9f-3d59-b102-d2dd549a843a | -16.833401 | -55.838501 | 2024-10-02 00:30:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| abb70854-cde1-3ac4-83a3-d61e34ae8821 | -16.8377 | -55.863499 | 2024-10-02 00:30:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fe41be0c-d73d-3fa8-ae46-812ae9f5b183 | -16.8419 | -55.888699 | 2024-10-02 00:30:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 50d198de-2863-361b-bda5-86a13b788593 | -16.8237 | -55.840199 | 2024-10-02 00:30:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 41bf5d49-8eb1-334a-b92f-16aab7ce60af | -16.827999 | -55.8652 | 2024-10-02 00:30:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84919343-c054-3bc6-b050-1bf59c19498e | -16.832199 | -55.8904 | 2024-10-02 00:30:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 55c592fc-e61f-36bc-bdaf-4bc1e0e9dcef | -16.813999 | -55.8419 | 2024-10-02 00:30:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 90913201-bc9e-3863-a8fd-0ac0a8f456d3 | -16.8183 | -55.867001 | 2024-10-02 00:30:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4ff1adc8-5b5f-3e16-9d0b-bbc6de9817c0 | -16.822599 | -55.8922 | 2024-10-02 00:30:07 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3b402a01-c6d0-3628-80d8-cd53a7442b91 | -14.5658 | -44.810398 | 2024-10-02 00:30:08 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8db8bfad-b468-35e3-b95c-b89a9759ec89 | -14.5675 | -44.8176 | 2024-10-02 00:30:08 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 430378f7-abe3-3566-811f-936b6dbc035c | -14.5691 | -44.824699 | 2024-10-02 00:30:08 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b68d9569-c76c-3307-83c7-606c319fcdfa | -14.5577 | -44.819901 | 2024-10-02 00:30:08 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e5a9f930-c339-3a10-a893-8a899a918ccd | -14.5593 | -44.827 | 2024-10-02 00:30:08 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d70b3d8d-383b-3b6b-a9d7-f81c00809731 | -14.5609 | -44.834202 | 2024-10-02 00:30:08 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a1ccb944-4198-3ed3-820b-177a7937a970 | -15.206 | -47.935001 | 2024-10-02 00:30:09 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 236de37a-1e01-3dfe-bfd8-5decc7306c9e | -15.2077 | -47.942902 | 2024-10-02 00:30:09 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ea2940a8-7c81-3aac-a1e2-1047d4f44dad | -15.1962 | -47.937199 | 2024-10-02 00:30:09 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be0c1a06-bda0-3fcd-a84d-35e77252625e | -15.1979 | -47.945 | 2024-10-02 00:30:09 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5f6c6147-2dc0-34bf-9d4e-e48d01e2b933 | -16.663401 | -55.8946 | 2024-10-02 00:30:10 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11bdae9d-9f3c-3302-a6eb-f0821de60053 | -16.6537 | -55.896301 | 2024-10-02 00:30:10 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b51890f4-92a1-325b-9a43-26f9271d14d8 | -16.6397 | -55.873001 | 2024-10-02 00:30:10 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 791b3a37-45d2-32a3-9fb3-4ee465589f3f | -16.643999 | -55.897999 | 2024-10-02 00:30:10 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 10290dde-165a-360a-84e8-b8b3fd06899b | -16.634399 | -55.8997 | 2024-10-02 00:30:10 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 234edbb8-915e-385d-951b-722c25bc174d | -16.624701 | -55.901501 | 2024-10-02 00:30:10 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3064fea5-d5f5-321e-9159-92860e3b9c53 | -14.6463 | -45.910099 | 2024-10-02 00:30:11 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d68d31e3-c435-3e64-8830-b8636e1adfe8 | -14.6479 | -45.917198 | 2024-10-02 00:30:11 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bd5f27d4-1af7-3850-8b78-699e6ebb69f2 | -14.4989 | -45.246399 | 2024-10-02 00:30:11 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a15ce15d-5b48-3aff-ba9c-cdec3741909a | -16.901699 | -57.626701 | 2024-10-02 00:30:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d1b0202a-d984-3412-b9d5-98dcc3f558d8 | -16.907101 | -57.659901 | 2024-10-02 00:30:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c488566f-21e2-38be-8fe0-00b30bf73060 | -16.892099 | -57.6283 | 2024-10-02 00:30:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac2c25a9-0b88-3915-b578-df471ce3ea6c | -16.8974 | -57.661499 | 2024-10-02 00:30:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 106d2f9d-0376-38ee-bb80-3f545e9282ff | -16.882401 | -57.629902 | 2024-10-02 00:30:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 78a821fd-a263-36c8-b49e-ada8b1fd9d98 | -16.8878 | -57.663101 | 2024-10-02 00:30:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 855e0b2e-2f9d-3cd8-8613-ed61352f428e | -16.7817 | -57.315701 | 2024-10-02 00:30:12 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 171c253e-e7d5-373e-bbda-1b40ea4a8e38 | -16.1094 | -53.501598 | 2024-10-02 00:30:12 | METOP-B | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a04102a9-5bc1-335e-82fa-04ab7789c793 | -16.112499 | -53.5186 | 2024-10-02 00:30:12 | METOP-B | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d255c2bd-ea2c-3c70-9d18-0e3a56771183 | -16.7721 | -57.317299 | 2024-10-02 00:30:12 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0acfe9fd-fabc-37a1-8bb7-dc0f6d207405 | -16.777201 | -57.348801 | 2024-10-02 00:30:12 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a684e084-fae1-3db2-9d98-7776aa749f24 | -16.7624 | -57.319 | 2024-10-02 00:30:12 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 753106fc-8628-316c-a1e8-bd655d917f7a | -16.767599 | -57.350498 | 2024-10-02 00:30:12 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f38dcde8-2da7-3bcf-94f8-9c72a843a68a | -14.4366 | -45.7066 | 2024-10-02 00:30:13 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1766299-f091-33ae-a1d8-24d3f2946ca5 | -14.4381 | -45.713699 | 2024-10-02 00:30:13 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d7d08f02-10ab-3574-91a7-0588c80723a7 | -16.743799 | -57.3871 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bd7c6c68-f3dc-3ed2-b053-4a40cad51a26 | -16.749001 | -57.4189 | 2024-10-02 00:30:13 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ba1b86ad-ec95-34c9-8e53-d84a6e31f008 | -16.6933 | -57.1399 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 71e3bd1c-7fbe-3237-a56e-d6785af25a00 | -16.729 | -57.356998 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 44697035-370b-34b5-8b23-0c8a32177870 | -16.7342 | -57.388699 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00c7d745-ab25-322e-ac9d-e07515364cb3 | -16.6786 | -57.111198 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e3bb97ab-24aa-3433-b266-790da17b7d91 | -16.683599 | -57.141602 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 75729ab1-9d54-3c89-a38d-a71da95b180d | -16.6887 | -57.1721 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bab607bc-e9ac-373f-a539-37b02291c3f7 | -16.7194 | -57.3587 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b103a725-9d51-3d66-9f5d-db125bbda2f2 | -16.7246 | -57.390301 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6ec7b33-06e1-394e-9a49-71493451cda1 | -16.674 | -57.143299 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 524de37c-a6e5-3b1b-a770-3ae9634e6605 | -16.679001 | -57.173801 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5f2d92d7-0072-33a3-b9ff-6cd53333f3d5 | -16.6994 | -57.297501 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7ee864b3-67c2-3847-ac2a-dcbbe749659c | -16.664301 | -57.144901 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aa9bffc6-f7cb-3756-a89b-166c3f3a9920 | -16.669399 | -57.175499 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8acf3082-8ee1-398b-8159-89050a927fd7 | -16.6898 | -57.299198 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e44ffb8-09aa-3bbe-b690-c898d93c5687 | -16.694901 | -57.330502 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 593991ed-5fe2-3543-9c57-da8b2101b7cd | -16.654699 | -57.146599 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0d0090df-1f42-366a-bd1d-fab501091a79 | -16.680099 | -57.3009 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 17f923dd-a5ec-3aaa-9a98-408eebf9786d | -16.6852 | -57.332199 | 2024-10-02 00:30:13 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 44355c55-5030-3329-9366-e801317cb1af | -16.6161 | -57.153198 | 2024-10-02 00:30:14 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e55d12e2-fd80-32b0-9800-ccd00f2d89c7 | -16.621099 | -57.1838 | 2024-10-02 00:30:14 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1b86a450-f078-34e3-a912-4002089e0bd5 | -16.6064 | -57.1549 | 2024-10-02 00:30:14 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 348b26d1-d89f-3a03-b7e4-47366fa51213 | -16.6115 | -57.185398 | 2024-10-02 00:30:14 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b3dd5a9b-6a92-377a-bde5-c6086a618bfe | -16.6166 | -57.216099 | 2024-10-02 00:30:14 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dea2a40f-2936-3e05-ac45-4a3482cbb99c | -16.626801 | -57.278 | 2024-10-02 00:30:14 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fc7a3054-8da1-367a-bb43-bbc8930295d3 | -16.601801 | -57.187099 | 2024-10-02 00:30:14 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5b0ee637-5238-387f-9b42-c635c0b79b22 | -16.6171 | -57.279598 | 2024-10-02 00:30:14 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 93b8aaf6-af81-3853-9cc9-8f8561746457 | -15.1347 | -49.567402 | 2024-10-02 00:30:15 | METOP-B | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
