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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a1cea42-ed42-3fcc-88c5-9f8bea48fbea | -8.9028 | -60.7498 | 2025-08-27 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0c5a5f93-e454-3282-a587-fd871211bd36 | -9.1719 | -59.5017 | 2025-08-27 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| b9fd5dad-081e-34df-a78a-6109a4dfd316 | -7.5673 | -47.4851 | 2025-08-27 14:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 08f10d05-0735-3610-b87c-e1d8795bea59 | -6.8875 | -44.4004 | 2025-08-27 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 997e90ce-d4fd-3c9f-b7d3-983d30386f97 | -8.9026 | -60.769 | 2025-08-27 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| e3c7a451-7ee7-3cf5-9f91-48fa1e123123 | -9.663 | -48.294 | 2025-08-27 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a82930bf-4072-3042-b46b-33e5d02a2ab1 | -12.38 | -45.0213 | 2025-08-27 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| b5c3fe12-afb9-3a08-82a2-a550881ac98a | -12.8036 | -48.1294 | 2025-08-27 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| b06d4b8f-af86-3eda-be4d-045394e1f6ee | -12.7259 | -48.1846 | 2025-08-27 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| d225d70e-ed0d-364d-9ecd-b81e3fe0976a | -11.3342 | -43.4742 | 2025-08-27 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| b48b5def-2516-35db-bf23-e40f478d01e3 | -7.8851 | -45.9004 | 2025-08-27 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 1c365a97-1582-326c-a838-d66151cf5b3b | -13.5004 | -46.8609 | 2025-08-27 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 7bc79226-9f62-3b3f-94a7-0de4d8d2a4c8 | -13.481 | -46.8639 | 2025-08-27 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e73e40e4-1e07-39ae-a94f-f7048cb74813 | -6.6759 | -58.846 | 2025-08-27 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a7759a24-cb5f-3249-98a5-2fb603e75044 | -9.1529 | -59.5609 | 2025-08-27 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d267f6dc-de9e-3e6b-8bd3-c91dd562cd32 | -7.4734 | -61.4037 | 2025-08-27 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 114.8 |
| de91953d-9338-3f37-9543-de824dcefbf8 | -8.3335 | -62.9443 | 2025-08-27 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 71892048-73a5-313f-81ed-635915545b6e | -13.4036 | -46.876 | 2025-08-27 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| f53a7e88-cf9b-3bd6-9646-009988f6f2ec | -8.4596 | -43.6645 | 2025-08-27 14:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 262.8 |
| 26784b01-4b68-3325-aa28-874c91ce639e | -13.6097 | -48.2126 | 2025-08-27 14:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 89947182-e34c-3a5a-aab3-889100909f66 | -15.6362 | -52.7393 | 2025-08-27 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ede45489-746f-39c8-8047-a0354948ca0d | -15.0756 | -48.5181 | 2025-08-27 14:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 13d3e7d8-b827-3273-8563-3f5fce88b56d | -9.209 | -59.5191 | 2025-08-27 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3eea7a66-6a17-366e-aa9d-51ea9273b735 | -11.1583 | -44.7859 | 2025-08-27 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 630.3 |
| cd021c39-b593-3cb4-9510-fd91525b1388 | -11.3338 | -43.4979 | 2025-08-27 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 257.7 |
| c4033aa0-acfd-3839-8f2b-26810d2f2f34 | -15.6168 | -52.742 | 2025-08-27 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 11826e28-22dc-35e4-810e-c71616f676d1 | -13.0674 | -46.3153 | 2025-08-27 14:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| b211e35c-7706-3284-84df-63e0e75778a3 | -6.4355 | -44.5764 | 2025-08-27 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 211.5 |
| cfb40cc9-b47d-3149-b94c-d0ed9ab5f3c4 | -6.0849 | -44.007 | 2025-08-27 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| cafe97f6-e592-31bc-b6b5-25c3135ccb43 | -12.784 | -48.1543 | 2025-08-27 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 63dd8c70-1075-315a-8818-f2dfc6688438 | -12.7263 | -48.1624 | 2025-08-27 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 22c4defe-21fd-3523-b06f-c5baff3742c1 | -8.8841 | -60.7699 | 2025-08-27 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 284.2 |
| 7a3d150d-5e5b-3a8b-8b0e-95f889d7c37a | -6.8413 | -58.9552 | 2025-08-27 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 98ac976a-e331-34a7-ac6e-6288db5dd91b | -7.6603 | -42.6698 | 2025-08-27 14:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 117.0 |
| cbb65bdd-ff8f-3625-aa6a-d2fe6017a154 | -9.0816 | -49.6068 | 2025-08-27 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 3eb443f9-72bf-3416-bc55-64fe9a9675bb | -9.5705 | -48.1505 | 2025-08-27 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 3b6c3245-43c0-323c-bca6-e7c9aca6fb1d | -8.271 | -45.1149 | 2025-08-27 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 95ab782e-49c4-3deb-8502-793de2a63285 | -15.6366 | -52.718 | 2025-08-27 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 05e3339a-3d5f-346e-b187-b3caddf8386f | -7.6414 | -42.6718 | 2025-08-27 14:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 183.3 |
| 788a5c0d-fd2a-3035-b599-fcf83782cebc | -12.804 | -48.1072 | 2025-08-27 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 4efde02b-8382-32da-a9de-e855d2a32ea4 | -6.8229 | -58.956 | 2025-08-27 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 182b82e3-6fda-359d-8f6e-5cde6c807d31 | -12.3805 | -44.9981 | 2025-08-27 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 7e176e0a-4621-346d-a716-7ea25598090b | -10.2557 | -64.4915 | 2025-08-27 14:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 42d59d69-6bb0-3c62-b22b-b5fd04060163 | -7.4636 | -59.8931 | 2025-08-27 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 07cb59f4-ed3c-3336-a8c7-7953b16bc883 | -11.7966 | -51.4169 | 2025-08-27 14:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| d7f19e88-f2f5-30ce-b622-cf417ac93543 | -9.1715 | -59.5599 | 2025-08-27 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| fba1c072-93d0-3d99-a6cf-ba02c3e5cba0 | -12.7643 | -48.1792 | 2025-08-27 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 971aa057-ac52-3a56-817c-a5825dcb0fd1 | -7.7359 | -51.1379 | 2025-08-27 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 91c629c5-f6d1-3e26-bb3c-5d60b84b7c9c | -9.4249 | -60.5316 | 2025-08-27 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| eff12d65-1114-38ac-a10e-7929927dfc44 | -17.8471 | -47.7428 | 2025-08-27 14:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 249.8 |
| 10cba1c4-44c8-33e0-a295-bff8a0f2b75b | -7.4414 | -42.0501 | 2025-08-27 14:40:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 6b0463c5-3734-3582-9c66-c9e1e9e11eb5 | -9.0771 | -66.0695 | 2025-08-27 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| a26de049-fe90-33a5-9fda-97363aa6752a | -9.6574 | -64.9845 | 2025-08-27 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 139.2 |
| 7c91c38d-7ab6-3042-ac03-5e8db1f117bb | -12.3998 | -44.9951 | 2025-08-27 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ee9abe1f-120c-39a2-bfd7-2d065d4be976 | -7.5922 | -45.2272 | 2025-08-27 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| bdc39bde-1237-361f-8984-25f2334f0b02 | -10.2743 | -64.4907 | 2025-08-27 14:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 143.5 |
| b50e4915-a4f5-3535-a13c-42cd1c6bf009 | -8.4785 | -43.6624 | 2025-08-27 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 30df86d4-c5c9-3256-9584-833311b8eb2e | -8.2522 | -45.1168 | 2025-08-27 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 1dcff2f5-a3d1-39e4-8a5b-55d2a9a82a19 | -8.4593 | -43.6879 | 2025-08-27 14:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 257.9 |


