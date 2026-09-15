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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e98cb0f-c7c8-3c92-b1cc-aba04987b142 | -13.39409 | -57.0221 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec1d78c1-91ce-3e35-b567-5198e6ca5888 | -10.45889 | -51.23346 | 2026-09-15 04:34:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37163a34-51a7-373e-a8fe-43911d237071 | -13.99398 | -54.07268 | 2026-09-15 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45aac041-61a1-30ee-a59a-11f8ca4e59b6 | -9.3588 | -50.11697 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2db756ba-3a51-3348-910e-75967318f241 | -8.11798 | -54.80244 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a38ff985-f46e-3dfc-8311-0f1641d890b4 | -11.26365 | -54.13179 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 897f4356-8c69-3c65-9567-0f07dc57bb5f | -9.26447 | -59.64167 | 2026-09-15 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3762cb6-acd6-3ee2-8c3e-2f5116c54f11 | -13.55717 | -43.5309 | 2026-09-15 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65734aac-48a9-376a-929a-7626485d520f | -13.26474 | -51.28422 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64e72395-9d31-3428-ac43-c6f8d63b6ab2 | -11.24502 | -43.46284 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94716dc6-3260-3f33-bcb8-4d8e7d187300 | -10.60323 | -57.31955 | 2026-09-15 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35cb50e1-080f-3aae-94a5-4179fdfb525a | -10.65911 | -54.15042 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1826b25-bd87-3147-bd50-8d4f240a35f0 | -12.11645 | -44.20775 | 2026-09-15 04:34:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27802d3f-82f5-3940-a8b2-e814b4ff30d1 | -9.35695 | -50.17166 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fe0247d-66a5-350c-a860-7c9436b8f0d9 | -9.63545 | -47.68707 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90895893-1ebf-3251-b2a1-5fba58b1d23a | -13.63903 | -47.88591 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b671fc8d-e58a-3c2b-93f8-ecfefaa643a8 | -7.92942 | -49.73335 | 2026-09-15 04:34:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0dcdc23-6a05-3837-b33d-c67d1367aaaf | -9.45463 | -40.38525 | 2026-09-15 04:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 7c8b0332-2dd3-332e-8d75-dddbe270f75e | -14.39144 | -48.30372 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34d6c5b3-3a82-38b9-91c0-186352265d95 | -9.35949 | -50.11288 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 26909ca9-bc69-32a0-9e30-fdf2ca58b2e3 | -10.24074 | -50.91246 | 2026-09-15 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68ef2707-2d3b-3368-8098-ae959e2f3334 | -13.27485 | -51.29043 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02be8bd4-be41-3f49-856b-15ebfb728327 | -8.53954 | -54.70222 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 098e18b0-ac53-3350-b5e9-6d3744e09a25 | -10.67659 | -54.18186 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e0b4aee-2033-3005-9dc4-cae7307382e5 | -15.07482 | -48.55621 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aadf9f63-ee7f-3851-8e2b-44bd54791ca2 | -6.88069 | -59.63836 | 2026-09-15 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7dac055-ed75-399e-9b11-5975294ce962 | -10.67614 | -54.15845 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1124748e-42d5-342c-99b4-183bcac5114e | -8.46952 | -50.78051 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3f88919-0da1-3351-afc3-1b4899218a1b | -10.30151 | -54.173 | 2026-09-15 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3056dc3-8239-3be7-a478-e7d431144c09 | -15.28628 | -42.79565 | 2026-09-15 04:34:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 530eb7ac-d3c9-3434-9512-8298afa81563 | -10.05237 | -45.48071 | 2026-09-15 04:34:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2841abc-c5a3-3a7b-a1f6-fc1dba7aeaca | -12.4909 | -41.41604 | 2026-09-15 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c17d26cc-b505-338f-99e1-5ea11315af1a | -14.19978 | -47.42548 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 81485f81-29f5-3934-84c7-170e561b6325 | -12.12648 | -57.18719 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 277d6359-8037-3eb4-8552-a17316c5e381 | -12.78625 | -47.56564 | 2026-09-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a606be4-919c-3322-82f7-ee31d64f5cf0 | -13.57773 | -47.90831 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef09fd6d-c0b2-3d9a-9cc3-cac361297691 | -13.77247 | -48.79875 | 2026-09-15 04:34:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 103b7b5b-b794-3dd8-a79b-95ddda08caea | -11.24795 | -43.46597 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7d270cbf-3890-3567-943c-ceac072fc680 | -13.61006 | -48.2841 | 2026-09-15 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7bdcc796-1648-3104-9839-3ae895752b75 | -8.50636 | -48.50063 | 2026-09-15 04:34:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a6a24df-7beb-37de-ba76-3e94d8ce29ea | -13.40378 | -57.02732 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d1eefd87-7de5-34e7-82ef-b8bf933b3a78 | -6.69199 | -58.69474 | 2026-09-15 04:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2750c31-e421-3dc6-95d6-e0b662ecfb3f | -8.63432 | -44.44733 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6ddbca3-b414-3df8-84ce-7c9d5489da39 | -11.80069 | -46.5915 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b914eb5-5c42-32b5-8bf2-042819ae5668 | -15.04996 | -48.56298 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60fab109-bbec-3321-b1ea-0f56c2b9258b | -7.77586 | -49.47811 | 2026-09-15 04:34:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 80eae08e-174f-34be-ae68-9a0e4c45c040 | -9.73638 | -47.09486 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b8e9137-9a0a-3431-bb04-aaab6698a33f | -14.00295 | -53.87685 | 2026-09-15 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 263069d0-e310-3890-a545-ce97910c4aca | -14.85134 | -48.14321 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2630b5a6-320b-3926-8da2-ce075798cb63 | -8.97877 | -49.68017 | 2026-09-15 04:34:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba6e12db-0daa-3f05-932a-9b87b89ced58 | -10.69161 | -54.17539 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a0064ee-8472-3ee2-863e-d3ddd62cd36e | -11.23673 | -43.46645 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e06ca68-dcbe-3b86-80b6-4b90df3f8c69 | -8.48696 | -44.58845 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 929b3ff6-8f86-3276-9d9b-caf8ec028410 | -7.74131 | -49.53374 | 2026-09-15 04:34:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c28b0bc-d0b4-3e7d-9785-fbe30e0b9579 | -8.48404 | -44.58418 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c629bca9-a2ca-3390-883e-8b9c98b5790d | -11.22913 | -43.46531 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79390061-82a8-3313-8330-a017bfc83b00 | -10.94136 | -54.08598 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb386576-ed32-31ca-ab48-b52df5ee35d9 | -8.96889 | -57.43289 | 2026-09-15 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccb661c1-f9c6-363e-af3e-a3c08d3bd71f | -12.40395 | -48.13572 | 2026-09-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89513450-6e91-3156-b06d-495536f8e200 | -9.45916 | -40.38588 | 2026-09-15 04:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 78d1baaf-cda6-38f2-a28a-2823e262989b | -13.31043 | -43.99679 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 066ef01e-acc2-3f49-8d6a-122ec4cacd9e | -13.25681 | -51.28718 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b053eae-aed7-3111-80aa-f54568f91f62 | -8.50895 | -50.14992 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 846389ab-f8e0-3ccd-b7f5-d34d50359ed4 | -15.04504 | -48.5512 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dac259d-bd79-395d-87ee-6677480cfb94 | -10.66679 | -54.1333 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fa9f1da-bc20-3095-9790-82b93f1a1dcd | -8.26307 | -55.02785 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30ff5d73-8092-3377-855b-20dea5f034f7 | -8.9674 | -57.44082 | 2026-09-15 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4c64f93-e3f6-3da9-b7f6-77ffebfee8e6 | -13.27196 | -51.28552 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf0c45f5-6fba-3f29-8113-9cfbc255e0ba | -12.92391 | -44.73368 | 2026-09-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf93fd03-1d88-3d40-b29b-6252a1f48737 | -13.33215 | -51.61351 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c9e5326-aad5-3f42-9b03-98fc97f4fc4e | -9.42411 | -49.54654 | 2026-09-15 04:34:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 419fe071-2ed3-30b8-a7fa-86dba5ea3515 | -14.85578 | -48.13661 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d839203e-c9c5-3899-bd66-e9a047df8ff9 | -8.3726 | -54.73013 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fa057090-5852-372e-84c2-07f87f2c9c43 | -10.24148 | -50.90812 | 2026-09-15 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a2eb794-fcef-368f-99d8-5c59cdfac0be | -9.4086 | -50.10438 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b631b9f6-61c0-3e22-9f3b-463304e853d6 | -12.1224 | -44.2112 | 2026-09-15 04:34:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97bc102f-2745-3e9e-85af-f00771a97e83 | -8.8303 | -45.87417 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99d843a9-14d2-39ff-8847-5bcc0263c097 | -12.0304 | -47.81472 | 2026-09-15 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ce83bbd-77aa-3c7c-b773-5fe5c85d1414 | -8.30292 | -50.89066 | 2026-09-15 04:34:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02348bf2-652d-31ce-a702-6d06968cb30f | -13.23028 | -51.66043 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ff72841-5aff-3116-941b-d698c7d1bedc | -12.92753 | -44.73419 | 2026-09-15 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f67ff31-70c9-3cf4-983c-46e7d4c69e3e | -9.73693 | -47.09143 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05b6b775-16b6-3d15-8c4b-7d6f622f8e12 | -12.77742 | -47.12002 | 2026-09-15 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08ce3939-147d-384c-aebf-fcfe95ac6de2 | -13.35271 | -51.71292 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25b7dea0-2935-3da1-affa-ab7b95da392d | -12.85408 | -44.38836 | 2026-09-15 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 6f5d18d3-c6b7-3af8-90ff-11bb34d9a573 | -10.11408 | -49.03643 | 2026-09-15 04:34:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a10d051b-9bbf-3e05-903f-0841688cd39e | -8.48219 | -44.58507 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52b66d03-f5de-3b9a-996f-571936441344 | -10.9031 | -51.54004 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48af150b-9d1c-3eff-88ea-0610f89a82e5 | -13.57994 | -47.91593 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 388283ec-1c73-3715-80bb-64cc88dcf68b | -10.70777 | -47.50293 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfbec6d8-3541-3fd9-9110-84ae0f9ac85b | -8.48398 | -44.57348 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 295d13c8-d329-34d8-b0e2-6bd5daf52ef4 | -14.20757 | -47.4193 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c120f5c9-aa9d-3a39-aa0b-f67e58a1a486 | -15.16468 | -43.84048 | 2026-09-15 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f8313a81-5efa-3b71-a77e-af27df2583e4 | -12.12582 | -57.19063 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef681183-db2c-37c2-9d33-6b1c323aa484 | -10.25378 | -57.69983 | 2026-09-15 04:34:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68625f0b-994c-3fd5-9eb5-2a0d4cce99af | -10.57775 | -47.74345 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4f763ba0-0f6d-3311-b8a4-92da04489bb8 | -10.23706 | -50.91184 | 2026-09-15 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4100477d-4b4d-3344-9a07-e5b1dea89ee6 | -10.66071 | -54.14148 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4313705-ef6b-3bec-9000-252761726fb1 | -10.50104 | -53.57002 | 2026-09-15 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e25f663a-01ff-342c-b6cc-95c8798eea31 | -13.56108 | -43.53146 | 2026-09-15 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README45.md)
