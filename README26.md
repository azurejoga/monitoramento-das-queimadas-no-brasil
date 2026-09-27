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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b34d1281-9369-311f-92b0-0b741f1732c7 | -3.96701 | -59.34475 | 2026-09-27 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0e2d8d0-e94d-36a7-b9b2-5032b09b0515 | -3.96508 | -48.12084 | 2026-09-27 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9acb6a53-5a8f-3e36-a1c8-e8d531a8cee9 | -5.18292 | -46.11876 | 2026-09-27 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ccea9a0-4175-37f7-b719-1fe578e50074 | -6.04714 | -53.60204 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c11c712-6c8b-3535-8d53-17194f408247 | -9.76278 | -48.20102 | 2026-09-27 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b26758ae-28aa-3c9e-a144-4c995448d2bf | -3.00536 | -54.202 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b34cffa1-e25e-3338-8868-31fe34d3b6eb | -3.01584 | -51.53439 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7429839d-735e-3a4e-9ca5-3fcbea19408c | -8.28461 | -45.42208 | 2026-09-27 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfda29dc-6bc0-3867-966d-a21804e9b901 | -4.98192 | -56.15367 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2ed8bac-122c-3846-84af-f6353e38cd7f | -3.42054 | -50.41968 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ded2a029-debc-3465-a254-d95a12b2560d | -3.18849 | -49.25021 | 2026-09-27 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 605ed490-d1c2-31d1-93f1-69ddb6b54e9e | -2.99751 | -50.47429 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87494345-3f28-3eb5-b848-b053763e6ffb | -8.50125 | -54.78102 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a258ced-4880-3be7-9a43-a6a9877b15b7 | -2.78931 | -57.69305 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 62c170e1-4bb9-35fd-85c3-bc34e127267c | -3.95819 | -48.11486 | 2026-09-27 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 585ddc8f-0353-3ead-b51f-fc4b68b511ea | -8.33935 | -44.16413 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7dfac933-ef1c-3b68-aea9-d1efcd7150e7 | -4.54523 | -54.96635 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ecc4f2cd-751e-374e-baa4-f52dc306033d | -6.78004 | -48.66684 | 2026-09-27 04:51:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0b15fe9-9ba5-3408-945e-c733dc5b094e | -4.15803 | -54.15085 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2d67777-88f1-3afa-8884-b0876be0f7c1 | -6.16146 | -47.13207 | 2026-09-27 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87fb6464-00b2-33cc-a0d7-0f87a78d33d8 | -4.36088 | -55.28128 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4762e56d-10cc-3ed6-84e6-2837baff918a | -2.9596 | -54.0917 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24b73e1d-db3f-3a41-871a-d59489afb6cd | -3.30031 | -54.69445 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68189024-60a1-318c-8eb9-57459f7dd0b7 | -2.73891 | -49.46642 | 2026-09-27 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 13c97753-590b-342c-9a76-ca13b171bf95 | -6.41999 | -45.85524 | 2026-09-27 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f416246-631c-33cf-96f3-7e2829b271a4 | -2.9169 | -54.16177 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d81f4d67-d1cf-317c-a543-a3924eec7c1b | -4.36509 | -55.27779 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78dd48ba-77be-3974-bde4-d7d2d0741754 | -3.05902 | -54.39267 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd2c2704-fb22-3267-b2ae-4ae7704134ac | -4.58685 | -54.91668 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e668770-2223-3d89-8c53-043aded77c6e | -4.25394 | -51.05032 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 795eabb4-7aed-3eb3-aa1d-4ff700dc0c1b | -4.54399 | -54.97416 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0869b88-f38d-330e-9297-b8070ddc3385 | -8.35695 | -44.1533 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a35caa1e-b66c-32b2-acc0-26638f3ef2f9 | -8.34806 | -44.13839 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 583cc12f-0e0c-3338-bf8e-d2a22e58a75f | -7.28145 | -55.57693 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59f10bad-329d-3307-87aa-94d3799d041c | -2.575 | -54.03652 | 2026-09-27 04:51:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d36e0ab6-a93e-338c-8629-1e94892587ef | -8.27877 | -45.41636 | 2026-09-27 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18e7a1da-b9f7-3b5f-9783-99de1ee8f31b | -3.06821 | -54.40186 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51925db6-e60e-335c-a8fa-506de661e29d | -4.5003 | -54.95543 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d8bbe90-f6f8-3524-ba92-0a4da3c03060 | -8.4951 | -54.77629 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd153f84-4336-37f6-91cd-30a7c94dcdd8 | -8.34907 | -44.1725 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 214.0 |
| a0abb7ec-70a2-32e4-9d78-3a162078a52c | -5.57527 | -47.41445 | 2026-09-27 04:51:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbb9126e-3aec-32c7-9532-c5aaee5a55b4 | -7.33003 | -42.0871 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b9288b51-828b-301a-90b6-4ef02180e164 | -7.19161 | -46.50542 | 2026-09-27 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa3ac92a-7fbb-370b-a9a8-52cdcbda5ee2 | -3.3613 | -50.46643 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9dc9dc6e-89f0-3cd0-b10b-678fbecd8775 | -7.6899 | -54.76265 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93753a6e-29bd-3ac4-89ad-c546c0556ee0 | -3.21592 | -53.95625 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46909d33-9a52-3144-ba22-87fc8567c26b | -1.94756 | -52.73151 | 2026-09-27 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11ebbc2c-1480-39e2-bbcc-2bb23d0ca824 | -8.35355 | -44.14541 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 079f0b47-6937-3e4b-96b6-d2ab1b7abd3d | -2.9328 | -45.50597 | 2026-09-27 04:51:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03381295-4ab3-39e6-a722-6006bebc6850 | -1.7431 | -55.25229 | 2026-09-27 04:51:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fe8fe6e-0c71-3e41-b817-9da79f29bc10 | -3.50585 | -50.4813 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c013cc96-6b4f-381c-bd7e-3ab0bb9a032f | -3.43356 | -50.33579 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46e9a9bc-3aaf-3a15-bd23-718f41cb9897 | -2.66878 | -56.46182 | 2026-09-27 04:51:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed344f8f-083d-3433-8586-10e9f12dcde5 | -6.87149 | -59.87155 | 2026-09-27 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eda67883-875b-349e-bb08-12542f3268fd | -7.69328 | -54.7632 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e3a42f3-1d28-3e56-992a-7feb6b533e98 | -4.56582 | -54.94961 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35c49dfe-6357-3067-8a56-149e7a9a290e | -2.80193 | -57.69503 | 2026-09-27 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b9916a5-7474-32f2-b3f0-7d3141f24338 | -4.47614 | -54.97158 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9882959c-d492-3604-8234-f38082cf89a9 | -6.64111 | -59.95005 | 2026-09-27 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 626aaee7-699d-3939-ac39-ed1ab4cac9ec | -7.29962 | -44.59696 | 2026-09-27 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49a2b8d9-9d11-36f8-94ba-fcf253b5bd25 | -3.22541 | -54.32101 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 906de4d4-d0a2-39a3-8625-a794d62da6e6 | -6.0686 | -57.8135 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1051be40-cb00-3208-9b2a-9098cef184cf | -7.98082 | -44.80744 | 2026-09-27 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce5fe0b8-cef6-38a7-b752-28439c442255 | -3.08149 | -54.40781 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4412a9a-343c-301d-948b-922fba20dd4f | -3.67739 | -50.84547 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c53cb64-72ab-31b8-bf04-5736f2b46a5e | -4.58527 | -54.91715 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6cbdcae-06db-3aa1-b9d0-2813e6bc7d87 | -4.29302 | -48.62163 | 2026-09-27 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e185d47-4231-3eb8-b83e-ddc8dbc80e00 | -2.4497 | -49.22433 | 2026-09-27 04:51:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2cb5f4fa-6cad-3fb7-a8aa-e5f10913f13c | -6.09975 | -57.6216 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46725a32-89e5-385b-ba31-6e64a14e101b | -2.92153 | -54.15482 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cfdb58c-4060-35b0-b39d-be3ed33cfd3f | -6.87861 | -55.55833 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78caf4bf-e681-3a93-b759-0350e11213d9 | -3.0516 | -51.21738 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88427e56-6da5-3e0f-bb61-5374b44e2231 | -7.70005 | -54.76428 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 582c2d45-a96a-399d-8238-ffb113b13a72 | -4.69344 | -55.9429 | 2026-09-27 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ce9e594-d748-34a8-8097-15b7f519e386 | -8.37461 | -44.1422 | 2026-09-27 04:51:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0530ce98-73b8-3d05-a5b7-ae73f947e686 | -4.54111 | -54.96969 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 177ea6b2-62be-3245-85c8-2d1e5c835717 | -8.34318 | -44.13428 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84d72060-1a5c-36ef-91a5-33508c5fa523 | -4.55594 | -54.94408 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79f6c0b3-79d0-3b49-b6f4-9d7f175fa61b | -4.30517 | -46.5749 | 2026-09-27 04:51:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0ac19da-a01d-3743-80a5-fe97aaef22b6 | -5.74758 | -45.06192 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 144cf83f-2a34-3bc5-a492-860115ef65f7 | -3.07881 | -54.37993 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1c61d87-2916-3ea3-8f6c-51ca4a9bb06d | -6.13613 | -53.05768 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d35366f7-d72c-3b1a-8fb8-6d69e17f796d | -4.55244 | -54.94354 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eba6e3fe-c420-341e-8e10-aa36ddb4b5d2 | -6.81034 | -46.24531 | 2026-09-27 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f44fda3e-09d9-3e9b-a048-c21df0acfa6f | -2.90888 | -45.42052 | 2026-09-27 04:51:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| de990223-360f-3625-92e1-5fccb20c3279 | -3.07862 | -54.40348 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ba4a74a-5b53-3c8a-9672-c438bfff2002 | -5.60465 | -47.44079 | 2026-09-27 04:51:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f49c39d-d41a-3762-b725-00034c05b36c | -3.02241 | -51.38335 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8761915-788c-3dcd-a40c-85398709edb1 | -2.42602 | -49.30913 | 2026-09-27 04:51:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7d573c43-8dab-3428-b387-c73603946c79 | -4.30352 | -49.12692 | 2026-09-27 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c993b05e-2ef3-3bd0-80bc-9ef107e163d4 | -7.60096 | -55.05156 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 390ebb75-36d8-3498-a104-ea24cab7a163 | -5.87957 | -51.95276 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 749a1b12-242a-3a2a-85aa-0669fd6fe8e7 | -3.07064 | -54.38661 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01f38387-f377-38b1-a632-869a87590e9f | -7.88641 | -54.72316 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2bb78ad-08b6-35dc-89d2-aed697f1433d | -6.17436 | -44.59647 | 2026-09-27 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d1a1b77-65fa-3f06-94e7-2a59b7750bec | -3.7169 | -54.6538 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac8ef1d4-b782-3a9a-bb84-632386c33519 | -8.34864 | -44.17582 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 36f8cd46-d7a6-36e6-9488-8c5fad95380c | -7.12286 | -43.66695 | 2026-09-27 04:51:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a810b21-7971-3dc1-a22e-dc88d87e66a7 | -7.88477 | -54.7232 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a386fdd-79f9-3511-ad8e-3160c557f7df | -3.42449 | -50.43893 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README27.md)
