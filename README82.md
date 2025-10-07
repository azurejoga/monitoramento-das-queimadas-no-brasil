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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3831fc2b-9dd6-3e35-be0a-d27b6f4cd56f | -6.6267 | -56.28225 | 2025-10-07 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 644b6266-9b44-3c96-abd1-39d3ea530ce9 | -4.68537 | -49.49117 | 2025-10-07 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35ad096b-cb23-392f-b5b2-cb685dace5c2 | -3.08816 | -51.25364 | 2025-10-07 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8585342f-3121-3c77-accf-fd7d6087a461 | -8.62029 | -44.93336 | 2025-10-07 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc134033-1e47-3d16-8d82-1cae557226be | -7.52441 | -49.91278 | 2025-10-07 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c59bc76-ac2e-35d2-a79a-19cd18a37e02 | -6.71657 | -42.85229 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 16bb4d77-b12e-3c27-8c55-302926aedda5 | -3.46946 | -51.6394 | 2025-10-07 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f835bee-3fc5-3bb8-b162-c5c560168f26 | -3.09953 | -47.02122 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b0c6f2f-8f1c-337b-9cc2-5de16608bae4 | -2.271 | -47.19706 | 2025-10-07 04:55:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46b0d098-ce4c-31de-a3d4-8a982300612c | -3.09618 | -47.01361 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eadcb7a7-4a0d-38a0-9488-c0d22c0c295a | -5.49666 | -43.06408 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69e0f402-105a-3424-a90c-dd01a3fa9bb9 | -2.93595 | -54.17649 | 2025-10-07 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff245b71-29a4-3338-b7d2-f215ec5606ea | -3.0898 | -47.02571 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e90a8d73-9b17-37aa-b64b-fa8def78f62b | -2.26669 | -47.19656 | 2025-10-07 04:55:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c917945b-a432-379d-944a-47529f7d8019 | -7.51667 | -49.91164 | 2025-10-07 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe12dee3-7ea9-3319-a140-0bf768c04c77 | -5.74588 | -44.98885 | 2025-10-07 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b8ee097-0397-36cf-9c48-77031a29fa14 | -5.74682 | -44.98547 | 2025-10-07 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae4f037c-3d69-363f-9d68-cbb7370d227f | -8.1947 | -44.23167 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6323e53e-547d-315f-ae02-958134a62790 | -8.1799 | -43.35689 | 2025-10-07 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 523a830d-3a7f-3dce-98ce-70eb18ddfc77 | -6.70974 | -42.85656 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a2755e5-ca4f-32ca-913b-cd1d6a34620e | -7.51737 | -49.90679 | 2025-10-07 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d046cee-125f-3466-893d-ade530ddc590 | -7.68951 | -42.41464 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3c9088ce-a437-38f9-9893-d60a14d5956a | -4.69212 | -45.83662 | 2025-10-07 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 35.2 |
| c98a4323-65b1-3199-ad6a-2f66f930d5e7 | -2.89558 | -50.73365 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5abf28c7-b4ea-3124-a4f0-9a12d2ad31e4 | -6.2968 | -46.09017 | 2025-10-07 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07a25af3-d9ff-34df-80c3-936a56aff5fa | -6.62731 | -56.27847 | 2025-10-07 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c5b55f3-695d-38fc-a52c-03bbc1cbad59 | -8.19078 | -44.12078 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0446d167-fe3f-3218-a47b-afe1e9c8c3c6 | -5.48945 | -43.072 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5b663a07-ba1b-397c-a9df-d72b7bdbd8fa | -7.46644 | -42.62494 | 2025-10-07 04:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a6cb31ce-d27a-30e6-9283-a5ebdb8b101b | -8.20091 | -44.1832 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92f915c6-f0cf-3e22-96e7-d4723a4cb9fc | -5.74637 | -44.98859 | 2025-10-07 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9fcb330-5111-37f5-af18-46124dea2da2 | -7.52323 | -49.91083 | 2025-10-07 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 426261c6-6f4b-3cb4-b9b8-0e038a63a5e2 | -3.09202 | -47.01126 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b91dd680-f995-3f8d-8c4c-ab0c50952dba | -3.09685 | -47.00935 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cefbfeb-aa34-31c2-8a92-086cc2918898 | -5.73988 | -49.13802 | 2025-10-07 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fe5b37bf-2376-3df1-adf3-ea62113ae10b | -2.79664 | -54.86097 | 2025-10-07 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1a21e43-49ae-3a04-8ff2-03bc44ebdcba | -6.16799 | -51.16091 | 2025-10-07 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75483739-eb7f-374f-af56-5fbcab7718de | -4.9158 | -48.02363 | 2025-10-07 04:55:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b9dd3f8-e9c1-3dd6-beb0-4e430e7b8070 | -3.13911 | -50.44545 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ebf3815-ddc5-3d8d-9e46-817a8532476e | -4.91159 | -48.02297 | 2025-10-07 04:55:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0955722f-71c1-39c9-b880-ae5ead069358 | -5.77381 | -45.7454 | 2025-10-07 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d66a2c1c-897a-3882-8b56-9daf15a962f9 | -5.03315 | -45.56242 | 2025-10-07 04:55:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 879444f3-4b6b-3db6-9c0e-36d639c46850 | -5.50013 | -43.06363 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4546a63d-ff72-3961-bedf-484f21d6ee9a | -7.46716 | -42.6197 | 2025-10-07 04:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 27104352-37b2-39ff-903a-a895bdb4943a | -3.4689 | -51.64306 | 2025-10-07 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e07191e-8173-35c8-95dd-471c44098ee8 | -5.49777 | -43.08081 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c18f8c83-6ce5-38c8-a646-8411c7439f91 | -3.13555 | -50.4449 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9370ab5-4515-300f-b02e-9f9ad83dc53c | -3.04849 | -51.10133 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 430b2e96-1a82-34bb-8913-d96b083cfd36 | -4.06897 | -44.50988 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03d889fe-6a03-3f18-8a88-7dfe4d5bd2f4 | -3.09485 | -47.02213 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 013cb883-564e-3077-a9d8-ddb06582a651 | -4.06415 | -44.5058 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5add8195-17ba-3899-b717-0432a8554a3d | -3.09075 | -47.01985 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| af664f78-3e1c-3afb-a7ad-301c00e1af71 | -8.20095 | -44.22844 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bc891d7-60d2-36c5-ba3b-0b4119bc7608 | -4.68466 | -49.49592 | 2025-10-07 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1c686e6-e0a2-34ad-8561-d854c8f4b432 | -7.00563 | -42.79053 | 2025-10-07 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 23a89426-fdcf-33ca-8d3d-e3786d9ee124 | -7.46574 | -42.63015 | 2025-10-07 04:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 58d6aba4-3bc6-38a1-a1a7-41c0e9f104fa | -8.20142 | -44.17918 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdeeadc1-451b-3ecb-8cce-5214370d7d41 | -1.09701 | -53.68764 | 2025-10-07 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b06b3406-200d-3c74-9c2c-23487d50c20a | -4.68644 | -45.84137 | 2025-10-07 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 078b50b3-0fa8-33f7-9bef-020153226ba7 | -6.5877 | -44.63056 | 2025-10-07 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ca9738f-fe52-38c9-bffc-519af1b188b7 | -8.48853 | -46.27165 | 2025-10-07 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5baf2a99-e084-3e77-b632-796f4f4f501b | -8.19708 | -44.20452 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41e642a5-1388-3d86-8f37-281e353fa28e | -8.21073 | -46.98952 | 2025-10-07 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd647a85-1ee1-3200-9fc5-2f9799f25e37 | -7.67497 | -50.21041 | 2025-10-07 04:55:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d97b6c1-e13c-31dc-9814-3492bda4ed36 | -3.6628 | -51.95042 | 2025-10-07 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7644440-35ff-36a6-9911-b4056cc7f78b | -4.55085 | -46.67931 | 2025-10-07 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53eeec78-7129-35bf-bbf7-229e09d01e87 | -7.01925 | -42.78278 | 2025-10-07 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 063dddb9-f7a3-316d-801b-c2e1909ea41b | -1.36819 | -49.03962 | 2025-10-07 04:55:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 349272d1-e8e2-3140-b778-95841f4cd8b9 | -7.68715 | -42.417 | 2025-10-07 04:55:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3b53afd3-f47a-37ed-9ab8-c443d0921fe3 | -4.0719 | -55.41902 | 2025-10-07 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4d7b82d5-9535-3e51-89fd-d815c91f7862 | -6.70223 | -42.86687 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bf1d279b-0ab1-346e-8385-4f4cb14ffae7 | -6.33886 | -44.02626 | 2025-10-07 04:55:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35f4ee25-284a-3272-a2c6-a8868221f800 | -6.7028 | -42.86281 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ea3d3c8e-c357-3f01-a29b-e6b7f86f7517 | -2.70457 | -59.68848 | 2025-10-07 04:55:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84473cac-9cf4-3b5a-965e-b3488a5023bc | -5.2546 | -46.57447 | 2025-10-07 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df69a3ac-e691-352c-841a-067bbda8524a | -7.51549 | -49.90971 | 2025-10-07 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0d39b8f-8308-3049-994d-bdef96840ade | -5.64044 | -45.96403 | 2025-10-07 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e38841a-1617-36bd-96a0-9e76387f9a16 | -5.7957 | -50.20942 | 2025-10-07 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bac8408-9594-3796-9291-fa290cab020f | -1.70612 | -55.68394 | 2025-10-07 04:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6f077d2-aec1-3a60-b39a-02dc17718634 | -1.08482 | -53.70004 | 2025-10-07 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 291d3001-9f76-3470-a36f-fbc65d66cd49 | -3.09139 | -47.01556 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 7e7636c1-c3a3-3fb2-893e-83b264dfc9cf | -8.19676 | -44.21558 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fd0a916d-4d50-37ee-8cea-ee2c459554e6 | -7.89377 | -47.81125 | 2025-10-07 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a39001cd-fc61-3ead-850d-86e45b15ec94 | -3.09419 | -47.02639 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26c9a11d-f23d-38fc-b419-43fa283c2456 | -8.19728 | -44.21155 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2d590aee-facc-3e4a-9fd6-b2be1f0827fd | -6.75349 | -42.23296 | 2025-10-07 04:55:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f12d3da-1e94-32a6-bd23-84438cc509a5 | -6.72278 | -46.32492 | 2025-10-07 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 45ff018d-b297-3b5d-995c-9710ddeda49d | -6.983 | -42.86968 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| f9227ffb-343e-3da0-9d24-6334856a5b93 | -4.68568 | -45.84662 | 2025-10-07 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 5afe6626-8aa9-3c01-bf05-d76cba89f25f | -6.72463 | -42.83882 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d81208a1-21cc-3ecd-b118-215110815f85 | -2.85372 | -54.09563 | 2025-10-07 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b11e11f-5726-30a5-89cd-e6b7c38150db | -7.47108 | -42.61812 | 2025-10-07 04:55:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| affe71c8-0117-3204-8dfa-96df46a74bdb | -8.6198 | -44.93699 | 2025-10-07 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d64bd716-d122-31e3-b7a3-14acbb662ca9 | -3.09113 | -47.01717 | 2025-10-07 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 75ed1848-2c08-3004-8723-bc59e849527f | -3.14267 | -50.44598 | 2025-10-07 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecbcfcc6-8a92-3835-bc42-0d23ef8bc153 | -8.19954 | -44.2294 | 2025-10-07 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dcc28572-5146-35d9-adc3-c404e7160a88 | -6.69609 | -42.8661 | 2025-10-07 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b99b4298-27bb-34aa-b8c4-84c598e6ec1c | -5.75676 | -43.39719 | 2025-10-07 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c6be31fe-ed4f-32bc-9d84-2cd057f21bae | -5.49602 | -43.0685 | 2025-10-07 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7eee48c7-2e7f-3955-817a-efd8e95715a3 | -1.56466 | -55.43762 | 2025-10-07 04:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README83.md)
