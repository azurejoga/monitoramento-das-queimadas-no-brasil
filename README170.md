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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2930f1bc-ba69-36ab-9743-252b1d5a077b | -3.03863 | -53.93998 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a853f2c-ec59-385c-87f1-a0ea86893bac | -2.99126 | -54.05679 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df1df739-46c3-3d37-8e9e-ce304d5fd138 | -12.09546 | -57.15909 | 2026-10-08 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cff8238e-2e18-395b-a0ac-2b5c10dc0d0d | -3.84933 | -55.98038 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5be6231-5ee6-3395-8d4e-2e6efc38ae5f | -3.56836 | -54.65992 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6679be83-ff75-3d5a-83b8-c8077a2e1b85 | -3.27785 | -54.04717 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4162b79-5592-3211-97f6-13398a5fcc51 | -3.05444 | -53.95451 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 555360a3-b922-3fb9-9709-1c97a1acc256 | -5.04506 | -49.76921 | 2026-10-08 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dc7d2b3-04f1-3637-8afd-7df0e64d7801 | -3.00048 | -54.06997 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| a32d7bd8-74e0-3b29-8f6c-ea72a75a68e5 | -3.57195 | -59.46011 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69ebbfab-565a-3f3a-8618-95978598edb2 | -11.30604 | -44.82653 | 2026-10-08 05:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a575ad25-6b83-319c-95bc-cb93134e52bc | -3.02815 | -53.91418 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26cb8b16-5596-3a1b-bac4-7296a3f65e51 | -11.66391 | -56.76678 | 2026-10-08 05:23:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79c4b91f-d121-32fc-adcd-0c7b46b78101 | -3.38354 | -51.66347 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f1e16cc-f4da-365b-98cc-14a3b731eec0 | -2.10368 | -52.06509 | 2026-10-08 05:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bafa5ac-c09e-3926-974c-c0919bc17daf | -3.26256 | -54.05268 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad5a25f6-da81-311b-9947-2513ebc29622 | -10.62264 | -60.48695 | 2026-10-08 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ffba33ad-eb6d-3a8e-ad81-6925ee2c033d | -2.27797 | -58.44247 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d77746f7-de4a-3067-9c17-e305b35d5568 | -3.51759 | -54.65262 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca051802-df29-3cc3-b149-36b12b5b372e | -4.41561 | -55.75505 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b2d3f47-83a9-343b-b25a-33052ccfabf0 | -2.97095 | -54.11695 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd44a5ca-332f-39cb-822a-1c26e0a29f20 | 0.87399 | -59.81122 | 2026-10-08 05:23:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8148bee1-22ec-3462-b629-b43b7e44390c | -4.61989 | -56.1725 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 739d7d49-9616-352c-a937-7f0482d810bc | -4.77982 | -55.74622 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92744749-28b7-3280-a349-8db1daeac654 | -2.50187 | -56.13539 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad96d329-8977-3209-b7e3-8f8dd5a40490 | -1.53636 | -54.55601 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 0ce2dbc8-878e-34c0-a9d3-c6dc0a6d5395 | -3.28183 | -54.06774 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78651c1e-a7bc-30ad-89d6-1c7657e4cfa9 | -3.28107 | -54.00354 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f1b35ea-d7dc-3b4e-a208-fb37044549b5 | -3.8927 | -55.87962 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37d2f969-5a1e-30eb-a07b-d7bdc2ace08a | -3.84041 | -55.97184 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa755f14-7731-3d64-9927-af47ba2bd35a | -2.89225 | -59.20603 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 534beb92-f06c-3b49-9970-4b95ba96a20b | -4.12662 | -54.03312 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f778dea0-bfc9-393d-b1fa-7887f7943e73 | -5.7426 | -53.45461 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6c33e6d-9d4b-3c71-8ac1-b43d4814675d | -3.16834 | -54.74413 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c14c8d4e-fde1-3cee-bcb6-7122af81ccd9 | -3.02412 | -53.89336 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35ba1d73-bd10-36dd-9966-056abb034bc3 | -2.54906 | -57.39548 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2670a6d5-e2a2-38a0-b45b-2f9c8f5fefd5 | -3.02724 | -54.10583 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df6c903d-5369-35f3-b0fd-ceea3148ada4 | -4.31266 | -50.78215 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d46ddf2-166a-3916-aa90-5d33fd5493ad | -3.17637 | -50.44852 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0ef164e9-efc6-306d-bcfb-4669998fcad1 | -3.83596 | -55.97829 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a29628bd-e485-3746-bcd5-80eeab5e89a2 | -2.57018 | -56.14946 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 319d75e3-47b2-3559-bea0-c4291f39b85b | -2.46902 | -56.06291 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 845b1be9-1965-3cc9-be6b-4dd2a51c04a8 | -10.12897 | -55.65352 | 2026-10-08 05:23:00 | NPP-375D | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 276e6af9-df52-310f-952f-8efd1857e8fc | -3.07914 | -54.28197 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3d40e2e2-ce48-3923-a54d-fcc27a3b7e73 | -2.95213 | -59.1655 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1678d83-7921-3127-982b-d7d56289010c | -3.28497 | -53.86246 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cf7df63-18d9-399c-97f8-4ee5671f9742 | -3.09345 | -53.93641 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 391a88e7-6632-3901-8a89-1c226511126c | -3.11611 | -53.76933 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7afcde6a-18be-3415-97fa-2c985055fc39 | -3.26959 | -54.05386 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9618b54b-360c-3418-b953-60d28ded65a3 | -3.13679 | -54.36873 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b42495b8-f97b-3689-8ee3-f4aa64b11bc1 | -11.7581 | -61.0586 | 2026-10-08 05:23:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 039fb90f-671a-3794-9ec5-1411f4c51a99 | -3.28994 | -54.08495 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4915adc-e901-3813-af2d-bf7a82fa7ca7 | -2.58184 | -56.16192 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5630075f-8dc5-3d2a-964e-ff0b9dce39ba | -3.5787 | -54.66154 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53c20cd2-ddb6-3800-9b67-6c8cbc60a2f1 | -2.79082 | -54.07434 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b87ba0bc-46f7-3d90-a5b7-420ce60afe9e | -2.48469 | -56.13624 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1931804c-4f0a-371a-a344-56bbbc0b2d11 | -3.06959 | -54.24627 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ead772b-1519-39fe-87cd-d51840549e3a | -3.19453 | -50.56112 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7194955c-bbdc-3dc9-9a5f-c157e8d1a073 | -2.84281 | -57.48085 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5a205622-7da7-38ed-a75e-bdd625129071 | -3.26897 | -54.05777 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f164c22b-c116-3dac-a6f2-77f7029afeb5 | -3.29793 | -53.87261 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1f6a0e5-f893-3a5e-b527-e77f0a2b9f34 | -3.0521 | -54.1532 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3183482f-3272-31d3-9232-3390dedd849f | -7.28042 | -46.80759 | 2026-10-08 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9055d7d-3191-3cc9-be1e-0856c8517245 | -3.51894 | -54.59912 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ce80c3c-e60f-3422-9c3c-f35c7be4df37 | -2.77364 | -54.06466 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 071a9427-ea63-367c-afc5-a00b2cfec268 | -2.98876 | -54.07608 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| bd9e6a71-b6a2-3f8f-a651-1ba4501decd3 | -8.59997 | -47.15094 | 2026-10-08 05:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b12ca84a-bd9c-3faf-a3fb-37abee85bf78 | -5.24308 | -50.91308 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5930e243-710f-3c2c-b273-2aa6a2eedc15 | -2.77212 | -54.07936 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9873271-6d46-3720-a864-440baa8a5564 | -5.04581 | -49.76428 | 2026-10-08 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6403662-580a-388a-9734-0f8071aa62cf | -3.51019 | -54.63231 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e04daf9-dbd7-3185-a6c2-f28937c8ff00 | -1.11306 | -54.12364 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f391700a-5b59-3b98-86ed-23809785a48a | -2.10432 | -52.06704 | 2026-10-08 05:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cea0dc99-30cc-3233-b9b0-9ba23beffcf6 | -2.50414 | -56.16408 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 805399be-25a2-3d38-acd3-ecde9c4b9c4a | -3.29362 | -54.0616 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6157105-997a-35c5-921f-4b72cae3cecc | -3.17786 | -50.55439 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20bdbfc8-76f2-3fea-af0d-f0d6cc1060bb | -3.27662 | -54.05499 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5915936e-81bd-3cf1-bdd4-6d130f6bf981 | -3.70977 | -54.23421 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 441bade2-1337-314d-868c-08b03276b9e1 | -2.94413 | -54.105 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d54317b-28c9-3dcf-a7f1-ad0ab819b9bb | -3.2702 | -54.04996 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5702e425-ec99-3264-bf44-e4c25aedb865 | -8.62585 | -67.02849 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 80aae17c-d93b-33f0-a5d1-e57569428940 | -3.17158 | -50.59507 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 56134745-efc9-3eb8-869d-4aedcb752106 | -3.01632 | -54.06051 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ae3305d-524d-3e50-9798-353554596a5d | -2.83198 | -54.132 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a66b2731-4742-3557-842a-15db8fde5eab | -6.92618 | -43.67066 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b823dfaf-4ffd-37e1-91b9-f974d9ecb9ca | -3.83317 | -55.97428 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36c4a1f6-4969-3802-8846-74e243c7d5ef | -12.20481 | -57.12665 | 2026-10-08 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 796bab97-0af1-3f23-8735-c8cd327a1d2d | -3.12145 | -54.1707 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| d8af183a-bdd1-3a4b-ac38-9b3d66800bcc | -3.5925 | -54.66362 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 814b8c08-b749-38fc-a3d0-467c7bb9da6a | -2.99795 | -54.75943 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e29587c7-c426-3933-8995-1dd815d10297 | -3.64814 | -54.28393 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ed21ac5-a1a4-3126-a1e3-da39a73d182a | -12.41187 | -54.36261 | 2026-10-08 05:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a61c2ac-52ab-3069-b44a-e1f10a8cd1dc | -7.60156 | -46.75935 | 2026-10-08 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a20fb246-113d-3ab7-884d-852391a50347 | -2.9904 | -54.112 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1ca57c0e-6e60-3f34-9db9-94bb8d4b82b7 | -3.54478 | -54.67542 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 98f41dbf-a1d5-39ef-ad6b-ad1c37066d83 | -3.01031 | -54.09925 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| f881c586-8237-36cb-bedc-8dfa7f937bd2 | -2.79663 | -54.08315 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f60c793-eaea-3d1c-8623-7455da44ff52 | -3.11298 | -53.78926 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fa57d0e9-edfa-3069-b530-5a01363b2e46 | -3.61809 | -55.27757 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b0824c6-8623-34c9-b410-9279502cac3d | -8.73081 | -45.15416 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README171.md)
