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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22795b74-c83f-3656-b2dd-bfa7f25352c1 | -9.09612 | -40.47515 | 2025-05-03 03:10:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4917e02b-e500-3ee9-8360-5b4e4b0647b3 | -8.42563 | -35.65212 | 2025-05-03 03:10:00 | NOAA-21 | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a677f7ab-1d68-37da-86cd-8ffb5c72155f | -6.6865 | -42.1252 | 2025-05-03 03:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 21d6e595-baf0-3cb8-80ca-b84576ae7e0f | -6.7053 | -42.1234 | 2025-05-03 03:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| b16f4d31-9e57-3536-afe1-6cd92b0a7cd8 | -6.7053 | -42.1234 | 2025-05-03 03:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| c4ca3e7f-dd52-3846-bbf1-ca2a08da3979 | -4.6109 | -38.68396 | 2025-05-03 03:36:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e054724b-5bc4-3c7c-9542-12f76344a3b5 | -5.16578 | -45.10757 | 2025-05-03 03:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4147abe4-2dcd-337b-a5a9-0392d56e4a19 | -7.47676 | -34.8421 | 2025-05-03 03:36:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 77cb8af0-419e-323f-a0aa-a040e5491d57 | -7.31247 | -37.42299 | 2025-05-03 03:36:00 | NPP-375D | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 679b8828-abb2-3b73-b61e-f0f06694158a | -6.97174 | -42.79156 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 19496ca3-bbca-3b6a-b3dc-5e8ebae73722 | -6.69459 | -42.13294 | 2025-05-03 03:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 7a2d749a-8979-38a5-9978-db2ff69cded5 | -6.96643 | -42.79065 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 20ebaf6c-1572-3b09-aac7-214c198a36cc | -6.9695 | -42.79235 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2a91a3e4-7477-3ed5-847f-6b59d5d3e5ae | -7.6765 | -42.98678 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| dd9aff30-fe52-3955-bb11-93fa07d123e4 | -6.70073 | -42.12794 | 2025-05-03 03:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| e773081a-8988-3075-b336-a2973255e351 | -9.87558 | -37.15768 | 2025-05-03 03:38:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 951643dc-35da-36d3-9f10-549eafeb8230 | -7.68712 | -42.98859 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 47289427-5fa3-3b29-bf41-59dbb9774a2e | -7.68886 | -42.98862 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7530a4a6-61b1-3a2a-9e10-273a18f7efa1 | -6.9636 | -42.79468 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 02d936e6-d5a9-3983-9397-dcb357308d24 | -9.09403 | -40.48101 | 2025-05-03 03:38:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ca63d222-e5dd-378d-ade3-8b615a5e8580 | -6.95889 | -42.79053 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ff4b6ff8-c539-3914-8bae-71bc8a92ad05 | -7.67763 | -42.99019 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| f189ecd1-ba6c-30e2-a253-f6a4b84c143c | -6.95829 | -42.80599 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4832c01c-136a-39a8-bcf9-05a2f099871c | -9.77385 | -37.21944 | 2025-05-03 03:38:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0df922d5-4ae5-3eee-88a2-2b1cbb458b38 | -6.96587 | -42.79388 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d742d38c-47ea-37a8-9e99-d97dde07d791 | -7.68243 | -42.98432 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| a1b23128-a58a-3200-b37a-f657b1a4bbe2 | -6.96474 | -42.80035 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 457761f1-3962-3d9f-84cf-d45ed120e6a0 | -6.96531 | -42.79711 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f75e26e8-f9a7-3455-8e98-31ea2d451137 | -6.96184 | -42.8044 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a6db4625-1a89-3a5c-968e-7501bafc6901 | -7.68944 | -42.98527 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 40309580-80ad-30ea-a399-384a0193fcab | -6.96243 | -42.80114 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 78536905-d32e-3697-92d8-2dafd7c18b77 | -7.68649 | -42.992 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ef0dec77-070f-34a2-a0e8-713f6d4eba2a | -7.68355 | -42.98766 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 0c723485-8ad1-3b7f-9044-986d7f8b68cc | -6.95886 | -42.80272 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f1dbce7-e991-3e77-a47b-417eaaef8491 | -7.67586 | -42.99023 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 9fe3a857-aa98-3ca0-a9b7-3547c506786c | -9.6048 | -37.04371 | 2025-05-03 03:38:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3888797a-9694-3d77-9518-6d96636eca35 | -6.69564 | -42.127 | 2025-05-03 03:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 49b44b8f-6395-3f06-83f6-782997729a4b | -6.9583 | -42.79377 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cd48c7d0-69a0-3419-8706-b619daaff796 | -6.96302 | -42.7979 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d5722ad0-5aab-3949-8bab-3f3a5bb5ea94 | -6.69968 | -42.13389 | 2025-05-03 03:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 1df0bfc6-e2a1-322f-acc2-a30c1706800c | -13.69768 | -45.20499 | 2025-05-03 03:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 001d2a33-e541-31f2-8d04-092d11a2d705 | -6.69512 | -42.12996 | 2025-05-03 03:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 53946d9d-094d-36bb-9eec-750c2fcf41f4 | -6.95943 | -42.79946 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0d41e5f8-ef0e-3eb7-a724-ea3288dd55f1 | -9.61034 | -37.03231 | 2025-05-03 03:38:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 15200183-d6b4-3942-970c-dc240a52e739 | -13.69908 | -45.19796 | 2025-05-03 03:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a727f679-9c46-3aa1-969c-7c563bc8c35a | -7.68118 | -42.99112 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| f7b8b49f-30c8-3585-9407-fea707f52d5b | -6.95469 | -42.79528 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74e7ddc3-c390-328f-b61e-6284436f3fb2 | -13.69217 | -45.20392 | 2025-05-03 03:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f63d04c8-b440-34db-8b68-a4e2aa4864c8 | -13.69147 | -45.20747 | 2025-05-03 03:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcb770e5-02aa-3f16-99e8-b504a8d0df7c | -7.67825 | -42.98672 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 8884ac21-6341-31fc-974a-a3baf72ef09f | -7.68773 | -42.98525 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6e7dc0cc-9b20-3093-a37f-39caa50d8ac3 | -10.69501 | -37.04753 | 2025-05-03 03:38:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fca2a9a3-0aa6-37eb-bc5c-cc5e32d68cdc | -9.09413 | -40.479 | 2025-05-03 03:38:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 70cdbec2-1e67-3f91-b5d9-b84b392d3953 | -6.95527 | -42.79201 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cd2ed6a6-8547-3da3-b0dc-fe4b50ae338a | -7.68295 | -42.9911 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 2d7d1c0e-625f-341d-a2b4-4cee16cb73eb | -9.60547 | -37.0397 | 2025-05-03 03:38:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0d5c2450-9da6-3bec-8a24-debb7353859a | -6.97008 | -42.78913 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a379e2c9-6bc4-31d0-9a1b-d0fb23d202e5 | -9.09475 | -40.47679 | 2025-05-03 03:38:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0f4d30d3-b438-3c73-99b1-1e935206a6ef | -6.96418 | -42.8036 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 66a933e1-8f25-38ce-b063-3e0e89ff5c32 | -7.68414 | -42.98431 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 91e26521-334c-3d4d-9a51-ca402bff8bef | -7.68181 | -42.98767 | 2025-05-03 03:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 44a229aa-bbc9-3ffb-b534-50663a91fece | -9.08966 | -40.48024 | 2025-05-03 03:38:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 40f5f0bb-317f-3d82-9204-797a109e6550 | -13.69838 | -45.20148 | 2025-05-03 03:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 588e0561-cfd7-3658-80ca-bb2b82a38779 | -6.7002 | -42.13091 | 2025-05-03 03:38:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 000ffc83-2025-3e85-b28f-c4cb136325b7 | -6.95652 | -42.80354 | 2025-05-03 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 12e587b6-ab4e-3694-87ca-ab089dc2513e | -6.7053 | -42.1234 | 2025-05-03 03:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 2c8179fb-1321-3fb1-9452-00f768f474a3 | -16.68066 | -43.88255 | 2025-05-03 03:40:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14811e5c-7975-36a2-8c36-5df15eef927b | -17.6228 | -50.91425 | 2025-05-03 03:40:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69f7531f-48ff-3dda-a861-7e135b2ffd8e | -17.86637 | -44.56765 | 2025-05-03 03:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78524907-c1db-3a9e-bd95-38d5403c6c00 | -16.67904 | -43.88362 | 2025-05-03 03:40:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 859100d2-471a-3548-a59e-a30c0c609bc6 | -17.62103 | -50.92174 | 2025-05-03 03:40:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5db4efe3-49a6-36d2-b96b-5a912b4d4bbc | -19.95581 | -49.82661 | 2025-05-03 03:40:00 | NPP-375D | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e0c4e541-4c56-338f-bf63-5ff238f8da7e | -17.8672 | -44.56836 | 2025-05-03 03:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36be5eb6-f23e-339e-a4e0-80ace8a13e1b | -20.41807 | -43.55418 | 2025-05-03 03:40:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 54b3db77-3bf8-3a53-a436-6f4bdcca2ec2 | -17.62444 | -50.91805 | 2025-05-03 03:40:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd8c13d8-d8b8-3e22-92f2-bd121611057b | -23.98289 | -48.91714 | 2025-05-03 03:42:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53b5f487-6d8d-328c-84c8-4b00bd7349ac | -23.98398 | -48.91991 | 2025-05-03 03:42:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 044364ba-de2f-3f9e-a595-4642fba7191f | -21.13996 | -48.61812 | 2025-05-03 03:42:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a94224ec-53ce-33de-8365-d65a2d10bb7e | -22.78734 | -43.75863 | 2025-05-03 03:42:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 093c2ac1-f0b1-3f05-9f78-1a13f9c3fada | -21.14783 | -48.61086 | 2025-05-03 03:42:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 22092fa5-8d08-3cb1-8296-8d1f8c0fc715 | -21.13891 | -48.62263 | 2025-05-03 03:42:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ce4e60df-06de-305c-8228-e31489626378 | -21.98451 | -46.82473 | 2025-05-03 03:42:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59a4e36c-257a-3f2c-9ee3-6b297a134387 | -21.98525 | -46.82133 | 2025-05-03 03:42:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c1f1d12-be71-3e14-b6b1-7c0d0a9b9472 | -21.63214 | -48.34213 | 2025-05-03 03:42:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fb2a9fa-2eb7-3878-8a5e-f5b3e7461ae0 | -6.7053 | -42.1234 | 2025-05-03 03:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| 9bf26311-6a0d-3014-9854-0e052f380bf2 | -6.69406 | -42.13158 | 2025-05-03 03:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 247666f5-7d1b-31e0-897e-2a1bd7d026fd | -2.65061 | -48.80031 | 2025-05-03 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9550904-692b-3f5e-8735-8a47cf598922 | -5.89495 | -39.42686 | 2025-05-03 03:57:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 157b0f08-39ba-36ac-b298-54871d503124 | -4.54785 | -38.48888 | 2025-05-03 03:57:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 210fb128-c399-3484-9c73-266db8c4d561 | -2.65122 | -48.79665 | 2025-05-03 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69ef2ffc-88c5-3ab9-a493-685d68a14f13 | -5.6397 | -39.53868 | 2025-05-03 03:57:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7fa2162f-6920-3fcb-bfb1-1ef0a8d6e1fe | -7.2444 | -39.17751 | 2025-05-03 03:57:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 71f6a9f6-9a72-38c1-bc4e-60782bf20c90 | -5.12761 | -36.38497 | 2025-05-03 03:57:00 | NOAA-20 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4fa240b3-953a-31fc-a6f5-5bb687d5f4fa | -6.69467 | -42.12779 | 2025-05-03 03:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 36.6 |
| 2508c249-e541-370d-8d45-b69f2e086626 | -5.35218 | -38.72888 | 2025-05-03 03:57:00 | NOAA-20 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 399dc810-2141-3a07-8979-8e2afb722aea | -5.79286 | -43.62003 | 2025-05-03 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff3838c2-743d-3b1c-b3dc-b7d913639a53 | -5.16716 | -45.1069 | 2025-05-03 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5d3ad965-e9cc-3df7-8e9a-a5ac997b92c4 | -6.70158 | -42.12892 | 2025-05-03 03:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 38.8 |
| 4ca164e6-096d-3889-9bd5-4f90f41bd1d9 | -5.7891 | -43.6194 | 2025-05-03 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98bf934d-4ce5-34f3-a740-f68c175db105 | -5.83137 | -39.20356 | 2025-05-03 03:57:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
