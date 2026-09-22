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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3995f2f6-5f05-30c9-b408-724845b69048 | -10.5748 | -46.7296 | 2026-09-22 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 421226d1-e864-32f2-9bbd-92836b7d6bfc | -3.6033 | -60.5664 | 2026-09-22 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 27da3b37-ebaa-3809-b8f5-7549f8e90c85 | -12.8526 | -50.91 | 2026-09-22 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 1d6e2b50-0463-3289-8614-fb0b3741d11c | -3.4599 | -59.5209 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 650d7b5b-4333-358f-b36c-0913fbfd6f55 | -5.8675 | -49.7864 | 2026-09-22 15:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 17d29bdb-243d-3d54-b3ac-9b6b4a4db797 | -10.8189 | -50.8436 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 87cb4d0b-f781-34ce-8bd2-9a8a0d4c71c2 | -1.6583 | -54.913 | 2026-09-22 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 8fadb35d-48d7-303e-9752-871c8b417b92 | -3.2372 | -60.8007 | 2026-09-22 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2d3ab431-d65f-3b1b-aa16-cfe820b9ec42 | -3.3001 | -57.8487 | 2026-09-22 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| a047ecf6-eef2-3a80-9a82-43a477211f9a | -7.1203 | -43.7323 | 2026-09-22 15:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 1c16ec43-2772-3003-8944-95452d01840a | -8.7517 | -45.8587 | 2026-09-22 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 40846044-0e9d-3f0a-8aaf-6740bdc17ab4 | -10.2446 | -49.986 | 2026-09-22 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1dcf840d-ac9f-3134-aa7c-df3041f85e50 | -10.744 | -50.7876 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 24d1287a-0106-3829-af41-14f32ebdca93 | -8.7703 | -45.8793 | 2026-09-22 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 092e7b82-56e1-3f9f-a385-9f6b57694f2c | -10.4483 | -50.2858 | 2026-09-22 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d253d51e-4c71-37a5-acbf-58c6d1343e71 | -11.0991 | -54.0285 | 2026-09-22 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a6fb9745-2adf-3b71-8f49-0879c7fa7011 | 2.2923 | -50.9377 | 2026-09-22 15:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fa5ea354-7913-3c07-a039-a55b39082f48 | -2.9525 | -57.72 | 2026-09-22 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a56a0c28-dbb0-3a5a-a687-e795e98e34c3 | -10.1182 | -45.5434 | 2026-09-22 15:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 8eec258e-66e6-3b26-a0c0-a617c15c14f1 | -3.4463 | -57.9424 | 2026-09-22 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 5d38b30b-5984-3429-8261-0307d464ba1f | 3.5481 | -60.6813 | 2026-09-22 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 32e7ae78-f02a-3025-a33c-4dfcea4c9bdd | -11.1184 | -51.0879 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 2776cc7a-84d0-3cc0-9d8d-f0445c57b618 | 3.7498 | -60.4684 | 2026-09-22 15:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 80.0 |
| d200e8aa-8512-332c-a22a-d10494b1fb1f | -6.9868 | -47.5104 | 2026-09-22 15:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 3714d077-ad64-3fc1-a6b8-96c1c01bca3e | -6.3012 | -59.9962 | 2026-09-22 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8318ea9a-d3a0-3da5-9314-6461fc939d76 | -10.7251 | -50.7896 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 2764f626-d2d2-345e-a136-e018b037fdf7 | -3.0535 | -61.2578 | 2026-09-22 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6c0a3246-34cb-3a46-ace1-2d756fe4d785 | -3.3625 | -50.7629 | 2026-09-22 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f66d9b91-25a8-3b0b-b1fd-cbafa401ccaa | 3.9354 | -59.6063 | 2026-09-22 15:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 315a1e79-b092-3fdb-a326-e8639d4047f5 | -11.8559 | -49.979 | 2026-09-22 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 5a700501-b16b-38db-8949-e4572c5681d5 | -3.1514 | -58.644 | 2026-09-22 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f3e30bec-1442-304c-acbd-8be6c3938f91 | -10.913 | -50.8762 | 2026-09-22 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| ca2e218b-0166-3a0d-9465-bfca03122f92 | -8.0466 | -61.3237 | 2026-09-22 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4a7f1741-17ad-34da-b9ee-6418966e77b8 | -8.1101 | -44.4211 | 2026-09-22 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 7134db27-752b-3de8-b2a0-651b2e8e1e59 | -5.9518 | -59.9701 | 2026-09-22 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 36f011be-dccb-35d1-97d0-c426bf9cd7e9 | -9.859 | -46.4114 | 2026-09-22 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 232.1 |
| 06a73f09-dec1-36bb-95fc-6b29cfd77cff | -12.8 | -44.2073 | 2026-09-22 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 0f4ed9d1-fdad-3699-b701-20d3068a05d8 | -3.3311 | -59.8101 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 39c2b9ac-367e-37af-894d-b3e782c14213 | -6.9841 | -49.7777 | 2026-09-22 15:10:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 3adf1e99-83ca-3677-a4b6-4dd9e1c2f50b | 3.9356 | -59.568 | 2026-09-22 15:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e0c54964-45f9-3dd6-aa0e-3e77904f2c46 | -3.6449 | -58.8647 | 2026-09-22 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 62f894ce-5066-3235-9745-02f6061eda32 | -3.331 | -59.8483 | 2026-09-22 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| c2b9b109-9413-3eda-965a-06fea2548d9b | 1.5836 | -55.7856 | 2026-09-22 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c572fca3-303f-3b02-ab61-6544ffb55b98 | 2.2187 | -50.8769 | 2026-09-22 15:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 11f6ef70-727d-34cd-a76e-9fc3a09fbd64 | -9.7883 | -46.0593 | 2026-09-22 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a7b253c3-7d36-3c96-8e9e-1ef15fa73d94 | -2.9997 | -60.8047 | 2026-09-22 15:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| bcbd5fab-fe52-318e-9a39-1fd067201836 | -2.5687 | -57.5135 | 2026-09-22 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fa16fe6c-bcd7-3ca8-99c1-5c43d88a3351 | -7.785 | -44.8212 | 2026-09-22 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 6ad27a45-7ab8-3351-8089-17d7540e407c | -3.6997 | -58.9019 | 2026-09-22 15:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| fbd31d29-7c65-38cc-9459-baa3d5a7ef98 | -7.2811 | -59.5159 | 2026-09-22 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| dcbcfe71-2cc9-3526-b7f3-e63fbbac5a0c | -3.6065 | -59.4413 | 2026-09-22 15:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 29378b79-ff22-37e3-85a7-0188b4deb8aa | -8.7916 | -44.2778 | 2026-09-22 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 7cd65549-8154-31e7-98d7-ef9c4680a67f | -11.3813 | -44.0554 | 2026-09-22 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 342.2 |
| d5b88dd7-7f84-385f-b248-26714ea049fb | -9.84 | -46.4136 | 2026-09-22 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 88229c7b-af48-336c-8097-5cfc1ccab473 | -6.0926 | -57.6652 | 2026-09-22 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| eba8188a-9529-3187-b6de-56dc3e40df5b | -6.0925 | -57.6847 | 2026-09-22 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 310.0 |
| 8ece2440-9611-303b-a94b-793df6243c0c | -6.0924 | -57.7043 | 2026-09-22 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 4b271e74-11be-3fcd-abbe-b88634ce0d9e | -6.61 | -59.89 | 2026-09-22 15:15:00 | MSG-03 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c7c13df0-63ce-3a8c-b7a8-2e436b6bc18f | -12.35 | -50.14 | 2026-09-22 15:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c7657b4-ce52-3b34-b5df-123d07d0a513 | -12.32 | -50.13 | 2026-09-22 15:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3411e61b-583e-3b28-aa35-f533265683fd | -15.81 | -42.05 | 2026-09-22 15:15:00 | MSG-03 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0bef2ce5-ac52-3368-a1b7-ad5335faab61 | -14.7 | -45.64 | 2026-09-22 15:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef7d5296-ef74-3ab2-a9fc-3553011f83a1 | -12.35 | -50.2 | 2026-09-22 15:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58dd54a8-62f2-3b30-b6e9-c2103e9ca92c | -6.21 | -41.67 | 2026-09-22 15:15:00 | MSG-03 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 901ccdc2-65f7-3d35-8dfc-7cff0382ec20 | -6.64 | -59.9 | 2026-09-22 15:15:00 | MSG-03 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a504a82e-17e0-3d76-9042-d8c87b9fd1c3 | -4.66 | -42.07 | 2026-09-22 15:15:00 | MSG-03 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 43135cab-d8ee-3620-ab6a-7f3e8439b3af | -15.84 | -42.06 | 2026-09-22 15:15:00 | MSG-03 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f7e83c32-b70b-301f-9526-0b0366904253 | -4.66 | -42.11 | 2026-09-22 15:15:00 | MSG-03 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b562b9f9-cb60-37c8-9c0f-a3e3c5b9e85b | -5.9152 | -59.933 | 2026-09-22 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f76fea0f-4119-330a-9ab8-6898da8ff848 | -9.859 | -46.4114 | 2026-09-22 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 179.3 |
| d7e68a8e-05de-3a87-9e65-0397931ec726 | 3.6753 | -60.9632 | 2026-09-22 15:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 64b2f280-44b1-3f87-a4e2-afff09ab83c6 | -3.6033 | -60.5664 | 2026-09-22 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 34ff48be-8e77-3b80-8251-6d12dab6fc11 | -3.6763 | -60.6029 | 2026-09-22 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 0a744c96-05f3-3c38-a491-0b46ae0e1b87 | -5.8678 | -45.2346 | 2026-09-22 15:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 662c63f1-4c5a-36a0-afc1-76c9e0cc621a | -10.3735 | -50.2294 | 2026-09-22 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 2c0b81f3-de75-3218-8f04-05fad224abe5 | 1.547 | -55.7466 | 2026-09-22 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d9000191-4460-3e42-9721-bf2e4e22f273 | -6.5953 | -45.4727 | 2026-09-22 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 9d367b44-c062-3815-871f-e2484f47957a | -6.295 | -57.735 | 2026-09-22 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 64ea9a38-506a-387a-b338-8cd127d31442 | -11.3784 | -44.2195 | 2026-09-22 15:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 174.9 |
| bec576c9-c7f6-35a0-8d7c-31feffcc4472 | 2.4212 | -50.9557 | 2026-09-22 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 18b37534-e945-3e70-a63c-dbac3e081aeb | -1.3742 | -49.3154 | 2026-09-22 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| b3303080-cbde-3ded-b529-31b44045ea44 | -6.3135 | -57.7342 | 2026-09-22 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 549c7938-a8e8-3d6e-8792-c0d0fd05b54d | -3.7313 | -60.5638 | 2026-09-22 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 882f0c09-32d6-34c6-9989-2a1ac7bc2b6b | 2.4028 | -50.9561 | 2026-09-22 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ebced1a9-13d0-38ca-a734-37a83f26b185 | -10.6881 | -50.7297 | 2026-09-22 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 156.9 |
| ce3a06d7-df0c-37d7-985a-83dc0e22fbb7 | -6.5763 | -45.4968 | 2026-09-22 15:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 0870d50e-e6f3-38df-82d4-7a0cf0d8c4a0 | -2.4206 | -58.2712 | 2026-09-22 15:20:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 356c7cd2-35ce-3d05-9856-d96a354014ef | -11.44 | -47.3579 | 2026-09-22 15:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 9e98db59-0966-3b21-a0de-59115edc9bdf | 3.859 | -60.6561 | 2026-09-22 15:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 3874a540-13ce-3a6f-becc-fea2a82b64c4 | -3.3001 | -57.8487 | 2026-09-22 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 90badeea-12c8-3013-b49b-8f350454bc61 | -2.9906 | -57.2137 | 2026-09-22 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 681e796e-4162-37be-84c4-354a3e5090d7 | -3.331 | -59.8292 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 0d8ada4e-2aae-3ff9-b801-38a73e1e6755 | -3.6764 | -60.5649 | 2026-09-22 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| ee37202c-fc59-3d43-8634-f6ab868d34ab | -3.3494 | -59.8097 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 05e72dbd-14cf-3a7a-9b73-a1712ca54d3e | -6.2018 | -47.5902 | 2026-09-22 15:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| eccac528-251c-3b14-bcc6-85fab209bf91 | -8.0466 | -61.3237 | 2026-09-22 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d88f1081-b9ad-359d-bfd0-dd575af79a8e | -10.3732 | -50.2508 | 2026-09-22 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 2c6fcf76-c27f-38ba-8ba2-76badb68a63e | -6.0924 | -57.7043 | 2026-09-22 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| fcbefe2c-75b9-37f1-a370-e61187b21383 | -5.8675 | -49.7864 | 2026-09-22 15:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| fb24fbef-eb26-3494-a8ad-cdb2f32bc56b | 3.5481 | -60.6813 | 2026-09-22 15:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |


[Clique aqui para ver as próximas entradas](README149.md)
