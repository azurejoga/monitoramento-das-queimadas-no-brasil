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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f9ec8b7-a3cc-39d5-848e-eb54e2144217 | -2.961 | -48.755501 | 2026-10-09 00:06:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db2b8200-8948-3813-9b13-b295d2e714f8 | -5.854 | -47.4212 | 2026-10-09 00:06:00 | METOP-B | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4bcf4e6-283f-3c72-b2d2-a3a6fd4d4a88 | -3.5606 | -54.650799 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a00bf1e-55e4-392f-a3c8-1217fb9aa6d9 | -1.0993 | -54.159801 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1063950c-dbab-3bd1-93bd-90ca9203ec0e | -5.2849 | -47.9104 | 2026-10-09 00:06:00 | METOP-B | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa4c2109-9e00-3e77-bb1d-0b0ae3a63e07 | -3.2098 | -50.540401 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e067c7-4c8c-33ac-87ab-aee96cc5996f | -4.5426 | -54.9692 | 2026-10-09 00:06:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b85abe6-5b53-3c4e-b930-cfaca703e22a | -1.7779 | -47.134998 | 2026-10-09 00:06:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00e68e68-567d-3f15-81bd-d5be553e639c | -3.0526 | -54.025501 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e05c813-288a-36eb-b684-636941082dcc | -4.1428 | -44.345501 | 2026-10-09 00:06:00 | METOP-B | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9cd91fee-f0e2-38f4-8982-061ae4ccfe28 | -15.7316 | -50.801498 | 2026-10-09 00:06:00 | METOP-B | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e2b0e677-0ca7-388d-9411-83336f071cff | -8.062 | -45.630699 | 2026-10-09 00:06:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 650c657a-8a5b-33dc-b45b-a12aa0c9c1ac | -3.0164 | -54.093601 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14ad2c74-28ed-3683-85dc-5e238a103566 | -7.4834 | -42.832699 | 2026-10-09 00:06:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| af1d75e2-5173-3d53-bbf0-954d59878669 | -8.9635 | -45.158901 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f9b932bd-2455-30b9-8fca-06e2dd4aaf5f | 1.7527 | -55.5508 | 2026-10-09 00:06:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6366746e-fe61-3b95-b4d3-25b27b26798e | -3.5862 | -52.681702 | 2026-10-09 00:06:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 601fcef5-8fd2-30ba-93dc-3d5307507af9 | -13.7842 | -52.780701 | 2026-10-09 00:06:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b68fbb2-11bb-350e-9b74-9a8c0386e10e | -15.3401 | -42.761299 | 2026-10-09 00:06:00 | METOP-B | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6ea41821-92a4-3991-ae64-bd610e4862e6 | -11.3985 | -46.6749 | 2026-10-09 00:06:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76993626-d19b-3cdb-8437-280c68db5668 | -2.8879 | -54.161999 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75d96725-b3a8-3687-898e-e72e7a436767 | -3.036 | -54.089298 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8d973ac-7c9e-394e-b8fb-1db808cd9946 | -16.5103 | -52.577801 | 2026-10-09 00:06:00 | METOP-B | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7285d6cb-250b-36de-8f0e-f6554a7e5962 | -8.7268 | -45.1618 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 915e2dbc-3545-3ab4-bc45-aaba2e86a68e | -11.8387 | -43.600101 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0ac88d88-8031-3e55-a786-97ae0f21132e | -3.0967 | -54.27 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70cf3b85-373f-3893-a769-91ee31d725da | -4.7349 | -55.6637 | 2026-10-09 00:06:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4df54405-ac4f-3224-8546-23ae4e743c0d | -4.6599 | -56.211498 | 2026-10-09 00:06:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6406966-cc74-3589-8408-f13a2a3c24a7 | -9.277 | -47.461201 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db10e7f7-6be9-393f-9062-52044c3869fe | -8.9028 | -45.208401 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b08d874e-1aca-373c-bd1a-e882cf50d0e5 | -2.8747 | -54.195301 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1bfa75a-4d77-3444-bc6f-2f6bde755876 | -3.1124 | -53.786201 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b55b1d07-16a2-3b93-9944-795bf03bd1ba | -10.3141 | -46.264599 | 2026-10-09 00:06:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a103ca0-bd2a-3f89-8183-cd6ef50abe5f | -2.8499 | -54.129902 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7516b76f-4c32-3bf7-8bf3-5b60680dc08b | -2.5779 | -56.181801 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43b7d9bb-dd4b-3b9f-9146-978cc79eec2e | -7.7568 | -54.9454 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bec7feba-497d-371b-968b-f16456576a84 | -12.4623 | -41.3195 | 2026-10-09 00:06:00 | METOP-B | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b544297e-ea30-3712-9ed7-e0285cd14d50 | -14.9377 | -48.091099 | 2026-10-09 00:06:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 895d7b6c-d809-3c7b-82c4-a809cd4e992f | -5.2621 | -47.9006 | 2026-10-09 00:06:00 | METOP-B | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d76f291a-f302-3125-9710-8773883d2f2c | -18.333401 | -42.378101 | 2026-10-09 00:06:00 | METOP-B | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc94733a-5b58-320b-a1c5-4b3af4350fbc | -6.7309 | -55.160599 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bf0a2c6-553f-3cca-b194-da6ee35d9112 | -5.7176 | -53.498901 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9257e9a-0bf5-3090-a818-16d14414843b | -14.1782 | -48.667 | 2026-10-09 00:06:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2b718985-e4fd-38f6-9204-a2675cdd3525 | -11.0578 | -44.053101 | 2026-10-09 00:06:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4ab50d1f-cce7-3c06-91e2-e2771edf4949 | -10.4191 | -48.879501 | 2026-10-09 00:06:00 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f693cbb-32c7-3e6a-a48b-a57cd131590f | -17.172199 | -51.742699 | 2026-10-09 00:06:00 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a567fe8c-59e3-301b-a01b-3d19fb177971 | -3.0074 | -54.2379 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee24f633-99d1-3dfd-922e-dbb79a3679f8 | -3.0826 | -53.9296 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd8b2e2-a4a6-3047-897b-da3e2486c197 | -3.8198 | -55.967899 | 2026-10-09 00:06:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c997399-39d5-35cc-9ceb-3e5ee596d4ef | -7.4011 | -44.745399 | 2026-10-09 00:06:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 49ed50b5-2ae0-3d5c-904a-3b67b94580d6 | -2.505 | -56.130299 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 445df2b7-2ee0-3cc9-9ca5-898784882dec | -2.9519 | -49.169998 | 2026-10-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9debdc15-7be0-32c4-845d-7c9c91c3c42c | -3.126 | -54.171101 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dacda631-b16d-3c1b-9532-97ca44ac97bb | -6.3763 | -56.2257 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e35fffc-ed43-3123-84b6-cf6251bde6f5 | -3.9279 | -56.040901 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fceeadc0-308f-3cd8-9f9d-87412a572bb0 | -4.9344 | -45.666401 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e808723d-7202-31fe-8d11-c716906e0b00 | -3.6078 | -54.5854 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fd5c9c3-0b51-3b52-afca-82adc71b97cb | -2.8318 | -49.505001 | 2026-10-09 00:06:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2741c82e-e0e7-36ae-a62e-10b680497610 | -6.7353 | -55.133099 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7737cbf4-0742-3fdb-a04e-e50a50e017b4 | -13.1109 | -46.356998 | 2026-10-09 00:06:00 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 230bf8e4-1354-3583-8f7a-0372bd272d7d | -4.8069 | -56.1366 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63d9341c-5a39-3d9b-8068-730d0d31d94e | -3.0727 | -54.254601 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d9f058f-1f17-390c-8c37-9490277e8953 | -8.2146 | -46.8284 | 2026-10-09 00:06:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a407b9d9-2edc-3f63-836e-0fe948ba7f21 | -15.1136 | -48.526001 | 2026-10-09 00:06:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e8a71d51-1329-3f9f-9a3f-740e929d7006 | -2.8661 | -54.156601 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b15dd84e-fe85-3fbd-82c6-b1f83507e1bf | -2.7165 | -54.6376 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07035cbb-7af7-3d77-98e2-0b28031be9ad | -6.7333 | -48.1124 | 2026-10-09 00:06:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3a94a2e9-70d7-324b-b251-ff09fe192cc0 | -5.7556 | -43.844501 | 2026-10-09 00:06:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 501e36a7-d8e9-36d9-93dd-2de886c15156 | -11.06 | -44.062199 | 2026-10-09 00:06:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f06cd107-0e4d-37b4-81b7-53762314002e | -5.6855 | -53.445499 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c94728c8-d712-3698-a3f7-3d8573bae961 | -9.1193 | -48.9146 | 2026-10-09 00:06:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12609285-b27b-3f04-9a3d-bff1bdc60518 | -1.1551 | -54.2248 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f524bbc-265c-36d4-a939-a4af9ddec7e6 | -4.6201 | -49.206902 | 2026-10-09 00:06:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00fe63bf-787e-320d-a358-a1486edcc432 | -3.2493 | -54.032799 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da2ffd4c-8cd2-33cd-a8d7-bdf76153eef4 | -2.996 | -53.9091 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1280668-bdbe-3e26-948c-1595809b0178 | -4.7515 | -43.999001 | 2026-10-09 00:06:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c1286da-24ca-3cc5-9328-69e0c6203016 | -3.203 | -50.5564 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 608fbecc-8b81-3d43-b9a7-3895bbbc0352 | -5.9975 | -40.943401 | 2026-10-09 00:06:00 | METOP-B | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3b6479dc-f6a0-39ff-be55-d775de3f6de4 | -3.5411 | -54.655102 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 848e6f56-8219-3a76-a432-c953278121fd | -7.0651 | -47.394798 | 2026-10-09 00:06:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4bd5f46-8148-3daf-91e7-9df9ff282f0a | -10.0265 | -48.041801 | 2026-10-09 00:06:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f366d9f-e959-3299-aa24-927cd55e475a | -2.8324 | -54.143799 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b4c723d-0712-3592-ad66-b3d25be0b862 | -11.755 | -44.952099 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9872e16-6674-3862-ba2f-bd5aac465697 | -3.1603 | -50.594898 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d582a7f3-2dcf-3f48-b5f6-8bb088a1aaf1 | -11.6057 | -43.7066 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d85617b-5d6f-3413-80eb-9ceed24b7d99 | -10.9104 | -50.757599 | 2026-10-09 00:06:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 66c64258-d991-382f-a9f8-02f4475e3d74 | -17.511299 | -43.668701 | 2026-10-09 00:06:00 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| aee05466-c9ac-388d-a2c7-80500c0e2b87 | -6.1257 | -55.6717 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85e3aa82-1a9c-38c2-b4cd-6d051dd857f3 | -5.3526 | -43.403099 | 2026-10-09 00:06:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b5ce20e-34a6-3478-98e0-54b5bb558909 | -9.8653 | -44.865299 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c7582be-b867-3cc9-9a5b-84bef7e8f6a9 | -6.889 | -45.911999 | 2026-10-09 00:06:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88fafeca-df5a-3339-ade8-087c62818f18 | -4.6216 | -49.213699 | 2026-10-09 00:06:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 103c3956-5e87-3b84-bd2f-e897bda7a157 | -5.415 | -44.631599 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15e51684-fe0f-397e-bae6-c6e0f5332bdb | -5.6994 | -53.462601 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e417c7e-d9fd-3b65-b3ed-8a364bb82934 | -5.888 | -57.712101 | 2026-10-09 00:06:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7059486-fe74-338a-91e4-447c3e7c6721 | -12.0069 | -43.438999 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 15a02fbc-1efe-39c3-bfbb-3b3ff8e3243d | -5.6724 | -46.3605 | 2026-10-09 00:06:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b321ff6-2a4d-325e-bcaf-2a93266af44d | -3.2775 | -54.067101 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee479940-eb74-3ded-9b0b-18012b9111bb | -14.0015 | -48.7528 | 2026-10-09 00:06:00 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a89a7994-449e-30a6-aeb2-accd6e92cdc2 | -2.5907 | -47.354698 | 2026-10-09 00:06:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README18.md)
