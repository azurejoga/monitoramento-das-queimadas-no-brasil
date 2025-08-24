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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a16f7064-dca0-3737-ad7e-76d412b94f41 | -8.14051 | -62.86584 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3170102-94ff-342b-b901-02503a40adba | -9.19812 | -59.65254 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 598477c2-932d-3463-afb3-fc8e7fbf5d14 | -8.13494 | -62.86786 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b518e771-9c1a-3a73-9d84-29180bc81933 | -9.23619 | -60.92466 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fded129c-4639-3e85-b193-78e148831c69 | -7.79109 | -61.57677 | 2025-08-24 04:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11f83739-f12a-3d3f-83b5-d0d05792e9a7 | -8.75619 | -46.75606 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e500c00d-a135-3264-a1eb-9d4b82b76c52 | -8.89794 | -62.44276 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39c60dd2-d6a0-3170-aaf7-831908e4f9d0 | -9.15154 | -59.45971 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d8f9c677-fa8d-3053-aa99-4903b10bb5e5 | -8.01447 | -45.49146 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e14e76df-7dce-340a-a78c-1776989def8c | -9.15776 | -59.47132 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6e29ac47-235d-332e-aa7b-6c166c9b3fb1 | -6.74847 | -62.86861 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5cf8980-8017-3d9e-a478-4ca6cde2b37a | -6.6291 | -58.54083 | 2025-08-24 04:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb21a877-927b-3b7b-b3d2-2cc77dd9de07 | -8.61048 | -62.64242 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ec50518-6a23-32e8-a713-80c08d403923 | -9.19496 | -60.77282 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6da8b2e-fdf5-333b-ac9b-033e82548528 | -6.57889 | -59.87695 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81d89c81-59b4-3821-a3b7-be3a01a8f51f | -8.90279 | -62.44366 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6242ad57-5d32-334a-803d-787a636ca85a | -8.76597 | -46.7576 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 22f0bf9e-501c-36a8-a286-e68e276055ba | -9.15373 | -59.50479 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c79e2f6a-fb33-3455-a981-a5ccc472f04d | -9.17884 | -59.69276 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0feb6cfe-099d-32cc-884f-701837a2c032 | -10.81824 | -46.39657 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ebb18be-61f4-3ca4-91a7-1a309ee9bfcc | -9.15949 | -59.49522 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 75e2212a-c0d9-3c9f-b212-dbb67a500b67 | -8.63329 | -62.62929 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5062520a-b751-3739-8d0d-01342d4567f8 | -8.13597 | -62.86193 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2261b415-36d4-33d6-ad19-fa087c03534d | -8.88436 | -62.43471 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74f2eee8-911e-3ed3-8ce3-5fa62d4b6f93 | -9.15387 | -59.45723 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 92debd45-19e3-3f10-a1de-646c43af628b | -9.15551 | -59.46039 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 51e3f601-1b4a-3eb6-8ddc-d297e6c27aee | -5.80682 | -59.22245 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bde429d9-17e0-384b-84c8-b1c8cef94d1c | -7.07087 | -60.05931 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 262b7b34-e051-3d98-84c2-9f642e5a236d | -11.3104 | -47.85158 | 2025-08-24 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ec6f364-c96b-3edd-af87-b5aec6d077d2 | -11.28059 | -44.97906 | 2025-08-24 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fde430f-140b-3d9c-9caf-463d217a0273 | -9.23103 | -60.92547 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54b56622-a7d5-3250-ae2e-52b2cfc9b500 | -9.16628 | -59.59786 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ed034ff-a940-3849-9f16-ba4238780e04 | -8.74481 | -46.71854 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97924cee-d049-3a90-870d-3670eadfc54d | -9.19161 | -59.61827 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4faa5331-7413-3158-83ef-b45db40f0e00 | -6.78232 | -59.64465 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0372a2f-5522-33f3-8de4-2486f1bdc25e | -8.9139 | -62.10869 | 2025-08-24 04:59:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee41ba10-8b40-32fa-8b2e-910bec3619e5 | -8.22175 | -45.11463 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0485125d-3287-3e50-a2af-51da5b55e861 | -9.2493 | -60.48742 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49c9e331-c3ca-3ae2-9cf8-7954a35fd148 | -9.15379 | -59.47062 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a4559e1e-c74c-32e5-bd42-a45943125f51 | -5.76508 | -59.88225 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f825e0f-4e18-3e46-a27f-386115085a76 | -6.65476 | -55.42069 | 2025-08-24 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a8a818d-d225-3ce7-8c62-92cdd9d73e73 | -8.01975 | -45.49226 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69a49994-bbac-3584-b77d-94a4a0554bfc | -8.89406 | -62.43649 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6175d58-daaf-32b6-9304-b2d4cfd84fd5 | -9.17771 | -60.76974 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4761ef8a-2ef2-30c5-9892-e32c375baa94 | -6.91713 | -52.85403 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 772fc2ce-fb53-3263-a23f-2c81a95186a9 | -7.91604 | -63.04774 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d080cac1-76d6-371f-a024-2392dc1218ed | -6.68317 | -58.85885 | 2025-08-24 04:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 19ee1295-b805-340c-97ef-771857452602 | -8.85845 | -48.52309 | 2025-08-24 04:59:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 875ff9d3-d236-37a3-9967-306bf66d607d | -5.61411 | -60.23975 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7eb33d35-31ea-3398-883c-8e1641162cef | -11.32905 | -47.85579 | 2025-08-24 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13ecf260-0571-3250-a9cc-a4ec2de0f55b | -8.61243 | -62.60025 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b89709f-316f-32b6-b926-fb25c198b462 | -9.17519 | -59.59398 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23a9eb24-47b8-3655-9413-bc3cbe203b06 | -7.80753 | -62.34022 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 492f068a-7a0c-390f-b9ed-0a8b762ccf22 | -10.82265 | -46.40331 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2ad50df-4a4a-3526-b9c0-d6175c77ebca | -9.12517 | -60.33035 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b19e050-7f78-3422-8068-74cf2ac31ca1 | -8.60946 | -62.64803 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e613d9f6-4938-3e39-9a73-a1c7bb2046ad | -7.75052 | -47.35255 | 2025-08-24 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 415dd141-a4f5-3f3f-8786-97044e9b8bbb | -8.86333 | -52.04321 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68757e33-0fc0-37fe-aecf-64ea57ee4dbf | -11.33384 | -47.8559 | 2025-08-24 04:59:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f25734ac-8091-3644-a322-58eaeb111704 | -8.61763 | -62.60332 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7088c97-de73-3d33-b5a6-9afa752c59f8 | -7.57164 | -63.44097 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc133266-d3ae-39ba-9d0c-66eabc8b774f | -9.20274 | -59.48158 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 334fe364-bfec-3889-beba-de701b153194 | -9.16719 | -59.59262 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 70471936-bcaa-31b3-8c15-543bd5a62bd5 | -8.89018 | -62.43021 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d9a00c9-e369-3f08-897c-e17681479941 | -9.0297 | -59.01402 | 2025-08-24 04:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8407676c-9e7b-3137-96de-4479648ffad3 | -9.47806 | -48.18412 | 2025-08-24 04:59:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a35c840f-2a33-315c-83c0-417cd3877e83 | -8.04237 | -45.00048 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe6ec52a-794e-317b-9bcb-dea7b3f35cca | -9.20758 | -59.47717 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 509aa82f-f167-312c-85ba-bc49cee4c404 | -6.63299 | -58.54148 | 2025-08-24 04:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e893f85-83fb-37f6-ab81-92f2f74abe09 | -9.84464 | -56.07666 | 2025-08-24 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7afa6432-704e-303c-9ad1-47bf528b7327 | -11.11122 | -44.78042 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e373f2a7-0e24-356f-b478-baf37a89f05d | -9.15641 | -59.48943 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c6d57c6e-6ff4-3a33-9713-432b247feab2 | -9.16086 | -59.47718 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 67450b45-768f-3c14-a954-144b4741c9ec | -8.7572 | -46.73709 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb22b69d-57e3-373a-ba12-52b5dc885373 | -7.97389 | -63.08072 | 2025-08-24 04:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a5e6b284-20a6-335d-a7a0-9c6624ca904d | -5.79446 | -59.22049 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 178cff9a-942e-3240-9002-220b7b03ab4b | -7.93 | -45.91587 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49596c6e-a505-37b2-bfdc-b478a72b04b1 | -9.15605 | -59.4681 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f85fb62b-161b-3469-b233-4339e92481fc | -9.1577 | -59.50549 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a726c61-a555-3e26-96d5-61f360fbab71 | -8.85919 | -52.04676 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 652cbbf9-b34e-38dc-8862-783692a9a77f | -9.15298 | -59.46231 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 957d6046-0a89-3eba-8a3c-5f4b2a89e971 | -5.77368 | -59.88369 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f38792e5-3f23-3f8f-8d08-8d3296e9b136 | -11.13387 | -46.33719 | 2025-08-24 04:59:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 469af3d6-324a-38ee-8a6f-c4bfda1a2a1d | -9.1688 | -59.47856 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| df387b5e-b5e3-38a8-a5fc-ad09e059eb53 | -7.92407 | -45.92106 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e22d487b-1d99-3f79-af3e-49b5bda68a2c | -9.02616 | -59.01518 | 2025-08-24 04:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fb98c822-39ba-32c8-ba33-e7ba31e7bc74 | -8.93382 | -62.43818 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1172d77-987e-3183-88cd-48eba3067f4b | -8.11578 | -47.13978 | 2025-08-24 04:59:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71e5ba4f-5d63-33f3-bdd3-bc6de40a903f | -9.15872 | -59.45282 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 62f414bf-d9bf-3631-9b9d-a04dda6d7c13 | -8.84238 | -49.90062 | 2025-08-24 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 994bda3b-c23d-32d8-afed-a646b3129731 | -9.16794 | -59.4702 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e51276d6-4a61-3b8d-84bc-737ceb262381 | -8.18205 | -45.08069 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e59d1d5-89c3-352a-b47f-d5ce10d1b262 | -8.75048 | -46.71386 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9044240-62d4-3b08-a6c5-607fdd5e8ad7 | -9.25363 | -60.92762 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e99e3ecb-b5e7-3d18-b981-b0b2a100a4f5 | -9.17427 | -58.30778 | 2025-08-24 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb692e91-ae8c-32fe-9263-d9298941ecde | -9.81977 | -46.44595 | 2025-08-24 04:59:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c92f609-65d7-33f7-b7ec-56cf0c8a4e71 | -8.18059 | -45.09143 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da78d066-9689-3809-9fc7-7817950b4265 | -8.14249 | -62.87113 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d45adab-71aa-3180-b199-107115e24445 | -9.13542 | -60.77609 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| feb65692-53f3-3bae-bfe1-a143c5fc4c1a | -9.2429 | -60.47419 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README59.md)
