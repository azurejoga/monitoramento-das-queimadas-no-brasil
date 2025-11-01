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
| 3a7bb2f8-7b25-3952-9411-4bf0e745cb3a | -3.2156 | -50.5795 | 2025-11-01 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 1b61ec21-cd78-37cc-9c2b-4bc8b2c7f69a | -11.3773 | -48.9307 | 2025-11-01 00:20:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 921a48fe-a9b6-32e3-8dc9-e1ac9cf399c2 | -8.2383 | -46.2481 | 2025-11-01 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| da524687-c769-3b23-897e-a479696fc80f | -3.234 | -50.5789 | 2025-11-01 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| c411c2c6-a35b-38d3-aed0-7905bdef6676 | -10.6316 | -52.1682 | 2025-11-01 00:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1aeb1049-fba0-3775-971c-4c0a96fc19a3 | -13.6468 | -44.3913 | 2025-11-01 00:20:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 741c7aff-1077-35dc-8ab5-fa70f08bf24d | -8.2195 | -46.25 | 2025-11-01 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 5808652f-6583-331b-a75c-67fe05df9b09 | -3.2156 | -50.5795 | 2025-11-01 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 3ff78323-e835-3fcd-b9f2-2fc1875e9b05 | -4.1924 | -47.6627 | 2025-11-01 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 40f65fc3-2785-3b64-ab80-db2d56904cb5 | -5.1166 | -43.3831 | 2025-11-01 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| ba96b0ec-5d28-335a-af42-87ecb97587b4 | -4.1739 | -47.6418 | 2025-11-01 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 4a759e89-954f-3b6b-a681-bb677c137672 | -8.2383 | -46.2481 | 2025-11-01 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7733238c-19df-3609-8c8d-7793684e96fd | -10.6313 | -52.1891 | 2025-11-01 00:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 3c3f63c9-3ebc-324d-b7b1-df090c6c4dee | -13.3337 | -60.7158 | 2025-11-01 00:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 1db4cae9-6957-3051-a220-f94930243999 | -11.2607 | -45.5078 | 2025-11-01 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| d5cddb55-063a-3abf-b696-ac4f578d0cbf | -11.2611 | -45.4849 | 2025-11-01 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 73e6b3a6-6f9e-38fc-b2e4-21c31562f2fd | -3.234 | -50.5999 | 2025-11-01 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| ad3ee223-b6ba-36a9-9b07-c3d7848710ef | -8.2195 | -46.25 | 2025-11-01 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 2cef97a1-913e-3528-9d68-302e9ca358e5 | -3.234 | -50.5789 | 2025-11-01 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 186.9 |
| 89cfedba-c729-329e-b636-06419ead8d03 | -10.6316 | -52.1682 | 2025-11-01 00:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 2d6f3db0-205c-359e-95cd-5a8c3f5390de | -10.6502 | -52.1873 | 2025-11-01 00:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 99a4dba7-33b9-340e-8316-86f60b2fbf0c | -10.1226 | -36.3067 | 2025-11-01 00:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.9 |
| ab1d5644-1dd0-352a-a1ac-df6950c4a246 | -4.1925 | -47.6409 | 2025-11-01 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 7c9d5b2d-6291-3e1f-b6f8-934df36bafd4 | -6.9481 | -49.6312 | 2025-11-01 00:30:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 500c6d3c-8429-307f-a256-ef41a38c392d | -4.5047 | -54.9247 | 2025-11-01 00:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 912a6bec-b140-3f00-93f6-38a3e902752e | -10.6504 | -52.1664 | 2025-11-01 00:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| fc9b31bd-010e-3361-8f58-b653c5505ed5 | -6.9295 | -49.6325 | 2025-11-01 00:30:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| f4edd5c6-188f-32cd-a4fd-9aa99e537395 | -8.2383 | -46.2481 | 2025-11-01 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b2552e59-9735-3351-b5d4-05b89ccc6683 | -10.6316 | -52.1682 | 2025-11-01 00:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 38b45dda-d830-3a24-b413-10cd5c13b53e | -11.2607 | -45.5078 | 2025-11-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| ce4aae0b-f00c-380d-b4ac-d441f088cb2d | -10.6502 | -52.1873 | 2025-11-01 00:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 5a4baa0b-c5fd-3417-8313-3e2f6fd823d2 | -13.6468 | -44.3913 | 2025-11-01 00:40:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 32910194-29f1-3755-866e-f37e0d76736d | -6.9481 | -49.6312 | 2025-11-01 00:40:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8917cae8-8ecb-3978-8354-b8b072d6932a | -3.234 | -50.5999 | 2025-11-01 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| d6d80a80-cd94-3fb2-9915-15cadd9ce673 | -11.2611 | -45.4849 | 2025-11-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f481f817-649e-3fd7-8008-4784ffe18d0d | -4.1738 | -47.6636 | 2025-11-01 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ce0ff688-c191-3cae-91e7-bf6944f4ef5d | -4.1739 | -47.6418 | 2025-11-01 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ec83b1dd-0ab1-34d1-95bf-28f2deaa35cd | -10.6313 | -52.1891 | 2025-11-01 00:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| d3e684b9-b607-304a-8030-3618c76447b0 | -3.234 | -50.5789 | 2025-11-01 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 169.0 |
| de1a89df-003d-309a-b61a-3c31e7fb717f | -3.2156 | -50.5795 | 2025-11-01 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| a474df8e-4f20-3bfb-96b0-aa60b18f9e27 | -8.2195 | -46.25 | 2025-11-01 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| b0fee5c2-caeb-36a5-9370-ccb389b864ee | -4.1739 | -47.6418 | 2025-11-01 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 68c4ddc2-3131-3922-8d8b-e92d700217bc | -11.7433 | -47.4741 | 2025-11-01 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 12ddbab9-d608-3ba0-aceb-3bb2758e088b | -10.6313 | -52.1891 | 2025-11-01 00:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 69f1e8e9-a0a7-3b9b-9c58-8b2f8d8d98ae | -4.1738 | -47.6636 | 2025-11-01 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d4d75574-9301-3d55-8503-128bac4f4675 | -5.1164 | -43.4063 | 2025-11-01 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 10154e93-e95c-3a1d-8db9-1e94e2f81ca0 | -10.6316 | -52.1682 | 2025-11-01 00:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5890288c-6549-33c9-b294-a178d56867c2 | -5.1166 | -43.3831 | 2025-11-01 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 161.8 |
| fa6c7b13-ba7c-39bb-9bcf-3f14437bc75f | -10.6502 | -52.1873 | 2025-11-01 00:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 0b5552c2-3672-3aa7-b382-56386a8a69c1 | -3.234 | -50.5789 | 2025-11-01 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 1522b362-e166-32ed-936b-91891834ad76 | -3.2155 | -50.6004 | 2025-11-01 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bb5d7299-d971-337e-b19e-a2d2ac1d5433 | -8.2383 | -46.2481 | 2025-11-01 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| a35f0615-7410-37ce-bc4f-031fee954df1 | -11.2607 | -45.5078 | 2025-11-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 1f212c91-59bd-316f-8fe5-d331f8849734 | -11.3773 | -48.9307 | 2025-11-01 00:50:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a807faeb-6d22-3b6f-8a69-af28d6f0ae22 | -10.6124 | -52.1909 | 2025-11-01 00:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 221429cf-0568-3d3c-b5fe-f31b7567d3f1 | -8.2195 | -46.25 | 2025-11-01 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| bbd1b268-922e-31d6-ba58-5f30c7167245 | -3.234 | -50.5999 | 2025-11-01 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| c64c2162-9a9c-3d9c-8b15-b9e832a0da2d | -3.2156 | -50.5795 | 2025-11-01 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 011a1edc-4a5c-3831-856a-1d918f0e3b76 | -3.2156 | -50.5795 | 2025-11-01 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 0394e96c-d751-3025-a6fa-d0a905ffd5a9 | -5.1166 | -43.3831 | 2025-11-01 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 12915a8c-3348-3114-b3c9-f826e622e2a6 | -10.6502 | -52.1873 | 2025-11-01 01:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0ebdadca-69a3-3a41-b962-857d4abf52a7 | -11.2607 | -45.5078 | 2025-11-01 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3b1e7c53-48ed-39e8-8782-873b43838a93 | -10.6313 | -52.1891 | 2025-11-01 01:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 5141353a-1be4-3b20-b5dd-20899cfc0bd1 | -8.2383 | -46.2481 | 2025-11-01 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| aedfc476-4b14-314b-a984-d4d13b31fde5 | -3.234 | -50.5999 | 2025-11-01 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 82984538-9fe7-3f26-95be-428b21e5f8ae | -11.3773 | -48.9307 | 2025-11-01 01:00:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c8a25e6e-46c0-39f1-a244-6a1a5012d93a | -3.2155 | -50.6004 | 2025-11-01 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 1219b264-2884-3e8e-9267-53a85c50ab72 | -5.1354 | -43.3818 | 2025-11-01 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 31d7f632-58fc-3b02-af34-31f80ed0167d | -3.234 | -50.5789 | 2025-11-01 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 158.7 |
| d6388080-8c26-3ce1-98c3-5ede79343cd2 | -4.1738 | -47.6636 | 2025-11-01 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f11cb3e1-b755-3eb5-9822-c30cb1d31420 | -10.6124 | -52.1909 | 2025-11-01 01:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 80c63ebe-3a87-3e54-9751-e5b7c4c106ce | -10.6316 | -52.1682 | 2025-11-01 01:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 149ce3e9-3b58-3ba3-8407-526fbaf76020 | -10.6316 | -52.1682 | 2025-11-01 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f00f82f0-abde-31c0-b9cb-89a1a65652b8 | -10.9262 | -51.2985 | 2025-11-01 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| f10446e4-901e-332c-8737-49806bfcc276 | -11.3776 | -48.9088 | 2025-11-01 01:10:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 0b15ffb1-88ec-3f4a-b45f-9f45cebbe54e | -10.6124 | -52.1909 | 2025-11-01 01:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 68ab594e-9594-3599-8a33-07f2fc72f0df | -10.907 | -51.3216 | 2025-11-01 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 620e737a-d509-3402-8206-d5f956374cfc | -8.2383 | -46.2481 | 2025-11-01 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| d641dcd6-b67e-3c21-b63b-18f793df9a3d | -6.5833 | -48.7356 | 2025-11-01 01:10:00 | GOES-19 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 4b8b075c-5ef2-3e78-b2ab-cc2c4f13437f | -11.3963 | -48.9284 | 2025-11-01 01:10:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 776ceda2-db9e-318e-aeb3-11ce49e4dfc2 | -5.1354 | -43.3818 | 2025-11-01 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| a189d067-c882-3d38-8638-a027980f302b | -5.1166 | -43.3831 | 2025-11-01 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 58a88e0c-cc54-3d25-a2ad-e87bd8630d2d | -10.6313 | -52.1891 | 2025-11-01 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 50b1028e-df2a-3efe-ae91-ce515ee09a6f | -11.3773 | -48.9307 | 2025-11-01 01:10:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 107.4 |
| bd20dbcd-4441-3eb4-859f-f64314082589 | -3.2155 | -50.6004 | 2025-11-01 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 09c97899-f5ab-3d5b-94b8-ccc44dea41f3 | -10.6502 | -52.1873 | 2025-11-01 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 44111c2b-368a-37e3-bbf7-2190e832ec8b | -11.7433 | -47.4741 | 2025-11-01 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| c1b7e7c8-7370-33d9-b312-453cf2da8336 | -10.926 | -51.3196 | 2025-11-01 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 179.6 |
| 3a90ea13-8d5e-3818-a7c6-ba65f7e48c4f | -3.2156 | -50.5795 | 2025-11-01 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| f15a93ad-8699-349a-823b-2e5958ca6661 | -3.234 | -50.5789 | 2025-11-01 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| c6bad856-5894-3a7a-a035-4dc0d6f8c015 | -10.9257 | -51.3408 | 2025-11-01 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 134.5 |
| e62a9293-8a3c-3226-a914-81712ec2de44 | -3.234 | -50.5999 | 2025-11-01 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 001cb117-0d09-3f57-b193-57b1eaefa4cd | -10.0834 | -36.3406 | 2025-11-01 01:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 0a0b2a74-cbaa-320b-9592-fa293debba6f | -11.3776 | -48.9088 | 2025-11-01 01:20:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| c6ec9b44-28bf-3bf8-b135-1cc30a1f2d4d | -10.6502 | -52.1873 | 2025-11-01 01:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| c69522b7-80b1-3ad5-afc2-f0f2d5b651ce | -10.6316 | -52.1682 | 2025-11-01 01:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 74ffbc6d-35d7-346d-a2a0-d26ea94604b2 | -11.2607 | -45.5078 | 2025-11-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ffe7e339-9bac-300a-a8e4-ff97323d608c | -11.3773 | -48.9307 | 2025-11-01 01:20:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| ee8e9096-b2df-362d-b95a-880bc91f587a | -3.234 | -50.5789 | 2025-11-01 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 5b40b8ba-0ebb-3a73-95ab-3ebe66c4a69d | -10.6313 | -52.1891 | 2025-11-01 01:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |


[Clique aqui para ver as próximas entradas](README8.md)
