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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbae5d54-626c-326b-a9d2-4a0aae03d2d2 | -9.1896 | -45.776402 | 2026-09-19 00:19:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa432b81-607a-342e-8551-a1f5637dd79c | -12.6057 | -50.918201 | 2026-09-19 00:19:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a57b688-4adf-3342-90b2-4f0b086cdd40 | -12.9845 | -44.821999 | 2026-09-19 00:19:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d7e80442-b45e-3370-b124-bc838c2e3385 | -11.1239 | -45.2831 | 2026-09-19 00:19:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7955cdd5-c433-37f8-86ea-76efc47bed9b | -14.6736 | -46.668301 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8d46de93-190b-3a6a-a9f8-050724a16618 | -1.6019 | -54.436001 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bfa3130-016e-37d7-87b1-40102d420f22 | -9.773 | -45.036499 | 2026-09-19 00:19:00 | METOP-B | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0feb8944-d4d6-3753-8e48-1f397582600b | -9.9215 | -46.586899 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c8bae37-2bcf-325e-ad6b-6537f2c08398 | -21.034599 | -48.237801 | 2026-09-19 00:19:00 | METOP-B | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 03d33ddb-7b83-3e26-9d07-17124c8efb4d | -11.0855 | -48.276299 | 2026-09-19 00:19:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37b89b74-83a4-351c-831d-580cdde62de5 | -11.3387 | -44.145401 | 2026-09-19 00:19:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 200cd621-b641-3133-b8d2-e1e53867bade | -12.6424 | -49.477798 | 2026-09-19 00:19:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 998718a7-ccb6-324b-961e-82c9dcaf322d | -10.8271 | -50.156799 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27753f2e-c97e-309a-b0c1-6d465d767ad0 | -10.9245 | -53.9534 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1e39542-bf24-3a68-bdc1-fae38975352d | -8.7609 | -48.665001 | 2026-09-19 00:19:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5c05a8fd-510e-3819-b73c-15cc92ad608c | -6.3767 | -58.295101 | 2026-09-19 00:19:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ea804c0-c4c2-30c9-947f-e68893e80091 | -3.3675 | -50.451302 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66973840-6a78-37d4-8bd0-a4752e35fde9 | -9.8426 | -49.2356 | 2026-09-19 00:19:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2f597d2-be73-3dcb-af5e-25efa5105dbf | -11.0561 | -49.758202 | 2026-09-19 00:19:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd796608-5d21-3206-ace6-4456addf4a0f | -15.6757 | -52.720901 | 2026-09-19 00:19:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f11f22e5-fd5a-31a8-aa6c-aa660e0a17d6 | -4.5088 | -54.958099 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46f62237-895d-3e91-aa77-73fffcd6c406 | -10.3675 | -50.448101 | 2026-09-19 00:19:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c057d6e8-97af-3a95-ba16-d028307f21f8 | -12.6975 | -45.931499 | 2026-09-19 00:19:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cedb2b6b-849b-3d4f-b381-6fb5dbd581f8 | -9.2392 | -46.1954 | 2026-09-19 00:19:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7b748c1-61f4-3a54-9d59-f3eadab3506f | -3.2106 | -53.940701 | 2026-09-19 00:19:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c1759a1-55b5-3d79-8825-09203ab718ac | -7.5818 | -57.673302 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae8f72bc-b120-3398-848b-f346eeed38bf | -10.8189 | -50.1661 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4375c9a0-2785-3032-b355-0215421314bd | -17.320999 | -46.625401 | 2026-09-19 00:19:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 63e16cfd-b7ec-3619-9376-fd8241834e33 | -11.1024 | -49.464802 | 2026-09-19 00:19:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 473dd216-fcff-379f-9a27-ef2b8851f0e0 | -11.9412 | -50.114101 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80c3a62f-8e86-3eb6-b020-910682b8d60d | -8.3684 | -47.214901 | 2026-09-19 00:19:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44077be2-8863-3bc9-9428-04d3799435c0 | -13.388 | -49.446098 | 2026-09-19 00:19:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ea8b5107-2521-3a7e-911f-1f9374c44c8e | -2.3875 | -48.515701 | 2026-09-19 00:19:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcf006f9-ca29-3230-801a-90cd73d2b113 | -9.7373 | -45.058998 | 2026-09-19 00:19:00 | METOP-B | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 525ba911-1886-3f81-a565-bd00759bc566 | -6.9267 | -55.016602 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a7468dd-fa2f-3c54-baa5-e770ae31dae1 | -5.8839 | -49.782299 | 2026-09-19 00:19:00 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb12ac21-e54a-364f-bb13-93ee351b28a3 | -13.6142 | -46.951401 | 2026-09-19 00:19:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e06a307f-2e2f-3430-91aa-aae99039bee0 | -14.1295 | -45.187302 | 2026-09-19 00:19:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7d99b4c-6fd7-368c-aee7-37222710d2a4 | -5.838 | -52.021301 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c116139f-31d9-3ee1-9193-53057a417ce2 | -19.1903 | -46.659599 | 2026-09-19 00:19:00 | METOP-B | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 06aa32c4-7eb2-3ad1-8c68-24553cb7b3d3 | -9.9343 | -53.9767 | 2026-09-19 00:19:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0423bb46-e5f7-3644-9e6a-c5538ac14586 | -10.8718 | -56.1768 | 2026-09-19 00:19:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b62b50d-c334-346a-a66e-df9405a77d2d | -11.2523 | -54.095901 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43a3687f-bdc9-392b-91f9-d39719029db6 | -4.7955 | -56.2052 | 2026-09-19 00:19:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14296982-3637-3986-b033-84efd01843c3 | -10.8598 | -56.168201 | 2026-09-19 00:19:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e04bb5d-8906-3b6d-a4a2-a31c766dbc28 | -12.115 | -46.991798 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a690b277-2e41-381f-8ede-14e3e37ca955 | -6.5812 | -44.157799 | 2026-09-19 00:19:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9b02dec-bf4a-3fcd-bb58-fddb87451973 | -5.892 | -49.7724 | 2026-09-19 00:19:00 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4c97eef-cb49-373b-9140-a024a82c2933 | -11.8643 | -47.591 | 2026-09-19 00:19:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ff83b30-380b-376e-8596-58c4b2d35042 | -8.3609 | -47.226898 | 2026-09-19 00:19:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f769b85a-2974-38c4-93b3-65dd0c75c081 | -13.873 | -48.5891 | 2026-09-19 00:19:00 | METOP-B | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 03ed15e8-4123-38de-988c-8f73ce9cfd3b | -13.6235 | -48.313 | 2026-09-19 00:19:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f1ba539b-b0bb-3eca-a54f-6324947c1847 | -12.4368 | -49.571602 | 2026-09-19 00:19:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5160e157-4241-3df7-9e12-97e7e82ea132 | -8.3632 | -47.236698 | 2026-09-19 00:19:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 181f4669-6515-3602-b164-220c2d665f62 | -11.1431 | -54.016399 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6aad93ae-e433-35f3-aeab-3bfd241c7ce3 | -8.4725 | -47.001598 | 2026-09-19 00:19:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ddf07fe-eb2c-3020-b98e-f8911deb2556 | -11.3129 | -51.726601 | 2026-09-19 00:19:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ddc4c59b-6a52-3328-bf91-1806974cf33a | -11.0817 | -48.260201 | 2026-09-19 00:19:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 534c5912-96ee-37a5-9806-bbb6acd7334a | -11.9767 | -52.455502 | 2026-09-19 00:19:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2fbcfdae-2169-30c4-921f-91b6e6110906 | -1.3167 | -55.820801 | 2026-09-19 00:19:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb2ff9a7-ec38-365b-ae37-63b8b7d308e3 | -10.4662 | -51.252499 | 2026-09-19 00:19:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68ce471c-e408-3544-9b4c-08e230b9e393 | -11.3099 | -47.255402 | 2026-09-19 00:19:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 971e34d5-0afc-366e-80f7-80fc890be687 | -11.4084 | -47.278702 | 2026-09-19 00:19:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a14f4fda-bc8e-3749-8434-ff2140be4921 | -10.9084 | -53.973801 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b1517ac-2af1-3009-b367-48dfe0e81f0a | -15.6348 | -52.721401 | 2026-09-19 00:19:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 718f131c-fce0-3bda-899f-1be527aa9a35 | -3.7286 | -54.643101 | 2026-09-19 00:19:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f2c7e45-23dd-3f2f-8c3a-93ddd9a75a63 | -2.0266 | -48.780899 | 2026-09-19 00:19:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 110f3e57-cc1a-3b92-8ce6-662864e6ae3c | -8.7744 | -48.679001 | 2026-09-19 00:19:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 754d9947-04fd-3054-876e-60fed10827c1 | -11.02 | -54.111801 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0215ab46-3c3b-3b67-ba80-cf350299ff6a | -5.6524 | -51.702 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 476dd53b-f362-339a-8635-5d776188498a | -16.069 | -52.250301 | 2026-09-19 00:19:00 | METOP-B | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 156c124a-c972-3253-b6ba-f74a1919b0ea | -9.0398 | -48.7103 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 368344f0-ff4f-322e-9822-b6579fea5c56 | -10.5185 | -44.8358 | 2026-09-19 00:19:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dd5a2c12-4b0f-35fd-aa57-b0b4f1cd538b | -5.2585 | -50.967201 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44778974-3e6d-3f27-80da-4f80b93b612a | -4.3539 | -55.417 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b1a41f2-c84e-3578-bd7d-dde7ac2db4f3 | -12.7412 | -47.018002 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04e18474-4140-3496-9d6e-b877c8ba2908 | -8.758 | -46.9011 | 2026-09-19 00:19:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 100e27b7-1720-37b5-83da-fac06642cc46 | -10.8722 | -54.0923 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3d397ce-149d-3053-a4e0-a1fe3c1962e2 | -12.6903 | -45.944199 | 2026-09-19 00:19:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 868819db-3cda-3c49-980e-0cffba39fb2f | -18.8309 | -47.928398 | 2026-09-19 00:19:00 | METOP-B | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4cdb449-16c0-3315-a946-165a63a1550d | -11.4366 | -51.448601 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 830220fe-b1cc-37e9-a2da-74962cc2c02e | -8.4237 | -54.726002 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4ca9492-2f46-3da4-8cbf-afd208c58c0f | -9.7404 | -45.071701 | 2026-09-19 00:19:00 | METOP-B | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f9d96f71-9db8-3ee7-85e6-5897a6ceed31 | -10.875 | -54.057499 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d78c1083-2735-3f60-a9f3-34bed8c43daa | -5.8939 | -53.554298 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19b575e9-d3ce-3253-ac03-b25244315000 | -6.9475 | -46.963699 | 2026-09-19 00:19:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b27e9258-3e47-36ae-8ac2-f5a6660b623e | -4.4278 | -55.518398 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34eb547e-3e98-3898-b98a-f80cd10a1bbf | -3.3595 | -50.461102 | 2026-09-19 00:19:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 204c1fcc-c9d4-31fb-8e31-c8d3f5d74d49 | -1.6816 | -54.9263 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c06cdff5-e5ae-3027-9b3d-f26732b808db | -11.9102 | -50.113899 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f34bd85-f9b0-3b9c-a753-993d996b8cff | -9.3874 | -45.358799 | 2026-09-19 00:19:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| afe613df-6e07-3fd5-a5ce-5894e58478ab | -6.1414 | -51.722301 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac0ecc55-d1ee-30c3-ab02-e9a9f3930522 | -1.1166 | -57.2616 | 2026-09-19 00:19:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2fc5fee-a493-35f3-8c8e-41521d8a57e8 | -3.3799 | -53.000198 | 2026-09-19 00:19:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33934f14-6b72-31c5-8c6a-6e268b60c321 | -11.3581 | -44.1404 | 2026-09-19 00:19:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85c69ef6-3ec4-364e-bcf1-a5cbc1b77673 | -5.8669 | -52.057999 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0d2a894-2521-32f0-9068-84c80a82965f | -10.8041 | -50.8764 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5266cea5-952c-3431-b805-3c25b0b376f8 | -10.8709 | -53.990398 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1158775c-24aa-3e47-a0b1-b5a2a98269f9 | -11.9369 | -55.898399 | 2026-09-19 00:19:00 | METOP-B | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 795b2e71-bae4-36e8-bf44-69c10c2b6458 | -4.499 | -54.9603 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
