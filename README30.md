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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cd283e6-bba1-35b9-8f59-aa27b49164c0 | -3.94268 | -46.43148 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 2edf6910-a6c2-399f-9d4b-e0ad70c4309b | -3.94213 | -46.43497 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f1b13a45-467c-3884-86df-03fc55823a68 | -3.9399 | -46.42749 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 5d737a3f-5f68-3f39-9751-cb4e957bf3be | -3.93936 | -46.43097 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 724cf80a-c5cb-3e45-92d3-4c860674217c | -3.93712 | -46.42347 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9b930e59-df15-3329-8a39-8f9d50882173 | -3.93658 | -46.42697 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5efa5821-9d32-3cb2-b6e9-399e521d3e94 | -3.92988 | -46.4044 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6496f370-b9f6-361c-a7da-3313e9f7385b | -3.92656 | -46.40388 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5049b97-c28e-3ea9-8404-4618ae627d6d | -3.90902 | -46.45121 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1312da1-d4fb-3994-beb0-8252608232bd | -3.89333 | -46.44178 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27218e57-8868-3607-a7c8-2c8b4bbc9e00 | -3.89001 | -46.44128 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15e707e9-ef94-3b89-a6d9-bf7923b567c4 | -3.88946 | -46.44477 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9302099a-f5f5-37d6-91da-c6b9ce6e37f3 | -3.87841 | -46.4502 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96ed27e9-4bbc-3458-bdb5-6f25f9328ecf | -3.87564 | -46.4462 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f26031e-c7ea-3120-b18a-4b121ec0d438 | -3.8751 | -46.44968 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a7e81ab-eb99-3b0b-9750-786b27414ca9 | -3.87178 | -46.44915 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b4e6e66-7ce6-3fcb-a881-ea5238ef616f | -3.86792 | -46.4521 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d3d7872-5348-3343-b925-4dc53944a3a2 | -3.86675 | -46.63296 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6b0f363-cd6e-3a11-aae1-6e12de8c75b4 | -3.86621 | -46.63643 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d49a7fe-f0b8-35c7-9b30-dbe938e0f1a1 | -3.86344 | -46.63246 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46094857-febd-3b29-a893-42b017ff4487 | -3.85201 | -46.48874 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b028d7d-cf2e-374d-9a18-4f3fffd4b455 | -3.84727 | -46.8912 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b89dcd1e-02c0-3f5a-8bec-c479b0f2daa2 | -3.83312 | -46.45744 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2efbe579-b0f8-34a0-8cbe-0538334edfb4 | -3.82988 | -46.47822 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33a9d7e7-9ea6-3b18-a626-58a6e36cc886 | -3.82762 | -46.93041 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1449c503-bf8f-32f6-a331-3ef893752535 | -3.8271 | -46.47426 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9a13f9e-df03-39fc-994c-3132880046d4 | -3.82708 | -46.93384 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc584369-c47d-3b9a-86ac-8bfda02c60d8 | -3.8241 | -46.92636 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7dda80a2-e291-3960-a1b4-1ab6f1af44c2 | -3.82356 | -46.9298 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4b648a7-81b7-3517-8d4c-569d0939666a | -3.82303 | -46.93323 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55a674ab-03d4-3006-b551-48685271a496 | -3.8208 | -46.92585 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c01300e4-39b8-3abc-8558-9966715f16b0 | -3.82026 | -46.92929 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bda5f46d-8d94-37ff-8cd6-095f02a1ed3e | -3.81973 | -46.93272 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99557f03-ca3a-38e8-907a-6cbfab73c2dd | -3.81804 | -46.92191 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6195b59-741d-3f89-8f45-b3821515d952 | -3.8175 | -46.92534 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b8217ee-9a97-373a-82fa-509a9df220a4 | -3.81696 | -46.92878 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94d93faa-8262-3dae-86df-d73c2d08b447 | -3.81474 | -46.92138 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 532e3620-2509-34d2-a764-546c55e01338 | -3.8142 | -46.92482 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42228174-46e1-3d5c-b8f1-5b19654b9f4b | -3.79796 | -46.50872 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06ef5c61-ef7c-37b1-bb8f-e8b2ff8e8e70 | -4.99942 | -46.48182 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a1b53e6-f5dc-3d82-9836-45a1cff82b64 | -4.99662 | -46.47782 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 837aa124-abce-3297-b942-4b3a60ba9f3b | -4.99608 | -46.48133 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 697f432d-11c1-375f-96e6-570bf5e4370b | -4.99554 | -46.48482 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5232dfa2-fe4d-3970-be0d-73020c3396d1 | -4.995 | -46.48831 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79f2c964-0e78-3cf5-b44a-0daec1e3909b | -4.99167 | -46.4878 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 294e8b5b-547d-3ded-a330-2991d127286e | -4.98942 | -46.4803 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16ca79f2-fe97-3f37-96dd-ec4f7304bd17 | -4.93604 | -46.84692 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3502f541-eefa-3e55-9799-0e87b0a2ed11 | -4.93272 | -46.84641 | 2024-10-24 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2c24318-2c78-3e8b-8b2b-d085f73a88b6 | -4.82601 | -46.85421 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 462073e9-0ffd-3860-8688-819e660e2e30 | -4.77039 | -46.40296 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9f04aed2-6b4b-319a-9f76-288c82f8d911 | -4.76985 | -46.40646 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| fa36c01e-fd7e-3c7e-a52b-b00ec46da26e | -4.76706 | -46.40244 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9e802b02-550a-37c6-aee3-ddee8a709b0f | -4.76652 | -46.40594 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e29b6be7-79c8-3cbd-bc82-8a09c9f8c088 | -4.76373 | -46.40191 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b5ab04e4-b629-3fc0-b5dd-18f3f08298c3 | -4.76318 | -46.40541 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2a4069ba-1184-33b4-b130-a35635b7f1c4 | -4.76264 | -46.40892 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 97661558-dcd2-3ae4-8c7f-f29221fc8f3b | -4.75931 | -46.4084 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ce34354c-95b7-326f-9d35-8a29c859d12d | -4.75664 | -46.64422 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9e037830-8bbd-3065-9eb3-6855a582d71e | -4.75332 | -46.64372 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6e2ceabe-53ee-36f0-8b8c-ca0c1de31f77 | -4.75278 | -46.64719 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b3dde301-50b4-3abd-afcb-83120d91665b | -4.75046 | -46.61832 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b5674781-9af4-3711-9bdf-7e3fd8f369b3 | -4.74714 | -46.61782 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b7a8d2ef-e3ab-3d38-9f4a-5157d1b5562f | -4.74582 | -46.60352 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40a1463f-a8a7-3ad9-a444-0ad83bfafd6a | -4.72724 | -46.46091 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 501529fa-621d-3a96-861d-5327c26b466c | -4.7267 | -46.46441 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f7916d7-30c2-36d0-8436-ad637fb714b9 | -4.69088 | -46.36543 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05dbc8a8-d67e-3c9d-b6ba-45b229544f4b | -4.66391 | -46.58362 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31db36a1-f5c4-372d-bc8f-446f91f49b66 | -4.66059 | -46.58311 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1e15819-b225-3dc3-b6c2-cdc99a12ab6f | -4.5626 | -46.68851 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 095d7259-dcfa-3a78-b12a-bf4a347fdf3e | -4.53238 | -46.73008 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 295bfa9e-7d73-389e-a5b5-cccd228d88cd | -4.53184 | -46.73353 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6dc489e0-2b10-30b7-8d8a-1eada0a9e81c | -4.52556 | -46.57615 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04481ce4-9222-3438-b78d-2ca7bcb62698 | -4.52502 | -46.57962 | 2024-10-24 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c5d300d-9ede-30a5-8a5d-fea0bc90bdce | -4.42742 | -46.46436 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44327c11-708d-3ee3-bbb3-2c227b351452 | -4.42687 | -46.46785 | 2024-10-24 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 43bd24e3-d516-37f9-9042-b820b48354fc | -4.35429 | -46.80165 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0a90345a-855c-3fbb-b78c-4a41ef79bdac | -4.35152 | -46.79768 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2707eefe-c0c4-345c-bccb-fb68e6622e40 | -4.35098 | -46.80114 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 766c6fd5-0a53-320b-a3bf-8ba6aac39dfa | -4.2832 | -46.75467 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f50d190-3467-3f18-b0f7-f73785ca5a1f | -4.28266 | -46.75812 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf2e3441-bf31-3fc9-a893-62a4cc10ccc9 | -4.28043 | -46.75072 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2eec6442-3336-34ea-9065-19dfead36629 | -4.27989 | -46.75417 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6ff28fe3-b673-37a9-83ee-0d58029524a5 | -4.27935 | -46.75761 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5603b3d9-4da4-32f6-8ed2-6d290e94da30 | -4.27604 | -46.75711 | 2024-10-24 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8ba3ffc-ae4e-3a88-985e-db782e54e12b | -5.33022 | -47.22036 | 2024-10-24 04:32:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f59a81d-865d-388d-83b6-46d3defa5663 | -5.30583 | -47.00424 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dad5dabd-a152-3050-a533-8a1e415a3945 | -5.30529 | -47.0077 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8ead12c-be19-3d30-8767-2461845f8be7 | -5.30306 | -47.00026 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2d42f0ad-b30d-3111-a828-4d2995435d2a | -5.30252 | -47.00372 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 59b844d5-81fa-31f9-951d-0534a2f4653f | -5.29975 | -46.99973 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8bbaee52-6450-36b2-8174-06605d000117 | -5.29921 | -47.00319 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c9698c68-ebf7-34ef-9bbb-33a5d9ee63c9 | -5.29867 | -47.00665 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3987422a-fc2d-3967-88a2-f71a04cedc52 | -5.29813 | -47.01012 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 707c9d69-a3ba-327e-bbc1-0304e99499b5 | -5.29759 | -47.01358 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ed87eb39-330e-3fe3-bb95-3bd3a0874532 | -5.29536 | -47.00613 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6aa3b8e0-44e8-30ad-b85d-e07bf3b71091 | -5.29482 | -47.00959 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a365c816-efde-3198-a9f9-eb17e187f781 | -5.29428 | -47.01306 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eec02714-267b-3430-8765-1c2ef2a20c66 | -5.29152 | -47.00908 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 129f30ef-7a7b-38ac-aa1b-38e48b63e8bf | -5.21229 | -47.19136 | 2024-10-24 04:32:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed6f18c4-55f5-3755-99ec-f2718903667b | -5.07801 | -47.8922 | 2024-10-24 04:32:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README31.md)
