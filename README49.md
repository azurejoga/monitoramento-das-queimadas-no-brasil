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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 920cf9ae-e466-3ab8-9533-2b1dd6c0c5ed | -5.9714 | -57.76898 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69ebf61e-7a64-33fc-ab90-80c1c0225b3b | -9.18383 | -68.21077 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e6a373b-5159-3354-87df-b976e0417e0c | -6.18779 | -57.72416 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77eb0c53-be4f-3925-9dc4-5442b6000d62 | -5.97015 | -57.77716 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1252f255-31e5-3b02-b143-09a76c0040ce | -6.09946 | -55.64369 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c865da86-770d-37c4-bff6-fb44047c4431 | -8.75222 | -70.81945 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b394abd-170b-34f9-b7a0-d8dfa2a64ad5 | -10.55333 | -51.34242 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0d5b2b6-0fc1-32e7-9e3c-c1f837def27c | -6.15975 | -57.71585 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1296ac5a-5d49-35b6-8d5e-51d78ddf05a6 | -8.70849 | -49.62034 | 2026-09-12 05:29:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1880db9-7b80-3346-8c86-7e08764c7311 | -10.23364 | -56.2627 | 2026-09-12 05:29:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4e2b1bb-f86e-3cb4-9369-3ae4f2ccf855 | -6.1181 | -55.65682 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8943203-d282-374a-8fbd-656acc8e5e22 | -9.1814 | -68.22462 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e5976a3-8fec-3cab-91da-024313f3577f | -6.76724 | -59.42549 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c80b6963-d653-3796-afd4-6db510223d3e | -5.97496 | -57.76956 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9a7476d-3c7e-31c9-8ed9-48598c80c91d | -10.97023 | -54.10041 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1b122ca-24d4-34d6-8b42-6d4ca72ecf4b | -9.29903 | -68.30483 | 2026-09-12 05:29:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d347e28f-db85-32ec-b6d4-8e34d60b2636 | -6.20145 | -55.26018 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38157d9c-b18f-3a36-95a1-6607aea0b57e | -6.51073 | -58.28731 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6d56032-40aa-39b8-a134-bb473894ce4a | -6.77342 | -59.43015 | 2026-09-12 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d989f8d-f648-33eb-b52c-9e8040669e16 | -6.10598 | -55.65516 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88449eba-5d57-3e86-acd1-821561c3dc57 | -6.50723 | -58.28677 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18d49531-fd7c-3c4f-b5f4-5ff7d477938d | -6.06637 | -53.49169 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac48cc92-323b-3e78-9bac-4ea7a16c75fe | -9.36914 | -48.41305 | 2026-09-12 05:29:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14d3482b-ed8a-334e-9121-c9b6f0202ad4 | -6.33098 | -55.85533 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92f40dff-4169-35d9-9cbd-3775922c0be1 | -6.88793 | -55.65131 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c2ac2e8-ded1-3968-ada1-15d1beb37dd5 | -11.23398 | -54.13488 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18b91fd9-4dde-37f2-85fd-189592725f3a | -6.88741 | -55.65492 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 413a1c5a-985d-31de-8356-1893b78facab | -5.97977 | -57.76193 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea2e1a57-8ed7-3d60-805a-7bd1bd2f3e7c | -10.89858 | -47.83286 | 2026-09-12 05:29:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d05e9ca-9e63-3a0a-ae92-fd06c00de4f2 | -6.2415 | -51.70091 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71883e19-462f-33e4-8429-cbf7ee5d9baa | -8.65949 | -69.97453 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7000647-f566-3c18-97f5-8706a5326af2 | -8.53597 | -54.69896 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c232582-f2f2-375f-a822-39b26f5daa23 | -9.17687 | -68.22385 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 630147b8-e4f3-3782-90b3-90d12b4d65ec | -6.23043 | -51.7028 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f633ca86-d408-36b8-8cb6-5a87df9c7559 | -9.46595 | -50.32048 | 2026-09-12 05:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c5bd0af-e4e2-331a-8f66-d380ac3ad9de | -7.35763 | -72.67314 | 2026-09-12 05:29:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 718c87ad-b70c-3ce9-ad4d-6382dad3a18c | -9.18076 | -59.68919 | 2026-09-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c46d6f57-a16d-3f86-993a-295f16cce9ff | -6.23229 | -51.6897 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b9a56f4-3631-3efc-95df-0225156b007a | -6.76554 | -58.62061 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8466cf97-03d3-38ec-8add-570a69f2e6d9 | -8.11714 | -54.79912 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f9a95cb-ed05-3976-8fa1-1379283bd53a | -6.08761 | -57.90873 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 654e5b64-5bfb-30ec-bd55-79bb8efddcd8 | -6.84881 | -55.80415 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d03925c7-df6d-3367-aa36-12da3cdbb7bb | -6.18172 | -57.74004 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd3161e3-f9fa-3532-9d4a-7ecd4070cbf5 | -6.61108 | -58.84784 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09b71086-e633-320c-938a-a5a144979292 | -8.83812 | -69.11189 | 2026-09-12 05:29:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f6eb2e4-4a87-30b3-812f-cff6eb923d83 | -6.28619 | -56.02395 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa04a329-6ec0-3d45-a5b3-915ebb525ac4 | -8.8506 | -71.08356 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca7354fd-3928-3c61-bf64-08d937f55f86 | -9.17769 | -68.21921 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ab4be00c-e6f6-3578-b679-01771de62ceb | -10.90281 | -47.83366 | 2026-09-12 05:29:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d0ac31e-3224-33b4-aa66-2a727887d650 | -8.75288 | -70.81593 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eeb4389f-5fca-3a8a-b086-c20e40a6ecc0 | -8.66462 | -69.97551 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb792d50-6f21-30d8-80b4-7ad3ca90da04 | -9.5259 | -67.1707 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 921da709-d756-34e3-be4c-c13588dcf7d7 | -8.50609 | -50.15401 | 2026-09-12 05:29:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e3b6e9f-ce37-3319-834b-bc17cf9b2bfa | -9.16248 | -71.84935 | 2026-09-12 05:29:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49279e74-f466-3785-a233-45972eefac1d | -6.17173 | -57.70924 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24ec9815-095f-3ca0-b32e-9d03e4ea6f57 | -8.9542 | -67.38165 | 2026-09-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af72c607-e026-3cba-b82f-5e6dc2ba984a | -6.19074 | -57.72883 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7405e851-136e-34ac-a095-e4b956c2524f | -6.23806 | -51.68713 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e79750d-502b-33f3-b2b8-1d323c3a1f48 | -6.10795 | -57.63338 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9188c8fb-94a3-3942-9053-623ff839f1e4 | -8.57433 | -54.57436 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ced7e50f-a82b-3ada-891c-d9a3ddc66113 | -8.07359 | -54.85238 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17ad7c34-fb1b-34c7-9dae-a37644e44b24 | -6.31097 | -55.15225 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75fcdf95-c1e1-3e63-9b5b-d1116fab14ca | -8.70203 | -70.68948 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f39f89b-3dfd-3c34-8e0e-e0a26ef519e2 | -6.39395 | -53.18324 | 2026-09-12 05:29:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 517b8bba-f127-33b9-8789-77ab056d3168 | -8.57047 | -54.56907 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64f56f81-faea-3aad-811b-04d63fe74f70 | -10.50346 | -51.31445 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21aebfe8-ef83-34cd-a571-373dc8cfd0e1 | -5.9852 | -53.72876 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67f215c0-37f0-33ef-b720-579ebf9f5246 | -11.23679 | -54.11348 | 2026-09-12 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16f23801-b9b7-3055-a294-4025766ef019 | -6.28221 | -59.92691 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c0a5790-9060-33c9-a6d1-c458ad541d15 | -8.61008 | -70.97104 | 2026-09-12 05:29:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12489500-48d7-355e-b966-d063a956b559 | -6.8453 | -55.80001 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ea04c48-5922-32d9-b95c-07172a85a644 | -6.28554 | -59.92743 | 2026-09-12 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9516c4f8-f29b-3a18-9764-5a6660b6ec29 | -6.28557 | -56.0326 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c54eb2f8-c0f9-353e-a752-57f99f8ccf8c | -6.04324 | -58.05621 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cea16953-44f3-3289-9369-6ac4ecfe773d | -8.53849 | -54.70182 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95b38dd5-18ca-359e-be2d-46417e538a89 | -6.88818 | -55.65263 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 029ffa1e-99a2-342e-ad07-e3e541622aff | -6.63728 | -58.51954 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0491923d-de91-321b-b6ba-59d4d2573db4 | -6.84482 | -55.25046 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbe2eaba-f6e3-3049-ac97-38441ecbe55a | -10.5629 | -51.35921 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| faebf244-a88f-3510-acfc-0b27bb8bbb69 | -6.60481 | -58.84305 | 2026-09-12 05:29:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 163e503e-75ea-3350-aba6-0ec24b51bcdf | -9.46431 | -50.32174 | 2026-09-12 05:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c810823a-38e5-3cab-bd45-956bfbe039c4 | -8.07984 | -54.8402 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4847ab76-a9aa-318c-9524-91fe2d73bc68 | -9.18254 | -59.44999 | 2026-09-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e6f5ed9-bef5-3375-a601-41fc64716ebc | -6.88519 | -55.64482 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f41bd20c-370d-39fd-97c6-520179d7ce0d | -6.17532 | -57.70976 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48509ba5-ff50-33a7-a0fa-413799643bd5 | -6.11862 | -55.65334 | 2026-09-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a7c73b4-a9c6-3859-abbb-cc75d7160965 | -6.84827 | -55.8077 | 2026-09-12 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 292bf7ad-8681-3c36-88bd-b5b11d7b7b92 | -9.98667 | -59.86852 | 2026-09-12 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d42b004-40ee-3434-8d76-60230bd88eac | -9.44293 | -67.02478 | 2026-09-12 05:29:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 910d35e9-bb72-35fc-9186-d5c27c9f6bd4 | -10.50487 | -51.30831 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b920656-b312-3aa6-8799-4ed9aa9bdbbc | -12.13502 | -48.97461 | 2026-09-12 05:29:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 088824d0-799a-3252-9dd1-a4f0aef03a8f | -10.89561 | -47.83313 | 2026-09-12 05:29:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70d1ab3b-9903-3574-aa62-5ad3aa20116a | -9.18539 | -59.45428 | 2026-09-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb4b57a2-f2a1-3c60-9999-649b92d1849a | -10.55816 | -51.35056 | 2026-09-12 05:29:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4c4c04b-a2c1-3a31-bd44-94dad3778a5d | -6.20919 | -55.26516 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9ad2130-6074-30dc-9241-1b48890f4457 | -8.85129 | -71.07986 | 2026-09-12 05:29:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18788d9e-9d07-3e05-a72d-94730cc43182 | -6.36434 | -57.86943 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd61bd40-3ae5-33c0-907d-effaa738e755 | -6.18421 | -57.72362 | 2026-09-12 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 726df79e-27c3-347b-8f4f-65363a1a1c39 | -6.19565 | -55.27103 | 2026-09-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31904145-3308-3742-9d5b-c30df8a2b5e8 | -10.51207 | -57.45628 | 2026-09-12 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README50.md)
