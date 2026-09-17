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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b45f7419-0efd-3ac3-bef6-d3712de53b79 | -8.7389 | -45.33755 | 2026-09-17 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c5f7bcf-2ff3-3dd6-a517-d12fe1f61279 | -11.25681 | -47.6695 | 2026-09-17 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2b80818-3e47-3554-b31b-8ce3e04f6f84 | -6.75948 | -56.32972 | 2026-09-17 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 491b621f-0d19-380c-bace-1c43c2890162 | -7.14615 | -42.09606 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f28480f4-9862-38c7-9f8e-1ca6332bd1df | -9.44698 | -60.38059 | 2026-09-17 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25f60cd4-db9d-3f48-8c90-0da69e3b3d5a | -9.88135 | -48.38234 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 47b2d41f-64b4-357f-b14d-21136d62aab7 | -11.29824 | -51.72781 | 2026-09-17 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cc323fa-a92a-3a54-b1d4-84b8d2fabeda | -8.58209 | -44.57898 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 758ce60d-d04d-3fc7-a063-838d32943351 | -7.37012 | -44.47723 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 527126fb-8c2a-3167-a1a9-24f96cd57b07 | -9.86649 | -48.38785 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 075b8def-cd14-33d7-864d-37a08ce21bb1 | -8.90402 | -43.88606 | 2026-09-17 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 70d0876c-3fd8-3921-adc4-d945432b315c | -6.35086 | -51.77669 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7dbd1f0-4e3e-3b85-9f15-45fe6761b074 | -9.61365 | -45.34401 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3a0ad3e-e7d2-36e5-a284-7ad7f3aab038 | -11.48423 | -45.77829 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd9130b1-a74d-3e15-a5b9-165f460e2215 | -6.36739 | -58.29129 | 2026-09-17 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e946cce-0a71-35df-985e-97dc69d27666 | -9.87335 | -48.38888 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a0321208-4741-3eab-8a1d-4bab96b48948 | -12.52632 | -45.96681 | 2026-09-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75a54504-295f-3a2c-80f1-b6fcc6bb0210 | -10.82334 | -46.17605 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf5cd1fe-4996-3188-b717-9f6a74c66e00 | -9.86281 | -46.76073 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e85aa6ff-22f6-33b9-8c02-72eca443cbd2 | -11.27392 | -43.49307 | 2026-09-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6956054a-bfd6-3183-b6cc-6fa6ef2efb67 | -9.04134 | -47.76171 | 2026-09-17 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ca11e49-5cc7-3b6f-82cc-d22aa809daa2 | -10.50352 | -46.33501 | 2026-09-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56b5ca51-dda1-3af4-b0e7-3e50e5543054 | -6.3628 | -58.2873 | 2026-09-17 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e265b3f-e7a3-3751-b45e-94d73a5fb7d3 | -7.1091 | -43.10803 | 2026-09-17 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d7e843da-d48d-3c13-b38c-ddd4802c7e40 | -10.40043 | -48.65873 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac5797cc-b742-35d8-8194-fbb251e01562 | -6.1037 | -55.57847 | 2026-09-17 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10826e4c-63b0-3ff5-a55e-273de5aadb16 | -6.51721 | -44.05409 | 2026-09-17 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b5994a7-6804-3d49-a0df-60ff32351489 | -10.11845 | -45.57104 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d3468a7f-ab4b-3edc-b7d0-0d059ca59f5e | -5.92657 | -51.6447 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f45a4104-dccb-3c51-b19a-c8c804b5e731 | -10.14921 | -45.67029 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78be69b5-546b-38a0-8504-dbd449ea2e85 | -11.59408 | -46.87799 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 162bf4db-d304-3822-a641-4da1404c4ded | -10.82745 | -46.14667 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 626317e8-afd6-3904-afb2-cb3d2c0195fb | -10.83268 | -46.13768 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 055f5959-1436-3149-84e2-08a9dc7845d3 | -5.15197 | -55.94224 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1f0e2ab-fac5-390e-8d3c-700de50a24f1 | -7.34799 | -44.20077 | 2026-09-17 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b1281ba-b920-381c-8d6c-dc40af8eeafe | -7.08604 | -41.76877 | 2026-09-17 04:40:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4cbf0e0c-fa7d-3574-8d77-8f78fdc75ca7 | -7.51393 | -44.93045 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ebaa8457-5a86-37a6-a379-37667031d4b3 | -7.10163 | -43.11297 | 2026-09-17 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b72272aa-015d-32f5-bd90-2f3002769a09 | -7.14312 | -42.15481 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2cb8a8eb-3056-3c8f-919f-6836a51b4b8a | -10.98254 | -48.30537 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48f4911a-9ad6-36e6-b332-55829afaa9bd | -8.50477 | -44.70943 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18ce353c-fa0e-3a2d-bfcd-8c5e1323c971 | -7.08849 | -42.09226 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7c4ac6d6-dd3a-3e36-b1a5-46a896e0c57c | -11.48973 | -45.73943 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b98637df-cb11-3032-9421-42dd388d4dab | -7.04269 | -42.07235 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b1d88dfa-0a63-35cc-a1df-b67ceb58cbb1 | -9.56025 | -46.60398 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21318f21-f253-30a4-9832-b48220714364 | -6.94253 | -41.70332 | 2026-09-17 04:40:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ada1fe6c-0cae-37e4-a84e-e136e98e3491 | -5.22154 | -49.31261 | 2026-09-17 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7583682a-8526-3f6c-bff5-94323c3a8282 | -5.86168 | -52.05497 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a857da0-5194-336d-9446-64590574594e | -7.44678 | -45.29073 | 2026-09-17 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4712a1ea-8716-3013-af56-b199c88d0469 | -11.60991 | -50.6338 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80421927-d322-327a-b43e-dee16adb0a0e | -5.36829 | -48.97883 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c3d540f-9c91-33e6-b747-7e2b122db2e5 | -10.60928 | -45.23 | 2026-09-17 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca08ba01-81f2-3f7b-b8e7-680e33956484 | -8.47945 | -46.88838 | 2026-09-17 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30c1ad65-39d8-38f5-93ad-0b7fc30a4936 | -11.8882 | -47.59489 | 2026-09-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b408902-1849-3d8e-89fc-b18e54f7dc8c | -9.82229 | -46.50039 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40471bad-12bb-36b3-a886-6fb45d59be25 | -6.93677 | -41.70851 | 2026-09-17 04:40:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1e70f2ef-5643-3ccb-9576-96b02c349519 | -6.78081 | -48.66372 | 2026-09-17 04:40:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e4706f8-2c1a-3ea7-9c0a-7cfc685c8bbf | -5.86275 | -52.0551 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45e8ce5d-c5a6-31c1-a916-a5829b852bb4 | -9.04077 | -47.76561 | 2026-09-17 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 627a1906-0c28-3431-a409-ea52521615f1 | -10.54426 | -44.85041 | 2026-09-17 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd30cf44-ba62-3381-a7e5-db3b96c5702c | -8.342 | -44.83542 | 2026-09-17 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 631cea33-3278-346d-bc91-9a21a9094f4d | -7.45265 | -46.16568 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| daa32e29-8ead-3141-ba7b-118c40dea2f3 | -8.86466 | -44.90277 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 165e978c-d5ed-33fe-83f6-3893707a744f | -9.34912 | -50.12901 | 2026-09-17 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21d58e26-c0f6-314e-bfcb-8956b1734f7f | -11.88941 | -47.58637 | 2026-09-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed6a5a10-55f1-311f-a813-ad11ae56c5d2 | -7.00432 | -43.33233 | 2026-09-17 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7bb9e6b8-8b69-3917-a34c-9471044ce06e | -11.59231 | -47.30947 | 2026-09-17 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a7e7125-06dd-3c0d-92a4-fe4155d7e70c | -4.52868 | -54.91849 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33916bc4-6e2d-3a85-863b-3ef3f7df06b7 | -8.92087 | -50.84184 | 2026-09-17 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de4ad580-d167-31b3-ba3c-d871919d56d0 | -10.57696 | -57.69131 | 2026-09-17 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a4545d75-8637-381e-95ad-73033f686a4a | -9.88077 | -48.38617 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 624d5da3-69ff-3717-a5c8-5f0a22c2d15d | -8.46388 | -44.91344 | 2026-09-17 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 540db5e3-204f-3724-bb2a-b5f566dca4da | -9.10845 | -45.72477 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 083d9541-c06c-31a2-bec2-60117e29b0c6 | -9.82605 | -46.50092 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 575652c3-0589-395c-b705-1ea1f7e3be78 | -8.22176 | -55.45878 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 578e9140-1200-35a1-a050-b94e0cbe5f57 | -6.20806 | -45.335 | 2026-09-17 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71590709-e3e0-3bd0-bea1-44f61d8c8e96 | -9.25553 | -58.89889 | 2026-09-17 04:40:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03ac4c4e-dad1-3d3e-addc-4c00adcd9dc4 | -10.80468 | -46.16822 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b38403cf-6f20-391d-9b6c-bfd72139eac4 | -8.58369 | -44.56764 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 537b2cab-027c-3040-b11b-c8e6f96e95d9 | -9.62022 | -45.35567 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99e4bf47-daf7-3294-a3ef-96fa8d397e5e | -11.21293 | -42.8311 | 2026-09-17 04:40:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 177dc8fb-6d68-3afd-b6f3-7dd079cfcc39 | -7.1703 | -42.09939 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c2d7b5ac-67a5-33f4-b35e-cc5cd999ac05 | -9.61878 | -45.36604 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8bcd0deb-2708-3b03-a634-d4fe9e69a7a7 | -4.42107 | -55.50201 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4ddbc30-d5c1-35e9-857c-67ca49daa632 | -7.12375 | -42.08652 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 40505652-8f05-317d-921f-09da55469809 | -9.6061 | -45.33941 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 68a517fe-47d1-3fa1-ae44-5eb653badee1 | -9.04191 | -47.75781 | 2026-09-17 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f7057dd-71d7-3b41-880f-7888c25534b9 | -12.74174 | -43.45625 | 2026-09-17 04:40:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64bfe809-e3f0-38b1-82c0-f829301ec959 | -5.88567 | -52.09092 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d95d40e-90f2-334e-880c-90860f2d42b3 | -11.32219 | -46.77519 | 2026-09-17 04:40:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 61e511b5-fbc0-3040-8b97-49010e2bf5b0 | -5.54133 | -46.59588 | 2026-09-17 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02b389e1-c11c-31dd-b38d-e400e94d2c3d | -6.32941 | -52.73216 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ef5a69a-2f6e-3b39-8660-844f01a5647f | -11.13207 | -49.0418 | 2026-09-17 04:40:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7415bf87-e423-3b4b-b5c1-1df0d50f1f9d | -6.4129 | -43.46969 | 2026-09-17 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 251a1113-c3a7-3b1b-bbe6-159a390d3d2e | -9.10299 | -45.72754 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 42a97a09-172f-39c0-a689-984670cbfadc | -6.79785 | -58.79089 | 2026-09-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c9074a73-4880-34ca-ac01-7e1b838bdcd1 | -5.92941 | -51.64537 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9341ee27-90a9-30cb-83b1-4846f6f2c0a4 | -6.9618 | -42.56922 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a63260ec-39af-3775-8c72-bfebf55f1939 | -8.56514 | -44.54852 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 350cc1f0-0d3f-3bd7-80fd-237a5d8b1c8b | -8.49622 | -57.64286 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README40.md)
