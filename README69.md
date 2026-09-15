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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be0da21c-ee7d-3eab-ac01-d475e1bd7596 | -8.08607 | -61.79925 | 2026-09-15 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db0a94ea-1f59-38ee-b8b4-a89649e401ee | -7.55605 | -62.33101 | 2026-09-15 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90c0c1a9-b720-36fd-92dd-0261aabf6b8a | -9.85226 | -65.18371 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b34e8d66-a046-3c11-a47c-03aee7f53a39 | -9.64373 | -63.50724 | 2026-09-15 06:14:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dce1c4c-449e-3303-9126-da07e21aa84b | -9.40812 | -62.7111 | 2026-09-15 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 86c40762-7021-30b4-894b-d6567d2fddcf | -9.1288 | -65.84071 | 2026-09-15 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48ac0a90-3ecb-3d73-97c9-a020d549330c | -9.5363 | -62.37329 | 2026-09-15 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 977d18c8-9e03-36c9-abb6-d544721c3821 | -9.01794 | -61.01421 | 2026-09-15 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f16dbf05-ab6c-35b6-b74d-0dc26d0df88c | -6.02449 | -59.93278 | 2026-09-15 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1bd3d518-7b59-3842-97be-dda83b211416 | -3.7346 | -61.74449 | 2026-09-15 06:14:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8d622891-1211-3771-98b7-cca094cce838 | -9.84752 | -65.183 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b25ab0de-3805-3e85-8f42-a76a8a6d3600 | -6.10397 | -59.88789 | 2026-09-15 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d087ee5c-5bbf-3442-adc9-904467b899a7 | -9.03741 | -60.52632 | 2026-09-15 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4c7cda3-be82-3327-9791-62a2545d3e2e | -9.12371 | -65.84449 | 2026-09-15 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b0f5535-e4cd-3887-8a2f-d41ed724217e | -9.542 | -62.37414 | 2026-09-15 06:14:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7d407b6-3b72-3c65-88ad-ac7bb146f285 | -9.41321 | -62.71549 | 2026-09-15 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| daaf6dce-6b73-3edb-8864-43150cc1c4dc | -9.01177 | -61.01327 | 2026-09-15 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afd8e1ec-6059-3df0-ab5d-4a7bd3551ff2 | -9.03806 | -60.5212 | 2026-09-15 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd74ee04-f927-339a-b715-6bcad3c6a6c1 | -9.1339 | -65.83689 | 2026-09-15 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a4639c2-4172-3414-bd25-db1fd30dc4da | -7.55556 | -62.32739 | 2026-09-15 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dff349ac-0fa4-3fd7-b295-a801e83e57c5 | -9.53099 | -63.62731 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 964f4b94-8505-3d97-93a9-58d219cc20eb | -7.56114 | -62.32818 | 2026-09-15 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0be661c5-bf5c-3d87-9740-8efd7fb6d73a | -9.52569 | -63.62775 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03882f81-8004-3c6c-a7aa-04654f86ea04 | -9.4091 | -62.70372 | 2026-09-15 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ec3d9e21-5da5-3aa8-a841-797d828c9275 | -5.45926 | -60.2245 | 2026-09-15 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bcd9232-3ce6-3a40-a563-50fb05cae5e4 | -9.67654 | -65.80036 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af04f564-9d50-385b-9081-848242c9496b | -9.85166 | -65.18184 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eff74978-7e12-3f8e-803a-a5e5cadbf83c | -9.53095 | -63.62844 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eff37e0b-d441-3f1a-8845-db31e8b5b782 | -9.12941 | -65.83624 | 2026-09-15 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9077e215-ea0b-32ba-a034-2dca98815edf | -6.13087 | -59.88156 | 2026-09-15 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9905337-70ba-3f20-8dc5-9292a490ce1d | -9.20504 | -65.62277 | 2026-09-15 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20da5774-17d0-32cc-8dd8-b7b5a90b601f | -6.01743 | -59.93697 | 2026-09-15 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 91257acc-d2d2-32c0-b53e-ddc0c1e803f0 | -9.71176 | -64.92149 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63f0015b-2699-33a0-aa45-c997f424c13b | -9.13452 | -65.8324 | 2026-09-15 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d0f1635-4f3c-3d10-830f-9aa8d04af752 | -8.08552 | -61.80346 | 2026-09-15 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74fd25b1-39ad-3932-aac5-a4d9ec5cbd5c | -8.78022 | -66.67804 | 2026-09-15 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dae51a41-1676-3160-9e83-a2fcca7126b5 | -9.41418 | -62.70819 | 2026-09-15 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 7c4515d1-156a-374a-bac8-083cc1c09cea | -8.77992 | -66.67895 | 2026-09-15 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee805de0-0b11-3b7b-8725-cdd224e83fdb | -6.11031 | -59.88913 | 2026-09-15 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39d1b585-82cc-3891-bb51-5e6f980cd70a | -7.56214 | -62.32809 | 2026-09-15 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aaf5a5b9-62fc-3ae4-8622-609eb7318c47 | -9.40861 | -62.70742 | 2026-09-15 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a9b5adf5-acc2-3289-b7d0-41b7d8a649f6 | -9.68491 | -63.42986 | 2026-09-15 06:14:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 424cd29f-1d04-325b-8f14-d1c8509b9215 | -9.84692 | -65.18115 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2417a7cc-0123-37d4-9af8-771103c849bc | -9.41369 | -62.71188 | 2026-09-15 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2daeb821-6229-3360-938f-db3c03b560fd | -9.12432 | -65.84003 | 2026-09-15 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eaf63bf4-cd30-3279-aa73-b86cd7542d97 | -9.26198 | -59.64133 | 2026-09-15 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6781c91-4ba7-303a-b038-a1a6b10b7be1 | -6.13724 | -59.88257 | 2026-09-15 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1e77b3f-5d29-379b-93a7-c7a68fac54fd | -9.718 | -64.91164 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 090f1ff0-5715-39ed-a591-3bfd412734eb | -9.64223 | -63.50896 | 2026-09-15 06:14:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d65bb9d-c191-3908-9b46-e6b6a33b90c1 | -5.45307 | -60.2236 | 2026-09-15 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfb6a4e3-9ea4-3238-af79-4c045ea9c858 | -9.69023 | -63.43065 | 2026-09-15 06:14:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1000ccff-d776-3b09-9588-cbab4117ffe6 | -9.52573 | -63.62663 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e8ba2ef-b72d-3a9e-b1a7-958bd38b0486 | -9.12181 | -65.84175 | 2026-09-15 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 053bbae9-0186-30ea-b75e-6d33a196e1b2 | -7.55657 | -62.32732 | 2026-09-15 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f7b8698-09a7-369d-a0a3-911384c34e15 | -6.02377 | -59.93798 | 2026-09-15 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c6519259-e1ca-301a-beeb-5b1f4c05ff8f | -9.67717 | -65.79571 | 2026-09-15 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 946890e7-2b1d-39b7-b50c-c0b9d5f8c831 | -5.45374 | -60.21879 | 2026-09-15 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f1fe050-fd7d-3a07-93c8-be61a4784994 | -18.1714 | -51.7466 | 2026-09-15 06:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e49dc96c-22cc-357e-b2b6-9d075ec4466e | -6.95015 | -44.53846 | 2026-09-15 06:29:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f8d88d45-d651-39a0-8845-7dc03664b781 | -2.90588 | -50.41923 | 2026-09-15 06:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b337866a-3e21-3ec3-90f4-704430ec28f9 | -4.66874 | -42.08743 | 2026-09-15 06:29:00 | AQUA_M-M | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 21b54039-98a6-3ff9-9d0e-1185a0f10c78 | -6.42482 | -43.06735 | 2026-09-15 06:29:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3548c795-658b-3276-b1f4-8781a9787642 | -7.07583 | -42.11559 | 2026-09-15 06:29:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 973fedce-1084-3b4a-b03b-278b2596ddae | -2.90124 | -50.41359 | 2026-09-15 06:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d6480952-1647-3e6e-bc3e-451515cfdd0c | -7.17123 | -43.52052 | 2026-09-15 06:29:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| d03dd94e-8227-3415-a374-537d68509acf | -2.91546 | -50.41578 | 2026-09-15 06:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 90f0d2a7-835e-3493-bd1f-2c4866c35ca9 | -6.43359 | -43.06865 | 2026-09-15 06:29:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 19866a25-59a7-30ab-b0c5-1ff4799b5d0c | -4.67008 | -42.07846 | 2026-09-15 06:29:00 | AQUA_M-M | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| c1d8aee0-c84e-36bb-9573-5be403f7c93a | -2.89166 | -50.41704 | 2026-09-15 06:29:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| cc545110-f13e-32da-8cf2-1802a202626b | -6.95902 | -44.53978 | 2026-09-15 06:29:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0c920650-7ba5-33d0-85d3-4734234fa3bf | -5.55517 | -43.43652 | 2026-09-15 06:29:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 075a05bd-2521-3074-9a7f-72a9342e050a | -6.25754 | -41.96857 | 2026-09-15 06:29:00 | AQUA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7dedba82-765f-3041-bbd4-ebf5adf8abe9 | -7.10409 | -41.80464 | 2026-09-15 06:29:00 | AQUA_M-M | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5c089237-9a5a-3801-b7fb-e9618e597987 | -18.1714 | -51.7466 | 2026-09-15 06:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 5e625a3b-4648-31b8-b1df-3470abb6d31d | -10.75533 | -44.82259 | 2026-09-15 06:31:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bcbfccc2-41ff-3ea7-a1c1-8afc95a0acaf | -14.16389 | -47.40319 | 2026-09-15 06:31:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26f12a2f-2a7e-310f-b396-b56c11a499d8 | -11.49542 | -45.78004 | 2026-09-15 06:31:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c3cdbcb7-eed5-36d8-8c23-985b82025b1f | -14.66228 | -47.99865 | 2026-09-15 06:31:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d125d9f7-e574-3f73-973a-ca46a20b6095 | -14.66053 | -48.00956 | 2026-09-15 06:31:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 73abc439-7e5a-3c43-bc3b-12c1d59be74b | -14.67426 | -48.00739 | 2026-09-15 06:31:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 84338327-bff5-3079-9040-3741c29bdad9 | -14.15635 | -47.39075 | 2026-09-15 06:31:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c5ee7c1d-6e63-3b09-a4a3-7cf55204a23b | -11.88554 | -43.81607 | 2026-09-15 06:31:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 08ac3427-091b-3537-aca1-81273943d071 | -9.35862 | -50.09339 | 2026-09-15 06:31:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| f687ee9b-eddb-3a7e-a2dc-08614084034d | -14.15459 | -47.40168 | 2026-09-15 06:31:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 13f00a6d-a47b-3e41-bbf0-1192a978b2cf | -10.98096 | -48.32123 | 2026-09-15 06:31:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d4e5b5d6-476f-33b6-8c0d-f201c6447272 | -8.79343 | -45.90384 | 2026-09-15 06:31:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f6ac8056-57fb-3638-942a-23f51374df41 | -14.20432 | -47.42629 | 2026-09-15 06:31:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b9ed0ee-e24c-3673-bf56-71ccb14f7404 | -15.58603 | -42.57381 | 2026-09-15 06:31:00 | AQUA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 6f01fea5-31e2-3f1b-baf4-ad0740ca2097 | -15.58755 | -42.56257 | 2026-09-15 06:31:00 | AQUA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| ca98958f-efd7-30ca-967c-20af3ee5cfbd | -12.85495 | -44.38803 | 2026-09-15 06:31:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6f9d7a5d-49a8-30f9-86f8-a3b57f66621e | -13.76015 | -48.80439 | 2026-09-15 06:31:00 | AQUA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 543838c5-a2cc-34b8-ac9d-7bd6d736add3 | -8.57803 | -44.48617 | 2026-09-15 06:31:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6a3058b4-66b3-339e-927c-859167b582a8 | -11.49221 | -45.74168 | 2026-09-15 06:31:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4c9aee60-5f39-347e-bcb7-082063deb333 | -9.35554 | -50.11163 | 2026-09-15 06:31:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 0d12e191-638b-30b6-ba4f-5729d38a5ccd | -9.87927 | -47.76665 | 2026-09-15 06:31:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2cac430a-38f4-3fe7-a06e-7fbb578adfc0 | -9.87736 | -47.77864 | 2026-09-15 06:31:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d2144f1d-4f0b-3942-bbef-32f7fc4108ca | -10.85965 | -46.30152 | 2026-09-15 06:31:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e64d9e3f-25c9-3948-91b4-72c6f58d4a91 | -10.75669 | -44.81369 | 2026-09-15 06:31:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 019bbad2-ed3a-3635-816e-504b8c58daff | -11.88419 | -43.82513 | 2026-09-15 06:31:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 93fc6cf4-f9cb-36a1-a677-932f25227168 | -10.04323 | -45.48156 | 2026-09-15 06:31:00 | AQUA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README70.md)
