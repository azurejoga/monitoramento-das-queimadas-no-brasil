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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 395b5c48-c8e6-38e9-8124-1b7427d39378 | -6.75478 | -38.57891 | 2025-10-13 03:53:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d387b537-8f86-3b0c-adbf-b06c4a28518c | -3.59002 | -47.28255 | 2025-10-13 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 34c156de-39eb-36f7-b1e1-81aa37cab652 | -5.84076 | -42.30698 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 30416e8e-6e40-36be-b363-d965c4f2dca6 | -4.46859 | -44.93282 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df484ef9-ae14-3f64-af42-7251880009f5 | -7.15853 | -42.1894 | 2025-10-13 03:53:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b6f99299-557c-318d-916c-605ab5f4df1b | -2.90981 | -49.17034 | 2025-10-13 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 77a8f9c5-6748-3628-8194-5966750f1c97 | -6.77323 | -42.82099 | 2025-10-13 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a413e8ef-89f2-3987-be60-b659b5737c73 | -5.41364 | -40.97995 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 72f8c94e-1612-3550-9d0b-abd6aa213e64 | -3.81495 | -45.76096 | 2025-10-13 03:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9355a848-f111-399c-85fb-514043ea8430 | -7.05385 | -40.32434 | 2025-10-13 03:53:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 04b6b7fa-c969-3dee-856b-a13fd724c9fd | -4.47165 | -44.94308 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 957ad45d-59fa-3542-87f2-4974f6519fea | -7.50057 | -42.16455 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d85d5d06-5066-3d25-9913-bf26e8076f2b | -2.24822 | -47.87315 | 2025-10-13 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6b027250-e024-3432-916e-daba5c7623f5 | -6.75808 | -38.57943 | 2025-10-13 03:53:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8bb71b7c-1f16-378b-8225-a62f1387e290 | -2.52967 | -47.79542 | 2025-10-13 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3909fa40-4661-39d0-b69c-a1299560d46f | -4.47548 | -44.9486 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a5727bf5-af2f-3398-b228-6a0f89113d56 | -5.33656 | -44.84077 | 2025-10-13 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fea0ce5e-a866-3aba-a00c-d14a35da7a8c | -5.93021 | -40.88412 | 2025-10-13 03:53:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| df3c662e-2573-39a6-975f-ccb955e21d44 | -6.27003 | -42.90804 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bb71418-2ffd-3658-b63d-26baa7b08101 | -7.21605 | -39.90279 | 2025-10-13 03:53:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3c84cc8b-521f-3c3a-af17-ea9d35013711 | -5.93372 | -40.88468 | 2025-10-13 03:53:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| b86d34b1-ee73-3988-bd60-79ac60e302ab | -7.34546 | -43.85798 | 2025-10-13 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 836c9ca8-22a1-3282-a47c-ee06e38ec5b1 | -6.21965 | -41.56767 | 2025-10-13 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 09f51906-7c2e-391d-9d97-646c47fde4ea | -6.74628 | -42.16408 | 2025-10-13 03:53:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e192ad19-4e17-36b0-8fbc-caab23877efe | -5.40862 | -44.32314 | 2025-10-13 03:53:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d416443-6992-316d-a197-1146447628d1 | -6.7433 | -42.15899 | 2025-10-13 03:53:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 612ad725-6cd0-3457-b4bf-a62dbfadbd75 | -6.28435 | -42.99173 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 352d14ce-fd23-3cb1-903d-cf049785a134 | -2.53407 | -47.80454 | 2025-10-13 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 5aa5a34c-8e39-30c6-838f-7eb075c5c826 | -7.14195 | -42.50095 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a2a13c3a-b4a8-3899-86c9-85f2a2cc1dce | -5.83789 | -44.06419 | 2025-10-13 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fc48a59f-70ea-35b4-bd50-8962bbaa37a4 | -4.40288 | -41.59267 | 2025-10-13 03:53:00 | NOAA-21 | LAGOA DE SÃO FRANCISCO | PIAUÍ | Brasil | 2205573 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b9ae49e-86bb-36bb-8279-b883865f9713 | -5.74198 | -40.76766 | 2025-10-13 03:53:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3902bcdf-f6e5-3322-aaf7-dc16dcdc3d55 | -5.90969 | -43.49097 | 2025-10-13 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ae42a66-a73c-3208-be39-aa1143f89880 | -4.48086 | -44.94457 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 02ab5f20-71fd-3a48-82e0-f36b08a881bc | -3.2251 | -50.05619 | 2025-10-13 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b69f163-a387-3385-9212-63dcf16214f7 | -7.35017 | -43.85492 | 2025-10-13 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 813da153-741b-3b5c-8262-e959a2e6820f | -3.73607 | -45.41169 | 2025-10-13 03:53:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fb82d13-91a8-3d55-a769-97259c7e111d | -4.83383 | -41.48193 | 2025-10-13 03:53:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6837c766-a69d-3e56-8326-6e271745bab1 | -3.1269 | -50.20399 | 2025-10-13 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 242f4434-cca1-3d2d-a11e-0791458778f8 | -2.26317 | -47.8545 | 2025-10-13 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3b6d073-cd60-3df4-98ba-c1a9a3712c6c | -6.77311 | -42.83381 | 2025-10-13 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a49638c9-d6f0-3459-90fc-a9c3a577f1a2 | -3.13689 | -50.21207 | 2025-10-13 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 89773520-da8d-3261-85c5-8d6d82c7d14d | -5.42472 | -41.33526 | 2025-10-13 03:53:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4f751d6c-f446-36b7-8f33-6ae27eab0f56 | -7.21548 | -39.90638 | 2025-10-13 03:53:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e4dc6762-7396-3699-9b44-99e43cb7e52e | -5.3135 | -42.89568 | 2025-10-13 03:53:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 42845115-addc-3a7a-9f94-edd835bea774 | -4.67643 | -43.26247 | 2025-10-13 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31f17321-156b-3832-9f2b-b3cd8c41eae7 | -5.56633 | -45.27238 | 2025-10-13 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f7704781-f96b-320b-b554-d084c6f45454 | -4.47087 | -44.94783 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd95b64b-f80d-385f-b119-a5df9f8f5097 | -2.26357 | -47.85332 | 2025-10-13 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5d23afab-9e67-31ec-b1a0-ab9293412290 | -6.29352 | -46.72415 | 2025-10-13 03:53:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3034a5a8-d5cd-3681-9f60-f64b66c58383 | -4.46781 | -44.93761 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 89f60325-b837-3006-b3f4-7542c695964f | -3.17137 | -40.15627 | 2025-10-13 03:53:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43ab059f-100f-369a-9edf-950584eaad16 | -7.28659 | -41.95866 | 2025-10-13 03:53:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b8e0d29a-a529-3128-9be1-103cd530fc2b | -3.12456 | -50.20463 | 2025-10-13 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1a1f7bd1-78f7-30ab-b1b6-ea4d27187b81 | -7.14798 | -42.51142 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0ecaeee9-63d4-3484-aaa4-64a5adc29e52 | -4.47703 | -44.93906 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b5db93c4-f02c-37b9-96e7-929beb9873ca | -7.26704 | -44.14861 | 2025-10-13 03:53:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 582c05f8-9489-3393-8287-573d0fc037e4 | -5.73912 | -40.7632 | 2025-10-13 03:53:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 43b60c98-69df-332d-a4c6-c9b980412dbc | -3.36803 | -40.63236 | 2025-10-13 03:53:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1560770b-2bfb-3a59-8a93-2f06ee890b34 | -5.93659 | -40.8892 | 2025-10-13 03:53:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1abe32ed-da5b-3ff3-b51f-7ab7c935fe40 | -7.0563 | -44.26285 | 2025-10-13 03:53:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25f70c9c-e3c7-3ffe-af5f-8faf1e4d52a4 | -5.04668 | -49.88151 | 2025-10-13 03:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d427cf98-dc46-35f2-850a-2508db7bda12 | -6.17505 | -42.54011 | 2025-10-13 03:53:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f2fda3c3-740d-34a3-a652-0cbcea561364 | -6.19567 | -42.67639 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6a2bd064-3a91-3001-99b4-079fa41e9bab | -6.42599 | -42.55299 | 2025-10-13 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fcfda8d8-01aa-3827-a91f-86c3582dadca | -2.91168 | -49.17128 | 2025-10-13 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1f20b2c0-ecd8-378d-94b7-7fd498d28069 | -4.48717 | -44.93331 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2bd0093f-14b8-397b-8bfd-05a09b72a8b8 | -5.91359 | -43.49152 | 2025-10-13 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aea42a67-f9ce-3a13-befc-04ba3cef2a76 | -7.64609 | -42.58011 | 2025-10-13 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bcc456fb-b8b4-3c73-835c-9224fff669b6 | -7.69003 | -42.38314 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2c65e04a-96a0-383e-84b4-875e8fe38e4f | -5.3216 | -43.43151 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 292af9f7-a9c8-36bb-be95-d2bf7e3940e5 | -4.28338 | -48.57758 | 2025-10-13 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d167aa2a-d99f-3418-bd49-c460f600580d | -4.47636 | -44.94128 | 2025-10-13 03:53:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 71fe5f59-a820-33b0-b899-61db607b4337 | -4.68241 | -43.12573 | 2025-10-13 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 68e0374d-daf6-3cbc-8269-bb2e6b3da622 | -7.14623 | -41.71294 | 2025-10-13 03:53:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b410aae6-23b9-3990-bac3-72601da4935e | -4.86669 | -45.91259 | 2025-10-13 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51c44968-9a96-3ef1-9484-1e1a6c09469b | -6.56481 | -43.9263 | 2025-10-13 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d4ffdc0-19db-3473-acd1-c212b35ae102 | -2.54114 | -47.79766 | 2025-10-13 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1bbdfb03-977a-3fde-a440-c51ea7eaec2f | -7.65137 | -42.57148 | 2025-10-13 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 95783a7e-64c3-3f5b-bb85-0e3e6621f700 | -7.27342 | -42.95491 | 2025-10-13 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| dc391232-3731-3998-a943-826b178af193 | -7.48802 | -42.75996 | 2025-10-13 03:53:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 44add024-8068-3a94-8374-c7c6384ce6d6 | -7.45837 | -42.03337 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5a878853-8900-3067-b9cd-0e439dcb6611 | -6.56541 | -43.92266 | 2025-10-13 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfb86a60-9897-3a0d-9820-37103ebffc45 | -2.64021 | -47.30363 | 2025-10-13 03:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba0d1e1c-c611-34dd-8a5b-fb30ff88f41c | -2.92718 | -48.30107 | 2025-10-13 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c0fa681b-fdab-3a0a-9b35-2d25f35487ff | -7.51231 | -42.16199 | 2025-10-13 03:53:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 28df9c30-ceff-3a3c-81cc-9f1bf59d4604 | -5.35328 | -43.41779 | 2025-10-13 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a8b26f0-422e-3b45-b55e-9eeccd987756 | -6.34064 | -44.33013 | 2025-10-13 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6cc601d-721b-3a48-926b-3915a6a23d97 | -3.87316 | -44.12242 | 2025-10-13 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3306392-5b95-39cd-96ad-f25557948664 | -5.89698 | -44.73131 | 2025-10-13 03:53:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2184866a-2ce3-3401-ac11-25e96125597d | -5.55087 | -41.32048 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 012e458e-4dd9-346b-b730-f010f5b50dba | -5.84 | -42.31166 | 2025-10-13 03:53:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9b893f15-7a60-3a78-a552-2b0e6de91d26 | -3.13829 | -50.21728 | 2025-10-13 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 709525a3-dca0-3e4e-91dc-7f2cda3bbe28 | -5.79501 | -35.36457 | 2025-10-13 03:53:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73e00a01-b32c-3793-9fc3-69c26cea58e3 | -6.22391 | -41.56421 | 2025-10-13 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4ee14376-d234-3185-9e53-c6c4bd826612 | -6.29404 | -46.72114 | 2025-10-13 03:53:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36d0326b-b773-34f7-90e1-e15dab8136bf | -6.5737 | -43.9241 | 2025-10-13 03:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15b16e0e-7c98-30ca-b036-4c379c5de1de | -5.04965 | -49.88174 | 2025-10-13 03:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 36aefc51-349b-3c61-b543-72402e35d808 | -7.13971 | -42.51472 | 2025-10-13 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b293feab-c843-3880-a4b0-7b8e19a9b628 | -6.48098 | -42.06005 | 2025-10-13 03:53:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README11.md)
