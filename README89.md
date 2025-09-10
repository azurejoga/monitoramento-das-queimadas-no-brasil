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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e7d6fa6-2886-3f29-ae10-c81c2ebe2465 | -6.88368 | -47.88873 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 70559533-fd14-3721-b320-cdfca1667ef0 | -9.45161 | -46.71672 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4601a6e2-c838-3cd4-87b3-38f30860ee47 | -11.11263 | -48.41709 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46e18dd2-29e5-3224-8e48-c1f82d64490c | -8.05896 | -52.32885 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1715ca3-aaef-3a27-afcf-4a15ddda153d | -12.02279 | -50.99288 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c7330a6d-6e15-33f9-81e9-3f191cb284bc | -9.34516 | -46.75584 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e98d7c5b-c783-3075-9757-f7f2d00411b3 | -6.68833 | -46.41596 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 009a89e8-943f-300c-8aaf-ddca8bfce908 | -6.85135 | -47.94003 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4afe9fd3-105c-3955-925c-38ba0acc1842 | -6.62241 | -44.00238 | 2025-09-10 05:04:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0731ed05-8a65-3ed6-9203-5a57c5af642e | -10.18994 | -46.81147 | 2025-09-10 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcf06420-4d1f-3a4d-9150-0fce48e2df4b | -8.09256 | -54.75579 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 467fb905-afa6-3ac3-b7bb-69ac1e86a58c | -12.01737 | -51.00057 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| ecf61362-3921-3c24-9fe9-b66ed0082251 | -5.42053 | -51.53713 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5901cee-5b99-322d-aac6-7d145288f727 | -10.7465 | -48.18397 | 2025-09-10 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbf07e65-1dd9-3377-b9a2-cd1555882ca3 | -12.83804 | -52.94631 | 2025-09-10 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98ddbcff-304c-3e90-9566-8eb759b05b3d | -10.46879 | -47.94817 | 2025-09-10 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ef16921b-ed88-34ca-b59a-eed6d9183fed | -10.5854 | -52.04557 | 2025-09-10 05:04:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00b11347-1edb-3d9c-8c80-db78f2ff1b78 | -9.00791 | -49.53617 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed9fd6b4-1fc5-35f5-91cf-88af8623d2b0 | -11.46337 | -43.63203 | 2025-09-10 05:04:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 41cd0eff-0395-3bcd-aaa5-3abbeefe8b1f | -10.72684 | -48.29288 | 2025-09-10 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ec2b8d0-e8b9-3661-9237-9846890600d9 | -9.14896 | -46.05774 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01f7fadb-2f3c-3194-8f72-a2077bfc66a7 | -8.63024 | -53.11092 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bf60a35-5bce-3a8d-86d7-5832214123c6 | -12.00343 | -50.97324 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 38.2 |
| c3e725f3-330a-38b2-9fe7-d2bfd0a7f88d | -11.14626 | -48.35775 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fedc937-20ee-34b4-92df-3cba3270eba1 | -11.20726 | -54.99379 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc0ff9a2-c774-388c-8631-4d31406ff302 | -8.15808 | -46.08945 | 2025-09-10 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85e3d355-d2c5-3918-9bc8-c69df4b4a80e | -9.69824 | -46.75616 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dade25c5-4183-32c0-94c5-80a57d0f9b2e | -6.88862 | -47.88948 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 567849bd-b5cf-3f8e-b275-262eca93744a | -9.45254 | -46.70977 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57bd24b8-2ce4-35b1-81ea-9a252b8246d7 | -12.01903 | -50.98813 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6e702c65-e915-3088-996b-17986289b6b1 | -6.64976 | -51.97574 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3175175-7d86-391e-bb61-ba51c4bb4db5 | -8.53012 | -49.13741 | 2025-09-10 05:04:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40fdc2ab-44ea-396d-aa8e-68d028f417e1 | -11.22045 | -54.99949 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fbb1970-d4e9-3c1b-b1b5-79c7ff25c8ad | -9.08446 | -47.06407 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ba23838-9693-36c3-b755-c975d614035b | -12.20477 | -53.88558 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d40556f0-f999-37a1-a79b-28e86fbff2e3 | -9.66682 | -46.64559 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 416771f6-0ba4-3803-b326-6f9e2789c333 | -9.82832 | -46.05787 | 2025-09-10 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bdf51c9-2fd4-3ca6-8f50-435a5cee7880 | -12.06171 | -51.0615 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 8dcd3e0e-5005-32c3-9fee-e6e8842c680a | -10.01035 | -48.08604 | 2025-09-10 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfa7b55b-06ee-34eb-bc7c-ecc79eae85a5 | -10.86886 | -55.71422 | 2025-09-10 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 963ac286-5582-3a51-ab70-d3af4d0b1f3e | -7.54171 | -48.21423 | 2025-09-10 05:04:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c423d3ad-a0e4-3c4d-af65-4a4c370c52ca | -8.34785 | -45.04553 | 2025-09-10 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 058ebe82-91ae-3f25-b594-a04d3a81a0c6 | -9.45115 | -46.72017 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17c7df54-b905-36dc-b4e4-2a8e43afd71b | -10.27539 | -48.81732 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c829c44a-df4d-3cce-94cf-0e220b2ee213 | -7.98207 | -46.32807 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2747339-51e4-3665-ae2e-51624ffbe545 | -9.55582 | -53.56451 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a02f8ed1-d9c8-3de6-b01c-e21fdb54a4be | -9.21539 | -50.55426 | 2025-09-10 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b329b4f-a314-34a2-babc-aebbcccdd470 | -9.10163 | -46.97816 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5372b3c4-5a8c-3c7e-b788-e0394eb2ebc5 | -9.44738 | -46.70604 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 42f3befe-685c-3a80-81e8-8393cb24f45d | -11.93853 | -51.0784 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c8416cf-8bec-3bfc-87bd-3a5855aba09a | -10.30467 | -48.82121 | 2025-09-10 05:04:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2b5d35a-4bf6-3cbe-933c-14ef39f22bb9 | -7.7778 | -50.77153 | 2025-09-10 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57385e1d-192f-30e9-8340-99e9b8e27298 | -13.00249 | -48.03997 | 2025-09-10 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b614fb29-a8b9-3bd7-b730-4c8f2c38e1ca | -12.0522 | -51.03495 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0c4f1443-4cc8-3e56-8460-01b00a713be8 | -9.05801 | -49.81936 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2294167a-8883-3a75-903d-830a13e2f5cf | -5.80422 | -51.736 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cc4e25c-a3ac-320d-8fb7-45c910ac4a60 | -8.16098 | -46.09223 | 2025-09-10 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcfcdeb3-1c9c-3abd-8390-0b17550a444b | -10.56217 | -51.49876 | 2025-09-10 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1192f824-90bd-3e40-aae6-491f8b981ddc | -8.07347 | -52.38605 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f4b3d6c-b81f-389a-aac2-17be15dddd97 | -9.911 | -49.87103 | 2025-09-10 05:04:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c89bd0b8-b64a-386c-a228-e6c4e42ffd35 | -9.01246 | -49.53682 | 2025-09-10 05:04:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3738bfa-1ff1-3414-b87b-b6d8f59ec04c | -5.7981 | -51.67425 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81e5d4f4-6b13-306b-93d6-f1429e94ade2 | -10.84025 | -47.75254 | 2025-09-10 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5d4d09e-137f-31a6-93b4-b7ff0d1f0515 | -10.58145 | -52.04506 | 2025-09-10 05:04:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cba6241-9739-3db1-8d23-cce1433abe5b | -9.09204 | -46.96722 | 2025-09-10 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3811e48e-d186-3339-9500-71a1a9f84414 | -9.75657 | -45.40262 | 2025-09-10 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 87d1a558-25d0-33e4-91ce-1349ed53f350 | -12.18428 | -53.87382 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc57a4c7-2b4f-3102-a709-846adfe6140a | -6.68882 | -46.41248 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc3fcece-c55b-3789-9b9d-997a996492c6 | -7.66535 | -50.26743 | 2025-09-10 05:04:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a5f211e-08e1-358e-98ea-04e5fd53b25b | -12.06917 | -51.0709 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 704dace2-d0e3-3203-bc5c-71e391bb2558 | -11.83304 | -46.74751 | 2025-09-10 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9770d6b9-8cfd-3f55-8c6f-6a09520c05b6 | -12.035 | -51.03256 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4dffb1f-3390-3891-be5c-11a771c23a4b | -6.85782 | -47.92958 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fad79a58-087e-3e6a-b555-3bfab3ac3e81 | -9.52021 | -54.65009 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5b4ef11-6713-34c9-bf62-3da3c9db6049 | -7.48799 | -54.95205 | 2025-09-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38fe0323-56d4-379b-822b-b44df408f377 | -8.85348 | -47.26969 | 2025-09-10 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 297802e1-4b78-3bda-a987-d4d3af6366f5 | -12.41301 | -47.50417 | 2025-09-10 05:04:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fcf48d6-9fbc-3fbf-9282-c09212b25880 | -8.52007 | -45.70878 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d877ffd-111b-3c62-8e47-63b30471bf3a | -10.02877 | -51.66089 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9a59b9b-4548-3ab9-8104-e9d69dbfe07c | -6.87872 | -47.88814 | 2025-09-10 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8fbfa2c5-3da2-3d1a-a8f0-5b92a69f082a | -8.78284 | -44.40471 | 2025-09-10 05:04:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10150878-bff2-3bc4-98c8-ad8534698ee1 | -12.02112 | -51.00531 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 9b0ecb5c-2fc5-30a4-bd12-71d4da877386 | -10.01573 | -51.66628 | 2025-09-10 05:04:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6732cbd-889b-3bb3-95fe-7b610e9bde3e | -9.71237 | -48.09359 | 2025-09-10 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4550608b-0e0b-3e20-a1e7-c3dccacd9296 | -9.05747 | -45.76529 | 2025-09-10 05:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10246f2a-fe71-39d4-9198-7fd258b7c908 | -5.66441 | -51.63829 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a2ecff7-4e8a-3529-a75d-bcac25a86131 | -11.11301 | -48.45374 | 2025-09-10 05:04:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 760b4e88-7053-32ea-9179-213a6b267593 | -11.11925 | -45.11379 | 2025-09-10 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb1bf9cc-bd73-3572-adf1-2b0558ecbf79 | -9.79448 | -61.52496 | 2025-09-10 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e18b9e9-8662-3f52-947b-4a65b738aafc | -9.52135 | -54.64265 | 2025-09-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 716e180c-6e72-3dd0-b009-af6ead211878 | -11.22101 | -54.99574 | 2025-09-10 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f4e9ef0-f872-3ae8-9bd5-2dc5915cd4da | -8.46924 | -47.30153 | 2025-09-10 05:04:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1779934b-f72d-3715-ae15-726f00afc1ba | -12.19691 | -53.88874 | 2025-09-10 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2caab00d-4bdd-3582-a113-975cde55c5a6 | -8.08622 | -52.35159 | 2025-09-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22785127-c8d3-3fe4-a60b-137b6978de6c | -7.25156 | -44.45821 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb389c1a-0f6e-30e3-b64f-31a0fa9e7dda | -10.18767 | -49.58522 | 2025-09-10 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75ef96a2-004b-3e60-a986-ed9ea32142dc | -10.18701 | -49.59007 | 2025-09-10 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dc00e8e-23a3-35e9-ae8b-a474bd0bd996 | -8.25875 | -49.92466 | 2025-09-10 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0883ad05-2744-3e45-8580-c4ee9adf130a | -9.3158 | -46.72242 | 2025-09-10 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c9623bd-e575-34db-a7b7-6573eab3eec6 | -8.0262 | -44.50424 | 2025-09-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README90.md)
