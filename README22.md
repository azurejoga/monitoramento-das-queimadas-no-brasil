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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4118ef2d-7fed-3a50-8b20-e297f680cba0 | -5.2904 | -56.01505 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54625aec-8aae-3de9-becd-f5d1ea288095 | -5.77533 | -45.0724 | 2026-09-05 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dd67b46f-bc93-3e67-a08f-fba66ffbde1f | -1.24657 | -54.53175 | 2026-09-05 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e964901-7875-37a3-b103-6e44b82a4ff3 | -4.36921 | -47.78154 | 2026-09-05 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6e5a5d1b-ba72-3c26-bac1-948fafc3cd5a | -6.03929 | -60.1661 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cb63ab3-45d3-3c32-bc76-1a2fbac64772 | -5.25407 | -59.97647 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 154a2b81-4c4e-39fb-abda-ad6300478de0 | -3.76745 | -61.75709 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc405733-bdb1-30c2-b320-b835446dd236 | -3.38569 | -61.33657 | 2026-09-05 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e51ea220-1911-337b-8082-4cf3c681a937 | -3.21277 | -57.85504 | 2026-09-05 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccbc827d-6acb-3bce-b90b-4979112933a8 | -3.58637 | -53.22055 | 2026-09-05 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 49656346-8df5-3f3f-a173-7938f31c5ae0 | -6.07312 | -59.98222 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec0e86bb-e469-3100-a806-44f3273030b2 | -6.13328 | -59.92274 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 282853c7-b77d-38c9-945b-219a0cca6d83 | -3.29877 | -57.88449 | 2026-09-05 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b21d2d27-bd70-30b8-a41c-11650fa31aee | -3.90285 | -52.03432 | 2026-09-05 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 073fbe1f-9d2c-3d7e-8600-bdb27b567f2b | -1.18606 | -53.82855 | 2026-09-05 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 140e24a3-820b-3bfa-bd8b-5a0884e4447f | -2.91588 | -61.00351 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d80ee08b-0624-38ee-b813-30d531c1e71d | -3.78866 | -55.87372 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cffef7f5-2de3-3c19-a507-b1f9d430682f | -6.35965 | -46.11496 | 2026-09-05 05:04:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46ed8101-f759-37a9-8d34-cca8f0d354da | -4.39549 | -56.34298 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e274df1-7b35-314c-afac-19d78fd45c8c | -5.34362 | -56.02353 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12f60ad9-99eb-3bb9-9626-e0ae9f4fdec4 | -5.32931 | -56.02837 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba9d0d9b-7a78-329a-808d-c49d242a5afc | -5.34416 | -56.02007 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d8fcd43-70ba-3b5d-8cef-3be8194e6583 | -2.91654 | -60.99952 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59b00e73-cb9b-3e2b-bf35-fd05aeb7e454 | -3.9328 | -59.3387 | 2026-09-05 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ae21de16-c768-3852-a33c-f449df1c1794 | -3.14577 | -60.65195 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0aeff43d-77c5-3108-a91e-b38fa976cc82 | -6.11929 | -57.68453 | 2026-09-05 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c66d579-301d-3585-a68c-99eca577bfdd | -3.03652 | -59.36463 | 2026-09-05 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac4aa88a-6630-35ee-b87c-c18dce6718a8 | -5.31686 | -56.01916 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80dd653f-4e4c-375a-a8f4-08dcfdba3b42 | -5.29863 | -56.00572 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03313635-0a2d-3299-94e5-898d7d0a0239 | -5.31463 | -56.01174 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5520c76f-155d-3b52-8d46-fc3750c0b6a4 | -5.65431 | -60.23464 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 87dffae3-17d9-38ba-8894-597b042f19ef | -5.84054 | -60.25529 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fbe6f150-f914-3cb3-81c3-6bc617e168f6 | -5.32985 | -56.02493 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c474398-088c-3c6c-a5dc-ee3d1a88b28f | -3.72244 | -59.3687 | 2026-09-05 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93fe8a3b-e7d4-31aa-9c8f-f5ab81a1e6c5 | -2.8103 | -48.67315 | 2026-09-05 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fe9db1fd-76c7-3714-8f1f-712d04d576bd | -5.33977 | -56.02646 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5fa47a59-1693-3933-ab14-95d6c19e8369 | -5.33646 | -56.02595 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 68924821-bf9e-3598-b15c-5ae5a44db5e3 | -3.79528 | -55.87475 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 132af29f-61e4-3b24-a89a-0622d21d9c9c | -3.07894 | -61.18095 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4448379-128e-3b7e-a223-5481c53e950b | -3.76158 | -61.76505 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6248faa-5a73-3f3a-9d90-d81397f27695 | -1.95316 | -48.22654 | 2026-09-05 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 781aef60-60de-38d1-bb28-f3e0921d7002 | -5.32294 | -56.02364 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f9add88-d5e1-326f-bfd0-48ed021734a4 | -5.17388 | -56.06359 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19c2db97-07f5-3169-b378-f8206b5e4af0 | -5.17773 | -56.06065 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84ea83c0-462f-3195-ae88-1180ec60eddb | -5.08057 | -56.2904 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94639dc5-fb08-3e78-8418-acc8bdbbee17 | -5.16726 | -56.06256 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21324e43-4e22-3e50-bd5b-be8fef641f9d | -3.25597 | -50.82529 | 2026-09-05 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb1756bf-a171-33e3-9479-829f6246fc04 | -5.34308 | -56.02698 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f2a700ac-e1b0-353a-af3b-53d600c993e2 | -4.13047 | -56.34037 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b0b1685-f503-372a-8e6c-774146f7097f | -5.32876 | -56.03183 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1476a8e7-d69c-3c8b-a5d4-3cdcbde9e134 | -5.17057 | -56.06307 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1b79aef-2bca-3535-976b-4800d0c9dfc9 | -5.29425 | -56.01211 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02b8b169-10aa-3f3c-965a-8e18fbe5e20f | -5.3453 | -56.03439 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 2a25f662-3036-3cb8-bf36-d212e0399fb7 | -4.08212 | -56.21498 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 887922ac-3ec8-377f-ad06-71ab02067afc | -5.83666 | -60.25468 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8da6348d-16ed-37a1-ae30-7601fefcf83f | -3.88829 | -52.0321 | 2026-09-05 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c165ba7-2df6-32cd-9f80-9f047e5f05d5 | -5.30748 | -56.01417 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 611b9770-c1f8-3b38-b3e5-f9f7bc7b87c0 | -3.93209 | -59.34327 | 2026-09-05 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b838e90b-bb2d-3ba0-9ef7-5a284a2333d2 | -5.77011 | -59.1893 | 2026-09-05 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba9f6d10-246d-3762-997e-6b2e78adfb72 | -5.6535 | -60.23955 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 673ecb98-ae9a-3bbb-8380-1d0744014bc5 | -5.33815 | -56.03682 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0c0a7270-5c0c-345d-9ff2-57dfdc9705a3 | -5.55599 | -60.17145 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad7004ab-e3ca-332e-bb55-f5bba44fd09e | -5.17881 | -56.05374 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be1e6ade-30bf-3784-aef8-79b1a5deab61 | -5.17328 | -56.04579 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 013e258d-59b9-380c-92fb-3bb8831ca7c5 | -3.8278 | -60.76484 | 2026-09-05 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8c420c7f-5c9a-3306-ae72-c0ed339c5c00 | -6.03465 | -60.1703 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73aac2b4-edcf-364a-b569-62d1191097bb | -3.66811 | -59.27211 | 2026-09-05 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f004a435-ea19-3a11-8440-eccf24bf9e17 | -3.43767 | -52.81395 | 2026-09-05 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a1b8f9d3-8f81-3a6a-a491-bd377ba4c25f | -3.08374 | -59.30832 | 2026-09-05 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 560e06fe-89b6-394f-9048-13ed1bc825ac | -5.32654 | -56.02441 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e4377e4-ebf0-3611-9245-c14ae72528cc | -5.34145 | -56.03733 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 91fe3292-bf01-3b99-bdb5-573128496209 | -3.17676 | -51.54399 | 2026-09-05 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c15d6135-a1ec-380b-9b8f-ddbe236cba31 | -5.3174 | -56.01571 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b05c6b04-f105-30a8-8d24-7ef2b6a237ac | -4.67907 | -55.63974 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f8fca738-d391-3867-bca9-e5f133bbe7eb | -4.15841 | -57.95403 | 2026-09-05 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e04e31b-22e7-3949-ad01-fb856bcdc0a8 | -4.10519 | -50.44293 | 2026-09-05 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdff695c-e928-37e4-8cb7-524138d80391 | -1.74614 | -55.8635 | 2026-09-05 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8905c141-4625-3074-adee-54e575f5aeb9 | -5.42947 | -60.18282 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de5bbf2b-87d3-314e-ba3d-8100a70ac285 | -5.1799 | -56.04683 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d233b05e-9354-34ea-9b98-27121fd19b0f | -2.825 | -46.71063 | 2026-09-05 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0529d03d-da28-3e8e-87b3-fd78ca65ac43 | -7.22793 | -49.59306 | 2026-09-05 05:04:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 175f96e6-15c1-3b81-ba1d-3f422ffadcea | -2.04792 | -56.43244 | 2026-09-05 05:04:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e67873f-f431-3ba0-b4e2-8fae6d68ad7a | -4.16144 | -49.70348 | 2026-09-05 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| de623790-92a7-38ea-9951-d74913581788 | -1.32848 | -55.68412 | 2026-09-05 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 680de41b-6dbd-3e02-8d62-3de76dfa5b4c | -1.18273 | -53.82807 | 2026-09-05 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d1063d7-e532-33f0-9136-cd7efdb9d5d5 | -3.14816 | -60.63696 | 2026-09-05 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbd41ef9-157c-37b7-8b93-226b582ef16f | -3.63307 | -54.756 | 2026-09-05 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a400d89-3da8-32cb-9048-9a18dc6105d7 | -5.34693 | -56.02404 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bc70c541-23d5-38c8-bbc6-8b6ebe25a333 | -5.31247 | -56.02555 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 296db129-95a5-3d5c-a31d-24fb61945759 | -3.77043 | -61.76646 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a4fce643-af8a-3479-a6c6-ea358e37c93a | -3.93282 | -59.34133 | 2026-09-05 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 01425565-4566-3af5-8952-ab1d120a4350 | -5.17112 | -56.05962 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 85db941b-a158-3207-8a40-197360d05599 | -5.29647 | -56.01952 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d75c4719-51e3-3d55-8cb0-f22397723506 | -5.17166 | -56.05616 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 71e97576-2764-355b-868f-644dcb19bc76 | -1.95634 | -48.22528 | 2026-09-05 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad6fe3ca-d638-3762-b9a4-0d8dad93ae7b | -6.0308 | -60.16968 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 015857a8-de1d-3591-8f2d-983bea68d1a4 | -3.58284 | -59.41468 | 2026-09-05 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9be5804-a5dd-3302-bf20-ff85aaba7989 | -3.23395 | -50.57378 | 2026-09-05 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a25c76d0-ecab-3ae7-bc61-27d90e1d8100 | -3.80414 | -55.8832 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5be35acb-b980-39fd-a415-1a1bfdb6b13b | -5.46353 | -60.04934 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README23.md)
