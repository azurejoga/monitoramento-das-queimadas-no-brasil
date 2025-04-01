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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5501c4c-2a29-3e44-8506-e423ad7a46c6 | -13.04434 | -45.11214 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3ed7bfd-58bb-30f6-945b-9aef94333a64 | -12.29197 | -43.54446 | 2025-04-01 04:51:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5220c170-64f9-3117-813d-2afb55956cc1 | -13.02822 | -45.11327 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04b08d33-40d0-3695-aef9-a25cb013ee91 | -11.54034 | -54.36998 | 2025-04-01 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 509cd5b5-33f4-32a1-8b54-ce1afc6e2b35 | -13.02783 | -45.11652 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d712d677-bea3-3cc0-bb33-0a4c72de25c1 | -7.23649 | -44.77097 | 2025-04-01 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f2b7b92-5b89-3b3c-9c4e-faa2f27b81ca | -13.03949 | -45.10818 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f8f6c901-2801-3146-a9e8-87116511b796 | -13.03465 | -45.10423 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f49a4e09-f081-3d0c-addd-da366ef55e88 | -11.53702 | -54.36945 | 2025-04-01 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1f7eaba-b0ee-38a0-8a01-94569bd88388 | -13.03425 | -45.10748 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bd69ed0d-a996-3117-ae1a-faf42caecf9d | -7.23813 | -44.77136 | 2025-04-01 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f3ca4ae2-9448-3eee-9707-c0dc220df488 | -6.20844 | -48.04445 | 2025-04-01 04:51:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6659136-9ec5-3f39-b7d0-d7a9bb8b8681 | -13.0391 | -45.11143 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 392b7ec1-95d2-3f6f-be07-4217ee13ce44 | -13.03346 | -45.11398 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52677810-c254-3c9e-9e97-5b691cebdf50 | -12.29352 | -43.54165 | 2025-04-01 04:51:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a807b1e3-eb64-3cfd-8d7e-4b25499a4ef8 | -13.03019 | -45.097 | 2025-04-01 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cadd2b8-c25f-3255-9755-97db7b3ffe62 | -13.5833 | -45.24562 | 2025-04-01 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c052297-21b9-32b5-bc15-bd913875b421 | -13.58393 | -45.24463 | 2025-04-01 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0f68ec2-d909-30c3-9bd8-d67a956bf01b | -15.07951 | -48.94268 | 2025-04-01 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a64a5ee-c9cf-3820-9914-0c5bece64e54 | -15.89719 | -43.45586 | 2025-04-01 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdbdc488-684a-32b1-b509-770877c2bd5f | -13.58371 | -45.24228 | 2025-04-01 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cd13e15-4f00-3651-b068-978d24364686 | -15.89067 | -43.45965 | 2025-04-01 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da7c57f2-297a-3905-a4f2-e9562b269eab | -13.58356 | -45.24794 | 2025-04-01 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e3956b9-ea71-39ad-a6fa-e3b040a6dd85 | -13.58318 | -45.25122 | 2025-04-01 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75800ff8-ab20-3fca-a0d2-7e654aec823a | -13.58432 | -45.24128 | 2025-04-01 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29b92c78-f09a-3286-b5e0-f62aae8cb3bd | -13.5829 | -45.24891 | 2025-04-01 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 948b3505-4617-3744-828d-203ade2ac106 | -18.73218 | -45.02345 | 2025-04-01 04:53:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1b4e25f8-19e6-30c0-9245-18383f402b95 | -15.07898 | -48.94679 | 2025-04-01 04:53:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e905c7c0-3f29-3331-84c6-b91c54b8b4cc | -25.19206 | -49.32587 | 2025-04-01 04:55:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cd8fca58-52c6-3c6f-8431-525933c219a5 | -21.28152 | -48.56961 | 2025-04-01 04:55:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ff39865-7e4b-3b41-a79f-a9d7bcf138be | -28.28749 | -48.85434 | 2025-04-01 04:57:00 | NOAA-21 | IMARUÍ | SANTA CATARINA | Brasil | 4207205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 26d5b8b5-a2eb-3a8f-a785-58f6b2eaa5ee | -27.68966 | -48.75027 | 2025-04-01 04:57:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f92f6517-226a-3b1c-8154-40c8789e5b1f | 2.02033 | -60.90092 | 2025-04-01 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64bf2c22-b228-38ee-8d71-e53f82f09b1a | 2.31163 | -60.22437 | 2025-04-01 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ef7ffc7-10d2-32c8-8e22-03458431790a | 2.01655 | -60.9015 | 2025-04-01 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f431334c-3ea8-3b53-80cf-de88fc9e5d04 | 2.01963 | -60.89634 | 2025-04-01 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 641f9de7-dd86-370d-86bc-43731caf2d35 | 2.31527 | -60.22371 | 2025-04-01 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efaef380-ac1b-3d3a-8f24-d17ced87a616 | 1.92979 | -60.38372 | 2025-04-01 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e57647df-33f0-3bfe-aa41-a5613e813fba | 0.82553 | -59.28302 | 2025-04-01 05:16:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edd73d14-f369-39d6-a1a4-b5d789dd96cb | -11.53995 | -54.36817 | 2025-04-01 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cb8283f-8439-3b30-81ba-6ba0a7fa71af | -11.53937 | -54.36823 | 2025-04-01 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eafafa01-fd04-3b26-b507-6a42d28a9ab7 | -11.35036 | -57.66414 | 2025-04-01 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1c3856c-b6c3-3a08-862e-15c3ba0474db | 2.20808 | -61.63307 | 2025-04-01 05:38:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c806707-a225-3c6f-aef9-8d6b460eaa40 | -13.5905 | -45.242 | 2025-04-01 12:10:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 1293fb22-51de-38c9-9383-b4c0ecf6b8b5 | -13.5905 | -45.242 | 2025-04-01 12:20:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| aef86b12-c8c9-35ca-b495-cf8b14d3b1dd | -13.5905 | -45.242 | 2025-04-01 12:30:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| a874a77e-c6ae-3c8b-a721-d24f37c0a2be | -13.5905 | -45.242 | 2025-04-01 12:40:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 3f97ae8f-9337-3daf-b0c0-cbb32ce49843 | -13.5905 | -45.242 | 2025-04-01 12:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| a1741d55-2197-3268-9c41-1246150549fc | -13.571 | -45.2452 | 2025-04-01 12:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 22ca821c-35b0-33d9-b12d-e3fb7f348fe0 | -13.571 | -45.2452 | 2025-04-01 13:00:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| d088e8f6-e0b0-31b4-899b-f7aea11cb7f8 | -13.5905 | -45.242 | 2025-04-01 13:00:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 381f8c52-710d-375e-a34f-fc33d3b5f5a1 | -13.5905 | -45.242 | 2025-04-01 13:10:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| d2c03279-be2a-3c6f-a32d-6d1b1d68d848 | -13.571 | -45.2452 | 2025-04-01 13:10:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 4bcbc200-be91-3bab-9a85-7ea3eb482a5b | -13.59 | -45.2652 | 2025-04-01 13:20:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 1bac2bd3-ec84-3833-a3c6-c46c362c3b48 | -13.5905 | -45.242 | 2025-04-01 13:20:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 610ebff6-b8f1-3882-9a35-492401364139 | -13.571 | -45.2452 | 2025-04-01 13:30:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| b4d12871-10bc-370d-8bdd-dc8ed1eadc78 | -13.5905 | -45.242 | 2025-04-01 13:30:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 57ac74b2-b65f-3c1d-b4c0-7a1cd3bb15b5 | -13.59 | -45.2652 | 2025-04-01 13:40:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| d2866c79-13ce-3940-b414-fa0b7fe37577 | -13.5905 | -45.242 | 2025-04-01 13:40:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| dfc20fde-987e-3834-b067-eb5d8d7f7875 | -13.5905 | -45.242 | 2025-04-01 13:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 4a2ec5de-b589-30b8-9bdc-afa665a77aaa | -13.571 | -45.2452 | 2025-04-01 13:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| eb9b64a5-1910-3568-b92a-61cf827af7f0 | -13.59 | -45.2652 | 2025-04-01 13:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| d8657348-928f-3dc2-beaf-3e79c4ce28a8 | -13.59 | -45.2652 | 2025-04-01 14:00:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 12b7da27-d4e8-3042-8873-db584d0a11be | -13.5905 | -45.242 | 2025-04-01 14:00:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| d6d248f0-ca15-3a15-8833-82b57d859462 | -13.571 | -45.2452 | 2025-04-01 14:00:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 0547c6bd-6601-33c9-83ad-1fc55617c862 | -13.571 | -45.2452 | 2025-04-01 14:10:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| cfa4dcf8-6282-3619-938b-828654112a20 | -13.5905 | -45.242 | 2025-04-01 14:10:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 175.6 |
| ebb04a97-02ac-34b6-a560-d9f66cdb07e6 | -13.59 | -45.2652 | 2025-04-01 14:10:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 5fa46794-a208-3b41-bfa3-72fe6feba108 | -13.59 | -45.2652 | 2025-04-01 14:20:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 55ef0fc5-1ca2-32fe-8a25-f018a0b3627c | -13.5905 | -45.242 | 2025-04-01 14:20:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 1186564c-09d0-333d-968c-0bcb680115be | -13.571 | -45.2452 | 2025-04-01 14:20:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| f3a7c5cf-99b5-3c3d-99c2-bf3783ec4e10 | -13.59 | -45.2652 | 2025-04-01 14:30:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| fa25fd0d-3343-386e-b61d-2d13fc19cb49 | -13.5905 | -45.242 | 2025-04-01 14:30:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 9f849373-7043-3433-8c75-31bb1a43e696 | -13.571 | -45.2452 | 2025-04-01 14:30:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |


