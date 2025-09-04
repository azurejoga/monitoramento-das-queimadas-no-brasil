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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed60a6b8-cb09-33fb-8a16-8ba587665c6a | -8.08091 | -47.59357 | 2025-09-04 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3ddcd27-d92e-34ad-921f-4e0d0cce6560 | -7.77652 | -50.96591 | 2025-09-04 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1649504-aade-3f65-a1e4-560b28b52e04 | -11.62577 | -46.65054 | 2025-09-04 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1e27de3-e08a-3377-bcf2-11c0ccccf995 | -12.49034 | -48.0676 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30c9bab8-8262-37e6-b260-1538d3131191 | -11.09106 | -52.02459 | 2025-09-04 04:27:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7292ffe5-cd43-3aea-9c23-8828a04cf5ed | -14.63788 | -48.94662 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74656d77-337c-3a51-a1c5-e1dc2ba81495 | -8.36083 | -52.54127 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ade3514e-2cfb-3c32-a791-32e2d33410f5 | -11.58166 | -52.15285 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b89262c-775f-3e2f-8d57-fcf98fde6909 | -7.38317 | -56.68887 | 2025-09-04 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 72377931-fc32-3b2f-86ed-5121033691f8 | -9.45801 | -46.79718 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cd379a5-6414-3e81-86e1-e2625f256b71 | -12.49695 | -48.06866 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a16098b-4946-3cba-b4b2-13320fcc074d | -9.61416 | -47.03627 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fec17a9f-46dc-35fe-8afb-01e1b665506d | -9.32922 | -55.22059 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ad13257-9b77-3248-bc34-81a069bad081 | -12.97368 | -54.78445 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3edc453b-012a-301c-ab5f-faa6e104497c | -15.02339 | -50.03223 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cebc6742-e04b-3c72-882d-ff454c863ab2 | -7.68798 | -50.26899 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5d3c697-2400-3dd4-a695-8bb1f932aac0 | -7.71742 | -50.31897 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3e69d009-ab9a-3ddb-91cb-ca458e68fe1b | -15.23952 | -48.06074 | 2025-09-04 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6848f8a-f8af-3dda-bed3-dac3aa418663 | -15.03743 | -50.07344 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 420dc802-93b6-341b-9c20-6877e3b72dbf | -9.64406 | -46.1213 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 012faee5-fe71-3041-ae71-7dbe1e181754 | -11.03401 | -45.14165 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 5e5e42b2-f094-35b6-bbe4-0d46eab31994 | -14.59345 | -48.01781 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec638668-1ac6-3b34-ac8e-e8d6fbcc5f3f | -15.04213 | -48.10556 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3fa9661-9e10-358d-a149-c64d35d164bf | -11.8496 | -51.45283 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27e87531-ec04-32ce-a3bd-45c7b4fe9cf3 | -12.86595 | -48.017 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7de01868-4a9d-3c9f-a239-7cdd028bb17f | -13.45755 | -46.93493 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa8639a1-0a70-3458-a48b-dd45962e0e43 | -6.83822 | -59.36734 | 2025-09-04 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 261c4f6e-561e-3355-86a2-f6c774e53f86 | -12.89175 | -56.95429 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b919f109-cd3d-3855-b5f4-0918176ddec4 | -10.57814 | -55.41657 | 2025-09-04 04:27:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1ab78935-a101-3861-a2f1-60d461f5748e | -7.80112 | -52.13644 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a24bd37b-5411-3249-a140-6cb1624804fe | -12.5057 | -48.0591 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18a3b391-a185-3079-9fb1-08de6823367e | -14.57031 | -48.07937 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d2baacd9-e25d-3dc8-a887-a75ca3effc42 | -12.88851 | -48.02428 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48872e03-7c6c-36e4-9770-44d4269ebe5c | -14.82441 | -48.21535 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0750d838-4ef1-35b1-adc8-97c410843d38 | -13.86239 | -47.97388 | 2025-09-04 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9027d179-ff06-323e-90a7-3d57ff635779 | -15.04608 | -50.06318 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0fcdd0d-5778-3b5a-8554-000c42c51fd0 | -14.91116 | -49.61845 | 2025-09-04 04:27:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f995037-14f5-3653-8bf6-3ff5af48ad9d | -9.57631 | -48.63465 | 2025-09-04 04:27:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f09aa4b3-4bba-36c2-9878-3d19ce344b69 | -8.89718 | -45.87097 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| feb62a73-e880-38a1-8bdb-c71541dd4f2e | -10.52842 | -46.75577 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0505cf6d-f625-3674-bfc2-c455cfad6145 | -11.63613 | -52.19121 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7520a292-128c-3b0c-b71e-15b18be6b518 | -12.465 | -48.07787 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed8d921a-a393-36e5-af20-4d443bcbe789 | -7.74615 | -48.76846 | 2025-09-04 04:27:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 58632c00-4ba4-38ce-a671-9ff33b2bc073 | -7.70415 | -50.28512 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dcd34f9-cbd7-3cf1-8ee5-4e4c803bde69 | -8.35359 | -48.31507 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76a454fa-bbb0-3f37-8008-dd9e80037663 | -7.38972 | -49.39787 | 2025-09-04 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71ca9897-f996-3ab9-8ec7-766a8b678e37 | -13.00286 | -48.07588 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c89c14e3-4620-39b4-8c93-907fb8ad8296 | -11.63914 | -52.19688 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbec9a47-7a93-3b42-9857-67cb24ccda9a | -11.87134 | -51.54926 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2067cae0-6604-3c5f-9aab-c25684e2a9f1 | -10.47984 | -53.63023 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 626a975f-3147-31ab-b152-98e7cc487350 | -14.82166 | -48.21127 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2b5dce6-ffa3-378d-83b9-667b9e48c387 | -12.9869 | -48.06965 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf4913d7-1fb1-336f-9cea-689d6c31f638 | -8.07907 | -45.35317 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0010409-420b-3f68-8c54-8dd0480b6062 | -14.57062 | -48.05354 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e65a12f-a2ae-36b9-ab4b-df1c97455d70 | -14.81889 | -48.229 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69f97db8-bd3d-3182-8da5-b7df843c2b13 | -10.09541 | -54.75706 | 2025-09-04 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef938700-cd5c-31dc-9bab-fa070aa7a454 | -12.97733 | -54.7899 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d466ab64-ac6d-336c-b0e9-c2ddb68c3c2a | -12.8852 | -48.02375 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 120e63c6-472a-3d8a-9a55-1f105e9ff356 | -12.48978 | -48.07111 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fde7527-3719-3e16-8a58-39aa89f684a3 | -9.6922 | -51.0443 | 2025-09-04 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eedef84b-c53e-3143-88f6-67ddf91a30d8 | -14.81891 | -48.20717 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57c56852-057a-3c9f-b14e-f533cf8838fb | -8.87597 | -45.85318 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ec9bf33-9bf2-3b14-b97d-b44a7f9bf519 | -7.68821 | -48.73625 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1d782fec-c766-3d29-bb3c-f35a8775aa69 | -14.42756 | -53.18972 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecf2693c-4954-3227-b166-73877daca222 | -11.64689 | -52.19833 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a9e0ae2-56c5-3bed-9520-dc48961909d4 | -11.85194 | -51.43929 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d9f339f4-5b28-3c2a-a3f0-2f9b77b36498 | -12.18037 | -53.88539 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26cf65fa-f7d8-3864-ac15-6c9a55585ea0 | -12.9104 | -56.94097 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e9d3775f-0413-30ad-90ad-be7e3f8f94d6 | -12.89484 | -56.93807 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b95760f-09a0-329d-8c77-950d11e97bb6 | -11.53385 | -54.49091 | 2025-09-04 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 585d52b2-6538-3f66-b28c-93f4fbca689c | -13.95483 | -53.9792 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3026594e-1dcc-3536-8123-32b7b6ade5e1 | -8.88375 | -45.84705 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cd87fdf-8294-30dd-8e18-67ff53a9aec0 | -7.7064 | -50.31703 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4bcccd45-504d-3a79-91b3-a2c002e24ea4 | -7.68867 | -50.26481 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94384ee1-c4f5-3d47-8b17-47d6a2d9a9a5 | -14.53814 | -48.06633 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8d1f6f47-1e21-3772-bb98-589322b5fa35 | -8.37879 | -48.33017 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d87c13ec-81a1-332d-8e5c-bdeb848087f7 | -12.47821 | -48.08004 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc95915a-7186-34b4-8aef-bf230bd7bbad | -11.59497 | -52.14498 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b97ac3f9-c432-3fea-b8bc-88732d419d9d | -11.62632 | -46.64698 | 2025-09-04 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5cb32c3-0c11-3438-96bf-2c17d7cbcd7a | -11.64974 | -54.52925 | 2025-09-04 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adb0aacf-f87a-303d-adfd-2b18d7ee1cbd | -10.49148 | -46.77511 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 011fa94e-0e42-3ff3-b25b-798a6d6715c9 | -12.90226 | -48.04455 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee391144-fc03-31cd-9306-44d2360bf861 | -15.04358 | -50.07837 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a216d47a-7fd7-35ce-93cd-d07d492a3450 | -14.59785 | -48.01124 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bc9003e1-0dc2-33db-869f-b91722e00805 | -11.83943 | -51.42336 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88268555-15ff-3259-8113-eb25a7627aba | -10.11432 | -54.78711 | 2025-09-04 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46162ff1-9c6a-3a2a-b314-1155e62b715d | -12.49794 | -53.84502 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64054bc9-f6b5-30bf-ae91-ffb21114959b | -7.71668 | -50.32339 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b0505402-6b29-3bf6-b5cc-65097a374180 | -11.55062 | -47.31446 | 2025-09-04 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ab43d80-78c5-35c2-84dd-8d3872a8bd41 | -7.97588 | -55.31142 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90d471bd-b6d8-3e48-9ece-f32a865bd523 | -8.36869 | -48.32856 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adcfacfc-d267-35cb-ae43-c455da99f46e | -9.60371 | -47.03818 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a82556c8-dc8d-3b83-9f08-6f6456f93325 | -11.59664 | -47.78128 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b4e33de4-d201-38bc-880c-868302dda8fa | -12.46058 | -48.08437 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| effc4dad-dde2-31de-99cd-3458ca07f549 | -10.03866 | -48.14399 | 2025-09-04 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b25fb4f6-4adf-3828-9175-be530079f142 | -8.89754 | -45.80182 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 024a2f9c-5c85-3427-934c-aaec8e277808 | -12.97615 | -54.77082 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b6eb32e-31e4-3219-85da-f234942afd50 | -10.02911 | -46.09042 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfd7d8f4-4780-3429-85dd-0ec319de8b1b | -13.46619 | -46.83207 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94136075-64df-3178-967e-5d16124425f3 | -12.99681 | -48.07127 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README37.md)
