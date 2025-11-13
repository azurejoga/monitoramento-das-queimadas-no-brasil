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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34758383-0d06-34c3-b18f-a92052c320d8 | -9.32414 | -47.84291 | 2025-11-13 05:03:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36599718-46e3-3c10-b348-d38307e97d0d | -4.21179 | -48.57463 | 2025-11-13 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e4936e91-dc4e-3b80-9a27-17e89521b648 | -4.71993 | -49.24434 | 2025-11-13 05:03:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c162df5f-810e-3186-8a34-7535337ea2a2 | -10.63012 | -45.25161 | 2025-11-13 05:03:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14f69c63-8756-36c9-8a37-adaf14358293 | -8.86755 | -50.19647 | 2025-11-13 05:03:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c594e1c-b1b4-3436-b545-696999d80218 | -8.86321 | -50.1958 | 2025-11-13 05:03:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d6b5f39-57b7-3c8f-9651-90959ee4fdd0 | -7.78108 | -43.79959 | 2025-11-13 05:03:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8633f2bc-ff22-32bb-8ad6-1eec22b231bc | -9.63068 | -44.55052 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c4aeed13-b5de-35d7-8c3c-21d709ebb13b | -3.30495 | -53.71021 | 2025-11-13 05:03:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5068ede6-e638-322f-9604-cae7d8d19da5 | -9.32458 | -47.83976 | 2025-11-13 05:03:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c0eda65-7cd4-308b-8e7b-e092935e10e5 | -7.10087 | -42.37355 | 2025-11-13 05:03:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a5f874db-b15b-3475-9a11-9e842b1f1c4b | -9.01766 | -45.4324 | 2025-11-13 05:03:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d423951d-bb48-3add-923e-5fa24cc283c9 | -4.71525 | -46.45067 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8a21329c-6485-3525-aa62-dd1a8ac77602 | -3.894 | -52.1209 | 2025-11-13 05:03:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1497b901-0ccd-306b-ba29-f30292a8f738 | -4.71125 | -46.44405 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f806951c-2833-36f2-87d0-08766ed880e0 | -5.32391 | -45.19989 | 2025-11-13 05:03:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 30965a9b-bb37-3d69-b98e-4aa57e481262 | -4.24663 | -49.67735 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4d6db52-3310-3d9a-8da9-fdbe53e83eac | -4.10678 | -48.02154 | 2025-11-13 05:03:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a34184a0-fecb-3bab-9ef2-ce6c576bd596 | -9.01106 | -45.43637 | 2025-11-13 05:03:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9d3fbf2-f2fb-30ef-b0f9-77d9d773415a | -4.56513 | -48.49699 | 2025-11-13 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac6b1585-d34f-3aba-85d2-f967a356a6e4 | -4.3078 | -48.24507 | 2025-11-13 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3896ddd2-058f-3b15-8473-da2587c01203 | -4.52977 | -46.43708 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 34164c93-2465-3a4e-b433-aebeccf6bf3b | -5.85147 | -46.45041 | 2025-11-13 05:03:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c9d11ca-fd50-3013-bc10-f77d888e6ae5 | -4.00633 | -48.81096 | 2025-11-13 05:03:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e848d2f3-b5d5-3aa6-b4f4-a00c14a513c7 | -3.49995 | -52.95316 | 2025-11-13 05:03:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a21c1fa5-87fa-3691-b68f-61666590974a | -4.7537 | -48.83335 | 2025-11-13 05:03:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b510b7fc-c9d5-3a66-93f7-97793f628245 | -3.87175 | -52.2182 | 2025-11-13 05:03:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e475a05a-0057-3309-862f-c89526b0cf73 | -4.10826 | -48.01168 | 2025-11-13 05:03:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d69e3c2b-40f7-392a-b1f8-89e579428d6e | -3.85596 | -49.79597 | 2025-11-13 05:03:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c2c7acc-1e49-3557-92a6-8edd88c1efa5 | -9.01051 | -45.4408 | 2025-11-13 05:03:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 610652ea-fbed-30e0-8bb8-f527cb749d2a | -3.85953 | -49.8003 | 2025-11-13 05:03:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d563694e-a2c0-3f16-b0ad-cbe7217f88f4 | -9.6313 | -44.54535 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5045aff6-2d5a-3498-9879-dd55a8bb233e | -4.20553 | -50.09452 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c9d0be5-afab-3844-8eb5-a212ee5a32ea | -3.87237 | -52.21414 | 2025-11-13 05:03:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f9dde4c-bdcd-359d-909a-7921feb7916e | -4.84252 | -49.26444 | 2025-11-13 05:03:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc64de20-a1a5-3b69-b142-18cf7e8f2602 | -4.71571 | -46.44746 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 06a78b9b-f934-3589-b4c6-5064f30aa6e5 | -9.6356 | -44.54625 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e289699e-ee94-3010-8ec9-a4bd3b05a88e | -4.69493 | -49.65456 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69c24bab-efd7-375b-95ce-cf2c03433cd6 | -6.14162 | -48.05405 | 2025-11-13 05:03:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 515046c9-faf0-3b9f-8ceb-4363d5e5f86c | -7.78034 | -43.80529 | 2025-11-13 05:03:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb7d9beb-2bd1-392f-acb3-6cc3fa25ca3e | -4.71174 | -46.4408 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 87d21fee-ce62-3294-8f03-d9b13b602d0c | -5.57667 | -47.10425 | 2025-11-13 05:03:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| bf3f4e41-b15e-364a-a154-cf90c8663835 | -4.71044 | -46.44661 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 92c5dbc7-bc95-3641-b8db-f861167d9955 | -4.71077 | -46.44728 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 5a3a2c0e-f311-3214-803c-35f8f1b91f79 | -4.45316 | -46.55545 | 2025-11-13 05:03:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82a6780e-2542-3101-8c6d-b69a8bcfa991 | -9.64196 | -44.54727 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a3321d2-1961-3d88-9f3c-974681510592 | -4.38421 | -50.87782 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a3f07d6-bd65-3162-866f-21c06fbab990 | -4.21014 | -50.09153 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c14ed89-dbfa-3b0e-905e-188ec59b258e | -4.72053 | -46.45142 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ce0d44e-67cc-3f3f-85cf-e7e2a1d8e7dc | -4.61371 | -49.29321 | 2025-11-13 05:03:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b35ed445-3a96-36e1-b584-ffcc221aeb0d | -3.8601 | -49.79658 | 2025-11-13 05:03:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65d5dff6-a017-3f58-ab5d-0f29d44f193f | -4.72099 | -46.44823 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3c80216a-5f4a-3da8-b6c2-c5e9c17bf9a3 | -5.57629 | -47.10696 | 2025-11-13 05:03:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a2f388ed-d166-3738-b156-eac4590df375 | -9.05997 | -48.83134 | 2025-11-13 05:03:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b385a7d-d3dd-3d6e-89f4-25f00a682773 | -4.06879 | -54.10806 | 2025-11-13 05:03:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 398cba4b-cd4a-381d-b0e4-d03868c5c0b0 | -4.5212 | -46.42189 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 736d4d22-cc67-3efa-bd68-74943aaa3315 | -4.23973 | -48.38561 | 2025-11-13 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e194b0c4-43d2-38ae-8cbf-085cbc209e34 | -4.53024 | -46.43382 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ec10eec5-f354-3469-8b79-9a2622b432c1 | -5.32451 | -45.19581 | 2025-11-13 05:03:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 85f56efa-b2cb-327a-b32e-820272c42520 | -5.38243 | -46.76683 | 2025-11-13 05:03:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ca35333-7049-3c0d-806d-375908cdf737 | -3.42506 | -52.6256 | 2025-11-13 05:03:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9cc700e6-363d-3a84-9269-a49a2ebc6db3 | -5.57876 | -47.10666 | 2025-11-13 05:03:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dffe3025-9978-3e3e-bc84-cec372b863ae | -3.46607 | -50.58452 | 2025-11-13 05:03:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78000e01-cb84-3256-bea9-b9ae38ff79de | -4.5293 | -46.44033 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d5f5376b-8d0b-32fb-9fc3-163d64d76fc1 | -5.04081 | -49.97831 | 2025-11-13 05:03:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68f88c1a-b918-37b5-951d-263eb673c937 | -5.32458 | -45.1995 | 2025-11-13 05:03:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b5e8d38b-2f40-3d63-9cf2-0153c60ab2e6 | -3.86482 | -49.79342 | 2025-11-13 05:03:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| acb9ad58-fb20-3bc7-81c2-0d9f2c184a51 | -6.97239 | -52.87207 | 2025-11-13 05:03:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a0afa2a-f734-3715-a7bb-b38a1497f57f | -4.6119 | -49.29435 | 2025-11-13 05:03:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a93500b5-ddc1-3fd8-8edb-06a9ba44eca0 | -9.32199 | -47.83691 | 2025-11-13 05:03:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81a8d630-8728-34ea-95c2-2d7a1cfa402f | -9.01709 | -45.43693 | 2025-11-13 05:03:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d22f4bd-ff5f-3606-bda6-930e80caa9d3 | -4.36639 | -48.7081 | 2025-11-13 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b76e57f5-c8f2-3b9b-9e47-0956f477ea19 | -3.91134 | -52.1278 | 2025-11-13 05:03:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72ce695a-a619-3938-bb02-8e5bc6d0d0cf | -5.57368 | -47.10568 | 2025-11-13 05:03:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c86d48c7-3c55-349e-bf4d-9079ef63e5da | -9.10731 | -50.05777 | 2025-11-13 05:03:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 034abaec-3b44-3259-b97a-1d52b92ebb9d | -4.00699 | -48.80659 | 2025-11-13 05:03:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa495c5a-dc20-389c-9150-257b8dd2cd8d | -6.16085 | -48.05741 | 2025-11-13 05:03:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb1ea512-bc33-33d8-81d5-c26d7e31700a | -4.71136 | -46.44011 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6655fdd8-1680-3eeb-8d99-e7141c7fd39e | -8.41151 | -48.05556 | 2025-11-13 05:03:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbfcc46c-cd2d-34d5-9d57-eee7223ea9ad | -10.8492 | -44.94429 | 2025-11-13 05:03:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a4233626-3a03-3551-9d08-e6acf7aa7c07 | -4.3085 | -48.24043 | 2025-11-13 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e029039c-e274-341a-bb8b-6ad0c4878201 | -9.34663 | -46.59503 | 2025-11-13 05:03:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 48075970-031a-3ae0-b862-56fd3ad2859d | -9.62858 | -44.55041 | 2025-11-13 05:03:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4b5da1c4-eb3b-3c6c-a40d-de363a296bcf | -5.83891 | -47.5663 | 2025-11-13 05:03:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ccb278c-ea84-32e2-b3dd-6676392aa69e | -10.36737 | -45.05741 | 2025-11-13 05:03:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33afd12e-39be-3fc4-86df-bf6a4f94a199 | -4.01076 | -48.81161 | 2025-11-13 05:03:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1496157f-1aa1-30a1-a977-03054cb34e97 | -4.71617 | -46.44421 | 2025-11-13 05:03:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| bfc3347a-7c2b-3cd6-b015-1a91064a34fc | -10.49973 | -47.98722 | 2025-11-13 05:03:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d989d0e-3749-3831-a29e-6cce810a2abc | -7.25435 | -45.37318 | 2025-11-13 05:03:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bca458dd-fe0a-3402-940c-0c9f41cf32f8 | -4.10751 | -48.01665 | 2025-11-13 05:03:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d0a77b1-c58a-323d-abb0-034e9db35ce4 | -10.77973 | -48.14096 | 2025-11-13 05:03:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f008e710-ac11-3d4e-b135-20c307637111 | -5.67913 | -51.14238 | 2025-11-13 05:03:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11d0e1d3-f8b7-304b-836d-8086ea2251fa | -9.01411 | -45.44117 | 2025-11-13 05:03:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3ecae07-8c4a-309d-9faa-a77f2f3d44af | -3.45481 | -53.51254 | 2025-11-13 05:03:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 711d4966-8c17-3e26-97f1-0cfdea57b4b1 | -7.21651 | -47.979 | 2025-11-13 05:03:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a81d2ef-689b-370d-90c0-d75b5d74fb7d | -9.34615 | -46.5987 | 2025-11-13 05:03:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dddbc5ed-c790-3901-9484-02422711db0a | -5.45103 | -47.69727 | 2025-11-13 05:03:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94469e61-5573-3b64-90e1-58ef740c9b92 | -3.3055 | -53.70666 | 2025-11-13 05:03:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89072cea-45a5-3cca-809b-48c80def4889 | -4.6955 | -49.65067 | 2025-11-13 05:03:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 221f8c7c-fc7f-3bd1-b14f-4c10d1852c79 | -5.44214 | -44.66047 | 2025-11-13 05:03:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README37.md)
