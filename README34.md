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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 764c205a-70b4-39e5-b0db-5f1005c2f61d | -10.97516 | -45.09682 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0806e32-b73e-3f24-912f-0cb318f6d5c7 | -13.84029 | -46.23177 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d78dc985-39f3-3a14-8fab-370724aa1715 | -13.13 | -54.9164 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b48df874-9b42-33c8-9315-6b24780f8064 | -9.45525 | -60.5248 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d42f6bd1-2a14-3509-b4e2-d241e4649773 | -13.65539 | -46.97913 | 2025-09-09 04:34:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbb0c738-2307-3a5b-9972-f4bd8427249b | -14.24136 | -44.95304 | 2025-09-09 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b002703-0750-3326-b0fb-6931b043ce92 | -9.55552 | -48.67047 | 2025-09-09 04:34:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad35d5f4-83aa-3fc7-8f7b-7671e478f386 | -12.47283 | -53.83831 | 2025-09-09 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44af121d-d73b-37c9-974d-f5d737ce368c | -11.33523 | -46.54642 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa47769e-a7d8-3384-af12-26c5bcc03aac | -9.86066 | -48.85126 | 2025-09-09 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80fb1c9d-db8f-38a0-8ece-250d483c699b | -12.85118 | -52.94771 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 912462c8-2ee4-3861-b069-92578e0235a4 | -11.2147 | -55.00116 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b7022a91-1624-3dd7-9001-cfaeab40202a | -9.80367 | -53.31327 | 2025-09-09 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e71b3c2-7929-38c0-9648-af664b7e645d | -14.33775 | -47.30365 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c9e5940-8df2-3137-b09d-8a68e7fb6dab | -7.28266 | -44.56367 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 968d6230-d74d-3d89-8e87-ab9dc0c335e7 | -10.83326 | -47.75037 | 2025-09-09 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87409341-8b16-37c3-aa64-6eb46daaa61a | -8.04944 | -48.6459 | 2025-09-09 04:34:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 548b40f2-91a9-327a-b7f3-28e184f8f982 | -10.96746 | -45.11625 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 1a0fb085-eab9-3060-9fc0-48f48ef1a667 | -7.87968 | -46.25081 | 2025-09-09 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 605243c1-30ef-3a0c-9f8d-46393e523bdc | -9.9662 | -51.18657 | 2025-09-09 04:34:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f4adbd7-ae22-3731-8396-f933aed4ea8f | -13.2872 | -43.73763 | 2025-09-09 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b1e9bd4-6cf1-31b8-8db9-1d7f72e4657d | -11.30598 | -46.50121 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6e76d097-5328-32bc-ac9e-8a188cba20fb | -8.05052 | -48.63899 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c56c50f0-eaac-3905-9d31-b5afcc53f534 | -14.24229 | -44.95188 | 2025-09-09 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7f16bc1-0cba-3343-a9ca-0ce3a0b16b2d | -7.72786 | -50.34415 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b202d25-efa9-31bd-951f-53f3a4ba4dd0 | -12.40693 | -47.79522 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9807cbbe-c232-346f-a89c-1aeb0eaf22e0 | -9.50475 | -48.27681 | 2025-09-09 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85fc13fa-d8f6-39c8-83fd-bc4351eb2131 | -8.23729 | -49.54101 | 2025-09-09 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f567a8b-3fa0-3ce7-8826-2270a568e68c | -14.3521 | -47.31377 | 2025-09-09 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cade00b6-3f26-3409-a5bb-7b91bfdac985 | -12.62994 | -56.98063 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3879e505-3c83-381c-a180-8e2808565a2e | -12.62799 | -56.96462 | 2025-09-09 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96e910e4-d81d-3e2e-bb8a-7069e11501f7 | -11.23087 | -55.00839 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc4b44f5-4f16-3e6f-b97e-7c71c56428ab | -11.42663 | -43.58982 | 2025-09-09 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a654c6d-9d35-39f4-89c6-257220639e17 | -9.94688 | -60.14458 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94634ca9-cabc-3736-9a11-e0dfd52efab9 | -12.95281 | -54.7585 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2e22de8f-39d2-3466-8965-13eb7bb32221 | -7.24875 | -44.81996 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 030012dc-85e8-3257-9b4f-a03512f5532e | -14.77254 | -45.31669 | 2025-09-09 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec51fb77-2583-38ed-bfd1-570b12522477 | -6.74905 | -51.96848 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0d4aec0-05a0-35aa-a4c0-6b58d98b45f0 | -13.29433 | -51.72831 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de7084d3-d438-33e7-8e6b-5b4fba2a4b37 | -9.44028 | -60.52397 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 18dbe382-9064-36a5-bbe3-8685569ce0e7 | -13.78391 | -50.78833 | 2025-09-09 04:34:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a4e9fbd-f4ec-3fd4-b6c1-b5e9cf3640a9 | -8.48532 | -47.32498 | 2025-09-09 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 14e65569-ec37-3519-b301-e25b2cb6a9f1 | -9.44366 | -46.73666 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14e319c9-b47b-32d5-83ec-032fd4773865 | -12.93546 | -54.7855 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24693288-8e5e-3578-87e5-74456c3b6904 | -11.98363 | -51.01477 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 728436a6-db19-337a-84f8-507ba46d0827 | -10.30457 | -51.73293 | 2025-09-09 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c68d1567-e06a-3d0a-b5cd-f70ef27e19db | -8.23395 | -49.54048 | 2025-09-09 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 359cdeb7-1440-3516-9ee1-62e8618a5b44 | -12.20854 | -53.89801 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1dfcf8d9-dbc2-362c-b493-b3e2fc644ffe | -13.95203 | -48.24451 | 2025-09-09 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1db8ba00-8872-3073-b068-c2bff28e518d | -11.62939 | -52.23959 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbdee666-69c8-37b8-aba7-f93e81598bd0 | -9.44125 | -60.51904 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 33002619-ce95-3c81-8c9a-003823a87a33 | -12.85483 | -52.94833 | 2025-09-09 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9bee774-c587-331d-9067-35422a2bf40c | -12.89705 | -47.98777 | 2025-09-09 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b5fbd5e-a58c-3b84-8f9d-1792cad38007 | -10.97254 | -45.10769 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e324dced-079a-3410-a18c-2269831039d1 | -11.13587 | -46.35165 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3077a0e-f38c-36f7-8c0e-926eefb569e0 | -7.40329 | -61.62812 | 2025-09-09 04:34:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aa845f8-9a1e-3575-abc3-775a1026a6cf | -8.03261 | -47.28739 | 2025-09-09 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37d5fb7f-27e7-3856-96fa-1f23b58060e5 | -11.27909 | -46.53119 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2c73890-1a60-340e-aba4-bf4ab90a6871 | -6.61893 | -53.37843 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 114d0011-9dbc-362c-b462-8e037c15e94a | -9.01803 | -49.79137 | 2025-09-09 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecab71a0-7194-3815-99e9-9d710017e465 | -10.18114 | -46.2276 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0190048c-2a84-37c6-844f-fed463f9fb09 | -10.23985 | -46.68441 | 2025-09-09 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f48b1dd2-69e5-367e-9f29-52db47c57bfa | -11.23082 | -55.00757 | 2025-09-09 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe4cf8b5-7aea-37bb-942a-2f51d1b7a55b | -11.29558 | -46.49261 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d06a4730-cfa9-3017-a87f-cfbc38ee6a92 | -14.25959 | -47.10157 | 2025-09-09 04:34:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aeb8e0d1-71df-3ac6-b07d-aae41f892c23 | -6.40383 | -58.20557 | 2025-09-09 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5eac7b1-f0f1-3a14-b2c6-adc9f58aef6b | -13.83255 | -46.23217 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dbeeff99-2fc0-36b6-bbe7-98366c034f4c | -13.27018 | -51.76768 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3998f506-899d-3b39-a249-973d95212717 | -8.50984 | -45.71105 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aec7de86-b0af-3361-956f-48602442cce2 | -8.30534 | -46.95243 | 2025-09-09 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bde4678-ae43-38a5-b8e6-3e3e55a2130e | -11.82746 | -47.55166 | 2025-09-09 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8e5d010-267b-3599-be11-e07697456dac | -11.97805 | -51.00621 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9983b5a7-cca0-33a0-ae68-bb9e0a06b6f8 | -9.45373 | -60.5214 | 2025-09-09 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6953f4c-b42b-3d41-b1d0-78cbbf8425fe | -10.96821 | -45.11911 | 2025-09-09 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ddfaf064-2794-3e46-a635-680fe83ad660 | -11.16705 | -48.36846 | 2025-09-09 04:34:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1d40e30-5745-3eaf-8c82-8f89c441261d | -11.4776 | -49.25897 | 2025-09-09 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b07eba1-6db1-3c8a-bf42-c483342706ac | -8.48813 | -47.32901 | 2025-09-09 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9a627a29-757a-3b28-b803-15fbec768f65 | -13.81056 | -46.28142 | 2025-09-09 04:34:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c581f161-256c-3305-9409-a38d2b87cc91 | -11.79345 | -62.73745 | 2025-09-09 04:34:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1cb3074d-45ec-3e87-bb05-853c9bbe074d | -7.72336 | -45.15581 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2116cd95-69ac-3b4f-ab77-c1a2d48597ab | -7.6937 | -44.97187 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34aaae9b-5010-3778-aa5d-27d4d381b533 | -10.83589 | -47.26563 | 2025-09-09 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f64958b-8046-391e-9231-8f7d0397f99b | -11.81048 | -46.76307 | 2025-09-09 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc56340b-4ba7-3818-af09-aac74a3581c3 | -6.62429 | -53.37173 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0d4b7b2-d18b-351d-8fc8-b22e15e8b28b | -9.13713 | -45.58099 | 2025-09-09 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2576ece8-9393-3367-872f-0c3e79f507bb | -11.22393 | -59.12633 | 2025-09-09 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58869d07-99ea-32b1-9952-790ab37e09af | -7.83368 | -45.41515 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7d69f5a3-daa4-3d69-bf6d-6aecc074469e | -9.0877 | -46.98234 | 2025-09-09 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8dea0d69-21b5-3af0-b6ac-8dc2cbc63e71 | -9.50529 | -48.27333 | 2025-09-09 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e936feaf-8bd4-35a2-97bb-47b9fa93e125 | -13.79836 | -46.26273 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8ef5f133-b5a7-3dfe-8ac7-2664cc1ffc79 | -8.82093 | -47.83974 | 2025-09-09 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14f2888e-49e4-31b2-8078-5259cae03bea | -7.70269 | -45.15816 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba430c3a-9eb3-3dec-a5ba-caf1c0dd2c11 | -6.6183 | -53.38208 | 2025-09-09 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5581adf-37d4-380b-8a81-d25e3223bb3a | -12.93129 | -54.76213 | 2025-09-09 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df5a8365-1014-3051-a634-ebc570ad81ae | -13.27551 | -51.75674 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| add3d33f-6a42-3163-ac72-326c09eef1d8 | -9.29287 | -60.85706 | 2025-09-09 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3127f1e-9e12-363d-8d9c-617277ec79ed | -7.69469 | -44.71177 | 2025-09-09 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fdae668-8446-31c2-86c7-d6ff4d654f77 | -8.01184 | -45.53043 | 2025-09-09 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba8b346f-4fb8-396e-95db-7260eee07944 | -13.82034 | -46.23927 | 2025-09-09 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6c3ad57-7597-38f5-8195-418fce90a3b6 | -7.44023 | -49.26824 | 2025-09-09 04:34:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README35.md)
