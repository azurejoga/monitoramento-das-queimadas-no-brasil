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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82e6909f-a801-366e-869a-b0f2218b0976 | -13.1838 | -47.2929 | 2025-09-15 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 7af73498-87be-3e3d-9fe8-3c45fa065e99 | -8.8981 | -46.2035 | 2025-09-15 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5dc782a1-8333-3459-b297-ac4ce7d20009 | -12.5979 | -45.7021 | 2025-09-15 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| c8badc53-956e-3d95-addf-ba9a43a7beb6 | -12.6768 | -47.7026 | 2025-09-15 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 1925b64a-d600-3c84-afb9-e9680d3f5a5f | -12.8212 | -47.1445 | 2025-09-15 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 59f4efc7-9f04-3bd3-b359-f3096be0811f | -11.6434 | -46.591 | 2025-09-15 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| dc7db92e-e631-3ea4-9aa2-3eaa29571e63 | -8.4145 | -47.2324 | 2025-09-15 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 96cee0a3-e545-32b8-a751-94f35a39e4f8 | -10.9452 | -47.3538 | 2025-09-15 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 1e07d108-231d-38cc-be8e-8e8882469c7e | -12.1663 | -44.1224 | 2025-09-15 13:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 0ce2ce87-e9ca-3920-97ad-3f8744de85e3 | -5.7363 | -43.1981 | 2025-09-15 13:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| f8f19ce8-ffe0-3d8e-8727-c8ec15c24806 | -8.5944 | -46.3695 | 2025-09-15 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1527b9a0-cf62-3b4a-bf5a-82b474449b18 | -12.5607 | -45.639 | 2025-09-15 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 0e1fd1fb-bc70-3ed8-bb24-ca5e5daafdd5 | -6.3372 | -43.1492 | 2025-09-15 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 066a2c02-47d9-35f0-b932-b440bf581271 | -7.3248 | -43.9449 | 2025-09-15 13:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 8a3ff23c-9f8e-313b-9ddd-dda59cae27e6 | -12.7875 | -47.9541 | 2025-09-15 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 41ca9a9f-02ba-36c5-8fd1-a3ac30530fed | -8.9601 | -45.7912 | 2025-09-15 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 243.7 |
| a3436ca5-67de-359b-99c3-27ed14475c97 | -10.075 | -47.1908 | 2025-09-15 13:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| c0fc9cbc-2f7b-3204-a24d-ff4aedba608a | -14.5168 | -47.3304 | 2025-09-15 13:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 1e7cc530-10c4-3100-867f-248d0242fb91 | -8.917 | -46.2015 | 2025-09-15 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e68bfea0-308d-3a01-92cd-ebbfccd6aa83 | -11.3884 | -43.6548 | 2025-09-15 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3667cbde-53d7-3910-8931-2061574a52c0 | -6.356 | -43.1476 | 2025-09-15 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 149.1 |
| b96dceed-dca8-3021-9244-b36c4377e82f | -6.1504 | -41.1889 | 2025-09-15 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| edcc61ce-7cc2-38f9-8fb0-0d07c34c72b6 | -8.9601 | -45.7912 | 2025-09-15 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 204.9 |
| ae220c73-ed99-33b6-8d71-556b4a5db0c7 | -12.6533 | -47.9507 | 2025-09-15 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 571c4dab-465f-304d-8a0a-8b0d2394de51 | -14.5163 | -47.3531 | 2025-09-15 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8a4baba6-a796-352c-9e17-df99e7b8c521 | -12.5975 | -45.7251 | 2025-09-15 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e68818ac-5537-3e63-8c55-d1d3cc1b235d | -8.9734 | -46.218 | 2025-09-15 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 288.0 |
| 11daa36b-cc00-379a-99d3-9d037d81ac1f | -11.6626 | -46.5884 | 2025-09-15 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 92c71617-9d30-3eb5-9dd2-a35663d31181 | -10.935 | -45.5978 | 2025-09-15 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 4e2d6492-29b4-3c89-8025-8bf7372de2dd | -6.1881 | -41.1855 | 2025-09-15 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 144.8 |
| bc8815b7-5548-39d7-bc95-7c1108505934 | -10.075 | -47.1908 | 2025-09-15 13:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 0a7ca256-e489-3b3f-a096-7142b30319d5 | -8.8981 | -46.2035 | 2025-09-15 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 97c2af6b-d567-3814-ab7d-752d9aeffd48 | -6.337 | -43.1727 | 2025-09-15 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 197.5 |
| bba6c3f5-072e-3774-b406-b310d7461f07 | -12.7879 | -47.9318 | 2025-09-15 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| ae641743-197f-32c6-b46b-f7d85e2671d5 | -8.9548 | -46.1975 | 2025-09-15 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 7ca0f707-ac8f-3953-ac59-72911e05dda1 | -10.9452 | -47.3538 | 2025-09-15 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 78962256-8bca-3413-9042-5e1bbfdf8772 | -13.1838 | -47.2929 | 2025-09-15 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 3014e878-341e-3676-b979-e22849d06c07 | -12.8404 | -47.1417 | 2025-09-15 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 74655f5b-c973-39ed-9185-1f43888c75b1 | -8.9604 | -45.7686 | 2025-09-15 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 183.6 |
| 8a106e0d-b7cb-304f-8c13-39d6709b521f | -13.2031 | -47.29 | 2025-09-15 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 01940167-0b11-3edb-a50c-a09183e678d0 | -12.9599 | -47.974 | 2025-09-15 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 70f39346-ffe6-39e3-93c6-c1ca6c8efe77 | -6.3372 | -43.1492 | 2025-09-15 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 228.7 |
| e40fbcef-636d-3122-aa30-77ed137aa3c4 | -10.948 | -47.1753 | 2025-09-15 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 3684a7a5-80d3-3b4a-b9ac-7d06d2ff8467 | -11.1303 | -45.3196 | 2025-09-15 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 84d5a599-a29b-3620-b42c-1061ccd8f6b0 | -7.676 | -44.4879 | 2025-09-15 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 116724c1-0e1c-3139-9772-0eb5883562a8 | -10.9159 | -45.6004 | 2025-09-15 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| f42da73c-2c51-3fdb-8801-866f67825c12 | -8.9412 | -45.7933 | 2025-09-15 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 237.1 |
| bd3d9282-2c4c-3d93-86ec-a956990d398a | -8.9545 | -46.22 | 2025-09-15 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 383.8 |
| 16bd93d1-1751-332e-9d6d-19eedeb1b294 | -6.169 | -41.2114 | 2025-09-15 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 211.7 |
| 1eb7c625-6d26-333e-87b7-b9ce251597aa | -5.7363 | -43.1981 | 2025-09-15 13:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 1f8f6f33-9acb-3056-82e6-d15f8d09c204 | -11.6622 | -46.611 | 2025-09-15 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 3e8a9de4-6d76-3f20-9212-132a435e4ffa | -9.5167 | -47.9369 | 2025-09-15 13:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 4d5101aa-a746-39e7-97ca-db2d3061283f | -14.8218 | -51.6362 | 2025-09-15 13:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| ccb90a64-87b5-3887-83bf-9f3814affede | -12.1861 | -44.0958 | 2025-09-15 13:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 878d4877-06ca-3b0f-89b6-64766a112eab | -16.6725 | -49.7838 | 2025-09-15 13:20:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4afe8e09-9ddf-3450-91b9-7287b4243d42 | -14.1978 | -48.7673 | 2025-09-15 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 76b2e777-4b87-3133-a1c6-659b8b5aa621 | -8.651 | -46.3637 | 2025-09-15 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 7a192b7f-5a5c-3c71-935a-d71d10c80614 | -9.9157 | -47.762 | 2025-09-15 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6abb191a-8558-393c-b67a-8050b85f5998 | -12.5607 | -45.639 | 2025-09-15 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 7435a538-8ba1-3234-8bd1-d96243cd6c28 | -5.8399 | -44.1642 | 2025-09-15 13:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| ac1188d2-65e7-3197-abca-1cf7739c5b7a | -16.673 | -49.7615 | 2025-09-15 13:20:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 8e119856-a222-3f71-9033-2f044da42cda | -8.9787 | -45.8118 | 2025-09-15 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| fe3fb9e1-ae31-3892-9ee0-d49a5f933134 | -8.917 | -46.2015 | 2025-09-15 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| c3d5fa5b-66af-386f-b457-6b6d5950ca53 | -6.1693 | -41.1872 | 2025-09-15 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 238.3 |
| a4404019-031e-30bb-af55-f25b1585463e | -10.9346 | -45.6207 | 2025-09-15 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| da59a464-6f36-3b4b-8036-7d87acb6c637 | -11.4512 | -50.3483 | 2025-09-15 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 20b437fd-03f1-37ad-99d9-050538181003 | -9.5164 | -47.9589 | 2025-09-15 13:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 70a371c5-8a97-32d9-a5f7-8ba0ce683d36 | -12.1668 | -44.0988 | 2025-09-15 13:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 99b5ff4d-143c-316b-9110-923df53419a8 | -9.2235 | -44.5052 | 2025-09-15 13:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 3830d411-0d21-3a82-97ef-cfb1be842a8d | -8.9784 | -45.8344 | 2025-09-15 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 2ef22690-aeac-3622-87cb-95d85e20712c | -13.9288 | -44.8106 | 2025-09-15 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 345ade58-9278-3a41-af7c-8c5b5de7d81b | -7.6838 | -48.8682 | 2025-09-15 13:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a4ff21d3-6287-3a98-8215-6b34f81793b2 | -7.9634 | -45.6449 | 2025-09-15 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 4ea7deba-0ee8-3b6f-b9d9-d01864e3a0d6 | -6.3558 | -43.1711 | 2025-09-15 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 53a778b5-3362-30c4-a260-d1a22ba97357 | -12.1663 | -44.1224 | 2025-09-15 13:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 7a3907a8-ca78-36b3-a4f5-2fd78de2924a | -12.7875 | -47.9541 | 2025-09-15 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 3684c390-d80a-36c3-a4bf-3e82184d3ee0 | -6.356 | -43.1476 | 2025-09-15 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 4299f7b9-56a1-3c5d-8fa7-c837c53cad53 | -18.9851 | -48.5844 | 2025-09-15 13:20:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 110.7 |
| b974d1f1-0494-35f7-a840-50602fe067d6 | -20.9096 | -46.4681 | 2025-09-15 13:20:00 | GOES-19 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 128.9 |
| 5091eb1a-62cc-3f9e-a6c5-399bd427fc2e | -14.5168 | -47.3304 | 2025-09-15 13:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 9bbf6bae-966c-3a87-87a2-99413038b9b5 | -11.3884 | -43.6548 | 2025-09-15 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 4117f8c6-81c3-32d8-8122-9b914a5409e0 | -7.8073 | -46.1323 | 2025-09-15 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 2d1a23ea-0b6f-3922-908b-292e644c763b | -6.169 | -41.2114 | 2025-09-15 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 150.3 |
| 486506df-68b9-312d-8676-a694d3116a02 | -13.2031 | -47.29 | 2025-09-15 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 9461ef0a-3d02-3b90-9c6d-f530454b3f1e | -10.9346 | -45.6207 | 2025-09-15 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 1a7dea16-eb08-3af6-bc39-d554a58e18ae | -12.6533 | -47.9507 | 2025-09-15 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5c8929dc-7e8b-3e6b-aa78-5a03bde3baa8 | -8.8981 | -46.2035 | 2025-09-15 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 346.1 |
| 4a356e6c-2ec3-3775-9ce6-e83b808e1809 | -8.8701 | -45.4611 | 2025-09-15 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 95231ad1-d8a7-3152-bd3f-74aba61ab113 | -10.9452 | -47.3538 | 2025-09-15 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 87ad801e-5e7a-35be-928e-cf016b9ba033 | -20.9096 | -46.4681 | 2025-09-15 13:30:00 | GOES-19 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 113.8 |
| 42121360-7244-3e90-ba19-39f1cad2f2ec | -6.1693 | -41.1872 | 2025-09-15 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 195.3 |
| 9df62387-8aa7-3e00-86b8-98f6eaf1a9f1 | -16.6725 | -49.7838 | 2025-09-15 13:30:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| f1c77fff-68fe-31b0-a3f0-c6b23326c58b | -16.673 | -49.7615 | 2025-09-15 13:30:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 141.4 |
| ea317e74-8816-30f8-84ad-f67cb96d5b02 | -10.9667 | -47.1952 | 2025-09-15 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 220.4 |
| d1b99085-22e5-3ef6-82bf-0d821694c5ef | -10.9159 | -45.6004 | 2025-09-15 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.7 |
| dc21d001-7fa5-31b4-839a-732fa1185b67 | -15.6778 | -47.7198 | 2025-09-15 13:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 5c9f659f-c90f-3d29-9cbb-304a90699a57 | -9.5164 | -47.9589 | 2025-09-15 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| d78ee737-cb44-3472-9c2f-a01f8d904598 | -18.9851 | -48.5844 | 2025-09-15 13:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 111.5 |
| a795c540-46f6-38bb-8f63-183763ba58d7 | -8.651 | -46.3637 | 2025-09-15 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 9a2a4d1d-ce3a-3a9b-bf45-a2de27ee7e76 | -6.337 | -43.1727 | 2025-09-15 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |


[Clique aqui para ver as próximas entradas](README73.md)
