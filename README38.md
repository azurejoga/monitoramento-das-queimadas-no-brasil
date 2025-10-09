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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8a25632-72af-3255-bd57-b11b6e26bb92 | -7.77961 | -42.39038 | 2025-10-09 04:19:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c86c068f-6ca3-338a-8ed7-f81ccf84ab9f | -14.41786 | -43.97817 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f4d6801b-d191-3951-80d5-cfd6f4e920b5 | -7.55506 | -44.29806 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b142a1e-665c-382c-8c2b-ca74d0f30100 | -7.7703 | -42.40485 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b08dab2c-40b9-343d-95df-37f6de78593f | -13.3265 | -40.90137 | 2025-10-09 04:19:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 989057b5-a2a4-3ab6-8af8-0827b4a829ff | -11.77825 | -45.15051 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7be2bc07-929a-33b8-910f-1a5d9b19c2e2 | -10.23575 | -46.09867 | 2025-10-09 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c54fa89-7e0d-3aac-902c-bd958cedc9a1 | -7.77844 | -42.39819 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6821d8b2-3653-36c2-8e2b-6b2839159a44 | -11.14778 | -47.737 | 2025-10-09 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 573c4e60-87ca-3c79-9aae-6ca83f378801 | -7.81711 | -46.70935 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46e4989b-d8da-3a6d-952c-d7ca810e6341 | -8.19885 | -43.36298 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 80f1b30f-dadf-3b28-9802-080a1b3990f9 | -11.9897 | -45.18761 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b64d564a-bf5b-3d1e-83ee-6e2aaa322a5f | -7.67686 | -47.42004 | 2025-10-09 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c9ac866-bb01-3c58-9e5f-fd3f6b72944b | -8.22584 | -44.15616 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a99f3255-2cb3-38d7-8ad7-f4ac37ba75ea | -11.77161 | -45.14944 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6905640-4815-3139-adad-29e773933b7b | -7.45617 | -47.17698 | 2025-10-09 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90293ba2-0c25-3ebd-a6c4-2a948b05abaa | -13.65248 | -46.80967 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7da77b98-124f-3010-ae16-dd4c6cd7bd38 | -9.19189 | -47.8619 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d30cd23-7eb6-317d-8c0c-0fd8c79c2644 | -7.71531 | -42.38105 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 065e7e63-593b-33df-8317-308c10577316 | -11.68553 | -44.25765 | 2025-10-09 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78db03b6-09e5-3935-a8c3-34e82ac82bbc | -9.76487 | -47.7106 | 2025-10-09 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e1e0042-99b4-3799-8d76-1b849ea2a30b | -10.92678 | -42.84661 | 2025-10-09 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 23496b79-971f-3dc2-bb33-d270d928254b | -12.0027 | -45.18956 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52ec34de-c693-3332-815d-d466ea796e40 | -7.73268 | -42.40759 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 735acf19-a2cd-3615-8acf-3c25e2e950c9 | -9.18836 | -47.86132 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf4bf486-7882-3616-82fd-479cc0866e80 | -10.44269 | -46.6324 | 2025-10-09 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d948b7dd-c96a-30af-a7db-9a3cf9df8126 | -8.55107 | -47.7253 | 2025-10-09 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7dfa3be-f96c-37a1-ae75-df2eefd10a2f | -8.62257 | -45.13246 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e9c1592-9397-3f8c-b8ec-7f522ad7d4c7 | -8.53178 | -46.19359 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 10eae3b6-e454-3632-821b-5e18748cb7bd | -8.18979 | -43.33166 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| c99db16d-f0a4-3659-90ef-ca7f275e0689 | -7.48784 | -47.1583 | 2025-10-09 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1f19b79-86d6-3b2f-817f-b5687e68f4e7 | -8.43599 | -47.19366 | 2025-10-09 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1161f6fa-4d6d-3bd8-a586-6355b739014e | -13.82539 | -45.80212 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a84934af-3f10-3d95-84aa-786bb0e25a2a | -11.78371 | -45.04996 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3f27fb9-fb18-310c-8851-580e9a0ac9e9 | -9.19542 | -47.86248 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84b6e3f1-b896-35c7-9fd7-d7636e0a78b8 | -7.81651 | -46.71308 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1e2bc92-91fd-3be8-b628-642d683f2a0c | -12.145 | -47.75304 | 2025-10-09 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22b09910-d85d-309e-9560-80804994a69b | -14.4019 | -46.02348 | 2025-10-09 04:19:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a97b5505-293b-3138-9e94-f12d66f0a1a8 | -14.42482 | -43.97925 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 957c83b9-3312-3df2-80ae-bc229d267953 | -10.81748 | -41.94952 | 2025-10-09 04:19:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 36f4b7b5-2472-3bbf-a447-cf49f8904cdf | -11.34359 | -49.37991 | 2025-10-09 04:19:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59636b71-8d9a-3146-88a5-4bf2f107eea6 | -7.76031 | -44.20156 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79624ce6-80dc-39b0-b5e0-a5f3e8610fd7 | -13.48341 | -42.02272 | 2025-10-09 04:19:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 66dff7d5-ac91-3c50-aee1-072d517fe5f9 | -9.79042 | -47.75092 | 2025-10-09 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8e4621d-cb1a-382e-8028-d723f5bb5a68 | -13.66849 | -48.74559 | 2025-10-09 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ff79e93-44da-38e8-8387-d6775f3f3b2b | -13.66589 | -44.30803 | 2025-10-09 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84277711-5738-347a-939d-93d8dce2bccb | -8.8353 | -44.42793 | 2025-10-09 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49f87e79-0e54-3f09-9afe-99ad200f7f78 | -7.29113 | -44.83145 | 2025-10-09 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2344042-ae63-30f0-82fb-9b3a012e4d79 | -12.24413 | -43.78136 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 358ea142-6086-3a43-85a6-bb3cfcdae90b | -11.72364 | -45.34772 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ac61101-fc7f-31af-b3e0-1c7f2d72641f | -12.26909 | -47.89397 | 2025-10-09 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 153b11d7-6355-3da5-98b0-15be736e73bc | -11.79092 | -45.04743 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48c0acc0-5fb2-31aa-8e08-1d990a70e88d | -11.47488 | -43.47929 | 2025-10-09 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73933c41-3e9c-39aa-abd0-56478e93c136 | -7.59607 | -44.03637 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3b6b6d5-386a-3e4c-b318-4cbac72942d8 | -10.19745 | -44.55228 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78951f0d-20cf-3322-9c44-0976dfb6ebf3 | -11.13552 | -47.74714 | 2025-10-09 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 317b6b93-972e-3c09-b4a3-413a47895b80 | -14.41669 | -43.98606 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 50d4a7e6-b0ab-3359-bda0-f4bd0df8dc3a | -7.66982 | -42.58663 | 2025-10-09 04:19:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e56f50b1-bc06-3f36-8c02-48a64efd0e08 | -8.52276 | -44.14495 | 2025-10-09 04:19:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad42df06-4d72-3e83-9abb-cfa296244d46 | -9.70648 | -42.2387 | 2025-10-09 04:19:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 88241bda-c6ea-3520-a7d2-ec1091c2bfa0 | -14.79132 | -46.09467 | 2025-10-09 04:19:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb2da392-2c92-3a66-8d4b-30dc5e7c8297 | -13.82593 | -45.82039 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea0452b4-6959-3fb7-9368-c86728e8a95a | -8.16166 | -43.32774 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c5dc9f40-e23e-3e0f-8a4b-3efa436c459a | -11.78102 | -45.15456 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17fc6ecc-3671-32b3-9a75-fd4995b7e8e4 | -2.3797 | -47.71125 | 2025-10-09 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 91bcf018-a09e-3861-ab19-eec8a79028fd | -10.86929 | -44.28747 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed2433d7-6733-3f4c-a28c-20948dfbb420 | -7.9045 | -43.53998 | 2025-10-09 04:19:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0994046-b0a3-35bb-aafa-9d0d5e9e046f | -7.77495 | -42.39764 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 72765f7d-f6ef-345f-a3b6-ed016a228aea | -11.88603 | -45.54646 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1bc62d2c-b86e-3c2e-8117-8633e8a0c8a4 | -7.45902 | -47.18142 | 2025-10-09 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e23ae91-8997-3616-88ad-0e51cc0e7f06 | -7.32524 | -44.78717 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed62d772-af7f-321e-b15a-fc1b89b064ef | -7.77785 | -42.40207 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a67e165b-b958-3b6b-812e-a693e8b641b9 | -8.50297 | -44.22838 | 2025-10-09 04:19:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae05e3a9-35d1-3d8b-9841-388664954a65 | -11.98474 | -45.21942 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5222a864-9a21-3ed3-a17a-8b2bf1215f71 | -14.07735 | -50.15767 | 2025-10-09 04:19:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f9d7fca-a1d5-3846-a34b-f22218152135 | -9.75637 | -47.6972 | 2025-10-09 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c571c52-12c5-397f-a561-9177c9f4ddba | -7.8243 | -45.1974 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf1a02ed-d0bd-3847-8505-060579123939 | -7.78028 | -44.24764 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c5924e4-d562-38e0-a255-751564d3c6e1 | -7.77901 | -42.41814 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fdcfd9df-88c0-311e-b2a2-d8e5ab00a255 | -7.79354 | -42.41641 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a737442-e3d8-3432-83e0-5016f323774c | -8.18302 | -43.33062 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 1dad96b3-50fa-3701-bb49-958566c63037 | -10.19858 | -44.56697 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4665d754-0b31-398b-9fc6-09b8905e1e40 | -8.5423 | -46.21367 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20cbb6bf-a490-304e-bb4b-8a9ac2db8186 | -12.58197 | -41.2882 | 2025-10-09 04:19:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2733d072-4d75-3488-9231-2162526faa39 | -13.48721 | -42.02325 | 2025-10-09 04:19:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24023240-afb4-39db-bb81-d05374ef489e | -11.8702 | -44.9283 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc5c9990-fc95-3dbb-8c35-d1695f982ba8 | -8.61762 | -45.12106 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb45807b-0f0e-32c0-863f-512b87189e05 | -7.32746 | -44.79462 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d66e4458-989b-3e8e-b7fe-e5fc830f70a9 | -7.77214 | -44.03851 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6bbb100f-138d-3a8a-aebf-37e7d68925b5 | -3.55692 | -39.11028 | 2025-10-09 04:19:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ac6b5e5-f26c-3496-85b9-3481f99df627 | -11.98529 | -45.21588 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20ae456c-7ca9-36af-9fbe-32e0a1da54c1 | -13.58726 | -48.66692 | 2025-10-09 04:19:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4688c3b6-c7cf-35f5-8587-99c476da3ed4 | -13.79001 | -45.87638 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bd19bae3-e7ec-3706-8930-a18ace81cd2a | -13.61803 | -44.43959 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec91d03f-2054-3e03-8009-6b6176ea8aa6 | -7.76773 | -44.04497 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88bf018b-99df-348e-8168-ec7af4cb815d | -13.79831 | -45.84499 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99b3626f-c131-35b3-821a-4cfdaa306b6b | -11.8717 | -45.52971 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ef1b2bb-0abe-3018-a333-b2fa189b6b1e | -7.34529 | -46.28387 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25630bcd-1baf-344c-a260-fa7ca8e68c99 | -7.99984 | -44.4715 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fecac916-6d92-3b1f-884b-833bd4dc5b06 | -10.55214 | -50.04176 | 2025-10-09 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README39.md)
