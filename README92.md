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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2ea14f7-25a0-3395-9e89-5ac39cfac512 | -9.5512 | -45.4296 | 2026-09-17 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| e744be38-3b11-3f0d-be63-6f5d205a6964 | -14.5709 | -46.5941 | 2026-09-17 14:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 77d5089f-d3ab-3cad-b66b-a60275850cab | -14.1742 | -45.1407 | 2026-09-17 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 73aac9d9-9485-32e7-92b1-0ebff3796b35 | -14.1937 | -45.1372 | 2026-09-17 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 537531d8-b1d8-30cd-93d2-7cb1dcde9d76 | -11.4861 | -45.7279 | 2026-09-17 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 2221fef9-427b-3608-9c92-9cfbed7acf12 | -9.1056 | -60.9703 | 2026-09-17 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d849919e-a2e4-3029-9da9-11b07a6b2b2a | -8.4983 | -57.6271 | 2026-09-17 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 7b8c7524-59de-300d-a49e-3ef611f39a67 | -8.9108 | -62.391 | 2026-09-17 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 118.5 |
| dace83f7-b714-38ac-9f03-714b3b2cf639 | -7.4412 | -45.2866 | 2026-09-17 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 2b8f6445-e4b6-34cb-b1d3-07b5a2015ee7 | -3.2212 | -53.9422 | 2026-09-17 14:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 92a4cdf1-260e-348c-ac1d-cd4a5354a81e | -11.8928 | -50.0608 | 2026-09-17 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 0a306a48-78e7-3470-b85d-7ac117263af2 | -7.0451 | -42.0666 | 2026-09-17 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 138.7 |
| 3086b06b-ef68-34b5-8bce-e63da5d6eb59 | -13.3949 | -57.0242 | 2026-09-17 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 529f11e0-a24e-3886-a609-32709c2093c0 | -14.1932 | -45.1606 | 2026-09-17 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 44e7455a-859c-3df4-ae42-2271ae3872f7 | -9.7794 | -60.4551 | 2026-09-17 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| a2581cbe-70aa-3f05-ac84-6c79f401f7b2 | -8.8923 | -62.3917 | 2026-09-17 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d3b23dbd-d059-37f6-9b7d-469dc9d2b1ee | -12.7515 | -51.2639 | 2026-09-17 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 2309a66d-b9e8-3cfc-8875-470ab91fde27 | -8.475 | -46.8943 | 2026-09-17 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 1fc51e37-0d8e-3d5f-a7ac-8706886fa21f | -10.0418 | -45.5756 | 2026-09-17 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 760bc435-4767-3f86-b349-9d34ac614f43 | -30.6109 | -53.0283 | 2026-09-17 14:10:00 | GOES-19 | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 362.5 |
| d1396b93-ca97-3fad-9efe-f5fba2b1ca0f | -11.8069 | -58.1759 | 2026-09-17 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| db26ad87-4f42-30d1-a4b0-c2274a335942 | -10.8919 | -54.0062 | 2026-09-17 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 532da838-3dda-31c9-b143-26ba38c2168d | -8.4982 | -57.6468 | 2026-09-17 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| b33a8d72-3162-3de3-801d-09641be492c1 | -11.3442 | -43.9906 | 2026-09-17 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 8fd281fe-8eb2-3f39-8c83-2349b2c625eb | -9.7608 | -60.4561 | 2026-09-17 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 482802cb-4ee1-34ee-8a2f-867f6ed79d33 | -12.7518 | -51.2426 | 2026-09-17 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| c1b4ab38-a859-3e86-9e11-9f0c0be4f3d3 | -6.6515 | -43.6354 | 2026-09-17 14:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 1acdbebc-966b-315a-9f68-7bca218ed349 | -10.8118 | -46.1594 | 2026-09-17 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| c193f415-4824-3396-9efc-4b598073917e | -13.6148 | -46.9334 | 2026-09-17 14:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| e784a7e7-24e6-316e-9a6b-483b5b6ef796 | -11.8069 | -58.1759 | 2026-09-17 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 59ad5b4e-1b58-34f5-9b35-c22c145dfc18 | -11.3629 | -44.0112 | 2026-09-17 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 4263ce37-5d7f-3dc4-9254-61dc8efef603 | -8.8642 | -45.9145 | 2026-09-17 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 4b8b46c4-14f2-33ae-b578-8416c7d81ff0 | -13.3055 | -51.3235 | 2026-09-17 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| dedce021-bdbf-3496-a3a0-12326738bdd2 | -12.7243 | -48.2734 | 2026-09-17 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 7c79c05c-00bd-3664-b7b9-69cce364e664 | -7.8221 | -44.8632 | 2026-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.7 |
| c4b2a092-787a-350e-8176-b50f1aaacb62 | -10.0612 | -45.5504 | 2026-09-17 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 167.7 |
| f1dc9310-784d-3acb-b34f-050dce5e864d | -9.7608 | -60.4561 | 2026-09-17 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| d7da343a-1eb9-3812-a116-fe86e4881b0c | -13.3949 | -57.0242 | 2026-09-17 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 6bdcc6f3-852b-34e1-a174-9dc663d26adb | -8.396 | -47.2121 | 2026-09-17 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 08c5fdd3-78c9-3537-91fc-6fa4972df39a | -15.5008 | -53.8132 | 2026-09-17 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| dea13d70-5285-3c43-8000-4a92822a6753 | -10.9107 | -54.0045 | 2026-09-17 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| aa2a06d8-7a55-3b99-ba59-8e8c6e7c565f | -9.1057 | -60.9511 | 2026-09-17 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 53df9d11-2b4c-3c08-858e-b14dc1182e29 | -9.3572 | -50.137 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 44071574-0fea-3726-a5bf-7afd33c0fe33 | -9.0868 | -61.0095 | 2026-09-17 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 38272461-30e4-377b-97c2-b72266cc0608 | -13.6148 | -46.9334 | 2026-09-17 14:20:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8c490ef3-13ae-38bc-acf0-c27f82957aae | -7.3669 | -38.9584 | 2026-09-17 14:20:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 175.6 |
| 99654056-a101-3ff6-b25c-8c088294021c | -14.5709 | -46.5941 | 2026-09-17 14:20:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 97a4948e-4a97-3460-a00f-ac0cdeb732b9 | -10.8343 | -54.0933 | 2026-09-17 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 264e9e50-89db-3cb5-a41b-b5d146b66bda | -8.7892 | -45.8773 | 2026-09-17 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 06dcbd30-3738-370a-b547-0f1a95adc6f5 | -10.8308 | -46.1569 | 2026-09-17 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 240.5 |
| 5950d4d2-8b5d-32a4-b01e-1c5b74cf479a | -9.3564 | -50.201 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| b12429da-2f00-3f74-a4fc-875b34055711 | -9.4132 | -50.1744 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 8acb8eb8-cd89-3f65-8e73-74d2c5688930 | -9.7794 | -60.4551 | 2026-09-17 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| dfae97b1-d0b6-33aa-94da-f3a458a86e5c | -18.8899 | -46.8519 | 2026-09-17 14:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 999be157-176e-3624-837a-758cc1acb345 | -13.2678 | -51.2856 | 2026-09-17 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 71a909f6-594f-3bc4-aa13-4bf17ad0c04e | -11.738 | -50.2295 | 2026-09-17 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c8b82cac-191f-3f99-addd-fdc31fd7bc8d | -30.6109 | -53.0283 | 2026-09-17 14:20:00 | GOES-19 | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 254.1 |
| 45ad66cb-d1b9-3f29-baa7-784823a699ab | -3.2212 | -53.9422 | 2026-09-17 14:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 1f2de5c8-092f-3036-aa69-babadb532211 | -6.9896 | -43.6514 | 2026-09-17 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 724ba0e9-16be-3231-902a-0c51a899b46d | -10.8118 | -46.1594 | 2026-09-17 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 76981c16-fdcd-3ad0-89fa-b71546dacdac | -8.4983 | -57.6271 | 2026-09-17 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 05b31135-ecd0-3297-b87f-6194582f7276 | -10.8312 | -46.1342 | 2026-09-17 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| f563a6e4-b43e-3641-ba57-2345692bc53f | -7.0451 | -42.0666 | 2026-09-17 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 133.0 |
| c3f13303-654b-376c-bbd5-c8627714a6d5 | -7.9828 | -44.0415 | 2026-09-17 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 4bda2c1a-e008-36d0-a2b6-4d68f5098c11 | -7.0084 | -43.6497 | 2026-09-17 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| bdc8709b-7d8f-307d-ad0c-782894f2f552 | -18.8906 | -46.8284 | 2026-09-17 14:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 89.5 |
| f3d10d23-b43f-39a7-9df7-fede4a27ac2b | -15.552 | -54.2255 | 2026-09-17 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 9db8417e-ecf4-3d6b-9072-018caff642a8 | -8.475 | -46.8943 | 2026-09-17 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f8ac4a5f-b06e-34e9-9404-65609cca6201 | -9.4139 | -50.1103 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| d28884db-92a0-3c21-a6ab-787b793785b0 | -11.8928 | -50.0608 | 2026-09-17 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| e1dbf8f4-96b1-3a29-bd1d-2b20cd0c4b13 | -15.5715 | -54.223 | 2026-09-17 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 5c4313b7-3fd3-33f1-acad-1b6eb6129af8 | -11.8924 | -50.0823 | 2026-09-17 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| dfaf207f-7fe0-34dc-9991-6c2eceda8868 | -9.7793 | -60.4744 | 2026-09-17 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 4a6ada51-ba58-3e5e-9c1e-3c4ec54bc070 | -13.2986 | -51.7501 | 2026-09-17 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c7b55ced-9aa9-3bf2-b10c-a2fe66a572fa | -6.6515 | -43.6354 | 2026-09-17 14:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8f36d7d1-b962-3a8b-9a06-1a1e9d212ea4 | -10.0418 | -45.5756 | 2026-09-17 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 480.0 |
| 02632736-2124-3ec3-96be-1089f24322ad | -9.1056 | -60.9703 | 2026-09-17 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5d777ec4-2718-3671-bd8f-8703fe869321 | -9.1337 | -65.844 | 2026-09-17 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 517cc1e6-b488-309d-b4d1-564adace5c7f | -7.1381 | -42.1768 | 2026-09-17 14:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 78b38418-0b07-3b94-bb6f-225416562f55 | -9.3765 | -50.0925 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| d08cb8cc-b764-3ef7-83aa-6c189cd9c878 | -7.8412 | -44.8385 | 2026-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 163.3 |
| e285c9ac-35d4-3d8e-876d-5bb8e2f0358b | -7.841 | -44.8614 | 2026-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 163.5 |
| dd08c235-ecc3-3966-adaa-0b5911669c83 | -4.5044 | -54.9845 | 2026-09-17 14:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 195.4 |
| 8437a0ae-b119-3c71-a08b-58e754ed9642 | -14.1547 | -45.1442 | 2026-09-17 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| b576d3e8-2177-3a9a-a361-829e30d17728 | -11.3442 | -43.9906 | 2026-09-17 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 193.3 |
| f05b057e-1c94-3fb3-b1e8-309f213fb4c9 | -15.4817 | -53.7947 | 2026-09-17 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| c4dbfa42-4ced-3f57-9a2c-b9f83cec7d0d | -15.481 | -53.8367 | 2026-09-17 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| b4f0081c-bf15-334d-8531-bf14b98b975c | -11.3437 | -44.0141 | 2026-09-17 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 391.8 |
| 24b67a7e-8c8e-3df0-a3c9-5f8f49fdacca | -10.8919 | -54.0062 | 2026-09-17 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 4d3a1b1b-bcaf-39be-b528-87f2ff3b72b9 | -7.6402 | -44.3303 | 2026-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 16cdac59-4747-3a07-97f0-7b1f97f31f18 | -7.0454 | -42.0427 | 2026-09-17 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 108.4 |
| 41b2c704-b9f3-367e-a967-88aa2dd60faa | -7.6381 | -46.1478 | 2026-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6fa5a9a7-24c8-38ee-9b46-37b8869c302d | -9.0869 | -60.9904 | 2026-09-17 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| eae7da31-5ef2-3077-82b7-fe1b4a8ed565 | -4.5229 | -54.9639 | 2026-09-17 14:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 168.6 |
| f670e32d-214c-34e8-9494-1e961d1c2b2f | -15.5004 | -53.8342 | 2026-09-17 14:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 2c7b40b8-f5c7-3e45-8cf4-3c0f8d7f592e | -13.3758 | -57.026 | 2026-09-17 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.4 |
| fc456225-efbc-33f9-ab08-e20769ca20da | -9.3758 | -50.1565 | 2026-09-17 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| cae91fea-9ee9-336c-9916-45e26c5f86bf | -9.8694 | -48.3814 | 2026-09-17 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 145b093b-a701-3e1a-97fd-5a4a571f8d70 | -11.3625 | -44.0347 | 2026-09-17 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 50b85c84-2074-389a-b27a-2ee0129a8be1 | -6.9932 | -43.3246 | 2026-09-17 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |


[Clique aqui para ver as próximas entradas](README93.md)
