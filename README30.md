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
| b5c47a39-e4cd-3f1f-8dee-827ae840c23f | -2.86824 | -46.66005 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb492cdd-8577-3ef9-ae81-4dd0dd8acc37 | -2.32551 | -50.51388 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7ec879f-fb98-3f98-868a-5825614c83b8 | -1.23764 | -51.75454 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| beb70777-7c6d-38a7-83ab-3da35097134a | -2.16068 | -50.51334 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ea85521-502f-3298-a6c7-44b2b739945d | -1.62316 | -52.23903 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a3bde15-509c-3986-a4af-051523d173f1 | -3.10983 | -45.96057 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf1ebb0a-c7c3-36c5-972e-42196087936b | -3.30804 | -42.48163 | 2024-11-09 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9ea7fc1-4b6f-32c4-bbe2-06dcb76f3dc6 | -1.24342 | -51.76964 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea98e75c-5888-35fe-93cf-03c675dce78d | -1.49925 | -52.55208 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24e5dba9-e0b6-3c6f-8411-af12953d72f2 | -1.67798 | -48.72947 | 2024-11-09 04:31:00 | NOAA-21 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb9a808c-82a4-3cb4-925e-68ef5f9871a9 | -1.34503 | -51.41043 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| efa2b10c-1af2-3673-99ad-45507c286b6f | -2.24691 | -46.49959 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bf3d906-4724-37e1-81b5-6745468ee465 | -2.5848 | -48.21339 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df998c3d-a1f7-32b5-a5cd-3099ada979a7 | -2.82379 | -48.47136 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a86fecbb-b127-3d8d-ac66-193f63ac6cd7 | -2.83121 | -46.63669 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3c28e2a-0dad-33b7-83ac-cdeb49b5b26c | -2.12358 | -46.74833 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30f5bb93-f40e-3c3b-93cb-ae8a7ff355a4 | -2.81198 | -46.6514 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a92dc048-d852-3f61-b47c-5b8a525dcda1 | -2.37155 | -46.72744 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2b61709-7681-3e29-9228-308fa1c3075b | -1.51735 | -52.19651 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 254aea27-b614-3150-8076-0c29995e0255 | -2.38442 | -46.77517 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e731be73-6350-325a-b83c-15f6665205cf | 3.36721 | -51.27858 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| df79eace-4298-3a75-adcf-55b9e16e8f81 | -2.40875 | -48.39974 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 594477d2-6ada-31b3-82fc-b5b9296bf0d0 | -1.52262 | -52.18982 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| af63a64b-0f56-3ac5-9d1e-6f482bfdcc32 | -3.14849 | -45.94863 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 334aa41f-70a0-3048-9d05-98172c44130a | -2.48397 | -49.07527 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79fecb4c-f206-39d6-8946-6fcc97c8ce1d | -1.61347 | -48.67465 | 2024-11-09 04:31:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7efe901-62e9-3ccb-9a1a-5dbd78f36bc8 | -2.4696 | -46.88324 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88027753-c4e6-3f39-9d56-149c5e545b87 | -1.55622 | -52.27043 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98a69c37-77a3-3d4a-a1da-cb9d11b7b132 | -2.82629 | -46.64654 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03f0b830-4db4-3dfc-a681-734e8c539aee | -1.21669 | -52.94321 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 983d001f-a66d-3393-861f-1671ba040487 | -2.3854 | -46.74718 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 597185ee-1196-3eee-bccd-d2de9ba84435 | -1.59683 | -52.4841 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e5009190-2f28-3952-9ada-128053391467 | -2.08778 | -46.5175 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09492078-8eea-3c6d-ac9a-4475dba34b0a | -1.94205 | -51.40327 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 5c02c857-e7ce-31cf-a285-1ccb48e51f34 | -2.31368 | -46.2233 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d487938-e35a-34dc-b1a9-a05f03bca55b | -1.72613 | -52.46097 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5acc6ce3-73a2-34b4-a42b-f8ec79f85b1e | -1.96003 | -48.702 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25ba1623-6745-3882-a956-9baac3e393e0 | -2.36558 | -46.74413 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba2f4396-69bf-3646-9bf0-ed340dc08069 | -2.40975 | -48.52396 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 790cdc5a-890a-3766-9467-2aa1c79862e8 | -2.36625 | -50.61278 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00982f72-702e-3b4b-ab91-627dc0d283ce | -0.91053 | -51.76337 | 2024-11-09 04:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7690448e-50ef-3ab3-9012-6ce2e4f2f295 | -2.67984 | -46.77919 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 183157f4-3e10-3cb6-b440-1cb2c730b3fa | -2.16833 | -50.53658 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23a1727f-ed01-3c03-8b5d-35a654d69e45 | -1.52114 | -51.30962 | 2024-11-09 04:31:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f8d4c9a9-8247-3bd3-a2c7-ccaec9bcd817 | -2.36258 | -50.61218 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97bbf928-9b75-30a9-af10-852e6bb4d93d | -2.57092 | -48.25809 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4edb032-4ad1-3a29-9c0e-c589898f0249 | -2.57979 | -49.1354 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b4ca7583-3b6c-3606-9d08-0efdd0e5d7c1 | -2.0384 | -48.98442 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48626e72-f3b3-396e-98d8-2c559f581168 | -2.63267 | -46.77472 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dec2ebd2-6bcd-305f-bdf8-49c423b3949a | -2.34191 | -46.63133 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79be01e5-aca6-317c-9594-0e87082a86aa | -2.46305 | -50.40401 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc9d7a1f-7bb3-3d5b-99c4-d49d2ec2b9df | -3.13398 | -45.95366 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c71d429-c4f7-393a-9105-5dcac5505b68 | -2.08591 | -48.29509 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dea062d3-0329-36cf-a27c-0c2d86ce4015 | -2.44525 | -49.18751 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6e1c187-0d90-3019-8812-cb103dfeffdc | -1.68922 | -54.25513 | 2024-11-09 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| edc48cfa-32e3-3417-8397-2fdc18bff98e | -2.10452 | -47.8916 | 2024-11-09 04:31:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd633ec6-e839-335f-a7f4-a4adafcab9fd | -2.39834 | -50.31296 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b7ac8ed-0f70-399e-84fb-944ea528d442 | -2.14694 | -46.6851 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee2970e3-c426-39f2-9adc-61edf83348a7 | -2.56749 | -47.3444 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8334aa27-e357-3448-b962-4522e0f5fcfd | -1.71182 | -47.8797 | 2024-11-09 04:31:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f89d3787-0d53-339b-a872-535167afb25b | -1.56215 | -52.28652 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 21f2635f-574f-3f97-b606-3e8708d40498 | -2.68177 | -48.50722 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97ff67d3-3720-3b5f-9baa-b712fac832a4 | -2.23591 | -46.50496 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 487b6571-9676-34e4-9ffc-80149cebec19 | -2.60145 | -48.19438 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a56aa4c5-7c26-3f78-a8c8-7086c72b915e | -2.23116 | -46.55714 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4697c88b-4915-3acb-8cb4-754e159aeaf0 | -2.17772 | -50.97601 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61a7d60d-8357-36b1-a07c-a40ebfdb4ee1 | -0.60337 | -49.55283 | 2024-11-09 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3111a60a-ca8f-3d70-bacc-060a11f02a98 | -2.18903 | -48.37628 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5070596b-bc15-32dd-b35a-7c151ab0b5b5 | -2.28352 | -46.50597 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad873326-443e-3b80-b013-09912dcb8f40 | -1.07174 | -48.76856 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e3809e7-bbf9-3608-9123-177b2cd2de6a | -2.42657 | -50.51562 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba1a5326-91f1-33e7-9777-8b6b104e3595 | -2.2683 | -46.47109 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c0a41a5-8a2d-3292-8acf-9f415a261a6b | -3.06741 | -45.40068 | 2024-11-09 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16f48eef-8928-3952-85f3-2f9503519700 | 1.32144 | -50.72367 | 2024-11-09 04:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4708d453-2e9a-3894-8528-932f6892cdeb | -2.31175 | -50.67106 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a7b8bbdc-c75a-38dd-ad3f-314b2366b288 | -2.37398 | -46.77708 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42dedf0c-c660-3975-b132-901ef093a954 | -2.57124 | -47.32038 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36b2cf99-dfe2-35f6-83dd-41e41c360f35 | 2.48078 | -50.83947 | 2024-11-09 04:31:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08ae7a87-e475-35be-ab4f-936bd47ed297 | -2.15444 | -49.13933 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ce86c43-9c41-3b64-9540-81120f0f7629 | -2.17554 | -48.33055 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a466e7cc-6ca0-3b85-b778-e217e2983777 | -2.5838 | -49.13221 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c536226e-cf86-38d2-b480-828fcc3405d2 | -2.1884 | -48.33617 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68b86640-0f12-3944-b8a4-ffdc936d8f27 | -2.50949 | -49.88344 | 2024-11-09 04:31:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a19f795-d7ed-38d3-bd4e-589774899601 | -2.80078 | -45.97523 | 2024-11-09 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ce9e5ca-7481-347a-b6ad-5ccf90e7875d | -0.90519 | -51.65548 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e217d576-f682-358e-92f9-71bcc212cdbf | -2.37232 | -49.35767 | 2024-11-09 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10d8cb9e-f3ae-3ec8-ab8b-d8f3cc60683a | -2.263 | -46.83381 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d809d91-fcfa-3e3d-81b5-ffadc8c9a8f8 | -2.37496 | -46.17925 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 059825dc-dcfb-3eca-9152-43d21f3c29f4 | -2.18678 | -48.36865 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62201a31-bdb5-303d-9ab4-1a61ced8b968 | -1.51676 | -52.17395 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8da50c50-8d19-3c24-8d0d-392ab480a4ea | -1.42582 | -53.9109 | 2024-11-09 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fd9d1e0-29b8-361d-ba7b-2ced05e1f111 | 0.81097 | -50.21816 | 2024-11-09 04:31:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afd4657b-9750-3f13-9eb8-799923f638db | -2.2432 | -48.37363 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6ddfb0f-d95b-321c-8ad9-f76c1b13b23a | -2.08352 | -52.04965 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f02390f-9a89-33e9-9400-c6d76c1be828 | -2.58254 | -48.18428 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9910938-d1fa-32d2-9746-dcd87494654a | -2.65149 | -48.63436 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb01a7c8-91bf-3b9a-85f3-b620f760ca54 | -2.83174 | -46.63324 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c38aef45-5132-30b5-acae-e9e4ceb66d3a | -2.83013 | -46.64359 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8f90352-806c-337e-a0cd-4ac2aed61d5e | -2.19566 | -48.36995 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05ae9997-706d-3173-9492-d90da0380a61 | -3.25512 | -43.20273 | 2024-11-09 04:31:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README31.md)
