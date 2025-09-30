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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b05eaf35-4237-3b76-91ad-36984f29143e | -11.37457 | -45.07047 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fc4e264-23ab-30b8-82b4-c16fd7fd04ed | -9.54545 | -47.77279 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5beaf750-2d8e-39dc-b616-2d6356655380 | -8.07365 | -55.22296 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eba957f1-87b1-399e-8967-cea81083f736 | -7.91598 | -44.60317 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80b6fbd8-9d43-39a4-b1ad-5419ffe5176f | -14.39547 | -47.14601 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88c0ec15-353b-37f5-816b-e422bb3110a8 | -7.52203 | -46.68864 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d530f24-6c3d-3c11-bf91-4ab5a4040201 | -13.15671 | -47.42474 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3eaadac-8a35-3035-9487-dbf96353d002 | -11.06564 | -47.82845 | 2025-09-30 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d4937165-8a33-32ba-b630-fd3016aadd71 | -13.36302 | -47.81437 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ada8dc69-721a-32ab-a09b-27bd2d566e5a | -10.60575 | -49.63921 | 2025-09-30 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69ed58aa-93d4-3154-9a2b-691a98bb1f73 | -13.174 | -49.14489 | 2025-09-30 04:40:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8adb8ac-2026-3dd7-8338-6658fe01c590 | -9.46031 | -45.48344 | 2025-09-30 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c42a917-34c1-3b82-9b2c-792180a0899f | -11.97787 | -46.57905 | 2025-09-30 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7faf7a9c-129a-3b5f-ba89-21a0c2ca282c | -9.98756 | -45.41584 | 2025-09-30 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 632b89b8-d2d7-3e4a-8811-db045319b28a | -11.41043 | -44.90014 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec65ce32-def0-3964-9390-6eb694388f59 | -7.76997 | -45.76014 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52a9d5a4-49fe-3d23-93aa-f9811a718c6d | -8.11322 | -54.86909 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4493221-4018-3b20-bf08-3da3b30dfe69 | -8.54682 | -44.67165 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa5d6935-e4ba-3c6d-9f9a-69db163e796f | -11.15575 | -54.12329 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 4d6734be-7a4d-3566-a602-599b1ce9f5c4 | -11.69666 | -44.47451 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56acfa7f-0221-3df4-99e7-b80e1b78a2ad | -11.26388 | -47.22875 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40a50119-c532-3f70-8af9-df67822e2888 | -10.88831 | -53.75149 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09788399-5c65-3f80-810d-7097f6e11046 | -11.40626 | -44.89923 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89c800d5-4a36-3ee0-8658-c334645ce452 | -7.36567 | -47.05011 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f60f693-8779-3633-af1b-af1075f84021 | -10.81106 | -45.3631 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af750d7f-a1c9-3c0e-8f52-9f1f7693e2ec | -12.82018 | -46.99673 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7a072ddd-eee7-3e40-b989-89650288499f | -12.02534 | -49.716 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 247dc916-407f-3af4-ac46-f7ce0d214fbe | -12.37138 | -43.20692 | 2025-09-30 04:40:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 215b5a6d-14b8-3a5a-8ed8-b2b0ec7e0cba | -7.5081 | -45.45588 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f9bd4d08-b2ec-377e-80e0-0fe2ce283b35 | -13.49918 | -47.39949 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 332096d2-b0b1-3d42-b011-bec9993e0ef6 | -13.24757 | -48.43885 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6265fa0b-4341-362e-b49c-ce214fa4dec7 | -13.23797 | -43.3739 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8d723213-0de0-389b-9563-9bee6f80d628 | -12.69553 | -45.28698 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6345671d-d062-3549-98c1-3409b2a0c935 | -7.61304 | -47.3333 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50849a7d-c1df-3c04-8800-b99fb68d70ec | -11.74816 | -46.83949 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbb89df9-60b2-38b0-a5b1-f652c1bfbafe | -13.84887 | -47.49292 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14182e95-6a33-31cc-892d-a3f325704080 | -7.77033 | -45.73173 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e549f9a0-3d7d-3200-88a9-92b49b82b835 | -13.65874 | -44.39604 | 2025-09-30 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91103bc2-a6d6-3e05-b791-6fc2230caeae | -14.38404 | -47.14455 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a6f0d54-3b78-357b-914b-60b16644baf5 | -7.76964 | -45.7364 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db4e7b54-dda1-3c3a-8603-821b255e8fdf | -12.695 | -45.29086 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c2a4898-9478-30b9-a1a9-69d389fc13bb | -10.39347 | -48.16464 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f6f554b-0e15-3d1f-8853-ffe4fc3f4cf5 | -12.95262 | -48.40795 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2e13c2e5-68e2-3678-b969-bbc6836981ef | -13.63233 | -48.03735 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c89ce2a-f153-3841-ac73-73aa420b2a27 | -7.85237 | -46.75578 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efdf6778-1cd1-3e25-ad10-30ffe05bb64f | -10.1847 | -44.90169 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5bae135b-b6c4-3381-bbc4-b34967c635f0 | -8.14194 | -46.37475 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 60254b59-c847-39ac-ba93-cf94b5c068a7 | -13.78261 | -47.85923 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ad28b02-1528-31c9-9698-953c49a2b55e | -9.82225 | -48.95884 | 2025-09-30 04:40:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 113bc886-f0af-3581-b6ed-f66efce68df7 | -13.36665 | -47.81485 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5315dc91-2808-3926-ad7e-5bb3dd26dc95 | -11.03431 | -49.81508 | 2025-09-30 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adbad018-ee57-39ce-9e3f-0ccb5c696a19 | -8.8351 | -46.18449 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 16a6098e-40de-375f-b02e-62c10cb6716d | -14.14578 | -48.87637 | 2025-09-30 04:40:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e73053a1-55a8-366a-8cc3-751526312066 | -10.19519 | -52.55844 | 2025-09-30 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d654131a-6fb5-3445-8fea-9ad18832824f | -13.86236 | -44.41457 | 2025-09-30 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5e6742b-8b30-3c4e-8433-ce8fa400cf3d | -8.22955 | -45.50622 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f10d8a64-3df9-3b7e-af19-72d4f9ca1bcf | -13.78128 | -47.94741 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 00f59018-a61b-3e3a-af36-3a0bcf90775b | -13.56949 | -47.30278 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d097a0e3-79b5-3d23-9c8c-f815a35095f0 | -7.51845 | -46.68811 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3552448-04c4-3999-9df3-5179e78c9f61 | -10.84073 | -45.41584 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2ac45e0-b959-35cb-8d2e-30ea23f6fe91 | -11.67247 | -44.28691 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbf2e8dd-a739-39e4-b91c-3db7700bd8db | -14.72452 | -45.23804 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae2abb99-903a-398e-90f0-b0f6a5826226 | -11.44159 | -43.50922 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8887633e-caad-35a6-8a0b-6245e21c5595 | -10.63927 | -53.66059 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e2d7372-2fcb-3b58-8eee-57cbb4d2c839 | -13.64945 | -47.31534 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cc657e3-574e-3178-8b83-a499b4aca419 | -10.40328 | -48.16996 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b833674-7262-3799-b61f-5cb47e36af99 | -10.80799 | -45.3555 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8be92ec7-fbbd-3980-85a2-26128b2f7a23 | -7.76031 | -45.77311 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eee423f3-8f69-3792-b497-afdc442582e0 | -7.51401 | -45.44201 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7213b1ae-4b22-3036-9489-d66048790bd0 | -12.96894 | -48.41883 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 15fb8685-efec-3afd-a28a-48086197891d | -7.9195 | -48.17891 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc04e6a8-b513-3caf-a65d-6a2bbcdb0ffb | -10.81764 | -45.37504 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 839b27c2-99a3-369c-a553-46450420b0e8 | -13.41142 | -47.55045 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a2370c4a-6900-3020-947d-871e3c693f52 | -13.09371 | -47.02809 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15eb45ec-d0d6-3ba5-b45c-d13a9dc9abe6 | -11.2566 | -47.22767 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b0d1202-80db-3f91-bbfa-df8b9afa90b5 | -10.65882 | -48.57195 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82179c7d-ab7d-35ed-bd8b-309b925da16c | -7.91216 | -44.62959 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d62f879e-c30c-322a-b815-acfbf456420e | -11.14915 | -54.11853 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1bf0c008-d69e-36c5-8efb-9fd13d6b5544 | -11.25205 | -47.22845 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef521333-1743-39e9-8c2a-ecc6d64aee88 | -7.44646 | -46.9967 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 773193f7-49b2-35ba-bfea-6ab2dfbb9c04 | -8.87787 | -46.63658 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed34f7d0-bac5-3ec4-8e5b-5a4a90290abf | -10.02882 | -48.18941 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6616846-a1ee-3dcf-8501-c4f1f1df2295 | -13.80354 | -47.97226 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68365619-5cc6-3f82-b4f0-84f0a975280a | -12.85095 | -46.96877 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e334006-7500-32cb-bfb3-1c61ac35d31a | -13.41165 | -48.15684 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dc6621e0-582c-3ad4-a96c-2796cb1d34f4 | -11.75129 | -46.84436 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af57a928-d47b-3969-b315-23ddc3050b75 | -11.16819 | -54.11651 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 5e547d02-367f-346b-b440-2ce91f46301b | -7.91678 | -44.62637 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fa2cff11-8c9e-3a03-ad0d-4fc558b3f811 | -12.89887 | -46.76471 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d6855de-5312-3933-8414-da04065feb22 | -13.21767 | -50.93744 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1c7e7c1-db87-3651-836d-e03f52c65c45 | -8.54735 | -44.66793 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97750696-81cc-3d66-9869-0e9c1e7774bb | -13.81806 | -47.97374 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 761dc251-5d53-31f4-9797-8142a8049dde | -10.19814 | -44.8958 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 447bdb68-861c-3803-be41-c8e569b3f28e | -8.83069 | -46.18859 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae29459b-3257-3bf2-b7f7-5551adcc9352 | -13.61443 | -48.0344 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 210b40a6-72a5-3211-8e15-ca247aec3caa | -12.1618 | -47.77303 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 967b35a2-be87-38de-a93d-69eb50845baf | -10.03602 | -50.19738 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a3a13be-936b-37dd-ac50-85b3f6b28326 | -11.45113 | -45.03834 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34dd7ff6-3dd3-398d-9ff3-9d6b8d22cbf4 | -12.8539 | -47.00252 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 3a4437b4-9fa9-3696-945a-95c510351c80 | -11.1938 | -47.24583 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |


[Clique aqui para ver as próximas entradas](README71.md)
