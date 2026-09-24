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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cacb23e-71cb-33ad-8ea3-bb59b4aa8415 | -3.46668 | -58.31308 | 2026-09-24 00:39:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3a15d0fc-1660-3201-9784-2d2063a2a1ce | -10.23061 | -57.82937 | 2026-09-24 00:39:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 47078ebd-3110-3bd0-8123-baea2a6f13c2 | -5.65615 | -60.20809 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a7a3eb98-9c7a-3788-a9a4-2d8929b709f6 | -3.68623 | -60.56218 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 6945de33-f65d-3327-8532-64766a335bd0 | -12.07737 | -50.76049 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7f503f02-960e-39cd-be1e-54b63648daaa | -2.89549 | -54.09018 | 2026-09-24 00:39:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0738d4f1-c4cd-3b72-a0cc-a986a90b1c8a | -4.15779 | -60.77413 | 2026-09-24 00:39:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7f8bec66-7e86-348b-8e6c-a52f31b96f26 | -5.28684 | -60.20261 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7e0b911a-d415-3015-b0e5-8e9cb2053e9a | -3.7148 | -54.21207 | 2026-09-24 00:39:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 8f38b632-990e-37ca-9759-9d9a5a132fcc | -4.38542 | -60.96 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3407a3aa-8fb9-354a-be6a-e61acdecdee1 | -11.95348 | -50.73997 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 94591d41-cb94-36f6-a9fd-4a835ed4eedc | -6.13299 | -59.93014 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4ffed71f-c3c2-3eb5-9b05-5a4142b2c461 | -3.69998 | -54.19603 | 2026-09-24 00:39:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 60008c54-4826-3b94-911c-b1bf3ddfca7c | -3.7026 | -54.21369 | 2026-09-24 00:39:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7095ec0a-8346-390a-9aa9-ee5f127993d1 | -11.74883 | -58.55016 | 2026-09-24 00:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2a14ac86-0e7f-37f9-a8b7-592df157afb7 | -3.43616 | -50.07977 | 2026-09-24 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| b6d38707-f56e-3c3d-a54b-9a96f41c84ac | -9.8796 | -63.46329 | 2026-09-24 00:39:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 08d84c59-82c2-34dc-acd4-9bf024095c55 | -11.44302 | -55.10329 | 2026-09-24 00:39:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 005f9c95-aedd-37f2-9d29-0412cf735fdf | -8.2379 | -54.69062 | 2026-09-24 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 7331b7f7-f0c8-3fb4-9256-1a8713dd286f | -9.32905 | -56.81134 | 2026-09-24 00:39:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 203d520d-24db-39a0-8c65-bcfdd23884ce | -4.67093 | -55.78518 | 2026-09-24 00:39:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b1b7c999-6ffb-3554-b85c-4b2c11271db8 | -8.28981 | -54.78815 | 2026-09-24 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| bd855071-8559-3010-be2b-aa3dd999de73 | -10.65016 | -51.33253 | 2026-09-24 00:39:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 6637ba3b-f470-3911-87af-c6ddf2153a90 | -4.11902 | -51.09883 | 2026-09-24 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| ad298c53-732e-31c5-adea-81e095e30ad7 | -4.02118 | -52.08641 | 2026-09-24 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| c476d0ef-7984-3993-a541-d1fe0702ead2 | -6.64097 | -59.93072 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 33c7a8dd-240f-3e1d-bbf8-63505802462c | -3.42256 | -54.01347 | 2026-09-24 00:39:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 0d053f9c-85f0-39e8-91a8-5313b5af067f | -9.02346 | -60.5292 | 2026-09-24 00:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f9a26164-0077-3d8b-a7a7-11fbf89dbeaf | -5.76994 | -56.5187 | 2026-09-24 00:39:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d8c5621f-e9ec-3b52-a059-5c70f1724d41 | -5.86953 | -60.15701 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 55e98ea5-9fba-38e5-b28a-4f929894bb40 | -3.68222 | -60.59879 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 827a0c8e-bc32-321f-8847-056895ad5838 | -5.41146 | -60.24208 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 27684463-6028-31df-832d-60ee3ae9cea0 | -4.159 | -60.7831 | 2026-09-24 00:39:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 06ed646c-5991-3e05-b75d-b4fe499e44fc | -6.60193 | -59.92447 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 3afb7c3d-16fc-38e9-9620-9805cf67d9b6 | -4.4705 | -54.97066 | 2026-09-24 00:39:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 12b96bc0-c447-3f19-afd6-e45fdfbc1abb | -2.88302 | -54.09201 | 2026-09-24 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a4860635-a0c1-324c-b812-b14fcea5ef9a | -6.45172 | -59.96034 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 87e1ae67-5c97-3dd5-b51a-1da43adb5400 | -5.2442 | -60.16934 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eca46c56-3104-388b-acc0-af9468f3944a | -8.08727 | -54.76816 | 2026-09-24 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 83f9db65-c30d-343e-9155-386f92eff875 | -7.6401 | -57.63558 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ace7fd9f-6740-3819-acb3-2dee25d216cc | -6.64644 | -59.42891 | 2026-09-24 00:39:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e8a7f2c5-7455-311a-935f-c34bb13b62bb | -8.88707 | -62.53933 | 2026-09-24 00:39:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 65e45d6d-b562-3e82-b5f5-08fd845ba4ff | -3.70871 | -58.85445 | 2026-09-24 00:39:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9509b8b7-bd14-3ba9-8eab-ba4b997c9f7d | -10.84782 | -57.17312 | 2026-09-24 00:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| dc433f02-fc38-3776-b5ef-e722cef4ab84 | -3.5816 | -59.06911 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e53b9b17-1f70-3d2a-9200-069b7dbf8fd4 | -6.44168 | -59.95272 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 98252c4b-34ca-3b21-a156-73395380c38a | -9.51742 | -59.75116 | 2026-09-24 00:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5b6f1650-5dac-3aef-8953-d8617b1e7449 | -6.60955 | -59.91436 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2101f3b3-bee8-37dc-94e2-d6d642618f7c | -4.11441 | -51.06809 | 2026-09-24 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 9fc302d3-63ac-3dec-a790-ea2c9b93bc00 | -4.51723 | -56.0668 | 2026-09-24 00:39:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b671469a-ac45-338c-bb90-b214af46ccea | -12.07331 | -50.73664 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 54ef7e92-e715-32c5-8bb3-425fbfba3ef6 | -9.84927 | -48.52456 | 2026-09-24 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 0ca4dea5-d92c-32fd-a239-32e7bad09a9d | -5.11003 | -60.25745 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| e1a100a9-6da0-3598-b108-ef13e9d02905 | -7.44839 | -63.63831 | 2026-09-24 00:39:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7802a284-f143-3c77-9b16-495e3f84a63d | -6.57175 | -51.48243 | 2026-09-24 00:39:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| ad5bf6b2-a56b-3264-aa48-00d909638d9a | -10.13651 | -58.75536 | 2026-09-24 00:39:00 | TERRA_M-M | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e93ca2e8-9d25-3c92-90fc-d3aacb717ebd | -5.65736 | -60.21698 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| f85c58c9-1709-30c9-9c46-b7e841346b00 | -7.45746 | -63.62302 | 2026-09-24 00:39:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| df3f8f99-9287-3351-9ff0-4151208f7da6 | -8.31548 | -64.05003 | 2026-09-24 00:39:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 32.9 |
| b57eba75-6e0f-318b-84d9-7c209c92c4eb | -3.16703 | -54.61521 | 2026-09-24 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| ca8bee05-8ba2-3ec7-8d86-775b3fd1c8f7 | -9.02473 | -60.53876 | 2026-09-24 00:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 027ae2d2-b692-379d-8e5d-989b531a9b1c | -4.10685 | -56.19468 | 2026-09-24 00:39:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 55121a28-dad7-3a67-9a5c-566a27416a3a | -11.94782 | -50.7466 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 86a2fc9f-ad96-31cc-92ac-98de0f988192 | -5.59951 | -60.20368 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| e12b4988-7758-35a0-94df-03c11e97d4cf | -4.01742 | -52.06059 | 2026-09-24 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 37b2b249-95b5-3d52-b5f0-af00f748f079 | -4.15063 | -60.7998 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fadcbb8f-4dcc-3c47-9004-5266f0e88909 | -4.38665 | -60.96908 | 2026-09-24 00:39:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9091366a-0d4a-3bb0-9813-9a8334aa0334 | -10.30377 | -58.0944 | 2026-09-24 00:39:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 86667e6f-0684-37ed-811a-aaa7439c1015 | -3.60211 | -59.41188 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fca5a488-515f-3a95-8102-5150e5976d47 | -8.12004 | -54.8124 | 2026-09-24 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3e01d611-bfa1-3442-a490-3661a008d9c5 | -6.42516 | -59.97943 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 48de1fe8-c9a6-303b-95e0-cf607a65cd51 | -5.8619 | -60.16713 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 499d20e2-0e05-3cd1-b9b8-ea6f990a750e | -6.61199 | -59.93211 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 0f920a56-0504-360d-b9d9-1486d865c876 | -3.96298 | -59.35476 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 30655585-b9c2-3488-9e24-c2392888a92e | -11.96555 | -50.7681 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 127.9 |
| ed3661e8-34a9-335d-971b-26aee2d44085 | -3.49554 | -59.17899 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fe95b107-99d6-35c2-af7d-976ddc4d1b38 | -12.15059 | -61.17549 | 2026-09-24 00:39:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4d8e7021-5a50-3bad-9886-a737645b8d9d | -6.43156 | -59.96043 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 84246bb0-5a4e-3ad2-9dd6-1d94ba9bdd8c | -5.45481 | -60.14886 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 892a13d1-fd3c-32ad-b869-608aa44919f7 | -3.16464 | -54.5985 | 2026-09-24 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 419ea6a8-6c0f-31d9-9a9e-6f8506ee1ae5 | -3.83436 | -59.36696 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 4fdc9dd7-2255-3af0-a6e8-327e7356372f | -7.92202 | -63.46978 | 2026-09-24 00:39:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e96d92d1-4180-34b1-92ca-7afc01d62885 | -6.73848 | -59.42755 | 2026-09-24 00:39:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| abc15210-52e9-3f8d-9df0-4f3b457e5d11 | -8.20961 | -54.72306 | 2026-09-24 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 61ebe45f-daa2-3d52-8682-18c22fee7c44 | -12.16372 | -50.76953 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 8059619a-2e1d-3307-ac28-d9da679b3708 | -3.75265 | -59.31246 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 2dd634c3-c8f0-3548-b32c-feb30b453322 | -8.58854 | -62.52338 | 2026-09-24 00:39:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 7d9d870f-868d-382c-8569-22b41ec042aa | -9.33049 | -56.82127 | 2026-09-24 00:39:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a8571c44-028d-35c0-ac92-c0ac9a9b5351 | -6.62052 | -59.99433 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ce62a62e-6f30-3ecb-96ad-2866aecfe982 | -3.83803 | -59.39353 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2148dd6c-66fb-3b03-89d3-5a8deec8e386 | -3.45657 | -50.0714 | 2026-09-24 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 2ef05f2f-8865-39ec-a95f-037690693ef7 | -7.04869 | -62.92947 | 2026-09-24 00:39:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 64926393-1b17-3405-b949-6f020644c7bf | -6.18538 | -57.77987 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d49cba97-ee42-3294-9be1-02f8c033ce89 | -8.87683 | -62.54068 | 2026-09-24 00:39:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4e2d6b11-25c1-3738-9261-f7b72860afc5 | -6.45051 | -59.95148 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 5f9c2658-b8ce-3be2-90d1-c7d6e77b9621 | -8.31744 | -64.06549 | 2026-09-24 00:39:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8bd9b78a-a902-3c30-adb2-a028d97ce5c4 | -8.44223 | -57.63601 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 151b57e2-b585-3d83-b7c6-4ee4ed5020d8 | -12.11861 | -50.75315 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 5d63cb9f-e895-35d9-b7f2-55d89bda75b1 | -11.59788 | -58.51394 | 2026-09-24 00:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2b974cdc-55f3-3423-aa5b-84a98d7462e5 | -8.35202 | -62.82266 | 2026-09-24 00:39:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |


[Clique aqui para ver as próximas entradas](README19.md)
