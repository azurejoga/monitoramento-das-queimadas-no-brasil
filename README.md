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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc43aa2e-f385-3a82-a3f0-10b95376142d | -11.6785 | -44.5712 | 2026-07-07 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| ba0bc838-41ee-32e9-a9a2-d9750cca11e4 | -13.7624 | -52.729 | 2026-07-07 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c32101cb-d253-383b-90e1-e2f331b7c696 | -12.7548 | -44.5428 | 2026-07-07 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 7e000dae-2dcd-3872-b0a9-879284e23390 | -4.2811 | -48.3518 | 2026-07-07 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| d44dc3e8-f7a1-3de8-beb6-14c20fc6d3b9 | -13.7817 | -52.7266 | 2026-07-07 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 133.1 |
| cf4cb40d-00d0-3b7b-8238-3f2ac688ff67 | -13.2607 | -54.2456 | 2026-07-07 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c8396ea6-f920-35d0-934e-abea76dc3262 | -6.9135 | -43.7281 | 2026-07-07 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 6888e9e9-50d8-3f34-8a98-32917d892eee | -9.1933 | -45.3114 | 2026-07-07 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| a727878f-0986-3814-bc2e-dc9fc9a50262 | -11.6592 | -44.5741 | 2026-07-07 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 35596d4a-d5c8-302b-abc2-e4307d409941 | -13.261 | -54.2249 | 2026-07-07 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 3778e0cc-dc1d-34db-8c2b-cd7096227069 | -13.7813 | -52.7477 | 2026-07-07 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 19f585cf-998d-3b6a-92e6-7bea332791b9 | -5.8058 | -43.7975 | 2026-07-07 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| e4e77227-0b0c-3921-b370-a9bd07008e26 | -6.9138 | -43.7049 | 2026-07-07 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 4deaf763-9f7f-307f-a870-8a67d4a8c31f | -11.6789 | -44.5479 | 2026-07-07 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 60463dd1-23fc-3fb2-904b-234af46d0c4d | -11.6597 | -44.5508 | 2026-07-07 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 1443bc33-37cb-30db-8805-29dd7d5b1456 | -13.2418 | -54.2269 | 2026-07-07 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 25f10147-3bdb-3044-91f6-9d8f78fccb8c | -6.895 | -43.7066 | 2026-07-07 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 7af967bf-b133-3b7c-a60b-4c4ad21e14cb | -6.9326 | -43.7032 | 2026-07-07 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 458c76ec-e0e4-33d9-8162-37db4c5ed6dd | -10.1913 | -46.47849 | 2026-07-07 00:01:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4f9a9eee-eec8-33c3-b684-746cfa1dbbcd | -13.53345 | -52.91111 | 2026-07-07 00:01:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 6cdb6ee5-e103-3c98-b8b3-0c8ca5026d78 | -13.78811 | -52.74496 | 2026-07-07 00:01:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 5f519a20-6f49-3f22-9ed7-e81a039c5c07 | -13.29076 | -54.35212 | 2026-07-07 00:01:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 60be4eda-a70c-3e65-9f3f-035c28cea5d5 | -11.66637 | -44.54866 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 17ccdc14-c08e-3ecb-8b86-2350f6c1c2b7 | -13.25901 | -54.22976 | 2026-07-07 00:01:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 208ac217-fd2b-3162-9111-356a31cb9702 | -12.75605 | -44.56446 | 2026-07-07 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 15451419-b2ad-3bb5-9b07-d04d4f980a55 | -11.76555 | -47.3436 | 2026-07-07 00:01:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 44826976-c726-34f8-a68a-c82002711b24 | -11.67869 | -44.56749 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| bfba30d1-df2f-3abc-9564-bf25fb9ce291 | -13.32258 | -54.37554 | 2026-07-07 00:01:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 99188976-d101-384d-89b8-3bee5aec7bfe | -11.39276 | -46.57242 | 2026-07-07 00:01:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7c7ccb3e-e0a8-3096-ba4f-0d1f3905b75d | -12.35618 | -47.42723 | 2026-07-07 00:01:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1f7644cf-af9d-3201-8f17-16e7a911b104 | -10.40735 | -46.83707 | 2026-07-07 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d61ec077-829c-3d0b-8f19-a2b5199d39b1 | -12.3651 | -47.42597 | 2026-07-07 00:01:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| dc6838c8-0f93-36e6-858b-e03a5169b7b6 | -11.40904 | -46.62487 | 2026-07-07 00:01:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e6930b31-a69a-3dc8-8979-3a801705f4cf | -13.53465 | -52.91738 | 2026-07-07 00:01:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 36.3 |
| e6b055c1-9a72-38d6-9f08-65720e51cc13 | -10.53807 | -44.12933 | 2026-07-07 00:01:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ec56262b-36b7-34ff-9e8e-9ac34cc20f1b | -13.26201 | -54.25581 | 2026-07-07 00:01:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 2fda4c1d-3de8-3530-9314-8a4d9de6c4be | -13.7856 | -52.71941 | 2026-07-07 00:01:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 00ea75d1-4a90-3c71-b667-00ff05d5008d | -11.68657 | -44.55593 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 34011c97-7ef9-3263-8d0a-f9a380aeca58 | -13.07955 | -48.16746 | 2026-07-07 00:01:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b644c38e-fbef-3211-bce7-15631bef1de2 | -13.22766 | -54.30698 | 2026-07-07 00:01:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| f2e7a4b3-b7e5-3973-966a-0ca90f36604d | -11.69753 | -44.13389 | 2026-07-07 00:01:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 652f78ae-c442-3455-9960-264d5a7d0c4b | -11.85076 | -48.25634 | 2026-07-07 00:01:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f849230f-04a1-3812-851e-020799f2e199 | -10.93461 | -43.06952 | 2026-07-07 00:01:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| c92ba4e2-2a93-3c1b-b4fc-8255d952bc77 | -12.50573 | -48.27005 | 2026-07-07 00:01:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 48dd82bd-3b16-3298-9d88-00d8e7a269c1 | -11.84036 | -48.24802 | 2026-07-07 00:01:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c8612242-b8ab-3144-8301-5897ab011c63 | -12.76384 | -44.5531 | 2026-07-07 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 8c0a5bb9-072c-3313-8940-32e3de8a1ab0 | -10.43243 | -46.88811 | 2026-07-07 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cea6a10b-3c95-3401-ace2-21e2afe62685 | -11.99238 | -45.14032 | 2026-07-07 00:01:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 4fb11b71-06ec-3450-b605-f14cb2a97ed6 | -10.19004 | -46.4695 | 2026-07-07 00:01:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 791aa920-9401-3935-b271-6873f521a627 | -13.23633 | -54.28515 | 2026-07-07 00:01:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 6ecb344c-f0b4-330e-a510-31fae3380f5e | -11.84164 | -48.25758 | 2026-07-07 00:01:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f15738eb-079c-3c64-b7d7-4c4a86f3358a | -13.26516 | -54.24995 | 2026-07-07 00:01:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 296f1895-7dec-390a-93fe-dca4d804d922 | -12.36386 | -47.4168 | 2026-07-07 00:01:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a0574982-a793-32e3-b468-22f9cb497d94 | -12.68211 | -48.21346 | 2026-07-07 00:01:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4a8d922e-e2a3-39d6-8079-fc96c243f2d8 | -10.92424 | -43.07119 | 2026-07-07 00:01:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c6f8fcb9-5610-3184-8be4-fcb745d87995 | -11.67721 | -44.55737 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| f960a2c7-912a-3ed4-a791-c7e3a32c380c | -10.76551 | -46.63295 | 2026-07-07 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3dcc0f38-e622-3810-8b26-343c6839a4af | -11.65064 | -44.5718 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 992476b9-e501-3d4b-a235-8dfb4ae44a8e | -11.63105 | -46.36326 | 2026-07-07 00:01:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 340f4860-60f4-38c4-9e92-378833d6858d | -13.77533 | -52.74654 | 2026-07-07 00:01:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| e4519b5c-5145-3e46-a322-c6d338140766 | -10.93272 | -43.05688 | 2026-07-07 00:01:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| a26f388c-7163-3a5a-bff5-a3abe145fe1f | -13.08874 | -48.16619 | 2026-07-07 00:01:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 517c6feb-f4cc-3ab0-be93-f0e6870cd9c5 | -12.50444 | -48.26032 | 2026-07-07 00:01:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f5943f7b-bd39-3e54-b9db-59d3423ec228 | -11.65999 | -44.57037 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 2a7ed39a-b212-3ecc-a167-2b785fc5d37d | -13.78778 | -52.73947 | 2026-07-07 00:01:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 270b9f5f-df88-33a4-be08-8766b47d04fc | -13.54635 | -52.9095 | 2026-07-07 00:01:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 73e8b2a0-5d82-3286-a13b-d6cd464d1368 | -13.54755 | -52.91577 | 2026-07-07 00:01:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 725579ce-10cf-334e-a9d7-25ac5670d003 | -11.68804 | -44.56606 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3746987d-dca7-3982-8c48-2643ba7b2a4f | -10.39851 | -46.83835 | 2026-07-07 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 225c8775-2be3-3416-a654-387157f3cd14 | -13.08084 | -48.17732 | 2026-07-07 00:01:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0d4a4e10-11d5-320d-b840-33f5ded7b4c9 | -11.6585 | -44.56023 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| a3c2f989-033b-3323-95af-08a452f6ad0d | -12.75459 | -44.55453 | 2026-07-07 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| b47b364c-c7dd-323b-80eb-d2e0bef7d08a | -12.34185 | -48.22023 | 2026-07-07 00:01:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d4f04235-4a97-3ab9-b2b2-7ff44a043896 | -11.64914 | -44.56167 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4d40dd47-c7d1-37b8-95f7-dfc94e3bf55f | -10.41619 | -46.8358 | 2026-07-07 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 61853ff4-e240-377f-8de9-f6532648c4be | -11.67082 | -44.57906 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 91eef4dd-186e-3120-a7e5-06e52df0adb8 | -10.82792 | -49.37563 | 2026-07-07 00:01:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2df36d0b-844f-38c3-8637-7a559ef64670 | -13.52098 | -43.99495 | 2026-07-07 00:01:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| da16059b-16d5-3a34-8d88-eaf6201fcbc3 | -10.19256 | -46.48748 | 2026-07-07 00:01:00 | TERRA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 61258a62-c3c4-3e27-a6d1-2bb263dc573c | -10.40859 | -46.84601 | 2026-07-07 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 5a59a0b1-f194-3045-9fb1-8c99ba211dc1 | -13.78576 | -52.72482 | 2026-07-07 00:01:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 232.5 |
| 1631748b-2898-3a7b-8d7f-91dcc5a5cdf1 | -10.76427 | -46.624 | 2026-07-07 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2ac2664f-5a91-3f34-b4a1-dd3cb4997486 | -13.23922 | -54.31079 | 2026-07-07 00:01:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 100b354a-644c-3d38-a4ca-4c3a3d450177 | -12.76529 | -44.56303 | 2026-07-07 00:01:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 880b736a-1ac3-39dd-a143-807dcdac71be | -13.27635 | -54.35387 | 2026-07-07 00:01:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| f2f560f4-4712-331c-90a5-649f4b89a906 | -11.66934 | -44.56893 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| bf179d6c-5c60-3717-a7d1-b6074a4cdb87 | -11.68017 | -44.57762 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b3866f63-8d28-3354-8678-6d73aa046a8b | -13.77301 | -52.72639 | 2026-07-07 00:01:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 238.2 |
| 541aa5c1-1c5b-3129-89b6-3446ff639af3 | -10.69392 | -49.61102 | 2026-07-07 00:01:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 968c040e-812f-3a92-b917-41a094022b7f | -11.65701 | -44.55009 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 19007527-c7cb-32e5-b3bc-33e0249add7d | -10.39975 | -46.84728 | 2026-07-07 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| aad6dbc8-3a93-30cc-b5e2-b5207b8ba010 | -13.32482 | -54.36877 | 2026-07-07 00:01:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| fe4f8096-cc30-3eb0-a7fd-2f03efbf7980 | -10.41742 | -46.84473 | 2026-07-07 00:01:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 44f46d88-283d-3dd2-b6ef-70637a1888b8 | -13.26235 | -54.22398 | 2026-07-07 00:01:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| ae0b390c-696c-3fc6-b826-b55b17eaae09 | -11.67573 | -44.54722 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 54578bf1-1ba2-35fb-858a-b8645b5d9ccd | -10.53647 | -44.11835 | 2026-07-07 00:01:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f89d8811-18ff-30c4-87e6-3e9eb825d7c8 | -12.35494 | -47.41806 | 2026-07-07 00:01:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 08ee29b2-bca1-3018-b4fc-3617e3c4a167 | -11.84948 | -48.24674 | 2026-07-07 00:01:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 35e0bbfb-1704-3eae-b4f8-c641c424ed19 | -11.66147 | -44.58049 | 2026-07-07 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d7a4bcdb-7777-340e-832e-5673f852998e | -11.86438 | -45.60376 | 2026-07-07 00:01:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README2.md)
