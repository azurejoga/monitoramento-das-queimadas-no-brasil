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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e041ce8-da9f-34af-a8a6-5eb28c2700e8 | -4.26553 | -55.1567 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60796469-d204-36e0-bf60-14fc8c33f60e | -4.2649 | -55.16036 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88f3d56c-d674-3df2-bbc2-9d6f2bc71570 | -4.26056 | -55.45183 | 2024-10-11 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61b82789-304e-3a32-bc63-df924cd08905 | -4.08918 | -54.61029 | 2024-10-11 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e612685-e165-37bd-9075-cf4b65e736bc | -3.97489 | -54.09232 | 2024-10-11 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b29465f-754f-3c3e-9e71-a9441dbe8812 | -3.90475 | -54.16876 | 2024-10-11 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeb61a8e-c989-3a22-a121-b51a6ed52457 | -5.39849 | -42.92583 | 2024-10-11 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 81f368af-4093-30dc-8e7d-305ac89f18e8 | -7.49637 | -34.86716 | 2024-10-11 04:23:00 | NOAA-20 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6f96bed1-0fae-3ce3-8af2-b7d98faa10b3 | -7.49573 | -34.87204 | 2024-10-11 04:23:00 | NOAA-20 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| def5fbc4-b831-3c73-8177-d32aeebd5677 | -6.83657 | -38.57666 | 2024-10-11 04:23:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 416e7c52-3c49-300d-bcd6-b629643ce4ec | -6.44392 | -38.82495 | 2024-10-11 04:23:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f2560435-113a-38c1-9c09-c0adc182c595 | -6.44866 | -38.82568 | 2024-10-11 04:23:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 48adaa9d-1c60-38fb-ac68-5530f3b12a98 | -4.15004 | -38.48283 | 2024-10-11 04:23:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d3ab2320-f5b5-34fb-88ad-da224779e723 | -4.14781 | -38.47953 | 2024-10-11 04:23:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 96984539-c49f-306a-b6e5-cc2b2ca3acd1 | -4.14711 | -38.48441 | 2024-10-11 04:23:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 496a2599-9729-3d0f-84b8-2e759020995a | -8.61447 | -40.52733 | 2024-10-11 04:23:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bcc16af3-a4ed-37e8-86fd-cd0397034ba5 | -8.52959 | -40.26384 | 2024-10-11 04:23:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 36bda379-0668-3f6d-9356-c6b7eef81619 | -8.61504 | -40.52314 | 2024-10-11 04:23:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 87d23707-c795-3fbd-95d1-ef512fa21591 | -8.427 | -40.82687 | 2024-10-11 04:23:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eaa4dfe0-a7ec-3de5-aeea-e43c6a2126e9 | -8.53063 | -40.26085 | 2024-10-11 04:23:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0183f896-8d33-3c0f-b130-c5445ba7afe8 | -5.69139 | -40.98396 | 2024-10-11 04:23:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 99712fe9-b23b-3843-a2e8-1017474177bb | -5.68733 | -40.98346 | 2024-10-11 04:23:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6b9e2dac-5130-33d2-9a34-e24e3e05921d | -6.38749 | -41.9613 | 2024-10-11 04:23:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1c56c9f2-7a5f-38d9-88ed-593eac52e792 | -6.37164 | -40.47571 | 2024-10-11 04:23:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3cb1c508-a856-32ca-b610-56fca258b6b7 | -6.40657 | -41.69699 | 2024-10-11 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a1c957d5-85a7-327d-8b11-dbe5e06ba752 | -6.30049 | -41.76347 | 2024-10-11 04:23:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 822c3bc7-e346-3c5a-8711-a4b02c4223f9 | -5.39552 | -41.24524 | 2024-10-11 04:23:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eca3e06d-5466-3366-91f7-281122833b37 | -5.20071 | -41.29072 | 2024-10-11 04:23:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| de0d3870-931a-3174-8748-a68c52cb853a | -8.00279 | -40.95337 | 2024-10-11 04:23:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4dad63c8-82f1-3c4f-8195-c0508f6cf51a | -7.9986 | -40.95272 | 2024-10-11 04:23:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0c724da9-1878-30f5-b033-c0ae11d79839 | -7.99978 | -40.95157 | 2024-10-11 04:23:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bfe44a86-7bb0-3d2f-b9b8-95da2d77e492 | -7.99578 | -40.97196 | 2024-10-11 04:23:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b0399665-082e-3e7c-af0e-ef93820d8201 | -7.9916 | -40.97132 | 2024-10-11 04:23:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 85290904-59b0-3a8a-a16e-e70984ebf3a2 | -8.00077 | -40.84967 | 2024-10-11 04:23:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1fe53f09-f631-37f5-a582-0c3d9165a8a7 | -8.14555 | -41.10472 | 2024-10-11 04:23:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7bbab064-b456-3816-b38f-055399ff9d2b | -8.13816 | -42.32221 | 2024-10-11 04:23:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 36fe0f6c-c497-3ed6-b5b5-cab0a7c8bb8a | -4.93696 | -43.01122 | 2024-10-11 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66f9ee42-9bec-37a4-8fec-fa0283338842 | -4.74398 | -42.92591 | 2024-10-11 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 858dec3f-b44e-33e9-8089-8ff66c7615c7 | -4.74692 | -42.93053 | 2024-10-11 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31a613b6-8c7e-35c9-9068-6d502f0c1365 | -4.74335 | -42.92998 | 2024-10-11 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2db6db3-32f7-367e-885c-7218f1e459a1 | -6.25417 | -42.51175 | 2024-10-11 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e24fb217-8bf5-3f12-afde-25755985e2c1 | -6.24608 | -42.51501 | 2024-10-11 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f9710134-982b-3283-b412-05d6ff78f330 | -5.88345 | -41.94715 | 2024-10-11 04:23:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 332ea518-f8f3-39e5-9c2c-aa5b7e85e050 | -5.75709 | -43.18021 | 2024-10-11 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1397982e-3002-3d9a-a28f-cffcd8cfb6fe | -5.75292 | -43.18372 | 2024-10-11 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1fd37adf-d002-3005-baec-c8958b15d676 | -5.74997 | -43.17908 | 2024-10-11 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b041ebf2-bc11-3086-b008-9f619bea3337 | -5.74936 | -43.18315 | 2024-10-11 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c36069d0-5658-32a1-9e08-c07db174e175 | -5.35161 | -42.94432 | 2024-10-11 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b9e7bea-c998-33d0-a758-bc9cff1fee89 | -6.25789 | -42.51223 | 2024-10-11 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e7c3d846-0c02-3ec8-b5dc-f5aa33eb3f9c | -6.07341 | -42.38673 | 2024-10-11 04:23:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c14acade-4a4d-3fcc-9bb1-17efb965ff93 | -5.89582 | -42.65527 | 2024-10-11 04:23:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 78b4df96-e2b7-32a5-b47f-555a67e6be25 | -5.75353 | -43.17965 | 2024-10-11 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ac20ea94-d706-33e0-b873-0d382e400357 | -5.40208 | -42.92637 | 2024-10-11 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 41b69403-ef31-371d-b279-a5278edfe1bd | -5.82208 | -43.23159 | 2024-10-11 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4282812-afaa-391c-82cf-f0a75d105f4c | -5.09559 | -42.70512 | 2024-10-11 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d931593e-614a-3ee1-869e-741d7726a108 | -5.0714 | -43.14912 | 2024-10-11 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee991b27-942e-31f0-a0d2-f452b03255c9 | -5.04758 | -42.97241 | 2024-10-11 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ae609b7-400c-3645-9a5d-2de51e30439d | -5.07079 | -43.15308 | 2024-10-11 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab6ffa12-8a11-3143-8775-839bcd30578f | -6.24978 | -42.51562 | 2024-10-11 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f32bedc2-d176-385c-bb26-b95ef910827e | -6.07407 | -42.38228 | 2024-10-11 04:23:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 11aaaa99-ffcd-30a7-a7ce-5c5a19681a28 | -5.78184 | -43.11302 | 2024-10-11 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 00c12129-d900-3ac3-a901-15e8a719631e | -5.75648 | -43.18429 | 2024-10-11 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f104be4d-5797-33bc-b887-b0f2aa02eec4 | -5.75515 | -43.07138 | 2024-10-11 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 74381718-6173-39d5-a639-893f11327c81 | -5.40271 | -42.92225 | 2024-10-11 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b240c309-e4f4-3d33-b47f-72d280aa6c48 | -6.25654 | -42.51049 | 2024-10-11 04:23:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6e0cff42-0304-3154-993a-d381824bf60e | -5.45643 | -42.39565 | 2024-10-11 04:23:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2fdb2ef5-eea9-3e72-91e4-fc3f2951db6a | -5.82271 | -43.22752 | 2024-10-11 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf1a78ec-abaa-377b-9b42-a463f7c82a24 | -5.07494 | -43.14966 | 2024-10-11 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b8083f8-0444-3c2c-a4fb-4b2589b332a2 | -3.41738 | -44.45843 | 2024-10-11 04:23:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bbf16cba-2279-3e48-bc08-74af8b2ed8a2 | -3.37016 | -44.37148 | 2024-10-11 04:23:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 638be909-1137-3de2-b7c6-b3f85379f219 | -3.36682 | -44.37096 | 2024-10-11 04:23:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1789b804-1550-386b-a901-023cdca1c844 | -5.02939 | -44.09681 | 2024-10-11 04:23:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b531dbff-9d7b-36e8-b9bd-544230844fd1 | -4.81819 | -44.35506 | 2024-10-11 04:23:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c927bd1b-21de-3a9c-92f8-53119c07164a | -4.0439 | -44.26731 | 2024-10-11 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e8f0c41-b9df-38f4-a66e-47313acde613 | -4.04335 | -44.27089 | 2024-10-11 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 028049b2-2896-386f-83af-0995db0ed641 | -4.04054 | -44.26678 | 2024-10-11 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4be370ae-a291-3b66-bff9-5f3835193868 | -4.03999 | -44.27036 | 2024-10-11 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c88571a-a097-3dda-921d-9f5d05868b27 | -4.03878 | -44.26633 | 2024-10-11 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0db99cf-8293-3da1-9f31-c5fd23d2ca9e | -4.03822 | -44.26991 | 2024-10-11 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a2f3110-6d72-3040-bfef-6f0f20cf2ff4 | -3.80232 | -44.05695 | 2024-10-11 04:23:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96605192-9843-3e90-9cb0-06c6d08f0039 | -3.79893 | -44.05642 | 2024-10-11 04:23:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20a45e8b-f0db-39ab-848d-16f30a16522a | -3.664 | -44.40264 | 2024-10-11 04:23:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 429ee3b0-1dd2-3dae-96ab-2badb8ad87a5 | -4.9438 | -43.67485 | 2024-10-11 04:23:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f38e648-adae-33fe-9201-01695893f9da | -4.40454 | -43.51423 | 2024-10-11 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71ed05d6-3e02-3694-b4f2-30a0bd51be8f | -4.73994 | -43.70342 | 2024-10-11 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b24011d0-9e50-3c20-b192-865024afbb12 | -4.40049 | -43.51752 | 2024-10-11 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7e0c248-40e2-336d-a3b2-2196815a0099 | -4.2653 | -43.7366 | 2024-10-11 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ceed0c9-eb48-339b-be5b-a2fc5cf1a2c3 | -3.78483 | -43.11377 | 2024-10-11 04:23:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c9f3974-8125-3a31-86c8-641e84fe5145 | -3.786 | -43.11349 | 2024-10-11 04:23:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49a6e0c8-7b5a-344b-8a0b-2827ae5c24f5 | -3.80288 | -44.05333 | 2024-10-11 04:23:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f508e44a-14ae-3e95-a5c4-90a37758d7f5 | -3.7995 | -44.05281 | 2024-10-11 04:23:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36febb25-e290-3a8f-a5d2-015cd277debe | -6.1647 | -43.7086 | 2024-10-11 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ed9240c-d5da-3686-abee-3993a7d3486b | -5.96041 | -43.69505 | 2024-10-11 04:23:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa8db829-c635-3bf7-9491-b35b19f86f5c | -5.69933 | -43.63301 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b95245f3-1306-33b0-b1b8-537ea01e53c7 | -5.69874 | -43.63686 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cab8116-fab8-3e85-a76c-a5eae9738be3 | -5.69756 | -43.64462 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 659c5dc7-93f1-3096-b92b-a92727de7fd2 | -5.69467 | -43.64019 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c9575ab-e0d9-3871-a2cc-4eb5152b4b53 | -5.69408 | -43.64407 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d4e2854-a09c-3b2a-b2a4-cf998f0100c7 | -5.69177 | -43.63577 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbbcb954-f6b6-3fff-88f4-fd5d5b684437 | -5.68131 | -43.63416 | 2024-10-11 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README54.md)
