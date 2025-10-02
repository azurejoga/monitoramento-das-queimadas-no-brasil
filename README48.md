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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 684caae2-0e16-3571-80f8-0e2f20de326a | -17.94705 | -46.78633 | 2025-10-02 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b486c861-511d-316f-adbb-e284afd2a9ea | -15.63215 | -46.25044 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45641712-1124-34fb-8e9a-a509f38dd5a5 | -17.17469 | -47.02504 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62edd5a2-e554-3987-90ba-58e53e294645 | -13.53284 | -47.25307 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79bfc58b-f821-3a2c-8144-407e42ae7133 | -12.49637 | -50.23957 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15c185fe-dc44-3017-8ebc-eab189fde84a | -13.78546 | -48.05586 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5613a1f9-5db5-3da5-9df9-8667a2518b02 | -13.21619 | -48.44104 | 2025-10-02 04:04:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f47ec96-665a-3933-8d6d-5749dcd09304 | -20.27079 | -44.50298 | 2025-10-02 04:04:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 07f0f1b0-714b-3f64-8d03-6790b3fde961 | -13.80559 | -47.52957 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e0d79d5-afed-3e7a-95d8-7fb6b064c0ac | -15.33859 | -47.94885 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c74de8b1-7494-3da1-8a1a-5d96ef9340eb | -13.17093 | -47.82542 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64d214a6-1f27-3161-bfd3-fabe86becb0e | -13.32195 | -47.81526 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d03d9201-de34-3122-8a16-3c38fa6b6a05 | -18.44807 | -44.49282 | 2025-10-02 04:04:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46fc8585-76b8-3eb7-a59b-598bf17fcdca | -14.42947 | -46.11179 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d69d37be-9adf-372f-9931-8fe8dc120b8a | -13.96283 | -48.13082 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f13e41f9-41cc-32fd-a95e-97df95d3eadd | -13.30936 | -47.83547 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4d48850c-5cf1-3ed3-a1c5-bc89974645f9 | -13.36855 | -46.34002 | 2025-10-02 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b64785ee-184b-33d8-ac12-009db3cd9e5f | -14.61573 | -48.23231 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37bd6fe0-c6b5-330a-983c-219ea6c6d2ab | -14.89873 | -48.32547 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a06443dc-4dc9-35e5-b579-4d12c29ad1d5 | -20.17337 | -46.02245 | 2025-10-02 04:04:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9552b62b-3fdb-3872-aead-ff1fd6f8a740 | -14.41647 | -46.119 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5a2b878-a875-3c5c-ab5c-c05480be38a9 | -13.3175 | -47.00369 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01093b6e-1be4-3016-bf2a-48dca338afe9 | -15.34496 | -46.28938 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3e4111be-8352-3344-865a-c14812119157 | -13.1998 | -47.83822 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83fdadc9-f851-3a83-8b1d-9f07ee7e56b0 | -13.20873 | -48.50671 | 2025-10-02 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 444e6a9d-18a6-3610-9b05-857e4595e79c | -15.50642 | -45.90328 | 2025-10-02 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2efc0ea8-ec9a-309f-a73d-d1156de382fc | -15.1712 | -49.08095 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b78f8561-62f9-3050-aceb-9d7b5093860a | -14.4198 | -46.09983 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| faf93d0f-d6bc-3081-a545-4b21cd0b5e73 | -13.47519 | -47.25296 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fe5aea2-b56d-36c6-b333-09290ba4f0d5 | -18.13143 | -43.99934 | 2025-10-02 04:04:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ced169e-49b7-3d0f-a2e1-42052543b9f3 | -20.03991 | -44.53944 | 2025-10-02 04:04:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6b917dcd-0dc8-3872-a4f8-2127ff6d042b | -13.47357 | -47.23798 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9493b19-00fd-3359-b84b-8f04c0a169b5 | -15.70476 | -40.48775 | 2025-10-02 04:04:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4d54abe2-16ce-3e8f-8cf0-40ff4ee7af8b | -19.04724 | -48.13388 | 2025-10-02 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42bed23b-93ef-3cfd-b748-2cf71d6a8aa9 | -15.40508 | -47.06243 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7213a012-30a7-3481-a1e5-9f9c15d0fe3a | -13.75226 | -48.71374 | 2025-10-02 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f5541b3-2dd0-3f01-adab-a6bcd2f9c643 | -16.01836 | -50.86993 | 2025-10-02 04:04:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d918ee1-ece2-3d56-b724-0b7096ef9bfe | -13.16582 | -47.81825 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7d0350c4-aa8a-35ff-8a18-69aee82d792c | -12.69003 | -48.57259 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79993a73-d84f-3b27-805a-9d8e21a26374 | -15.20707 | -48.16304 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00ac5a65-ce08-3c20-a73d-5c5a431bf1fa | -15.27842 | -46.40475 | 2025-10-02 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea2a1d45-d873-36be-a2d3-9fe421a1f392 | -13.16633 | -47.85028 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51cc2c1e-a199-308f-9830-02deac0a9a59 | -14.88417 | -48.33162 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58d99f97-5baa-3aa8-93f6-82cde2c08d4e | -14.30991 | -45.99306 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ff3b404d-bd2e-3bbf-a33f-8791c6cfe51e | -15.25345 | -49.29777 | 2025-10-02 04:04:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7e967f9a-a9d0-3e9f-8b7e-b0ecf65dbddc | -13.40265 | -47.77567 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16ea5636-407e-335c-9434-545f32bf036a | -13.31177 | -47.82234 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d93835f-8b65-30ec-a188-ca541410ead6 | -15.25817 | -47.91117 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 87474ee7-51d4-3247-b1b1-589ff4ce5ba2 | -15.64524 | -49.25753 | 2025-10-02 04:04:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41600a52-6a5b-3be0-ae1c-67f4b9b27fdf | -15.2309 | -48.08207 | 2025-10-02 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4d61f91-b4f6-3ed4-8e0d-39565862a480 | -13.8243 | -43.06739 | 2025-10-02 04:04:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 55db7732-9a7a-36da-96a1-59e549fd56d5 | -14.41773 | -46.13428 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9931a8e-871e-3ee9-a729-1d59900f3ded | -14.36593 | -45.96254 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 187fe6d2-e2e9-33c4-a712-f25f30b72189 | -12.76314 | -50.55488 | 2025-10-02 04:04:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 47ba0ca5-e8ca-33e3-81db-12a337ee05ca | -13.39062 | -46.94769 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d75d8b9-da77-3411-9e58-c4e59802b493 | -14.3396 | -47.15135 | 2025-10-02 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 966936ca-39e2-3e4d-8de4-03bf3d9b8f28 | -17.17671 | -47.03587 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 28100086-f489-316f-bf14-61c42b7af20a | -14.20983 | -46.12111 | 2025-10-02 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0aae2c1c-1f8d-3e72-bcfc-9150c35a8af9 | -15.66823 | -39.99503 | 2025-10-02 04:04:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bed6cfed-a5a3-37a7-840f-3e4ffc1d6bfd | -15.25891 | -47.90715 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0c6ef3db-7844-3d57-8cba-20fa14549d11 | -18.50804 | -44.03217 | 2025-10-02 04:04:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a56d4702-eae2-3615-a152-3da2d318f6fd | -14.42858 | -46.35616 | 2025-10-02 04:04:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb7044d4-19b9-3549-a886-16f9b1f3dab5 | -13.56795 | -47.27143 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41416ff5-b144-36d1-9857-926f84f4dd81 | -19.28878 | -43.75209 | 2025-10-02 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22703072-f996-3c10-aca1-ad087f11f77b | -19.80596 | -46.50235 | 2025-10-02 04:04:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0432d22d-c0aa-3e0b-90c4-2f09b4b03712 | -16.28995 | -45.24602 | 2025-10-02 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b013cb0-fa23-37eb-8a13-f6bef42d4e05 | -17.11515 | -47.1116 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5203a9b7-e85f-3ddb-aad8-c222130ee9bb | -13.32207 | -47.33228 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7a3d4795-1f2a-33ef-b5df-16d4663439e3 | -13.85929 | -47.95321 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae6dbb9f-8c8f-302c-b440-78584bc20c10 | -14.47869 | -48.43748 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| be4052bd-6ff9-3452-bd15-3161e66509f6 | -16.5835 | -45.12311 | 2025-10-02 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60c0aec2-adf8-3fdd-83c7-c1ddf99dfd9c | -13.17459 | -47.80564 | 2025-10-02 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb45bc16-8e5c-3797-a365-18e74bcce067 | -15.21076 | -48.00249 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 21a23642-c69b-3c1f-89ef-d406dcb67266 | -13.31393 | -47.00314 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3e3c6bdd-0614-31c4-9cc3-268c3b413015 | -20.12707 | -46.35009 | 2025-10-02 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce73dd07-62f2-3f75-ba86-8a54d8bbc061 | -15.54476 | -48.1778 | 2025-10-02 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d6602cb-cf50-36e9-8819-c7cb570d166d | -13.65377 | -47.30569 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ced31d3-5fde-3c44-b49c-e3b9a994df35 | -13.80853 | -47.51342 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3378d428-627e-3963-a631-b63bfb72de68 | -14.49821 | -48.43016 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c016c884-cdb1-381c-a447-c632e0eeb1bb | -15.21914 | -48.00433 | 2025-10-02 04:04:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e31040f-d20b-3cb1-8aa5-ca213cfddf46 | -13.13187 | -47.42004 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa4baac8-0386-3a6c-a215-4b31c32feb21 | -15.55324 | -48.17934 | 2025-10-02 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc6994bd-d56b-3cd8-a56d-f271f701d85f | -12.50167 | -50.25138 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e43f3581-9202-3f32-8d67-bacb90a5c5e4 | -16.00375 | -50.91713 | 2025-10-02 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5ba56fc-377a-36ee-b98e-ad6d39495690 | -13.13022 | -47.40762 | 2025-10-02 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 423eeb71-2c70-3558-ac3a-3c9aa63cc4c2 | -14.02514 | -47.99501 | 2025-10-02 04:04:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d414d870-a49a-385d-9217-e55cfb9b603d | -13.33293 | -47.80378 | 2025-10-02 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cffcd0f-93fc-3da8-aa41-fc1db5d34250 | -13.87055 | -43.60208 | 2025-10-02 04:04:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 350ee8bf-7dfd-35c1-ba38-94bb3704844f | -15.74739 | -43.67847 | 2025-10-02 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbc82935-2c82-3777-a111-cbb5545610ae | -14.42443 | -46.09571 | 2025-10-02 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc864cca-5058-3f20-bf1d-14b0d96d8496 | -12.70543 | -48.5671 | 2025-10-02 04:04:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1bf6ff21-a4ce-3f86-ac4c-ef2c3eb17e7b | -14.30304 | -45.89915 | 2025-10-02 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a69c54b1-2ba3-3434-9098-7079a3b3bb9f | -14.35493 | -43.8432 | 2025-10-02 04:04:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5eedd397-449d-3a24-b050-c81dc460d571 | -12.49578 | -50.24271 | 2025-10-02 04:04:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3477ff4-54e0-3ce1-b751-3a25acd2ccfb | -14.4826 | -48.44067 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6edb449c-992a-3159-8818-c5e2d389f5f2 | -13.32344 | -47.20532 | 2025-10-02 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 89e06981-ec8e-35cd-87ba-588eccda4ef2 | -18.50226 | -44.04667 | 2025-10-02 04:04:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7455591a-4248-37e0-87d5-811b427e0e0c | -13.54228 | -47.24799 | 2025-10-02 04:04:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 35cbb3ff-2b99-3746-a12f-22c05e411ca5 | -14.65686 | -48.26065 | 2025-10-02 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 690dcf78-e348-3c9d-b592-4aa4720dd0cf | -17.17644 | -47.01531 | 2025-10-02 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README49.md)
