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
| ce7c1d4d-a82c-348c-ad71-c266b3bacc04 | -6.87942 | -43.68373 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2e07ecb-2f8f-3ee7-a6c0-7006faffdf56 | -5.07008 | -45.58484 | 2026-10-07 04:19:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 701892b0-f097-34dc-ade3-3a0d5f140590 | -7.19501 | -46.52531 | 2026-10-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05f900f2-b30e-3c84-ad20-a8fec01c2222 | -2.80623 | -52.0866 | 2026-10-07 04:19:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6fdcd47-d9ae-3fe5-9000-198f634c759b | -7.99287 | -45.4971 | 2026-10-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c43a0e2c-5495-3b66-84a6-66d4941b5866 | -2.78311 | -51.68329 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 56b448d8-ecf0-32a1-80ac-e54f188055fe | -3.00114 | -51.11887 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b28cdbf-e536-31b2-99e0-8b7130fdd70c | -3.04871 | -54.22355 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49fade14-9007-3f80-804a-fdd5cc43b5bc | -6.92188 | -43.67274 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e50b42a-9b67-3e5c-b543-fa5f399bc95f | -6.93843 | -43.67537 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 230d8f3f-d730-3442-aee1-0245893b6f5b | -3.35904 | -50.474 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 179482d0-2100-3bc9-a45a-59bf7a5a0c37 | -2.97354 | -54.13426 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44190f43-2d89-3add-b415-a1c88e719340 | -4.13229 | -54.91434 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b2647efe-09fe-313c-b3d1-f1ca0ffe7789 | -3.19163 | -50.55861 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 413ccced-2e4a-3d49-b18d-71437e91fd94 | -2.77481 | -54.08371 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e63937fe-0b2c-3724-bce9-ee94d5f407c1 | -3.99099 | -56.2715 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d5fee5f9-53a5-3a67-a75b-6531b887b8c0 | -3.8567 | -55.9572 | 2026-10-07 04:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 2f290c32-be0f-33e5-acce-dc9387063810 | -2.7612 | -54.1142 | 2026-10-07 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 30bd86bb-1438-3713-9e66-f5167509aa42 | -3.5127 | -54.6362 | 2026-10-07 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 590fd110-7c53-3c57-bf67-343ffe6badf6 | -3.1787 | -50.5597 | 2026-10-07 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 88251d5b-7ef9-3bcb-95d6-0b3a035f66e5 | -3.658 | -60.6222 | 2026-10-07 04:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 704a326f-3c01-36e2-bed8-0c5ef117379f | -15.2511 | -43.2743 | 2026-10-07 04:20:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 7d3e38e8-560b-3b85-9ca7-ad921becf23b | -2.7797 | -54.0736 | 2026-10-07 04:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 7d01ca41-bc1c-3374-8707-03ca65108a76 | -2.7613 | -54.074 | 2026-10-07 04:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 2b0b9eb6-7caa-3320-bc14-51cbba264106 | -3.0375 | -53.9066 | 2026-10-07 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| aa00bc84-95a2-3a91-8927-13096f1e9071 | -2.7796 | -54.1138 | 2026-10-07 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4705fc57-e485-379a-9231-662cc74e4c29 | -3.0001 | -54.1086 | 2026-10-07 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 85d6a05f-7792-3982-b06d-9708b833cb43 | -3.0731 | -54.2473 | 2026-10-07 04:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a0b429d4-ed94-3df3-980d-1cdc54ed8482 | -8.7039 | -45.1832 | 2026-10-07 04:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 6b6858b5-e57f-3f17-bcba-fd9ae20868dd | -3.531 | -54.6557 | 2026-10-07 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b0ff8a29-98f0-3df6-997b-b9026fa51a92 | -3.8567 | -55.9769 | 2026-10-07 04:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 10a6d40c-a40e-3784-80ba-bf4c16b9e1d5 | -3.0914 | -54.2669 | 2026-10-07 04:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 2e3f78af-64ca-3efc-b310-36e3ff75cd14 | -3.1115 | -53.7637 | 2026-10-07 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| fcc5c560-f5df-3dd3-baef-f3e755c8034a | -3.0913 | -54.287 | 2026-10-07 04:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 892c7bca-8f7c-37f2-837b-ff007487e833 | -2.7796 | -54.0937 | 2026-10-07 04:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 235.0 |
| 1d475445-db61-3b2b-b3ff-782b3485b33a | -8.7036 | -45.2061 | 2026-10-07 04:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7f7e4e9d-4263-3e9a-905c-8954d36e3e9d | -3.5311 | -54.6357 | 2026-10-07 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 87583496-80ae-3ae5-a5ef-4833b01b9bbf | -8.7228 | -45.1812 | 2026-10-07 04:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| dcc3d35d-0726-35ed-9372-eb9a580c2b03 | 1.7121 | -55.6261 | 2026-10-07 04:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a7e51180-b8bb-3f31-8595-8e3533357a00 | -2.7613 | -54.0941 | 2026-10-07 04:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 221.7 |
| 93fb76d6-6dc1-3a79-b427-8c1f5f361016 | -5.7376 | -45.1533 | 2026-10-07 04:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 4f2525ac-92ea-32c4-a989-9a9d72085c0b | -3.5127 | -54.6562 | 2026-10-07 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 848d9eff-538f-3690-a0f2-6bc17eaf4a49 | -9.1518 | -65.9367 | 2026-10-07 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ef6dfd4c-02ee-36c3-ab8b-0ba480d48ba1 | -15.2517 | -43.2501 | 2026-10-07 04:20:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 144.6 |
| 047766c4-20a3-3bc2-a7cc-2356ff2219f4 | -5.7189 | -45.1547 | 2026-10-07 04:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| b72121b6-c17b-3de6-9759-6783ab908478 | -11.73305 | -43.66053 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e7be30bc-8b2c-393f-9a9a-235fde7e26e7 | -11.78803 | -46.70607 | 2026-10-07 04:21:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 23fb587b-5770-3c48-87de-5a1523302f9b | -11.10961 | -45.72459 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e74ca9a-6dfb-3db6-8f92-372ed85d42cc | -11.72972 | -43.66 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbf1322c-0c62-3364-bac6-ae467111eea2 | -8.71323 | -45.19262 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0333de1d-dd93-397e-a9ec-40eab9dc187d | -10.84827 | -50.66239 | 2026-10-07 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1092589e-f765-3f9a-863b-41bb08e9b33b | -13.29131 | -48.67137 | 2026-10-07 04:21:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01c4e131-ab2b-3e22-a674-ebf27ef102d4 | -8.2822 | -50.26937 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| bcd590f2-4591-3f0a-9d52-3a4403b52931 | -15.72641 | -43.92548 | 2026-10-07 04:21:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e81797a-f0cc-3d16-a499-2204f9bd3870 | -11.72846 | -43.42542 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fa6b7ef-5b5e-3539-9281-01e06e1aaa01 | -15.42042 | -43.70525 | 2026-10-07 04:21:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 8363ca06-408d-3a94-a4b0-ea12c1e73a2b | -9.75595 | -44.7991 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7616175b-42a5-3153-90e7-d3688eadd172 | -10.85314 | -50.6855 | 2026-10-07 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 423a5c18-37bc-34c8-b4ba-72d5a773abbd | -11.73804 | -43.65039 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb9ff245-0257-3fc2-abb8-7ba8c9b16b8a | -9.92372 | -46.79737 | 2026-10-07 04:21:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d0d42a0-3d88-3c48-8440-b429ef92e21e | -9.25597 | -45.64744 | 2026-10-07 04:21:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf4fd761-2991-3630-bf18-ed91246cec37 | -10.37124 | -45.03006 | 2026-10-07 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c110914-9aba-359a-94ea-da6fef003061 | -7.89503 | -49.83835 | 2026-10-07 04:21:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0686e12b-90a8-36a1-b4e5-820e83d15e44 | -11.62601 | -43.67281 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3aae0d48-0947-3430-a613-4ccb07e42278 | -8.53823 | -55.37824 | 2026-10-07 04:21:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 577bab81-aacb-3472-a034-b83fca1dc125 | -11.07429 | -45.64444 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c4d6cb9-55c9-399d-ba7d-be412a060a6e | -9.78424 | -44.79285 | 2026-10-07 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0380912-67fa-3d62-a239-4ba7eb2a9578 | -16.0409 | -39.84816 | 2026-10-07 04:21:00 | NOAA-20 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 320152f7-dd58-3e9b-abc7-1089bae0b1e9 | -16.07629 | -43.7179 | 2026-10-07 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f03150ba-e5d9-375c-9a68-f4c743b9a85d | -8.71382 | -45.18901 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1cfbb4c1-5e1a-3823-8c3a-22ff5df7ec5e | -16.02127 | -45.13316 | 2026-10-07 04:21:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c87237c-9afd-30f0-a4d0-463777293884 | -9.16179 | -45.11028 | 2026-10-07 04:21:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0b9a660-b1a2-3ddb-a72c-d3aea7db2750 | -14.01237 | -41.84858 | 2026-10-07 04:21:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de8ec169-8a23-3a2b-b922-353b386eef41 | -13.50605 | -44.37059 | 2026-10-07 04:21:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d6c043f9-a53a-3532-b3f5-803e64edf7a7 | -8.43709 | -47.01425 | 2026-10-07 04:21:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c354d3b-4194-3953-b38f-9f3cf53be2f5 | -9.95463 | -43.54775 | 2026-10-07 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbaf5fed-9da4-31e4-982b-d2e05b644bda | -15.56282 | -44.52296 | 2026-10-07 04:21:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a939dd9e-49a3-3d49-809a-246e4a2a5565 | -10.85263 | -50.6632 | 2026-10-07 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7ae3b03e-7b89-34cd-876f-2cedfa14382e | -14.24927 | -41.62546 | 2026-10-07 04:21:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 1d67135d-6448-3e60-b4f0-5e77b00efc26 | -11.66696 | -43.62448 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6627255-4006-3a0a-a1d3-fefb251a4348 | -11.57527 | -48.43698 | 2026-10-07 04:21:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad721f65-4497-31f8-830f-22aab67d4be3 | -13.55207 | -44.03437 | 2026-10-07 04:21:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2f2afedb-f241-387f-973c-18015603290e | -11.05515 | -49.57364 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c1287e7-ecac-328a-8123-e097c4108c83 | -11.23312 | -44.87053 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 603eb4af-cfc9-3212-b52f-1cd2f7340ddd | -10.88819 | -46.66914 | 2026-10-07 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fa26da0-181f-3199-8d19-5920d32ab180 | -11.23974 | -44.87161 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7aca4891-9b3d-387f-9249-c37a782e83cd | -11.62436 | -43.66153 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fd9db78-3470-3398-a13d-18af706379a8 | -12.5348 | -47.57998 | 2026-10-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0af42f5-e99a-3ba5-ad2e-5d0a180034dc | -14.24988 | -41.6211 | 2026-10-07 04:21:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f259ee03-9d30-3dc0-893f-d724c18e5455 | -11.82456 | -43.55117 | 2026-10-07 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5960880-67a1-34b6-990b-a6f356d7b241 | -11.0511 | -49.5729 | 2026-10-07 04:21:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33c9d6e7-a33e-3509-a4c4-8684f9bcb639 | -11.32913 | -46.67772 | 2026-10-07 04:21:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1036a644-4453-3dda-8a75-34fec2180026 | -11.09925 | -45.6819 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4bfe2cc-f35e-314d-8308-01a98cd3bc35 | -11.00588 | -45.43745 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 63f5d2c7-5be9-3f8d-9639-6dd93f7a8456 | -8.69901 | -45.21624 | 2026-10-07 04:21:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92d8d334-e3a3-3813-bb1e-0238d671d2ae | -11.0114 | -45.44576 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b4bc041-e3a8-3fa0-9b82-408d08927553 | -16.41093 | -43.72644 | 2026-10-07 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 678d5b74-93ec-3231-8f43-626c80e16f25 | -10.14376 | -36.25275 | 2026-10-07 04:21:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 6ba14945-c9d4-3b9b-9754-39a92b5854e4 | -11.22621 | -45.27186 | 2026-10-07 04:21:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1037694-dff2-38cb-b06d-09a5883a09bc | -8.49941 | -50.13382 | 2026-10-07 04:21:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README58.md)
