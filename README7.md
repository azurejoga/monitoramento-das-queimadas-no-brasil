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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b875099a-792f-34eb-af20-877f4792546a | -9.1733 | -60.8302 | 2025-07-17 01:09:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f920fad0-5ebe-338b-a86a-85cb8bb7bde3 | -23.056101 | -51.499802 | 2025-07-17 01:09:00 | METOP-B | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 725bd732-e419-3924-8c54-4afe97b4374f | -12.5011 | -57.7663 | 2025-07-17 01:09:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cea8b0f0-0178-3135-a2a7-1f344e41d7c9 | -10.0535 | -59.088402 | 2025-07-17 01:09:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35dfc047-378d-3726-a6f7-a4a3a8089fc2 | -9.1049 | -64.141502 | 2025-07-17 01:09:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ab503cd1-795e-3919-9d70-5f70d3c24254 | -12.5031 | -57.774899 | 2025-07-17 01:09:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be18f3ec-0842-3caf-969d-b9ec6d15b339 | -10.669 | -56.531799 | 2025-07-17 01:09:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31e494d0-937b-3d86-b9d7-4c43d9b6a778 | -11.9423 | -63.831402 | 2025-07-17 01:09:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d2f3da92-4c35-30a5-958b-2ce0ad7d344f | -10.0553 | -59.096298 | 2025-07-17 01:09:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b7bbd04-cd42-36ce-9e72-f84796ff07db | -9.0224 | -61.211498 | 2025-07-17 01:09:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7405e0f7-c0aa-303b-9e3c-c7d9e96ab276 | -12.4914 | -57.7687 | 2025-07-17 01:09:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31d37031-aede-3f0e-9d48-4ffe29ae84b4 | -9.4615 | -63.138901 | 2025-07-17 01:09:00 | METOP-B | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c0811a62-fa85-30a7-a8c9-9e6510a27d3e | -9.1749 | -60.837299 | 2025-07-17 01:09:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a996a1ab-4b2f-3815-bacc-575f6fb2d75f | -11.9504 | -63.8214 | 2025-07-17 01:09:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4639284a-1b75-3b70-8f2d-4c1956b7ba5a | -11.9406 | -63.823601 | 2025-07-17 01:09:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93eee6a8-2b28-3c0c-923d-d75a1f0235b4 | -6.7006 | -44.3247 | 2025-07-17 01:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 8331caa9-d27f-362d-993a-81e2af4aa98c | -5.6565 | -43.7393 | 2025-07-17 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| df00e926-9764-316b-b2f7-27858fdaee68 | -5.6569 | -43.6929 | 2025-07-17 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| a35f03e9-20c9-310d-8cc0-1bd504303bff | -9.2449 | -48.5546 | 2025-07-17 01:10:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| c660252c-a3e0-3de8-a9c9-2d626125da18 | -5.6754 | -43.7147 | 2025-07-17 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| d8cb2def-e4dc-3b13-82fd-65cd29d43a70 | -11.1121 | -48.875 | 2025-07-17 01:10:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 6fdf8345-5d61-3d42-b73d-012962ff109a | -8.1072 | -43.1646 | 2025-07-17 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 87c3f521-b340-39d0-a072-d89774c84897 | -9.2447 | -48.5764 | 2025-07-17 01:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 661288ba-5eeb-31d1-9223-da296f4fc4b2 | -8.1075 | -43.1411 | 2025-07-17 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 168.3 |
| 68a78438-e678-3006-89fb-efda47f30e4f | -3.3957 | -47.5003 | 2025-07-17 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 573a909f-3a6e-3a0b-bc43-f58dfc2703d0 | -6.7382 | -44.3215 | 2025-07-17 01:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 286181bf-f56b-304b-8dda-7a118b6f7901 | -3.3958 | -47.4785 | 2025-07-17 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| c6e041e6-5e5d-3158-9ac2-496f7f2d5eda | -6.7194 | -44.3231 | 2025-07-17 01:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| c41037e6-ea4e-3de2-8987-b2cf3786fa20 | -5.6567 | -43.7161 | 2025-07-17 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 371.5 |
| f3df3d80-7554-38fb-bf9f-c74ee65b284d | -3.3772 | -47.4792 | 2025-07-17 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 09a64392-4920-395a-b69c-679ebb2c4e38 | -6.7194 | -44.3231 | 2025-07-17 01:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| a981495f-0dfd-3e52-bddb-6e7ef436d5cb | -8.1072 | -43.1646 | 2025-07-17 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 1ee6ea49-bb7c-3233-bd92-64b0711f44da | -3.3772 | -47.4792 | 2025-07-17 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| e5a3a8ad-b1ea-35c7-9480-974f1040068b | -3.3958 | -47.4785 | 2025-07-17 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 60688a29-165f-310c-9833-fa0dd52ef71a | -5.6567 | -43.7161 | 2025-07-17 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 447.3 |
| 0937d188-ad38-3946-9085-b95b700b67b7 | -3.3957 | -47.5003 | 2025-07-17 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 972e2c60-86b2-3865-a54e-05dd68006ee2 | -5.6754 | -43.7147 | 2025-07-17 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 5287e5a6-fedd-3b95-afe8-014f00e69d15 | -6.7382 | -44.3215 | 2025-07-17 01:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| aef49e79-5c00-3097-a2bc-ca4abf260f22 | -11.1121 | -48.875 | 2025-07-17 01:20:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| da7c481c-51e9-3b35-b515-d2bf07000d45 | -5.6565 | -43.7393 | 2025-07-17 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| e5db4bf3-51a9-3455-a1e2-6a0fda6503e4 | -9.2447 | -48.5764 | 2025-07-17 01:20:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| ede592a2-6e62-36ac-b62f-147392a8e4d3 | -5.6569 | -43.6929 | 2025-07-17 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c741d9d9-1504-3a2a-b4ea-fa4a3d1d270d | -8.1075 | -43.1411 | 2025-07-17 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 183.3 |
| 1349714f-21a6-3ccc-9cc3-8492ed410de2 | -9.2449 | -48.5546 | 2025-07-17 01:20:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 3344b2ec-121c-3bef-8089-cb875964c238 | -3.3958 | -47.4785 | 2025-07-17 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 835c7adf-19ec-3941-8ac1-9d00719f6a60 | -3.3772 | -47.4792 | 2025-07-17 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 679a1bd3-0e78-358d-8ab7-5911c80fcf9c | -9.2447 | -48.5764 | 2025-07-17 01:30:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0ccbb7a5-7b96-3794-8921-fb861da616f4 | -6.7382 | -44.3215 | 2025-07-17 01:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| edc99aa8-ab8f-3bac-a600-f48d16f6dc1a | -6.7194 | -44.3231 | 2025-07-17 01:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| aacccfae-9649-38a5-8475-51d3b4d63a07 | -5.6754 | -43.7147 | 2025-07-17 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 28b273fe-eca3-3adc-b4a2-3c4282b7115a | -5.6565 | -43.7393 | 2025-07-17 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a50f379f-1ca8-3e63-8010-7abc782507d3 | -5.6569 | -43.6929 | 2025-07-17 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 296b9c3d-6d19-35d2-8d10-e67bd837ff87 | -3.3957 | -47.5003 | 2025-07-17 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 2e336c39-5aee-3eef-8af1-1a792e9b4cfc | -5.6567 | -43.7161 | 2025-07-17 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 430.2 |
| 22691198-ce17-345b-93f7-b96f524b8979 | -8.1075 | -43.1411 | 2025-07-17 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.6 |
| b54d5ab3-fc38-333d-b431-a051382a4098 | -9.2449 | -48.5546 | 2025-07-17 01:30:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 03778fed-b210-3433-8b8e-fe569ecc4c1b | -11.1121 | -48.875 | 2025-07-17 01:30:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| b62a2180-3e7f-3d5e-969f-f9eb2ef1f146 | -8.0886 | -43.1431 | 2025-07-17 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 3114a4a4-8ef8-3ac4-b26d-60e59ce13fbe | -12.427 | -50.0387 | 2025-07-17 01:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| a4e1a139-c7cd-3806-a95c-eded1e495dde | -5.6569 | -43.6929 | 2025-07-17 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 8c03d1b4-7eb0-306f-8856-7cbd7f8ed297 | -5.6754 | -43.7147 | 2025-07-17 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 228.9 |
| b4ca8493-6b03-331d-9daf-e7af5d44b790 | -5.6752 | -43.7379 | 2025-07-17 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 95b320d8-d5b0-3b8b-aad5-50b876df7a86 | -9.2449 | -48.5546 | 2025-07-17 01:40:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 89a08260-e34d-3d3b-8567-5ab7d528a1be | -5.6565 | -43.7393 | 2025-07-17 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 00f50c2f-ef9e-3476-98d6-a9b49b5a2a57 | -9.2447 | -48.5764 | 2025-07-17 01:40:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 7dd6577d-2926-3050-b5e4-90aea8f45f7e | -3.3772 | -47.4792 | 2025-07-17 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| d0236a80-827e-3376-aedd-873f842d9cb0 | -6.7194 | -44.3231 | 2025-07-17 01:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| a6de8f6d-aa40-368b-b18f-19afd6222f27 | -6.6118 | -45.6967 | 2025-07-17 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 98060a05-84ec-3f6a-9ee1-e0a07f36d9fe | -5.6756 | -43.6915 | 2025-07-17 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 9ab2edb9-3fc9-3ee4-84f3-3b9f4593db51 | -3.3958 | -47.4785 | 2025-07-17 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 0932b26e-855d-385d-a7e7-8ed864c35baa | -8.1075 | -43.1411 | 2025-07-17 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 7477560e-9dc4-3ea6-bab4-19eaa251ea90 | -5.6567 | -43.7161 | 2025-07-17 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 312.2 |
| 7a4a30a4-f613-355c-8bb4-149025da5a22 | -8.1072 | -43.1646 | 2025-07-17 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 8d14f00c-ba1c-3a09-85fc-f8a4df040470 | -3.3772 | -47.4792 | 2025-07-17 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| cfa3af5b-bf89-3252-8a01-f7265f3e9db3 | -5.6565 | -43.7393 | 2025-07-17 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| fe9b4905-78c1-3271-8cf9-55ff5ddf3ea0 | -3.3958 | -47.4785 | 2025-07-17 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| fd72a24f-331d-3bee-9ea8-c14dc1609955 | -8.1075 | -43.1411 | 2025-07-17 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.8 |
| 907a27df-fe15-3dd6-837e-c23ef8729823 | -12.4202 | -50.4702 | 2025-07-17 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 7164b4df-7795-3afb-aab2-e439a763d0df | -5.6567 | -43.7161 | 2025-07-17 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 477.9 |
| 74663aff-20bf-35c6-b2bd-005888cdcb66 | -12.4198 | -50.4917 | 2025-07-17 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 947c440e-f179-3d2f-92b7-63de01aa70b8 | -6.7382 | -44.3215 | 2025-07-17 01:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| acbc9fe8-f820-3231-ab44-79e107177f4f | -6.7194 | -44.3231 | 2025-07-17 01:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 2a892381-1bd7-3097-b767-8164d2f0f705 | -5.6569 | -43.6929 | 2025-07-17 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 484a808b-24ed-3f02-b5a1-7cf78f4e9ffd | -5.6754 | -43.7147 | 2025-07-17 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| cdc223c3-67aa-3953-9337-c86e891410bb | -9.2449 | -48.5546 | 2025-07-17 01:50:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 230b4148-0156-3a5e-974e-4b15cb841319 | -12.4202 | -50.4702 | 2025-07-17 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 59d746c2-62e3-305a-a6fd-a9a9cd69849d | -5.6756 | -43.6915 | 2025-07-17 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 7c4a65f2-c8f1-3227-97f0-1a7db39501b3 | -5.6565 | -43.7393 | 2025-07-17 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 1d6b5668-4713-3fdb-8f34-ce12e3d3b70d | -5.6567 | -43.7161 | 2025-07-17 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 372.2 |
| 5e65ab40-0bc6-34b8-a04a-61ca4797594d | -9.2449 | -48.5546 | 2025-07-17 02:00:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 5e6ea10a-4356-3ce0-8248-745369a436bf | -3.3958 | -47.4785 | 2025-07-17 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 1add9348-4a95-392a-8ff1-13bc9063a0f8 | -6.7194 | -44.3231 | 2025-07-17 02:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 8d07e337-f3dc-34ae-8e1e-c1fb13884b46 | -12.4198 | -50.4917 | 2025-07-17 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 5c66ead0-097a-3fab-b2c1-f7ab51cc238a | -8.1075 | -43.1411 | 2025-07-17 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| c81e089c-c3b2-3da6-8a6a-f20e1770c301 | -5.6752 | -43.7379 | 2025-07-17 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 5aebac1f-60e5-3419-a9a0-6fe07c29886b | -5.6569 | -43.6929 | 2025-07-17 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 9f659d52-8e16-3eb4-b6ef-cb41519f3c3e | -5.6754 | -43.7147 | 2025-07-17 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 210.2 |
| 9694a23a-118f-363c-9f13-d85c720a3ce9 | -3.3957 | -47.5003 | 2025-07-17 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| d3b5e6da-3005-385e-aea7-8a650f1885bd | -3.3772 | -47.4792 | 2025-07-17 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 886dd710-f81a-3a7f-a5b5-e18a0b02506c | -2.1708 | -62.0098 | 2025-07-17 02:00:00 | METOP-C | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
