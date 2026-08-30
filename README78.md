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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0683d90d-63d8-37cf-9e0d-b3f0e732aa3c | -7.5136 | -55.3251 | 2026-08-30 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 165.8 |
| be836f20-8386-364f-9e9f-9bf70ff6fdfe | -7.9422 | -44.277 | 2026-08-30 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 199.4 |
| 590b68fa-3834-32bf-9c16-8ea773afbd36 | -14.1456 | -52.8082 | 2026-08-30 12:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 8230b950-7afa-3880-9802-c48a5ab9d70c | -12.3619 | -48.1903 | 2026-08-30 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c2c34f98-02df-31a0-a3bc-2866f44c3973 | -7.5323 | -55.3041 | 2026-08-30 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| fa8946c0-d4cb-3cf4-bf5f-aea02cefcb4b | -4.9604 | -55.8424 | 2026-08-30 12:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 50be6520-c96d-3b84-8301-1c314172cabc | -11.2443 | -45.3497 | 2026-08-30 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| cb2ea200-1725-3288-a967-5358fc41fa6c | -12.3811 | -48.1877 | 2026-08-30 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 063f3443-e9ad-3e70-8999-93045c6aa9ad | -7.9611 | -44.275 | 2026-08-30 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 312.4 |
| 8f9784e3-5d78-34b5-8eae-093ab4ab144b | -14.4197 | -52.5413 | 2026-08-30 12:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 6ddcb846-eeb2-3436-ad0e-2397fe54aec1 | -14.9383 | -56.342 | 2026-08-30 12:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 85ad30d8-35d8-3d1e-9696-0569d006b47f | -6.9361 | -55.7157 | 2026-08-30 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 61907b47-ed59-3566-a490-bdaab1752da9 | -6.8753 | -59.4557 | 2026-08-30 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 84da9735-a5ef-32ef-a344-d5cd15cf2930 | -7.5137 | -55.3051 | 2026-08-30 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 348177fb-a418-30e4-8c24-aa312732fa2b | -7.9419 | -44.3001 | 2026-08-30 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 600ce668-a444-3a03-bce4-a584c8723baf | -10.7454 | -50.6812 | 2026-08-30 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 5059c8b8-84f0-32c3-90fb-c306ed29f146 | -11.8211 | -51.0322 | 2026-08-30 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| f45fbaa9-4027-311d-a846-c8730fc0594d | -14.1649 | -52.8058 | 2026-08-30 12:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d418986e-3694-3a19-95af-179a3c96dfd2 | -7.9425 | -44.2538 | 2026-08-30 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 04d81468-175b-342e-8ebc-723a1590fb06 | -11.2503 | -54.0146 | 2026-08-30 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c5897cb7-497f-3fce-b4ff-48b055b5faa1 | -11.2638 | -45.3241 | 2026-08-30 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 9632f983-6428-3967-8a27-4f2201585769 | -7.6152 | -44.8605 | 2026-08-30 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 55c0cee9-caea-3bfe-aa1d-faf351b2bbee | -10.1538 | -45.6982 | 2026-08-30 12:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 173.2 |
| cae3e3e2-2835-3094-b498-026eb4659093 | -8.1534 | -45.4904 | 2026-08-30 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 6ba092fb-c25b-30f7-875e-3800833d6981 | -14.1459 | -52.7871 | 2026-08-30 12:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 77e6fba3-8b06-3045-8ca1-7f3a200971b0 | -8.6156 | -54.7743 | 2026-08-30 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e5350ec3-9a11-3911-a677-50aa61f0dca2 | -6.8568 | -59.4757 | 2026-08-30 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ceb08f30-dff7-333f-b8d2-584e40a13e6f | -6.8752 | -59.4749 | 2026-08-30 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 239.7 |
| 9886b2e6-13e0-3bb4-9341-b6499c8f88e9 | -11.8211 | -51.0322 | 2026-08-30 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| d2285c70-d089-3496-8d0e-438702950a5e | -14.1649 | -52.8058 | 2026-08-30 13:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 138.2 |
| e54505c6-b72f-3f26-9b90-5cf661c723c7 | -6.8568 | -59.4757 | 2026-08-30 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 6fec500e-975c-3f02-817b-e6734b5f62a2 | -7.5136 | -55.3251 | 2026-08-30 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 271.3 |
| 5914fb31-265d-3b68-9d86-8d6713737923 | -8.6156 | -54.7743 | 2026-08-30 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 22cfc664-b330-3482-b1cb-deca789e26c0 | -11.2317 | -53.9958 | 2026-08-30 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 455559cb-7897-3879-a0c6-eb0b91ee1513 | -14.4387 | -52.56 | 2026-08-30 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 97c7ac05-6706-35f7-aa6e-f6d6d78f9149 | -7.5137 | -55.3051 | 2026-08-30 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| a22fbb11-a068-30ae-9357-fb1609de62d5 | -8.2229 | -54.9412 | 2026-08-30 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1a627b1c-6cd0-321a-b917-f9a314999355 | -11.2443 | -45.3497 | 2026-08-30 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 254.3 |
| fad90550-6457-3f60-b76b-c973628552ea | -7.9419 | -44.3001 | 2026-08-30 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| f292bbba-7c48-3033-97f1-3d6b6b81dea4 | -6.8753 | -59.4557 | 2026-08-30 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| bd20be22-745e-36aa-afd3-b130750e1d88 | -13.3943 | -51.7595 | 2026-08-30 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 636c2e86-a09c-3e47-8241-009031ca5891 | -7.3001 | -46.1778 | 2026-08-30 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 672f5775-1b30-3392-a0fd-2f7e9674ed97 | -7.5134 | -55.3452 | 2026-08-30 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| b2b6bb73-9f69-3d65-ae31-bb005e0b712a | -11.1726 | -51.2728 | 2026-08-30 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 1b0462c2-c507-38b7-85cb-0a280f65e4fd | -14.1456 | -52.8082 | 2026-08-30 13:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| d1b152aa-6203-3d1a-b606-972d5ba5d3ab | -11.2314 | -54.0164 | 2026-08-30 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| a53338c2-feb8-33ff-a347-c3ba07b54851 | -4.9604 | -55.8424 | 2026-08-30 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 174.6 |
| b68d623d-41c6-3c3e-8762-e1347f36de54 | -10.1538 | -45.6982 | 2026-08-30 13:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 4bd99004-1853-329b-bb1b-297e038e3cf2 | -8.6154 | -54.7945 | 2026-08-30 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| cbaa05f2-09f3-3437-a0d0-226db2b8fe4a | -14.1459 | -52.7871 | 2026-08-30 13:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 77201ed3-fe9b-3e14-8337-b6c9a480aeec | -14.4004 | -52.5438 | 2026-08-30 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 18b20e76-3b0d-3d39-afe6-f30aea828d03 | -7.9611 | -44.275 | 2026-08-30 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 320.9 |
| c7b3f135-9285-3b71-95fe-9fdb29e9d286 | -12.9216 | -45.8812 | 2026-08-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 3fb039f6-76f5-3da3-9bbc-c6c51607f290 | -4.9603 | -55.8622 | 2026-08-30 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5de35d57-e2bc-32ff-ba62-00a68cbf81f8 | -7.3118 | -60.5897 | 2026-08-30 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 172.6 |
| 3d247e16-cc59-3238-a6a7-c6a0b46ddf06 | -13.8749 | -54.1361 | 2026-08-30 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 2485a30b-5dad-3d3a-82b3-48ce74522894 | -7.3302 | -60.589 | 2026-08-30 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| e257e526-312c-33fb-af31-605fa41583fb | -7.5323 | -55.3041 | 2026-08-30 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| d0f39185-0fe9-3efe-a5f5-186e4a54be2d | -7.9907 | -46.5177 | 2026-08-30 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 8fad146f-a1ca-31da-9eff-23678ac8c2d0 | -10.7647 | -50.6579 | 2026-08-30 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d6057406-bad6-308e-a3d1-2c06bf766087 | -7.9425 | -44.2538 | 2026-08-30 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ab09907d-3f86-39b5-8709-df388f8155e8 | -14.4197 | -52.5413 | 2026-08-30 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 166.6 |
| f36dbfe2-12b0-32e6-82b9-606f138aea10 | -11.2503 | -54.0146 | 2026-08-30 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 6bd38704-6365-3b1d-b141-2ddba4c46272 | -10.7454 | -50.6812 | 2026-08-30 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| b34cd8df-4e3f-304a-9734-63919c7f3df7 | -8.1534 | -45.4904 | 2026-08-30 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b2621deb-438b-322b-9268-a00ec8241882 | -7.9422 | -44.277 | 2026-08-30 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 3b192e42-b0f4-3dcc-8948-2466f73022ee | -14.4193 | -52.5625 | 2026-08-30 13:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ea716a10-0e01-33a6-b566-d65c55333f9f | -11.1534 | -51.296 | 2026-08-30 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 68ab35a8-15d3-36de-9b3c-0cc94a9ba543 | -6.8569 | -59.4564 | 2026-08-30 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b2e5123c-608f-3cc8-a015-ae3a5c4a195d | -4.8704 | -66.89321 | 2026-08-30 13:08:00 | TERRA_M-T | CARAUARI | AMAZONAS | Brasil | 1301001 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a35701b1-fc21-3875-af2c-f7665f9fcbf5 | -5.87829 | -57.7635 | 2026-08-30 13:08:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 136bf369-fc39-3d1f-96fd-f0b42778faa8 | -3.63354 | -60.56798 | 2026-08-30 13:08:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 60a9bc1b-faed-3fe6-b508-0a1a46625ccb | -3.63645 | -60.5459 | 2026-08-30 13:08:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 32.5 |
| fdc845f6-123e-3577-acf1-3c1ac5fa5e43 | -3.25729 | -60.64819 | 2026-08-30 13:08:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 3aea935c-43d3-3a93-8963-e89d250738f4 | -3.2612 | -60.64216 | 2026-08-30 13:08:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 48b51e6b-3200-331e-9ff3-7c93b1465514 | -6.16772 | -57.78155 | 2026-08-30 13:08:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 9ed99001-072e-32d0-93bb-2475b00cb9e0 | 0.13508 | -60.39447 | 2026-08-30 13:08:00 | TERRA_M-T | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| bd875e5d-dd9c-321a-a33d-146f31ac5c9e | -5.8804 | -57.76876 | 2026-08-30 13:08:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| b262bf42-c230-3adc-8fbd-7ea5ff9590f4 | -4.15652 | -60.68821 | 2026-08-30 13:08:00 | TERRA_M-T | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| b6655b5e-c124-3299-97dd-9b04a2cba925 | -3.63877 | -60.56185 | 2026-08-30 13:08:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 00a84a3a-417c-3539-9137-d28d77b8f276 | -12.3619 | -48.1903 | 2026-08-30 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 84d4ba76-99bd-3134-b49a-b5c0b8d32d2c | -6.861 | -41.6772 | 2026-08-30 13:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 1292bb04-9c5d-33a7-9bf7-531e544485dc | -4.9603 | -55.8622 | 2026-08-30 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| d50c4d88-5d55-354b-9607-c8f417624aac | -10.8425 | -50.5005 | 2026-08-30 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8ac33946-394b-3b1e-bb4d-7073fe790ecf | -11.2443 | -45.3497 | 2026-08-30 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 567.7 |
| 24a7e72c-b9aa-3449-8f19-b66cd2bd6cec | -8.1534 | -45.4904 | 2026-08-30 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c778ac29-82ee-383e-8d7c-bcee4d83a577 | -7.6155 | -44.8376 | 2026-08-30 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| ed1d1402-e121-3815-9876-2451d03ab0c1 | -14.1649 | -52.8058 | 2026-08-30 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 748875a1-31f0-33bc-914e-d929be2fe171 | -8.2229 | -54.9412 | 2026-08-30 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| da0ce8f5-a224-362a-b3c5-bc978156e03e | -11.2506 | -53.9941 | 2026-08-30 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 47cf75b3-49e7-30b8-8b5e-fa17e288d01d | -11.2294 | -45.099 | 2026-08-30 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b5e02d9d-bf69-3656-825e-41bfdc6e639e | -7.5134 | -55.3452 | 2026-08-30 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 33697c9e-3058-3407-a12f-e9754bad04da | -8.6154 | -54.7945 | 2026-08-30 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ab090671-5649-3acc-aace-f0347375c502 | -6.8752 | -59.4749 | 2026-08-30 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 214.2 |
| 8d298d08-ff31-370a-8e81-f7b31b89492b | -11.2634 | -45.3471 | 2026-08-30 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 584e22cd-ab4c-33f8-9ca2-2d988787e1a3 | -14.4004 | -52.5438 | 2026-08-30 13:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 758c1f72-1577-3437-b55e-b6cb3a6ec37f | -12.9216 | -45.8812 | 2026-08-30 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| e0f07554-084f-3484-a6b6-320dc422ee46 | -11.2317 | -53.9958 | 2026-08-30 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 8f9df88a-1a46-3254-af18-4d204727e9be | -14.4197 | -52.5413 | 2026-08-30 13:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 177.2 |
| bd0f4f54-832c-35ca-b280-143e45fc0b91 | -14.1459 | -52.7871 | 2026-08-30 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |


[Clique aqui para ver as próximas entradas](README79.md)
