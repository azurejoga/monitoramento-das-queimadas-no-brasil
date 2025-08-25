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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ae5b713-ce86-3d67-9f3c-16dd6a79e8e4 | -9.19825 | -59.43999 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1470f7c6-4b02-3b3f-a3e5-f6c366e54763 | -9.51948 | -60.51812 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6920a11-f337-3834-b32e-fe0e7e2f1e54 | -11.17467 | -55.03094 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b08a4020-d4fa-3659-b1bc-eb1d4206284d | -8.12297 | -62.85626 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4c24a34-2542-3fc8-89a5-d098fb8d098c | -9.20808 | -59.70039 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b43bc451-f72d-3a9d-9ed5-d5a200055d64 | -8.89397 | -62.4459 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99f783cb-4eaa-3550-b56c-af87461e8d45 | -5.4494 | -60.18661 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d66b4882-7b50-3817-8883-a2903efb5b31 | -8.92341 | -60.71919 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4176372-3979-397e-a867-32fff8fc0196 | -9.1959 | -59.49869 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51fdcbe6-774c-3658-92e6-cf5f0b1d1d78 | -10.70658 | -50.55117 | 2025-08-25 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f67a7137-4845-3e57-82f6-bb258007bbbe | -9.06653 | -65.71906 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fb9955f-b921-3547-8eaa-7cff30afc541 | -6.68138 | -58.85617 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b6e5fc7-170a-348c-a1b0-d3a65172bd36 | -9.13872 | -60.76776 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fa9eb6af-7f47-348b-9f1f-d4c73daf1061 | -9.19838 | -60.78832 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c981f329-dc52-36a4-9e1d-6e34127076fe | -9.16803 | -60.82754 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 021a4cd4-9a2f-3d0f-b901-b96ceead35ef | -9.19472 | -59.61774 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0115544-2ea4-3580-b202-5b9cd1e6a2e9 | -9.71195 | -54.98189 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f66489e4-f333-30e2-825c-d0ed00b5573c | -11.60488 | -46.35809 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8c8808f5-c0e2-3237-a3e3-fe3215666d86 | -9.64546 | -59.63287 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0e8ea033-c76b-331d-bee9-5e0f6f6de0f9 | -9.15064 | -59.46148 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b18684d2-e267-3150-b50b-c4367d3238ea | -9.00777 | -65.39219 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f326e4a-89f2-3ec5-883f-93398893d2d1 | -6.68071 | -58.86026 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37cbdb09-6aeb-3fa3-817a-65452f1d5abe | -9.24307 | -59.62459 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b3e58e1-029a-3176-a052-1b749ad69f63 | -6.88738 | -47.92876 | 2025-08-25 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6dd7ded-c640-3269-bae1-15a2f3d74b11 | -9.31348 | -63.43939 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c05341bc-02bd-3f48-a0c6-f41a9145c8b0 | -5.80636 | -59.21442 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbc0b052-8d34-33e0-aa4e-ea4df2e6fde9 | -8.98798 | -65.41176 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5515abca-99a9-306a-ac13-4809a9c24287 | -8.68367 | -62.87213 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49d458e9-abe2-3ad4-8e7f-3bb01096710e | -11.59167 | -46.36881 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 47a533b3-bd69-3d10-a9b0-100c2004c316 | -7.32153 | -44.5344 | 2025-08-25 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea470eac-eac6-3ff9-a522-b6b274e57d48 | -11.6054 | -46.35371 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 27c510aa-1a94-34d2-8330-5c886d8dab08 | -11.47099 | -55.47492 | 2025-08-25 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c836f6b-82e3-359e-aecd-23a1ceb3be89 | -10.89303 | -55.79382 | 2025-08-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5bc99a6-a6ff-3c3e-9b43-a0c440360aa1 | -10.47862 | -57.94263 | 2025-08-25 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96ef7239-f4ae-3407-991a-f8b025b7415d | -8.88756 | -62.45737 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2f8254d-8f21-395c-ae4f-b71b1f72aca0 | -10.88969 | -55.79329 | 2025-08-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebc4746e-7c1c-36c2-b29c-9e237a209fc6 | -6.68225 | -44.4264 | 2025-08-25 05:04:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f28f721a-7875-3c3b-933c-4c088439833d | -8.90677 | -62.42298 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45697973-fd99-3b55-8f0d-b28fe8d17061 | -9.17564 | -59.46568 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5e0af8e8-5664-3263-96ef-07e26b22e7e9 | -5.80078 | -59.22057 | 2025-08-25 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa1ce304-2970-3d99-ab32-b3d276fab518 | -8.10882 | -47.13177 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f3c651a-b2dd-36bb-a0e9-1472d3b923b1 | -11.16167 | -55.09407 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e5615e9-2b06-380e-bd9e-ec28d70c8016 | -9.8188 | -64.26443 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47ae92ad-805f-3b73-a12f-5e280682fc6a | -8.12036 | -62.88653 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb2c1ebb-0a45-3708-a6d4-448622aee70e | -8.10653 | -62.87175 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 874c68b0-c7b4-3a7e-b98f-455162d2fe23 | -8.53923 | -48.864 | 2025-08-25 05:04:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1047f95-7bbe-3e49-ae42-1c1b58e6d168 | -9.15586 | -59.49619 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a14f849-9af7-311a-8d5e-e65e8f3fd5fd | -7.80381 | -61.35562 | 2025-08-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 841decba-b1ff-367f-88a9-f330e0e25fbd | -8.76693 | -49.94978 | 2025-08-25 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db759bbd-4580-3a02-bb19-d7753758e413 | -8.11994 | -62.8741 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 46e8ea05-cee5-36fa-9055-c35b8aeea126 | -9.64612 | -59.64016 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59c63cf9-bee6-305f-9e8c-ac06a9d687b6 | -9.61685 | -55.3535 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63488f62-4b4f-3ddf-a05a-98027c7d47df | -9.15241 | -59.51681 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 822d550e-5f40-3635-92c9-4689c93adc43 | -7.59184 | -45.24171 | 2025-08-25 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1ab907f-bb06-385d-ba14-5718bd55443c | -8.10206 | -62.87098 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95c429bb-5579-3f96-890f-e1ce192f13c0 | -7.35239 | -57.63482 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9faf39e7-2a97-354b-86e5-ce9e926a27a3 | -9.39891 | -60.54232 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94793b1b-1246-3cde-b7d7-b17c8a37ba23 | -8.92178 | -62.43818 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 004f98df-02ae-3b04-abaa-3a5cb9cf569c | -7.28776 | -44.46922 | 2025-08-25 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fe48157-54c1-30e1-95c6-d7e3821dc762 | -9.21562 | -59.62564 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33b68a92-6b0c-3362-84ba-94d302ea2a95 | -8.37069 | -54.98537 | 2025-08-25 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ebf292b-c41a-33e3-906e-45d2c1f6a534 | -11.17238 | -55.02289 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95444ea9-3a6d-3cf9-9aa6-d4913894ba70 | -12.29479 | -49.14641 | 2025-08-25 05:04:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99f1b6b4-2fb9-3661-9058-048826a21433 | -10.25579 | -59.11331 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2387b66-bcc8-3c76-92fd-497812ec74fe | -12.75048 | -44.41877 | 2025-08-25 05:04:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7484bd45-99c8-311c-9035-fdcc95af0601 | -8.60006 | -62.59868 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a4c093a-9ca1-3bfd-a2ba-6e510a53b04d | -12.74397 | -48.10686 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 545a8d36-a9c6-35ee-98f9-6497606fedc1 | -5.5222 | -52.00496 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99a0582f-c834-37b6-a60b-5b1193b383c3 | -8.0603 | -49.68044 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c426e769-88c2-3ed7-9ea3-735b17c81524 | -9.24736 | -59.62104 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c49fe46-dfc9-3806-b6ba-d00fee38c8c2 | -11.16839 | -55.02611 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b67cd872-832e-34bb-9afc-754074773248 | -10.88745 | -55.78559 | 2025-08-25 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d854db34-b192-331a-993d-039e3bae2132 | -9.13982 | -60.73848 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a7dbcae4-c552-3182-8a63-8b89375b4e30 | -8.12574 | -47.127 | 2025-08-25 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8957d172-6f1d-3f46-85c0-fe6e1418c000 | -9.15449 | -59.50442 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73a3bcc1-f94c-354f-b2e3-4758451c26c8 | -4.96115 | -55.8136 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11ffda10-3efb-30e2-8b05-c6d7729441c7 | -9.61013 | -55.35247 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bc618a9-4c67-359f-a303-4bd6b3634a97 | -8.64971 | -63.43738 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bf35f1f-ab6f-3ef5-af52-cda71c391ed3 | -11.19614 | -48.47269 | 2025-08-25 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df44a400-04a5-3415-a169-88f23e4b8478 | -9.00137 | -65.39764 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f0a54582-67df-3f0b-9af0-ec1ad504d08c | -8.46996 | -63.93316 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e773cb7-75af-31c6-b488-dc6dca4939c9 | -8.91538 | -62.44972 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d7138cb-98de-3cb1-9774-29e71f9e6977 | -5.7477 | -57.58405 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a5e7ad4-bb18-3275-8997-8e4ecd1b777e | -9.20747 | -60.80476 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2e83a4c-234d-3df1-8bf9-815337874996 | -8.21577 | -61.38866 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a7d73b14-a1cc-39a1-b0e4-48814b9ff18d | -6.83137 | -58.95381 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8f4f1162-e2b4-3699-b77a-f16722e85885 | -10.61492 | -55.05361 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f454abcf-a920-351a-8ac6-cf208eefe73a | -8.68886 | -62.86855 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 843263d1-6820-3a9c-b296-5a9d6e8bc73c | -9.06432 | -60.63585 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9884fa-f35f-3e18-a3b1-798cdd82e8f9 | -11.17637 | -55.01966 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb12e712-91a6-3e3c-b31e-6133e80c5f72 | -11.19748 | -55.04217 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13dd9446-bab7-3790-a8be-f8cb86fdc36d | -8.60584 | -62.59101 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2673ec41-2b5a-3d51-a2e0-c64b46e34c8a | -11.17979 | -55.0202 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50a6261f-0ba7-300c-9ff1-700810ab1a3f | -9.19522 | -59.5028 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 332e0dbd-15d4-3dbb-8721-9f8109ed1679 | -10.7091 | -47.13541 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e5441bd9-14ea-3bec-a98e-9e91631ebdbc | -8.68732 | -62.87732 | 2025-08-25 05:04:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c2c6311b-89c6-3be9-96ed-78390cb0e041 | -7.57366 | -63.43982 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f2e6c32-4e59-3554-8526-835bc7ff6dd8 | -7.54593 | -63.84267 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e2ed050-13ab-35da-a6a1-7b4e7bc4241d | -8.1073 | -62.86726 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0ba7852-f4bc-31a1-8e4c-09c707a0336b | -10.09998 | -57.76395 | 2025-08-25 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README62.md)
