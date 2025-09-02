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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7517c7e-0fc8-3b6b-9fe4-fe2ce8fabd9e | -4.9124 | -43.187 | 2025-09-02 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 173.7 |
| ff673368-2842-33b5-91c4-35cdc638692e | -10.062 | -48.1197 | 2025-09-02 13:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 4a7870de-37bd-3413-97af-c4bd3d3a7734 | -5.9513 | -44.2707 | 2025-09-02 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 952cdf0d-471e-3d6c-875b-51b35410429c | -5.3974 | -43.3867 | 2025-09-02 13:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 06c8e018-9a2e-3c35-84dd-af37386a13b0 | -11.9876 | -51.3532 | 2025-09-02 13:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| b35d82e0-e5f1-3200-b0bd-31344e8a72fe | -10.0623 | -48.0978 | 2025-09-02 13:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 2339e53b-42a2-3d31-a81f-2f5ef607b06f | -8.8656 | -45.8014 | 2025-09-02 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 7b3a5d1b-f091-3fe1-9c59-3ff0b2cbd359 | -4.8936 | -43.1882 | 2025-09-02 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 58d9788b-2303-3c15-9e72-89083cb7d102 | -11.9224 | -50.6153 | 2025-09-02 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 2976a1e5-754b-3f53-9868-80dc5201af2f | -7.1089 | -44.7703 | 2025-09-02 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e525ed2e-435f-3d07-a37c-bc5e3f386b21 | -11.3907 | -46.8724 | 2025-09-02 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 3e167acc-9f54-3408-947b-cd6fd34c5131 | -6.7909 | -52.8165 | 2025-09-02 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 63d9d117-40c4-3b3a-9287-10cbb9bec439 | -7.9163 | -46.4577 | 2025-09-02 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 188.1 |
| a5df877b-177d-399a-962d-8638edc660d2 | -9.7483 | -48.9814 | 2025-09-02 13:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 977c0731-e90f-3737-a7a6-146ef80e195f | -11.8653 | -50.6219 | 2025-09-02 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| fa508ef5-3f5a-3880-8922-b4338f2af452 | -6.9444 | -44.3494 | 2025-09-02 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 3cc12bd7-cbd7-30fc-8684-0d454da669a7 | -8.8638 | -50.5847 | 2025-09-02 13:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| fcd3bf6f-588f-39f3-8a3c-9c56a3439019 | -8.02 | -44.084 | 2025-09-02 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.3 |
| cae43639-c7e9-3b0b-9b4b-9cb6e7d25f34 | -12.9189 | -57.0074 | 2025-09-02 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 91817072-1b07-3a9b-8c97-80d2ef893a25 | -6.9632 | -44.3477 | 2025-09-02 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 212ca227-08f9-322c-96a1-d3612dbf3da4 | -6.3432 | -42.5602 | 2025-09-02 13:40:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 20710ae0-a85d-37ad-a111-8d69dd7155fd | -11.1249 | -50.6195 | 2025-09-02 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 689b1f7b-7e15-3f08-8a78-9004e082b3d8 | -8.8281 | -45.7828 | 2025-09-02 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| ca7fdbeb-01b8-3a4b-a7e3-8846334e0162 | -16.2953 | -52.9443 | 2025-09-02 13:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 709d8286-83e8-3fc7-97eb-783da2eb03d7 | -6.982 | -44.346 | 2025-09-02 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 4bc3ed20-9b36-3729-a61e-1329a1e1ea07 | -6.9629 | -44.3707 | 2025-09-02 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 8931bcf7-b9ad-3844-a392-2fd51272527a | -11.1033 | -44.6548 | 2025-09-02 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 287.6 |
| ac757413-a564-35fb-83a0-611ce46c7223 | -12.7516 | -44.7067 | 2025-09-02 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 52aabb57-ca9b-3d08-b111-5a38024d83f5 | -6.2038 | -43.3475 | 2025-09-02 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| d8e029ec-216f-34ff-bde3-8ba0901ab090 | -11.3884 | -43.6548 | 2025-09-02 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| b1b3b28e-9f23-39de-8e1a-c550b96c469c | -9.5025 | -57.8032 | 2025-09-02 13:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8c63ac70-2258-3880-801e-daed0a14ca23 | -12.9382 | -56.9856 | 2025-09-02 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| fcdd6154-f550-3a60-8676-40ddc9293c59 | -8.0203 | -44.0608 | 2025-09-02 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 62644a79-1b6c-38c7-85fc-e84cb6f75a96 | -12.5769 | -44.7814 | 2025-09-02 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| f1d6db46-7adc-39b9-9082-796cfae8b930 | -11.6717 | -52.189 | 2025-09-02 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| fa9cdb34-2ad9-3642-94e7-e1f599bef1e4 | -4.9122 | -43.2103 | 2025-09-02 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| e302fb38-a599-3ba5-b044-f3efec2711ce | -10.8487 | -47.4546 | 2025-09-02 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 40c62631-607e-31c9-b9f0-c81ad2380a48 | -11.9415 | -50.6131 | 2025-09-02 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7c2073c3-d24b-371e-96e8-51f748812392 | -8.8467 | -45.8034 | 2025-09-02 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| db1f4583-2bb6-37ed-af77-764b06c6b189 | -8.0011 | -44.0859 | 2025-09-02 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c2518570-b184-3663-97b7-5f28483a0f13 | -8.2008 | -49.5345 | 2025-09-02 13:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| a1ff963d-6577-3e6d-b80a-737686884c87 | -11.0841 | -44.6575 | 2025-09-02 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| cfe925c9-5156-3443-a645-b1e7a78ae334 | -8.6883 | -62.4002 | 2025-09-02 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.5 |
| b15ac23e-7b62-3fa1-bd00-8d05ac66d8cf | -9.1207 | -61.4864 | 2025-09-02 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a8b567ab-9140-30c9-80dc-892e7b3c8c0c | -6.5305 | -44.454 | 2025-09-02 13:40:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 204.0 |
| 895d4fe7-1b12-33ab-a4bb-75c409e27d06 | -8.201 | -49.5131 | 2025-09-02 13:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 7b3a0416-f967-304d-a7f7-2a35631c9774 | -6.8911 | -45.8538 | 2025-09-02 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 680ebadf-c3e9-3bf3-b4be-75b7205f5a45 | -12.9192 | -56.9873 | 2025-09-02 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 7297a890-1961-3628-b606-99f0485cb0bd | -11.653 | -52.17 | 2025-09-02 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 6619c6e8-cd49-3273-95ee-630db3bbcf9e | -6.9942 | -43.2308 | 2025-09-02 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| a3701456-4160-302f-8d7b-3a6eb1616c49 | -16.6368 | -44.5879 | 2025-09-02 13:40:00 | GOES-19 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 103.9 |
| abf78c6d-3252-397d-8785-4649ea6bf6c1 | -6.8095 | -52.8154 | 2025-09-02 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| dc05d5a0-9607-3ef1-9a72-a4ae4ca815f8 | -11.815 | -51.4572 | 2025-09-02 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 4849b36d-40e0-3a96-b609-fa6e6839d765 | -7.9165 | -46.4354 | 2025-09-02 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 76d9e789-4641-3d95-b20f-bac0ac837310 | -5.8694 | -43.0003 | 2025-09-02 13:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 6e984a95-c505-34de-aec9-25be21d05027 | -11.4297 | -46.8223 | 2025-09-02 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 71a92e17-6074-37ab-9e96-923f77e61e0d | -12.938 | -57.0057 | 2025-09-02 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 4b474fe4-ae23-31e2-a320-d6ec04707efd | -7.5477 | -61.3247 | 2025-09-02 13:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 118.5 |
| d3e85469-f46b-3d38-b12f-6c9bf7f934ba | -7.5476 | -61.3437 | 2025-09-02 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 52e51d84-a937-3461-afc3-b4b40dcf00f5 | -11.3907 | -46.8724 | 2025-09-02 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 40dcd95a-a220-3253-ac96-3323f62b444f | -6.2036 | -43.3709 | 2025-09-02 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e78bbf16-cedd-3cda-a254-c5329adfad15 | -11.6647 | -57.3533 | 2025-09-02 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 44ad2d25-c5f5-33c3-8bc2-9341bac74b77 | -6.5305 | -44.454 | 2025-09-02 13:50:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 240.8 |
| 4f456685-d08a-35c2-a65e-14da204bdc04 | -8.1995 | -44.8023 | 2025-09-02 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 134.3 |
| c574de46-459e-38b6-abe4-273ae07d2e5f | -5.7357 | -45.3796 | 2025-09-02 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| adb8cecf-227e-34f4-b387-8456c22a632c | -7.0097 | -43.5331 | 2025-09-02 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 9baed2de-c3e4-37b3-be4a-599b721eda83 | -7.9163 | -46.4577 | 2025-09-02 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| b87325e3-b6da-3541-9cd5-d35a7becf34d | -12.9382 | -56.9856 | 2025-09-02 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 203.5 |
| 68ae299e-9251-3426-89c5-a099b6cb6752 | -11.9978 | -47.1045 | 2025-09-02 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| f3de2116-c00c-3d90-a507-6281fdccef77 | -4.8936 | -43.1882 | 2025-09-02 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 2a219924-f9aa-38e3-b27e-7e022c88f84e | -11.9876 | -51.3532 | 2025-09-02 13:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 5da67fdf-0af3-32ed-853a-0c725fd5ea33 | -10.7688 | -45.2769 | 2025-09-02 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 353.9 |
| 1c3b34b2-3c5a-3809-a824-fdc8fe565c2f | -9.1207 | -61.4864 | 2025-09-02 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 79d21666-b29d-349b-9ef2-0fc49a309c6d | -8.7438 | -62.4169 | 2025-09-02 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 5406b0a2-0a43-36ef-b6da-492d8275d3f5 | -7.1089 | -44.7703 | 2025-09-02 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| f9619e98-adda-332e-a405-69db7e4ac8bb | -11.4491 | -46.7973 | 2025-09-02 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| d4449936-3780-391e-8bb2-a902643e195f | -6.2038 | -43.3475 | 2025-09-02 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 202.6 |
| f2fcc9e9-4533-3812-b5a7-4c89d17107e9 | -12.7516 | -44.7067 | 2025-09-02 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 89f3ba99-6acc-30bf-b3f0-072ce701db5a | -8.6883 | -62.4002 | 2025-09-02 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 0ff50963-4ce1-32aa-afe6-77960cb521f8 | -11.815 | -51.4572 | 2025-09-02 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| bbdf7884-97d2-3dd6-a4db-1a0d95890f7b | -6.7909 | -52.8165 | 2025-09-02 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d3aa5e8e-9299-3f26-a700-8a92ebe704b0 | -9.5025 | -57.8032 | 2025-09-02 13:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 294f4dbf-41fb-37d9-b5d3-e5c4a8e094c0 | -8.201 | -49.5131 | 2025-09-02 13:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| d8437a48-6969-3885-977e-4edda6068c42 | -8.8848 | -45.7767 | 2025-09-02 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 6bec3ffd-c5a1-3fb5-a309-ad7697b36307 | -6.9629 | -44.3707 | 2025-09-02 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 1551ae79-4dbc-34de-9077-766662f0e4c4 | -9.4794 | -46.4994 | 2025-09-02 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 8d88981b-6bf0-32d0-a95d-8fd58234f808 | -10.062 | -48.1197 | 2025-09-02 13:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 2919fce7-639f-36b9-8ebc-e2988726dcc5 | -9.0141 | -45.9886 | 2025-09-02 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d58dc524-1b2f-34a0-a9ac-a2f82f3a663b | -5.717 | -45.3809 | 2025-09-02 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 6f2e8cbc-ce70-3bab-90a8-ae0a2a132803 | -11.6715 | -52.21 | 2025-09-02 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 115ee49d-01c7-349a-845a-2cf4e39eb016 | -8.8281 | -45.7828 | 2025-09-02 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 80db2384-2e41-3016-83aa-cffa4b95a219 | -12.0069 | -51.3298 | 2025-09-02 13:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| b5c5dcd0-8b44-3483-8c0e-fc620f0c069b | -10.0626 | -48.0758 | 2025-09-02 13:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| dded9caf-3707-35f5-a2fc-afa1bcf66adc | -4.9124 | -43.187 | 2025-09-02 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 204.0 |
| 2a379806-d080-3441-94a0-ab83bc348ab0 | -10.0623 | -48.0978 | 2025-09-02 13:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| e3a8c422-6eaa-3270-9cb5-eaef875fc2ec | -6.2676 | -44.4984 | 2025-09-02 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| b03fdb7a-0957-317a-b22e-bd707fa958e8 | -12.938 | -57.0057 | 2025-09-02 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 290.9 |
| 6b2e8021-224a-34c5-a38a-df3f720e8357 | -7.1091 | -44.7474 | 2025-09-02 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3fa1c840-5484-36a4-a0e0-1621c07f2b5c | -5.9513 | -44.2707 | 2025-09-02 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 9d89d156-a0c7-3d82-a5d2-48fccf81b67c | -14.5802 | -54.5315 | 2025-09-02 13:50:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |


[Clique aqui para ver as próximas entradas](README98.md)
