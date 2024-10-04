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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c0d5c82-36d7-3181-9ce7-27fae57895c6 | -5.31205 | -44.86039 | 2024-10-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad822279-d7b8-348e-9456-8dd438b533af | -7.84856 | -45.35587 | 2024-10-04 04:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ef68435-afbb-3bac-aa05-7113cdbcf68d | -7.84811 | -45.35917 | 2024-10-04 04:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f680455-878c-3d76-9419-ff0bb985fefe | -7.39851 | -45.19968 | 2024-10-04 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29427c1f-68d0-3e4b-8b94-a24c91f91b42 | -6.61405 | -45.03733 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d5d96f4-a11b-3878-88e5-6e195d272ad9 | -6.60872 | -45.03649 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4cc993aa-ae42-3a48-a403-9a7ecbeaf948 | -6.51899 | -44.50393 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b07cc580-d7df-3a0e-a71a-aa27b4352181 | -8.29725 | -45.4807 | 2024-10-04 04:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 917e5025-691d-31bb-96b4-cba884fc3ee7 | -8.29295 | -45.47259 | 2024-10-04 04:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae909548-aa68-3656-94e7-93f4b47cf73d | -7.85658 | -45.33656 | 2024-10-04 04:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52a50578-042e-39d1-9d2b-18f7c187f322 | -7.85387 | -45.35659 | 2024-10-04 04:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| dd19a9e8-a27b-3abb-a859-b8203275987e | -7.85343 | -45.3599 | 2024-10-04 04:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 97df01eb-d2cf-32b2-bf3c-4fd765d9f615 | -7.85299 | -45.36317 | 2024-10-04 04:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f2fd3e16-fee5-3d65-9199-d1280bbe4d7b | -8.12308 | -44.81606 | 2024-10-04 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d04515ec-3f0d-35b6-b4f3-091e6b8715bc | -8.2934 | -45.46931 | 2024-10-04 04:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa9e65d6-6847-3c40-9e30-86f83ebcec90 | -8.6827 | -45.26231 | 2024-10-04 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f09abaa5-d1de-3f9b-a28d-1fb4c85b9870 | -8.68054 | -45.26143 | 2024-10-04 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c274b4e6-8657-3cf7-a86c-8a80f7b98d22 | -8.68009 | -45.26472 | 2024-10-04 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 094a0722-db83-37e3-b376-6905b4a5e3dd | -8.67726 | -45.26175 | 2024-10-04 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1326ad33-bd66-34f4-a59f-c3dab6f45ac8 | -8.29773 | -45.47721 | 2024-10-04 04:55:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f70de416-5a0b-31a7-8c3e-4348eb7bd802 | -10.8096 | -45.6151 | 2024-10-04 04:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52a0d8cb-e311-37dc-b469-98cfba6369d0 | -10.80505 | -45.60721 | 2024-10-04 04:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90f0956f-bf00-3e0b-9bb6-22c7c09bafaa | -10.8046 | -45.6108 | 2024-10-04 04:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c28bcaaf-5178-3e83-b1fe-be8bd6e48956 | -10.80415 | -45.61438 | 2024-10-04 04:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62fec737-eef2-3164-95fc-881e845ac996 | -10.8001 | -45.60257 | 2024-10-04 04:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c9b0e70-8ed9-39ff-9c1f-74904a311ca5 | -10.79961 | -45.60645 | 2024-10-04 04:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cffaed91-ee69-30f2-a45b-51c1aea7444a | -5.00426 | -45.49055 | 2024-10-04 04:55:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de874c21-40ae-3d8d-8abe-fa5f3c1ba3f2 | -5.00382 | -45.49358 | 2024-10-04 04:55:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca823efe-3200-33db-9a30-5e9206495f1b | -4.69288 | -45.86833 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff012950-7b6f-37ba-a2cb-282c0f1024b9 | -4.69205 | -45.87399 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b2a4ba2-afd2-3f6b-9edb-590ecd58c01f | -4.68797 | -45.86771 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 704e450d-a4e8-3914-9317-69dd7b9d7571 | -4.68714 | -45.87339 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09feb1f8-b224-31f8-b15e-808e618d670d | -4.68633 | -45.87892 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac89e55e-a708-3c79-af62-c9a08109e381 | -4.68309 | -45.86686 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 809f792e-7b2d-367b-9a29-5bbd8f989a71 | -4.68229 | -45.8724 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 744ad1bc-9857-3497-84d1-2e85aaab4614 | -4.68144 | -45.87819 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce220129-4278-309b-8c44-89f22c96af9d | -4.67821 | -45.8661 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7234be74-a6cf-39f5-a0a7-5f19aee8254d | -4.67743 | -45.87139 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96e2028a-1065-3c4e-b8f2-115cea955d5a | -4.59759 | -45.75193 | 2024-10-04 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f07a15bc-1ccf-3f09-ae65-47c33073f660 | -5.97613 | -45.38116 | 2024-10-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7083c620-31f5-3594-9cbb-4e7f24f319bc | -5.97143 | -45.37724 | 2024-10-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3dc3ef9-b394-3a8c-a297-cb0952412e40 | -5.97098 | -45.38034 | 2024-10-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68e56578-8fbd-3117-8c29-edb54531b48f | -5.97054 | -45.38342 | 2024-10-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4fe232b2-c7e8-3f1e-8e45-6b414aa9b39b | -5.97009 | -45.38651 | 2024-10-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 639a1949-7d7b-36fb-9628-6adfaf332805 | -5.96584 | -45.37949 | 2024-10-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96641c15-b08f-3723-a717-612023bf5ed0 | -5.96539 | -45.38261 | 2024-10-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d0fd22b8-b8d5-3546-992f-6aa25bfd579d | -5.96494 | -45.38572 | 2024-10-04 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9e6681e5-966d-30a6-bda2-9614ee459b6e | -5.79371 | -45.08611 | 2024-10-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b633fdbf-2083-311e-9f13-6070f189e345 | -5.79325 | -45.08926 | 2024-10-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 257b4b00-9033-3243-9255-c02adf9c01f4 | -5.79279 | -45.09243 | 2024-10-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36cea411-45d6-3d45-be4f-eb01fdfd0043 | -5.78799 | -45.08857 | 2024-10-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84c0a6a3-1a7d-33ed-8354-2a1e6bf68ee7 | -5.78753 | -45.09179 | 2024-10-04 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fcaa3e5-41c4-3a8e-b544-64043098652e | -5.10805 | -46.13883 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 084ff49f-cc0e-35ac-be0b-8ace30975568 | -5.10731 | -46.14386 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee0b7814-f16b-30dc-b7d9-301169d66671 | -5.10248 | -46.1431 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 954b5503-f53f-3a78-b273-b1b2d1af63cf | -5.09109 | -46.11977 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec869fc1-fb9c-3d2f-bf69-b3a54b3fb766 | -5.08628 | -46.11889 | 2024-10-04 04:55:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e833bfca-feb5-3252-aab6-7eab2f6fc1aa | -7.62572 | -45.5399 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 78326957-33e7-3719-932c-443da3e6e36a | -7.62526 | -45.54329 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a916f9a-4e8f-3f7e-a956-10b47c84e332 | -7.6248 | -45.54662 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3a8ca44-e8c8-369d-884a-020ee04d35cd | -7.62435 | -45.54987 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75f758be-9112-3d71-9030-0b8fa57edfca | -7.62391 | -45.55311 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d0b0c05-5f98-31ea-be91-d7aeb512a6ff | -7.62095 | -45.53576 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e30e588c-813a-3691-889d-bd7d2491c5d5 | -7.6205 | -45.53911 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| be9912d2-cffc-3722-80d0-97b34d239a0b | -7.62004 | -45.54243 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e83f81b6-2335-3d98-8f0e-34f40558091e | -7.61959 | -45.54572 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1215813-ebe4-3610-9e92-ada03d61242d | -7.61915 | -45.54897 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 463043d8-948f-3beb-a7e3-1816ff019f3f | -7.61871 | -45.5522 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fee8a92-933a-3635-b597-c6b0854b3b70 | -7.61666 | -45.52817 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e27dbbe-8299-3e47-81ba-8ed648058772 | -7.61574 | -45.53489 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 445e0d2e-376a-3df8-b9e3-27c4e79ca900 | -7.61528 | -45.53823 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| db3aaef9-a99c-3060-ba61-e9a5c3cd56d5 | -7.61484 | -45.5415 | 2024-10-04 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f6c6b8cd-dc7a-30cb-8127-f91b6f7a035d | -7.22112 | -45.59833 | 2024-10-04 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 02df131c-08d1-3634-acb7-7996ad233a06 | -7.22068 | -45.60143 | 2024-10-04 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4fd4ecc3-1343-316c-86f2-95abad88d5a1 | -6.76368 | -45.65293 | 2024-10-04 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5115113-eb3c-3752-baef-5c02142db7b3 | -6.75856 | -45.65216 | 2024-10-04 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0087c93-6f08-373c-b0db-e7f7f5553a17 | -6.62055 | -45.79648 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0860dde2-dc81-3e72-a8c4-857b231d7d4a | -6.61549 | -45.79573 | 2024-10-04 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc9f6331-ce0f-3163-acbd-dfb602b29ee9 | -7.76572 | -46.15456 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7ee9226f-a97b-3ae6-bef1-95546cd581fd | -7.76533 | -46.15738 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29e7e9d0-14e9-35e5-8632-2adbba9c89e1 | -7.76067 | -46.15401 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 829b4053-2f0f-3c78-b819-e5e077879fc6 | -7.76027 | -46.15686 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c4b05d7-fa18-3269-8257-7612c8b1c96a | -7.75524 | -46.15623 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f98bd8a7-6ed0-3ae9-b936-9ea343a51902 | -7.75064 | -46.15242 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bb9a45f-da61-337b-b985-26b126f5ae66 | -7.75023 | -46.15541 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbb6fc98-8629-3b4e-9838-97fffe7ab456 | -7.74563 | -46.15157 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99c93199-047e-3d44-93d7-4ff6e905e1f1 | -7.70479 | -46.15199 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 823a73fb-3ae3-342a-9d52-4f1bbdf91eee | -7.70437 | -46.15493 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d231bc32-c053-353a-b999-2200d6d93de2 | -7.70437 | -46.15372 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 070d124a-e9d6-3823-8318-9affe1055ecd | -7.69936 | -46.15289 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55d27725-be90-3306-ac26-86b72f25d055 | -7.69897 | -46.15582 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 367f3007-4bc4-38a5-be0c-7c682bf25388 | -7.69895 | -46.15701 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37995b35-8f7e-3e8d-bd7d-737026d5a07c | -7.69859 | -46.1587 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c516ab61-5a36-3944-81bf-f59a47605f9b | -7.69855 | -46.15988 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1327cddd-69ed-3327-aab9-ea94209334aa | -7.69707 | -46.16999 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2db023f5-b046-323e-ad64-2e44595c76f4 | -7.69695 | -46.17113 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96d41286-ed29-330c-b34e-2d255c3f607b | -7.69669 | -46.17286 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 491b2ccb-6390-3547-b32e-c98e7fc81d89 | -7.69654 | -46.17403 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0108270d-ef0d-3186-8594-2660c671d7b2 | -7.69396 | -46.15498 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90dd7d63-992d-37af-bda6-c9bd8c944b44 | -7.69395 | -46.15621 | 2024-10-04 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README140.md)
