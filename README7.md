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
| 1b12803e-e07e-3d98-9836-ecf8bdf88116 | 1.55245 | -60.28598 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15ceb37c-3fd0-3071-a7d1-e4d33d7842b4 | 3.45638 | -60.28712 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9f88ae8-87a2-31e0-a887-87a1dfc9dd89 | 2.32046 | -60.38513 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 01f4312c-47a6-3659-b85f-fe2a3f01df6c | 2.52379 | -60.8102 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 80364496-87dd-3fe1-839c-2ee43abf00a4 | 3.48866 | -60.77945 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35d9219d-32c6-3654-a639-9f4dc8e0637f | 3.15142 | -59.90391 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ab0c757-6a04-36c1-9d00-db228e936e74 | 1.48394 | -59.93519 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62d125c1-d3be-3a6b-b508-42a6a106e2c4 | 2.61869 | -60.61173 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f205ce32-83d4-3e1a-b729-b16a72c27de2 | 0.99912 | -59.60005 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10305f61-504f-3073-883e-199fa0890fda | 1.4834 | -59.93176 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9143e18a-b476-34ea-9fe6-db5a44c66d33 | 1.03191 | -59.46277 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47053763-6d16-38ad-a528-5a206daec723 | 1.16476 | -60.37134 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b5e488a-e948-3ff3-be91-d9ab4d49f022 | 2.22076 | -60.74517 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7affc1f5-77cc-37ab-8226-236f46338c3a | 1.5098 | -59.92765 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 376ad9b9-3ca5-3b6e-bc44-17e25370af61 | 3.16344 | -59.91606 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2d3d979b-3807-3315-82f8-2ed388051dee | 1.06436 | -59.2558 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bde66b81-0e18-3f51-8c58-b343fc7ac3c2 | 3.16069 | -59.91999 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8de018ef-b848-353d-a805-269a08f7fdd3 | 0.07729 | -60.64752 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a3d9c21-1c5c-3884-b905-f05d054d9d32 | 1.49828 | -59.91886 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 7f2b361a-9877-3fb4-9057-f6090ba0748c | 1.0075 | -59.48089 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2a295d99-6137-3463-ac7a-429d38b5be1b | 1.20391 | -60.62087 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7921cad2-52a2-3115-8593-7fbd91029363 | 1.36267 | -60.30845 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25c97568-492c-394f-83ca-036f7bd857ef | 2.37298 | -61.43621 | 2026-03-01 05:29:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 354af16a-2826-3772-935d-96342c766338 | 3.49143 | -60.77547 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf7d2088-50b6-36ef-a911-82b631df1785 | 2.25619 | -60.1044 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ca9ecfd-516a-3ec9-932c-af8dcf68e5b0 | 4.24653 | -60.8145 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44120b58-ba77-3661-aa5d-71647bf47d18 | 0.8536 | -60.40641 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ff2a11c-fbd2-3563-ad14-2145e271b02e | 3.31349 | -59.89905 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b3552a7-aff1-3368-a249-befa5a5881ee | 1.48064 | -59.9357 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaf93b44-f019-3a7a-8be7-6b8a92cac0e0 | 1.36649 | -60.31136 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69c6fdd6-b7ad-385c-baf1-da6f96a4f1a5 | 2.74802 | -60.743 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9fbbb54-30c8-3e22-a9d3-544dfb88456c | 4.24485 | -60.82549 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 164c275e-fb1c-3aeb-80cf-001e5c8a2700 | 1.86468 | -60.40828 | 2026-03-01 05:29:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac2cede9-5c5f-3aaa-9e35-479111014f00 | 3.48312 | -60.7874 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bd15f8f-177c-38e2-9bf6-287d22743a2e | 1.08377 | -59.25246 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ddf3e4f2-0224-381a-a937-0e61ff8786ab | 0.85636 | -60.40248 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8410105f-3bf1-327b-81ae-361230effea9 | 1.50757 | -59.93503 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17b13115-459e-3578-b8c0-f881c93e40da | 1.47404 | -59.93671 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf96f555-70b3-3b52-a496-38b79a9d83f7 | 1.20747 | -59.97105 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7085053-6587-35f5-bac7-01cbb16ad970 | 1.02072 | -59.80294 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3130f32f-cc81-336e-aa09-fa1f97a38b16 | 0.85418 | -60.23809 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44c0a42b-4296-3da6-9cf5-739566c58580 | 3.95294 | -60.22312 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5f686a0-50b9-30d6-bdd8-d63a0d08f3c5 | 1.47902 | -59.92539 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7ac27248-113c-3abd-b775-31758d9f5aae | 3.46428 | -60.8187 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3021305a-6abe-3e9c-9129-24a48e7331c4 | 3.44224 | -60.80786 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ddde0b-c513-3125-8201-2306630aff35 | 4.149 | -60.71171 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a9270e0-8fa5-3b2e-97d4-99b0a26085aa | 0.70377 | -60.27537 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d282b2d9-092f-3fc0-aa1e-b14a8ae15456 | 3.16129 | -59.90238 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebc78eea-b34c-355c-a7d2-d62abc9e324f | 0.07783 | -60.65094 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad2b7e25-7438-3f9f-85e9-30255343ce34 | 3.15518 | -59.92786 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44e9fa7c-3e7f-3eea-97e6-902d7771e5fc | 3.31624 | -59.89512 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3d63a5f-47ec-373b-a202-5764b1f9af37 | 4.29289 | -60.06339 | 2026-03-01 05:29:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a113491f-7ed2-3cf2-aedc-2b06c248786c | 1.50865 | -59.9419 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4153f42-fa67-39e2-a614-e62fcc1fbd40 | 3.45049 | -60.81726 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d231dab-6478-3056-a50c-62fb62713c65 | 1.49444 | -59.91593 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 004e8954-8e38-31ce-a28c-58b68afa1b07 | 3.99856 | -60.1205 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb3b8660-e950-396a-b055-14df0abba033 | 1.05767 | -59.25684 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0bc5f6d-0177-3fb5-a666-683c4ec3165e | 1.47242 | -59.92639 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c7bff2e0-2e34-345a-8394-5175671e77c4 | 1.49168 | -59.91988 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2b9a0e87-9528-3c07-bc48-cb38ade57d5e | 4.06511 | -59.89262 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ab87aaf-883b-3be3-903b-87d88cc8f9c4 | 3.65483 | -60.64381 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bf30728-8066-3cbd-bb11-e545de3845a9 | 1.02914 | -59.4668 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e9b89cd-244c-3d03-aa88-0bad9ae056d2 | 1.55575 | -60.28547 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 63feba13-92b6-3210-acef-5ecb4f613a41 | 1.02403 | -59.80243 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72dd19b4-297b-3794-95e1-c7c77dbf7ed4 | 3.9899 | -60.08675 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f4d3463-d845-33cb-b05a-4dcaa37c3073 | 1.47848 | -59.92194 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2b7197b5-f208-371c-9dbc-607c5558f304 | 4.09036 | -59.88169 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c986686d-8356-30cd-b1eb-2e91940dc7e2 | 3.51148 | -61.90955 | 2026-03-01 05:29:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00e05e7b-daaa-30a1-a09a-d7cd81a457c8 | 2.90966 | -60.42594 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5c9915f-de57-3114-a73b-ad70d57d0dcb | 0.99967 | -59.60353 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1230b7c2-3dd1-3758-8907-cb9dbb892083 | 3.31678 | -59.89854 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e88987a7-0370-3deb-b0fd-cb2c35405c0e | 1.87587 | -60.91552 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 221a8113-5a47-38fe-9a8c-717cd654f953 | 0.63319 | -60.28284 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13ea1fac-e56a-30bd-8a57-004ca8fb10ec | 0.64717 | -60.37188 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac5caa25-ccd0-3abc-9c31-e7067e40da97 | 1.48784 | -59.91695 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 15962587-322e-3ae9-9d1e-6e1bd6c42eac | 3.44941 | -60.81032 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34474892-fe02-312e-be05-30594b9c4328 | 1.29224 | -60.42452 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ea860c9-4853-3efb-88ef-da3dce124d10 | 4.24599 | -60.811 | 2026-03-01 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33b80be5-e632-364c-ba1e-1189b3cbed84 | 0.19563 | -60.44331 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dacb9a31-b4ed-3800-b426-3c37a1025ab1 | 0.19287 | -60.44724 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a68ec66-1f71-3f51-8ca2-710621d21183 | 0.89283 | -59.7907 | 2026-03-01 05:29:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9bf64de0-0f35-3d74-a5e9-298de5ba9bfb | 1.50427 | -59.93555 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1123133b-5941-342b-85a3-dd0b71a03c4f | 0.47358 | -60.3961 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bce97e2f-6b4b-3267-9a4e-aaf438172ad2 | 1.27693 | -60.41288 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7363b712-d80d-3844-aafc-ccc17333c82c | 3.99043 | -60.09017 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69262136-e33e-3ccc-bbff-13a923692b74 | 1.2917 | -60.4211 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c849eedd-c8b5-376a-b730-ae825fecb4f1 | 1.33551 | -60.59288 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac63652b-1ad8-394c-9186-edc06ac12b89 | 4.09748 | -59.88409 | 2026-03-01 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dce3ad39-185c-3793-a980-71e6b638fed8 | 1.50481 | -59.93898 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c6a5386-bb5f-37de-9d98-fb327ba34318 | 0.19616 | -60.44673 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e6b8ba3-354a-385b-ba50-2371f0fe0272 | 3.39412 | -60.21959 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 540f37be-b8af-3b17-9b83-15bea3049760 | 3.16398 | -59.91948 | 2026-03-01 05:29:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc65625a-a560-348a-afe3-d4d5c9116baa | 1.4867 | -59.93124 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 448d26ae-39ee-350f-acf0-bbba5b8f944f | 3.45272 | -60.80981 | 2026-03-01 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23d00221-0432-3687-8df0-9d22b4439940 | 0.6299 | -60.28339 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54b3e3f0-975d-301d-84d2-de8d3fcf5edc | 0.18904 | -60.44432 | 2026-03-01 05:29:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a6fc0ed-e4ca-3149-9cc7-e4b9594c6240 | 1.11386 | -59.20429 | 2026-03-01 05:29:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3728665b-c50e-3510-a1b8-865f3ee01d80 | 1.4972 | -59.91199 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 8d360238-60b6-3aec-9c72-41dbd19fdb00 | 1.50266 | -59.92524 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75d5a383-46e0-370a-bcfd-1a48a755db08 | 1.4933 | -59.93021 | 2026-03-01 05:29:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
