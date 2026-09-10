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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 321cc9f3-7481-3830-a757-e029b12654e8 | -6.82843 | -58.99202 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 736e65e3-2765-3f9a-a1aa-e32a8bca1812 | -6.79562 | -58.89514 | 2026-09-10 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7d7f690-733f-3dd7-8b0b-52facf252ed3 | -7.97596 | -43.98527 | 2026-09-10 05:12:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45b2b2f1-6c23-34c9-a0d0-fe6ce3189c36 | -6.77173 | -58.61873 | 2026-09-10 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c06f8f03-e780-3892-b2ed-72cb4839377b | -6.81399 | -60.13561 | 2026-09-10 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cac23d04-cfb6-33f5-bec0-53b797f9c1cf | -13.2887 | -61.62942 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fcc3f09-bd27-309e-b991-2690c2de0973 | -10.6234 | -68.61434 | 2026-09-10 05:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbca6256-46bc-39db-9d90-2070b7a0c6b5 | -13.28805 | -61.63339 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98c33d73-f053-351d-9e52-7644dd4b14dd | -12.44769 | -57.73731 | 2026-09-10 05:14:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 731abbff-c299-3a37-a02f-94765d8496f2 | -10.62223 | -67.9285 | 2026-09-10 05:14:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e86c7ffe-5092-38c8-a033-446e47f862c4 | -13.22276 | -61.65895 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e557049-2361-3baf-868a-d766fc6ef627 | -13.31526 | -61.64957 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e539b305-cbca-3f68-906c-a677153d7c9a | -13.20237 | -61.82456 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3a980b2-064d-30c4-a618-1ebcfdfd8fd8 | -12.77287 | -62.02835 | 2026-09-10 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c80e6e9-ad9b-3beb-9e2d-e602ec315dc0 | -13.29265 | -61.80609 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4caec983-a4d1-369e-9566-0d99d815f865 | -12.15726 | -64.13503 | 2026-09-10 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1456066d-16e6-3981-8d05-6479efa4da53 | -13.30561 | -61.66426 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea61d18f-73a4-35f1-aaad-c4d799a375f5 | -13.28933 | -61.63288 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 210ebcf5-2e36-32ab-9ab3-1f459984dcf9 | -13.31393 | -61.65751 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 758a0b9f-da59-3dc6-8258-e354a1e623a7 | -13.27604 | -61.61908 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8c69b5d-c3f8-34cd-8999-d9580b558ab1 | -13.32423 | -61.63887 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a62f674b-816a-38e0-ab96-1f908f088ff3 | -13.30977 | -61.66088 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e6f42ce3-4d8d-346c-9073-d36a09b28414 | -13.28999 | -61.62891 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f6b38bd-f69d-3bb2-b23e-1e539f09b414 | -13.22541 | -61.64303 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7129ceaf-ebec-330e-acb0-01a64d6e039c | -13.3756 | -60.41912 | 2026-09-10 05:14:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12ab6781-0fb8-3e12-b0a6-1eb7c9865a88 | -13.32356 | -61.64283 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae16a0a9-9e33-3636-9d14-c4f23ba5ff43 | -13.31044 | -61.65691 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b0f8ab5c-c525-3ebf-9f67-43f671847068 | -13.32555 | -61.63094 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2750f84d-cc1b-36ea-b229-599cbd3ffef8 | -11.70936 | -60.86145 | 2026-09-10 05:14:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27ae0eee-dc3c-3e30-85b4-f0c02d6b8373 | -10.62415 | -68.61047 | 2026-09-10 05:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f57a02b7-97a4-39a9-baba-2cdcadf19c12 | -12.28601 | -57.392 | 2026-09-10 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2579151-b6b1-381a-9470-7fa1a3905f11 | -13.32489 | -61.63491 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9067c04d-f087-3f57-ad89-ea4874870703 | -10.62285 | -67.92515 | 2026-09-10 05:14:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e77b87f-f96e-3b0e-9138-78613eee8149 | -13.2865 | -61.62832 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6d771af-6a53-35e3-9b26-7a79db630376 | -13.2719 | -61.62244 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b09c8a4d-a5da-3d04-923d-e2cd6b6cde9c | -13.28913 | -61.80549 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d2910820-3155-3352-ad8a-1d0f6ebe921d | -13.3091 | -61.66486 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7bfdd92b-22b2-3c0d-ac84-71abe583cadf | -13.22956 | -61.63966 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e471f9e-737e-30c5-bfad-a70aee4bcb93 | -13.23476 | -61.67329 | 2026-09-10 05:14:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5ded11f-c897-3fa4-a8c8-2e3973024228 | -13.32007 | -61.64223 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cae1806f-f9e1-334f-ba41-e030c080011d | -13.31326 | -61.66149 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ea0050c5-a234-3f95-ba06-0c31563b6222 | -12.16132 | -64.13577 | 2026-09-10 05:14:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4b85277-afd9-3316-bc90-b6a1c095c922 | -10.57862 | -68.77051 | 2026-09-10 05:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b598dcb-ef47-3dd8-8c55-ca3ba88b9d32 | -10.62031 | -68.61039 | 2026-09-10 05:14:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| edb29e10-d6d1-3c4a-82ab-2489e1d95ab3 | -13.32771 | -61.63947 | 2026-09-10 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 901585c9-6e10-3894-8ad4-57670ab1f580 | -12.83 | -44.35 | 2026-09-10 05:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8bee97bb-5952-3826-8006-3e1f4c2ddbcb | -12.86 | -44.36 | 2026-09-10 05:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c6899df7-3452-3eba-b5a7-b03291a69bc0 | -12.83 | -44.3 | 2026-09-10 05:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| df5124cc-22f7-30e1-92b6-5d6e0f36fb55 | -9.71 | -43.37 | 2026-09-10 05:15:00 | MSG-03 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 74b06d00-24b4-3095-a4a8-cd342f7c85a1 | -9.71 | -43.42 | 2026-09-10 05:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b80e6f5e-18a2-30ac-a0db-a84e4bf0b3c5 | -3.4058 | -59.2347 | 2026-09-10 05:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| a69082fd-714d-343c-bbac-0abf1d374255 | -6.5453 | -62.8914 | 2026-09-10 05:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 3282922b-da0f-36c5-8d3a-07f9c01f07ff | -3.4058 | -59.2347 | 2026-09-10 05:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7ffede8d-bdac-3b88-a962-c2155de9b5c7 | 2.51525 | -50.84925 | 2026-09-10 05:44:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 795c3546-7ce2-3fe1-96bf-80f979654c37 | 2.50815 | -50.85159 | 2026-09-10 05:44:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1008129-074a-3d8e-8c74-3be41dbdbdba | 2.50922 | -50.85014 | 2026-09-10 05:44:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3567d5a-9be7-3f3e-a432-35c03f2eb412 | 2.50999 | -50.85462 | 2026-09-10 05:44:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 362ae177-9c60-37e1-96aa-6942f932d07e | 2.51419 | -50.85072 | 2026-09-10 05:44:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc2f428b-f9af-310f-85c1-610bd91f1c7d | 2.50072 | -50.99288 | 2026-09-10 05:44:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18085dd3-0709-3358-ba4e-729c445ff674 | 2.51601 | -50.85371 | 2026-09-10 05:44:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c617edb7-4d87-32e9-9c1b-a92da254c6ed | 2.51345 | -50.84624 | 2026-09-10 05:44:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 411b73dc-8438-304d-8a67-0006da70ccad | 2.51491 | -50.85516 | 2026-09-10 05:44:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a307454a-a03a-3cfb-97cc-d3cb038fa8ec | -3.03911 | -59.22358 | 2026-09-10 05:46:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9d9ec31-2325-3272-83af-60c8a685fe44 | -1.70659 | -53.69463 | 2026-09-10 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef268fbc-1b5e-3269-b1ab-087a4846ca29 | -2.72965 | -57.62725 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f118f4d0-dd5d-3d69-8228-cb168f15a0ad | 0.25163 | -51.45995 | 2026-09-10 05:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d85cc26d-3e55-33a6-8f34-8e5aa78836fa | -3.6629 | -58.89999 | 2026-09-10 05:46:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a03b76cb-23af-3290-a11c-1f798ebb6957 | -2.94205 | -50.47925 | 2026-09-10 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57c72050-db54-3b7b-affa-ec1ac92e4a7b | 0.24491 | -51.45646 | 2026-09-10 05:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61d6366f-9401-311f-a77b-91cefb912b06 | 0.24947 | -51.45751 | 2026-09-10 05:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| caef7724-3937-3850-a917-0446ffbb5bfc | -2.7261 | -57.62295 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c4837ac-0a69-3f98-8ce0-6b9dbb017a1b | 0.25016 | -51.46195 | 2026-09-10 05:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c02f50b5-9a9d-3518-b04c-ccf3e22346c5 | 0.2509 | -51.45554 | 2026-09-10 05:46:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 689bc47a-8efc-31b8-81a2-22ac4af9d86a | -3.37341 | -59.43286 | 2026-09-10 05:46:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fda986a-36b8-3d54-af03-d3c0bfbb7dbb | -3.15505 | -60.66031 | 2026-09-10 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b9e7284-913a-3bac-a274-79bb25b9f555 | -2.73138 | -57.6162 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47d0d34a-0dfe-3999-870b-e8ff91b9ec2e | -3.59065 | -59.07446 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d827c3b-93ae-35ce-8d7b-be48aa35158f | -3.15215 | -60.65589 | 2026-09-10 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90469d86-e932-3517-8bac-1b4a1df46346 | -1.72533 | -57.15736 | 2026-09-10 05:46:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebf4b111-96d5-3aa4-8948-37cd119b7ca8 | 1.00849 | -51.10801 | 2026-09-10 05:46:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0f5ec083-597b-3f1f-a4bf-f4ef6171525c | 3.30486 | -61.02863 | 2026-09-10 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ee0489b-d200-3477-b27a-ed77cfe06c55 | -2.93708 | -50.46696 | 2026-09-10 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bddba2ce-00b5-34ba-a6ad-75a78aad5f1c | -3.41252 | -59.22833 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 2b6dbfb8-7427-364c-a6ea-c696f8c907f7 | -3.15624 | -60.65258 | 2026-09-10 05:46:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 273925cf-489f-33aa-9a8d-68081251583e | -3.65977 | -58.89462 | 2026-09-10 05:46:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51ba4f9c-92d3-34f3-85a3-64d862868113 | -2.7308 | -57.61989 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 894f7c07-9bc9-3735-8337-a20115d7cf3f | -1.70709 | -53.69142 | 2026-09-10 05:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccd31259-f7fc-36cf-b8e5-09f171df7355 | -2.93409 | -57.91012 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 531060a7-8572-3a17-b44b-bdbc16be12bc | -2.73493 | -57.62053 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 680672b3-1e88-3ec4-a723-8c7b144dc9ce | -3.40692 | -60.31598 | 2026-09-10 05:46:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86d08ed1-17be-3bcf-8e59-1835436d76a2 | -3.59446 | -59.07503 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5311cc1-d753-32a5-8771-a76776350096 | 1.01378 | -51.10229 | 2026-09-10 05:46:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8ac1405-0b13-3f5e-9e77-ffb471e77ac1 | -3.65905 | -58.8994 | 2026-09-10 05:46:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 823adab2-b230-3077-a3ca-74cde125136e | -1.19053 | -55.71582 | 2026-09-10 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c6be939-f596-33f6-b090-afb32a2a8c78 | -3.36969 | -59.43228 | 2026-09-10 05:46:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48c46ab8-4f27-3760-a419-5b77bf1bf92f | -3.49715 | -59.5751 | 2026-09-10 05:46:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2edb55d-4b72-367e-89b8-c0f665219992 | -3.53909 | -58.9516 | 2026-09-10 05:46:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8671369d-b360-32c6-8005-ddb627396ad9 | -2.73321 | -57.63157 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 31c98f2c-f0b7-37cc-8879-7c8924fbb77c | -2.72908 | -57.63094 | 2026-09-10 05:46:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e1ae06c-4cb1-3fd0-9613-e3d9fe069381 | -2.93622 | -50.47265 | 2026-09-10 05:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README38.md)
