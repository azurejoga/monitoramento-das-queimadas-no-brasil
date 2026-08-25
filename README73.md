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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6294d814-bcab-34eb-9a5a-41ffc1d67096 | -7.2903 | -45.3456 | 2026-08-25 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 2cbb80c6-e675-3fde-a8bd-79f424803a8b | -8.1765 | -46.7007 | 2026-08-25 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 7f8d0ff1-750d-3bc0-bf94-c2dec94f9ce3 | -13.3402 | -48.2079 | 2026-08-25 13:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 2434102b-2f68-3862-b8d5-6ae110f5c9f3 | -6.1284 | -57.8588 | 2026-08-25 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 72433d4d-d7b3-3d2c-a0b1-b4fb25e99688 | -6.641 | -58.4987 | 2026-08-25 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 190.7 |
| 125a6987-1527-3690-bc7e-5c962635b956 | -11.9991 | -45.9287 | 2026-08-25 13:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3cbb6e25-95ef-38a7-a7d6-ff10deb9b067 | -6.6411 | -58.4793 | 2026-08-25 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d32979ce-2846-39e6-b8c0-d329934aaa9b | -10.8605 | -50.5626 | 2026-08-25 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 7b02b355-31e6-3d50-bd71-b5c697965d2c | -6.6226 | -58.4995 | 2026-08-25 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| de61f599-fce7-3fd4-b7bd-c416269787d0 | -11.4494 | -44.5353 | 2026-08-25 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| c6ea3982-26ec-39e2-b9df-97b4cb0c76ed | -11.4298 | -44.5615 | 2026-08-25 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 393.2 |
| 1292d523-9358-3858-9357-9a4134104138 | -7.3849 | -55.1723 | 2026-08-25 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 6b134027-1c1f-343c-85eb-7a9286af9e77 | -3.5407 | -48.1673 | 2026-08-25 13:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| c8881ff3-5269-3dc0-a16a-f56002b828d6 | -11.9991 | -45.9287 | 2026-08-25 13:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 56f59f03-80d1-30c2-86bc-a74d2edfeaa9 | -8.6078 | -50.0124 | 2026-08-25 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 7b10e716-f3fe-32fb-98fb-1b23f2ad8f28 | -6.641 | -58.4987 | 2026-08-25 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 194.9 |
| b55ea3cc-63b7-34bf-bbe2-3b153167ebdc | -6.6411 | -58.4793 | 2026-08-25 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| f9466a5f-bf60-3b1c-8ad5-efe95b3d63f1 | -3.4167 | -43.3867 | 2026-08-25 13:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 63b9f9bc-8071-3e7b-85ff-85b4142a2f3d | -6.9872 | -59.2582 | 2026-08-25 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 175.9 |
| 08ced762-11ec-3e0b-9b8d-be462fcc7889 | -8.5775 | -54.8575 | 2026-08-25 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d680e533-5b6d-3cdf-a47f-517fce5ccebb | -7.0242 | -59.2374 | 2026-08-25 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f4734db6-0a9f-359e-adc3-1013f757efd4 | -7.4289 | -43.0947 | 2026-08-25 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 122.9 |
| e529ce9d-0118-3698-b1c2-3fb886cd1dda | -6.1284 | -57.8588 | 2026-08-25 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 3fc7b8a1-4798-3e29-8f92-9379a3fa5a9d | -7.4474 | -43.1163 | 2026-08-25 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 308.6 |
| 2baf6633-743b-3df1-83ca-4b793074fb98 | -7.3849 | -55.1723 | 2026-08-25 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 9b1f5d30-6e18-3b6c-9fbe-3f12fe09a076 | -13.3595 | -48.2051 | 2026-08-25 13:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 148.6 |
| c16603df-078e-3eaa-b09f-5b2196fe5c1a | -6.6409 | -58.5181 | 2026-08-25 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 62be4c82-bbbc-33ae-9da5-70e366c5922d | -9.5753 | -49.2367 | 2026-08-25 13:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 317dfccd-2c2a-38a3-8b4b-04332e7a7eb9 | -7.2903 | -45.3456 | 2026-08-25 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 0d5bd02d-e18a-32c8-8fee-21c8a8fcc17f | -13.3402 | -48.2079 | 2026-08-25 13:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 7926e23d-a7a2-3bff-ab67-baf9683b1f26 | -7.0057 | -59.2575 | 2026-08-25 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 6a240fa5-afa1-31e5-83a6-8531ebfa6734 | -6.6357 | -45.1752 | 2026-08-25 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 631dc08b-aa7f-350f-b39a-e047f5d917b5 | -12.151 | -50.6098 | 2026-08-25 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 0f40c879-08ca-3b09-a630-e8c23b30311d | -11.4494 | -44.5353 | 2026-08-25 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 8ed66e9c-c909-3e80-918b-5a7168812ba6 | -11.4306 | -44.5148 | 2026-08-25 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 99566ba0-6ed2-3743-8c6c-a65671a29d1f | -7.4286 | -43.1182 | 2026-08-25 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 144.6 |
| 02c9ae7e-cb7e-3206-a046-d3f08e083214 | -7.0058 | -59.2382 | 2026-08-25 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 5869545b-e7db-367c-a76d-f53bd0a627f2 | -7.4477 | -43.0928 | 2026-08-25 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 219.9 |
| f06ba3d0-1333-3de3-837d-d6d941bae9f1 | -8.1577 | -46.7025 | 2026-08-25 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| f8f38ee7-e6d7-3d7d-9c19-e867e05847f6 | -6.6226 | -58.4995 | 2026-08-25 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 1eed2ac7-6e63-3935-9040-c647b706175a | -7.2901 | -45.3683 | 2026-08-25 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 56a02a6d-5c5c-3603-916f-22cf466f8279 | -8.1765 | -46.7007 | 2026-08-25 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8ab3c1aa-4c78-319e-9964-557826faec1f | -6.9873 | -59.2389 | 2026-08-25 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| f3210538-d634-3063-b1a7-adee29ac7ee4 | -11.4298 | -44.5615 | 2026-08-25 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 350.9 |
| 77d4742f-4d19-3f22-9792-133331c81063 | -14.7397 | -48.7943 | 2026-08-25 13:20:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 1dacc5fe-6921-3260-b7b6-3f42bc84cc55 | -7.4286 | -43.1182 | 2026-08-25 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 114.6 |
| 4c7549a4-eda3-3f3c-bebe-f1670432efe5 | -8.5775 | -54.8575 | 2026-08-25 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 02081e20-5f1c-34ba-ad1a-c77ff33f27b2 | -6.1284 | -57.8588 | 2026-08-25 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 446f352a-056f-3fa7-8c17-239c0af6f2a6 | -8.589 | -50.014 | 2026-08-25 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 92903a0b-3fe2-318b-b4c2-226076432b7d | -6.6169 | -45.1767 | 2026-08-25 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 9798442f-aa08-3c2f-a1bd-10e2c87fc4bf | -14.7592 | -48.7913 | 2026-08-25 13:20:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 108.7 |
| cacc8a8f-8a8d-3b9a-89ec-18efdaf7ff14 | -12.757 | -46.4538 | 2026-08-25 13:20:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a4ee8724-cab6-30ce-8754-63b52cee9315 | -6.6359 | -45.1525 | 2026-08-25 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 342.8 |
| a50559a8-ab44-3c7a-a24c-f58c9972e678 | -8.0918 | -47.527 | 2026-08-25 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 2f5c95cc-bc00-3fa9-8cb9-e0352ea07a02 | -4.1934 | -54.5755 | 2026-08-25 13:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f912e305-31fd-3580-b51d-c2d87e8ca4d6 | -11.4494 | -44.5353 | 2026-08-25 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| dda64196-a0c7-362e-a170-cd433ca620a9 | -7.4474 | -43.1163 | 2026-08-25 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 162.7 |
| fb2f418d-d217-3588-872e-3a503856fe8a | -6.6411 | -58.4793 | 2026-08-25 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| ef686e40-bfa1-3c2d-8594-8133cf6d7467 | -7.0241 | -59.2567 | 2026-08-25 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 7d130a69-b9cb-322f-8465-e8f8a1718462 | -6.9872 | -59.2582 | 2026-08-25 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 157.0 |
| 54901a8f-52f3-32fa-8854-608e45aa5a7b | -8.6078 | -50.0124 | 2026-08-25 13:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 6c5a9a6a-961e-3996-93e1-bc8b3ad411bd | -6.641 | -58.4987 | 2026-08-25 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 284.5 |
| 754bf669-6927-36f9-9170-8a8b1514afeb | -7.2901 | -45.3683 | 2026-08-25 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 160.7 |
| c6602b9b-6958-358f-8ce7-dcc42c29aac0 | -12.151 | -50.6098 | 2026-08-25 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 43ec82a2-d317-327b-92fb-7addb916fbad | -7.0057 | -59.2575 | 2026-08-25 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 165.1 |
| f89a52c6-7483-3c10-ab94-ff3b43cb3193 | -8.1765 | -46.7007 | 2026-08-25 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| a98dad2b-7947-35ce-94ad-592de2524f2c | -3.4167 | -43.3867 | 2026-08-25 13:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 10063edd-cca5-3533-9b64-f49b50ec7afe | -11.9991 | -45.9287 | 2026-08-25 13:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| c0f51546-d646-3439-bd36-35a96374593a | -3.5407 | -48.1673 | 2026-08-25 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| c9b3abd0-c76b-3f5b-bff6-9608e8ef8aea | -9.5753 | -49.2367 | 2026-08-25 13:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 45c79abc-2ee6-3ab7-a124-e504b5fc1924 | -8.073 | -47.5287 | 2026-08-25 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9db3fd2d-2ae2-33b0-b9bd-4b0f03c7711c | -6.6409 | -58.5181 | 2026-08-25 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 2661083e-5571-3351-a4d8-f105e36f62ca | -6.6357 | -45.1752 | 2026-08-25 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 735.4 |
| c0693b72-3022-3a32-8707-caaea5da1fa3 | -13.3402 | -48.2079 | 2026-08-25 13:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 62527775-db59-3e92-ab3b-df7e3fe0e9de | -7.0058 | -59.2382 | 2026-08-25 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 2a7cff8a-7d38-3a6f-a243-501731e632a9 | -7.0242 | -59.2374 | 2026-08-25 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 0a523a28-d348-3906-8ee8-081b091d1a5a | -6.9873 | -59.2389 | 2026-08-25 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| b64cef2a-8fa7-3fe8-9e4d-21f2311f9b25 | -7.3849 | -55.1723 | 2026-08-25 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| acdedcb4-f539-3234-953a-71117cb56219 | -13.3595 | -48.2051 | 2026-08-25 13:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 4f1d37f7-c5eb-3753-af87-93e027f8cb7d | -7.4477 | -43.0928 | 2026-08-25 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 24a7243b-0524-3051-828b-e74e0e418077 | -6.6226 | -58.4995 | 2026-08-25 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 6426945b-f953-3884-8df9-5bcb53354250 | -6.6172 | -45.154 | 2026-08-25 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 5d6b16e9-0a07-3de5-b2de-726684984c22 | -7.2715 | -45.3473 | 2026-08-25 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| d885f6da-3096-3c72-b170-f861c37b7581 | -7.0058 | -59.2382 | 2026-08-25 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 874770a1-c87e-3ef2-a4b5-0d9ac4827848 | -12.151 | -50.6098 | 2026-08-25 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 7b9c94d5-099a-3a66-a3b4-8d6123119188 | -13.3595 | -48.2051 | 2026-08-25 13:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 113.0 |
| dfc769ba-c4b9-3a46-80dd-67e7d2ae318f | -7.2713 | -45.37 | 2026-08-25 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 4aeefbd0-4bdf-32cf-9eda-aa51d7e90a23 | -7.4286 | -43.1182 | 2026-08-25 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| bdff1af8-37b5-3791-94c9-147bb06cbc88 | -8.1765 | -46.7007 | 2026-08-25 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 3479a4c9-357a-3a56-be33-0f55fd0de54a | -7.4474 | -43.1163 | 2026-08-25 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 364.8 |
| 5ea8992d-daf5-3685-ac62-e06516ca433d | -6.6226 | -58.4995 | 2026-08-25 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 4354fe14-c7c0-3b66-8ee2-ce2601ab1e1a | -7.2901 | -45.3683 | 2026-08-25 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 198.3 |
| 4a186a11-453a-34ec-9c28-d3fa20410d2e | -4.1934 | -54.5755 | 2026-08-25 13:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 0ae2b96d-dcdd-3cd6-a749-3a31ba8723bc | -8.6078 | -50.0124 | 2026-08-25 13:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 509cab12-7625-3f98-be10-38f13e08ce5f | -6.1284 | -57.8588 | 2026-08-25 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 8c571298-f7bc-3206-b593-0bc638c56265 | -6.6169 | -45.1767 | 2026-08-25 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 323.4 |
| 83fe98dd-c7b9-3ab3-afda-682ee16d06cc | -12.757 | -46.4538 | 2026-08-25 13:30:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e2260ff2-8c60-33ab-9e83-5138dbe83ee5 | -6.9872 | -59.2582 | 2026-08-25 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.3 |
| c78a3c9a-ec84-30af-9ec4-fa30a94ce1ce | -7.0057 | -59.2575 | 2026-08-25 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 1ca2f3f0-31ee-3628-a4d3-4c77b66c621c | -6.9873 | -59.2389 | 2026-08-25 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |


[Clique aqui para ver as próximas entradas](README74.md)
