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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baed3437-7c9c-3525-b7a4-fa583ede3f08 | -8.32277 | -47.93293 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| abc49a74-fbc4-3332-874b-a4c133d43bdb | -4.36261 | -48.72606 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 937ff0e2-5784-3942-ac61-fe03c300f484 | -5.64195 | -43.27868 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6c7fd5f-2f41-31aa-9dbf-b309a1a328d0 | -6.95132 | -40.91638 | 2025-10-30 04:25:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| faa6b3f4-1ace-3897-a3c8-4333696391d5 | -4.66756 | -46.02088 | 2025-10-30 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1be38e8f-012b-3817-9687-11706a06aea2 | -5.64216 | -45.98137 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 47fe05de-eec5-3e78-b35b-99ea2cc43d6c | -7.06336 | -44.46529 | 2025-10-30 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34b03cdd-42a8-38f2-a5cd-c5ee9375f627 | -11.03605 | -47.83774 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 250f48ac-1b50-3b38-bf39-08722089aefa | -5.99664 | -42.50026 | 2025-10-30 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2823d74f-a73c-3ed4-a535-7be5bc2fd4a9 | -4.35903 | -48.72548 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2761ad5d-afc6-39d0-ae4a-3bb45d9412a2 | -7.8664 | -44.22717 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 158964b6-ed47-358e-af83-0d457dc11e13 | -4.33123 | -47.88906 | 2025-10-30 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d8245c60-a08f-398a-84fd-db8c27aa006a | -11.96187 | -43.2879 | 2025-10-30 04:25:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecd7b4b4-9c9c-38fb-8912-3f24bde99fd8 | -8.7216 | -48.00816 | 2025-10-30 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 793958d3-f5c6-3c62-99f9-72953a65fe2b | -7.40355 | -43.93882 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b6a4d50-413c-37ff-8bf0-ca8df12d19bb | -4.48674 | -49.30619 | 2025-10-30 04:25:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf54236b-596d-3764-951f-212fe7333b22 | -11.16181 | -48.34652 | 2025-10-30 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6678df6a-d14a-336e-a102-17fa1cf742cc | -5.79475 | -40.81234 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1b3c925b-4848-3df4-9fd9-a4afe3840ace | -5.4765 | -45.00306 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4c1ba5a-d04c-3173-beee-d361e68593ec | -5.89406 | -44.95947 | 2025-10-30 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b37c46d6-312e-31cf-a7b9-f68771c5660a | -7.61194 | -43.56667 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33810ed2-66e2-3e23-92b7-8bad81520998 | -6.21182 | -41.82535 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0461237f-b4b3-3bda-aa41-d2b8de11d27e | -7.50052 | -46.26161 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1903465b-c495-38e2-b6be-783210ce2114 | -11.1672 | -47.71873 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7df1b79d-f452-3b1f-a32c-144142616467 | -4.84266 | -45.42749 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d055a90d-8af5-3ef3-b2c3-88b88682c88a | -5.28158 | -47.24204 | 2025-10-30 04:25:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f410e025-9604-34b3-a4d7-f22be44cee13 | -5.80596 | -40.82101 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 34bc0776-dff4-35de-a849-e068a828312f | -5.22933 | -46.14145 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02504906-4111-3f93-860d-aa8c63715cca | -3.97644 | -51.07105 | 2025-10-30 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08ca63e7-d856-33b3-8403-bbff8c5b6b0e | -10.55843 | -48.99654 | 2025-10-30 04:25:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa3cc05a-6f5e-3838-8036-450284f548f7 | -6.22118 | -45.36665 | 2025-10-30 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81dd5d8e-8fdc-33b6-9381-8b0a37a515fe | -11.00806 | -47.75742 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b43ab5f1-2ff0-3340-a3df-f1401ee7ad89 | -5.22602 | -46.14093 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1931d3c5-2ed4-30bf-bee5-06b44d4d4eda | -7.58168 | -43.64922 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e24f31d1-b66a-3200-9836-b6a26a47112c | -10.35012 | -47.81254 | 2025-10-30 04:25:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dfd8cb6-c528-3a5f-944f-cad78c156401 | -7.06171 | -44.93489 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e434215a-877e-3e46-ad59-c20edb75508a | -7.27003 | -46.88126 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8aa12d8b-1bab-3215-b0d5-285821d7e47a | -7.34723 | -47.63288 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bf7e4f7-27d1-3f21-97c4-a9f90536e13f | -8.32522 | -47.92941 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 285cdf2d-b78d-3d0b-b0db-d5dcd132c277 | -7.62314 | -43.58905 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c701714e-aa51-3466-bec1-1f2531673e2b | -6.13835 | -41.69955 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f0390822-ed03-3317-bdd7-41ead89b79a2 | -7.02155 | -46.43364 | 2025-10-30 04:25:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc8d555e-3961-39bb-8e97-f0e44dcb5b34 | -5.59013 | -51.12447 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71e6e6e6-94f6-3cbe-a34f-fde592e4ffbe | -3.7603 | -50.37302 | 2025-10-30 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 519e4471-1c40-38f9-bbef-a9157636194a | -7.95578 | -46.73503 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 962d2a73-81f9-3a01-bef2-f39e4810a866 | -6.9206 | -42.25246 | 2025-10-30 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c21fab37-a437-32eb-8035-2004a55d66e1 | -7.95083 | -46.74491 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab397865-0b2b-3181-9ce0-918ec06f2fc0 | -5.6005 | -51.13732 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 236686c7-f088-3bdc-84ee-337091d18dba | -5.64601 | -45.97844 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53437611-e299-324a-a2d8-c2c09722788a | -5.84104 | -45.53831 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a90bc8c-8e9f-304f-837e-3e3788b4353e | -4.84749 | -45.84821 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65f87c5e-f75c-3e14-960f-5f7a8b6983d0 | -5.12843 | -45.35929 | 2025-10-30 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f27a6f4a-841a-3dcf-bcb6-cbe67059a9f6 | -4.59669 | -46.05938 | 2025-10-30 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 136ea187-3066-3fbd-bf96-8c1d6efdcbed | -9.08818 | -47.90611 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7bd80ca-af49-38dd-a3bf-9361ba8e53c1 | -7.15534 | -44.70828 | 2025-10-30 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1f0091d-4bd7-328b-a672-373d4f77cd64 | -9.8925 | -49.1174 | 2025-10-30 04:25:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64d86e5c-31f3-33e0-b8e6-b06355529b8a | -7.27883 | -46.783 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08fe49aa-66ea-3ba3-a18f-74101d71677c | -10.26524 | -44.57941 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6ed6004-0fde-3d8a-8326-24572d74e6d9 | -6.51886 | -46.90446 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 12ea9433-55ee-3043-9775-8bd4a74a2de9 | -10.9335 | -47.79941 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f8e04d9-73ae-3fbf-9be2-551f2feeca9c | -9.90554 | -47.9145 | 2025-10-30 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0d95941-5aea-3ec3-a09a-803e3327b26e | -11.70882 | -46.69417 | 2025-10-30 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83a3aae0-cba8-3fc3-a64b-a8a5594afbce | -4.53724 | -54.96617 | 2025-10-30 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45ae7e11-8830-37c2-9bfe-c1dd6a351101 | -8.51985 | -44.09167 | 2025-10-30 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0dd2332-6ed0-352e-82a1-124ba8797d90 | -7.93193 | -45.48133 | 2025-10-30 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3900dfda-7b30-38c5-928c-9536075cf2cc | -7.26893 | -46.88816 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35d9763f-8c0a-3d61-bba7-968f8084c444 | -10.59341 | -47.92835 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b90b652-fe68-3370-b6d9-e383b6c32c4f | -5.42074 | -44.839 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99d4dc72-cbd4-3f68-80c4-e145e13a363c | -10.49056 | -45.04232 | 2025-10-30 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 59ee8aeb-84f6-3a49-9cd8-704b8ec890b9 | -7.38744 | -47.63934 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1c4935e-a583-369a-9f6b-b7954e553bb8 | -8.33135 | -47.93411 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| deae57a9-f882-31c8-8870-3cdd5ed86321 | -5.92807 | -47.32313 | 2025-10-30 04:25:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b706a87c-4869-367b-8529-2a08dbac25f3 | -5.40924 | -46.01494 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78cbf829-9e33-3900-b139-5ff0a82e4880 | -8.89678 | -47.80216 | 2025-10-30 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2a370d1-aefa-3a20-b448-f9c428df42f2 | -10.86143 | -47.86713 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 553a0dff-6605-37dc-b293-a819132a776a | -11.55607 | -44.69216 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38c4b317-2967-37f2-97ca-72e7abe08413 | -7.25787 | -45.5786 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5695bf9-2aa8-3d74-91d9-6d59c4c27000 | -10.98458 | -50.11855 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 582c4ea1-e614-3ab1-96e6-bb8255d3ba37 | -6.42303 | -43.7766 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12d47cd8-5a88-3521-bd03-2769e051c639 | -6.36943 | -40.97355 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 46ec20f9-b1cd-3026-b63d-61f7f85a4d10 | -6.42246 | -42.32486 | 2025-10-30 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a705dcbe-0839-3b34-88e6-f826b747a1e4 | -5.05939 | -45.32368 | 2025-10-30 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8f17b1c-a3e4-3fc8-95c2-f89776279037 | -7.31392 | -47.81886 | 2025-10-30 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a8ea370-c96e-33cb-9860-e4f756403c11 | -9.73689 | -47.69469 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 982c59b4-b582-3dcc-98d5-218d55c8a7a8 | -10.58484 | -49.75214 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4005cb36-5c71-3488-84e7-609d1b553296 | -10.37423 | -44.74244 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f4c5050-8cab-392e-a394-51ea07d9bf9b | -12.03095 | -44.80129 | 2025-10-30 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da52a4f1-064c-369c-afb1-f9aa60be4a22 | -9.55129 | -47.89732 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a742d418-7ed5-3894-9c50-2b18fd83427c | -5.70011 | -43.16039 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e4b645a6-e075-3010-9a04-f2508d839a3e | -11.13296 | -51.08982 | 2025-10-30 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bbc7fbd4-92fe-35df-805f-8915193c1889 | -7.08132 | -44.94177 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6dca67e4-74a4-37fc-b869-c05a6ab5f1b3 | -9.71345 | -47.75593 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44b96b6c-da28-3105-8f46-e327acff0a27 | -5.20133 | -46.19003 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1b27018-d36c-31fd-9c01-a138b558ff38 | -9.94023 | -47.18578 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0f2fd91-c8ef-33eb-8c23-7cb1a027dd9b | -10.86423 | -47.61488 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c40c620-cd82-3780-b4a5-ad4e9799d119 | -5.64106 | -41.09061 | 2025-10-30 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e969e149-98ca-33dc-a87f-02aafb3614d3 | -7.37912 | -47.62687 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0b01fb1-4a43-3f99-9f56-db2de443a97b | -11.94539 | -43.86022 | 2025-10-30 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba39bfff-58a5-332b-afb6-606f663d90cd | -10.93406 | -47.7959 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb4d8b59-03ed-3130-9ef3-bc7e4f53c144 | -5.19759 | -45.61113 | 2025-10-30 04:25:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README54.md)
