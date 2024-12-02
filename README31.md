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
| 57e66a51-497b-3e24-9394-3d628e6389c6 | -2.20015 | -53.77796 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 579d3265-0105-35dd-b0f2-531f5e383126 | -2.67973 | -46.62086 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 043665be-e151-3b4f-874d-d00418277d86 | -2.55261 | -46.34747 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7746b2d2-87d0-3acd-9eda-ee50e06d2b40 | -1.02982 | -53.55587 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ab73eb1-eb55-3ab4-9bb1-1eb66fc652a3 | -3.05021 | -48.52804 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1243eeb-ec5d-3749-81aa-c47c97d297a6 | -2.75405 | -46.10649 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0b8a6ef-c5cf-300b-8b42-a7fc6782727c | 1.11574 | -55.99937 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9dc9cbf-8037-3bfd-ada6-0df0fe5a7c43 | -3.01316 | -48.00218 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4d16a0b-93f6-3dcb-b066-f50f8094795c | -2.19967 | -48.33722 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82be327c-e287-3820-9df1-f4bd3ef71041 | -1.72357 | -52.47981 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f41665a1-4b5c-3450-8ea5-13466348d860 | -2.48022 | -46.57858 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b89d94b-074a-3d9e-b41c-ae4fe4ca76e5 | -2.24088 | -46.39617 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a099ca52-d581-3148-b9fb-aa5b394414c0 | -1.07813 | -53.44964 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1dd6603-bfed-3ed4-ac5c-47d830e026f2 | -2.45366 | -52.21815 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a155f7a2-6466-3e95-ae6d-2102efb8de2e | -2.92545 | -45.83462 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d99bc210-6544-37aa-a277-50bdce56cba6 | -2.56489 | -46.3999 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b803c41-815f-34f0-aae5-e2f18a9fe42e | -2.92199 | -48.0078 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59d6b4dc-258e-332c-a6ef-25ee8487301e | -1.07208 | -53.4548 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8665738-81fe-3b2a-97d4-928c4edd5b02 | 1.21239 | -56.02262 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a129690-ffff-39be-aefc-c012e54e4689 | -2.97843 | -46.93817 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e84840b-9e87-3d41-9910-004853c95fa6 | -2.87924 | -46.79424 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b90e26a-4f08-36ba-80a2-21e8ff13aff0 | -2.09776 | -46.61424 | 2024-12-02 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bbb75b3-9e8b-3745-b67b-f200c4e4e475 | -1.80687 | -48.77134 | 2024-12-02 04:23:00 | NPP-375D | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f34026a-e498-3949-a1e8-c3aaec8894a6 | -2.68254 | -46.60309 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf7c5607-2622-3697-a536-f85ee2f2afcc | -1.465 | -53.41836 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb981f65-fe3b-3952-b539-db99cf2758b4 | -2.27255 | -53.60373 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cf464f2-2e99-341f-acf3-8e9b6d219531 | -0.20288 | -51.5443 | 2024-12-02 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa5e180c-b0ed-3677-a99b-9a71565bf929 | -1.73532 | -52.77655 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b41a4d7a-384e-30e6-9dfa-979d455cf1e9 | -0.34745 | -51.98149 | 2024-12-02 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21c5c8ac-afc8-3f33-8533-b524ecab5aeb | -2.58918 | -46.00948 | 2024-12-02 04:23:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3dce2bb-d36c-3341-93a0-91fcb4dd4e34 | -2.72754 | -46.23107 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa669d19-f4ae-3835-8288-05a025886e09 | -3.21798 | -45.76028 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 848bc6df-7266-3f10-94b4-ac94645fb8d6 | -2.6471 | -46.11837 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d46c159-5fd3-3256-8924-4723b91bdc86 | -1.47128 | -52.68102 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3710672d-ef45-3b5c-9359-b7576f35dd71 | -1.45094 | -54.52175 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9019cab5-3389-3093-8dda-481989a52a4c | -2.65322 | -46.12289 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61d0adb9-2c0f-3697-b86b-6bcd84f4bc04 | -2.19501 | -53.77714 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7afdfc1-8daf-349c-892f-5c2d802d327c | -1.27684 | -54.55246 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ec2ddfe-3361-359c-91a5-ca3ccf5b1e83 | -2.46787 | -46.54749 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31f3af80-4732-3d8d-8cab-bcf826a483e5 | -1.96372 | -48.39192 | 2024-12-02 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a9bb733-274b-3120-841b-8f8f39a1d124 | -2.68086 | -46.61375 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 92f03287-8088-3262-af24-f9862b249377 | -2.80201 | -46.82253 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a8804df-b6a4-3e9a-a871-d8abb52002b3 | -3.13428 | -45.98815 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 400a0318-dede-3e3c-a79d-4844da5da876 | -2.49652 | -47.26854 | 2024-12-02 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c83cbc9d-0625-38a9-aac4-5cde530274e6 | -1.3777 | -52.56253 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bef0bc2-38c6-3507-867b-cb0a07617f71 | -3.45823 | -46.42385 | 2024-12-02 04:23:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e792179-e75a-33c5-8107-80d2ffe3ba5d | -2.7828 | -49.21632 | 2024-12-02 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11458314-f8b2-3847-9f4e-301de2adc25e | -1.72934 | -45.60852 | 2024-12-02 04:23:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afa79a6c-fbcf-3faf-a516-be2b3aca6320 | -1.78755 | -52.74864 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd6e61c9-f154-3879-9ba2-c3a5ea01c70b | -3.05742 | -48.52918 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fe43843-7122-35d7-b67a-57ac76416dc6 | -1.68885 | -46.19123 | 2024-12-02 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4969ebc-6673-3361-9880-adf8be96de63 | -1.82203 | -45.32255 | 2024-12-02 04:23:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1c86f76-056d-3687-8716-d89f3319543b | -1.48024 | -47.34126 | 2024-12-02 04:23:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 985a2424-9b2f-3c56-afb3-9d5783621f5f | -2.95782 | -47.89759 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76bc5940-d436-36aa-8320-d9b6e1859db5 | -2.84647 | -48.09799 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b32d1c03-ed55-36cd-b2b7-6f624e52ead7 | -2.45665 | -46.57487 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0877907b-ebdd-3483-9fee-af3b2036e594 | -2.28981 | -45.74569 | 2024-12-02 04:23:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dbbc03df-9306-34d7-b054-ab9f96b59b7f | -1.39505 | -53.65589 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c96f5267-8fdb-33f2-8cf7-eedc90e8ffc9 | -2.66627 | -46.5969 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 098e992f-3425-3d74-ad2d-8b93b75e1cab | -3.11768 | -45.98861 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efbdceb5-c15b-3b1e-a742-970f7e89f820 | -2.93446 | -47.99772 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb3f4b35-348e-3a25-8835-8a94c04c9260 | -3.16858 | -46.28934 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a5515ea7-d108-3171-85d5-04e18bf746df | -2.23361 | -46.37693 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 852d3f2b-193f-3c7b-a3a1-b389b8b5916c | -3.13208 | -45.98376 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5b9c0db-c557-3870-8e3e-d56aea4977b2 | -1.82703 | -47.28883 | 2024-12-02 04:23:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11eecfd3-4cdc-3c51-8a99-c80b8bd2a4f8 | -1.43751 | -53.39552 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac4a972a-dd8a-36f9-8910-418a0e2bd3da | -2.67129 | -48.79672 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d939613-37f1-36c2-8eb5-0acf68d53ada | -1.67204 | -52.09982 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 815be83b-31db-3ce6-967d-3cbf18ca83e3 | 1.10551 | -56.01581 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a097fc9-16bb-3f76-a5fb-f14a423e24f7 | 1.13617 | -55.985 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd311ed8-ddad-3ec9-8442-b03e516a361a | -2.83027 | -48.47639 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e82e5df-fc9c-389b-9805-8051810ced9b | -2.50188 | -49.01746 | 2024-12-02 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00271488-cba4-3c3b-a91e-dba2a94e7ff3 | -2.45444 | -48.16285 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46da14ce-177c-3f05-b46c-ed40a1fc2a29 | -2.43468 | -46.67006 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af844a84-d78b-3b53-9f06-82ce0a83d315 | -1.40556 | -53.65635 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4e449014-6188-37cc-8616-4ee5c0a5323a | -2.45945 | -46.57896 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5e547a4-ae6b-3b96-85bc-45cd4fa1e645 | -2.70548 | -47.73729 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95363a3b-48c1-33b7-80b5-fa25223e118b | -2.9322 | -47.98936 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0f6f532-f853-30ae-9962-909de72375af | -1.6751 | -53.75027 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e2ab694-9b0f-3f2e-8230-6dd4cb84a701 | -1.72698 | -52.64186 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35f12e91-2481-37a9-aae1-c996f291ad50 | -2.46562 | -46.58358 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42925661-4c19-3890-b084-c71e7e78f818 | -3.19285 | -46.58073 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c867c38b-7be0-35d4-8397-df93b8bccb61 | -1.81742 | -46.64067 | 2024-12-02 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5fdd3e2-6ab3-3078-a262-7ac99db5b761 | -2.96982 | -48.04757 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9abee6d4-fadd-3a06-b765-793fbc4486e2 | -1.27079 | -54.555 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57c469b7-8197-3f72-bb3c-256e28c756c3 | -2.47853 | -46.56738 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6db6a863-918f-3dc3-a241-5c4e846fa491 | -2.51462 | -46.22969 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 898fbdac-0c81-31fc-bdd9-2ee6f42645d9 | -3.12821 | -45.98671 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a0b677b-e588-30f3-8ffd-c95122a9aee5 | -2.36966 | -46.07105 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5aa4c47c-5a3f-31b4-8be5-6a63e9be67f7 | -1.72288 | -46.24676 | 2024-12-02 04:23:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b9dd3dc-fe09-300f-87ec-b7662fef24bd | -2.47797 | -46.57093 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43a017f7-227a-37c3-8842-f9347df4b955 | -2.49709 | -47.26912 | 2024-12-02 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f232f69-b15d-363f-b3b9-39d4d0ca539f | -1.73176 | -52.64264 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fbcbbfcf-aff1-3aa2-aeb4-08a2d69b133e | -0.92812 | -47.61836 | 2024-12-02 04:23:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68ff9790-54c0-3000-a25d-d01928bd7c4a | -3.22131 | -45.7608 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6240825f-2f25-3987-91a9-0f9fad9c885d | -2.59516 | -46.57863 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e7b2239-6165-348f-97c8-3bd6b1b4fbca | -1.406 | -53.65364 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b2157aa8-da41-3192-bb74-31bcdc38ba1a | -2.66374 | -46.09957 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56c56dd8-883e-352a-b6de-fe06be06cd33 | 0.88654 | -50.95984 | 2024-12-02 04:23:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9c562cb-c799-3682-bf41-b4df13606a53 | -1.82758 | -46.22693 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
