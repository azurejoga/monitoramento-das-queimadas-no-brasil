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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3f22999-3a90-3dda-bcad-9ffdd8d9c4ba | -8.87136 | -47.81383 | 2025-09-27 00:13:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| dc26f3ea-f68b-3629-b84a-d187979c15d4 | -7.83604 | -47.60886 | 2025-09-27 00:13:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a13182a7-f230-37eb-8b24-282446905031 | -5.53102 | -43.87319 | 2025-09-27 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49aa2a64-a897-3c57-852d-10e7913a6369 | -3.93815 | -47.56524 | 2025-09-27 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a89b4939-da58-3a8e-8c2e-672030333393 | -5.48567 | -43.08643 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f041c43a-f6f8-3bb1-b771-1e33d959ba59 | -7.1396 | -45.51824 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0eea5eb1-d40d-3dcd-8010-9384d96d49be | -5.52097 | -43.86558 | 2025-09-27 00:13:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 74273fdc-ff84-3e5e-89ff-832883618b90 | -4.78521 | -45.34415 | 2025-09-27 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9410c737-f09b-3d12-93e6-2e1c7da4c778 | -8.08675 | -48.13748 | 2025-09-27 00:13:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0195e92a-7dc5-381f-ba19-d350fa2ebba7 | -3.86883 | -40.44771 | 2025-09-27 00:13:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 2763747d-538a-3fdd-9a6f-993687c0af26 | -4.0082 | -43.27023 | 2025-09-27 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0d2d65a6-2ac5-3710-bd0b-7285e65224ae | -8.72025 | -47.98369 | 2025-09-27 00:13:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8055fbdf-06df-3043-b992-5538bdde07a8 | -7.14868 | -45.517 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 28814d45-ad1c-3791-a534-614ee454d70c | -7.37204 | -47.02569 | 2025-09-27 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1c118e4f-7102-3fdd-afde-10cb6403e53c | -2.26293 | -47.18758 | 2025-09-27 00:13:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 67296d74-23ae-3b45-ada1-7cc968f09767 | -4.32398 | -45.27557 | 2025-09-27 00:13:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| d4b4aa43-5755-3c38-ad1a-7aeb37a8fa6a | -6.42605 | -43.08553 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 48a0f9d1-83eb-3afc-98a5-008748a00ba5 | -5.22191 | -44.49743 | 2025-09-27 00:13:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 94ddd9a4-eb26-3d04-944b-c18e3637771c | -4.15065 | -40.00143 | 2025-09-27 00:13:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 7174362c-0242-3a2e-838c-05066d544056 | -4.16776 | -44.27493 | 2025-09-27 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 989a8151-7c8b-3b00-888c-bba3d7a64acf | -2.26428 | -47.19753 | 2025-09-27 00:13:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 02779477-b6e3-339e-a308-535c0b7e6cbd | -3.6011 | -49.46329 | 2025-09-27 00:13:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6427b096-d417-3e12-8c9c-56420fe3ccbe | -6.0564 | -44.74464 | 2025-09-27 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8304d489-817e-3485-8ffa-601affb66498 | -5.75544 | -42.90697 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 6a014a70-0670-3a5f-950e-7731332064f6 | -7.6462 | -46.77183 | 2025-09-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6bcbcec2-5951-3f85-a08c-835ff94d8cbc | -6.54091 | -43.8425 | 2025-09-27 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 41140455-f69f-30c1-a289-66cb9bb8961d | -5.98193 | -43.60689 | 2025-09-27 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5ad4be49-6e6f-3fa6-b92e-08898b91ecad | -6.99868 | -46.98639 | 2025-09-27 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 06bf9a1d-30eb-3d56-a4e5-8b060a197353 | -5.95902 | -44.56003 | 2025-09-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f29bdad3-af35-322a-956c-47059d24a88e | -5.79828 | -42.81918 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 55aeef01-e40a-3c8e-955a-cbd3338b6ca5 | -5.48308 | -43.06806 | 2025-09-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e0bac632-c45f-3f89-9477-ab5a46a0b1f1 | -7.13509 | -46.09582 | 2025-09-27 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7c2efb4f-0838-34b3-aee7-1d3b77fc5aa1 | -3.24283 | -46.80413 | 2025-09-27 00:13:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7f470790-1ec8-3964-abf2-4eec6710d996 | -5.806 | -42.80859 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 56b5daa7-0964-3c92-a110-a02a6d3d8c6a | -7.81366 | -46.88966 | 2025-09-27 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8c36a7d0-162a-3f2b-b9fe-9313803f166d | -7.65273 | -43.8176 | 2025-09-27 00:13:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 357473ba-07a8-3f0a-894d-42b9de7b0f01 | -5.06997 | -44.86311 | 2025-09-27 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bfd2d15-73b5-3c1c-949f-aae05a39ebdf | -7.55642 | -46.41888 | 2025-09-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 8dff3842-dd20-3045-8cd1-b3137adad2c1 | -4.70547 | -47.48351 | 2025-09-27 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f997debd-3c6a-33bb-89f2-cbbafdf1e503 | -5.93412 | -43.52289 | 2025-09-27 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7165ab1d-5731-3f99-aa04-eda7a45a89c4 | -5.77078 | -42.81959 | 2025-09-27 00:13:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a7b1b84e-5699-35b7-8907-468dff70ec90 | -6.63542 | -40.97485 | 2025-09-27 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 08a59d07-86e2-3074-afc5-e465d86b1515 | -4.38756 | -41.92323 | 2025-09-27 00:13:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 08ec3e96-d711-3a90-a691-463e9a0cca13 | -5.18836 | -43.72354 | 2025-09-27 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e2121022-6e92-3a15-8a9f-ea5f9461c2dc | -7.1721 | -42.2286 | 2025-09-27 00:13:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 32973242-3f56-3739-9ff7-cc8926b4dc9d | -2.44934 | -49.01793 | 2025-09-27 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1c5df83d-7dee-3dd4-aad4-d759d3b31b40 | -3.82298 | -40.35798 | 2025-09-27 00:13:00 | TERRA_M-M | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| d392b848-6a10-37eb-b051-5664e30c17c1 | -7.52293 | -46.6833 | 2025-09-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 255b6e88-aee3-3193-be0c-e846ea50791c | -3.82101 | -40.34443 | 2025-09-27 00:13:00 | TERRA_M-M | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 6d76db28-dfd8-3508-84f0-9aac043f5e10 | -1.14035 | -47.25188 | 2025-09-27 00:16:00 | TERRA_M-M | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6a2f07b1-2da8-364a-8c0b-36032a6be2a2 | -2.14449 | -47.60102 | 2025-09-27 00:16:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f1997ce8-fd04-3fbd-af84-13ec3af9c76a | -0.9143 | -47.54384 | 2025-09-27 00:16:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8ae3594e-bb60-312d-86b0-9a70411a37b3 | 1.87102 | -50.84299 | 2025-09-27 00:18:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 21.8 |
| beb1a24e-b300-3ac9-af35-5efb797b5eca | -3.4313 | -44.1247 | 2025-09-27 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| ac595701-6011-358e-8d91-8cf2d25253ce | -5.5056 | -43.866 | 2025-09-27 00:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 2b47e8f8-770c-36fb-9f89-009e46e28822 | -11.3646 | -45.0108 | 2025-09-27 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 215350c7-9d33-3428-8cf2-c69d5f7c94fd | -11.365 | -44.9876 | 2025-09-27 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 05d81686-5b38-3b9e-9915-e3ea203815c5 | -5.494 | -43.0526 | 2025-09-27 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| a668250a-757b-37c2-965c-62f4960af8f2 | -12.2829 | -44.0568 | 2025-09-27 00:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| db48163b-b040-35e7-b619-8ca558473031 | -10.2412 | -50.2429 | 2025-09-27 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 93e19900-91f2-33a5-a77a-6e4fdbd251a7 | -22.6077 | -49.0351 | 2025-09-27 00:20:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2ed6963b-2e3a-3dd5-b0fa-b0fcedea9663 | -12.2641 | -44.0363 | 2025-09-27 00:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 4d11aeda-e83b-3561-8224-dd4a83e4250a | -12.2636 | -44.0599 | 2025-09-27 00:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 376.2 |
| 688486b3-0efb-3377-ab2c-5b20112e92a0 | -5.4937 | -43.0761 | 2025-09-27 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 6092b56d-f2a7-3b8b-b8c1-1485e4b7ca49 | -3.45 | -44.1238 | 2025-09-27 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| d1fa0713-c30b-35d1-b715-b94a143beaf0 | -5.7961 | -42.8182 | 2025-09-27 00:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 3dd93c13-ed50-3f16-970f-fdfda231886d | -5.4752 | -43.054 | 2025-09-27 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 30d25862-e75c-3008-8ea1-c2ce8a954261 | -14.8644 | -45.621 | 2025-09-27 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 337af93e-416d-3050-af54-30d4f0a3ac47 | -10.2409 | -50.2643 | 2025-09-27 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 36d0fd50-4020-3fb4-82a0-350b88be72a3 | -5.4562 | -43.0788 | 2025-09-27 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 92bff8aa-1ab5-3e0e-a827-b88051307858 | -5.4935 | -43.0995 | 2025-09-27 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 069b6d4d-34b9-3cba-9477-9fd198fbaa4c | -14.8454 | -45.6013 | 2025-09-27 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 681be15b-7c9b-3970-ac0f-57ef5f1af9b1 | -22.7271 | -51.3948 | 2025-09-27 00:20:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 69.0 |
| 523f113c-6fc0-31cd-a0d1-bdd89d50848a | -5.5243 | -43.8647 | 2025-09-27 00:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 66f02d3a-3cc3-3d1f-aeac-ea96a9b783c6 | -14.8649 | -45.5977 | 2025-09-27 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 0fd508fc-16cd-3fea-bf3b-3e58d0a90a91 | -10.222 | -50.2662 | 2025-09-27 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 86ecbf0f-c312-3478-953e-24cf6ffa2a21 | -14.8448 | -45.6246 | 2025-09-27 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 534b2903-8cd3-32cb-9910-6cde82afd627 | -15.0462 | -47.1274 | 2025-09-27 00:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 0914072f-edf4-3b37-a555-2064c36b9f0b | -15.0262 | -47.1536 | 2025-09-27 00:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 49115427-ecfc-3402-97c4-abca51ef5fb6 | -5.0862 | -44.857 | 2025-09-27 00:20:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 55050b4e-eb66-3f68-8b74-6884b26f9af9 | -5.4748 | -43.1009 | 2025-09-27 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| bf351f6a-220f-361d-bf1c-a35f891cb70f | -11.3455 | -45.0135 | 2025-09-27 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 5f91c87b-40b0-34c7-aaeb-19fff5f5ef49 | -4.0107 | -46.9712 | 2025-09-27 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 14aba9d5-87cb-32da-a052-c960e116db36 | -5.475 | -43.0774 | 2025-09-27 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 384.2 |
| f232cae0-a341-3079-aa2f-7d1295ee11ee | -15.0267 | -47.1307 | 2025-09-27 00:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| a213edcb-f000-3481-8d8a-48af281dc009 | -5.4565 | -43.0554 | 2025-09-27 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 3c51dfde-d75d-3198-93af-3ea6dd77e810 | -12.2632 | -44.0834 | 2025-09-27 00:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| d3169565-376d-3eb8-90a7-3d1a933fe2b3 | -5.0676 | -44.8581 | 2025-09-27 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 39cdf432-e044-3943-88f3-faf388c4b493 | -5.0862 | -44.857 | 2025-09-27 00:30:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 11deb702-84af-3a12-b1ab-7b63f53c648f | -22.5589 | -48.5802 | 2025-09-27 00:30:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| 8e3718e9-8072-3271-a03d-f374880f15ba | -15.0462 | -47.1274 | 2025-09-27 00:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 90a65e7a-bed1-3ce9-a890-623f8a17e444 | -22.5799 | -48.575 | 2025-09-27 00:30:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 467.8 |
| efe93f25-cce2-342a-bbee-5d275bda8601 | -3.45 | -44.1238 | 2025-09-27 00:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 63e2dcea-dff2-34de-b014-7a61b00b57f2 | -5.0676 | -44.8581 | 2025-09-27 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b40fffe4-aa1b-3a99-98fc-fad519716e15 | -22.5582 | -48.6038 | 2025-09-27 00:30:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.8 |
| 12b73b16-9ce1-36d8-9b4a-75782c5e176e | -12.2636 | -44.0599 | 2025-09-27 00:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 893b7ceb-3547-39ff-95c6-68013552bae5 | -12.2829 | -44.0568 | 2025-09-27 00:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 8066c412-5016-37e2-ad04-ff8bb360ce57 | -22.7271 | -51.3948 | 2025-09-27 00:30:00 | GOES-19 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| 554063f2-5a79-3e72-8c4a-872e977329ce | -5.5243 | -43.8647 | 2025-09-27 00:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c0079c98-4ca3-3295-9ecf-93d6a94ef340 | -10.2409 | -50.2643 | 2025-09-27 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |


[Clique aqui para ver as próximas entradas](README7.md)
