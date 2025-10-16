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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf727f69-ef40-3c4b-b5e1-eff66915d296 | -6.06001 | -44.31124 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60e06a58-ad6c-39aa-b5ec-edd3e00f8e43 | -5.6084 | -49.03324 | 2025-10-16 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4707e7b1-27fb-326f-bdb8-259fbcde3ccc | -7.48939 | -44.58213 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c4d658d-70b7-342c-8859-6319932ecf30 | -8.19606 | -43.96791 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b13d1d0b-a37c-36bf-8953-94bbd0f1d683 | -8.23787 | -43.40814 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c5438a49-9193-342d-8a30-7bf6ea645907 | -7.48031 | -42.6746 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eeacae64-7c09-3a21-907f-813d611d52c6 | -6.06916 | -41.90319 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a973b102-411b-3368-9cc9-ad9a9cce309f | -6.55183 | -43.92382 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9bac766-9eeb-3c98-ba48-af1f440f289b | -6.01171 | -43.11731 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 36be16da-14fe-3a06-b7b0-f7b451ae2a37 | -5.68978 | -44.35713 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 871ecf32-8a66-339f-bec5-5cf164ab3119 | -6.19286 | -43.29455 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 039a7028-f995-313e-ad41-3e6738d64ad7 | -6.22364 | -44.60045 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 22b571ac-fba7-3ac3-b3e5-93ca9308e453 | -6.41101 | -42.54931 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a2640351-3228-392a-b49c-540b4808e473 | -6.18105 | -44.30713 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b89ef23-982f-3f4b-b68b-afcb9e7c5cad | -2.63008 | -46.83634 | 2025-10-16 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e93ce9eb-ecf8-3dcf-8be1-9c084011ae4a | -4.8765 | -48.64331 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a405fc99-54c2-38a6-a218-4309739395d7 | -6.25951 | -42.89835 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3bfa9b5-f555-30a9-857d-ee16971e5854 | -4.41543 | -40.17998 | 2025-10-16 04:38:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66fe4bb5-26fc-32f2-a774-b2243140ed77 | -7.20677 | -45.48235 | 2025-10-16 04:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7c82bb0-4a08-3b3a-bc6c-7612303b7f9a | -4.37367 | -43.39725 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 69f7fa41-70c5-35d9-a787-a396af242a8c | -6.06421 | -41.89629 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6840f655-34ec-3963-a69e-536cb3f36d59 | -4.65391 | -47.95015 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a06cdfb-1bad-3c37-b13a-1c9b70a2be6c | -5.39304 | -40.90094 | 2025-10-16 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| af4919c4-5a6f-39a2-b25e-c4aecc6a14aa | -5.17395 | -46.41077 | 2025-10-16 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbaa6478-45a8-348a-9b55-3c4513978eaa | -5.53814 | -46.1608 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8669f14-fdef-34f8-a218-8691ec4e62e8 | -5.76863 | -47.91105 | 2025-10-16 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fee9bd51-246f-35d6-862b-07a301ff47f1 | -4.38367 | -43.38723 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad380fe0-8976-313f-9fa5-31085b3a0335 | -4.11131 | -48.02707 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6c8a6caf-7d6d-361e-8fed-ee34d70c0f24 | -5.25556 | -44.90227 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9fb36e6-6a03-3623-86e6-589d524e0bd8 | -3.01483 | -45.38875 | 2025-10-16 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 06f6daa4-f4f6-3957-af3b-81dafd45363a | -1.49723 | -47.81016 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20aa2799-a65e-30ff-a717-32750074874a | -7.31518 | -50.36666 | 2025-10-16 04:38:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3bb5844e-1f73-3d2d-bb91-4c30cdc8fa1e | -5.66175 | -45.96561 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64b48de9-5c1b-31b7-9109-ad8b9f82662a | -3.17039 | -49.5377 | 2025-10-16 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c754c17-0fb3-3444-8ecf-2cc8a7a0e668 | -5.68926 | -44.36058 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b63d513-4302-3b31-ac2c-d072327a169c | -1.39406 | -48.99195 | 2025-10-16 04:38:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b169286-797f-3a17-a48b-1f8761956357 | -6.62044 | -42.22573 | 2025-10-16 04:38:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b521bf1f-fa61-3b5f-bea6-a2ff8980704f | -7.94859 | -44.13091 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97197829-7f45-3bf9-b2ce-778da066e2b6 | -3.84155 | -44.5447 | 2025-10-16 04:38:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc3dc26c-97e2-3c2c-a245-7314101fce9f | -3.11652 | -51.15265 | 2025-10-16 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e7480a4-2783-3330-b518-c55a7dee0218 | -4.67 | -50.70714 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8111d4ad-b0c4-3d69-8e91-e7a24256e719 | -6.38705 | -41.4796 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| a1c216ca-2956-3234-a2eb-53fe300ff117 | -7.67591 | -47.5253 | 2025-10-16 04:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 300134b2-442d-3ab7-a215-84b3bfbcb168 | -6.26301 | -44.33763 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6bca068-ae23-366c-b074-de94642d9e51 | -6.77623 | -44.65609 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 888ab571-52ff-359e-9a18-5114f17e80fb | -5.4767 | -42.93036 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4c82c84a-3d32-3a4d-a349-45b5515bbb75 | -6.99265 | -45.5966 | 2025-10-16 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c844a2a4-ba3e-3f7a-b35a-d6e1ea0c2977 | -6.5654 | -42.96599 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75539c3f-f0a9-3d1d-97b3-75f35627f847 | -7.3561 | -43.8578 | 2025-10-16 04:38:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d5f747c7-4066-3d0f-a55a-8ca929d5a2dc | -7.39649 | -39.69539 | 2025-10-16 04:38:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 51.0 |
| 697c50a0-b836-3dc0-9a1b-5db908b202da | -7.96589 | -44.12931 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4ef242a6-4fdb-357b-9633-dc4d7010eaa0 | -4.10906 | -48.01964 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| f72f6b48-9e30-39d0-b709-d25773e9f14a | -6.14765 | -44.219 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f07ecc7-319e-318c-b0f0-7f526fb5d079 | -6.79005 | -44.5307 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62a85ac7-f5d0-3a5f-9ffc-f22ca099c4a4 | -4.71109 | -48.71926 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 050c9af5-b3a9-3535-b4ef-8b29e2300961 | -5.87792 | -43.87433 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e3f8a37-9d91-3de6-96a2-15927cf0c3ff | -7.40863 | -44.74563 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f481455-6354-3c8f-af7e-a192ba3ec526 | -3.15965 | -49.17476 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cfa3f4a-91f0-3a40-b506-8a6fab2061ff | -7.44097 | -44.74722 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88bb54c7-ff67-33a9-a165-164a1fb58340 | -2.96406 | -49.57277 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b89167fd-00ab-39c2-b8bd-aab5fb24a1bd | -4.38423 | -43.38343 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a0c698c-e2ee-308f-aae9-d09d3be339ef | -5.82549 | -42.34499 | 2025-10-16 04:38:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e47ccb75-5a3f-3d2a-8f06-b060e953a558 | -2.38414 | -47.71144 | 2025-10-16 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0ee725c-3508-38f6-b86c-0ff90625b561 | -5.3857 | -48.9133 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee678248-0021-38d1-a004-63d50f5293ce | -4.28288 | -48.58526 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 558e1f7a-f3cc-3880-804e-06556374e703 | -6.14039 | -41.74095 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f1d5be83-9da3-3286-ac82-5261c3b1459d | -7.61166 | -46.47354 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 200327d1-c8bd-3f7b-96bf-7f6bcb91b7dd | -8.25383 | -44.07758 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0802511e-a669-31a6-a624-f7b39880bf72 | -5.85616 | -43.8789 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d06d6298-3639-3191-97fa-0cc3f56e70fd | -7.2609 | -41.74069 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 27b21205-18e4-33e2-b247-e20ff6dcfae6 | -2.43915 | -47.18519 | 2025-10-16 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b17d453c-ca05-3526-973f-774f1ee164c2 | -8.24217 | -43.41129 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6e8d969b-5f83-38bf-9dd3-194c5f234334 | -4.41225 | -50.31673 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9b4680b-8e2b-3e1d-8534-4f1befb6b3b1 | -3.23636 | -43.45975 | 2025-10-16 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 47475cd4-2616-3cf6-a56d-e9bf3992c4d7 | -7.55947 | -43.91672 | 2025-10-16 04:38:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ac68909-8729-36dd-9013-351e83b3bc04 | -3.05737 | -52.65283 | 2025-10-16 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e08629df-3c69-3a79-b94c-c2e8e6990a8b | -3.27261 | -45.83574 | 2025-10-16 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7bc9b436-9274-36fb-a365-f1dd3acfab85 | -2.45408 | -49.41805 | 2025-10-16 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8908584-feea-39bd-9997-fde520c00f2c | -7.92767 | -44.12783 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bef2bd41-4c82-3ca3-91df-255bbd907731 | -8.13725 | -44.4753 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bbd98d6-b3ee-3f39-9fc7-eadd6d6c7c1a | -3.45036 | -51.61004 | 2025-10-16 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ff8361a-4dbb-3ff0-855c-3009a7266fce | -6.06051 | -44.30774 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1619f613-8010-33e9-bd2e-b5877fd71215 | -6.05437 | -41.93086 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9548dfb2-2564-305c-8440-e7f67325e3c4 | -5.29533 | -42.66377 | 2025-10-16 04:38:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a79afb44-59e2-3ec7-9faa-730914282ace | -5.83463 | -42.34652 | 2025-10-16 04:38:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 52887b34-f540-327c-881a-3ed509713842 | -2.44062 | -49.37265 | 2025-10-16 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 985cd80c-aa55-35f3-8199-c5f173a0358d | -7.11528 | -44.72647 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32d21974-6332-390e-a8d6-f3a967145c1f | -4.87927 | -48.64726 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0bfe6d0-a35f-332d-aff5-70db73b6a502 | -5.73304 | -48.97515 | 2025-10-16 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0a1e22a-faa7-3ce9-99f4-0bda3a9fb40b | -7.20742 | -43.8375 | 2025-10-16 04:38:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ef593ce-b23b-3fc0-b679-b765746f1ebd | -7.46649 | -41.5181 | 2025-10-16 04:38:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f175acea-3d0d-3c49-b013-c6d1d9c5eb55 | -6.06168 | -42.71736 | 2025-10-16 04:38:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7e67e077-e363-3882-a338-fc0e527d506c | -2.26074 | -56.05432 | 2025-10-16 04:38:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26754a07-7253-31ba-aeff-bd75a2736032 | -4.66882 | -44.10156 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| becb38e1-f61c-358c-8750-c6382e8676f1 | -5.88389 | -43.8909 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0afb5d8f-f604-3bc0-bff5-d847c9ed0aea | -7.54893 | -42.05875 | 2025-10-16 04:38:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| befce58d-d9ea-3dc2-9bde-9235ee2a0f22 | -7.49876 | -46.6521 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f535e3e-4c12-39ac-ba8e-451e63c91d10 | -4.3607 | -45.53118 | 2025-10-16 04:38:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 014cec2a-0b37-373d-b5e4-aaa7ba9e744c | -6.56854 | -42.97551 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3bdda798-e44c-3970-b7e9-b17546864b3e | -4.40285 | -44.07568 | 2025-10-16 04:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README59.md)
