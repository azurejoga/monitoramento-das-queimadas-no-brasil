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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 744599cc-fd55-3feb-99d2-39febb125827 | -10.25284 | -36.36201 | 2024-11-15 04:23:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 50a8a1a8-dbfa-32f4-8357-74e34f9bfe2c | -6.16213 | -41.16839 | 2024-11-15 04:23:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 69f70039-d4ad-3ffb-9057-d361eb6bd5ce | -6.75661 | -38.6486 | 2024-11-15 04:23:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b2e550d2-9623-330c-8ada-0db5fb9b786c | -6.64775 | -39.14787 | 2024-11-15 04:23:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 07c180ed-23f1-3846-ae33-b9d8a78ff8af | -6.1476 | -38.32031 | 2024-11-15 04:23:00 | NOAA-21 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2062d651-b85b-34dd-a4d2-13d389c8ccaf | -12.57562 | -57.81725 | 2024-11-15 04:23:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0053874-df2c-330a-a98c-aba3644ee45a | -3.06684 | -53.28117 | 2024-11-15 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4dfa207-b1d5-304d-8ce2-e0eb9b17339e | -6.94713 | -41.02812 | 2024-11-15 04:23:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6ba19dbe-a578-3f6a-a7ef-cf1ce09ef2f9 | -6.1628 | -41.164 | 2024-11-15 04:23:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 303a352c-27bf-3647-a54c-494141ae7904 | -3.69136 | -54.57669 | 2024-11-15 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82a24e7f-fc41-3b52-b51b-b0dc3d85b3fa | -17.63788 | -57.54847 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 97e9180f-fead-394f-a632-bcae63024f4e | -16.95397 | -57.63832 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 89cfd7c1-163d-3d2d-9a74-9752f9c6eacc | -17.58129 | -57.54328 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f3fd426f-b247-33fd-9fdb-3814494b550d | -17.25168 | -57.47602 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9fc60339-2821-38a4-9030-cac4bb765639 | -17.55958 | -57.53838 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 8a84b2ab-a930-3536-8a78-58bd54fc0c9b | -17.57718 | -57.45425 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 50980c9c-f0bd-3828-916d-1c0ac01704e4 | -16.10474 | -60.09856 | 2024-11-15 04:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8f764d9f-4bb7-3b39-8ee2-a71456b4a040 | -17.26877 | -57.47598 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 20a59eeb-c8ac-3de9-8ea5-7fbc4d6953f1 | -16.94373 | -57.63204 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 1a5c8a47-2a38-3860-be82-b0ce2ddd2940 | -21.30641 | -56.02604 | 2024-11-15 04:25:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a83ae1f8-80d5-39c0-a71c-0a941ec12d49 | -22.05672 | -56.01 | 2024-11-15 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdc4d084-4311-39d0-a055-1bb8f1b2ab2d | -17.23845 | -57.45763 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 43372b8d-1d05-3e3d-a1b7-f302f87e63b8 | -21.90737 | -56.45898 | 2024-11-15 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2b63e17-6a82-3550-8dca-9d3594c62771 | -17.6309 | -57.55458 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| b7918f47-2902-3122-87f1-9607dbf44bc4 | -17.5819 | -57.48586 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 0fa17a65-9a3c-3485-8a7d-0223fa58ef4d | -17.60762 | -57.5571 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 2b79fefc-366b-322e-a5b4-8f3262eef3cd | -17.25399 | -57.46495 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 50ef0fd0-4458-30d3-a119-9660bb8e17ea | -17.7191 | -57.53991 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d2cbd222-8b2a-3ca3-a641-ecb6941483e3 | -23.71201 | -55.16396 | 2024-11-15 04:25:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0f2c23f9-4e3e-3279-897a-19ebc1e1d4c4 | -17.24855 | -57.46373 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| da6f2f95-bdfe-3946-a2b9-cbaa0174a2a8 | -17.28661 | -57.47223 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c387a85a-b4f9-346b-a33d-b29b1aede1ea | -17.62547 | -57.55337 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.3 |
| e90898a1-bbbc-3e62-a79d-1056beba0838 | -21.55713 | -55.82647 | 2024-11-15 04:25:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39b56abe-3567-336d-859b-9189c6bb15de | -17.25789 | -57.47354 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| d89f1c53-e757-3e5e-b26a-57d6d270cfb5 | -17.23691 | -57.465 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 3c798f07-cb23-3609-a95e-57020c509915 | -17.59801 | -57.46277 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| dba4879e-2fb6-3828-8742-80c68d6e915e | -17.2933 | -57.47145 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bacff11d-9dd6-37d1-a593-d1e082bd4698 | -16.94926 | -57.63327 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ed036d28-1ff5-331d-92bf-6db62956f3b4 | -16.95478 | -57.63449 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 20409a55-f570-3d85-91fd-92371b7c7015 | -16.09826 | -60.09704 | 2024-11-15 04:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f89a52b0-d7d0-3b93-84a8-57c55b56c34b | -17.56501 | -57.53961 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 2ad70e2d-e899-3ff5-8822-6d20fb1c1207 | -17.26256 | -57.47845 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 47abaf48-fa53-38af-a74b-b5b156839759 | -19.77173 | -55.41402 | 2024-11-15 04:25:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7fe33cdc-c24f-35b4-85a2-83bc725d7ed4 | -17.61384 | -57.55462 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 206161fb-4fd9-38af-988a-36a315d06952 | -21.57767 | -55.81367 | 2024-11-15 04:25:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03e79aa3-1031-3981-b704-1c4a2f941cba | -17.60039 | -57.47856 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6e2a31de-7ba5-3db9-9401-171da3dee0c9 | -23.64929 | -54.5589 | 2024-11-15 04:25:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6150a052-bac3-37ed-ba60-ff7efc6998be | -16.01926 | -59.40147 | 2024-11-15 04:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd284759-9c79-3f28-81fc-e787452e87ad | -18.03461 | -57.34983 | 2024-11-15 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bd6801e1-233a-3e9d-aafb-16a7285505d5 | -16.95007 | -57.62945 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f2a44e54-3eec-3b24-b68a-1395f8676177 | -17.25553 | -57.45757 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 54998454-b604-3df8-99b5-b66fd13d2c0a | -17.70058 | -57.54724 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 04a64840-aa2d-3122-9c5d-d586f256b00d | -17.62626 | -57.5497 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fba0501d-c679-32ea-816d-3f0577610de9 | -17.57427 | -57.52246 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 542dff34-e412-355b-b056-ac604faf4c0a | -17.62391 | -57.56075 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.3 |
| 588a13bf-9626-3246-b620-d651b94eda9e | -17.25712 | -57.47724 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 6ebd6033-df5b-3211-87c8-cbdb793cf8b9 | -17.56731 | -57.52857 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 44d8e013-7409-345e-b4ac-9ecfe28d86f7 | -17.71835 | -57.54357 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 650d7963-7142-39d9-98bb-e4e3b1025ae0 | -17.69754 | -57.56195 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 6df2fd63-2b05-379b-bfe1-234d56f9c6cb | -17.69355 | -57.52652 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f8418f9a-2550-3274-b7ff-911dceb4776d | -16.95869 | -57.64337 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a3213d8e-a570-33e1-b052-2d583d1b3566 | -17.70516 | -57.5577 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ceeb2bc5-6caf-3ca5-b240-63293d89a98d | -17.59499 | -57.47734 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 950365ca-a726-3505-9ffa-8140e55fa180 | -17.67426 | -57.53746 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ad17d9c3-3753-38bc-8f9d-c5c357bac99d | -16.02167 | -59.3902 | 2024-11-15 04:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| beadfcc2-1ba2-30a1-8ff0-54453c27d3a5 | -12.32803 | -57.75417 | 2024-11-15 04:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cbb0a0b-de58-3e5c-b8a6-b59fdc0fb80d | -21.08266 | -47.47497 | 2024-11-15 04:25:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0bc1b28-ff2c-3bdf-b92e-64019fd26cc3 | -17.72737 | -57.49977 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 26fc8752-6df1-3786-b997-680db380e776 | -17.58052 | -57.54697 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 029b7435-f2d1-3969-860f-221c9d9f7f68 | -16.94763 | -57.64091 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 51882025-4024-3206-a98a-edac77dfd22f | -17.58673 | -57.54449 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 54349bb3-01f7-3d11-9f8a-b9f5af38848f | -17.6154 | -57.54728 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a9d1ed6e-309f-37e7-9b2a-3fa54a5b064e | -17.57125 | -57.56419 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| d419c2dc-86ec-3b37-ab6d-95a502dff3c1 | -17.57048 | -57.5679 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| b1f56707-b289-3f23-8213-2ba0bf2d217d | -17.71835 | -57.54914 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7030986c-2efa-3322-a457-7f0dc4f0adbe | -17.63324 | -57.54359 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| e18a6261-1393-3802-a3b6-14143af31563 | -13.39021 | -40.47176 | 2024-11-15 04:25:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8818bca4-d06f-300e-8f8c-6e0beda52249 | -17.57976 | -57.55066 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b176e9dc-bb2c-3046-bc69-97b9da6669b1 | -17.70914 | -57.56071 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 192799ff-9334-3e83-ad93-7c93cda8ae83 | -16.02049 | -59.39569 | 2024-11-15 04:25:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4ed8e1e-a6c6-3f47-bca7-e6394ba44bbb | -23.71117 | -55.16819 | 2024-11-15 04:25:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b5b4b618-23f9-3e23-87b9-2fd0bbf45d73 | -23.73429 | -55.38499 | 2024-11-15 04:25:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 37597415-48dc-39b4-a251-23352b80d25e | -17.56578 | -57.53592 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| b45d380e-ff24-3d6e-870b-f3cda7dbec13 | -17.72461 | -57.49332 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d3d1ded8-1452-3156-9fd7-09a120aaf3b1 | -23.64958 | -54.57935 | 2024-11-15 04:25:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3d252827-7c17-340a-bd93-37651b6d5cd4 | -17.59186 | -57.46519 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 30d162f9-fc6a-3632-93df-8ebf0d715227 | -22.05221 | -56.0089 | 2024-11-15 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b7e72e1-3bad-374b-92bc-04e2263f5d32 | -17.61386 | -57.55064 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| dfd52867-138f-39c2-aa3d-3b30c5f7d20f | -17.60115 | -57.47491 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3ba5f8f3-f206-34ff-897d-be63df4844f8 | -17.58832 | -57.56421 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.6 |
| ec9e552f-3ac0-3579-a590-f5bb6e7393f0 | -17.64486 | -57.54235 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b25769b4-b713-3a5f-9284-07a943f53cc6 | -17.58097 | -57.43613 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| af7c17cf-6021-352f-a68f-2c37a80dfe57 | -17.56655 | -57.53224 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e35c716f-2012-3e4a-aa34-af01f6809570 | -16.93739 | -57.63463 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| aca2a7d2-c2d0-33d6-95d7-c0ab0a09588f | -17.6983 | -57.55826 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 83b5084a-03d1-30a6-8c68-cba8fa923804 | -16.94292 | -57.64211 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| c64d2153-64d3-37a9-a57f-4c71e93c56c7 | -16.94292 | -57.63585 | 2024-11-15 04:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 675840e0-41fc-3d9c-bd96-ae671d18db11 | -21.07877 | -47.47813 | 2024-11-15 04:25:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce2cd8ee-b132-3a38-88e4-69adb8664f6e | -17.59271 | -57.4883 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f4bf7cba-e468-3c73-af5b-93ebaf264da2 | -17.62079 | -57.54451 | 2024-11-15 04:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |


[Clique aqui para ver as próximas entradas](README16.md)
