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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30c53d80-66ee-3130-a909-76753bb69dfe | -3.10494 | -53.24666 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12d6e7ab-327b-3baa-8346-18da1a347564 | -2.96343 | -53.11722 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e60c1e6c-990b-32d7-a151-a47240b57316 | -1.54085 | -53.87319 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b39a9cd-587e-31da-859a-131212d5b386 | -3.83312 | -41.57579 | 2024-12-12 04:59:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aa654690-a6a0-36e6-9748-68a373815e8f | -2.97024 | -53.11821 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4e319e5a-48ed-3b1c-9416-5b1215d62ea8 | -2.81931 | -53.07637 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e6f63c1-9bad-39a0-b616-5720c1ba98c8 | -3.81916 | -44.12145 | 2024-12-12 04:59:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c0f65c4-c081-3a45-87a9-f79a9562ee80 | -2.81987 | -53.07272 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83677236-0053-3d4e-8458-6490f480ebe8 | -2.27161 | -53.48162 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ab52d79-46d4-3b6e-bb2f-d21f5c2f7649 | -2.96684 | -53.11771 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7040bff-cdc9-3ea4-b0e3-13637ad85849 | -4.38501 | -42.14601 | 2024-12-12 04:59:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a7d5268f-4b11-3353-8a53-8f98277467ca | -2.83634 | -53.01141 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51f8f9f4-8a84-3e9c-8140-4bb4dbb51084 | -3.78801 | -47.09733 | 2024-12-12 04:59:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 306c3a32-cb8f-3f17-9f90-8339833fbb0f | -2.46734 | -47.8334 | 2024-12-12 04:59:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ac3a6f0-314e-3629-af57-48bccfc59c2e | -2.46324 | -48.35864 | 2024-12-12 04:59:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95643bc8-b85c-3b1c-82de-f96dd99c2c4c | -2.81703 | -52.97831 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77835f25-5065-3a6d-b53a-3403932c2115 | -2.964 | -53.11357 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a13cdfaf-4a11-3084-b599-2ac0556ed184 | -2.91466 | -48.0346 | 2024-12-12 04:59:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98a0e8e5-04bc-373b-b14a-ef34189ac04c | -2.81364 | -53.06803 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 798f2772-9faa-36c4-a71d-3eea771e3a76 | -3.8261 | -41.5748 | 2024-12-12 04:59:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 41990624-0f42-3b4c-8fed-8acf8c690c92 | -2.91433 | -52.95943 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4550de65-17f2-3cef-bf4e-bb36a6f4467e | -2.30682 | -46.99344 | 2024-12-12 04:59:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c883a8dd-3404-3aee-bd11-587fc0626982 | -4.54798 | -43.56618 | 2024-12-12 04:59:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 010fa2f1-1771-3f99-ab60-c30b11b98d9b | -2.96627 | -53.12136 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 549d5df2-65d7-3768-8422-b5174a9f6669 | -3.26529 | -53.29272 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4163dba-dc87-3242-8165-1e42e69743a8 | -3.13909 | -48.5299 | 2024-12-12 04:59:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c18932e3-5276-3b65-964a-3c35382d9adb | -2.97365 | -53.1187 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8ea911c1-d5aa-3fbf-a9a0-68c357134d34 | -2.55783 | -53.42778 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6af2ca26-b30b-33d3-8f39-a0b412cdd0dc | -2.79401 | -53.23959 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce21b620-9d04-3dd4-9746-5a4ffb6cf0ba | -2.77992 | -53.24105 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0818b0b-0a5a-3d10-ba7f-e75a27063461 | -2.81704 | -53.06855 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 512b5e1d-3370-3209-813b-3b07d41deb5e | -2.57044 | -53.676 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21568eaf-1596-3722-82b8-24af5c00d3cc | -3.04442 | -53.83561 | 2024-12-12 04:59:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4dc6eff-03aa-3dec-9c64-6a13d32c73a9 | -3.04059 | -53.25152 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a5e3a71-f914-3b84-9dd6-d94e333cb200 | -3.24356 | -46.87369 | 2024-12-12 04:59:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 60f67fcf-859d-3677-97a5-59c917687350 | -4.49456 | -46.10783 | 2024-12-12 04:59:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32544d23-1686-3967-a03c-b52a8d61cc0f | -4.38414 | -42.15213 | 2024-12-12 04:59:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 07d3934c-f681-33e7-ae44-f7a5e9047667 | -2.83234 | -53.05969 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47ce3c2a-971b-3a66-a4b8-0b38b9fe5993 | -3.32904 | -53.24685 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75c6be99-7aec-3f84-9c91-d72f1bca2230 | -2.51889 | -51.79013 | 2024-12-12 04:59:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4087b711-3546-35f9-a39a-1b75f1cd03c4 | -2.5788 | -53.68813 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10a26450-5bee-36eb-9cf2-1d22d74c024b | -2.9606 | -53.11305 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38a26b39-a962-3293-8dcf-d82087c32d99 | -3.24767 | -46.88013 | 2024-12-12 04:59:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1af7283a-e70e-314f-924d-60082554358e | -2.82667 | -53.07378 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7df9d14c-36bd-3f34-83ee-8f65270b87f5 | -4.05227 | -46.66499 | 2024-12-12 04:59:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5972b9c-dd78-35f5-b10a-2d43d6810304 | -2.99872 | -53.04771 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 206e33be-177e-3170-8f7e-adfd738bbe18 | -2.83574 | -53.06021 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d393e263-c38b-392d-bd65-f8b7eb66f749 | -3.24183 | -46.88535 | 2024-12-12 04:59:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6e2062cb-1fea-36dc-b0be-20e062245353 | -2.56004 | -53.41356 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 376ce4cb-2805-3c1c-958f-a4c764a039f9 | -4.05738 | -46.66566 | 2024-12-12 04:59:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9de991b4-cf3b-3f6f-a80a-952e8c6a8046 | -3.41648 | -44.457 | 2024-12-12 04:59:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb2ec60f-c99c-31a7-8073-e1dbcbcf4498 | -1.86616 | -47.08821 | 2024-12-12 04:59:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7594bcb0-1c55-3c0f-95b5-25e76c087943 | -4.07795 | -46.72753 | 2024-12-12 04:59:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a83c3bba-ad3e-3153-9549-5e63b332ebb2 | -3.10044 | -53.2534 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01b7899b-f94d-30fb-b169-c39e308fb24b | -2.52246 | -51.79068 | 2024-12-12 04:59:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25692f61-bdbf-3f4b-b4ab-8af3e69ca422 | -4.08948 | -46.6104 | 2024-12-12 04:59:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24a47db6-10ad-3685-a909-07326ba7f5cd | -2.95324 | -53.11561 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f47fad51-74e8-3ac6-88b8-f4df7b89d045 | -2.821 | -53.04296 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d2c3396-d7e1-3571-804c-f434cef9d21f | -2.78964 | -52.8614 | 2024-12-12 04:59:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e081c93-0387-3f32-8ed0-a93939a8c9a6 | -4.55356 | -43.57212 | 2024-12-12 04:59:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7f0f10c-8537-3ba9-81ca-fd452f1abf76 | -4.08903 | -46.61354 | 2024-12-12 04:59:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d20c16b-09ca-39a7-bf16-e8051b9b0b5c | -2.96741 | -53.11407 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56a4deae-f664-335b-ae47-1262fbd0ba81 | -2.83858 | -53.06439 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c88c74e-8b64-317c-8fe3-4600036962ff | -3.04033 | -52.84978 | 2024-12-12 04:59:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab482ba9-53c5-380a-9d55-4cf379a8bfe9 | -2.91466 | -48.00741 | 2024-12-12 04:59:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52e77588-72e2-33c0-a5d9-6d1dc6aa4702 | -3.92102 | -47.00148 | 2024-12-12 04:59:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a452930b-45cd-390a-9272-b58081b9d743 | -4.09143 | -46.61237 | 2024-12-12 04:59:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f3e07b4-1372-3870-bc21-a01d4d9a0bc6 | -3.78717 | -47.10286 | 2024-12-12 04:59:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6b52b0e-9794-3993-b759-ad7c2d252789 | -2.52668 | -51.7871 | 2024-12-12 04:59:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d815fb6c-e62e-3098-8423-939b1151a525 | -1.81217 | -52.72539 | 2024-12-12 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a0defa7-6c4a-356e-a751-94ddbb505fe8 | -2.58483 | -51.92285 | 2024-12-12 04:59:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be056bda-a598-3a65-8077-6f6ee99ae1d3 | -2.91775 | -52.95997 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2627085c-730c-36f6-9ff9-58430fe1d6d9 | -3.99297 | -46.96108 | 2024-12-12 04:59:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d22d22ed-1301-3a95-9996-b5847c84d2dd | -2.0772 | -52.28154 | 2024-12-12 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ada1240-8695-329f-8d33-b1a5719361ac | -2.95664 | -53.11615 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac643d61-f408-3c48-84fd-35e7ded968c0 | -2.97081 | -53.11456 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 074209c9-b808-3fa1-80db-9cb8af1a5b14 | -1.52973 | -55.32592 | 2024-12-12 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57a04fb7-5195-368e-9131-05e6a4c47993 | -3.00545 | -48.0541 | 2024-12-12 04:59:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b091bd18-aab0-3cd7-98d4-7323a113ec23 | -4.04716 | -46.6644 | 2024-12-12 04:59:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d9e5842-bed4-35fe-b974-6125c37f1086 | -2.78907 | -52.86509 | 2024-12-12 04:59:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f4c26a6-617c-34a5-aa78-5994010a6a70 | -2.83293 | -53.01089 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8936896b-a576-3a4c-a0dc-6bf2340c8c95 | -2.54774 | -53.42624 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 297991cc-5cd6-3d51-94e9-86ae373bdd14 | -2.52604 | -51.79119 | 2024-12-12 04:59:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8576d26b-d869-3c8b-a222-7b41e35c1ba2 | -3.03946 | -53.25875 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f3f4c5b-9cec-3c0e-925b-64d6929d1d0b | -2.57555 | -51.88859 | 2024-12-12 04:59:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad428c9f-d9f2-31be-8fee-94e4b8e8d16e | -2.5231 | -51.7866 | 2024-12-12 04:59:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfe7e0aa-754a-33e8-851b-c667958e8cb3 | -3.78223 | -47.10226 | 2024-12-12 04:59:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1c5da2a-1173-37f8-a282-174090291731 | -2.96004 | -53.11669 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc7a2d3a-efc5-36d6-9da1-4ea574b95e8c | -3.04776 | -53.83612 | 2024-12-12 04:59:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30a28e9d-0bcf-3e57-ae79-728b2d5fb2ee | -2.7771 | -53.23692 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e991e5f9-209b-3dbe-bb4e-5ac7b06017a6 | -4.54396 | -43.56783 | 2024-12-12 04:59:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcbe7fa7-d0e4-3369-88bc-faac4bfca604 | -3.18336 | -52.44841 | 2024-12-12 04:59:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a42e3088-faa2-348d-8721-f958bbc9d07a | -2.96967 | -53.12186 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8af8fbf1-ac29-3438-93bb-ff324d0c22bf | -2.80684 | -53.06697 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 101268a8-69fb-3f66-ab3a-861472095228 | -2.64429 | -53.3493 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c748893-b03a-31e6-9fe4-93d1de49eeef | -3.05696 | -52.42578 | 2024-12-12 04:59:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1c3b860-2cc5-311c-93d4-eadd783fcf1f | -3.81665 | -44.12215 | 2024-12-12 04:59:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3178a82c-fde4-3522-bf71-3298c64099f8 | -2.78849 | -52.86879 | 2024-12-12 04:59:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34d46678-c423-33ac-ab35-ff750c3c24cb | -2.81759 | -53.04243 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70b95a15-0eb0-332d-9872-bb37d6da25ce | -4.07834 | -46.72475 | 2024-12-12 04:59:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README29.md)
