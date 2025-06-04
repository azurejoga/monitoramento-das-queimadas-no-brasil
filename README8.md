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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c01210e3-1304-3b46-be8f-75a6bd34035f | -13.42573 | -47.53045 | 2025-06-04 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 839e88f4-ffc4-3052-8693-2781b02aaf85 | -11.90717 | -47.4522 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6c41ed4-08fd-3402-92f5-3c42978f998e | -17.87025 | -45.54571 | 2025-06-04 04:02:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e0c7204c-f7d6-3545-9b42-81cdc87ee8ef | -11.83605 | -51.28096 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fbf2f7a-c5ed-31c4-9369-8dcdc7c5b210 | -11.8313 | -51.28725 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a15817fe-2fb5-350a-903a-5d559a3495b1 | -11.53922 | -47.31171 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5db5dd9-1b5c-38a1-bc7e-353dbd29b95f | -13.38064 | -47.44623 | 2025-06-04 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91f9a45a-90f5-31e5-b4fa-f2df8cd43f15 | -10.86811 | -49.54962 | 2025-06-04 04:02:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a75aece-dc63-37ed-af72-45e6353e963d | -10.87046 | -49.54932 | 2025-06-04 04:02:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 182c32a6-792b-3227-b6a3-cdd29113c899 | -11.56006 | -47.62115 | 2025-06-04 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c915e077-b5f6-34b5-8f1e-877edcc4e7c1 | -14.71457 | -45.10032 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 411e41be-9bb8-3481-9b14-950ea395e884 | -11.83055 | -51.29111 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 109d9eff-d0ef-33af-9d4e-58cc7511efaf | -14.71492 | -45.09317 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3eb40141-7fd3-35ce-af8f-59e223b065ac | -15.99695 | -49.71415 | 2025-06-04 04:02:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95dcf677-fe9d-35d6-a96f-ea73ea4325f9 | -11.90047 | -54.7954 | 2025-06-04 04:02:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13dfcb09-eb25-3fed-86cc-45c74053a171 | -13.02942 | -48.25542 | 2025-06-04 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3ec1fbe-3dc9-3486-a117-2f683d2c9401 | -17.36998 | -46.99368 | 2025-06-04 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d9ad16a-aa84-3be7-bb03-9d0121763189 | -10.70909 | -48.77676 | 2025-06-04 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ec9542d8-0765-3a24-b1f2-186e206479c3 | -11.56053 | -47.62266 | 2025-06-04 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9bd4d02-d861-39f3-92bb-97e721da0960 | -17.8708 | -43.75936 | 2025-06-04 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a85de976-ba8e-3823-b9db-34dc786a92b0 | -11.89341 | -47.45399 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d25ce3b-05bf-3a41-a46a-0bfbeb5a7d9a | -12.6478 | -54.12043 | 2025-06-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c83a8d3-4955-32e6-96cd-e8def08a5036 | -15.3497 | -48.02958 | 2025-06-04 04:02:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24a34d98-49bc-3aa9-973f-66570c8b9454 | -11.25105 | -49.49376 | 2025-06-04 04:02:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34267204-ab87-3a45-89ae-2b661bdecf61 | -14.01468 | -55.12942 | 2025-06-04 04:02:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d65cc395-e020-3361-9095-cc6ab3bc9e7c | -14.72252 | -45.09739 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00d2dc4f-5c03-3448-9ba7-ed58df71a5da | -12.64192 | -54.12265 | 2025-06-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c77b62a6-5226-3f3c-b039-ef2b1e5c918d | -14.68273 | -52.68741 | 2025-06-04 04:02:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c11da4ad-62be-3e66-9fa7-c356ea619603 | -12.29222 | -50.11158 | 2025-06-04 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50f940f6-8fd0-3a91-8a7a-c24e9caea9e6 | -11.83543 | -51.29597 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ce3a1a2-1430-3c46-b2e3-f367e0978323 | -11.90243 | -54.78719 | 2025-06-04 04:02:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b72ae2fd-5a23-36c5-95ea-0ded498f5721 | -12.64655 | -54.1263 | 2025-06-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17a5f425-b9b2-3b78-97f7-aeea28ccdc55 | -11.90106 | -54.79383 | 2025-06-04 04:02:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65a7af3c-e0d4-315d-9c1e-1449043ec637 | -11.57571 | -47.45932 | 2025-06-04 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76cab9f6-2030-3189-8e4f-17dd35d7226e | -11.61528 | -47.61826 | 2025-06-04 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dba42296-9687-3347-8435-9fc73ec8ca76 | -11.54784 | -47.31342 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5465c700-db8a-3192-9075-a11d41f2c474 | -11.90996 | -54.81843 | 2025-06-04 04:02:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74bb1244-3e23-306e-948f-65630c28b58a | -11.5334 | -47.31919 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5320aa81-0ed8-355c-892a-bd192bcc7b89 | -10.87319 | -49.55057 | 2025-06-04 04:02:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 001d20cf-22a4-3ac7-bb69-a140981b492e | -15.27368 | -51.48084 | 2025-06-04 04:02:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 226d8f51-76c1-3c76-98c6-3a0f1e88d48f | -11.90488 | -47.44564 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20a8b15e-98a8-329a-8a2c-60a08b66eb84 | -12.2928 | -50.10844 | 2025-06-04 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2107fb72-99bb-3bd0-b8b6-cc3d05610f22 | -14.71058 | -45.09679 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13172c60-18a7-361d-8e03-16c83d2ae832 | -12.09516 | -49.47619 | 2025-06-04 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5ff9835-7d2e-37df-b378-820c168e6748 | -12.28767 | -50.10739 | 2025-06-04 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e14e3b8-987f-35e2-ac3c-328eba45ea15 | -11.61088 | -47.6174 | 2025-06-04 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51aff53a-87f4-3c6d-9d86-fcb0bcb997ba | -15.91958 | -49.25653 | 2025-06-04 04:02:00 | NOAA-20 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 544a6faf-d5c1-360d-bd96-41adbc5396cd | -14.71132 | -45.09248 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45de6fef-21e2-3deb-8a54-b356da982e6d | -14.62837 | -47.73865 | 2025-06-04 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63eed4dc-d008-3e88-8ccf-40764e6f2807 | -16.31342 | -49.91581 | 2025-06-04 04:02:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6efb2f4a-7b97-35a9-8ae4-6b658a090a59 | -15.2722 | -51.47661 | 2025-06-04 04:02:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e9a5502-1d28-3144-b7e8-5ad1f43e4e22 | -11.83859 | -51.29736 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d446f702-1c99-324a-954d-2e7c062a79f0 | -19.71637 | -40.35234 | 2025-06-04 04:02:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c00e64a4-fa45-3477-8f93-56d0c516f0e1 | -11.83937 | -51.29349 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a45b52d-105e-3727-8ace-b48eebedf6cc | -11.40679 | -52.94717 | 2025-06-04 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47e7cd7e-7900-3973-8ebc-e10d80a58f64 | -14.70771 | -45.0918 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2a39518-75d1-31f7-976e-85e540455fdf | -13.09847 | -52.02256 | 2025-06-04 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 646f4abc-38fc-3886-ac90-d46535ad4299 | -14.71346 | -45.10182 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14a2e009-b36b-3cb1-8850-93e5aaf2156d | -11.56131 | -47.61821 | 2025-06-04 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ae7cc5a-cfd9-3462-8454-0c76f8c1b4a3 | -12.31788 | -47.26221 | 2025-06-04 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 126f2168-4b2b-3da9-acea-e5bd8398a373 | -11.25161 | -49.4908 | 2025-06-04 04:02:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ea8c9ea-f4e4-3e60-8e85-2f6f6d2f5068 | -14.71892 | -45.0967 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5fe8c1dc-4f60-3e9c-954c-a311c5d13202 | -13.42505 | -47.53408 | 2025-06-04 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69153d5e-9fbb-3121-84a7-11a82c15b477 | -10.70808 | -48.78215 | 2025-06-04 04:02:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5e815e49-d701-3ff4-a7c8-f0cac08a75e2 | -11.57642 | -47.45532 | 2025-06-04 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4125ccab-087a-38cb-8a8b-979ac39b34ef | -11.84176 | -51.29319 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 43deb998-d5f4-345a-afef-2d44f171d544 | -11.90207 | -47.45567 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60cbc447-b5b3-3639-a8dc-ed9e75aa3060 | -12.27516 | -44.59108 | 2025-06-04 04:02:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9d069b6-b25b-37fc-9023-a1326be55bc2 | -14.71817 | -45.10102 | 2025-06-04 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bfc19664-d148-3c86-9aaf-c4a734ddbf98 | -14.81234 | -48.45819 | 2025-06-04 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3bc13c9-62f4-3637-a37a-d6060ff7cbf0 | -12.31935 | -47.25403 | 2025-06-04 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 736dfd0b-b0d0-386a-971a-f13a8a1ad29d | -11.7889 | -46.38287 | 2025-06-04 04:02:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dac13efb-600e-378f-80bc-fe21e4ef8978 | -17.77885 | -42.80933 | 2025-06-04 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2d47835-033f-3901-9512-7944f7514f03 | -14.02684 | -55.13858 | 2025-06-04 04:02:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 748fe26b-0675-3bfb-b9a6-6f61a0a457f2 | -10.49517 | -53.65379 | 2025-06-04 04:02:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4b0c1cda-7991-3c2f-a7a5-1ae479977c06 | -12.64842 | -54.12421 | 2025-06-04 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c0e7b66-4790-3bf7-bc91-4e4247c16392 | -15.26547 | -51.48242 | 2025-06-04 04:02:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c973a55c-8d51-3a7b-bcb6-9e108945c943 | -11.57693 | -47.6287 | 2025-06-04 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a47dd647-f309-315c-b708-1a22e4c7899c | -17.78216 | -42.8099 | 2025-06-04 04:02:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16edc33d-085e-3520-b37a-73cd68574682 | -15.91962 | -49.25566 | 2025-06-04 04:02:00 | NOAA-20 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e9b5a85-18ee-3669-bd89-def3332758cf | -11.90283 | -47.45139 | 2025-06-04 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f80475be-9f29-3f65-b1ba-ac4a1943be6a | -11.57252 | -47.62785 | 2025-06-04 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 79e5f9d8-163a-3fc0-abed-6bb726bfbf18 | -13.09874 | -52.02642 | 2025-06-04 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1611edc2-87a6-35c6-b51b-e0650c14d7fc | -12.27799 | -50.10217 | 2025-06-04 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28d00f8f-8f67-3412-bbab-c2c3ff60a969 | -16.02735 | -43.68204 | 2025-06-04 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb1a506c-93f4-357f-b7c8-f7875953a69e | -12.37749 | -54.1619 | 2025-06-04 04:02:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d40cb7bf-3a4e-396d-8527-c855980497ae | -13.09768 | -52.02657 | 2025-06-04 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc422c00-7834-304c-a041-e07b2299bf44 | -11.89361 | -54.79387 | 2025-06-04 04:02:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cf60e63-75e7-3941-805b-339883335353 | -11.40157 | -52.94077 | 2025-06-04 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e34fd3d-22ae-318a-985e-2808790fa692 | -17.38525 | -42.65725 | 2025-06-04 04:02:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32f555cc-5593-3ca4-bb90-89a1538e11f1 | -13.09304 | -52.02511 | 2025-06-04 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1bfe7fc-d905-333d-a7e3-7e68cc565864 | -15.27437 | -51.47736 | 2025-06-04 04:02:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fe20ec0-79ba-32b1-bb04-82ed2662e937 | -12.31862 | -47.25812 | 2025-06-04 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 208d05a9-437c-3d77-ae8e-41bf09cb03cf | -13.09956 | -52.02242 | 2025-06-04 04:02:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 340e523c-67c9-3697-abc7-616a796e9a99 | -11.5764 | -47.45837 | 2025-06-04 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9f2d1eb-4a9f-3965-8089-905d5803939d | -10.49127 | -53.65987 | 2025-06-04 04:02:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b886e253-73f6-317c-a46a-61f1d6eb07ef | -15.56945 | -47.85369 | 2025-06-04 04:02:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d1ddced-d09c-3bf7-94e1-3a4a1a9919e0 | -11.83529 | -51.28477 | 2025-06-04 04:02:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 27124fc9-034f-3e4e-82b2-b8e1c8a1aca6 | -23.63112 | -46.4246 | 2025-06-04 04:04:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 97b977d1-16ff-372c-97c9-0634b695a9ca | -22.17858 | -42.46921 | 2025-06-04 04:04:00 | NOAA-20 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |


[Clique aqui para ver as próximas entradas](README9.md)
