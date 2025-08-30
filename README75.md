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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa4ba74e-f7ed-3027-ba3f-b2f432baa717 | -13.36354 | -47.02262 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e548cdb3-a817-3e98-85ed-93106f75dc00 | -12.69613 | -48.14112 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a4a5ef5-c533-3953-8b0c-54d454d77f55 | -10.06866 | -62.90119 | 2025-08-30 05:12:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9b606cc-bc90-31a9-bbc3-a53b79283c14 | -13.39224 | -46.99513 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f0e517e-cdb8-35b3-bd10-ea1e04e2f7ed | -11.31486 | -55.20761 | 2025-08-30 05:12:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efd91f81-65c4-30a9-b104-0c05af578d4e | -9.77263 | -64.25201 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98d437ed-d38d-3ddc-85cb-1d80d98b6a2c | -13.50782 | -46.84048 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfe5f83b-5324-3635-9715-758d36051cdf | -12.82379 | -48.09554 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b710e0e2-0448-358e-98c5-299572813013 | -13.67585 | -46.92122 | 2025-08-30 05:12:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 814984d3-1f79-3da4-8095-16e129f47fdd | -13.39012 | -47.01487 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ce739e7-3c75-3535-9c55-a96e2438b49a | -12.93356 | -48.11606 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d8738b9-64e5-348c-8a98-020ad2f0d3b9 | -10.86958 | -60.80505 | 2025-08-30 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f4cd418-6afd-36d9-acaa-08b096c0fe2c | -8.91157 | -70.60107 | 2025-08-30 05:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72553457-38f4-3a62-9cd3-a8511934a324 | -13.37389 | -47.02463 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 125f743a-1c68-3866-be0e-c88f8a515f47 | -9.71872 | -64.53629 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5be1f9a-d3da-3ed7-8147-cbd0f468db6c | -14.2368 | -48.06791 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e2aa9ce-e0e9-3da5-9454-88ef982116e4 | -8.84488 | -70.62872 | 2025-08-30 05:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07557c8c-069a-3e12-8f4d-cea5c28b424f | -12.9909 | -56.91682 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5217ca6-950c-3a28-91ab-ca8e900e610b | -13.38135 | -46.95891 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47c1ee47-a352-3723-ad3a-056e307ede8d | -9.54308 | -65.70093 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e1b0633-b9f3-3236-a0bb-dc17ea321d14 | -13.49476 | -46.84075 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c181f37-795b-356c-a48e-3cf72858e852 | -9.32904 | -68.21689 | 2025-08-30 05:12:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e22e1d95-dd5c-376c-ae82-0361470a70bf | -8.85256 | -70.62433 | 2025-08-30 05:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e82cd53d-0c98-35a1-8996-8c32f839f358 | -12.93253 | -48.12525 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c56d9bce-0185-3338-9e83-f24c72e09122 | -13.38998 | -46.99654 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a3e3f675-c26d-3045-853d-34e850832215 | -12.8264 | -48.08995 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f160285-a423-3d07-a6bc-288dd3615a6c | -12.82665 | -48.12317 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 159d0b92-c413-33a6-8599-612202cf808c | -12.9261 | -56.97749 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46fd122e-ce5c-3b36-9c4d-041d849c0655 | -13.35851 | -46.87373 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6df44ae-2b04-3f32-82d0-6bf0d39ab701 | -13.49683 | -46.94404 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 06fe31c0-513e-30bd-8e2e-e084593565c0 | -11.74083 | -51.75606 | 2025-08-30 05:12:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0f30858-5019-3679-a8b6-4a42bb07a162 | -13.35249 | -51.773 | 2025-08-30 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81504ec6-8622-3d5e-983f-0a20c2d6e7ee | -12.93345 | -48.1305 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04f79881-8904-36a6-b53e-c852fbfc8d4c | -14.23898 | -48.0694 | 2025-08-30 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bbe8836-c3a7-398e-9d90-cd3c26486de1 | -12.92154 | -56.98449 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15200098-b7dd-37f2-829b-75744d40c31e | -13.36512 | -46.98827 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 522bcf28-dce5-346c-a3ae-8b48a7400132 | -11.39614 | -63.25812 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e4a2e4c-1158-3da3-98db-3a0d1ce80496 | -12.62807 | -57.0053 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aeea5f89-56b5-37d2-a51f-d3212768eedd | -12.85088 | -48.17255 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff59594d-17ce-3cab-b794-80b2e840a51c | -11.39098 | -63.24158 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2810ff7-56e9-3c9a-91b9-33a0c9103bec | -13.3694 | -47.02796 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df395ab1-5cc1-33be-975c-4981de35ace4 | -13.67633 | -46.91683 | 2025-08-30 05:12:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 887ca44e-041e-3a5a-b81e-905fef656c96 | -12.93942 | -48.1306 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e080427-da49-3d0c-b5f5-88df6d1a3a38 | -11.35588 | -63.25895 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc3f7556-1855-383f-8577-2d8a1afa1353 | -12.83012 | -48.09245 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73761815-c3aa-340d-aa02-1b1eee51ecb8 | -13.36981 | -47.00385 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8a34b937-48fa-3d07-91d4-29c08a941746 | -12.82274 | -48.12064 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c7806b7e-4c7b-3891-87f6-5cf7d8746faa | -13.36396 | -46.88311 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 906b7b35-2256-37f5-a92f-427628ab56c4 | -13.19454 | -45.28017 | 2025-08-30 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08b25093-6ee1-332d-ae53-572fb2bdbdac | -13.50337 | -46.94334 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4125ec4d-c369-3a30-81bb-9fbe1adf0b75 | -12.8504 | -48.17672 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2ccee56-d002-34d0-b651-2ca4f896a72b | -12.61236 | -57.01531 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fbc80e9-8b9a-32d3-8c15-a7180e25de03 | -14.25171 | -45.24376 | 2025-08-30 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2bc963cc-8338-376c-9c9b-970ccad5fde7 | -12.61634 | -57.01207 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f6be9a9-1033-3bb2-9e6b-00cd0cea7032 | -9.33393 | -68.22185 | 2025-08-30 05:12:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6ffede4-09bf-360c-86d8-382517c24a62 | -13.39529 | -47.0065 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0912a778-c29c-36cf-bc40-67cdead255af | -12.82967 | -48.09643 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b0e2a24-ab6f-30e3-9fe7-ef8c21de445d | -13.37631 | -47.02356 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 506221b4-4666-3d40-baa9-1bbe818c8a98 | -9.77334 | -64.24792 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72c162b0-e075-36a4-b16c-075bca46f562 | -9.7243 | -64.91191 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a156f8d7-6b6e-3d71-ba94-8bc35c306188 | -9.54873 | -65.69666 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5530ee94-2c10-37ad-a0e9-1dca70ae5a4e | -11.29723 | -63.31672 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bda9810-7395-3f86-80a4-83fbbde1a3ae | -12.93394 | -48.12637 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f7644d90-8350-3358-87c0-5821a3ad8058 | -13.98211 | -46.32516 | 2025-08-30 05:12:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c23c5d65-2b5d-3419-b050-01d68c1b0fb9 | -11.39401 | -63.24731 | 2025-08-30 05:12:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4580383c-86ca-3639-8033-948f17beb506 | -10.23937 | -68.09177 | 2025-08-30 05:12:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4846c1a2-2a4e-3a1a-944e-4cd1c1e50767 | -12.92667 | -56.97371 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ede0449-d9c1-3665-9c8b-4ab404cdc18b | -12.83255 | -48.12385 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12c48bcd-d67c-3f86-ae5d-61f30f14dd80 | -12.9819 | -54.75934 | 2025-08-30 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5406ceb6-a8cc-3031-b630-17cacbac59a6 | -11.31598 | -55.22535 | 2025-08-30 05:12:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 390fb699-eac4-3ce0-a9a4-ebfcf1be7917 | -13.46678 | -46.96319 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| baaa3d72-50ca-35cc-b1b0-fc85a34b2ceb | -14.10454 | -51.77691 | 2025-08-30 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30f236d6-baae-36be-8187-11e71106fdb7 | -12.82118 | -48.11872 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d3a5a76-91fa-350a-88cb-290b798901e9 | -12.62751 | -57.00908 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe3f7c9b-4501-3067-ad37-4b724cf022ac | -13.4741 | -46.95554 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59a3d9e7-ca8e-3f62-ab48-ca6378fb08cb | -13.65616 | -46.92307 | 2025-08-30 05:12:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e69991ec-d91d-3770-8e3e-ece4f1cfd31e | -13.57067 | -46.92063 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faa41b29-f92f-35e4-9d64-f47a9503a110 | -14.25882 | -45.24455 | 2025-08-30 05:12:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8afadf2-50b7-3a2b-aeae-35df4e28299a | -13.57891 | -46.90489 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a67fc8d-9b0e-359c-8cf3-291c05a2b28f | -13.97491 | -46.32959 | 2025-08-30 05:12:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c967b56c-90a3-3925-b29e-80160f1a9871 | -11.37557 | -54.33797 | 2025-08-30 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e9ee3fb-1e8b-3097-a118-4a14a0f06c00 | -13.35755 | -54.38554 | 2025-08-30 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a78837e-3f8f-3139-9ad2-f2bc323d60ee | -11.31849 | -55.20817 | 2025-08-30 05:12:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09f89dc6-6665-3d28-83aa-2c3016db9e0d | -13.35915 | -46.86803 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee59eb60-1fe0-35ea-8afe-4490c90544da | -12.62012 | -57.01177 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88790a3c-f8f5-3783-b2aa-815975499870 | -9.77192 | -64.25611 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abeb3ec8-3c93-3eee-a68e-73cde1ce822a | -13.38945 | -47.00116 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0cf6e804-fcd8-34de-9d2d-2e05f8c3e681 | -13.5017 | -46.94047 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf19797a-fc3a-332f-8b91-ba73205787db | -9.77833 | -64.24459 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80861158-7c53-3f96-ae6c-7bd27d532eb2 | -9.78548 | -64.25436 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fc33007-0ead-3fe9-a96d-8906597bad3b | -13.97808 | -46.32533 | 2025-08-30 05:12:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d9108dfb-6e09-39bc-9ba3-063fa33ea4cb | -12.84994 | -48.18066 | 2025-08-30 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b90b7233-3c34-3845-b5c8-339a1ff20d03 | -13.36458 | -46.99302 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 34c02d18-f13d-32f5-a1bf-9b7a4ee870aa | -10.355 | -64.46811 | 2025-08-30 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1d87b31-8626-3ad7-930e-5f479d36dd34 | -13.57121 | -46.91578 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bd094af-d1fc-3f26-9df6-40d8088ed887 | -13.38156 | -47.03456 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcfb84f9-e2d7-37ff-aa06-40935e3449b8 | -13.46767 | -46.95517 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c9f91ee-905a-3ab5-a809-9e300766bd9e | -9.67589 | -65.02616 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 787cc28b-406d-38ef-a124-3f8cdaf184cf | -13.35805 | -46.87791 | 2025-08-30 05:12:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff40bca6-42e0-3aab-b53b-4f829d0bce77 | -9.78761 | -64.24203 | 2025-08-30 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README76.md)
