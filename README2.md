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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c692533-f9bc-3158-9073-421819c309d1 | -16.28907 | -40.77337 | 2026-02-08 04:36:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| aeeaa12a-2e40-34b9-9dd5-bddc24f0c1c2 | -16.28871 | -40.77657 | 2026-02-08 04:36:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6c8ccace-20c6-3c86-a973-b755f4d4abd3 | -15.42404 | -41.42837 | 2026-02-08 04:36:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 92c28496-c6e1-3c28-8b9b-43a66e0f304d | -12.91244 | -49.4783 | 2026-02-08 04:36:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 703381b4-fc6f-3fb0-93f1-21782773de98 | -12.92125 | -49.48698 | 2026-02-08 04:36:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b06d9680-d676-356f-a496-e01efb0132e4 | -12.91519 | -49.48237 | 2026-02-08 04:36:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d8947994-e4a0-39c4-b272-769b15a37384 | -12.91794 | -49.48643 | 2026-02-08 04:36:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4461e5d-89cb-3ce3-a6cc-452bd617f42a | -15.42876 | -41.43218 | 2026-02-08 04:36:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4924724e-76a3-3636-ac2f-892f271b19a8 | -18.15886 | -39.79502 | 2026-02-08 04:38:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c8f6fa52-3557-32e9-b1df-47d5da4a2ffe | -22.68559 | -50.47525 | 2026-02-08 04:38:00 | NOAA-20 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa2dda33-4601-381e-9120-9381f6eebe70 | -22.68421 | -50.47582 | 2026-02-08 04:38:00 | NOAA-20 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d26d3b86-4834-31a2-81ee-92acf690b5ca | -18.15254 | -39.79877 | 2026-02-08 04:38:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e63ee30e-1eb2-3e56-9879-ec1b9ad660cb | -18.15299 | -39.79438 | 2026-02-08 04:38:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 51a78f4b-2fe6-3c41-a928-dfcfa3d0ef85 | -29.81659 | -52.01955 | 2026-02-08 04:40:00 | NOAA-20 | GENERAL CÂMARA | RIO GRANDE DO SUL | Brasil | 4308805 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 79902479-62a7-34dc-8472-9681f556a474 | -33.0594 | -52.64603 | 2026-02-08 04:42:00 | NOAA-20 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 883d2fb0-90b7-3449-815c-6b124c3d1a1a | -31.46647 | -53.6524 | 2026-02-08 04:42:00 | NOAA-20 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 173360ee-b005-3bb4-b4a6-e68c8ce836e7 | 3.01673 | -60.856 | 2026-02-08 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23065175-1728-3596-b00b-6d4b54727bab | 3.04962 | -60.86266 | 2026-02-08 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85042f5f-89cd-3d51-9aee-ecf18b97a49c | 0.15319 | -60.49279 | 2026-02-08 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04ba4709-bd72-331c-be82-6487d60eb67b | 0.15207 | -60.48571 | 2026-02-08 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d53cbfb8-d8ef-34d9-8635-2f5c357fd939 | 1.35645 | -60.07123 | 2026-02-08 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a04d9b4a-b112-3c67-a0d2-a3b45af35436 | 4.89646 | -60.59902 | 2026-02-08 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8718d9fc-fa44-3fbb-943f-01d6ebb5daf7 | 4.16294 | -60.16053 | 2026-02-08 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c8430ad-14ff-3c81-9229-fe0fc15d0ade | 4.40315 | -60.72043 | 2026-02-08 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fa965b7c-4180-313c-ad75-c68529d265aa | 4.89587 | -60.59518 | 2026-02-08 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98316530-864d-3999-8b44-e9d0a1281e8e | 3.05021 | -60.86645 | 2026-02-08 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a30742e-8a5a-3d2b-9836-52c034162704 | 1.35311 | -60.07172 | 2026-02-08 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f64bef59-aa5d-3394-ac5a-656698ba396b | 3.01732 | -60.85979 | 2026-02-08 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4580ccf-558c-3749-92d9-2d6ad8f992e8 | 4.38457 | -60.71531 | 2026-02-08 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b9e9cc59-a897-32c8-b3e9-dbc77ea48285 | 1.20478 | -59.97253 | 2026-02-08 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 446a7e10-b896-322b-8c64-1d9b49ed26b4 | 0.14985 | -60.4933 | 2026-02-08 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5024836b-8569-3146-b4de-8c0cdee0bdc8 | 1.36535 | -60.06268 | 2026-02-08 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f709d1cf-1337-3d96-bf44-0039d8fb3cd8 | 3.01386 | -60.86032 | 2026-02-08 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 898f8c25-a945-3fab-82a9-88145aba8144 | -0.14506 | -60.73926 | 2026-02-08 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ed4a8bc-0f0d-3ae8-9dda-4e85d3d1ea35 | 3.01445 | -60.86413 | 2026-02-08 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 050bcdbe-cf74-3ea6-b490-c7732fc462e2 | 4.38807 | -60.7149 | 2026-02-08 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ae3d4a5-7e87-301a-bebc-c7b5dfaa4fa5 | 4.16711 | -60.62341 | 2026-02-08 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1e10820-d55f-387c-8c34-3365ee345c90 | 4.28682 | -59.96563 | 2026-02-08 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b6b2cec-189a-3c76-bcc2-054c85007b60 | 1.34978 | -60.07222 | 2026-02-08 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b927eed-c50d-31ef-9478-22ae75de2627 | 2.87959 | -60.26272 | 2026-02-08 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10260bcc-3426-3b6a-83d1-dea81258bd84 | 4.39968 | -60.721 | 2026-02-08 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 142db294-19fa-39df-bd4d-8056f9649025 | -0.14449 | -60.74284 | 2026-02-08 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce365fff-ce5f-3d6e-8da2-6daa3fc58e7d | -0.14113 | -60.74231 | 2026-02-08 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21058723-fd22-3b92-9735-7bf7077507a4 | 1.35256 | -60.06822 | 2026-02-08 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a5c03d8-9417-3faa-80cc-6e79dbc1e0b8 | 1.36202 | -60.06319 | 2026-02-08 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68ad8eae-809d-3dad-97a7-8e595d9db0f1 | 3.16992 | -60.55323 | 2026-02-08 05:22:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50928c1c-7b89-31d9-8322-a31d8a7c0446 | 0.15263 | -60.48925 | 2026-02-08 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ec23c71-389d-307e-b505-1b63fe2906bd | 4.89934 | -60.5946 | 2026-02-08 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f663d5cd-cf4f-3f82-9826-818508915b08 | 0.9561 | -60.53957 | 2026-02-08 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e472c17f-1afb-3365-94b5-85a3ecc34b99 | 1.35366 | -60.07524 | 2026-02-08 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6d9efe83-6160-3c15-b99b-ed331ff90ce3 | 1.28345 | -60.43399 | 2026-02-08 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b984ec9-87e1-3191-9508-9c9497e18b27 | 4.39909 | -60.71713 | 2026-02-08 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2f96228-fc39-387e-9546-2ba33d820352 | 0.15375 | -60.49632 | 2026-02-08 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34e65a53-b770-3a5f-a43f-f46bd981e07c | 3.29977 | -59.91906 | 2026-02-08 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3dbd0eda-1df3-3e09-832a-c307c8adfe87 | 4.16653 | -60.6196 | 2026-02-08 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 680f45b9-b675-370e-91bc-50f0a159671f | 0.95498 | -60.53241 | 2026-02-08 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67bbb60d-3c82-31b8-a0c5-83b08c62f713 | 4.38748 | -60.71106 | 2026-02-08 05:22:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ab60308-ca1b-381c-ae4f-2058456ea7d9 | 1.27773 | -60.53035 | 2026-02-08 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddbc8ce1-48f1-3307-b652-753645c1ba89 | -12.91426 | -49.48214 | 2026-02-08 05:25:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 25d5a808-8a1d-39a6-92d7-ab9ba4afd91b | -12.91933 | -49.48119 | 2026-02-08 05:25:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1ade31fa-655a-31ce-9c11-54368875c7c6 | -9.19119 | -62.28017 | 2026-02-08 05:25:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eb08f7c-74e0-3f4e-8576-4929524c9640 | -3.11845 | -59.92902 | 2026-02-08 05:25:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abccb288-8179-3f28-9550-70d87bfd834f | -12.92086 | -49.48306 | 2026-02-08 05:25:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 907a3252-ed0d-3094-8a0f-1a6cd467188a | -3.07289 | -59.89038 | 2026-02-08 05:25:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dcc1a4d-980b-3489-8f50-82f09ab55951 | -9.72374 | -60.20168 | 2026-02-08 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 93ba6f37-b5f6-3ca9-8a7a-926e81170a21 | -12.91872 | -49.48702 | 2026-02-08 05:25:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bdb2b3bf-6266-39c4-88c1-4ab6d2d29038 | -9.11589 | -61.48669 | 2026-02-08 05:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6db030b-9e57-38be-9f16-b2447a23db12 | -12.91273 | -49.48026 | 2026-02-08 05:25:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0aec18b4-eb21-3afb-9853-21ef48265778 | 4.38818 | -60.71928 | 2026-02-08 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4492be04-0bbf-37ef-ad69-1ede078efe73 | 4.38668 | -60.71017 | 2026-02-08 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc84cb4a-170a-3e7a-bf22-0d7d1e310e13 | 4.38743 | -60.71473 | 2026-02-08 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| feaf2ce7-c55b-3115-834a-398bea5684d3 | 3.29911 | -59.9176 | 2026-02-08 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba3ce39b-5799-3419-a68c-d6727481aa97 | 0.15225 | -60.48893 | 2026-02-08 05:52:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd2f0f5b-8adf-39b2-ad5e-fd1cc7acf8ce | 3.9552 | -60.81171 | 2026-02-08 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12590648-8330-38a0-9b89-43df02b8ca87 | 4.90087 | -60.59473 | 2026-02-08 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d94c429-2527-3a94-8346-18c83e1f6eeb | 2.88021 | -60.26194 | 2026-02-08 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77bc4bfe-e5ab-3595-9503-025cec6d5057 | 4.38445 | -60.72007 | 2026-02-08 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 531e135d-79cb-39d8-8ec2-8354eacb8f33 | 3.01605 | -60.85865 | 2026-02-08 05:52:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cde799c-d83c-3100-b54f-a020ce5cb3ac | 1.35492 | -60.06881 | 2026-02-08 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 188675ec-3d59-3a7a-b765-d9611c69b466 | 4.38371 | -60.71556 | 2026-02-08 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58329a2c-082c-30b7-b0af-9c1eca49318c | 3.30312 | -59.91695 | 2026-02-08 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b012142-8541-31d8-8595-a98c21d0b7c1 | 1.3666 | -60.06321 | 2026-02-08 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb1fa625-cc5b-3011-a605-3b81e80cb916 | 4.8971 | -60.59524 | 2026-02-08 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b35921b2-b2a5-3a94-8dd2-ca479f7a14f1 | 3.05246 | -60.86703 | 2026-02-08 05:52:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 504c1ea6-f946-3453-a0ef-9b05be5631bd | 0.15281 | -60.49245 | 2026-02-08 05:52:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98ae00bb-664a-3cca-892f-64cf47273553 | 1.28445 | -60.43523 | 2026-02-08 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 373e8734-c1aa-3b9e-9776-512b93001d07 | 3.05172 | -60.86242 | 2026-02-08 05:52:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b4bcafc-6cd2-35f6-8f61-832cf3c48dbc | 1.35143 | -60.07312 | 2026-02-08 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 161dabef-319a-3751-884c-5de43f5c75e6 | 3.95594 | -60.81622 | 2026-02-08 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 943c2623-4ce7-3a5d-9746-814264994097 | 3.013 | -60.86386 | 2026-02-08 05:52:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6709f59d-f8ac-3be2-8faa-1bd5c52cbcac | 1.36251 | -60.06385 | 2026-02-08 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a7982ac6-baf7-3bce-95a3-d185085fd09f | 1.11954 | -59.19871 | 2026-02-08 05:52:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aea763ca-cfec-35b5-8046-1528ff7343d3 | 2.87905 | -60.26476 | 2026-02-08 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32a15af7-df23-30ef-b0d0-f6417cc82fbe | 1.35551 | -60.07241 | 2026-02-08 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f4ece52-c8ac-301d-8f15-3ea4c1c35d8d | -12.97044 | -59.52786 | 2026-02-08 05:57:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bce5d70-bab8-3d08-a96e-3dfe490591a7 | -9.11516 | -61.48802 | 2026-02-08 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ee4e8bd-04ce-325d-a481-d01109183ea8 | -12.91574 | -49.47942 | 2026-02-08 06:41:00 | AQUA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4eb59f98-f076-3ebe-be16-97b75680567a | 3.1647 | -60.5554 | 2026-02-08 08:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 34.4 |
| bca236a3-a923-3fc8-835c-f736ee6462f6 | -14.35929 | -41.69579 | 2026-02-08 11:53:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a6cd4a00-c8ba-305b-bfe8-67570979d40e | -15.42997 | -41.42484 | 2026-02-08 11:55:00 | TERRA_M-M | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |


[Clique aqui para ver as próximas entradas](README3.md)
