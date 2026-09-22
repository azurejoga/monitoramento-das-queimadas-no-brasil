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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c3a4264-d2e3-3255-ac15-0339b1ad59f9 | -10.24989 | -68.77637 | 2026-09-22 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04967798-cda3-32e6-b395-5ede8d868e94 | -9.18259 | -65.85789 | 2026-09-22 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e056673-c011-3684-8eb3-a5706918542f | -18.5022 | -50.3225 | 2026-09-22 06:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| ce399edf-43fa-3d29-b29d-efe0315981fa | -18.5223 | -50.3188 | 2026-09-22 06:30:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 138.3 |
| 0402e2aa-b84b-3bfb-9e4b-13960aa19702 | -18.0502 | -50.935 | 2026-09-22 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 100.5 |
| f80e4746-edd6-3848-9511-0bdff2de3e1b | -18.5022 | -50.3225 | 2026-09-22 06:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| 9ea1182b-ef83-364a-bbca-73eb2d9192c7 | -12.8715 | -50.9291 | 2026-09-22 06:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| f452d5ed-7f78-3176-9f62-e0893e932a5f | -18.5228 | -50.2965 | 2026-09-22 06:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 93.9 |
| 737a604e-bdc6-3f4f-b47b-990d40ad8810 | -18.5223 | -50.3188 | 2026-09-22 06:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 187.1 |
| 369c9c87-7b6b-3efd-99de-003beb19124b | -18.0507 | -50.9129 | 2026-09-22 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 2eb71e2a-820d-3bbc-9e83-2a28eccaf2dd | -12.8906 | -50.9267 | 2026-09-22 06:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 186a1473-9d87-3da8-b105-4ba822abec44 | -10.6094 | -53.9902 | 2026-09-22 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 64c89852-2f6f-3bd5-8553-ab96a700f3e1 | -18.0303 | -50.9385 | 2026-09-22 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 7b74a7de-984f-3656-8545-802a4249554c | -18.0507 | -50.9129 | 2026-09-22 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 271fd31d-fced-3144-aa9b-c755688f5fd3 | -12.8906 | -50.9267 | 2026-09-22 06:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| aba666e2-02f9-3909-a68d-5eb9154bf9b3 | -18.0502 | -50.935 | 2026-09-22 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 181.9 |
| ccdae1da-1aa3-3052-88b8-e88d81dd5369 | -12.8715 | -50.9291 | 2026-09-22 06:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 9cc2a79b-d36e-3586-ab4a-7afb5bdb3cbe | -18.0308 | -50.9164 | 2026-09-22 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a365e50d-fe9d-37cb-86f3-c83729620a99 | -18.0303 | -50.9385 | 2026-09-22 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 37cef65a-1a6f-3901-af86-bb41dffa631d | -12.3018 | -50.7203 | 2026-09-22 07:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ed5015d2-f1a8-3961-b702-86bdf3941cd2 | -6.6332 | -59.9073 | 2026-09-22 07:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a5c65483-855e-3dfe-b4f8-ecde231e2ae2 | -18.0502 | -50.935 | 2026-09-22 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 009a9906-230e-3c9a-8385-e5cbdb05832a | -11.6888 | -50.9833 | 2026-09-22 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| f4c39bbb-ddf9-3151-be00-93e9aaa1f78f | -6.6148 | -59.908 | 2026-09-22 07:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 2c4c5bd5-b7bf-3a77-96dc-6b8313f64fad | -18.0507 | -50.9129 | 2026-09-22 07:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 114.8 |
| d4c71925-6bcd-32fb-ae8b-cfbf2e50c4ea | -12.3021 | -50.6988 | 2026-09-22 07:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 547e3de3-83db-34d0-af85-f5c3884f5b27 | -12.3212 | -50.6965 | 2026-09-22 07:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| c0597ce9-a39c-3c5e-be21-a8ab959c4ba0 | -6.6331 | -59.9265 | 2026-09-22 07:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 4a4442bb-068d-397d-9129-695d2796eb5d | -12.8906 | -50.9267 | 2026-09-22 07:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 16ea8535-0f96-3ce1-8853-5dad55ef0a4f | -11.6891 | -50.9619 | 2026-09-22 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 0e795ef3-ab1e-3ba0-bd21-66760a784cad | -6.6146 | -59.9272 | 2026-09-22 07:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| def313ce-6f16-3c8f-ac8a-03e99f603159 | -10.6094 | -53.9902 | 2026-09-22 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 97521a0f-5f43-3d73-a9db-b639a47fd90e | -12.8715 | -50.9291 | 2026-09-22 07:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 754168ae-f6e0-3fee-b8cb-f36fbe42fbfc | -6.6515 | -59.9258 | 2026-09-22 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 56f0f894-7614-31ac-8b0c-ac0b4c375488 | -7.90382 | -72.94538 | 2026-09-22 07:03:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a72ad6c-f72c-33ee-b510-dfc17cb21af8 | -7.90331 | -72.94929 | 2026-09-22 07:03:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91dcee4b-52e9-3741-88cf-4d44a47d5dc8 | -8.67568 | -70.03059 | 2026-09-22 07:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e88039df-2e74-3d93-8dac-aea11009e652 | -8.6765 | -70.02415 | 2026-09-22 07:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4c6a8c3-d187-3ab0-9e2d-54af36e8fde5 | -7.9029 | -72.94685 | 2026-09-22 07:03:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b4155d4-e08c-3829-a57d-2b42cdcf54a2 | -10.6094 | -53.9902 | 2026-09-22 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 46109686-6714-32c7-a474-e2689d3377cc | -7.5889 | -57.6757 | 2026-09-22 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 13180eb8-705e-3f16-b331-bb48d61a5bac | -6.6146 | -59.9272 | 2026-09-22 07:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 580a3db9-bef3-3415-b29a-91bd6484532f | -11.6891 | -50.9619 | 2026-09-22 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| db402ec9-81b6-3543-a77e-4effc68a677a | -12.3021 | -50.6988 | 2026-09-22 07:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 1316500c-08d6-3d83-b770-eacaa204586c | -6.6331 | -59.9265 | 2026-09-22 07:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 134.6 |
| ae1553ec-919b-3930-ab0f-9947bbaf5140 | -11.6888 | -50.9833 | 2026-09-22 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 612dc6e8-14d4-39de-820f-87c36287ec1e | -12.8906 | -50.9267 | 2026-09-22 07:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 4313e97c-dbf6-3b16-9c4e-2866455e2e38 | -8.6135 | -62.5171 | 2026-09-22 07:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 36ea6054-fa2c-3b99-ab29-c547df92e5e7 | -12.8715 | -50.9291 | 2026-09-22 07:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 157.4 |
| ed0b4783-cf0b-3e66-a380-c8958e8e3006 | -6.6515 | -59.9258 | 2026-09-22 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ad2a6f98-7256-3690-b4e3-c20f8cee8e6b | -6.6332 | -59.9073 | 2026-09-22 07:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 62c4bd68-9e03-3822-9ede-8b0b6c96bbd6 | -12.8718 | -50.9076 | 2026-09-22 07:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8a954826-4794-3e14-83a1-065c8f536a70 | -12.8715 | -50.9291 | 2026-09-22 07:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d8923484-d733-32e0-a725-658ee7af0e84 | -6.6331 | -59.9265 | 2026-09-22 07:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 08be9c48-b324-349f-99d8-7d5d0c3ae843 | -6.6332 | -59.9073 | 2026-09-22 07:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a5d8aae1-0e59-3ec5-a88e-59fba5151fe9 | -12.8906 | -50.9267 | 2026-09-22 07:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| a372c1f3-44a0-3414-88e1-45023739cfcc | -10.6094 | -53.9902 | 2026-09-22 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 202b402c-69de-3dc0-b75b-29fb21a22535 | -6.6146 | -59.9272 | 2026-09-22 07:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 99e0d9ec-3e03-38dc-8e82-d43c54d98e51 | -8.6135 | -62.5171 | 2026-09-22 07:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 5b6223f0-5961-35fb-994a-8bf5427162d1 | -11.6888 | -50.9833 | 2026-09-22 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 55ab4bae-7176-35ed-a398-5d77a3a9c6eb | -6.6515 | -59.9258 | 2026-09-22 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c7352393-2edf-3619-a8f5-c5d771946ebf | -11.6891 | -50.9619 | 2026-09-22 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 1ba40b2d-1344-38a8-8a9f-3b10b94a2cb8 | -6.6331 | -59.9265 | 2026-09-22 07:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 12e354b6-f623-343d-9ed6-df090ed24ddd | -7.5889 | -57.6757 | 2026-09-22 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| b79089c4-8651-37ac-a348-f4bf3df769d9 | -6.6332 | -59.9073 | 2026-09-22 07:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| ecb00e38-4c0c-341e-942f-20008ac345ed | -11.7082 | -50.9598 | 2026-09-22 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| d9e9d73c-7a0f-3249-951c-05827f98282b | -12.3021 | -50.6988 | 2026-09-22 07:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 80293364-45e7-3069-9310-a74d35a475ad | -11.6888 | -50.9833 | 2026-09-22 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 014ca0c6-78fa-3b8e-9fc3-9eafc3332fb0 | -8.6136 | -62.4981 | 2026-09-22 07:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 11b85de3-e398-3047-b9ed-f47934a243dc | -12.8906 | -50.9267 | 2026-09-22 07:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| f4b5fb94-171e-3adc-a190-9a230f0f4616 | -6.6146 | -59.9272 | 2026-09-22 07:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| d5507e79-5863-3ef7-b45b-ea195a39db73 | -12.8715 | -50.9291 | 2026-09-22 07:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 0fb41a0a-239d-36c0-8c1e-07c9e19a228d | -8.6135 | -62.5171 | 2026-09-22 07:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 4044c153-d4ed-3ca2-b0aa-16662afa2c08 | -10.6094 | -53.9902 | 2026-09-22 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 406cda8c-6887-31b7-9d0e-ac18a0d1f4ac | -6.6515 | -59.9258 | 2026-09-22 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e4c19353-4e92-356d-ab57-f8f21994b114 | -6.6148 | -59.908 | 2026-09-22 07:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1bfc93dd-4ca0-3e4a-bc74-ada7b3d9fe70 | -12.3025 | -50.6774 | 2026-09-22 07:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 6072d1f3-e252-376a-bd8b-69c1b567c0e0 | -11.6891 | -50.9619 | 2026-09-22 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 8ba0d5e3-9dc2-3ff2-9c5a-0dbd652b552f | 1.53107 | -55.9211 | 2026-09-22 07:37:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c1949c5c-9870-3d00-8f4a-fe2c7423f021 | 1.54883 | -55.90727 | 2026-09-22 07:37:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| bab94407-c145-3db2-9316-a436c469463f | 1.55354 | -55.87306 | 2026-09-22 07:37:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 58cc201d-296f-3584-a7a3-74f9a70bc3ae | 2.09991 | -60.20362 | 2026-09-22 07:37:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 463e6557-5a4a-36be-aeaf-a64d1c9075e1 | 1.55186 | -55.86212 | 2026-09-22 07:37:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6e6bdefb-8839-34f8-b444-7b0a5de59b07 | 1.5391 | -55.90872 | 2026-09-22 07:37:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 972dbb25-c969-3e5e-b4ba-feba7f74908b | 1.07973 | -60.67592 | 2026-09-22 07:37:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ad94be69-db85-331e-9bc3-b556a90465e1 | 2.10128 | -60.21281 | 2026-09-22 07:37:00 | AQUA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 71da6625-07f8-3748-9865-4e1fc72c1007 | 1.55521 | -55.884 | 2026-09-22 07:37:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 1e3451ea-4890-3f44-bc79-47311689c1f6 | 1.54079 | -55.91964 | 2026-09-22 07:37:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c70f1041-a363-3513-88e5-523e14fd48a9 | -2.56306 | -57.50072 | 2026-09-22 07:39:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 79f9f791-3a0a-3ce0-9a59-8ec27167b4eb | -3.29367 | -57.85472 | 2026-09-22 07:39:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 308f4b3c-e215-3a6a-91fe-74ed627ec58b | -3.28442 | -57.85339 | 2026-09-22 07:39:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f478a410-88e7-35c0-b9f5-c0caa85047d7 | -8.60926 | -62.51394 | 2026-09-22 07:39:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.3 |
| a83860d9-93b1-37d7-820e-4fe0cf462796 | -2.85779 | -57.80976 | 2026-09-22 07:39:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b189148d-e9cb-3957-93b7-2a424f6b69a7 | -8.61071 | -62.50461 | 2026-09-22 07:39:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.8 |
| e0e0f5bb-d0ca-3f76-b8ab-5a0a390d3f88 | -8.60172 | -62.5032 | 2026-09-22 07:39:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 9eefa032-3396-34a4-ba40-a47ba4d63e5f | -6.73873 | -59.42189 | 2026-09-22 07:39:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2ede5643-e652-36bd-9e6e-c54ae5d3e005 | -10.61095 | -53.96285 | 2026-09-22 07:39:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 285c9787-dfb6-3994-a5e6-b30628feed82 | -6.03843 | -57.82475 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 25c0100e-0d6f-3654-93d4-7b8fc3cb8595 | -1.94144 | -56.59103 | 2026-09-22 07:39:00 | AQUA_M-M | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7f85130a-2f28-35bf-b57e-afc74cbf0792 | -3.48159 | -59.57317 | 2026-09-22 07:39:00 | AQUA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README121.md)
