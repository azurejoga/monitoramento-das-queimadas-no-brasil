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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fb75bb0-bb61-3d57-9a7d-82cd8a8e82c5 | -18.0487 | -44.6066 | 2026-08-20 05:10:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e5ce1844-59a6-3895-b746-e8ed95ddece4 | -11.8188 | -58.8459 | 2026-08-20 05:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 7871adc9-4752-3aa4-8f77-a1b070988974 | -11.2189 | -55.0585 | 2026-08-20 05:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| eda15a90-89b9-32f5-8dd8-0ee57ec89553 | -18.0487 | -44.6066 | 2026-08-20 05:20:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 459ecc89-4171-31c2-896e-875ed18295ca | -17.3372 | -43.6139 | 2026-08-20 05:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 708d7999-3650-38e2-89cb-7f32cef53922 | -11.8377 | -58.8445 | 2026-08-20 05:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 9f4ba68d-8a4f-34e1-b64d-fdd057c19303 | -8.6727 | -54.6492 | 2026-08-20 05:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| bc11f334-2df8-3ed7-9f7c-c83adee226c8 | -17.3365 | -43.6383 | 2026-08-20 05:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 48.8 |
| c53e33c8-00c8-39fb-9e62-66daf1484cfe | -17.3365 | -43.6383 | 2026-08-20 05:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 0744d081-9fee-3b14-bb6c-d34826b20c20 | -17.3372 | -43.6139 | 2026-08-20 05:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 0acc5962-6b3e-3b5b-bdab-d14543114649 | -9.4257 | -60.416 | 2026-08-20 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| cd7333a9-e1e5-3a9f-aa9a-6026829de151 | -11.8377 | -58.8445 | 2026-08-20 05:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a3e7dc0b-7020-3c63-b816-238db2c1cc03 | -11.8379 | -58.8248 | 2026-08-20 05:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ad681fd0-fd5d-3c9c-9b67-3ad5d1f0f3b7 | -8.6727 | -54.6492 | 2026-08-20 05:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 860ce053-2884-36f6-b0c4-d889445d19bb | -18.0487 | -44.6066 | 2026-08-20 05:30:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 5b5a5e17-2ba2-333d-b11f-ad569f679904 | -9.4256 | -60.4353 | 2026-08-20 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 16f7be00-d023-3299-9b61-adffb95eaf8a | 4.31841 | -61.31089 | 2026-08-20 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 043a9e39-ea26-361d-a884-1db0f0e722b6 | 4.32235 | -61.31395 | 2026-08-20 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 358ce963-badf-30f6-aa68-0173aabc4544 | 4.32178 | -61.31026 | 2026-08-20 05:38:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a76ac930-9a1d-3386-ab1e-303f3b282293 | -17.3372 | -43.6139 | 2026-08-20 05:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 102.1 |
| acbdf314-ce86-3c2a-9933-8c88a3675d1f | -18.0487 | -44.6066 | 2026-08-20 05:40:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 43f35ed1-a7e9-3018-b8ec-41cb28a6100e | -17.3365 | -43.6383 | 2026-08-20 05:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8f6f80c9-f982-35c5-838b-03397520774c | -5.49233 | -60.13477 | 2026-08-20 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3175df6-2730-3291-a7d0-b5ff25de8212 | -4.44019 | -55.38159 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05fb8772-dc55-3146-bac8-cafb8a0b643e | -6.35791 | -54.90152 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6787c7e1-7cf7-3e8e-8559-57f79d79cef1 | -3.09912 | -61.19142 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45f8d2a1-eaba-3c39-b17a-8c3a8ef5bb19 | -5.36294 | -60.1565 | 2026-08-20 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c61bb62f-e3b9-32b3-8b9e-a679c3d9b2db | -6.63931 | -56.41523 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c9382c7-daba-3c18-8f9a-8435f26d7333 | -6.38775 | -54.9378 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 099496cd-d3ba-3b2c-b60f-bab89e2f37bc | -6.08786 | -57.91972 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ba6ac9c-850d-3acb-9545-1e8e16cdca3a | -4.38569 | -55.47472 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3188261c-cd43-33f3-a315-a7b0a950e463 | -3.1304 | -60.69511 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 102b7ed8-965c-36cd-a4f4-3475f13983c2 | -6.09243 | -57.91551 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00b5e799-36e1-371f-9670-282058414483 | -3.09753 | -61.223 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76bf2fcd-a255-35f7-bec0-a4787985c594 | -6.34845 | -54.90003 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b19a7eb8-47a4-3d87-8852-55496a667f3b | -6.6928 | -52.08135 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37b40d09-6ec3-3e8b-8ca4-e22aa8d93e6c | -6.42458 | -56.19028 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27c00f50-6196-3650-b2c0-a8af05d5a7bf | -6.43234 | -52.72507 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef753307-767e-3cba-a662-5f691b5451fe | -6.68549 | -56.15644 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15149db5-3fe4-3e1a-b0f4-02f39d4baf0d | -2.05052 | -48.04063 | 2026-08-20 05:40:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d606aad-9e48-3be4-abc0-bd75e0096284 | -3.10358 | -61.20627 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24f1490e-0bda-3113-a683-263b363973e6 | -4.50488 | -55.45403 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd5e5978-b76b-3a13-a909-dcdf8d1d51e6 | -3.0953 | -61.21558 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74828e9d-9b18-3353-a7d9-af3bd5bc7af8 | -6.35865 | -54.8964 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1d8c101-6a1e-3926-878e-4e1fe17fd104 | -6.24741 | -55.40523 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 894e9243-8134-3897-a1fa-fb24419c7f48 | -6.44383 | -52.76328 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5b489c1-92cd-3aa0-926a-58ec56277412 | -3.25873 | -61.16679 | 2026-08-20 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6566caea-daac-3592-9d31-01311c1fdcd8 | -3.10249 | -61.21317 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb7e6b0d-b66d-3685-8956-a1e4b36d88bc | -3.1008 | -61.2023 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ac5b4e9-23c6-3339-baeb-5a0feb042124 | -3.10139 | -61.22007 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d185ca3a-944e-3053-9140-9dbaf5e0b8e5 | -4.38665 | -55.47256 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acf80284-f1b1-3461-996f-ed08b1e6584a | -6.44387 | -52.72299 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f1937c1-fdd7-351b-85d5-484bf679ffcb | -7.76262 | -49.20406 | 2026-08-20 05:40:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74e31229-0e53-36ca-b2ed-50bbbcc76479 | -3.10635 | -61.21024 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59b82731-a3e9-343f-a68d-46baada9d8b4 | -5.80349 | -55.72759 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ca741d1-4ace-35e6-b8b2-3b9779db7482 | -6.61495 | -56.3549 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6774797f-882d-3681-afc1-59a6c3044cf2 | -6.31307 | -55.91754 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db0a4bdd-34c1-341e-8131-e74fde829033 | -6.14504 | -57.85455 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60094241-cbbc-3639-b1fe-ab050a02fead | -4.37645 | -62.56675 | 2026-08-20 05:40:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 758e51a4-099f-33f8-8158-f0383f90f257 | -3.55437 | -62.07768 | 2026-08-20 05:40:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb6483b2-648e-35bc-a600-24b043f239ab | -4.50997 | -55.45021 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 299459a6-8f31-328a-a4e9-7473d4e19d1f | -6.43885 | -52.71866 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c41abcc-401d-354c-9adf-c086cc155cd1 | -3.01319 | -51.05767 | 2026-08-20 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bab5ab07-05e0-30dc-9c47-132b385e235c | -6.31748 | -55.91819 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17f5afca-b154-35e1-9c1a-2e3a79e8d5e6 | -5.8054 | -55.71463 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22e9f7e9-2df5-36ab-9140-eef4563a3249 | -6.34371 | -54.8993 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c81bc18-d9da-30be-9a5f-90dd35c95245 | -5.49635 | -60.13158 | 2026-08-20 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66ffca8e-603e-3e1e-88f3-4125f53276a9 | -5.80095 | -55.714 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 954ffbdd-8f9a-39f0-9e18-72b3595275fb | -6.38595 | -54.94129 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2a981aff-3f99-340d-a270-3a52ba10a145 | -5.49576 | -60.13531 | 2026-08-20 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb312d78-f00c-36eb-bcd2-9c5bd9515b3b | -6.42159 | -54.93757 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc230a5e-f204-326d-82dd-ae48cf32c342 | -2.63656 | -47.98697 | 2026-08-20 05:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2c758cc-4e8b-3be3-b28c-50f69a912dbc | -3.9007 | -55.88086 | 2026-08-20 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ef158af-ad3a-3693-a586-10e67553b440 | -5.79777 | -55.70473 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eca5f36-6703-3c7e-80af-a4e1942859ba | -5.79841 | -55.73129 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d883dc41-0980-3c15-8e39-5e806ce6a25e | -6.08857 | -57.91492 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 998788a5-f324-3b46-a19f-a00eeaab52f1 | -6.38047 | -54.94567 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 732d4461-c636-37bd-b904-b0abe71f72fd | -6.00095 | -57.86058 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4047b7ff-ff1e-3a8f-b18f-54cdc1849a1b | -2.81144 | -48.59065 | 2026-08-20 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98575c52-5a8f-3af1-b5bc-18408e93e925 | -6.39109 | -54.9485 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d28bded-3cc2-39f4-b4f5-7845a4f69bd1 | -5.36352 | -60.15279 | 2026-08-20 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c6f70d0d-3ba4-343c-a5d6-ac87c15c68a6 | -2.82528 | -48.65123 | 2026-08-20 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d0c10e4-187f-3deb-a4a5-e9594ef5c3f6 | -6.44434 | -52.75969 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42f555a3-0406-39fa-88af-d9d775760872 | -5.80475 | -55.71899 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6397b66-5d44-3390-a7e7-cbda77558e1f | -6.00726 | -57.87122 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1e84033-f96e-3b49-b810-9381c7ad3e50 | -3.1349 | -61.39493 | 2026-08-20 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b0d2581-a4a2-39bf-9d9f-4e2abfef4d1a | -6.08471 | -57.91436 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 496a7d6a-478f-3fa4-aaf8-b7349a450d25 | -5.79206 | -55.71274 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d88dfc77-b69d-36f8-a471-5f88c6b517ba | -6.38521 | -54.9463 | 2026-08-20 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4107c24-4b49-38a6-84cd-9ca802273816 | 0.80779 | -59.8689 | 2026-08-20 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a61dfaa0-e55c-3da2-ba96-578f2e1fde43 | -4.3863 | -55.4705 | 2026-08-20 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dd2f51b-2bee-3f92-9635-cf6a93ab848f | -6.44184 | -52.73745 | 2026-08-20 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff76617c-cd34-37d5-bcd7-6efd0a11e8ad | -3.10471 | -61.22059 | 2026-08-20 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61592368-0a57-3dcd-8ca6-24d1f1da0886 | -6.2454 | -55.41924 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fd44453-fd43-376c-8c88-14917a7b9908 | -5.80222 | -55.70535 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14de4840-0751-3205-b267-791727fcd16e | -5.80793 | -55.72821 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f0786ab-13f5-3fde-8af4-156e24db4529 | -6.08542 | -57.90958 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e632829b-3e9d-316f-8fa8-9062b65ab3b5 | 0.80724 | -59.86542 | 2026-08-20 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b6c4d7b-9353-30e7-9c60-450f60bfbfed | -6.10345 | -57.8679 | 2026-08-20 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cedd19ad-ff74-36e5-961d-ebb5ef58fe59 | -6.64418 | -56.41184 | 2026-08-20 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README58.md)
