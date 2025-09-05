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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a41ba76e-2df1-3fa2-8020-d4de30fb44a6 | -22.49192 | -52.76537 | 2025-09-05 05:01:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d96bc6b9-3111-3827-a6b8-12e40bebd1d6 | -21.95713 | -52.24962 | 2025-09-05 05:01:00 | NOAA-20 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fef20733-aed1-3ca9-9d30-2d45a13bcce7 | -23.07914 | -48.92056 | 2025-09-05 05:01:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef98a258-3555-3e33-a384-001dcf6269e5 | -21.36845 | -46.95338 | 2025-09-05 05:01:00 | NOAA-20 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaa9d5dd-cbd8-3778-9044-c60f875bc485 | -20.88813 | -54.98588 | 2025-09-05 05:01:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a496665-d713-37ed-9035-caf6fd3670e0 | -21.79819 | -46.80144 | 2025-09-05 05:01:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 946a8804-d515-3938-85b8-b7b05750bc11 | -23.44046 | -47.04338 | 2025-09-05 05:01:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ebaf73d1-f754-37ed-ab5d-2657c2321f82 | -21.36737 | -46.95015 | 2025-09-05 05:01:00 | NOAA-20 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81fdbc0d-a97e-3e79-be1f-42518a05a698 | -20.85945 | -54.98571 | 2025-09-05 05:01:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efa58498-2b6e-337b-a6ab-1b97a5cef383 | -23.08071 | -48.92154 | 2025-09-05 05:01:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bbac061-546f-3423-80ef-81e010469ad1 | -20.45702 | -54.51654 | 2025-09-05 05:01:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6014cc23-143c-321d-8a2e-935e65ddf762 | -20.88871 | -54.98179 | 2025-09-05 05:01:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 329b1ce1-954b-3684-946b-5927658e508b | -22.65851 | -46.81792 | 2025-09-05 05:01:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7611c71a-4259-3e0d-b039-05e4dc7530ec | -22.66888 | -46.8226 | 2025-09-05 05:01:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e0a1c850-f2c0-36f8-a501-8aee7997272f | -21.02275 | -47.67601 | 2025-09-05 05:01:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| eef8f58d-c1a3-3504-bb93-644c44c64c7f | -22.51599 | -47.09306 | 2025-09-05 05:01:00 | NOAA-20 | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3dd13210-7a7f-3fb9-b922-86fc33d74d17 | -21.95761 | -52.24572 | 2025-09-05 05:01:00 | NOAA-20 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f699f6b5-302c-3e9e-81fb-c2594aa6bfee | -22.9242 | -46.57742 | 2025-09-05 05:01:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a0b5b9f-b0d1-3e67-b4ad-2173e54519cd | -21.02202 | -47.6835 | 2025-09-05 05:01:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5ec34321-cc39-317d-856a-36e6d9dbbd53 | -23.08102 | -48.91827 | 2025-09-05 05:01:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a502e5c-f62f-346d-a4d1-fd327c4529db | -24.37893 | -50.68892 | 2025-09-05 05:01:00 | NOAA-20 | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6497e097-dfc9-38cc-95c1-250a0bd6cdd0 | -21.02238 | -47.67979 | 2025-09-05 05:01:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f72a2fa2-6972-3b7e-bbc7-dea5b10fe715 | -22.92242 | -49.60908 | 2025-09-05 05:01:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 52318196-e18c-3858-8d74-9cbc8ea45a09 | -22.51638 | -47.08897 | 2025-09-05 05:01:00 | NOAA-20 | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ee1f4b3-0c58-36b1-818b-95dc2ca44821 | -21.79851 | -46.79602 | 2025-09-05 05:01:00 | NOAA-20 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cec3b37f-79dc-3812-92fd-21d6703f417a | -22.65756 | -46.81638 | 2025-09-05 05:01:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a6bf1f65-4c60-3056-b597-c5275f9bec03 | -23.12728 | -45.7621 | 2025-09-05 05:01:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c72ce686-e7cf-3ce6-91be-62bac9bc9364 | -23.35963 | -46.32478 | 2025-09-05 05:01:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 26eeef6e-79f5-3b73-8ffe-64fdd805b1c6 | -23.12686 | -45.76736 | 2025-09-05 05:01:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 84699c06-c875-3318-a001-fc711c75542e | -21.36307 | -46.94874 | 2025-09-05 05:01:00 | NOAA-20 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7d4d3bc-bb9b-33e6-8eb6-69753a38f67f | -21.36163 | -46.9495 | 2025-09-05 05:01:00 | NOAA-20 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06e996ac-725a-30fa-a6c7-444abfeddca1 | -21.01732 | -47.67505 | 2025-09-05 05:01:00 | NOAA-20 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70ec3daf-5cda-3076-bc7d-b803cdbaca9c | -22.46188 | -49.40403 | 2025-09-05 05:01:00 | NOAA-20 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 843235ea-7032-31b1-a3b2-fd66f449c465 | -21.36699 | -46.95406 | 2025-09-05 05:01:00 | NOAA-20 | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b465de46-2338-3cb8-adc5-ce85eda71305 | -20.89222 | -54.98238 | 2025-09-05 05:01:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6a49b46-3b3d-34fa-95b6-6d8cd1242fb3 | -22.51694 | -47.08906 | 2025-09-05 05:01:00 | NOAA-20 | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eed32978-50d5-3921-8592-6bca42bb3b21 | -22.65815 | -46.82195 | 2025-09-05 05:01:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d3c15565-3424-3ca0-8367-76ba8b196101 | -22.27637 | -49.56855 | 2025-09-05 05:01:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 846b1e1e-4251-305c-9135-7e7c6232a126 | -22.50802 | -47.69909 | 2025-09-05 05:01:00 | NOAA-20 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8f6e7fe0-2235-3156-960d-7f265f1d207a | -22.92126 | -49.60808 | 2025-09-05 05:01:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| e048665e-a20f-39d9-a2d7-8666d7917348 | -12.9668 | -54.791 | 2025-09-05 05:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 186ad4ff-8b59-3955-960e-c81569582726 | -12.9856 | -54.8096 | 2025-09-05 05:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| a96a85ea-dec3-3157-b7bc-9a5d1e52eeff | -12.9853 | -54.8301 | 2025-09-05 05:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 0c3633cd-93e2-32f8-b002-53ee14e48979 | -12.967 | -54.7705 | 2025-09-05 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| ac471b91-f912-313a-97d0-85def846c5eb | -12.9477 | -54.793 | 2025-09-05 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7e201acb-fc12-3e15-930c-19f0e479ae7c | -12.9668 | -54.791 | 2025-09-05 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 8fb0504a-862a-3b9a-886d-266901a37787 | -12.9856 | -54.8096 | 2025-09-05 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 30760118-f11c-3b23-8dd0-85cf4dffd2fa | -12.9859 | -54.7891 | 2025-09-05 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 7d067d8c-b253-3e86-9914-60cfa33e830e | -12.9668 | -54.791 | 2025-09-05 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 69306734-3e81-309b-9f14-a9cd10817ddd | -12.9856 | -54.8096 | 2025-09-05 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 1ebbb2ea-e4df-3579-bbb3-0a08ae19f497 | -12.9665 | -54.8116 | 2025-09-05 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| ac7995e8-39e1-3cdf-a7c8-b5bdaaef02f7 | -13.0044 | -54.8282 | 2025-09-05 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8ac43367-ad8c-3320-9757-8f80f8f1e75c | -12.9477 | -54.793 | 2025-09-05 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| bd422608-0f63-356f-a3c0-fa17ac1368a9 | -12.9665 | -54.8116 | 2025-09-05 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 86f3703d-7c10-3a4e-ab3b-d0d6c1d1a9e5 | -12.9856 | -54.8096 | 2025-09-05 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| f11150b1-e57d-3f6d-8194-b661b870645d | -12.9668 | -54.791 | 2025-09-05 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| d8a11db1-d14c-354c-9952-a7a267a1d777 | -12.9859 | -54.7891 | 2025-09-05 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7892442c-0976-35a0-87fd-c7ed38014b3f | -12.9668 | -54.791 | 2025-09-05 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| af48ca1f-3ebf-3326-9a7b-afac6d4851f2 | -12.9856 | -54.8096 | 2025-09-05 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 620e065e-e5ad-353f-9573-6817ea6dabb1 | -13.0044 | -54.8282 | 2025-09-05 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| ec954515-806d-38b9-a659-b90377a0b8d4 | -12.9665 | -54.8116 | 2025-09-05 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| b5b7c81a-eaa0-3428-bad6-e8293cb4c070 | -12.9477 | -54.793 | 2025-09-05 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| d9dcb25e-2227-3af2-988a-c49f7df7dad1 | -12.9477 | -54.793 | 2025-09-05 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 00550b3a-4f4c-3576-b659-20301c58ff7c | -12.9668 | -54.791 | 2025-09-05 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 216.7 |
| 403e9737-e6a2-3a03-ad94-d4472520f7c4 | -12.9859 | -54.7891 | 2025-09-05 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| b5172790-7d81-3bda-885d-11676282b981 | -12.9856 | -54.8096 | 2025-09-05 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 5cc24088-3f6c-32d8-8318-387cc72464ba | -12.9665 | -54.8116 | 2025-09-05 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 0d1043a7-ae81-3493-8509-cc17e7acdc68 | -13.0044 | -54.8282 | 2025-09-05 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 60359e81-fb34-3bc5-8b7e-05c58e522848 | -9.2102 | -57.0918 | 2025-09-05 06:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 8f655a81-c8d7-3e0e-8428-9d7b4c47b770 | -12.9856 | -54.8096 | 2025-09-05 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 5026431a-d3e3-3a50-8bf0-30df7c002ccb | -12.9477 | -54.793 | 2025-09-05 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 9a9fa21c-ec9c-37a8-af5e-36a9e4f0cc76 | -12.9665 | -54.8116 | 2025-09-05 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 7378485b-ea64-349a-b100-8b1b8365af38 | -12.9859 | -54.7891 | 2025-09-05 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 03660fcf-ffd3-3237-b81b-83c6b385eff2 | -12.9668 | -54.791 | 2025-09-05 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 164.7 |
| e6fe9243-b45e-3709-bde9-ae084eea44c1 | -13.0044 | -54.8282 | 2025-09-05 06:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 3b350097-1073-3c2e-a48d-06b4c3922f44 | -9.06968 | -71.96285 | 2025-09-05 06:16:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb535162-2401-3378-88f5-bfb98c46c1eb | -8.03207 | -71.25665 | 2025-09-05 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7db5ff31-74e0-35ca-b621-af9a22d1601d | -8.65737 | -68.77332 | 2025-09-05 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d10807cb-c00c-3fc7-a901-cec54dd5d2a7 | -8.66594 | -68.74227 | 2025-09-05 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b661392-c669-39dc-8167-ce6d58e1fdfa | -8.88247 | -69.34319 | 2025-09-05 06:16:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8e1232d-b817-3ec2-bbb9-4f65c9a9581c | -6.89045 | -71.511 | 2025-09-05 06:16:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55ced4f5-a223-3ea1-a4f6-b1f2a3d72561 | -8.6614 | -68.74521 | 2025-09-05 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a592df1-8863-344e-9827-e985ed9b61d0 | -7.57754 | -69.89431 | 2025-09-05 06:16:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00134b5b-a3e7-3b08-b0ed-20d0addcf5b0 | -8.85741 | -71.0378 | 2025-09-05 06:16:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9df67bdc-ebf4-3a56-8587-d4bce3b63f73 | -7.80612 | -73.00644 | 2025-09-05 06:16:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 503697e9-d811-3097-93c4-94a9ecdbf989 | -8.37452 | -70.85032 | 2025-09-05 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b03d1523-0dfe-3db7-89fb-63741572dcd0 | -7.99469 | -71.00793 | 2025-09-05 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5db8b624-2187-3c2c-9578-926b14e8bbb9 | -8.35599 | -70.30674 | 2025-09-05 06:16:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0eec7eb4-dbda-3134-9fd7-07407f6de5d7 | -9.32717 | -68.68829 | 2025-09-05 06:16:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 910b1a4d-063b-3605-b42a-69b5c5e78d65 | -8.6629 | -68.76339 | 2025-09-05 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc277935-81e1-33ee-a199-f9f5fd113662 | -9.23046 | -71.89534 | 2025-09-05 06:16:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d47800fb-3b61-3995-bf54-3aaea50f3d82 | -8.66341 | -68.75988 | 2025-09-05 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ccb71b85-166f-3ce2-a1c8-5ce060b353cb | -8.75946 | -69.33805 | 2025-09-05 06:16:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ecfc84e-2280-3d5c-96e0-e25016570dee | -9.0347 | -72.37127 | 2025-09-05 06:16:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1df92a4a-8ba8-3c52-94c1-91868998c3b5 | -8.05204 | -71.05689 | 2025-09-05 06:16:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59b6cd26-1cb3-30f1-ada0-f34ac5153b7b | -6.77443 | -63.13265 | 2025-09-05 06:16:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0185b9eb-cdb7-30da-8ed0-7418c1745270 | -10.24895 | -61.78332 | 2025-09-05 06:16:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 616ca3a0-4c40-31b8-bca8-576d86ce55d9 | -7.57384 | -69.89375 | 2025-09-05 06:16:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06224e86-86cb-3871-9598-f8b67d82896b | -8.6624 | -68.76688 | 2025-09-05 06:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c18e6f6-39d5-3a44-97eb-fe50b875f975 | -8.75863 | -69.34126 | 2025-09-05 06:16:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README60.md)
