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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 201ba078-8c09-3ccf-93f8-bb380c672932 | -2.52653 | -51.17292 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c3eb8d0-6dc1-30e7-8d88-481c3ab5830a | -2.52582 | -51.1776 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fb9938f-3278-355c-b323-c0a177170d95 | -2.52512 | -51.18228 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f15bedd7-8bb8-3577-9ed9-1a1caeeca27f | -2.52442 | -51.18694 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 907e2672-5043-32ad-b1dc-d3050d9c300e | -2.52372 | -51.1916 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8734407f-b350-37b5-904e-ee1f8f5cf6d5 | -2.52268 | -51.16746 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5613dfe8-a0fe-3836-b9f2-4657b695310c | -2.52197 | -51.17216 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 15babb98-325a-3c07-9110-35379547988d | -2.52126 | -51.17687 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 338bcbb3-439c-3b3b-acf8-07e316d1b712 | -2.52056 | -51.18156 | 2024-10-27 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec78376b-62e5-35fd-b65a-3b63f7403884 | -3.91818 | -52.19374 | 2024-10-27 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecf005fa-ab90-306e-b1f3-a63b412dd76b | 1.07892 | -52.21508 | 2024-10-27 05:16:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75b6f3c5-99bf-3c5d-b1ff-bdb8cb3f3d8c | 1.07489 | -52.21567 | 2024-10-27 05:16:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d368aaa0-a99d-327f-aae1-b92cc94abe59 | 1.0079 | -52.21851 | 2024-10-27 05:16:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2be33d85-7c9f-3ccf-b951-d22d9e851f78 | 0.98848 | -51.98697 | 2024-10-27 05:16:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9dbd7a47-a3cd-343d-8f1f-18dd2f2106cb | 0.9359 | -51.99873 | 2024-10-27 05:16:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f058649-266e-3dc0-9f9f-1460ae6cc74e | 0.92358 | -52.13038 | 2024-10-27 05:16:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f113828-9ee4-3ec5-8ca4-19427690cab7 | 0.923 | -52.12677 | 2024-10-27 05:16:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6de19b9a-b2be-32fd-8ee0-8f9720a23c54 | 0.6925 | -51.44676 | 2024-10-27 05:16:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2aedff7-f830-34f7-b5e7-8a5d7a3f0885 | 0.69222 | -51.44868 | 2024-10-27 05:16:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cec5511f-6544-3505-8f15-76f00725e73c | 0.41744 | -51.4925 | 2024-10-27 05:16:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2013c10a-f8b2-3ef2-b0f8-a3d8a27bcd10 | -0.12058 | -51.6276 | 2024-10-27 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 500e20a6-2a71-319e-9510-4f6eb39e0ae5 | -0.11632 | -51.62693 | 2024-10-27 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1dcb8481-b8a3-3824-a408-8223bf2eb843 | -0.11332 | -51.61828 | 2024-10-27 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1b887d0-897a-3cc0-917f-46bb8308a2f7 | -0.11206 | -51.62627 | 2024-10-27 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80ca0449-eaef-32e6-ba56-b72dd658f4e0 | -0.10416 | -51.62103 | 2024-10-27 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0959827d-c6a5-3348-bf4a-b3f65919ed9a | -1.93316 | -52.09273 | 2024-10-27 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfcd1ba6-0676-3a41-893b-6bd57c0a962a | -1.93011 | -52.08412 | 2024-10-27 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 620d841a-ce08-37b6-976f-c3de0ffc0564 | -1.92951 | -52.08808 | 2024-10-27 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8777904-62ff-34ef-b810-7f39c9bea93e | -1.92891 | -52.09205 | 2024-10-27 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c044fbbf-e169-3208-a77a-3a0ec83b4675 | -1.92586 | -52.08348 | 2024-10-27 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a42a1963-a5a2-3cd8-ad01-c2f1457467a3 | -1.92526 | -52.08744 | 2024-10-27 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f2a75da-e9ca-3fa4-aaf6-c1c9fd4cbeca | -1.92467 | -52.09142 | 2024-10-27 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12a345ac-8e89-313b-b245-1b27e101d508 | -1.88912 | -52.32816 | 2024-10-27 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0189e33b-495c-3a5f-9718-697bfd3f2872 | -1.67174 | -52.04754 | 2024-10-27 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a3fd938-3c58-3d2e-978d-3071a50bc6df | -1.66751 | -52.04688 | 2024-10-27 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3c3c2f2-0f6f-3cd8-9e57-2989b53a23f1 | -1.64125 | -52.941 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2038333a-a5b2-35f2-a0fe-a48efbd72c8a | -1.63726 | -52.94038 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5b73908-ed30-3f5b-8873-1e8e53c67dfa | -1.61412 | -53.32669 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd2a9fdc-9e55-31aa-8e87-a72375854e0c | -1.61338 | -53.32503 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8d21e1f-f5de-38df-9c59-3716e3ba0a16 | -1.6056 | -53.33036 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32fd3a31-0648-373e-a65c-59010029bf25 | -1.60483 | -53.32868 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfaa1ff7-10f3-3c39-8316-a41576572c7b | -1.54744 | -52.14958 | 2024-10-27 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12e5bdf3-5f6b-3a11-bcde-90eabd857640 | -1.4103 | -52.65742 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49f15002-d96f-3443-8365-1e72d6844995 | -1.26786 | -53.0412 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a3f1269a-be42-3f56-9d37-00b6998003ba | -1.26391 | -53.04064 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b296f8e3-4654-3e7c-bb4d-f679aac79c11 | -1.26315 | -53.04556 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| baf31153-d1a0-3474-b64a-c20fff3bef8d | -1.23091 | -52.12274 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e97735d-038f-3c9b-a4dd-bc1969a984d7 | -1.23031 | -52.12656 | 2024-10-27 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b64fdc6-1d5a-3a9b-958d-035145f6d5ab | -3.59064 | -53.09261 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ce9889d-e9ed-3297-a9d0-277af9a569bb | -3.3243 | -52.65565 | 2024-10-27 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa1d9ce3-fcfd-3f94-89f1-dafa5cdebfb4 | -3.23233 | -53.28091 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 582526ca-8f8a-3bb3-bd42-67692b6b1c9f | -3.2318 | -53.28437 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b49f768-439f-35b9-ad0b-e94e5b5d56d4 | -3.11558 | -53.17412 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48621bcc-cf8a-3beb-9313-d87cce4ad2f3 | -3.11505 | -53.17759 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 779df364-6fb5-33da-bfc9-bfdebb206287 | -3.1094 | -53.13358 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 254f8c72-f7fe-3eb9-99c8-670df1cc1a11 | -3.07193 | -53.24564 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31a07aa1-91cc-395f-8a69-00b548c74369 | -3.06793 | -53.245 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c9c62ff-16f9-304c-b6eb-b7af67ba0094 | -2.98476 | -53.26765 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32e3ced6-1c0c-3a61-8be7-73c574c8b92b | -2.98128 | -53.26368 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb871287-18e4-39f7-abdd-8607c95572b2 | -2.98077 | -53.26708 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab37eff1-c68a-3b0b-b410-2c658e8ed4fb | -2.97677 | -53.26653 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f288ec8-fdc7-35d6-bf24-020ec80425a1 | -2.97278 | -53.26596 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31c4a844-b888-38f6-b66e-22f08f61b116 | -2.97029 | -53.03624 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1d504436-41ba-3a42-9d7e-aa1143d1b119 | -2.96977 | -53.03975 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9645887-e9cb-3dde-a755-42e8c5e7b8f2 | -2.96925 | -53.04325 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc60ce36-631d-376f-a573-4110a2b98fc7 | -2.96872 | -53.04677 | 2024-10-27 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fcf2aa9d-8890-35d7-bf62-d2251c899ec0 | -2.83893 | -52.54937 | 2024-10-27 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 978518d1-a189-37d4-8663-72ffa2ecc1e8 | -2.05589 | -54.63189 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7c18f01-c292-393b-b8eb-8afe227a0291 | -1.95678 | -54.40399 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e900ed40-5b69-3ffc-820b-2380bf5118f8 | -1.93282 | -54.5578 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1e5ebb0-7235-318e-b096-5220377720dc | -1.79023 | -54.26513 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4332fb80-a3bd-3a44-bbcc-47418322ab5b | -1.51701 | -54.779 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f1c3fb9-a895-3898-bbed-0d6d30ac7bbb | -1.51343 | -54.77844 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95c3b13b-7d8a-3143-affb-d89b5a09002f | -1.51281 | -54.7825 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f58e6fd-59c4-3149-96c9-7e1737f7da91 | -1.45741 | -54.28897 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfc5e595-e8a2-3356-aef9-e1007293794a | -1.4537 | -54.28863 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bcadf26-c941-379e-9108-212f7c670410 | -1.45302 | -54.29296 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cf2e6d0-2c9d-3cd5-b1fe-999dadb1bd54 | -1.43722 | -54.07943 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee438aa0-9928-3b0e-9e52-48db5db07169 | -1.4342 | -54.0743 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27d683d3-cca3-3d15-9a9a-1e16e8f605f1 | -1.4335 | -54.07887 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d5d0e42-f9af-3f12-8a56-12a7876222d8 | -1.43187 | -54.06474 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8499e649-ef63-3096-856b-2ca627619ead | -1.4314 | -54.4838 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c071e864-00f2-35be-bb6b-43bd57b55de1 | -1.43013 | -54.48541 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 958f19f2-0274-3820-9d47-ee3c4eed4016 | -1.4272 | -54.48047 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9bd2d94a-dda9-3afe-8339-7e52373c0a95 | -1.4035 | -54.05129 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 478b0528-17b8-352e-a323-df160bb45e96 | -1.38898 | -54.17139 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75f6f183-f945-3b84-a4d3-156c6924ea61 | -1.35128 | -54.61087 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a98ef0a-784f-3ba6-ac5b-7291e55662f9 | -1.34976 | -54.64444 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3ed9ec9-36e6-36e8-9221-4d5508dee77b | -1.34767 | -54.61035 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4eb1bacc-f6f8-3427-a6a0-4adc17558dd0 | -1.3468 | -54.6398 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d324f656-958a-3a2a-bdb4-64a5efb10e51 | -1.34407 | -54.60982 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 214eb5b6-021e-3209-97ff-6d2fe9eebdae | -1.34342 | -54.61401 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 830efad2-24e4-3ca9-a11a-2ee7f33a434e | -1.3432 | -54.63926 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6db918f7-3538-38d0-8cd9-094106f48adf | -1.34046 | -54.60927 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 848cc09f-c9e9-33d1-9a24-521039b36856 | -1.34023 | -54.63464 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3770b63e-fa2d-3af4-ae9b-6a8af0f61b8a | -1.3396 | -54.63874 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba7c99c0-9f8d-3a3d-81b4-f99a1f93f297 | -1.33663 | -54.63411 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70d3d05d-326c-3729-8a64-e585c99adc91 | -1.23271 | -54.14341 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31687013-92b6-32ec-905a-937898994905 | -1.18475 | -53.90236 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96a90e9f-a211-34d1-acde-d0288374bb30 | -1.18101 | -53.90177 | 2024-10-27 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README60.md)
