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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2a486c7-0ffd-3a26-8395-d56040a7ec5b | -6.65934 | -59.93774 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f4b6881e-1378-3e90-82a1-970205c12a33 | -6.66005 | -59.95664 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| c5a693d8-232f-3e6f-93a6-b32326d5a2f2 | -6.59151 | -59.92395 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8cda1355-6c9a-348a-a79b-fd85f7029194 | -6.66078 | -59.94923 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| fc478f79-e86b-3ef5-b90d-0fc5356563ab | -9.46586 | -67.42995 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d22ce1b9-463d-3ee8-9af3-350bd360564b | -6.65552 | -59.96056 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2603fec7-a9c1-3083-8034-5fa014bc8fdd | -10.30422 | -59.4594 | 2026-09-05 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51e91847-5261-3ea1-bc7a-3103f557e129 | -6.66225 | -59.94003 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| a38eb5dd-34a8-362f-9507-39c87fa7cc45 | -6.59604 | -59.91993 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6d7a8810-bf03-3210-b1be-d93d10f934f7 | -6.69088 | -59.98062 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc362502-4442-32e2-9cce-dfd77427959d | -10.76157 | -60.74131 | 2026-09-05 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6456b92e-6577-3748-a92e-f6aa26995048 | -6.65252 | -59.95541 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 611f6641-51c7-38ce-aa95-e6bdc65eb5ac | -6.64874 | -59.95485 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43b956fc-0418-339f-bbee-e3b2698866a2 | -6.59377 | -59.91026 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0c34f2ea-8b67-3d84-bfe4-991e570c8fff | -6.68486 | -59.97021 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b87a8ff-92bd-3868-a39f-c03569667175 | -10.16426 | -69.34659 | 2026-09-05 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 826e6ca1-b0b8-3a63-9bc0-3a4c88d0377b | -12.43369 | -43.27778 | 2026-09-05 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fb0eb24a-6991-36c2-b319-e752898c28ae | -11.53955 | -44.896 | 2026-09-05 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7dbc559-7dd0-3ce4-8313-f29b5e77eeb6 | -6.65398 | -59.94349 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01cd1dca-8489-3bad-b9e4-579ff0edb459 | -6.65775 | -59.94406 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| d612d7a7-ea22-31dd-9d49-1bd331e46543 | -6.69464 | -59.98127 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7229f4d-c004-3c60-824c-eeff07ca8914 | -7.54281 | -61.34232 | 2026-09-05 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5160e696-72e0-3dc6-86cb-325758de8a24 | -6.6841 | -59.97478 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 815b2f89-ae01-3fe1-96a4-f483c59a2bf6 | -9.5341 | -68.63053 | 2026-09-05 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d208a74-f625-3ecf-8427-c8a6b5008df3 | -6.65404 | -59.94631 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7a800e3b-7c65-38ab-badd-11389a3fde47 | -6.66757 | -59.95787 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ac8e468-631d-3813-be93-9a8b13770984 | -6.68718 | -59.93289 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aca165b-b3c2-304c-9d12-2fd1fe166431 | -6.68266 | -59.93683 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff27146c-03a8-332a-b19d-4c7712152882 | -6.67814 | -59.94079 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 467302f5-f4a0-3365-b0dd-cfbced03f644 | -6.64874 | -59.95204 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fc0e2f31-4ddc-306a-b2ce-06d0c1d94637 | -6.59001 | -59.90966 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c3ade40-c389-3a69-80f5-c0d8adf1e10f | -9.1312 | -67.80316 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2622cc0b-3a09-3cea-9ef7-e55b8f98e09c | -6.66081 | -59.95205 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 83f3d111-93b6-30a5-9dd6-90fe1e91ea1d | -7.54685 | -61.34304 | 2026-09-05 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4e39a8f-0b5c-33d2-b12c-b54316f85924 | -6.59227 | -59.91933 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 11f4c5c6-4e3e-39be-a2fe-2da329ec55df | -9.53673 | -68.63462 | 2026-09-05 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3047bc11-d596-3921-9faf-6811867ce906 | -7.26142 | -61.10175 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84a2b69f-7610-3225-a802-9358a96251cd | -9.38506 | -56.9935 | 2026-09-05 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c9188fb-4ab6-396e-b5c5-2ff89915101b | -9.38175 | -56.99297 | 2026-09-05 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0edc37b3-a9a8-33a7-bc98-625f87749355 | -6.66987 | -59.94411 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c0b11a8d-5403-3562-a329-14086b423e5a | -6.65175 | -59.95996 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69c0d459-3048-3a2d-a06e-a5c66a601a14 | -6.65555 | -59.95776 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0abdbfaf-f352-38f9-946c-81161ac5cffa | -6.67062 | -59.93957 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fae1de7c-baa1-3324-99f9-7f8ec690aff6 | -7.54745 | -61.33948 | 2026-09-05 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dde8680-7c31-3034-8a8d-7599d17d35da | -6.66381 | -59.95726 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f55c6bcb-b4dd-3d5b-90f4-6857751cc5dc | -7.26201 | -61.09825 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 211c36db-5996-3d72-a977-b652b52986e7 | -6.5855 | -59.91357 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2539db1-81ed-3f38-8149-9f6de5709e7c | -10.16469 | -69.34766 | 2026-09-05 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 452498f3-80c0-334f-8aa4-4844ca0c4052 | -9.04814 | -67.6395 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b84215d-7deb-30dc-b253-c53567e9193c | -7.55209 | -61.33665 | 2026-09-05 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21cc5d36-dc88-39b5-afc9-42d4679a9c5a | -6.65629 | -59.956 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| ec3c5695-c022-362d-b5e2-d5c1c1cca8c3 | -6.58625 | -59.90906 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0285a32-fc42-33fa-b8b3-f04a22735dcb | -6.67438 | -59.94018 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a81403d-ea20-32da-b8d1-de6df735a490 | -13.43086 | -43.82322 | 2026-09-05 05:06:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 96d625e2-79a6-3d56-9a6b-d3786bee1b91 | -6.67733 | -59.96895 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d15bb47-6f9f-3897-8a91-ee75f913d6a2 | -6.68562 | -59.96563 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0de77786-4ae2-3115-a045-39d3b1cdc6a9 | -6.68109 | -59.96958 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5745def7-e8ef-30ce-8183-723a04c97b77 | -6.59302 | -59.91479 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2ce70e26-200c-3e0e-8dec-2523f2436c27 | -6.67363 | -59.94474 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91a0e647-28d1-3dd7-8a68-217861cc572a | -9.61415 | -48.5654 | 2026-09-05 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| acd526ef-8620-3157-8fe7-c22da7f694d2 | -6.68862 | -59.97083 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74e8b10c-dc5b-3428-afca-af7148777313 | -6.66311 | -59.9383 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| c370aa8d-f003-32f1-b606-1257a72822e7 | -6.59678 | -59.9154 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 046ed44c-9bca-36e6-99cf-fa2ac0190bd8 | -6.66158 | -59.94746 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| e5c77037-2f38-3338-90d4-11f85afd5cc3 | -6.65848 | -59.93948 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 88ab6a42-6b66-3e53-bf8f-fc710fa8245e | -12.44423 | -43.27632 | 2026-09-05 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c7672749-0570-3d6e-bf28-4d2da5f44d5b | -6.65178 | -59.95717 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 403ec9d7-dee5-3a8e-8511-5e7a06c28736 | -6.68642 | -59.93744 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0569f240-4a49-36e0-ac7c-fcfc6cea1b68 | -6.52595 | -59.94303 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7eff20c3-f2e8-334d-9797-974f9eb9476a | -6.6691 | -59.94868 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 41971eae-c4ff-3210-b34a-5b620dfc3be3 | -9.75103 | -66.61888 | 2026-09-05 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0a8e03f-9ad4-34ce-b6e5-d4c97eda4863 | -6.65931 | -59.9584 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1da36ea1-4eaf-39cf-8f2e-8fbc31a83856 | -6.65471 | -59.93893 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5b38cb0-ef0b-363d-a689-e2e03f94a726 | -6.64951 | -59.95028 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ddb6c030-bf3b-3724-be39-32a1344453f6 | -8.96998 | -69.27884 | 2026-09-05 05:06:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ed0b7eb-482e-3be5-a345-f993fb8ab02a | -12.43633 | -43.28265 | 2026-09-05 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cc0e39f8-388d-34f9-8b6e-b50be09b377e | -6.66457 | -59.95267 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 2615734b-f5f4-3471-aede-c922787e46b3 | -6.64948 | -59.94746 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0ccd4d26-1cab-3c50-9a14-0aed6891a46d | -6.66304 | -59.96185 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 285551a1-0c46-323f-b480-94b597e993c0 | -6.65104 | -59.94117 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41b3b912-e4fc-374d-9062-61f4a020020e | -6.66534 | -59.94807 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| aeec66dd-5a14-35bc-9bce-8b7f52aa8882 | -8.47042 | -57.63445 | 2026-09-05 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7557eebf-59dc-3486-bd48-580faef3b7f4 | -6.6789 | -59.93622 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f3398ac-5bca-3d77-8424-c8ed8c0143b1 | -9.53045 | -68.63329 | 2026-09-05 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06155bcd-00bf-3e4c-bc5e-db0dd13b035e | -6.66611 | -59.94349 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| df49b467-e80e-3ed0-a69a-f8793b52ddaf | -6.68342 | -59.93228 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43a877a0-72ee-31cd-a171-0de68cbd55da | -9.46463 | -67.42873 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9779363-e992-3d67-950c-28a8a5fbef20 | -9.05495 | -67.63617 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 616fae84-c41a-39b2-bd66-33508e7e0197 | -6.65781 | -59.94688 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 50d569b2-d115-31f4-8e0c-b6f171562e0d | -20.34438 | -47.59683 | 2026-09-05 05:08:00 | NOAA-21 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77e36dfc-780e-3fe5-8ef9-b5350ef07880 | -19.76279 | -46.61977 | 2026-09-05 05:08:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71e8d3a9-e58d-3c01-9805-f31132123dbe | -21.52052 | -50.03362 | 2026-09-05 05:08:00 | NOAA-21 | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bd71536d-b091-3ecc-b433-73cc99434bd3 | -16.2312 | -57.4332 | 2026-09-05 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 50e9b0f4-7de0-3c36-b542-1c0d6afe92d0 | -17.16561 | -55.92034 | 2026-09-05 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7be47c0d-0883-3be6-92b6-2d74d5a3b5c5 | -21.39276 | -45.509 | 2026-09-05 05:08:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| cf119629-d5af-3cbe-8393-d7f0001c3c79 | -19.16645 | -57.3448 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8178fcf6-5aff-3118-9581-2611567d3f1e | -20.76625 | -57.88903 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 09561858-f487-3fd5-9ae5-f679ed7570e9 | -17.1887 | -54.30296 | 2026-09-05 05:08:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6163b5f-ffad-3a8a-aa2b-34e6af573642 | -19.20255 | -57.38187 | 2026-09-05 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1409cbf2-561f-33eb-9276-fe7daf9ae766 | -14.74255 | -47.14629 | 2026-09-05 05:08:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
