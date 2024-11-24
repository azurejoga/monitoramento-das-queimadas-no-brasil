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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba060ee2-152b-3c53-9196-4001eba1fe9d | -3.70574 | -54.54188 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 014ee414-8730-3956-acaa-089cafbe53c4 | -3.79079 | -47.49207 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be00242e-6f1d-313b-882a-d4b0ece92b6d | -2.381 | -49.84828 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 559c59e1-0aa2-3ff7-9b3e-c79db31eb9c0 | -3.09835 | -54.29282 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9a7e87c-5c1a-307c-9f1c-53baa397596a | -2.71319 | -46.28728 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8de37180-6db7-3be3-9039-a84284ec43f3 | -1.82007 | -46.38742 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7142a43e-9dac-3991-ad95-a452dc85df19 | -3.25242 | -42.02278 | 2024-11-24 04:53:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1450225b-033f-33d2-bdc5-e3773b1bb3e8 | -2.76142 | -54.07264 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afe1a9fc-b0d5-3a88-a385-16c6458c0ed6 | -3.19793 | -54.32816 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c550622-ee84-3674-98d4-b2c9100f44ad | -11.5097 | -48.1268 | 2024-11-24 04:53:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7652ecaa-5d35-352b-ba40-9d1fad11d9aa | -1.42766 | -53.37925 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 09bfcfd3-9180-3f88-9a13-57b6f1c49c16 | -1.27107 | -52.68864 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c0b480e7-96d7-3cbd-b980-31346e0ba232 | -2.76368 | -54.08064 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c354b454-2b0e-375f-ac81-ab010727754b | -1.77634 | -53.61577 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02e553c1-9c9e-3ae2-93bd-3b4c6a96180f | -2.63315 | -51.74366 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ecf92b0f-6341-386d-a134-d6ce42eeac42 | -3.18776 | -54.77254 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ef7cd94-ab82-3c3f-b5f8-7dfea51ab3e6 | -3.05777 | -53.22295 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4aa74459-2560-3e14-bd0d-acea6eae017d | -2.18172 | -49.15746 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0960607d-46fe-3b5c-9b03-7595ef39934c | -1.22242 | -51.73745 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10a5da4d-d6d3-396b-b05e-812f94613a9e | -3.09245 | -47.75341 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca346d25-617f-3e59-885f-9b3ed9e22edd | -3.2548 | -53.2714 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| beb2e2d4-c815-35e5-8ed2-e6d5716a13f7 | -2.16944 | -53.79629 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa388a83-45f4-35cc-99db-12a8081db2f8 | -1.42069 | -55.27561 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e52639f4-50df-3697-adb4-68a69a97fecc | -3.10331 | -53.99619 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 228c5ce0-2b66-3db8-bfa2-e254511134dd | -4.13496 | -46.70415 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbeea35f-6ba8-3421-a9b6-f3cf0d805620 | -3.98565 | -49.99266 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0118ff6-47a1-327e-933e-f4972fcfe6c8 | -3.33726 | -53.33112 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a6d7818-30bf-3a07-9696-18b91b91c494 | -1.45415 | -53.40946 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 46c6f096-de37-3ce1-a483-5c11806faf48 | -2.86866 | -45.83797 | 2024-11-24 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 22bf1ea4-6da9-38e6-8573-8e0990a010a2 | -2.69674 | -46.28117 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b37693f-5b87-3fe0-bbf7-7161e22eeb30 | -1.2472 | -51.62193 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 553ae79c-a12b-3a4e-9762-397954758480 | -3.83754 | -52.41805 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f371bc62-e535-3c0a-a28a-ae16c8dd4106 | -2.28844 | -50.58777 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14989b1a-f604-39e0-8819-f744d7097230 | -2.1011 | -50.85579 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a48e55c8-118a-34c0-a91b-ea64e036e747 | -4.21433 | -50.40418 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| acad5b5f-f650-3319-8ef3-deb225bf7395 | 0.05142 | -51.72414 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6d254a3-e0c5-317a-aa49-09f457ebc692 | -4.09274 | -54.75777 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7b1ea25f-f8bf-330a-96df-cee0c13b7c97 | -2.70198 | -48.66642 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49978058-51fc-3864-9ccb-3886ae5e9bb7 | -0.95968 | -51.78379 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62484052-b49b-386a-827e-5af7241419af | -3.51404 | -51.63377 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef4a89b2-8774-3636-ac1d-a4cf286d154a | -2.57595 | -51.88952 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8675c6ae-c4fb-35e3-8652-078cbb9a8940 | -2.38376 | -46.43594 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 756d7825-8b3e-3e4b-ba80-d1447985a233 | -2.38889 | -53.71735 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d64c2a7c-a349-3cb3-b898-87276599a3ab | -1.01794 | -48.06947 | 2024-11-24 04:53:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37c29058-b053-3299-8947-8390a10e8313 | -1.53196 | -51.56052 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b10450f2-5244-3d22-bde2-c16e06710f4f | -2.53629 | -46.39645 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2639fe89-3ddd-3faf-bee2-97354ed1a4e1 | -2.4735 | -47.09127 | 2024-11-24 04:53:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d4bbf77a-56e3-3e9f-aaf9-9eca71d6ef28 | -1.67756 | -54.97526 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48d2d19d-193b-3dab-98fc-b4d39f9df343 | -5.54787 | -45.33343 | 2024-11-24 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4bbacc6-af22-317a-952a-7d4c0d3de59c | -1.36349 | -52.55304 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bb5beac-6227-32fe-ba94-25622bbfdce0 | -1.84045 | -46.6422 | 2024-11-24 04:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d986df27-df36-324c-9626-511fa0506c2d | -3.68114 | -52.37206 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 591c839f-e27b-329b-aee5-6ba5d75577bd | -3.48857 | -50.08274 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71fabbc2-369f-3bae-975c-5ff91537cc10 | -2.75 | -48.66945 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9db5ac6a-08b6-3f2f-9d13-a0bda25380bc | -4.08312 | -46.15221 | 2024-11-24 04:53:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f0ee7d1a-2994-34a9-9afa-b255a81b0328 | -1.74019 | -53.51297 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40b865a6-bf27-3594-aecb-7a505579b4f6 | -3.23935 | -54.24583 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 912e0476-d9b7-34dc-98df-56d80ae0ce4d | -0.87685 | -51.72479 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dffc999b-9b2e-3847-9e1e-2e436da196a0 | -1.41303 | -54.898 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f1e1ae0-7610-3439-a24c-3d2215d385d8 | -3.33815 | -54.62331 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8ee0122-a9bd-3bb1-8c97-f4afd4203cd8 | -2.45159 | -53.7005 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d8842c49-6324-3ea6-aee8-b98cd01f1e8e | -1.42293 | -46.0575 | 2024-11-24 04:53:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f40229d9-8349-3282-94a4-df00051bcd33 | -1.07838 | -53.36995 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b9fcb31-0143-31a1-bbdb-e7ff6532f917 | -3.5048 | -53.8148 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 691588f3-c882-305b-963e-e72164fe0e02 | -3.30983 | -46.67109 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a43d0e5b-8fef-3216-b888-a6ea248a133f | -1.01294 | -53.09435 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c36728cb-22dd-3c99-ad29-a3e0bafc7f33 | -2.39665 | -49.05339 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2a50d81-2d98-38c4-a1a6-a9b2799f15d0 | -15.67917 | -59.15138 | 2024-11-24 04:55:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e50683f-4192-382d-984f-78f62c08cc94 | -8.74275 | -50.41461 | 2024-11-24 04:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d447bea-00d4-3199-86fa-865711f7fc04 | -7.68979 | -42.98651 | 2024-11-24 04:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e53bbda7-36fd-3e59-b21b-1dc97d0a20df | -17.75484 | -52.4342 | 2024-11-24 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5402018-2e21-328f-813a-41144f21737c | -15.22149 | -60.3768 | 2024-11-24 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d09555fc-4692-38d3-9526-865a3944fc9d | -7.57456 | -49.40462 | 2024-11-24 04:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46fb4c6c-e72f-3a54-87fe-e8049d33b496 | -7.57828 | -49.40519 | 2024-11-24 04:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 091bf9b3-3e4d-3fb9-895a-bb57f3b35a0d | -7.6937 | -42.98524 | 2024-11-24 04:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5cb9366c-d3f3-35cf-acd3-438c9c31d984 | -7.69029 | -42.98258 | 2024-11-24 04:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ffe2cad2-b493-3d91-951e-31f0c58640dc | -7.82193 | -44.19323 | 2024-11-24 04:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cf0d9b1-4628-3c21-9042-bf61421483dd | -6.8693 | -51.98742 | 2024-11-24 04:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4d9b68c-0eb6-3fd4-abc2-50d1176681f8 | -6.86596 | -51.9869 | 2024-11-24 04:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fffab4a5-1e6b-358e-b42b-7014f1ebcce2 | -7.6908 | -42.97864 | 2024-11-24 04:55:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 40bcb202-29af-3b3a-ba67-7908537846a6 | -7.69423 | -42.98132 | 2024-11-24 04:55:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2f0f1453-036f-3cfd-b341-eb7c7aa1626c | -7.57762 | -49.4097 | 2024-11-24 04:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63b42343-b55c-3e79-b94d-1a97898a379c | -15.5839 | -59.29309 | 2024-11-24 04:55:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54a00e9f-5bf4-3166-a5a3-c20bd75ebc2c | -16.08748 | -60.08862 | 2024-11-24 04:55:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a75e10c-9345-3fba-b8cc-01b8a573cff9 | -8.74335 | -50.41051 | 2024-11-24 04:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c600b0b-228b-3ab6-9c8b-54c127060e94 | -17.75842 | -52.4347 | 2024-11-24 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78bb3fd8-1740-3e05-91d9-a2c8e7288914 | -8.05102 | -47.08928 | 2024-11-24 04:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fd3c58e-6fad-377d-bb47-54281941e300 | -7.68907 | -42.97654 | 2024-11-24 04:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 978afacb-3755-37fb-a296-f893bfe9d0d3 | -6.87263 | -51.98793 | 2024-11-24 04:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99bfe671-2c81-3761-8afe-9876069bbaae | -8.07877 | -47.08082 | 2024-11-24 04:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 332d5ae9-cc34-36ee-8230-54c353fa5c4c | -17.75783 | -52.43894 | 2024-11-24 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 437a5ceb-744e-391a-8c1e-e776bac02256 | -7.32233 | -45.4763 | 2024-11-24 04:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 557e7591-b9c4-3c93-b4a6-7c9c87dba151 | -20.32707 | -48.82011 | 2024-11-24 04:55:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1be62e68-9ca0-387d-a222-a2a0f7c5ddc8 | -7.76049 | -46.22099 | 2024-11-24 04:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5ddb4f9-243a-34de-a5c0-bc806b30062a | -7.68961 | -42.97258 | 2024-11-24 04:55:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 25396b8c-fa5b-3f0b-b990-7fd1077479ba | -7.69131 | -42.97466 | 2024-11-24 04:55:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7ec0b88b-e3f9-3a11-87e3-ee12962fe50f | -6.22414 | -55.65592 | 2024-11-24 04:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fdd4c590-f001-33ae-9b86-0deb5ffe5c70 | -7.68853 | -42.98048 | 2024-11-24 04:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3195eedd-ce7b-37df-8ff4-1d030f1e4648 | -15.67927 | -59.14988 | 2024-11-24 04:55:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b41208e-a49a-3ec6-b93c-0fffaa58e9a2 | -8.93242 | -44.24949 | 2024-11-24 04:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README67.md)
