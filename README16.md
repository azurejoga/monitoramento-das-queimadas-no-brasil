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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60b02132-2a09-312b-acfd-371c7d20252f | -3.0865 | -50.5625 | 2024-11-09 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| ddfa6e2f-1ccb-357e-a3f5-c20500b7a5c6 | -2.6764 | -51.8189 | 2024-11-09 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 6a77afc2-3ebf-3313-bb52-9b9a7419e1d8 | -4.2058 | -48.5491 | 2024-11-09 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 4890124a-b3c5-3409-a964-41206675f3f9 | -1.5164 | -52.1696 | 2024-11-09 02:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c86af7b5-3c8d-331e-ac1e-c83875b2411c | -3.9854 | -48.1708 | 2024-11-09 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| ed29de18-6104-3453-b1a6-67a39a5250ec | -3.9668 | -48.1932 | 2024-11-09 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 220.1 |
| 0a29db3e-8427-37c6-a3b8-b8fc92917c1c | -4.2671 | -47.572 | 2024-11-09 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 8235a78d-661c-34ce-b96e-e9493380997c | -2.4104 | -48.5265 | 2024-11-09 02:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| da8b0d99-2ceb-357b-bd2b-256d63d50c02 | -3.0865 | -50.5625 | 2024-11-09 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 384af8ec-cd2e-324d-8a27-f801f0ccaf15 | -3.1327 | -52.9736 | 2024-11-09 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c1b23e11-d641-379c-ae60-0cac2d1aa983 | -3.9669 | -48.1716 | 2024-11-09 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 264.0 |
| 8532766b-ade8-3990-9c97-a9700d48e716 | -4.2486 | -47.5729 | 2024-11-09 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 177.3 |
| cd8a22a1-885f-3252-8dc4-326b74ec4042 | -4.2033 | -45.8538 | 2024-11-09 02:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8a54179a-4f88-3152-916b-c1ef80b71242 | -3.6004 | -47.3395 | 2024-11-09 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 307.4 |
| a31ae4c3-cd20-3c87-b587-6730d53170d2 | -4.2484 | -47.5947 | 2024-11-09 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 547034a2-6943-3b28-969d-2abce485f2d1 | -3.5818 | -47.3621 | 2024-11-09 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 187.6 |
| eb787f35-1822-3307-8055-903291d66c25 | -3.9853 | -48.1924 | 2024-11-09 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 43d43cae-f984-3586-94cc-8145078aefaa | -2.2479 | -53.7829 | 2024-11-09 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 34ff9146-6688-37a0-8606-ede6c0a3855c | -3.5819 | -47.3403 | 2024-11-09 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 219.8 |
| 4f88991d-0e36-38e1-950b-bc265ec24027 | -2.2295 | -53.7832 | 2024-11-09 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 40172ca2-cc7c-3e49-b29c-d5259282bc88 | -3.6003 | -47.3614 | 2024-11-09 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 250.8 |
| 08fd3b6d-e040-3b30-ac79-41529005f2e5 | -3.5462 | -43.5663 | 2024-11-09 02:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 7e669a19-0425-33cf-b08f-f031ccf5719e | -4.23 | -47.5738 | 2024-11-09 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d2be6d05-8fc2-3722-a084-bfa5719611b3 | -1.5163 | -52.1901 | 2024-11-09 02:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| cb5d740a-ecc8-33a9-a959-3678a85c3737 | -4.2032 | -45.8762 | 2024-11-09 02:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 862d0549-11fa-31ba-a628-001b918ea41a | -3.0864 | -50.5835 | 2024-11-09 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5ca7e319-d91a-32ce-8462-73d4b726546b | -3.1511 | -52.9731 | 2024-11-09 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 434c8f11-4592-3e05-bdf2-59688bb4e640 | -3.9483 | -48.1724 | 2024-11-09 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a78bd423-3ebb-3270-9a1d-289e4bf5831e | -9.44625 | -35.93067 | 2024-11-09 02:53:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5ba7b360-f74f-3684-957d-75d149d2b2a3 | -9.79308 | -36.14415 | 2024-11-09 02:53:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| dcd4a657-992f-3b45-9542-9c9c96855504 | -9.79423 | -36.13838 | 2024-11-09 02:53:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c1ce4bbb-878b-3e17-b53d-4352b1791144 | -3.5819 | -47.3403 | 2024-11-09 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| c3ad91f6-1404-332a-a1d2-de2afefcdf41 | -3.9668 | -48.1932 | 2024-11-09 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 1acf3768-771e-33f5-ae11-df91c1d2eadc | -3.0865 | -50.5625 | 2024-11-09 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 68ea3e27-755d-34fa-8711-1073abfb2e2c | -4.2033 | -45.8538 | 2024-11-09 03:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 7ff29293-8e53-36de-99e7-65d5f9c28884 | -4.2671 | -47.572 | 2024-11-09 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| feb6ebfd-efb2-37f2-89cf-d0e0daf5e70e | -3.6004 | -47.3395 | 2024-11-09 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 345.9 |
| 2b9a3eb4-4d2e-3fef-9d40-e3b18dc8f68f | -3.1511 | -52.9731 | 2024-11-09 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 148.3 |
| b752cf9c-381f-39bb-82be-64c569e5b35a | -1.5347 | -52.1899 | 2024-11-09 03:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| ca44b4fb-e272-3b5b-a7af-2062f622b01d | -3.9854 | -48.1708 | 2024-11-09 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| c2aef50b-a148-3b96-8982-eb69d71d70e7 | -2.6764 | -51.8189 | 2024-11-09 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 10eaf02e-a1ac-3b5f-a18c-5f740cb4228a | -3.068 | -50.5631 | 2024-11-09 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 2f9df21b-e7b4-3b71-9714-9c924f30912c | -4.2487 | -47.5511 | 2024-11-09 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 8f817692-47b1-3694-89ce-d9ca501a6e10 | -3.9853 | -48.1924 | 2024-11-09 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| dec95a16-ef0a-3b38-ad43-acabb6fd785b | -3.6003 | -47.3614 | 2024-11-09 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 239.2 |
| 6628d0f4-6c7d-355a-ad2b-72bf6a9d4034 | -4.2486 | -47.5729 | 2024-11-09 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 194.2 |
| 98acc239-e3a2-3ab2-94d1-bb6d3c929ef9 | -4.2484 | -47.5947 | 2024-11-09 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| c21cc5b2-e826-30c5-ab23-540e7a1d8bd7 | -3.1327 | -52.9736 | 2024-11-09 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| df3c7964-733e-3983-b0a3-8612dca4481d | -3.9483 | -48.1724 | 2024-11-09 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| beec197f-b357-3c5c-b32e-9990f1ec0433 | -23.8884 | -54.0649 | 2024-11-09 03:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 69.2 |
| 2df6b8d8-3955-394b-bc4d-4631a9b38a5a | -2.2295 | -53.7832 | 2024-11-09 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 84341cc6-d024-3de8-ae86-fc1a5ceb5649 | -3.5818 | -47.3621 | 2024-11-09 03:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 1366bf93-0d2a-339d-8e9a-a39c08182671 | -1.5164 | -52.1696 | 2024-11-09 03:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3549c502-9969-3f3f-8d86-60e60ad6940b | -3.9669 | -48.1716 | 2024-11-09 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 221.8 |
| fc6de767-6808-3c01-b37f-007c597fa61b | -1.5163 | -52.1901 | 2024-11-09 03:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6a628f51-9186-32c1-941b-d0d90ad42ff6 | -3.58 | -47.35 | 2024-11-09 03:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49362d1e-7098-39b0-b196-b232e1dfafc6 | -11.09 | -43.36 | 2024-11-09 03:00:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26a06fed-8479-32b1-9926-9285ecb50873 | -3.9669 | -48.1716 | 2024-11-09 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 218.1 |
| 4e6b23f4-d816-36c1-b26f-775c38d70177 | -2.6764 | -51.8189 | 2024-11-09 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| af976639-37d8-328d-bec4-16e10d741a73 | -3.6004 | -47.3395 | 2024-11-09 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 319.9 |
| 6bd2f204-6567-352c-881e-55c33809939d | -4.2484 | -47.5947 | 2024-11-09 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 2b5deede-2c81-3257-90a8-82de00484231 | -1.5164 | -52.1696 | 2024-11-09 03:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 8044f12f-8e80-3f3a-bffe-cef304edce47 | -3.9853 | -48.1924 | 2024-11-09 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 48210294-48d1-35f8-a91b-14e2f57023be | -3.9668 | -48.1932 | 2024-11-09 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 681be29c-3397-3e74-8f5d-defa9dfc1a54 | -1.5163 | -52.1901 | 2024-11-09 03:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| a36f0459-c1b1-3f52-91fe-b221e5e0abfc | -3.1327 | -52.9736 | 2024-11-09 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1934f431-6b98-3a12-9bb9-ccafada0f078 | -4.2486 | -47.5729 | 2024-11-09 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 172.9 |
| 969f85a5-ca87-36e6-8e2a-2106855610b1 | -2.2295 | -53.7832 | 2024-11-09 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| db25620a-3def-347b-8129-19e491205427 | -3.9854 | -48.1708 | 2024-11-09 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 311d2b34-03b8-30b8-a355-79b4d731ee34 | -3.9483 | -48.1724 | 2024-11-09 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 13269ee8-c3c6-310d-b022-9d27759e200e | -3.1511 | -52.9731 | 2024-11-09 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| e8e503aa-740c-3671-a734-ac4a285f0790 | -11.0881 | -43.3219 | 2024-11-09 03:10:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 8e864adc-c4ca-31e3-bd97-ef6babcc4c65 | -3.0865 | -50.5625 | 2024-11-09 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b6292fb1-98f6-341d-9ab4-eafdd5e21528 | -3.6003 | -47.3614 | 2024-11-09 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 209.1 |
| 43c31226-6c98-3753-b6d8-40b80b6a2127 | -3.068 | -50.5631 | 2024-11-09 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 3ddfb3d0-0a91-3a64-a5a9-eef7afd61146 | -11.0877 | -43.3456 | 2024-11-09 03:10:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 12f203f8-5cb8-3458-b627-e9c52d93f2e5 | -3.5819 | -47.3403 | 2024-11-09 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 501c88dd-ab42-3ff0-9148-068d460daa6c | -3.5818 | -47.3621 | 2024-11-09 03:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| b28f935d-8e83-30d9-8edf-98cac5032793 | -9.80698 | -36.14993 | 2024-11-09 03:17:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| d7526906-c308-3b65-93d3-ef825820ff1e | -7.10733 | -35.02052 | 2024-11-09 03:17:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| efbb679c-14dc-3b0e-af61-9911c4827594 | -6.24777 | -39.71368 | 2024-11-09 03:17:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 95eda3e6-717a-37ff-a3b3-d2b3def2dbe3 | -6.24854 | -39.70941 | 2024-11-09 03:17:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8d0ad7d6-c7fa-3a41-95f7-cb1862cad256 | -6.5414 | -39.44148 | 2024-11-09 03:17:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a1a5502d-6c2f-3ee8-ab99-f33662edcf03 | -9.12666 | -43.18153 | 2024-11-09 03:17:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d3171707-3868-3f60-beb9-27b72a340670 | -6.50212 | -39.55861 | 2024-11-09 03:17:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 521bf78e-750c-3f95-a059-577493d59458 | -6.24254 | -39.70818 | 2024-11-09 03:17:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8296802d-f690-31d4-ae66-1fd30d7f9b03 | -5.594 | -37.87018 | 2024-11-09 03:17:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2fbd7069-f97a-314f-b212-30f0abcc4561 | -5.11448 | -37.56886 | 2024-11-09 03:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1d92a2b2-b463-36fc-850c-db06a9df384b | -9.79067 | -36.13763 | 2024-11-09 03:17:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 36a66982-489c-3073-8134-bd57a8a3ee49 | -6.4962 | -39.55742 | 2024-11-09 03:17:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cd91ab0d-a051-36ef-86b6-a0b8bce0fd26 | -6.75975 | -34.97763 | 2024-11-09 03:17:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b088a5cc-d661-3130-a48e-3c2802615af3 | -6.13386 | -42.56409 | 2024-11-09 03:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| beed9ae0-846e-320c-95e2-4c58839d87de | -7.24199 | -38.92315 | 2024-11-09 03:17:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e39a740e-9683-349e-913d-1a5fb33dd8c2 | -7.11237 | -35.01711 | 2024-11-09 03:17:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| b1d5dbcf-6d2d-3259-a876-a90cff724e82 | -5.84173 | -39.62847 | 2024-11-09 03:17:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d1892a3a-a597-3d58-b955-15574381a24e | -6.76478 | -34.97441 | 2024-11-09 03:17:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 40a1ab5a-7dab-37dd-9c8f-1945957550c3 | -9.78618 | -36.13691 | 2024-11-09 03:17:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2d994eb3-0772-3cd0-9825-1c3734668f39 | -6.12812 | -42.56781 | 2024-11-09 03:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 931d8328-d188-3c65-94c3-d99c26074c4b | -4.5586 | -38.0048 | 2024-11-09 03:17:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 86f890b2-2744-3dc2-8168-6d485b771023 | -6.32246 | -39.52025 | 2024-11-09 03:17:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README17.md)
