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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55acd8bb-0f52-31eb-ae89-68202d76d291 | -5.1039 | -49.60339 | 2026-09-03 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e09dda02-11c8-3d0a-b01c-6fab02323de5 | -6.67819 | -59.95268 | 2026-09-03 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 334f7e07-2f62-3642-80f8-b43bfc9e33de | -3.34104 | -42.8063 | 2026-09-03 04:38:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e7cfccd-24b8-3f74-9f60-6942ce49b417 | -5.89004 | -49.88398 | 2026-09-03 04:38:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 645188ab-cb0e-3444-8754-a91701481b2d | -1.51126 | -54.96002 | 2026-09-03 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c41c642a-7cd5-3185-b8a0-9e88577d05fb | -6.62192 | -55.23106 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2560b800-bbdf-37ee-a8ef-7aed0d1a4072 | -5.46598 | -60.05981 | 2026-09-03 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 400895b2-9443-3c21-9113-577a19ab40d6 | -8.76922 | -46.43449 | 2026-09-03 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab99f247-e435-36f2-a701-f3801a4b1618 | -6.76832 | -59.44107 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6be3c5d7-f627-3ae2-977d-89bdad60908a | -3.25026 | -47.25129 | 2026-09-03 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4a518cc0-28f0-39f2-8b10-7722a56ee8d9 | -6.39173 | -55.22622 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 75142453-3f12-3281-84b4-54029b1b4f0a | -3.80604 | -49.11173 | 2026-09-03 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02dbdad7-115d-3cae-a07e-eaee9ea1b77c | -8.4304 | -54.7421 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe9533cb-1b39-3d7a-9176-3796f577c318 | -2.72313 | -49.78845 | 2026-09-03 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c11114a-5c80-34d3-81aa-1a0d1c71785c | -6.14967 | -55.67258 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a5130a4-de64-349f-bf81-5af361c4c058 | -3.22276 | -48.61173 | 2026-09-03 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8e683b1-cc20-3a66-b4f8-a668d434e2f5 | -1.9781 | -50.79745 | 2026-09-03 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0954f14f-0566-3fc5-84cd-092ae47b21a5 | -7.61282 | -49.93224 | 2026-09-03 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 249fde8e-58f6-37cf-b6c0-425cb6d6ec35 | -8.43524 | -54.68645 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ff2b1773-7e51-3178-ba60-281c98047294 | -6.15592 | -44.64962 | 2026-09-03 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb0d22dc-aa19-3bcf-9732-e0f3f99cd204 | -8.43528 | -54.74308 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 376161dc-5b74-31a3-9155-7b82cc69d557 | -5.25017 | -55.90322 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7878604-d228-3b8e-9a45-0a243f0083f5 | -7.07919 | -56.51658 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f1c4c39-caf3-32b2-8e64-bdd25dafba83 | -8.07605 | -50.97356 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faec5468-365f-3765-ab39-7ed5a9d6f2cb | -4.94571 | -47.65843 | 2026-09-03 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b0f2c15-eb6d-3c9d-8bbb-9161a430df39 | -4.10811 | -51.02657 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 337ad51e-3c6a-34bf-aec9-080517671ccd | -2.26526 | -47.00912 | 2026-09-03 04:38:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9f89009-ae7e-3c00-940f-ec5646d1542f | -6.64839 | -59.43683 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a47819c-a7b2-3eac-822c-3a55cb05d3e8 | -4.96641 | -55.85574 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfd2b8b4-6326-3203-a267-8306d8cd6a8e | -7.04423 | -59.21788 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5b9b73e-f74a-3bc9-aadb-f05d042dfa51 | -3.93187 | -49.0521 | 2026-09-03 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 664fd372-74ca-334b-9ddf-fd99f78882f3 | -3.24967 | -47.25493 | 2026-09-03 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 91fd9129-1cad-3c5d-987b-322c6cc78b21 | -6.64445 | -59.45016 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2787fd5b-fa4a-3e19-a09d-87fc4ed26fcf | -6.56185 | -43.90427 | 2026-09-03 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4bf25be7-b23f-361a-a799-18d40582ee6f | -3.39375 | -59.36261 | 2026-09-03 04:38:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 043f6e06-f81b-3ebf-a7a2-b575bc281e5c | -6.64691 | -59.43671 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eda55860-2834-3f93-9d11-e832d674490b | -6.7631 | -44.56312 | 2026-09-03 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea4335ce-d847-3fcf-9593-405e3cf63675 | -5.25261 | -55.90691 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbad376d-95fc-34f1-8f17-b9ec33ebe5c8 | -6.88012 | -56.50788 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26312783-a637-3bd6-9677-552f31d4fbe0 | -3.44933 | -56.32506 | 2026-09-03 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ee7c7e2-2a83-3674-81d9-371030489db2 | -2.55283 | -44.14294 | 2026-09-03 04:38:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d4ef64d-7004-37ee-b4e9-982f6b68ad56 | -6.10715 | -52.24377 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43b47526-8e46-310e-9f27-c1c2b807bbdc | -7.31731 | -55.13374 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5288010-6cd6-315e-a723-a3980efbc3e1 | -5.20544 | -38.03289 | 2026-09-03 04:38:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 894aadfb-a92f-37bb-a377-d7d533b4cbc1 | -4.08462 | -51.04164 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1d18cea-19a0-3c5e-b45e-4de4f61dd7e5 | -9.28527 | -35.53062 | 2026-09-03 04:38:00 | NPP-375D | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 0e3d80df-c21a-300c-a686-0421441f9be7 | -3.80316 | -49.11226 | 2026-09-03 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d05f9573-385f-3b26-8a11-467bfd4fcc72 | -8.70811 | -52.36047 | 2026-09-03 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61a804b9-d1a1-33b3-8aa0-ea0c63e8e57a | -1.02045 | -53.72713 | 2026-09-03 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 355f73b5-39bb-3854-addb-1c29495e5a1a | -6.31502 | -56.04029 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ea411164-e1c3-349f-9545-d38157f55590 | -6.62544 | -55.24173 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed6b350d-6737-3e13-ac3a-0fdf9ff350ce | -3.24779 | -47.91507 | 2026-09-03 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8e92afb-2c67-309d-bb41-3bcde64f2a44 | -3.92754 | -49.05572 | 2026-09-03 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccbbe03b-f76b-3c72-8432-d6cb8f77936b | -6.64961 | -59.43042 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11f184a7-43ad-3424-8ea3-92ffccaf9855 | -4.97393 | -55.84574 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2065cd4-c011-3df7-972f-46113e25df21 | -4.26769 | -55.15982 | 2026-09-03 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 246ca03d-ebb2-345d-ae26-2272f54ad292 | -6.15013 | -55.66569 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecc0dbb5-5293-3b4f-978a-6a8392a0750d | -4.54559 | -54.9138 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7a93761-41be-35c1-8dac-3124c3790100 | -4.11164 | -51.03065 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94115e18-4d0a-3a60-98b4-4fd169b2347f | -6.48894 | -45.92223 | 2026-09-03 04:38:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f6d9536-c4d4-3f42-9cae-7787f298f273 | -4.02294 | -47.72237 | 2026-09-03 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ec8ecd9-0aae-3fd4-972e-f4900c7b5b64 | -3.97133 | -41.52249 | 2026-09-03 04:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fafb6405-3cbe-3541-84db-6a06c27ddce2 | -6.74665 | -59.43707 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b26d9c0b-83b1-33da-9dcf-d17ca932aeb3 | -7.12094 | -45.81876 | 2026-09-03 04:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 607ed555-317c-3c0c-835d-5d661a5229e2 | -6.74794 | -59.43752 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b975ddac-2a38-3b92-8857-41f2d6c64b8b | -7.24002 | -42.76384 | 2026-09-03 04:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6b62be6a-864a-36db-ba37-3777e61446a3 | -9.61025 | -40.34226 | 2026-09-03 04:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| cd572402-fd92-3b24-ba9b-8b482d8060b0 | -2.26129 | -47.01221 | 2026-09-03 04:38:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42686fd0-94e4-3c65-8b15-9461ab7d670a | -6.31569 | -56.03661 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1af80643-5872-3f00-8b3b-d90abe26aa79 | -5.45884 | -60.05839 | 2026-09-03 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6eea2de-6e17-3c77-99c5-43d1a2becc4f | -4.69484 | -56.06544 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58a20634-bee7-328c-95fc-abf05b6ddb00 | -6.68515 | -59.95414 | 2026-09-03 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f45795d2-9383-3601-8a91-b6b728685c69 | -4.11632 | -51.02771 | 2026-09-03 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6b7df54-259b-3fd6-b1e7-efc51f088ccb | -2.92809 | -54.0957 | 2026-09-03 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ff774fd-c48b-3229-ac1a-184d21c2b4da | -3.96667 | -40.05338 | 2026-09-03 04:38:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45296d38-7550-3f08-a2ab-a77e3f26585f | -6.68646 | -59.94727 | 2026-09-03 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb30ca8b-732e-395e-ac36-aecefed6cd89 | -8.06485 | -49.79882 | 2026-09-03 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 275f0cd1-6bd7-32a7-9b2e-01f4b7059a8f | -6.76138 | -44.57421 | 2026-09-03 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dad59539-94a6-34ac-8bb4-96a9c3941fe7 | -5.80247 | -50.13231 | 2026-09-03 04:38:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d472144-4042-356d-b81d-2a7dd4c4ede2 | -6.62023 | -55.24073 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5d2446a-abd5-34d8-bdfb-6778f42822a5 | -5.4682 | -60.06093 | 2026-09-03 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e11c38db-e598-3ebb-b857-18ccbe9a04a8 | -4.69098 | -56.06356 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73821116-446e-3301-9c5d-e1f0dccbde48 | -1.02598 | -53.72576 | 2026-09-03 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6813ca6-a001-36dc-9bd2-062ae5b2fd68 | -6.62601 | -55.23852 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69b74be0-461e-3d2e-a0aa-6def130d38eb | -8.45556 | -54.65696 | 2026-09-03 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6955ae9e-d918-36e5-91bc-4391c7d3097e | -5.41648 | -44.80295 | 2026-09-03 04:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e03237e-2af8-36a4-b04e-40711eacbfbb | -4.37898 | -50.76589 | 2026-09-03 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d9ae17f-836c-3cb7-ac6d-1d769d658500 | -6.14477 | -55.66441 | 2026-09-03 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 02152b28-3f8b-3f5f-97c2-23dc4729384b | -6.67594 | -43.41185 | 2026-09-03 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e87d3bd-5b52-375d-a6b0-7d89fcc792c8 | -6.43578 | -42.10572 | 2026-09-03 04:38:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| db4897d7-9565-32d5-a0b4-8affa0ca47b7 | -6.76701 | -59.44074 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d4c9b917-a85c-3e39-9229-3bed721b98eb | -4.97263 | -55.85313 | 2026-09-03 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9afcc47a-01cd-3e54-b749-d717d3d13c1a | -1.62151 | -55.16883 | 2026-09-03 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfafcfcb-326e-3980-a729-368b08fa21a7 | -5.47313 | -60.06123 | 2026-09-03 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4698af00-5bb9-3875-b5e8-4e2c8f22da4d | -7.29035 | -49.80784 | 2026-09-03 04:38:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3289ca83-dc54-3b7d-a17a-5117985533af | -8.96017 | -49.51579 | 2026-09-03 04:38:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93faa6ac-e202-3087-b0f8-b86196d609bc | -8.0815 | -50.96474 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 27d2b0f6-b413-38c0-9c22-126ea6d5d917 | -8.08374 | -50.97488 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f07b3e8d-5efb-3d02-8137-6a29584fc430 | -6.65263 | -59.45155 | 2026-09-03 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0012b08c-14d9-3f7e-a125-a480f5ad3699 | -8.08615 | -50.96062 | 2026-09-03 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README25.md)
