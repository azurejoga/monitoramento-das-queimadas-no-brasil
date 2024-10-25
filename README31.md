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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc6b5e9f-0fce-3afb-8dfc-86629123a4b0 | -4.07692 | -48.27492 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01f38f0b-a53c-334e-8f2b-f18e8d300c0f | -4.07144 | -48.28202 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db4e5497-a139-344a-9590-768309d095d5 | -4.04416 | -48.10758 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2ecb47f6-dd2b-3c5b-b098-3de5dc1a2be1 | -4.04108 | -47.95602 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99218209-ad44-30a0-8d6d-e507edc44f05 | -4.0402 | -47.95283 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2118f65a-3701-3421-afd6-025566609e14 | -4.36537 | -48.61037 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bac37e3-779a-3ed4-94cb-bb41a696df9e | -4.36306 | -48.59746 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d0951cf-e48e-32a2-91ae-b2a513c86922 | -4.34196 | -48.6189 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 725aed0d-6b2f-3444-b0e5-85d044973b16 | -4.3307 | -48.6338 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| e6167c15-0b19-3117-9e1f-d1ee225581c2 | -4.33002 | -48.63794 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 9558f259-670c-3d4a-9409-ad49e497fcdf | -4.29267 | -48.62357 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c8c3b4c7-327e-3a9d-9b31-a134115b4e83 | -4.27026 | -48.59932 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6485eab5-7a4c-346c-99f8-15476949ef4d | -4.24853 | -48.55383 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| da8b4db1-412d-35b2-bc40-dbe52feffbbe | -4.24782 | -48.34501 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ad242a5f-e07f-3c09-aa40-60c9a4b1add0 | -4.24489 | -48.54914 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 58a537b7-5848-3dc5-9d67-0222946df40d | -4.24424 | -48.3404 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1449db3f-9137-3dda-a9fa-62b0b102d853 | -4.24359 | -48.55717 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4bbdd2a3-6a4c-318f-8732-696464e63ad1 | -4.24358 | -48.34443 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 06dd6d2a-33b9-3e44-8398-4603e6e3771c | -4.24061 | -48.54849 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 9a276fbc-9a00-320d-8305-bf89d023df35 | -4.23865 | -48.56049 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dfe8d239-d342-3423-a99b-cfd2a5578031 | -4.21655 | -48.56116 | 2024-10-25 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9b76ed67-ddb9-3ff8-b0ee-23e9dc3195e3 | -4.14183 | -48.74373 | 2024-10-25 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e50ddf35-51c3-354b-925e-f9e1cdc394ec | -4.14073 | -48.96552 | 2024-10-25 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db8451be-7f56-399a-a678-703b3d7155e4 | -4.13749 | -48.743 | 2024-10-25 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95ff242e-5a58-380f-b91d-cb063064e0aa | -4.1356 | -48.96915 | 2024-10-25 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0f392151-eeb1-36dc-bfe5-4afd42231653 | -4.09581 | -48.2381 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9593cee0-96c0-327b-9a21-2cfdbf3fbae9 | -4.06954 | -48.29372 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7081389c-f2db-3030-be07-e425906048ef | -4.06874 | -48.24549 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a81049a-06fc-3981-96b3-582f3e94f452 | -4.05187 | -48.11269 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c4a23a44-0dd1-36d3-bb03-035dab78ab86 | -4.05126 | -48.11639 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0c809ea8-f05b-3dec-b404-3e414c517a15 | -4.04478 | -48.10385 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1f493ebc-c30a-3bff-8314-688fd07edb87 | -3.9863 | -49.02283 | 2024-10-25 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c184790a-4b9d-352f-bf1d-78494944dbe6 | -3.93327 | -48.35693 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4bddb24-50ac-3232-9280-0801a5c1637b | -3.9323 | -48.33626 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 787d248e-4adc-3672-85aa-b23879b8a198 | -3.92741 | -48.3395 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d4346854-4098-374c-bd80-988496c4b168 | -3.91788 | -48.37102 | 2024-10-25 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3da69d68-caa7-3112-abe6-b283741d790e | -3.91363 | -48.3703 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 808c4f01-4f68-3cd3-a1dc-59a45eaebae1 | -3.91005 | -48.36555 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 278f0e03-4395-3252-aebb-9444e572df21 | -3.90939 | -48.36959 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a48d3f6e-a3cf-3344-a9b5-967f4827248a | -3.82824 | -48.88772 | 2024-10-25 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9d05e89a-2086-3c0a-84b5-88c1872c6f16 | -6.4891 | -48.76354 | 2024-10-25 04:14:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c797817a-95ad-399b-9d32-e74681f3574e | -6.48522 | -48.73518 | 2024-10-25 04:14:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10cbe85d-89b4-36b2-8cd5-5d73e9ed5552 | -6.29921 | -49.30493 | 2024-10-25 04:14:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fda68ea3-6cfc-34be-88fa-b7ae590fad3e | -6.48458 | -48.73903 | 2024-10-25 04:14:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a04f18d-3632-3038-ab82-4255ba1299e9 | -5.52838 | -48.10558 | 2024-10-25 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fd9bbae-8a36-3da7-b799-d5766ed5bf78 | -5.30689 | -48.17827 | 2024-10-25 04:14:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28286b7f-697b-3e22-98c7-5edcc1f851ba | -5.22353 | -47.95136 | 2024-10-25 04:14:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd6e5b40-c74d-3587-aeec-cb4498804553 | -5.20875 | -48.21506 | 2024-10-25 04:14:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9ab5259e-47e2-34f5-ada5-b9a13a1c8a58 | -2.80927 | -49.23831 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0de60224-d027-3304-beb8-b2f59e1dce41 | -5.21224 | -48.21947 | 2024-10-25 04:14:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fb67e2a4-bfe2-3436-a6dd-8556d0655e91 | -5.20812 | -48.21878 | 2024-10-25 04:14:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 01335aaf-90dd-3874-b7f1-d1f31f047b74 | -5.20749 | -48.22252 | 2024-10-25 04:14:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c7aa4687-e614-3837-945c-fd4bd4e71806 | -6.30357 | -49.30565 | 2024-10-25 04:14:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6da73204-e21e-3db7-b5e4-00640608c475 | -7.8209 | -49.82882 | 2024-10-25 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40e0263a-03e9-3c77-9054-4e3474d504b1 | -7.79323 | -49.52338 | 2024-10-25 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad1c9f92-8172-3986-91d4-7bcf630f5531 | -7.79127 | -49.52303 | 2024-10-25 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39cb6e5d-97d7-3d14-8e38-6ac093cdc822 | -7.69873 | -48.85559 | 2024-10-25 04:14:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 642547bf-a73f-3947-b554-0de7e08e8c0c | -7.69698 | -48.85501 | 2024-10-25 04:14:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1f6c707-b356-3d0a-9fe5-cb520a7eb4cc | -7.5953 | -49.61594 | 2024-10-25 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 479e960c-8e3f-3cc6-aab5-9da96759194f | -7.34331 | -49.13702 | 2024-10-25 04:14:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d0e1963-ca91-3a5a-9668-daa538aa3d32 | -7.33906 | -49.13638 | 2024-10-25 04:14:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 72182993-4169-30cf-9b04-7d1e3c5838fb | -7.33837 | -49.14036 | 2024-10-25 04:14:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b77b1fca-0b1c-39c0-bf50-4db2464d8f1c | -7.33412 | -49.13971 | 2024-10-25 04:14:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f5dcbc3-5a80-3e74-af48-106672281ba5 | -7.26731 | -49.83851 | 2024-10-25 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92a33dcb-df8a-3df9-8f11-c85ca9416ca1 | -7.11142 | -49.16963 | 2024-10-25 04:14:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d52fc087-6b9b-3a11-a633-c329bc33068f | -7.10716 | -49.16893 | 2024-10-25 04:14:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26d60f89-2e1d-367d-ba87-19386a6386ee | -7.10645 | -49.173 | 2024-10-25 04:14:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8afc09f3-3186-3a2e-bab0-944abe538b02 | -7.10304 | -49.17242 | 2024-10-25 04:14:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d492238-fcf0-39c8-949f-1417da0275fd | -7.10219 | -49.1723 | 2024-10-25 04:14:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbb02b82-317c-3ba8-a3d2-2c803059816a | -7.03137 | -49.28465 | 2024-10-25 04:14:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dacff067-8544-3227-88a0-1750f4e5961f | -6.66633 | -49.463 | 2024-10-25 04:14:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f81fcc1e-eb0d-36a5-ba09-b1d92bc2e3ff | -2.11111 | -49.27304 | 2024-10-25 04:14:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3ed2e911-9147-362a-9bdc-5177d668c99d | -2.10645 | -49.2723 | 2024-10-25 04:14:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 183dab83-b4bc-3e23-bbea-e72231c8c827 | -1.17669 | -49.08774 | 2024-10-25 04:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf6fc850-d211-30ed-8f17-da1703a2a9b8 | -1.1759 | -49.09263 | 2024-10-25 04:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1251b779-7c65-326c-8288-559ad9fc4866 | -1.17203 | -49.08702 | 2024-10-25 04:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a3155b9-290f-367b-ae98-c47669e1ca83 | -1.16736 | -49.08629 | 2024-10-25 04:14:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9538d7d5-339b-329f-b93a-adb96b1005bc | -3.23421 | -49.1186 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f13b3d0-48a8-380e-aee0-a178e85fb886 | -3.23045 | -49.11327 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae135449-2ab2-3ea0-bc8e-adaa48faf008 | -3.22969 | -49.11785 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7b39144-4ef4-3cb5-aff8-0fdd9b157462 | -3.22064 | -49.11642 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d997e806-5e1a-3839-9f38-8f4ece772b8f | -3.21611 | -49.11571 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e16d2d7e-a440-37e1-abbe-48b9d2a45ac1 | -2.81615 | -49.25398 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d3b583a6-4a61-36d6-aa7b-5d0e669f5cc0 | -2.81538 | -49.25874 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c0a67727-552f-3737-9837-a6f3b45752ac | -2.81155 | -49.25325 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 59682023-0610-3358-8540-1681e81a5b84 | -2.8085 | -49.24304 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 211eae2c-1381-393e-8ae0-96e27623e0c4 | -2.80773 | -49.24779 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 97a22abb-7506-3e79-bd2a-0ec7e810489b | -2.80695 | -49.25253 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 169c76c0-ac87-3795-ac4f-b97748510087 | -2.80617 | -49.2573 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 840b1f5b-6b97-3d4d-91b9-4b1a718a1a2c | -2.8054 | -49.26204 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 42ebce65-4dd7-3836-be6a-3d46cf7b935c | -2.80467 | -49.23758 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bee46fd6-c4ef-3313-9c7b-1b91db0b8c7b | -2.8039 | -49.24231 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 88c1acc5-4f20-3970-99ba-226e2101e157 | -2.80313 | -49.24706 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e9d9be6f-9614-36d9-9efa-ae50ee52191a | -2.80235 | -49.25182 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bf72bbd1-aa3e-3db0-8047-855d8c7ca4f5 | -2.80157 | -49.25657 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 028e2370-48a6-360c-9891-0d457ca280ba | -2.79931 | -49.24158 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ccc41d61-1da8-3942-8211-86ebb0bcae1c | -2.79853 | -49.24631 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 716437ea-3e6d-313f-ae7c-b7935cf52367 | -2.79775 | -49.25107 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6d6409f6-bdea-3a5e-b7b3-b7eb18c7af1a | -2.79698 | -49.25581 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1a764b3a-7e67-3300-9b6c-ddbf815c3e14 | -2.78248 | -49.2292 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README32.md)
