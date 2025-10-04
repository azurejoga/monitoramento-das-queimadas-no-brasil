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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b10cd27e-defc-356e-9d84-570883a44a26 | -5.30628 | -43.09963 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ec575b6-e1ba-3e8b-bbf7-41c9fde3fd71 | -7.72166 | -42.5799 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d860d6b8-1971-3ddc-858d-ad11ef7166c2 | -7.76545 | -42.51495 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cdb32c96-a770-3440-8778-946da804c608 | -6.65114 | -41.95224 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 716f0c7f-2feb-360a-acd0-4aa91e6f8521 | -4.51114 | -50.80295 | 2025-10-04 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e58fb50-ed0d-348e-9ade-e8ad1028f1f3 | -7.48391 | -43.03409 | 2025-10-04 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 52bb77f8-8540-3393-bf2e-160feaf731db | -7.71002 | -42.56731 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d2371cf3-19ab-38df-a538-116ba8b5381f | -7.7467 | -42.54794 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5f0ebce6-22af-3da6-917d-538c9912798b | -6.0946 | -43.48441 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cced391-aea9-3d86-915b-4ba96adab621 | -2.25971 | -47.85917 | 2025-10-04 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d582dfee-97f7-3c99-8aa8-21cef6b5c98b | -4.6098 | -43.14235 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c850249-5be4-3445-ab48-d6677998eb17 | -5.66008 | -42.71054 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1319f8f9-7085-34b0-8218-54c5be4af934 | -7.00378 | -42.30645 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9debe8ef-153b-353e-8f4a-8df11a07398b | -5.69314 | -49.30654 | 2025-10-04 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1eee3528-e978-3ae5-8f69-529f3a82c283 | -3.84421 | -41.57798 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6f782710-194b-3b8f-872c-bc00e10479ee | -7.74615 | -42.55145 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a58b69cf-c5be-3a5d-b4f9-80f21e855945 | -5.68714 | -43.03305 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 19ab5109-067a-3a59-a410-be6b18f09c17 | -7.77136 | -44.15746 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05f680e8-1e53-3765-9cf4-70e241f5a1d6 | -5.68925 | -42.69744 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3635f70a-7f74-32e1-a9ba-4889d3510e33 | -6.66408 | -43.51479 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44011729-0244-3724-8745-5b9d71251fd0 | -5.19744 | -45.0722 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 481c0abe-1e29-3133-b4ff-9f5b22969ea9 | -5.86988 | -42.67263 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 02943a63-1bdb-3771-adee-37609d2e0f11 | -6.42322 | -43.03954 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40475098-5330-3c05-89e1-e95526c9b7e0 | -5.65351 | -42.73072 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3db39dde-4ffe-3f51-9519-522dcca3aec0 | -6.60816 | -44.30959 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37884aca-e007-3de7-b8e7-a03cdc470d2b | -5.19521 | -45.06394 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| c4f7111e-3cef-37ac-ac2b-b6b125ceb640 | -5.77365 | -45.76423 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 091671bd-2798-3bd5-aa16-6d72df2c0b7f | -4.25027 | -48.56601 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c8909af-78e8-3e3d-be40-4833f6ad323c | -5.96705 | -43.4964 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1928ac7f-1459-3620-ac3d-31aa9bfbf445 | -2.89029 | -50.73302 | 2025-10-04 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 106a37c0-9957-3b20-b84e-7e19c2b1abb3 | -7.78167 | -42.58572 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e85e3dbb-96cb-3c5f-a905-8ddf1b4e40cd | -5.2633 | -43.15668 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a881861a-2f6a-35e2-a1a0-c84beeb566a8 | -6.36961 | -44.30066 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b8e40a4f-4191-3b8f-851f-78acad0f0838 | -6.71307 | -42.81642 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e86278c4-0e76-3a18-84e0-6ee0727e6e47 | -7.70787 | -42.60277 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 005f8c91-fca3-3260-9c49-a1c11f8974ea | -4.4354 | -43.2355 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f0c2495-d439-36ce-bbab-8b68d8004cda | -6.05149 | -42.50985 | 2025-10-04 04:12:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf48e57c-808e-3022-a2cf-58b3091c6ab7 | -5.82588 | -42.88519 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c1549456-f120-30de-a93d-6f039a395fd0 | -6.16252 | -44.61249 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44eb41f2-a756-3e3f-8014-6300f0f4a325 | -7.72827 | -42.55943 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7518dafa-76b3-39c3-b2e8-6c7032b453d9 | -3.09113 | -47.01821 | 2025-10-04 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ded4d1de-7190-3627-af6f-94223bb93abe | -6.0548 | -42.51037 | 2025-10-04 04:12:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 773af8c6-7da2-385c-8f5a-6d4e6b24640d | -6.28209 | -42.44699 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 19f26e4f-7c23-3087-bb98-73e6cdaf382c | -5.66284 | -42.71451 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a4ef5549-075b-3974-bd51-37d09ea97737 | -6.07798 | -42.51399 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 92.1 |
| e4831cf8-3742-3530-8413-5aeae7325c86 | -6.69242 | -48.21019 | 2025-10-04 04:12:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71a77140-adfc-347f-bde2-bd965cd2d10a | -6.09848 | -43.48143 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbc0dbd3-5290-37cb-a98f-14f3f512bdfa | -6.07135 | -44.33114 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8125e687-407d-3b28-9e67-06607040ab92 | -6.99096 | -42.79995 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a5f9bd06-533e-319f-9e5b-7d0f5e4e2628 | -5.24657 | -45.55162 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f6fdd30-c3b8-3744-a799-252b8442deec | -5.22135 | -50.8288 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0bed261-72ea-3ef4-9c7a-88d085ea0527 | -4.43873 | -43.25741 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03d34ac3-bf7e-3235-b27e-5071f0c10dcd | -5.90746 | -49.29393 | 2025-10-04 04:12:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c0e8c2a-2542-3377-8e8a-12e66d91e90a | -7.78472 | -44.13789 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a43bd8dc-c8ba-3dcd-9b83-400de8139a7d | -7.65621 | -45.44107 | 2025-10-04 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a24aa03d-6a52-36e6-9659-02e9e7c08f6d | -7.04918 | -37.96756 | 2025-10-04 04:12:00 | NOAA-20 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| be10aa47-b76d-38e5-a048-737bde71d89b | -7.79105 | -42.56926 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 76f428f7-627f-328b-a0a6-0873707cd87b | -6.28571 | -43.62857 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce2591f1-d826-378a-a6fc-4f3bada750d5 | -5.32478 | -43.34763 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aad73d04-a9ee-30ac-a2da-0c2a9ebe5d67 | -6.68994 | -42.83408 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9035cdce-1974-36be-b3ee-86ab79d5a385 | -5.48613 | -44.10606 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5625f387-245e-39c7-b08d-1ebd087948ef | -5.19868 | -45.06454 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 8c56eefd-f82c-3d06-baf6-197ad876139a | -5.20153 | -45.06898 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 55321564-5fe8-351d-8fd6-5d2d3be581f5 | -7.74718 | -42.52288 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 46e54856-689c-3555-b6d4-f89861a95eff | -5.9853 | -43.48856 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 92f02e09-b96c-31aa-845d-285cba10cc1d | -6.37281 | -44.65709 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 906542fc-8f28-3a6e-8f23-8686c5238e05 | -5.2672 | -42.91714 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4deaa793-8795-3484-b17b-3d70734ec6ad | -6.6513 | -42.79961 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c54edb0b-bfdd-386c-8aad-2295a3a5f16e | -6.17375 | -43.92776 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd581369-9e22-3f5a-8d45-f0b9f633f842 | -7.10603 | -45.09222 | 2025-10-04 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a89f7c5e-a9be-3146-a632-fd7a17f84ee0 | -5.48499 | -44.11322 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4a0cbc51-3eb4-3b30-a643-a542ccafeb5f | -6.99383 | -42.32642 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6b1632f7-acbb-3356-a1e6-4839f79d070e | -5.68349 | -42.8415 | 2025-10-04 04:12:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 367009d8-1e2d-3c30-affd-060e829fdbfc | -7.05024 | -43.22075 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6cf8219a-2e2c-3392-bd00-a4a8bd4bf3e5 | -5.2618 | -37.93213 | 2025-10-04 04:12:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 65d71491-26c5-38cf-92b8-b112f01e474e | -5.73557 | -42.92048 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 66801b49-9f62-33aa-bc65-ff9d3df06353 | -5.47245 | -42.77961 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 20b6c3c8-4556-3162-9cce-004d916fb2c2 | -6.15783 | -44.11375 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d89ea79-4565-3165-8dc0-5463e84902ba | -6.61046 | -44.2953 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40d47fae-d0b3-341c-bae9-69e9cf48190d | -7.78528 | -44.13439 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f4c94a0-8f16-3472-bdda-ec1551bc91cd | -6.35147 | -43.45021 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb432637-ac0a-3b9e-9079-be6a7a87a76d | -2.26035 | -47.85524 | 2025-10-04 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f19c6ccc-e68c-30d6-b09d-c8ff0bc4c579 | -7.75383 | -42.52394 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7e32530a-cb37-35c9-beda-66d6a2c13015 | -5.87746 | -42.5147 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 635aa9a3-52b5-379c-8f37-91b0d1e0fba1 | -7.71501 | -42.57886 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 17a9fc17-8dd5-392e-bc17-841b4e3e28cf | -5.27878 | -42.65042 | 2025-10-04 04:12:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6148164c-fa43-37d7-ac5a-a29ea98e3e9a | -5.80021 | -42.72554 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 124fab3d-005b-386f-b54e-f8f5e319c0ae | -6.18629 | -43.59204 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b3da5f1-5b31-3526-bef5-2da9aa14e784 | -7.0196 | -42.31215 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f8141f8b-02a9-3f14-b214-d6f09cfc0538 | -5.49229 | -44.11072 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd3e9d06-7af0-3c6a-a6e5-fa07da05ad37 | -7.15416 | -44.21087 | 2025-10-04 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dabcfb9-39be-310b-a1a6-a73492616a07 | -6.64724 | -41.95533 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 709a853a-c76b-328a-adab-f2095f7e22fe | -6.10675 | -43.42938 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be107c5d-5f1b-3750-97f4-e33abe494adc | -5.32565 | -43.14877 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23771cab-f8dc-39b3-a489-c602749cc802 | -5.7367 | -42.9348 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1fba248b-7719-3067-9bf4-e86f7f679218 | -6.22041 | -44.27298 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 202faf64-4f8b-32f9-94a5-14d1fd6587be | -4.27634 | -48.87674 | 2025-10-04 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b94c237-9f92-3337-b516-0548ed74dcb0 | -5.60909 | -43.22617 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5592878a-9b1d-332a-ae2f-b30d4aa02c15 | -5.7128 | -42.63399 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ae3b69a-1cb4-38f8-8170-fb18c7f9ee1b | -6.34153 | -43.44865 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README58.md)
