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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 727081f2-aec9-3c18-9dda-3ac9127b1ad3 | -17.26888 | -42.32612 | 2026-09-23 04:29:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f85e384e-cc45-303d-90c7-af60ff71c0e8 | -14.73965 | -45.63761 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 772e1c86-5f12-34f7-95f1-30d8f40de563 | -17.08644 | -43.20647 | 2026-09-23 04:29:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2e696de-03b3-3fd8-9371-e268fbb97828 | -17.43515 | -42.46956 | 2026-09-23 04:29:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0ff98c7-a766-35e9-9c3f-96518e099559 | -14.96801 | -47.53542 | 2026-09-23 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| daed1609-6b8d-34af-9682-ac5e72008011 | -14.75663 | -47.15655 | 2026-09-23 04:29:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ed2c557-964a-3ff2-bf5d-7fbfd6c29be8 | -14.71797 | -45.58857 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8be1e092-6b50-3d76-818b-ac41dfc43f9e | -15.49595 | -41.55391 | 2026-09-23 04:29:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ee8afb13-87c1-318a-913b-6b606c8e4fb6 | -14.73495 | -45.64511 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94296476-b4fb-3d11-a77d-c6baf0cbe536 | -14.71326 | -45.59617 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 01d58c15-495f-37a4-a7da-199eb78d0346 | -14.70857 | -45.60369 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7820a507-97ec-3557-80b4-32fc02cc10e2 | -14.71679 | -45.59671 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a7eb72e0-00e0-3881-953e-662f7766c811 | -15.52281 | -47.34871 | 2026-09-23 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f60867f0-c8e4-3ae2-921d-b767126d921f | -14.96412 | -47.53854 | 2026-09-23 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08048af1-23b2-32f6-a55f-67b978352fd7 | -14.74488 | -45.62875 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 534f7034-1c41-3685-9171-6f884f81645b | -14.73032 | -45.60284 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6fe984a9-01b1-3fe3-9f89-6bd71f26e1c0 | -16.82391 | -41.90746 | 2026-09-23 04:29:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e9811db8-6064-33f4-9ebc-087f781aa400 | -15.49534 | -41.55114 | 2026-09-23 04:29:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 571b805a-ec5e-3ccf-a79e-7523f265d033 | -14.74719 | -45.61239 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36055260-24df-3139-8d14-2508e9607ebb | -17.16288 | -45.18101 | 2026-09-23 04:29:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec17892d-15b7-3d06-bcb1-f3f4d6e1ce49 | -16.58514 | -43.36345 | 2026-09-23 04:29:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 095891e6-2efe-3235-95cc-c1aa469096cf | -14.7663 | -48.59828 | 2026-09-23 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb4186b3-7971-3246-bd18-891f51f71b54 | -14.74014 | -45.61129 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e08d72c-e99e-3394-a45b-434653c1f6ab | -17.26306 | -44.4486 | 2026-09-23 04:29:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c098bc0e-e37e-3d4c-a168-ca1d3f20144c | -14.75328 | -47.15602 | 2026-09-23 04:29:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10cd4704-70ea-33f0-9746-9cb230292c1f | -17.7512 | -44.23478 | 2026-09-23 04:29:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec1a0b68-442d-34c5-8d1d-cc2d0c02b879 | -17.97629 | -43.98553 | 2026-09-23 04:29:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ceaf263-a05d-38d0-a953-1cc454c67160 | -14.72973 | -45.60691 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fd65071a-6afa-3bd5-8df6-1b3974666cc6 | -14.74072 | -45.60718 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4028aac7-9d2b-3962-8602-626d3d2df2e2 | -14.71385 | -45.5921 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c3cd9af5-eb21-3e58-9e01-8044659f7565 | -17.43495 | -42.46791 | 2026-09-23 04:29:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc9cd012-2864-3c71-9e36-76c4089290c6 | -14.73325 | -45.60746 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e170ffe0-604d-3348-8d44-c85b035a3267 | -15.2704 | -47.60265 | 2026-09-23 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaa21857-2317-38d1-9c1a-250c8c1fb902 | -15.25267 | -47.60719 | 2026-09-23 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8b278d9-604c-3a1a-9cb0-75aac48e1d5f | -15.24935 | -47.60665 | 2026-09-23 04:29:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc9b78ca-1ad5-348a-bb2a-0baef491ba7f | -14.96745 | -47.53905 | 2026-09-23 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd265b1d-06ad-3d94-9c26-6bbef753b819 | -17.16721 | -45.17702 | 2026-09-23 04:29:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de4f26d1-908d-3f46-a488-e723c31ac6ae | -14.71092 | -45.58744 | 2026-09-23 04:29:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a061c629-7bd0-3ae3-b820-5ede0fde4baf | -14.75048 | -47.15183 | 2026-09-23 04:29:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 657ff232-d6a3-329e-8466-63c92a4ea9b0 | -14.96523 | -47.53127 | 2026-09-23 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 630060fa-19e5-3c75-b546-0eae717cd9e5 | -8.9165 | -61.4767 | 2026-09-23 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 31d97044-8ffa-3f40-a959-c9cd85f19d70 | -8.9164 | -61.4958 | 2026-09-23 04:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 4612f087-2111-369c-b625-a1641babc6bb | -1.82683 | -55.71875 | 2026-09-23 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a6d3844-0f71-37e3-b69a-67f9e8d7b361 | 0.60907 | -55.98105 | 2026-09-23 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8c690db-360a-379f-96ad-c7c33114527a | -3.50596 | -53.2034 | 2026-09-23 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b34a09b9-d7d7-3078-9a1f-b35ad8b0d190 | -3.2357 | -53.95578 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b5b88e8-ac89-3ac1-9b0e-1627c50ddc20 | -2.59753 | -47.35122 | 2026-09-23 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7cb9bc43-998d-3c94-93f8-8b752e9d8b57 | -2.74427 | -51.54405 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce1f7b53-34bb-3a19-96b2-e0f775e854eb | -3.39158 | -50.82647 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0941d5f3-5830-3a30-9c29-0b26b772885c | -3.25239 | -53.9623 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c8c3538-842b-32b2-b4a6-fcd3a9e1fa8c | -1.21854 | -54.55126 | 2026-09-23 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88cca0c1-c6bf-3cfa-af21-a9b431899c95 | -3.45265 | -50.61362 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce7f91af-4e31-316e-9031-947ef3f2b8d3 | 4.30562 | -59.94641 | 2026-09-23 05:01:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e52fb2ee-8b15-3903-b2ef-0de7753b5ca0 | -1.14708 | -54.15718 | 2026-09-23 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64f93a08-363f-3324-aa9e-5c70ef5077f3 | -3.25299 | -53.95853 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0dd1b9d4-df5f-3a8f-88f3-5d140a6469dc | -2.29814 | -48.58201 | 2026-09-23 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45ee5c8b-a31e-3d11-8a1b-248d65047b05 | 1.44076 | -50.81492 | 2026-09-23 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50629bee-4de2-338f-a991-019fec8b9eb5 | -3.44308 | -50.60847 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4956ef18-2339-3052-a6df-ea9d20ab2b0c | -3.07528 | -54.39124 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a73640a8-a668-3921-bcfd-05f4e8df6c8b | -3.07591 | -54.38729 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12f2b585-8f7d-39bc-a495-8699363a1abe | -3.23038 | -46.94464 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f2dff1d-d9d9-3d29-aed2-17542a15bd0a | -2.59711 | -47.35368 | 2026-09-23 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d0582a44-eb5e-3af2-8d98-91527ea23548 | -1.21556 | -54.54662 | 2026-09-23 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c9b94c0-a1ad-30aa-9c8e-5f91ca122e0c | -2.94902 | -54.08178 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f8969a6-77ff-33f6-8484-977782ea4b6c | -3.50258 | -53.20286 | 2026-09-23 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bb99ff91-4d03-3283-834b-73f6b6229478 | -3.03545 | -51.00614 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| faed9931-276b-3faa-ba03-cb92a61e802f | 2.33268 | -50.76286 | 2026-09-23 05:01:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ce99ec5c-60dd-3d59-a236-a4b8d2771925 | -3.44141 | -50.66312 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b4311db-c496-3528-be34-04fbf0ce054b | -3.26289 | -54.27947 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19bca716-f38c-3743-b456-230de0c6e7d4 | 2.08786 | -50.95017 | 2026-09-23 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b80727f-5f89-3193-9f97-0eacf4491a8e | -2.96049 | -52.14117 | 2026-09-23 05:01:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 104d5b2e-87e2-362f-9140-d0f4be505362 | -2.56717 | -57.51784 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c39b423-b210-33b0-8dcd-ccc53ebb23ff | -2.76271 | -57.03028 | 2026-09-23 05:01:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6058a09-4566-3246-a2f0-96f81aceed97 | -2.95523 | -57.72907 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f046123-618f-31f7-bd72-cb9e156a4b6d | -3.06697 | -54.398 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 849b355e-45a5-31e8-b34e-ca56539c6f1d | -3.07049 | -54.39855 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c7eee27-d156-393f-ba19-5dbd462f044a | -1.82846 | -55.72071 | 2026-09-23 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d021aedb-ceae-3662-a6b1-8b39bf8b4665 | -3.43353 | -50.66921 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e939572-065b-3c39-9359-4fe6ec77c439 | -2.98669 | -50.51614 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cafe07c-f08e-3f6e-95ce-b87ac5389b84 | -3.14698 | -48.07272 | 2026-09-23 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cfaf2df6-e74c-343c-afb6-d605d415277b | -3.5522 | -49.82067 | 2026-09-23 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1894bb77-d900-370b-9ffc-c1b402655b45 | -3.22938 | -53.95098 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e1525a3-9c14-321e-8bde-5b39a72602d9 | 2.7693 | -60.26296 | 2026-09-23 05:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66b35777-c904-3476-aadb-5816c44e81dd | -3.00578 | -54.17341 | 2026-09-23 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33eb60c4-1d9e-37e1-aaf4-0107d8569c4d | -3.24727 | -53.94998 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2058a8a-62ef-347f-abae-a80162dbf5bd | -3.2351 | -53.95951 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b218b95-2b5f-3b90-b316-526af75a2ea2 | -2.9244 | -57.78214 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2ed640ed-f76d-373f-88c6-9dbccc9aee13 | -1.25614 | -54.22186 | 2026-09-23 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d74d1102-32c6-3e2d-a877-51b6033c7f6a | -2.98048 | -50.39803 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cfa7f05-28d2-38d2-9b12-3e33c9e57813 | -2.76623 | -57.0346 | 2026-09-23 05:01:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9070497-61c3-34f4-a179-27a1ad1fdfea | -3.50202 | -53.20644 | 2026-09-23 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9626086a-5e88-38d8-8223-83f54551abbe | -3.44534 | -50.61613 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b83eda62-6618-3c38-9883-98bb45d6dedb | -3.88346 | -51.95396 | 2026-09-23 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3f82ff4-08c5-381b-a1d2-a6969a8b9727 | -3.04618 | -54.41473 | 2026-09-23 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7125ee8-8b1f-327f-a5fa-8657d980a09a | -2.96918 | -50.40366 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b5a4912-5b53-3cf2-ab8d-5c8793938570 | 1.77221 | -60.23199 | 2026-09-23 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 226ae49f-0e2e-3057-a5dc-41c2f2a855a2 | -3.24321 | -53.95316 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b04be843-6f51-3765-b452-7699745d2ea7 | -3.22533 | -53.95411 | 2026-09-23 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0316c6d3-c92b-3be8-9509-0ee9799ccacf | -2.92345 | -50.42964 | 2026-09-23 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a190386-62b5-35d7-abd1-d718d07a6d39 | -2.85441 | -57.79618 | 2026-09-23 05:01:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README74.md)
