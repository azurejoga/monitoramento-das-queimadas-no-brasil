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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c5bdab9-3272-359f-9276-4279598f72a3 | -1.34277 | -51.66716 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8eaf9828-3668-3cb7-8d70-fea198255a9d | -1.10693 | -53.40178 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff30bf56-7de2-3cbd-9274-2499e3fee00c | 1.44727 | -55.92443 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fb98e75-de75-3d93-b24e-7dc6ec189b5d | -2.86335 | -46.83899 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0bcaece3-eda8-3e2e-a808-b87c64e0f994 | -1.68803 | -52.60799 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea532906-f424-303a-a1aa-815bb37f5e1a | -0.99151 | -51.72332 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e501ba7-558b-335f-9deb-ba5426dc3d5f | -1.04418 | -52.42025 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca92a1bc-51ba-3956-b953-d30109b5016e | -1.70184 | -52.62951 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae54e9c3-2269-36e6-a6b3-c86412d3e9b7 | -1.15375 | -53.56654 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c8f107e-1a71-3adb-93f1-fe6704f02636 | -2.87363 | -46.85559 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0717a75f-6cee-32c8-99bc-db4494b89957 | -1.5794 | -52.26718 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9f64eb30-cbbe-3664-a16f-6287680419be | -1.62649 | -52.46941 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e64dfd2d-2f0f-31b1-ab54-4039818e2d75 | 0.98661 | -50.12519 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 98b74238-9fce-3608-b625-74ffb4771d0b | -1.66831 | -52.7394 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d995f769-872c-308e-b37c-acffd652ee65 | -1.44594 | -52.59618 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd0984fe-0ca0-37de-bb17-1e6639b20f0e | -1.62031 | -53.32827 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 524757b8-952a-3f6b-baf2-11b504730aa8 | -2.85564 | -46.8478 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72a062fc-7a31-3ed1-be19-eb322f13015f | -1.79974 | -52.75477 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 304eede9-2e7b-3c61-ac08-54aaf628e564 | -0.58876 | -51.70216 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95ac201b-3f29-351b-a230-d95b134afd1e | -1.46764 | -52.69035 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 460fa707-2895-3876-b410-df60fa41257b | -1.31459 | -51.73319 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a6d6152-05d4-328a-ad6b-49fb494edcd4 | -2.84794 | -46.85654 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26f7111d-4395-353d-8705-c22b658235fd | -1.10369 | -54.146 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 084568c4-e705-3e58-b322-27be28f917c6 | -0.87496 | -51.72016 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f536f901-e4fb-3db1-9df4-33f8e26c8cc2 | -1.16425 | -53.67737 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79832d02-f822-323a-a19a-e13e8323bedc | -1.35547 | -54.63498 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed8771c0-710c-32c1-935a-5d3143133719 | -0.99589 | -51.72401 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6228f5eb-9521-3f2b-95f0-f3eccb48b1bb | -1.10483 | -53.38951 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8c736476-22db-3978-9cdf-d81e038fb96c | -1.49642 | -52.44278 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 628cb024-53a5-30ed-895f-a19f4518b8d4 | -1.64822 | -52.73248 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 606c9242-627d-3cfd-96af-321ce0807fc8 | 1.45064 | -55.9239 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bb1d629-a180-32e0-94e6-adbcd1446a7e | -1.90114 | -50.58564 | 2024-11-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8f37ebd-43b4-3350-867d-b63e2f55407f | -1.3067 | -55.74298 | 2024-11-28 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96d52ee2-6f76-3b27-9330-7d3770971fad | -1.42967 | -55.24665 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8af62248-e140-34c0-b784-27e60339b172 | -1.62522 | -53.8753 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c44e33aa-07e5-324c-befa-c85106e78678 | -1.62857 | -52.37014 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e04ed451-27fa-3dc3-a3a6-565716158187 | -1.04478 | -52.41644 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fb212e3-2485-36a1-ae70-4c2fb95a2a55 | 2.08782 | -50.62475 | 2024-11-28 05:16:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f819c45d-4960-3436-b672-a97380815d1c | -2.53287 | -47.32747 | 2024-11-28 05:16:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 619ac299-0582-3e90-880b-80ee07b922f3 | -1.39244 | -54.99769 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b4770242-9386-3bec-b50a-31f659604d18 | -1.1622 | -53.51186 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22c8c79d-70fa-3266-acc5-9b6b12bd78c1 | -1.45661 | -54.53849 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 406c32e0-2d0c-3cb6-879a-357609282373 | -2.86594 | -46.85209 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f545ca58-76e6-3efd-a0fa-7d2c996a7ae1 | 0.98693 | -50.25994 | 2024-11-28 05:16:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0533cb84-1f6e-307a-969a-2df613c7e381 | -1.31666 | -51.92317 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f6d08bf5-c70f-3e43-91e7-c421fa2fb45f | -1.21709 | -54.18936 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28be3cc6-a838-33c3-8d2f-a57c4340bb00 | -1.64265 | -55.22795 | 2024-11-28 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d3982fd2-6b67-35fb-8aa0-114af5fbc856 | -1.058 | -52.42221 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6dfa372c-d2d9-3b02-bede-d1b5e4e20f4e | -1.47398 | -51.54644 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 079e5c89-f07c-39d6-8fc9-a2afad82ff1b | -1.15998 | -53.57764 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| adf1c0f3-35e2-3ec4-8aee-b5f218f0e9a5 | -1.35306 | -51.98614 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9813bf39-3709-3572-9fd0-fa1832e32a80 | -1.61161 | -52.62337 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 8db1dbe4-05a2-3884-8a77-cc0e4a1b6bfb | -2.84726 | -46.84877 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39950536-d626-3f01-bfc7-2b12ec33b6aa | -0.59246 | -51.70704 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f25529d7-1814-33c0-b806-e01eb359dc45 | -1.66887 | -52.73568 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 82bd3823-cd6b-3bba-b7cc-32333f7fabd8 | -2.8626 | -46.84397 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d20d4288-3580-3a2d-9db8-c9034af4625d | -1.11508 | -52.30093 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de3a8bb2-b51b-3ffd-80ec-008e352e73dc | -2.80719 | -46.82979 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5be548b3-eb74-3ef5-80e4-d04cc3fc850a | 0.94285 | -50.7356 | 2024-11-28 05:16:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d0193b0-085c-3e8f-98f2-7216c9f4272b | -1.33563 | -52.44315 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cff1b99-b04c-38d2-ad1e-c9eb2b35a837 | -2.43976 | -48.24173 | 2024-11-28 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 75dc7601-3978-3757-99bc-13dbbd9a3f07 | 3.81636 | -59.60145 | 2024-11-28 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 146e18e5-1286-3701-8d54-844e9da8c100 | -1.35973 | -54.65621 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47e2c1e3-b797-36b5-86a7-afc12b9906d7 | -1.04814 | -51.73857 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a1604ed-cae8-32bb-90c4-5abb2162b313 | 1.3141 | -60.4122 | 2024-11-28 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fde3ea3b-f719-3a42-a638-2f1a825cdbad | 1.44 | -55.89983 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7bf2c19-b76a-3aa3-96e8-770fe0a832e6 | -1.35415 | -52.5439 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87928596-637b-316b-84f3-8eda58b48ca7 | -1.06811 | -51.75465 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a66abbd5-7477-3753-9bab-eb088467c7ec | -2.8549 | -46.83998 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ce2b1c1-21a5-3951-bc37-5a6fb510b1c6 | -2.15691 | -48.71327 | 2024-11-28 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2d58c2bf-2d1a-311f-b06a-170abae919c7 | -1.28822 | -51.72903 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 03cbaf31-496c-34c3-9522-8122116ea09d | -1.49852 | -54.46386 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 986d1066-9bbc-3586-b524-8c74424249d4 | -1.10325 | -53.39963 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8300c42e-272a-38a9-a588-77d17ebb80d4 | -1.28384 | -52.10645 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89769f88-c380-3a02-ac47-060f03f4f1a2 | -1.6528 | -52.40993 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6c514b7-5543-3e58-bb1a-725369c18aa0 | -1.10218 | -54.14759 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc235389-d6e2-3d5c-9b16-d2ccc553162f | -1.33327 | -51.94069 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 837f4ffa-9786-3c5b-973c-63ca9d99779d | -1.35246 | -51.96067 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de0a0bba-fca7-3cc3-a80a-ab94b4e5a00f | -1.80959 | -53.58675 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5238b98-48c1-3eb0-8a55-bc8e671e88d8 | -1.68746 | -52.61177 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44307ce8-432f-3528-b7d2-1342d30b70c7 | -1.34874 | -51.98546 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8efbe3fa-ee43-3ca8-bd3f-008eab11f67f | -1.7956 | -52.75413 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 631f0749-c080-33ce-bf51-043ba0593971 | -1.79786 | -52.73923 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7dcfb7e7-6573-3f4f-9eb3-d08b403b4867 | -1.89931 | -53.03106 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6e32cf1-78b4-384e-b338-c219483b5db0 | -2.15743 | -48.70968 | 2024-11-28 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 867784f7-f167-3b27-94a1-b1f02408d8b2 | -1.33204 | -51.94898 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| efd5b8af-ca83-30db-890d-b4ec241e1fcd | -2.86885 | -46.8449 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af20c8e9-09b4-3fda-b47f-6422801b2f28 | -1.08679 | -53.37637 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c5397abd-c706-333e-a7a9-94cd05c03404 | -2.87062 | -46.87546 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f2ec463c-257c-35c6-8bb1-f2fe234049e0 | -1.55482 | -53.51966 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4bf1422f-9a9c-3837-a85f-08a592c576f8 | -2.8714 | -46.87033 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c7184f96-332e-3866-b5dd-0963f1d10778 | -1.31557 | -52.87001 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c844b873-639b-38a8-9bc4-314e4d9f4fd8 | 0.33268 | -51.07437 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7158aaa7-1589-3814-9759-781a27105642 | -1.66401 | -55.23128 | 2024-11-28 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e49a489-1dea-3b79-8107-5e1f14487633 | -1.30954 | -51.73678 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26b50f08-e8b5-3222-bc65-c0db451a5801 | -1.62211 | -53.86995 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d6ddddd-19f6-3bff-926c-50f17c290228 | -1.3044 | -55.73483 | 2024-11-28 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da8834ff-7e38-3bfa-a173-e4ceee704f5b | -0.45758 | -52.01651 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8d1ca153-abbb-3ab3-a462-fc3a1ec80049 | -1.63439 | -53.86671 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a164e7ea-87e4-3b06-98db-e56b7a79cff6 | -1.27878 | -52.1673 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README79.md)
