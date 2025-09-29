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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7663826b-396a-3f29-a31a-ddeb43798c9c | -14.70648 | -45.21087 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71d7a9fc-7f8d-3ba9-b86f-01b1964e8207 | -18.91255 | -41.12581 | 2025-09-29 03:19:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ec2a8dc4-a4dd-33de-8106-460fcbc536bc | -14.59104 | -45.01196 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ce3ff45b-0b19-3c1c-b3db-796f1817fc6d | -15.05347 | -42.33569 | 2025-09-29 03:19:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 28.4 |
| f5ac4d8c-02fb-3002-b256-e16649227ec5 | -20.08263 | -41.35928 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 75afd1ae-1f04-3424-b64d-0fbbfdd9d5c1 | -20.08045 | -41.3597 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f0b4e8f0-ecdd-3109-91e5-31e95352ec57 | -15.24574 | -40.4437 | 2025-09-29 03:19:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fc851068-6ddd-3821-ae5e-0e3b9d14c5d7 | -18.86374 | -41.98845 | 2025-09-29 03:19:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8ec9cd35-87b7-331b-b5f9-e88fdec94b10 | -12.2788 | -44.12721 | 2025-09-29 03:19:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 23df7f47-4bf5-3499-8dd9-6d7ddb3edba0 | -18.11458 | -42.19293 | 2025-09-29 03:19:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 02561431-cd0f-3adc-8734-a2da46e63a8e | -16.24824 | -42.21479 | 2025-09-29 03:19:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 64c2b462-9528-33fb-9299-8970b727d12e | -14.58795 | -45.02586 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 10b933f8-f375-3e3c-8e1a-cfa2583a726e | -19.67875 | -43.76833 | 2025-09-29 03:19:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec0fa0aa-a488-3e19-bca2-bf3cf1bac753 | -16.99797 | -43.50589 | 2025-09-29 03:19:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 402bc327-74cb-3945-90ec-8de9faf031be | -20.08474 | -41.36481 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 28ddd9ac-2b9c-3dac-be0c-4b4328c8a4d5 | -17.28652 | -42.69965 | 2025-09-29 03:19:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8deb9b98-d57d-3494-9b00-6b044774bfc7 | -12.28314 | -44.1068 | 2025-09-29 03:19:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 0524df21-bd6f-3f5f-82f9-591cde816ffd | -16.99693 | -43.51064 | 2025-09-29 03:19:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1b34be8-93e1-31b7-9dd2-4dbb03f94b21 | -20.05373 | -41.33401 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 0686cc3c-9031-39ba-9354-b4e4021c9efb | -18.90671 | -41.12798 | 2025-09-29 03:19:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c86fa486-2b0f-353d-beff-7b20d49db524 | -20.0693 | -41.33627 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 993c769e-b1f7-3e80-a117-f9af73fa9cb9 | -18.90588 | -41.132 | 2025-09-29 03:19:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 79ac0f5d-b8f6-3a62-b9b5-49fadaf571f8 | -17.2807 | -42.69818 | 2025-09-29 03:19:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbfeee72-6fb8-3d34-b15a-218377cf63de | -18.86358 | -41.99209 | 2025-09-29 03:19:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 34fb66a6-a020-339e-b021-14c1e921ec62 | -19.67771 | -43.77283 | 2025-09-29 03:19:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1fdb48e-51bf-3de7-85e8-04a884a53e0f | -15.26462 | -40.61462 | 2025-09-29 03:19:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 510787af-0741-3a57-a17b-909bb920dfb5 | -16.24924 | -42.21009 | 2025-09-29 03:19:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 15db806c-9736-37b3-9b76-c5edd16a44cf | -20.08868 | -41.3561 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b8a4e8c3-b908-394a-84b6-4151373320cd | -14.77731 | -40.09101 | 2025-09-29 03:19:00 | NOAA-21 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e7aa5ee3-edbd-35f1-b006-dbdbcce016ac | -19.86914 | -43.80776 | 2025-09-29 03:19:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6bafbdde-d7e7-3cce-808c-61c49bce74fb | -14.59253 | -45.00526 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9bfac05c-1698-3ab2-8382-f117147cedcc | -15.05947 | -42.33683 | 2025-09-29 03:19:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 288bd3d1-887a-3f94-b1f3-030673f1025f | -20.08554 | -41.36097 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fa222154-99cd-3493-8871-2125c4afa25d | -12.28024 | -44.1204 | 2025-09-29 03:19:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| bf150787-92eb-3adb-880f-3ccf77262136 | -14.59043 | -45.00422 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ec345c61-50cf-3206-82d8-505909b46f77 | -14.58729 | -45.01794 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2a0b06b4-2e99-37e4-9dfe-c710609682ba | -12.28457 | -44.10004 | 2025-09-29 03:19:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| dabe59c5-be56-3a3f-b50d-a9a847bca9be | -12.2733 | -44.11898 | 2025-09-29 03:19:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 09f540c0-55e8-3513-ae6e-4cc388c14c02 | -15.06168 | -45.05641 | 2025-09-29 03:19:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c79af53-956c-33c7-b75d-260a7c378c5a | -12.27184 | -44.1258 | 2025-09-29 03:19:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| d1872d41-6edb-3337-9fbf-286021ad1adb | -14.5857 | -45.02489 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d4b43fef-29af-3429-9e5b-dd968805e276 | -20.05819 | -41.33825 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 0ba50695-7788-3cb0-b619-f607dfca42ba | -20.07964 | -41.36361 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ddf2363c-dd3b-3711-ab5c-f3fc102a1f11 | -16.55229 | -45.31277 | 2025-09-29 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 33f7abc1-4e81-3773-9915-93dccb779fba | -14.70393 | -45.20634 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88e54c0b-2f8f-3b1e-8030-fb6f1b481b51 | -14.58887 | -45.01101 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 51c9d25e-4f4d-3d2a-ad53-cd583f1b9e8f | -16.54696 | -45.30447 | 2025-09-29 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f6b98845-5765-311f-8655-b83a6647e97d | -18.86296 | -41.99214 | 2025-09-29 03:19:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 23876170-77de-36ef-b6ae-fc0ff5838d88 | -19.9687 | -41.7359 | 2025-09-29 03:19:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 307d9bc0-9dcd-388e-a0f9-b0396a70c0ef | -20.04843 | -41.33384 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 171aa43d-3377-3380-88f4-8f63703e57b5 | -20.09146 | -41.35821 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7c359fdc-6f8e-3548-a358-4903cb5433e0 | -14.71343 | -45.21298 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 67613447-c9b6-303f-aaa2-3d5d6059b0cb | -14.47135 | -42.1701 | 2025-09-29 03:19:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d715e617-26bd-3fff-adb1-63e0db83329c | -20.08174 | -41.36341 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 09956d39-f8db-37ca-b94d-e810ec03e3a2 | -15.05241 | -42.34075 | 2025-09-29 03:19:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 28.4 |
| cf682eaf-0cc0-3c26-8a3d-4aafd0d056e0 | -15.78338 | -43.85959 | 2025-09-29 03:19:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| eebb015a-942a-3922-945a-a82b64150c04 | -18.86438 | -41.98842 | 2025-09-29 03:19:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7984c3b5-abdb-3a81-8f63-0912452afd87 | -14.71087 | -45.20845 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| de7a4e33-2297-3656-b95c-b1bd36855ccf | -15.06006 | -45.06355 | 2025-09-29 03:19:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4008c791-37c1-3472-a745-8c019321159d | -15.26391 | -40.61809 | 2025-09-29 03:19:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8df78e58-67fa-38ae-9406-97759d1cf00b | -20.08769 | -41.36068 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6dc58394-9977-3390-b71e-6d42a44b2adf | -14.46783 | -42.17575 | 2025-09-29 03:19:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b3b34da6-ad81-374c-9cd6-86bb10b3a4bb | -17.94837 | -40.20204 | 2025-09-29 03:19:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 887b4cc3-f3fb-3526-92ba-4f37702fe25c | -19.30679 | -43.81935 | 2025-09-29 03:19:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56c1289f-ec10-3da3-b2bd-99df0c39c84b | -16.9955 | -43.50971 | 2025-09-29 03:19:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ab6c7b9-8e11-33fc-8023-cff382fa809b | -19.30573 | -43.8241 | 2025-09-29 03:19:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74a558e1-d66b-3e82-852d-b3915c484593 | -14.5895 | -45.01887 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| dd0be382-4d3b-32a1-b612-8ea198804939 | -16.36791 | -41.59247 | 2025-09-29 03:19:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3b64e55a-9d8e-332e-a31c-6482085a0fc0 | -20.0699 | -41.33341 | 2025-09-29 03:19:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5632ce3d-9729-3824-a7d2-7e6cc5201250 | -20.05284 | -41.33825 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| fdb87898-a8ac-38d6-bf52-940131627ae9 | -15.05841 | -42.34188 | 2025-09-29 03:19:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 6fb8a3b4-9d3f-32c7-a331-d4797e22739a | -20.06478 | -41.33235 | 2025-09-29 03:19:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7773b63b-605e-3f29-8501-717984a0a4d5 | -19.87012 | -43.80354 | 2025-09-29 03:19:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d8bbda89-bd7a-37c5-a270-08363d59df35 | -12.27475 | -44.11218 | 2025-09-29 03:19:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 2de40741-e855-367b-bfb3-e9f15b773a16 | -20.04755 | -41.33801 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 03054bcd-a8a2-3bef-b205-f0bcba6c4724 | -14.08936 | -44.09269 | 2025-09-29 03:19:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ede584b5-ebc2-3926-b79d-3252f368d09d | -20.05896 | -41.33459 | 2025-09-29 03:19:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| aebf89c3-b14f-3eec-9c47-309210cec678 | -14.59584 | -45.01271 | 2025-09-29 03:19:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 308a4b85-afa6-33d7-a6e0-28f54f609cee | -14.46875 | -42.17127 | 2025-09-29 03:19:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| b7ffbc1b-b353-32d4-8a0d-2d442fac9e0d | -14.4704 | -42.17455 | 2025-09-29 03:19:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 54fb670e-1af5-3391-b555-dc3c1a953156 | -11.8288 | -51.8148 | 2025-09-29 03:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 44224a30-a8d9-32da-a418-f79aadfb8682 | -9.4007 | -54.6984 | 2025-09-29 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9ae4fef6-8266-3d99-aff2-dac2b97f4c9b | -15.2888 | -49.5256 | 2025-09-29 03:20:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 3855116c-7d0c-3b48-bac6-aa539653ab6b | -15.0579 | -42.3424 | 2025-09-29 03:20:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 0a89bec7-a481-3803-9e61-46ff19f6986b | -8.2662 | -45.5018 | 2025-09-29 03:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c037aedd-3de0-3738-9eca-b7fd0cfe2204 | -9.4194 | -54.697 | 2025-09-29 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 92274d98-7c22-348e-be0a-988b9eaf55e7 | -20.0698 | -41.3189 | 2025-09-29 03:20:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 122.4 |
| 875f8177-835c-3355-b641-4410a470b430 | -15.3088 | -49.5004 | 2025-09-29 03:20:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 101.4 |
| e2d21875-5bb4-3757-87d0-425d053eb563 | -0.1012 | -51.2738 | 2025-09-29 03:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 40.6 |
| bc05762b-d5ef-36c3-b40b-217fe966a673 | -11.8294 | -51.7725 | 2025-09-29 03:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 49c27a57-c9f7-3475-bba9-cde6c1815f06 | -15.2893 | -49.5035 | 2025-09-29 03:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 572c4e78-1b74-3e75-85ae-39ac02033f1a | -20.0689 | -41.3449 | 2025-09-29 03:20:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| a09ca794-4141-3351-a820-8fb9de4c6350 | -20.0491 | -41.3251 | 2025-09-29 03:20:00 | GOES-19 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| 6c3ed618-8612-32ab-96fa-3c30cd525957 | -11.3634 | -45.0801 | 2025-09-29 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| e7138d2a-3aed-3113-a3e2-f10c71fe8bac | -3.1013 | -47.0082 | 2025-09-29 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| cad4942c-bbe5-3cef-9bdc-7b16be9b3844 | -11.8482 | -51.7916 | 2025-09-29 03:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 3b6f4fa5-fb54-3e7c-be69-0804e09cd6d0 | -15.0585 | -42.3178 | 2025-09-29 03:20:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 37ebbd1a-5ac8-3459-afbf-6fe90c93e558 | -11.925 | -48.0273 | 2025-09-29 03:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| c9a49643-92db-3a5f-8ece-3041c04117e1 | -2.5772 | -48.4146 | 2025-09-29 03:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 74da9fdd-f1af-3551-a337-7da7d58fd338 | -7.2214 | -44.783 | 2025-09-29 03:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 157.3 |


[Clique aqui para ver as próximas entradas](README8.md)
