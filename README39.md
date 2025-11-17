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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bfe8e6c-a500-38e7-9304-40c2e8fe6c91 | -11.61539 | -48.56989 | 2025-11-17 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 518b4b35-f2fb-3985-a328-a9bde5dcca72 | -10.82103 | -44.31212 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c7ad27cf-bf00-30b3-a26f-d6ccb18acdc4 | -10.9287 | -48.68439 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 512b254a-48fd-3b36-b58d-4098782c01ba | -13.6987 | -47.58866 | 2025-11-17 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 775e281a-2a53-3443-9e1c-ef23d70faf83 | -11.70905 | -48.85915 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e775129a-9468-37fe-9244-eaf515424795 | -9.51249 | -47.26692 | 2025-11-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62ed7c22-b9bb-30bb-9653-c2a78ac52dbf | -12.2011 | -49.63162 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf6ec172-7bfc-309d-afaf-fa53c0d75cf2 | -11.15972 | -49.4427 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b655aa6-3cbf-3ef0-b94b-755f721922d4 | -10.91187 | -44.84258 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 00fc2551-689d-3ff6-a6a0-605a0cc54917 | -12.85291 | -46.46412 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cb50ce3-2363-34ad-8d27-111f620ff869 | -12.38382 | -43.77654 | 2025-11-17 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd72a005-b8c0-34f9-94f6-8d337bee8f80 | -12.87296 | -46.433 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39eaca80-8adf-38db-b9ce-cd2cd8dc464d | -12.63489 | -49.13634 | 2025-11-17 04:40:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2019a6d-dbf4-3116-b868-16f07b5d256b | -12.98374 | -49.79901 | 2025-11-17 04:40:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79b17398-a674-3ce8-b1e2-4964b6e44768 | -11.71812 | -48.86811 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1a2d8a9-7a65-30ca-8f49-341e14083a12 | -9.81573 | -48.58242 | 2025-11-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7420658b-0fe0-3a81-81e8-63be91683513 | -10.91957 | -49.41217 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| da7e2327-7e59-3005-8fb5-bc1e4fb7c781 | -12.69815 | -46.76952 | 2025-11-17 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96abfad0-28fe-3c9e-8acc-a4fecafd1c27 | -11.72695 | -49.84156 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0a48ff1-4a93-304e-8b00-ea4dc9bc3d0e | -9.51779 | -47.47126 | 2025-11-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d27747d-dad4-36d1-a1f4-571e18110fa3 | -13.72904 | -51.45839 | 2025-11-17 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 396ca5a3-f5e3-37d5-aaa0-9a2f3c963c59 | -11.34434 | -48.90158 | 2025-11-17 04:40:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 487a97d3-52a5-35aa-a9e4-5d840b4ee534 | -11.96509 | -44.93709 | 2025-11-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f656b79-c801-3066-aa57-ccf185b234e5 | -22.10929 | -48.2675 | 2025-11-17 04:42:00 | NOAA-21 | DOURADO | SÃO PAULO | Brasil | 3514304 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c69b520d-3fbb-31c6-869b-a72ba145ff54 | -6.6875 | -42.0296 | 2025-11-17 04:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| f6059b6c-1ca3-3ebb-8eaa-435ad6a69d06 | 3.7808 | -51.81254 | 2025-11-17 05:03:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2549b387-9b64-354b-b411-3227e2df00c9 | 3.7774 | -51.81309 | 2025-11-17 05:03:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b4ce3c5-aa9c-3968-a8b5-639321ac6ba8 | -2.64371 | -49.10238 | 2025-11-17 05:05:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7df6478a-c408-389f-841a-0ebc9c040f4b | -1.26506 | -55.39592 | 2025-11-17 05:05:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 23f60c8e-2009-3479-9cdb-76f4c1a7b0fc | -2.17772 | -52.08868 | 2025-11-17 05:05:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13a9545b-cae8-36ee-985f-b880612f9e2e | 1.00981 | -59.51783 | 2025-11-17 05:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50633edf-ce0f-396b-a3c1-1029208d9269 | -2.58666 | -51.83258 | 2025-11-17 05:05:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c6e11d8-784d-38f5-b868-d9e4aa2a44a6 | -3.34605 | -43.49163 | 2025-11-17 05:05:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b6275c9-787a-398a-bd92-0f7b15e737b0 | -2.24911 | -53.61958 | 2025-11-17 05:05:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ea2b366-021f-3a89-bb7d-f6ab5d0d4a31 | -3.07878 | -45.19742 | 2025-11-17 05:05:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17108ef1-19b9-3f5d-a23d-e116cf263e52 | -0.82197 | -48.64896 | 2025-11-17 05:05:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 227f7396-9232-3120-9cf8-c4c7c4304e0e | -2.53205 | -48.95852 | 2025-11-17 05:05:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c8e7635-8e64-38f4-bf66-41fe586cbf16 | 4.52091 | -60.88773 | 2025-11-17 05:05:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cc57b0b3-f49f-332c-9933-51dcbbb2cdc6 | -1.46467 | -55.22427 | 2025-11-17 05:05:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0625b107-d6a6-374f-952b-db8c4475e656 | -2.50818 | -47.82015 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 56070c84-fcba-3d77-b2b0-4872da959e7b | -1.46627 | -53.41898 | 2025-11-17 05:05:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 031b5b7e-4718-39ec-b73b-d9d5341b85a5 | -1.50975 | -54.81055 | 2025-11-17 05:05:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f933a2e-be52-354e-8167-7e35138ef748 | -2.24463 | -53.62616 | 2025-11-17 05:05:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ecf16ea2-9812-3568-b4f0-1ad8a4f540ac | -3.59695 | -43.5999 | 2025-11-17 05:05:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf295085-49f3-3feb-bc8e-c41afe3eba55 | -0.82625 | -48.64964 | 2025-11-17 05:05:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fff12d78-9fd0-3efc-bc95-3e610dd863eb | -3.35001 | -43.488 | 2025-11-17 05:05:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 97699698-49fa-3694-bdfc-ff63ccbcfa2c | -2.47254 | -50.24073 | 2025-11-17 05:05:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fde6a1e-7c7c-399b-aae4-b381e72ed195 | -2.66839 | -51.88171 | 2025-11-17 05:05:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5119cbe4-7a37-32ab-98fa-3f63d8361fcc | -2.24519 | -53.62261 | 2025-11-17 05:05:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b58b854-a74c-3f8a-a1fa-1fab9d5412bf | -3.37779 | -46.06864 | 2025-11-17 05:05:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43f83496-4e20-3e96-b206-7ce118b28ca3 | -2.45451 | -50.27901 | 2025-11-17 05:05:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87f44292-b485-340b-be17-aadf9a0828dd | -3.34925 | -43.49324 | 2025-11-17 05:05:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1dcd02f0-057d-31a0-bf85-47a2af4b1f7c | -2.23028 | -51.79886 | 2025-11-17 05:05:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4915e237-67be-3fb6-ae35-0f2b6e8b979d | -3.66385 | -44.73147 | 2025-11-17 05:05:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bf3e9c8-cae9-372b-9ff3-fa4a8a99c7de | -2.00141 | -50.52068 | 2025-11-17 05:05:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16282995-514e-3d2e-a91f-a49d4ed77068 | -3.658 | -44.7306 | 2025-11-17 05:05:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e067989b-b0d7-36f5-a7ce-2fe997e57171 | -2.50891 | -47.81532 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a9215ea4-ab28-3d2c-8492-de33d5fc5dae | 0.73489 | -52.05659 | 2025-11-17 05:05:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f76097d2-6518-3b6e-9215-c1519e6434b4 | -2.58731 | -51.82848 | 2025-11-17 05:05:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf80cd7d-2c5c-3614-ac37-f73a961c342e | -3.59065 | -43.59913 | 2025-11-17 05:05:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1edc226d-3983-31d1-9bca-bb3e1b38e8b1 | -1.66147 | -53.67369 | 2025-11-17 05:05:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84eeac00-e816-3746-b62c-c917ae447242 | -2.23701 | -50.52198 | 2025-11-17 05:05:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fca8cdda-411b-3027-8878-f781536b701a | -3.22179 | -43.35884 | 2025-11-17 05:05:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 426b6854-d913-30a2-bd98-ad43e51cf0e7 | -2.51821 | -47.81688 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d36b7a45-7514-3f36-b17d-c3bef64917ae | -2.51356 | -47.81614 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0f4ba36d-ab20-3d80-8f54-68587a981d1a | -3.33865 | -46.28823 | 2025-11-17 05:05:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6716b61-ffff-3288-8f82-5ee53436d208 | 0.72838 | -50.72398 | 2025-11-17 05:05:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d778cd1e-accd-37a9-983b-778b3f2ed55a | -2.66144 | -49.07249 | 2025-11-17 05:05:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0522eea4-a77d-370f-bbda-07b3ee522a65 | -2.7567 | -48.42385 | 2025-11-17 05:05:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ac717de-4f81-3198-a6d5-bf29ef53502c | -2.80746 | -48.67898 | 2025-11-17 05:05:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a043963a-15ee-39cb-b911-99a82b3574d7 | 1.63065 | -55.95868 | 2025-11-17 05:05:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc03c7eb-b607-329b-a836-50bb65dbffcc | -2.6855 | -52.06728 | 2025-11-17 05:05:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0ced2dd2-6935-3f56-b969-897c4f92bfff | -1.77246 | -56.16624 | 2025-11-17 05:05:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2056b52d-61f4-38c7-bc92-704580913732 | -2.01581 | -51.404 | 2025-11-17 05:05:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54e7561d-2f02-3013-8fce-bb05ee5a178e | -1.69442 | -53.68243 | 2025-11-17 05:05:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22aa45b9-1954-30db-8a2d-6bb2e9e48979 | -1.30278 | -55.71432 | 2025-11-17 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ab42526-7a61-35c8-981e-84176f5afdb2 | -1.34858 | -54.609 | 2025-11-17 05:05:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0716f463-bf03-33f4-b7b4-0d497470f914 | -1.41508 | -54.46776 | 2025-11-17 05:05:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 668ff092-c8a1-3007-8472-9ef9e381ef63 | -1.1786 | -49.19208 | 2025-11-17 05:05:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54962cc1-eef9-3442-ab01-c4f1432994fb | -3.07567 | -45.20326 | 2025-11-17 05:05:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8a8122e-f5e2-3e3f-a6c4-87e6ed1bd00c | -0.75543 | -48.63575 | 2025-11-17 05:05:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb8885af-97eb-355b-9591-7917c28b72c9 | -2.68907 | -52.06783 | 2025-11-17 05:05:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a878e56-036f-3d6d-adc2-bedbd150d383 | -2.43256 | -52.12165 | 2025-11-17 05:05:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8bf879e2-d3df-35eb-ace6-f72256666df8 | -3.58993 | -43.60399 | 2025-11-17 05:05:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a177a6e-d10e-30f7-b65d-233ec67e33bb | -1.97931 | -51.99867 | 2025-11-17 05:05:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e0235c93-142d-34e0-9803-eff9a4887c01 | -1.0605 | -53.02703 | 2025-11-17 05:05:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 11451f6e-56d5-3fc9-97bb-818604c53076 | -2.24574 | -53.61906 | 2025-11-17 05:05:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ba89c01-e24b-3822-8b83-20ce570785d8 | -2.50427 | -47.81451 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ca54a5b0-6fa6-3953-8a3e-7f4451d5ac49 | -3.1507 | -49.42349 | 2025-11-17 05:05:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e2d6488-ebe9-384d-890c-cc2305ee1a43 | -1.53306 | -55.51989 | 2025-11-17 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c84f0a2-4a25-3236-a394-c44bc5885bff | -3.07317 | -45.19652 | 2025-11-17 05:05:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6891f80-c56a-3197-b081-931ae812511e | 4.52134 | -60.88508 | 2025-11-17 05:05:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76bea3d4-a2b7-37a5-b3f0-6a3a5e7c2103 | -1.1191 | -54.11409 | 2025-11-17 05:05:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b34b889-40a4-322e-a888-ab01608c4ae7 | -1.46347 | -53.41489 | 2025-11-17 05:05:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44937894-1f2b-3c84-8cdb-5c2c169ea88e | 0.23432 | -51.0153 | 2025-11-17 05:05:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c2d89e28-76ad-361a-be74-e660d9052ec5 | 1.6427 | -55.96825 | 2025-11-17 05:05:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 187bdf48-7430-3a04-8536-3ed3ff470a09 | -2.01647 | -51.4059 | 2025-11-17 05:05:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b344f199-a78e-3838-a8f3-b3f726d788ea | -0.89884 | -57.17218 | 2025-11-17 05:05:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6004484e-d045-37b9-91d4-2396556574fe | -2.47332 | -50.23569 | 2025-11-17 05:05:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 916cd655-fd09-333f-8a56-f96a978616fb | -3.07622 | -45.19951 | 2025-11-17 05:05:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README40.md)
