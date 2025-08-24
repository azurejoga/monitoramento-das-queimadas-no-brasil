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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 406c8d9d-0854-373f-8003-1dc3286aa1c1 | -20.3594 | -51.7023 | 2025-08-24 08:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 27def5b1-8935-383e-9a36-5ac0f3a065da | -9.1535 | -59.4834 | 2025-08-24 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 50fffb21-1bc9-3fe5-a1ca-55b0cd38dc85 | -9.1536 | -59.464 | 2025-08-24 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| c956c344-41e9-35cf-98a2-915dc465bdc3 | -20.3599 | -51.68 | 2025-08-24 08:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 9a87d68c-5ea0-3a4d-85dc-6fbf8e8d440a | -9.1536 | -59.464 | 2025-08-24 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0fa1ae87-24a6-3f8d-ba85-a99e774b6b25 | -20.3599 | -51.68 | 2025-08-24 08:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 83.2 |
| bd05c6ef-93d1-35d5-8985-af6534e276b2 | -9.1535 | -59.4834 | 2025-08-24 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c3df932e-7465-3c87-8855-14c824a7c1c4 | -21.0607 | -49.0283 | 2025-08-24 08:40:00 | GOES-19 | CATIGUÁ | SÃO PAULO | Brasil | 3511201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.6 |
| 1b1f2f53-dc2c-3f25-872d-38d006a2a1c1 | -9.1535 | -59.4834 | 2025-08-24 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 2a08899a-c061-3b0d-aa0c-4f65e69dec62 | -9.1536 | -59.464 | 2025-08-24 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 42de09d8-ca11-35cf-b086-92dea37d5d83 | -20.3594 | -51.7023 | 2025-08-24 08:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 87ca369b-5f1f-3117-aa66-570da0581869 | -20.3599 | -51.68 | 2025-08-24 08:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b5e398c8-5834-3dc3-9847-b28ef4c99382 | -20.3594 | -51.7023 | 2025-08-24 09:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 186d9d46-c4b7-3770-bf60-5c241d63900d | -9.1536 | -59.464 | 2025-08-24 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 53bd6769-2f46-3e13-abca-ac114803dab8 | -20.3599 | -51.68 | 2025-08-24 09:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 686b5778-eb61-3a6b-b1d7-266ad3f93efe | -9.1536 | -59.464 | 2025-08-24 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f9371ad0-4c14-3594-a9a6-2233c333c965 | -9.1535 | -59.4834 | 2025-08-24 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| df4e5332-aa2f-30ea-a361-138e26e52b94 | -9.8204 | -46.4608 | 2025-08-24 10:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 9bfc5c8c-e15c-3c6a-ad57-d46ed161fc11 | -8.2147 | -45.0978 | 2025-08-24 11:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 57b64143-b74e-393d-99a5-5cdb7bccc25c | -8.2144 | -45.1207 | 2025-08-24 11:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 8f385bfe-0adf-3860-85c9-5f281eb8808a | -8.2336 | -45.0959 | 2025-08-24 11:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 32a8ef0a-6847-3b30-891c-fc7304c35281 | -11.6112 | -46.2337 | 2025-08-24 11:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 781484ac-dbfb-3e41-97a0-f032b4aa345b | -8.21665 | -45.12705 | 2025-08-24 11:34:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 62176a21-3938-384a-8cbe-1ed18297757c | -5.25357 | -36.70312 | 2025-08-24 11:34:00 | TERRA_M-M | PENDÊNCIAS | RIO GRANDE DO NORTE | Brasil | 2409902 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 95232089-d19b-3a31-8205-d5c03187747b | -8.22844 | -45.09046 | 2025-08-24 11:34:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 07ae2daa-50b7-3553-8a18-265182fd465a | -8.22204 | -45.09544 | 2025-08-24 11:34:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 221.5 |
| 5c1e33cc-9ff9-32f8-976e-4ac5888284a9 | -8.22323 | -45.1225 | 2025-08-24 11:34:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 639379a4-ef51-34a5-8d2c-03876f06879b | -8.05684 | -44.98867 | 2025-08-24 11:34:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| ea5d2b7c-2842-3dc0-9002-d57b3720f8d3 | -6.95696 | -35.19395 | 2025-08-24 11:34:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 2ae5cbf9-02c4-3f87-b1ab-63401a25d93f | -10.4705 | -46.89927 | 2025-08-24 11:36:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| d56550b1-a640-3e1e-a31f-fdf4911c978d | -14.77703 | -45.38502 | 2025-08-24 11:36:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 5149f1ab-5eac-318a-bc5b-a4859448a0de | -14.77426 | -45.37849 | 2025-08-24 11:36:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| a54f2278-8f6a-319e-a6e3-768ffe12579f | -12.99144 | -45.22116 | 2025-08-24 11:36:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| acae18cb-dc43-3bee-b153-7465ba0779b7 | -11.28355 | -42.01839 | 2025-08-24 11:36:00 | TERRA_M-M | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 68091085-4d5f-3091-9f31-6d6c820de524 | -11.28091 | -42.03494 | 2025-08-24 11:36:00 | TERRA_M-M | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 34.5 |
| 8a5189a1-92cd-3099-a8fb-dd67f37f4943 | -16.18222 | -43.63346 | 2025-08-24 11:36:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 40.1 |
| d39cc172-88db-384a-8ce5-e5a82ce88c3e | -10.45319 | -46.89646 | 2025-08-24 11:36:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| bb30d2ba-789a-3d7e-8ce0-f43043d23ef9 | -10.81525 | -46.41922 | 2025-08-24 11:36:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| f88992c2-fdc8-3184-8c9c-224ed6622570 | -11.27456 | -44.96842 | 2025-08-24 11:36:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| cc433ab2-2644-3f9c-b14f-1746b9e880d2 | -14.12709 | -42.11268 | 2025-08-24 11:36:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| fe25db03-c002-3b26-97f0-c7cecf2b24c2 | -10.46908 | -46.89352 | 2025-08-24 11:36:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 8800df68-7e76-304d-a448-f393505f4198 | -10.81073 | -46.41082 | 2025-08-24 11:36:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| e8a34cca-d41c-3179-9b59-801d86faf8af | -16.18632 | -43.64022 | 2025-08-24 11:36:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 60f4ec2e-a717-3f23-8a28-258eeed72f1b | -13.04139 | -45.2153 | 2025-08-24 11:36:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 1aac845d-dc79-328a-ae6f-08a8066b3db4 | -13.04077 | -45.20789 | 2025-08-24 11:36:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 0ac3b377-1d86-37e7-b4b0-c02d1bf48256 | -11.29048 | -42.02583 | 2025-08-24 11:36:00 | TERRA_M-M | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| cfae58fa-9a40-30c9-b5c1-317ef2f0ba55 | -13.03605 | -45.235 | 2025-08-24 11:36:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 19e70d80-846e-3dc6-8e39-378a2e5552bd | -12.99237 | -45.22699 | 2025-08-24 11:36:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 7ae7e9c4-dff4-35b5-a1bb-b7f51a7f933b | -22.59282 | -43.30502 | 2025-08-24 11:38:00 | TERRA_M-M | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| ce9f1c7d-24dc-3ff4-bb15-47a25038b4d4 | -17.55277 | -44.2543 | 2025-08-24 11:38:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 047333cf-db57-3ae7-ae31-9e31bedfb21d | -17.55849 | -44.24139 | 2025-08-24 11:38:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c10593c8-a6aa-3fec-bd50-803ca3af3388 | -19.93107 | -40.38655 | 2025-08-24 11:38:00 | TERRA_M-M | FUNDÃO | ESPÍRITO SANTO | Brasil | 3202207 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 39e5953c-9dbc-36c5-9217-c6ffccd768f6 | -21.34122 | -41.00748 | 2025-08-24 11:38:00 | TERRA_M-M | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 22.4 |
| 90b8365d-2294-3635-a1e0-d1a183735b5d | -20.39051 | -45.59423 | 2025-08-24 11:38:00 | TERRA_M-M | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a59d0dfe-26ed-3875-9941-99fe8f8b18da | -21.34285 | -40.99694 | 2025-08-24 11:38:00 | TERRA_M-M | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 4a6278b4-74e9-3aa9-ab65-1bbae24071ea | -22.45173 | -42.30273 | 2025-08-24 11:38:00 | TERRA_M-M | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 7b5cb163-72f7-36ea-8f98-29d89dbefc5e | -17.60999 | -44.31025 | 2025-08-24 11:38:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c813d505-b8c0-342c-a1eb-551b168b7d1a | -21.86024 | -41.33009 | 2025-08-24 11:38:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 67503fa6-d84a-3fa7-82fd-022b69f1f9e3 | -19.63059 | -43.18481 | 2025-08-24 11:38:00 | TERRA_M-M | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| e0078283-740b-36bf-9cc4-0d170cd5f70f | -11.6112 | -46.2337 | 2025-08-24 11:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 0173fe07-e6a2-30d7-832a-757d1fba2bd4 | -23.33175 | -47.84316 | 2025-08-24 11:40:00 | TERRA_M-M | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.2 |
| 8d6704c0-9fdc-377c-9b44-9703bfe3a789 | -11.5251 | -50.4898 | 2025-08-24 11:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 597a6315-ecf0-330b-9fb5-c0f70ada128c | -11.6112 | -46.2337 | 2025-08-24 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| a1d63cb4-42d2-3845-afb7-fbf15cf443f2 | -8.2336 | -45.0959 | 2025-08-24 12:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 2b5547f2-6c07-3de8-9cc5-4abadc96f5bb | -11.6112 | -46.2337 | 2025-08-24 12:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| ad4ae67d-c789-330d-aae5-0509ea7fef33 | -21.4096 | -47.5973 | 2025-08-24 12:00:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 55862a9b-0999-34eb-b3c3-ec8f9e287868 | -11.5251 | -50.4898 | 2025-08-24 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 2ff39803-75d6-31a0-86e5-177aadcdb2a0 | -21.4089 | -47.621 | 2025-08-24 12:00:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 96d30b79-2023-337b-a43a-070eda599574 | -10.478 | -46.8534 | 2025-08-24 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 5ca1c2d7-47f3-389e-bff4-09c00fdf8a5f | -11.6112 | -46.2337 | 2025-08-24 12:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 0805cd12-02a9-3056-8a35-17fa5bba00f5 | -11.5251 | -50.4898 | 2025-08-24 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 1c5e1176-8ee7-3491-906c-883b70021138 | -10.4777 | -46.8758 | 2025-08-24 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 509f621c-1d65-37ac-b22d-526880ad3a27 | -5.663 | -45.136 | 2025-08-24 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 5ca5a68a-9520-3c20-a940-d42768cea57d | -10.6012 | -50.1629 | 2025-08-24 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e3eae4aa-891e-3df8-afbf-a01dc761d677 | -10.4584 | -46.9005 | 2025-08-24 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 67bba8f9-9b61-341e-a86e-66ef137c386b | -10.8269 | -46.4058 | 2025-08-24 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ba393487-eb86-36e0-8df6-edca97f9a0f2 | -11.6112 | -46.2337 | 2025-08-24 12:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 60ef66b2-b218-3e6e-a121-631c26913ee4 | -8.0652 | -44.9989 | 2025-08-24 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 33f6babc-c5af-3e5b-a854-3bd7803e0b94 | -5.663 | -45.136 | 2025-08-24 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| fe7952f4-5172-3fc5-a7f6-4db2d41b6541 | -11.5251 | -50.4898 | 2025-08-24 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| e826a150-0896-31ff-a19b-b4e8c6a75231 | -11.5251 | -50.4898 | 2025-08-24 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 61660b49-d982-381f-bad8-43d741a6a935 | -11.6112 | -46.2337 | 2025-08-24 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| bb8e399c-980c-3d12-9a49-46588dce5606 | -10.8075 | -46.4308 | 2025-08-24 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| c57826f6-63e3-3795-a6cf-973ad6dfea64 | -10.4777 | -46.8758 | 2025-08-24 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f1c1a844-d42a-37ad-baf2-3ce76956ac05 | -10.8078 | -46.4083 | 2025-08-24 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 1c693153-8dda-3bea-900e-7cf7b1b5fb40 | -5.678 | -41.3987 | 2025-08-24 12:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| 75ed4086-127f-3188-a568-6b10e4304860 | -5.663 | -45.136 | 2025-08-24 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| e5c6596b-f00b-33cb-a041-2e8ab7be1a1c | -5.6628 | -45.1586 | 2025-08-24 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| f7b7e62a-e486-363f-96be-e498d6554ea5 | -14.7722 | -45.3822 | 2025-08-24 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b16698ee-833c-3a9f-808f-36775a2c63c3 | -10.4584 | -46.9005 | 2025-08-24 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 4d0df1fc-18dd-3e01-8e3c-aeafdbe56b7f | -10.478 | -46.8534 | 2025-08-24 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c54e36f9-74ce-3202-af0d-1d6b758a27b7 | -11.6112 | -46.2337 | 2025-08-24 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 2d1b5d02-0e88-3422-bf8a-67cd4a0f06e7 | -5.678 | -41.3987 | 2025-08-24 12:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| d9326f5d-0da2-3eb0-be26-d7a779e5edae | -10.8075 | -46.4308 | 2025-08-24 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 1241972a-0640-3211-8de6-d0e08e3f93e0 | -13.0501 | -45.2158 | 2025-08-24 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c7d8612c-55ae-3e2f-ba4b-6eb34a3ca937 | -8.0685 | -49.6524 | 2025-08-24 12:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 9c9d0ed2-e037-3777-857f-3b40e831fa90 | -5.6628 | -45.1586 | 2025-08-24 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| cbc9ffae-40ed-3b18-87b5-9e2605d17259 | -11.5251 | -50.4898 | 2025-08-24 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a3d356d5-cd5b-3944-9b2a-ac62008f19bf | -10.4777 | -46.8758 | 2025-08-24 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 9f309bb9-5e22-3c71-b87c-af0ae6bb6582 | -8.2336 | -45.0959 | 2025-08-24 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |


[Clique aqui para ver as próximas entradas](README91.md)
