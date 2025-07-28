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
| ace013d8-b84d-337a-aaf1-6bb0d6f00e3f | -13.52711 | -46.29432 | 2025-07-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 262587a6-12cd-3ff1-8443-c104ff6a3e64 | -14.49018 | -48.65033 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95ed361b-d350-3e1f-864d-2f3387bbd259 | -14.48878 | -46.536 | 2025-07-28 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9a2a503f-c70b-37ae-819e-bf11391c0bb8 | -13.13086 | -47.34194 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ab73480-c458-3b8e-8c0a-772c1316d16c | -13.49946 | -45.57693 | 2025-07-28 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ea37d335-6cd5-3437-8563-c7fb5bb3d493 | -17.36213 | -42.63715 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 37a9ca44-b0bd-3ab5-b9fe-725958d4b41f | -13.52282 | -46.29193 | 2025-07-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff24ebff-8a6c-3e6f-99d1-a717cef922e5 | -4.15666 | -46.81247 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 03a8c135-ebd9-3b4a-bf9f-9469d35a81af | -17.53482 | -43.92174 | 2025-07-28 03:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 508b88c0-c4cc-3c88-b2c7-4bf03bff1ed2 | -13.12871 | -47.35283 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f44a1d6-7c48-3857-90d2-9c1bddba2028 | -14.49169 | -48.64267 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4204cc26-35d5-31b6-89c2-d4286ea4cca2 | -12.66805 | -47.01466 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd110102-1ef5-31a9-a180-ca1c11e244b0 | -10.84468 | -46.67825 | 2025-07-28 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3426bd0e-9a87-3208-abb0-773b2ec4e66f | -6.41236 | -41.13967 | 2025-07-28 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f8a7b230-154c-3bb1-a9f6-a2dfc40a82bc | -6.01581 | -44.06792 | 2025-07-28 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb0d0161-27ac-3522-bff3-45a4badabd8b | -11.97918 | -46.70155 | 2025-07-28 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f407ab32-dcc2-39b6-a7e4-ffc1313ead86 | -12.74393 | -44.73735 | 2025-07-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b33e6404-02f3-3353-8d5a-f17e0a2f4e46 | -13.50677 | -45.58825 | 2025-07-28 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e16c120-72f3-3980-81ec-e4d76ed9df41 | -13.29245 | -40.97856 | 2025-07-28 03:49:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7cab10f4-3f86-34c7-9a44-1b565a977990 | -12.66718 | -46.99197 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c0e4a6c-cd75-331b-991b-1134c80c1e36 | -4.16174 | -46.81882 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 3718dc4a-2242-3af7-b5ef-5b797a8bf5fe | -13.11322 | -47.37718 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab6a09ef-0e44-35df-92d1-cd3d155d84ab | -4.15075 | -46.81321 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 603d5808-bce1-3208-888b-13377546275d | -5.6806 | -43.66804 | 2025-07-28 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6814fc21-7e0e-384f-bfb2-69d369ac742a | -5.85737 | -44.23726 | 2025-07-28 03:49:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca7faa7b-ad2d-3c70-adc1-e193249c0b57 | -3.29529 | -49.1923 | 2025-07-28 03:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3d2c98b-487a-3fa3-ac0a-a0cdc8287f22 | -14.49487 | -48.65536 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e869b4f-6686-33cf-b65c-4ce3d66171c2 | -4.15597 | -46.81638 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9810f078-af9e-353d-a0e6-af6eb2a52f20 | -16.60634 | -47.82394 | 2025-07-28 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b21e99c6-cc52-37aa-a6e3-b1be234c8f1f | -6.21044 | -38.52467 | 2025-07-28 03:49:00 | NOAA-20 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d6c25460-a10a-3dca-880e-054489d873ba | -14.39116 | -43.77213 | 2025-07-28 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af5d5ba6-5dd0-3d27-80a9-eee264f9e5b1 | -13.10323 | -47.31074 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 127e5f75-5c8e-3c57-babd-948d60340edc | -12.66666 | -46.99464 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3942be73-bcb5-39ba-99ea-67d07de89e18 | -13.10746 | -47.37264 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e48b9f4f-c6b2-388f-a906-b3a1fb1ae6d4 | -6.39689 | -42.83299 | 2025-07-28 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fefdc36f-3f15-393f-baad-8771538d8b7b | -14.22151 | -43.94805 | 2025-07-28 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e1bb3b5-204c-3286-86bc-c26bfdfb934a | -4.16178 | -46.81728 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 0c40e18a-1e13-3e51-b75c-e7f5c3d50fb8 | -17.53569 | -43.91688 | 2025-07-28 03:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bf8abcb-8cb6-310a-bb3f-b2d4ccadaac5 | -15.41766 | -39.39418 | 2025-07-28 03:49:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 62930814-33d7-3ae3-85e9-111af9e4429a | -6.43945 | -41.88686 | 2025-07-28 03:49:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f2405c79-c528-366e-8071-eff10af256e9 | -14.87907 | -48.39843 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8e7731a-bbd3-3cd6-bdf2-59decfb2a0cb | -5.74473 | -43.9791 | 2025-07-28 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f498f69-5630-3b22-a0f9-b3041af054d5 | -17.35708 | -42.64506 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f781aa98-fea2-31a0-953c-c6f3c23c770f | -5.0696 | -37.71615 | 2025-07-28 03:49:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 58aa287b-327a-3b66-bbd3-d942a8979e14 | -4.16615 | -46.82646 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| cb0a888e-1ecb-335d-ad43-301bb693facb | -5.00357 | -42.29604 | 2025-07-28 03:49:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 94d7aa00-f99c-39c8-8ac7-dc308ae93f00 | -12.68536 | -47.03429 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 139e5c56-0551-3d7c-834d-8794d111e3a8 | -12.691 | -47.03233 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 490d9715-79e6-39e3-aaa9-14fbbe871b1a | -6.21265 | -43.75069 | 2025-07-28 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f8018af9-1e36-3745-8707-8e330c3f6d03 | -14.49149 | -46.54753 | 2025-07-28 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 056e59f8-f4ef-3fd1-937f-4ab5e584ce42 | -17.35961 | -42.63979 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ddacc670-8123-3007-b28f-88a3c4b8d145 | -14.87302 | -48.40089 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f759cf5-5731-3aec-ab2a-13d63da92bcf | -4.15013 | -46.81562 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 79323ce6-1c41-331d-97b3-70f91ade1ac2 | -6.57097 | -41.5099 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3310e41c-1492-3217-820a-dc67e7a9d8bb | -6.56535 | -41.5193 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 971076b2-51d9-3ee1-9156-127aae75b237 | -6.37406 | -42.63491 | 2025-07-28 03:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3d3fed03-ad98-3dcd-af09-eef7799380a6 | -12.74546 | -44.73134 | 2025-07-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a998bad-95f1-3742-a148-aa9a4031f19c | -4.59802 | -43.30491 | 2025-07-28 03:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 651410fb-4af4-30a2-bddf-48b2a17d9de5 | -11.98362 | -46.70565 | 2025-07-28 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9071eda4-a3fd-3bad-8b26-72a606e3a0bf | -13.10866 | -47.37312 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31999ac8-6a01-3a63-8e86-bc9e1144d185 | -10.54616 | -49.49221 | 2025-07-28 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0bc5243b-9f49-343a-8c0c-fbd0b8e019da | -4.16241 | -46.81487 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 27.2 |
| fe30fb45-4bac-3b99-9d35-7268c394b74e | -16.60608 | -47.82505 | 2025-07-28 03:49:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e3f84abd-49a3-346f-847a-a41fe78be948 | -10.54684 | -49.49561 | 2025-07-28 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cab82acb-7bf6-312f-b17a-8f0aa4eee2e9 | -6.42303 | -41.14639 | 2025-07-28 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8be3e6d2-f305-3d67-9c90-72b4400d1458 | -12.68601 | -47.03089 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd80727f-bc44-359f-bcf2-55b278b9cf41 | -5.87544 | -39.76283 | 2025-07-28 03:49:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7a3b175b-6b43-3f06-9208-54e9178999bc | -13.52608 | -46.29967 | 2025-07-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3248803f-c529-38bc-9f7b-3c107a75b0f9 | -6.41732 | -41.14322 | 2025-07-28 03:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4aa6f2ea-63e2-36c6-bef0-349d2d0648a1 | -5.8668 | -44.23927 | 2025-07-28 03:49:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 776ca8ec-6c06-3e99-9da7-abeb81b67f37 | -16.32356 | -43.61725 | 2025-07-28 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f37268b-e77f-3582-a3da-e972724b099a | -13.07071 | -47.36892 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d76ce167-2cf8-3953-a951-09000d0aafe4 | -6.25699 | -42.8372 | 2025-07-28 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 93d4afd5-f108-3560-a4fd-d71b999f107d | -4.11033 | -47.93924 | 2025-07-28 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b517385d-43f3-3f11-8964-21331c362463 | -10.45281 | -46.51294 | 2025-07-28 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bab90f04-599d-3c48-bfc2-f0628a46c148 | -5.8743 | -39.76179 | 2025-07-28 03:49:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cb0860d6-49c6-3af1-9fcc-21af436895a3 | -13.10934 | -47.36971 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6895eb9f-b356-3fec-87cb-bd63f8373a6b | -4.10491 | -47.93354 | 2025-07-28 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 458af090-90eb-364b-ae8c-dc7c8404e6ef | -6.11994 | -43.1613 | 2025-07-28 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b32e8620-366b-3dd4-9048-c7b5cf8c62a5 | -5.78611 | -43.6024 | 2025-07-28 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1ae15bf-5691-3748-b9f4-a4004548bf5a | -13.11701 | -47.37872 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a20359e-6f0f-30d8-bec5-253d0ec57e11 | -5.74269 | -43.96306 | 2025-07-28 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5a1d67c-b732-33c9-a8a7-c8dad4715833 | -12.7161 | -47.01115 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22b5f601-333f-3da7-aa79-ded8d39bfb84 | -5.74856 | -43.98479 | 2025-07-28 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3550706c-40e1-392e-8f69-43eb0e897d29 | -17.35886 | -42.64406 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 959ef66e-0dda-3585-83c0-e2ec63392783 | -12.6712 | -46.99835 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9623ca2-c321-3413-9644-4caa18dcc493 | -17.35781 | -42.64079 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 060f8ae5-aacf-3d7a-9910-4f8d83de2572 | -17.36066 | -42.64575 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0b2d2fda-bc56-3106-9386-9c5bce307db9 | -12.66109 | -47.02343 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 079ddcb3-3c1d-3517-813b-31003ac1772e | -4.11281 | -47.92502 | 2025-07-28 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12af4532-a14e-3826-aa77-d199b6039a3c | -14.5015 | -48.65327 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 590bbc2a-28a2-39d7-a327-18953ad08ad6 | -14.49216 | -48.64338 | 2025-07-28 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbcbe899-7dcb-36f5-8691-ffd1f3420f9f | -12.74031 | -44.73481 | 2025-07-28 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79b9bb89-cd0d-3f07-a628-5e468941060b | -17.3581 | -42.64835 | 2025-07-28 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1de4c4da-2077-39fa-a271-25bc8e2d5b76 | -13.52182 | -46.2973 | 2025-07-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90d3e585-b3fa-34ad-913a-0568d2e9aa75 | -14.97963 | -46.96135 | 2025-07-28 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a53aba2-3465-39ba-b8e6-21fae6f64551 | -4.16751 | -46.81871 | 2025-07-28 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 1ed8faf1-14f8-3230-96bb-488dc6939ace | -12.1913 | -41.57338 | 2025-07-28 03:49:00 | NOAA-20 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bc6e3a1b-140f-3f26-90bf-5b88dc65ecee | -13.07174 | -47.36358 | 2025-07-28 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6868a14e-5baf-3e56-a1d9-c9b00d916dba | -14.49252 | -46.54221 | 2025-07-28 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |


[Clique aqui para ver as próximas entradas](README8.md)
