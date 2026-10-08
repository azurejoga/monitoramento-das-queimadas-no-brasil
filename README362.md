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

## Dados Diários - Página 362

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61435f49-f6a4-3842-96b3-874360138813 | -2.52174 | -56.61202 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 392dbecd-b595-3fa3-91f3-dda1adcce944 | -4.0547 | -55.32325 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26ffeeb5-8a56-3e94-a115-2bf0df1fdb99 | -1.33216 | -56.4016 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 2d744a0e-bf0c-3ff2-8d3f-441663bb7c9c | -2.58795 | -56.14635 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 13fb7f23-d702-3eed-9333-8248113f8817 | -2.56682 | -56.16674 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 4ebf8a3a-b555-3a86-84a3-b7631868fa65 | -3.58203 | -59.52554 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 79149f51-e8c0-3da3-a478-310aafd928e5 | -6.05135 | -53.48495 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5bcd86e4-b5e3-3198-9843-af1948d5b7f6 | -5.98886 | -55.3601 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8ecc651f-fb92-30aa-83b7-a0356fc14a08 | -2.10488 | -56.62039 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 59fc032d-ecef-3f3a-bbab-4c9b4b14ce26 | -3.13555 | -42.93526 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cf642250-51a9-3c46-9e5a-af4c95fe64ee | -2.85957 | -59.30595 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6a5189ae-a34c-3188-8629-95e62826b03b | -5.67595 | -46.35522 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 08d93003-4f84-3880-8a64-7a8a461edd7d | -2.18308 | -56.30718 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 35edf13c-60a6-39c8-a82c-f98bd3c70248 | -2.97801 | -54.04016 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| b873e300-7018-3319-85ff-b85c1bbc8544 | -3.73765 | -55.39077 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 638e2942-46fc-3beb-8489-45e1f1c09463 | -5.30353 | -45.718 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d5b280b7-a643-322c-bd96-6f48eabbe7eb | -3.50225 | -59.26034 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 031d7d63-1eff-3cf6-90c0-5497489b31d4 | -5.59285 | -47.2652 | 2026-10-08 16:39:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9ab13a1e-bc13-30f2-a20b-4722c355b219 | -2.75915 | -54.11392 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d017d03d-d67c-34c3-854f-9d45a4fda7b6 | -6.19217 | -52.87334 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 56924416-31e2-364f-a4b7-706ac6b51a92 | -5.93243 | -44.27573 | 2026-10-08 16:39:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64a2c7e0-66d4-3119-b459-f959ee8e08d3 | -6.40777 | -51.94561 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d29e95c9-db48-39a4-8f94-4770243962c6 | -3.29525 | -54.002 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f5564172-5b6d-3cea-8c08-262f123ddfc4 | -5.23733 | -40.57785 | 2026-10-08 16:39:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 51a20692-f859-346f-a735-9b15b2b6ec6e | -6.2688 | -52.88678 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| aa4f3eed-cff1-3005-98ff-fc6de258ee91 | -5.16789 | -42.89133 | 2026-10-08 16:39:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a434e790-0952-3a2c-8f13-f9f56691ed1b | -5.919 | -49.93714 | 2026-10-08 16:39:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8ed576aa-92c6-3bb0-a2d3-4b8ba3681eaa | -4.92871 | -55.85937 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 860f4257-6026-3c27-9620-ce3401dd0849 | -2.7355 | -54.11733 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 206.6 |
| 2aa742fe-69db-330b-a998-fe872dd62376 | -6.4122 | -55.19286 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d8769ed8-03e4-3218-83f8-f78052273d3d | -3.72263 | -57.14157 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c7d70a73-4455-3d28-a720-b95359f87134 | -3.13486 | -42.9308 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ae847cb9-5bbd-371f-a2cf-477d77965082 | -3.0164 | -51.01525 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4a0f13db-b320-3b42-9647-79464c6415d0 | -4.31844 | -41.23536 | 2026-10-08 16:39:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 37.4 |
| 78464b96-c37e-37c8-a635-f55acfe70c9a | -3.74006 | -59.44267 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 67b1c177-0ea5-3cc0-9bdf-34189b89689b | -3.48238 | -59.50829 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0578f45f-dd3a-3105-887c-221a75f1cdcf | -3.52083 | -44.31531 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 17631939-fb72-3fb9-9fe4-df4dea7c5564 | -5.37021 | -44.1977 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 7ddcf281-6793-3224-ae36-17d9a08c88d7 | -7.18443 | -52.61407 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 0e1365a9-4bc8-39b2-a1af-f243797b4506 | -1.53636 | -54.83917 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| de05c098-9159-314f-9e55-ff52310abce3 | -2.46715 | -46.01415 | 2026-10-08 16:39:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac06ba82-baf3-3a41-950a-71b99db8bad5 | -6.22165 | -53.27493 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 19826cb2-01fe-3eb5-82cd-cf3bb7ca9312 | -6.23952 | -52.68357 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c796d0f0-c5b8-32cc-a010-ec3c4d8c1d15 | -5.39791 | -45.91197 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 9b3bb55e-474b-3bfb-8cec-8ffc7f9779c8 | -3.11103 | -41.17027 | 2026-10-08 16:39:00 | NOAA-20 | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d5ce66c6-fd6d-35db-bda2-93baa659078d | -5.70404 | -53.44778 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| fb7d6f73-7b0d-32ea-9eab-65db0a9c8ceb | -2.24414 | -55.05497 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 170a1bcc-aee8-3261-9ae0-6b74f30e3e36 | -2.1407 | -56.70931 | 2026-10-08 16:39:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| d320bb7c-1a43-37c7-8789-688e2791f26e | -3.54291 | -54.63046 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 35c57fb9-2df8-3315-98d1-ed62e0245899 | -6.24785 | -52.67743 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d3766737-6421-3acd-9773-0397d38a5582 | -4.0565 | -44.73994 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 16d41925-f164-3c71-af69-03b37cbd6022 | -2.52573 | -56.6115 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 128f5066-f2cf-362b-934f-22512d5e1452 | -3.12392 | -53.79774 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 4eb3b22a-6666-3365-88c4-34b3e996aee1 | -3.53675 | -59.5005 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ad38f95e-f7ae-3557-a035-ef836e624ec3 | -2.86271 | -60.25533 | 2026-10-08 16:39:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| ce27ffca-236e-30c0-8c0e-df67ddadcbfb | -3.94407 | -56.02038 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 5f476dd5-3133-391a-aa00-0a0dc5066638 | -3.2798 | -50.14226 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0442ce34-51cb-3f44-8234-d50b5b4ee570 | -3.01507 | -54.72841 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| c0a0b300-0350-3ed3-a91a-bd3c881feae2 | -5.67783 | -43.41413 | 2026-10-08 16:39:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 53a6259a-4205-3571-b863-a6093ee6dc72 | -2.99646 | -54.02465 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd3bdec9-d2c5-3742-898a-05675606e667 | -3.01667 | -54.73948 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8aa56fdd-fe0e-3463-87cd-5c38f95da9b1 | 0.38951 | -51.16111 | 2026-10-08 16:39:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4073e4f3-0544-3a34-9c2e-9e46ba98eb0f | -4.79833 | -43.13609 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2754c979-eee1-35df-b1ac-699ab69aa8f6 | -3.65498 | -58.89462 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 370cd485-2ccf-3901-98a7-852498458a79 | -2.8431 | -57.48523 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 6b95ccee-8a5e-3f08-b5fc-3e1dd540af96 | -3.98865 | -59.34944 | 2026-10-08 16:39:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 18e6ee25-694e-3dd7-9a36-5cf96fda9a91 | -1.20086 | -48.92902 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f04db645-c096-3abd-844b-c48492ea806f | 0.38784 | -51.14735 | 2026-10-08 16:39:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8bec254a-421d-37c0-9c15-5f3a8a60255c | -4.36823 | -55.6415 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d156ed93-89ac-371c-acde-6cadf71f5798 | -4.18947 | -40.48043 | 2026-10-08 16:39:00 | NOAA-20 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| c495e5f0-1221-38fb-a6b7-3c4fb139d2a8 | -2.50331 | -56.60336 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| abca2adf-cad5-3337-b3e3-2f3a9bd7ef99 | -0.59411 | -49.43145 | 2026-10-08 16:39:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 34e96d90-266f-3f6d-a90f-f58f1d9167ca | -4.77384 | -42.67628 | 2026-10-08 16:39:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 32.0 |
| ae390d6b-0391-3eda-91dc-eadfad3de867 | -3.04968 | -53.96074 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1d6e5676-d8bf-36cd-8a98-393f0f838211 | -7.31371 | -55.00997 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e420f018-0f34-3ac1-8c45-859439c34c26 | -2.77748 | -54.07522 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 78a83b3c-dfa3-3a9e-adf6-9815c4d6800e | -5.39685 | -45.90506 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| b070fae8-497a-3128-bc04-1a63fe67d649 | -3.58587 | -54.6817 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3277c45c-1347-32fd-b2c6-7012331a99a3 | -4.79472 | -43.13664 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b353abbf-5741-364c-ae11-eb8ef706320b | -3.89364 | -59.43864 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6cd4ac31-7862-3ae5-87f5-fc7f3ddd910b | -3.77431 | -58.52001 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0a3d8b3d-15da-3667-b8eb-9a886b359339 | -5.2765 | -47.91309 | 2026-10-08 16:39:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fefda542-73fa-32b9-807b-02fa9a81deaf | -4.57605 | -55.99409 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 821757a5-8220-30a6-86b0-807465561804 | -6.67325 | -55.09748 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 22b2512f-a9f2-3f11-863e-1d5bf95a6485 | -5.88275 | -45.97637 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 587120c6-743d-3ab5-b0da-fef1fda340de | -6.07342 | -53.60331 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 01a4178a-1139-30e3-a568-08040d2814fd | -3.07996 | -58.02849 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 79a64584-2a00-3ff5-8566-5b167f8646bb | -2.48984 | -56.17101 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 03b8862a-1112-3de9-a25f-1ae4a5be27e6 | -3.89548 | -59.43859 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a2080c8b-e85c-3a94-92e2-8ba3cf2454f0 | -3.90222 | -59.4499 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6982c97d-8fbe-37af-bd28-ed897a39521f | -3.45505 | -58.06603 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e94f5860-9ae7-39a5-9536-5f0b2a47e778 | -1.70118 | -50.38295 | 2026-10-08 16:39:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 12c8c4c0-27aa-3d1c-b8a2-c110ea2efe73 | -1.43471 | -55.25584 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 45d5ef41-4082-361d-9260-15b7d3b6e848 | -1.29472 | -55.71127 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0eb37901-3118-3093-a4f4-0273589fcabb | -6.21243 | -52.78534 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f8f3953a-b9d6-3078-b32b-c8a59b6b0804 | -2.97853 | -54.07594 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a01d5f49-6b03-372e-8ee0-e1ef39d611ff | -3.61097 | -60.32468 | 2026-10-08 16:39:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 76b4971c-0e8c-3c36-95d2-b0a9ce8b7dd6 | -2.39548 | -57.22968 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| da20649c-5250-384b-ba18-900cbfa67c1b | -3.58029 | -57.59119 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8bcfbf64-6248-3c0b-bfa6-e6c11a2e1037 | -5.67542 | -46.35176 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |


[Clique aqui para ver as próximas entradas](README363.md)
