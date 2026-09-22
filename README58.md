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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a34258f-1934-3a8d-af65-c15a52c7674e | -10.46093 | -51.3215 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 012c9d1f-9d35-31c6-9575-8270825a3ef8 | -6.71181 | -59.45223 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38db25bb-0b92-38c5-bef1-ce05cbd9df61 | -3.24353 | -53.95508 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ae753862-83a1-3b06-9b1a-63748c526df9 | -6.10943 | -55.68738 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7122f508-e273-38de-a1dc-f55565687bf4 | -6.97733 | -55.70483 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 765094e9-c9b9-3b01-aeff-dbf34d1038dd | -3.06355 | -54.41588 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 746f7230-6662-341a-a5c7-7c1285409c87 | -9.7574 | -54.29971 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 56ae2685-0f78-3f9c-9a0a-75b2f069c095 | -10.02289 | -45.20861 | 2026-09-22 04:46:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6282a54d-c256-3724-8bf8-eff562fc6fca | -3.06804 | -54.41197 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ee0a0739-8a0a-33cd-bcbf-d3b1a48ad7e1 | -6.85919 | -59.90637 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1568d8d0-fc1e-3703-b063-c14572d8ef0b | -6.71982 | -43.98293 | 2026-09-22 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb73e3cb-7de0-38b4-bfa9-43291bcc80cb | -6.64635 | -59.91647 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1a545a9c-b36a-3f83-989e-b82a298f954f | -4.38464 | -55.03204 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38baf244-9930-36dc-b8ce-1c53351f6f79 | -3.06467 | -54.40418 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9578fd2-fd90-3645-8421-3af8dd7f08b6 | -6.79317 | -59.95156 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a32f5eb4-5aa9-368c-ad47-6397c447ed9e | -9.29204 | -46.17348 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3065d5bd-a573-3f8a-a25e-ebb1dcd2ccf5 | -7.59497 | -57.66426 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b80f0946-7c97-3e74-aefd-dd290efad789 | -9.76856 | -48.33472 | 2026-09-22 04:46:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8f52345-3c6c-36e8-b479-ef88f2f8dfba | -6.31204 | -57.73962 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a763b83f-a046-300b-9a3f-e15ab3bb4391 | -6.64367 | -59.93183 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bb258dd-2570-3b84-bd12-7ca7c30511aa | -3.00856 | -59.36914 | 2026-09-22 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb607d9d-46c5-3a76-9365-0bbfc099e9a6 | -6.67113 | -50.94046 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ddc8ece-1698-35f8-b041-ba8270e3591a | -4.50407 | -59.55892 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6705e0f-9529-33f1-b671-a1a452fb17c9 | -10.25367 | -45.50046 | 2026-09-22 04:46:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78f7a0d0-927a-31ed-9473-151e1162cdef | -4.27729 | -56.25979 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80ac5146-fb29-330b-aab1-ec1d1331d443 | -7.13073 | -48.43153 | 2026-09-22 04:46:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d35b6b7d-dcd4-3360-81c0-eb1366e588f7 | -3.24069 | -53.94889 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3565b7f-763e-37e2-8631-073614a79a95 | -7.88426 | -54.72377 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5bb3989-5776-38bf-ac07-1c36009dde9c | -9.38403 | -47.7662 | 2026-09-22 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9f1f086-9f07-3dac-8e36-4e0cb4efaa73 | -8.32314 | -50.83238 | 2026-09-22 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e1d00a3-ef55-3993-a233-2f849764c2d1 | -3.93313 | -56.04716 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8c7ce39-f0f3-371a-893b-710508494928 | -11.38663 | -46.78998 | 2026-09-22 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3638c36-03ae-33c0-a4fa-71f7fe94c54e | -3.4425 | -50.61595 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79bad9c9-f3c8-3d91-889f-17bc21d5a078 | -10.93924 | -47.86282 | 2026-09-22 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e60c3ee4-cadf-3d6f-a34e-7dffff5f0ff7 | -7.18952 | -47.47845 | 2026-09-22 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ec1df5d5-697d-3d90-be69-bcfd4d764ade | -7.32574 | -55.59836 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5673bc9b-b939-35b1-b019-84b44702a30d | -7.35393 | -45.34499 | 2026-09-22 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7fe03377-5e3c-3ab1-ac16-21bf39e9b92a | -10.90952 | -47.38414 | 2026-09-22 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0d05447f-5da4-3c85-9053-42345be1a4fd | -5.88737 | -52.09805 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b21c6db8-d7f6-39dc-81d7-75ae3db065a8 | -8.60599 | -54.63321 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5effb47-baab-34e0-9b27-7f0395c0b361 | -7.3439 | -55.60668 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| baad2ef8-05f1-326a-b7ee-9ff21d1589d6 | -8.62376 | -54.63615 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1cb0911-9e8c-3d7d-a3ff-5b7e03674986 | -8.48994 | -57.61369 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a718dc01-abea-3bb8-a013-2d0fd69cab3b | -5.1292 | -60.28134 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 239cb6da-9fb2-39ef-96b9-951a9eec2821 | -11.34179 | -43.37845 | 2026-09-22 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e399c317-8a4f-3ade-a267-ea1c362cfd63 | -3.75498 | -59.42469 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e350081e-5bb9-32e7-a0a5-4b32e783e87c | -6.92772 | -42.88919 | 2026-09-22 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3cf7a9f0-81d7-3810-a5fd-29555b4532a4 | -11.14562 | -42.79106 | 2026-09-22 04:46:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a249a5a3-967f-373a-8ac7-100b63d93964 | -5.87739 | -52.07476 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6553bcc3-00e4-3d6a-80d7-30ce1c3771c4 | -6.74879 | -59.06867 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfe6ba6d-cadd-3049-ad67-700a0f2ea538 | -4.05571 | -56.33014 | 2026-09-22 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f765baa0-d9af-3adf-bed3-3a2c6f93c0c5 | -7.43111 | -49.84484 | 2026-09-22 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3f53116-dd2a-391b-85fb-e1669998fe89 | -3.39352 | -59.51928 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22883cad-23ed-3f45-9f58-9faf4939c322 | -3.06052 | -54.41076 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0208233c-b0a8-3f7c-bb7a-c1377510e380 | -7.1989 | -46.55187 | 2026-09-22 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d606469-8d26-370f-9346-293c51514aca | -6.42531 | -59.97548 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e73312b4-9e35-361c-a993-87c585a91242 | -4.28146 | -56.2604 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52ad0a62-20b5-38ff-9627-4f598a025ebc | -9.6099 | -43.92706 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1e9f00ec-01af-373b-93e7-825fb80db83f | -6.81363 | -59.43148 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34272380-45f1-3a87-9533-62bf7fbf3c0b | -4.96681 | -55.82863 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62173c1f-0092-3a04-b781-57e15c8c2057 | -5.88696 | -51.58033 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b41dde5d-0eee-34ce-ab0b-61224650da56 | -3.36352 | -50.44568 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77c6c9e0-9ff1-3771-a958-edd84ab0860e | -3.23703 | -53.94833 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96aa40e0-9b10-3cc0-abad-c49e88127a55 | -11.0941 | -48.32973 | 2026-09-22 04:46:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c256478-9686-3cd1-8d76-eb9d61e08b82 | -5.1298 | -60.27791 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04d61185-9339-36c7-8455-4747d3d2d111 | -10.84853 | -50.15003 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7b1fd31-f7e6-3116-9deb-3b969cb53076 | -9.3809 | -47.76102 | 2026-09-22 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c53c4a38-9b4e-3136-9d10-42651a1062c3 | -8.92082 | -50.92547 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 43feff45-c32f-3bce-a44f-c3edf0f3c407 | -9.85038 | -48.30965 | 2026-09-22 04:46:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4684c59-3323-33c0-bd45-b9ddc4ecd5df | -3.07097 | -54.39397 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34f25e0d-8c24-3acc-84ca-b8af20a61876 | -5.82628 | -52.11723 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fcd3403-e0e5-3d1d-a2b4-2dda98130574 | -4.5992 | -52.62661 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2392695a-a547-3287-9f26-1ede5980b76d | -6.02467 | -52.15576 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a38f4c0c-4da5-3b8d-add8-aeafa8c8bcc1 | -8.36787 | -45.62104 | 2026-09-22 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9045f03c-5a25-3b8f-a209-e569448b2e92 | -7.38777 | -51.77229 | 2026-09-22 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7abaf47b-92e5-3b6c-a223-c7e39ce97e02 | -7.58135 | -57.69201 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b7a5ca6-8b7d-3dc0-a8a2-16db446c116d | -6.29293 | -47.65514 | 2026-09-22 04:46:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ac277e6-1cca-3ba9-b389-e37bc452e03b | -3.45017 | -50.6101 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 92e85b3e-bb10-3b6f-9889-b1c528af33dd | -6.57247 | -44.89872 | 2026-09-22 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fc37dde-6593-3851-a7a6-1c9c2a7281fa | -3.41682 | -60.20315 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5da11b95-9e5a-3724-a78d-cfbe16a6de00 | -4.26869 | -55.44427 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b17cc431-4c2d-3d7d-a472-56c861c26dd6 | -6.58304 | -44.1485 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f722578e-3ad4-3eea-b86c-0ae29cdb23fc | -5.60461 | -48.22752 | 2026-09-22 04:46:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de57ecc2-7e13-39f5-845f-22a626cd2cf6 | -10.8514 | -50.15435 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dbce2fb-54f7-3dd7-9474-f99da7fd903b | -3.29647 | -57.86179 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a3b677b-07fd-3492-8a92-3043e89182b4 | -4.55391 | -54.90178 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02e62cf1-6ccc-36ed-830f-3c32492df8c0 | -8.78996 | -44.29926 | 2026-09-22 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0b5fc9cf-dcd3-3de8-b362-92ffa2175907 | -3.4524 | -50.61748 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eb0dd02-9452-32ef-b7a7-df779eb67766 | -10.38244 | -48.917 | 2026-09-22 04:46:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3af90e5-e01c-3f42-8a45-e36f2a5982d6 | -10.4808 | -51.30291 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32c55f3b-3393-38be-8bfe-bd9c2dd33087 | -9.97774 | -50.25451 | 2026-09-22 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 768f7e90-580a-3f80-b008-2b2f03e1e64a | -5.93776 | -57.70358 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9756718-1ac0-3d65-94f2-4d6567a3d384 | -5.78071 | -43.7694 | 2026-09-22 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6fe8f10-d9f7-34dd-8564-f556645781b4 | -5.93745 | -59.98217 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 809cb595-a2bf-3575-95a5-ec17658cc2d5 | -10.45653 | -51.32799 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02093d44-3fb4-3f1e-986e-13dfedb885d1 | -3.08508 | -61.16751 | 2026-09-22 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f9d6411-8f59-30b4-b160-a4c36ca00278 | -4.3085 | -55.59232 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ada0da83-dd68-3341-8204-5a393d66b75c | -8.42189 | -45.85063 | 2026-09-22 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ede1773-2a0f-33f4-b5e1-e3675d6e4e2a | -6.28056 | -56.03468 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77d72796-55c8-3b73-9493-416351be90ad | -3.34281 | -59.86127 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README59.md)
