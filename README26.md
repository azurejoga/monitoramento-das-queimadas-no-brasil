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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7ee080a-ce33-3e3a-a738-d747d1a3167a | -10.46749 | -47.04562 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 3a53c069-1f55-377a-a433-4ec12a8f345e | -9.46437 | -57.83931 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 26fdf8dc-fffa-310b-9d0b-74cd137ba88e | -9.49494 | -56.08758 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fe9f11c-bb09-3754-9f53-93b638b483aa | -10.46173 | -47.04749 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0a1e3b82-f86d-35d7-9d80-873f0f0427e7 | -11.13809 | -46.64061 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a0307e01-98b8-3df0-ae9d-590df44ad9dd | -10.86456 | -53.76543 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7849419b-02f9-3e4d-b223-7db2882a4559 | -12.22636 | -54.29716 | 2025-06-20 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9916b98c-7b60-3ca5-930c-7acd79184142 | -12.58422 | -56.97372 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7a8d439-b1c4-3b32-b87d-efdeb1c963e5 | -11.15159 | -46.62795 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9305b5d-adb0-333a-9619-e70384bb8338 | -11.9518 | -58.74323 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab58f182-a83c-3178-8b48-7964d95a7c7e | -14.43328 | -48.91389 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| be7ba96a-cdf9-35e2-9a7c-ce024a22bec1 | -11.93709 | -48.42496 | 2025-06-20 05:21:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61f5c292-2d0d-33f9-84ce-bd1ea5839699 | -14.43104 | -48.9166 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be798d34-dd69-39d9-9175-3b1a6f02a42e | -14.17198 | -60.05419 | 2025-06-20 05:21:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 938d473f-f943-3762-8739-c5596bacb45d | -12.52103 | -57.20848 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8589fba5-dfa4-3426-9198-927b254ad789 | -10.83414 | -54.01258 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc91c161-2aa6-350b-ac5f-3804227bf3c1 | -10.6552 | -49.36934 | 2025-06-20 05:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70348953-92b3-3bd0-b6dc-7fadc7834809 | -12.0281 | -57.09689 | 2025-06-20 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2dc858b1-830f-354a-8015-f60d3bdbdcf3 | -12.4263 | -54.87446 | 2025-06-20 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72d7f0af-32bb-389d-b3d5-28f3e39ca28b | -10.67978 | -56.55481 | 2025-06-20 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e418778b-b29b-3e5c-babc-ce06eede7306 | -9.31604 | -47.78997 | 2025-06-20 05:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c47eb26d-87f2-3097-b60f-5796e6b10ec5 | -10.85081 | -53.76793 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdca1bcd-650b-37d9-87ce-2c145645dfec | -13.09439 | -52.2985 | 2025-06-20 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8923e853-6e6c-37ea-9b75-94270a33f1bd | -14.43223 | -48.924 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 35d1e15a-f926-3ecd-8b34-1faba787bda7 | -10.86516 | -53.76121 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84d1be72-9578-3068-9c88-90b62231528b | -10.50069 | -47.00829 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ae80db6-4d85-3d1b-ab00-a781a02f10f9 | -10.46103 | -47.05355 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 85fee8af-9a61-3503-8508-ba41e9870b4f | -14.62842 | -48.12231 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83e6f4c9-4596-39cf-bc39-17a47a7791a0 | -10.08472 | -60.49802 | 2025-06-20 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ced8ce1-bb71-3044-b9c8-3ca88d156dcd | -11.14159 | -55.19298 | 2025-06-20 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50957bfb-504b-302f-bf1a-b8fcadb528fe | -9.32889 | -47.8327 | 2025-06-20 05:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7585b0d5-98ac-381d-bd2f-83d4f00defa3 | -10.83623 | -54.0105 | 2025-06-20 05:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4acdee8c-36c8-344b-99c4-27cfe49409a0 | -9.58682 | -65.88223 | 2025-06-20 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3d9252ce-c0ad-3e35-8ad4-85ed826458a0 | -8.72619 | -64.16511 | 2025-06-20 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd6a27ae-bcba-3f9e-b428-074fb4585215 | -10.59401 | -46.93302 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0374335a-7bcc-35de-b334-5c1305ce0640 | -9.92524 | -59.90265 | 2025-06-20 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cefdf3d9-bdf9-3723-a806-ca0f81dffbd7 | -14.82024 | -48.46618 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78c511fe-b171-3cc4-bf19-7f7588d903a2 | -10.46988 | -47.03648 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 598cf504-a665-3d9d-a0a7-c161d224b86b | -11.07831 | -55.05437 | 2025-06-20 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1369daa-36fd-37c6-b12b-c73f72e3f689 | -9.37837 | -63.42729 | 2025-06-20 05:21:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9bb8716-2581-3cdf-993c-0c859016a5f1 | -10.47594 | -47.04348 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 0e201b93-92e7-332a-a10e-cc71d9439d2c | -9.48444 | -56.08149 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1d080141-d40b-385c-abe1-de0f06790917 | -13.36959 | -54.25752 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b47d4392-d4e4-31d3-9039-9b1ed9ffb080 | -13.79786 | -54.29129 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 074f9722-7033-378b-bc4d-35436c934265 | -13.1427 | -56.80643 | 2025-06-20 05:21:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ac04ead-b0de-3934-96ab-1b46b069bfde | -11.80437 | -48.09529 | 2025-06-20 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5a03342-568a-31e1-a2b7-fd98a8637185 | -11.13619 | -46.63892 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2e123152-634e-3d15-bf16-95a6bf8b5a52 | -11.46731 | -47.29671 | 2025-06-20 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b66f74ca-7ad5-3474-8d00-d6fbccabe861 | -10.66813 | -56.55743 | 2025-06-20 05:21:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91179551-6613-3bd1-a174-67e1cef6d108 | -12.8949 | -56.98373 | 2025-06-20 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cfc6f61-fe86-3e67-9d80-d5e711b08ac5 | -11.94897 | -58.73898 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f3312e32-a9d6-3902-b875-6908369dd469 | -13.77805 | -54.20366 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7f5520f7-8317-3b70-99c9-04a3fe0f5a85 | -10.07447 | -52.74575 | 2025-06-20 05:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 42cd7612-95ba-3f6c-b6ef-b1dc2021cf89 | -10.4924 | -47.02027 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 731038f9-31e3-3b5c-bc7e-100830c20668 | -11.1563 | -46.649 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 728a871f-606d-32e0-879b-b44a896a5dd1 | -11.08235 | -55.05495 | 2025-06-20 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fefed1d0-58fb-36f9-a939-c43cee90a7ea | -11.87401 | -54.682 | 2025-06-20 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc02697a-8781-3e97-8590-978dfaa6626b | -11.27245 | -52.46768 | 2025-06-20 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfe9480c-1224-38b4-a19d-dcb12981c9e0 | -12.02871 | -57.09267 | 2025-06-20 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b856baf7-842c-34cc-9c27-c2d010185cfa | -9.49187 | -56.0826 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fee23d7-db64-338f-b21d-dbc48ca7c3ae | -12.65187 | -54.11599 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4344be1a-265a-3647-ade2-fb7a748dc282 | -12.55451 | -57.70748 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57f04adf-b377-379f-83bf-3fe1cf948f5a | -11.91548 | -54.8232 | 2025-06-20 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f51fcbe-1bbb-3422-ab23-3ffb89e28bd3 | -9.45808 | -57.83448 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37a46221-847d-34f5-a324-7a435ffe0d9b | -11.53014 | -56.99482 | 2025-06-20 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12e04b59-7a03-326d-b3f5-908cb89e12f0 | -8.88012 | -49.26382 | 2025-06-20 05:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 71a6e5b5-7c26-3d22-8639-9b02f2fcc87e | -12.6463 | -54.1239 | 2025-06-20 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 433c1300-4b57-3027-a4e0-2ae00f001f94 | -11.12786 | -46.66734 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7effd15-8706-3c43-bca8-1cea52f878f8 | -10.93011 | -49.27702 | 2025-06-20 05:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4599320a-af5f-3c5e-96f0-6eab1dbee38b | -13.09514 | -52.29272 | 2025-06-20 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b82dbc4-ff2f-3ed1-a07e-d83e02016b87 | -11.53137 | -56.98639 | 2025-06-20 05:21:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c0131b7-8202-3c2c-ae8f-adafeda2b031 | -14.82085 | -48.46571 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3666ab90-a4f5-31a4-ba1b-f3e8babe28a1 | -12.34723 | -49.31246 | 2025-06-20 05:21:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 183a3cd2-630f-3d88-a17b-66e8b4884656 | -14.43684 | -48.92222 | 2025-06-20 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbfaf944-1897-326e-af49-6dea4e2d001c | -11.37598 | -55.11446 | 2025-06-20 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2cb867b8-cbde-30f4-8974-1bc8ea1201fb | -9.48201 | -56.07206 | 2025-06-20 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea939244-7d84-352c-a911-5f8b1cec5a47 | -10.53506 | -46.65437 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43f6f840-c000-31e7-be72-db36b331ee3b | -12.02509 | -57.09209 | 2025-06-20 05:21:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c25dffe1-ada7-3363-9584-bf9bae43a5a5 | -10.07976 | -52.74162 | 2025-06-20 05:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3aa23516-9694-30d8-af65-25fcd13d33e6 | -10.94104 | -49.43435 | 2025-06-20 05:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8f581ac-869e-3544-85a4-1ddd57c95c56 | -11.95294 | -58.75853 | 2025-06-20 05:21:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 118e8ae0-d9ed-343d-93d2-723c1863adc8 | -12.42684 | -54.87062 | 2025-06-20 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e66b0a28-bc2b-3378-ba4a-b2ce871bdf39 | -11.62226 | -58.29587 | 2025-06-20 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42a6389e-3c31-3651-86bd-ca35593906b7 | -10.08376 | -52.74711 | 2025-06-20 05:21:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6e1c8ab-d67a-3462-99c0-d8a8d72c85ca | -10.46824 | -47.03953 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| fc8f7c57-8586-39dd-aae3-2f9c8c33ad8f | -11.47278 | -47.29633 | 2025-06-20 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6618a50-2ec0-3042-bf70-9851e9809692 | -10.37127 | -57.50839 | 2025-06-20 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f19653c4-180b-36bd-8454-0db3a8b07650 | -9.95335 | -64.98961 | 2025-06-20 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 915c0c29-cb46-374a-83be-2b64ff44d76d | -9.30157 | -47.79337 | 2025-06-20 05:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36f1b212-591f-3853-b38b-ffb6caa23b8d | -11.46603 | -47.29552 | 2025-06-20 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c866572-1b87-31ce-8cf5-2cbdee3e5ffd | -9.33075 | -47.82846 | 2025-06-20 05:21:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f67f3640-aa98-3803-835b-ac6f93d0a672 | -9.45637 | -57.84569 | 2025-06-20 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf98938b-84c8-3503-8420-2ae7ad014e52 | -11.1201 | -46.67319 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 481ea743-bccf-37a9-ae7f-880157bbae0d | -10.45181 | -47.06149 | 2025-06-20 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c19f642e-f24f-3721-95e2-0a7c6ee53235 | -9.37763 | -63.43177 | 2025-06-20 05:21:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cca8677b-309a-30e5-94fa-e78529393e57 | -10.92417 | -49.27631 | 2025-06-20 05:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4abc370-6bfb-3f1d-9e5b-203a0d0224d7 | -12.19942 | -49.62168 | 2025-06-20 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5afbe230-36d8-30f5-a21a-e52c21c6560b | -9.95679 | -64.99397 | 2025-06-20 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4631b85-7c73-3794-9f0a-947e502de814 | -13.2359 | -49.83677 | 2025-06-20 05:21:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1cf7e623-8765-3872-b0c2-64d3afdf23a2 | -11.47406 | -47.29753 | 2025-06-20 05:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README27.md)
