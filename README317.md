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

## Dados Diários - Página 317

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7805af51-58b6-32b3-813f-d57da3cb6582 | -11.0825 | -44.03741 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 233a32fd-bee9-3469-a2d1-7efecb3a0d80 | -8.96174 | -45.13892 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 47d86b0e-ed6c-3cc0-88e1-40629d50ef53 | -10.1586 | -39.24682 | 2026-10-08 16:37:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 8f21fe41-fc12-398b-bc5b-b77135fe83f2 | -11.76492 | -45.55106 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 508c88cc-c107-3816-ab3e-7c878945c426 | -6.84341 | -39.56232 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0dd6883d-39d2-310f-bb94-ec5f81ae487e | -12.62287 | -47.88919 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 0fa90135-b16e-3338-9dcb-4b574baf6880 | -6.04323 | -37.57037 | 2026-10-08 16:37:00 | NOAA-20 | MESSIAS TARGINO | RIO GRANDE DO NORTE | Brasil | 2407609 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 37730bad-4a7b-3c54-9b58-f41083947315 | -8.07134 | -45.61938 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 301cfba7-274c-3921-b2e4-eaf8751e2270 | -11.07972 | -44.04149 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| c5b92468-0a2a-3f9f-bc87-51a0bae12571 | -6.53446 | -45.37903 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| afc0de22-8ec3-3fbd-8663-5b467588fafc | -8.29566 | -45.73307 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 176.4 |
| e83e64a0-d267-3cfe-a012-07a4ea3c38c9 | -7.21553 | -44.27728 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b1c26679-100a-3666-94e1-5c0b80e15d34 | -8.96982 | -47.55433 | 2026-10-08 16:37:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8566d53-2742-3c42-99ed-8b8f41f6eedc | -7.16971 | -47.7987 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 476cd9f8-8184-3398-a799-fd37865c1352 | -11.77413 | -43.53114 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| a25c9a7d-d7fe-34c4-b742-cc3545591e71 | -6.8601 | -41.74249 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| cd2771d9-b20e-3044-b89b-ba65b4215b54 | -6.91194 | -45.47215 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 28fecada-e761-32a9-9d8d-206e1ad83fc2 | -8.32776 | -51.30991 | 2026-10-08 16:37:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 0bb32598-0a6a-34e0-9881-07526bf28604 | -8.65692 | -54.55877 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4da9cd9b-78d6-35f9-90c0-058e6bd83e5e | -11.57029 | -45.36076 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| a5da4332-6d65-3f5f-a87a-6101bf8fd2b7 | -6.66163 | -35.11554 | 2026-10-08 16:37:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 6bc382d9-a535-3f7b-9f8a-e49682447806 | -6.5289 | -45.387 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2adf2151-255b-3e4d-867c-c7a1b1df881b | -11.13892 | -46.12266 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e8253332-c156-32b9-9a7d-762da40c37df | -18.28713 | -42.23859 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.6 |
| ee1eb0c0-f1e4-3939-b501-1b039a45b5cb | -7.3801 | -46.2277 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 86b291b8-0f7b-3aa6-aeb5-a33902b578c4 | -9.08021 | -45.1156 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ef7b261f-ee0c-3ef5-a340-9c456daee027 | -13.35585 | -43.8765 | 2026-10-08 16:37:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 158.7 |
| fb3faaa9-9a59-3bcb-936b-80241d1337bd | -11.30623 | -44.82706 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 81e6867c-f4ac-373f-b127-2bca22a3c13e | -11.44959 | -43.38792 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 06d53c38-beb1-34e0-91c3-e8f06cdef953 | -7.22498 | -44.16061 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d37b7af2-1cb6-3387-8fef-a0b149add516 | -8.20993 | -46.42284 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 411aeca6-c1ba-38b6-8d08-ad5afd1b41a7 | -6.68075 | -45.57981 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15f469d5-850f-3215-8478-18df99e13e9d | -9.7596 | -44.78776 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 74df2223-e464-392f-b17f-de3ec2a1f193 | -17.22092 | -39.38174 | 2026-10-08 16:37:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| e6135c1b-4fc6-35da-8718-ee45101ed3e8 | -6.59668 | -39.06298 | 2026-10-08 16:37:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 323475f2-938b-37d6-9fa7-082cc5af1563 | -8.88663 | -45.60363 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0b894e00-81a9-31eb-b824-c6610ddc7f58 | -11.22191 | -45.25459 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 9b08d205-0d47-3ca2-8ea6-bbd549f716c9 | -5.97158 | -40.91348 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 5c8a344a-f0fc-3bd1-b134-e70898a45333 | -11.33518 | -46.69058 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| abfa5bda-38e4-3508-bb22-8d3370591485 | -17.98584 | -43.22519 | 2026-10-08 16:37:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 24118e44-efa4-3654-af37-1f6c722c3b7e | -10.508 | -50.83931 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b6d86ba3-0b9f-3023-9d0b-1beeb87ea560 | -11.58536 | -43.66928 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0d0edf86-43f4-3d34-8819-b166891162b6 | -5.74971 | -41.73167 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| f4d3b725-b1cc-30a4-a36e-896887c93576 | -11.59374 | -43.67903 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| b84b13a5-6640-3e1d-8ca7-341d9b790f06 | -13.64355 | -47.67287 | 2026-10-08 16:37:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8671c880-fd26-3a18-9a05-2302622e4231 | -11.7157 | -43.65512 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aa5a2dda-9c3b-33f3-aff9-98ae13faa7f3 | -6.69098 | -45.2933 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d87d0529-6b5b-3c55-8029-be76711170f5 | -19.70059 | -42.17907 | 2026-10-08 16:37:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d229c1be-c5e0-3436-b245-c1f85b5fdc27 | -8.54606 | -46.9195 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3facc5a0-2828-3cd1-9436-9a35cdd66a9c | -10.22405 | -49.34573 | 2026-10-08 16:37:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9ce83605-fe2e-3f05-9fdc-adaa025994a0 | -8.06816 | -45.59855 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08901694-8a2c-31bb-bb10-3dc7bd181c13 | -6.22641 | -44.8573 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a02950fd-e558-37fa-b996-f3e2bb011e34 | -7.81536 | -44.57352 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b7443b1e-0c2e-37b1-a3db-f379ecf57a21 | -6.97295 | -47.67555 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 82ccb31c-caaf-3826-994d-39ceee9050bb | -11.76271 | -44.95059 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 24290bd6-70d7-3183-baa2-d528de4406c1 | -5.9723 | -41.36946 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 9aedf998-d983-38b4-a0cb-95bd268033e1 | -9.02863 | -44.38404 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 9d959843-e15f-33bb-a7be-4d1e0d6f139e | -8.59091 | -44.86942 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cc6b61e5-7999-30f0-ab4d-3d642f4a3640 | -8.79725 | -47.04866 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 92333d94-964b-35e7-ac1c-89b9575c2a32 | -8.55336 | -46.92213 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62d161f0-9871-3402-8194-b10d8dc0c7b9 | -9.5214 | -45.60578 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 6e8f7798-5ae6-324a-a025-2e8412771460 | -6.89028 | -43.70406 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| ad59ad8b-d96d-3fa3-881f-e07d1115befb | -10.76059 | -46.5881 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6cf62283-adf0-332b-9757-9b99a1c6baa8 | -8.35065 | -47.65369 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf6c7932-f182-3fb2-ac1a-dec2ef1f4bce | -8.96014 | -45.12847 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a9444bb0-cf08-33e9-bc70-df30bb6d54fb | -6.67202 | -45.36816 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1a4cd3f5-f36e-30af-be49-2582044bf1cb | -7.22216 | -44.16477 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c26ded27-8bee-3d4e-b0bc-33ad38e964b3 | -10.30626 | -46.61267 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1b1da0d7-0d85-3076-bf79-544f740af52a | -11.20612 | -45.21751 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 7e904085-dc8c-3ab2-af9f-b5f7c6950288 | -9.57895 | -46.85093 | 2026-10-08 16:37:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f46c1531-33c0-3c9e-bb6b-a7b7850523c4 | -8.04765 | -49.40545 | 2026-10-08 16:37:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 95c5b0af-06ad-3a43-813d-8882e155a957 | -7.22576 | -37.94577 | 2026-10-08 16:37:00 | NOAA-20 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ce6fa88b-1a1b-3422-82ea-3167979d99db | -7.03811 | -44.73038 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bcd56ef1-2ffd-3d44-b7e5-a305fc633fae | -18.52277 | -40.77306 | 2026-10-08 16:37:00 | NOAA-20 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f499ee1a-bda8-30cf-894e-c588d749123d | -9.39142 | -45.89121 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac93106a-8d9e-3e6e-b8da-75880d53f565 | -7.88249 | -55.00534 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 52416d78-3f89-37a0-9767-616e500912e0 | -9.89897 | -44.81186 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 37.6 |
| ae4db0b6-c445-3d5d-85e3-f8e8d50e9b0a | -9.8999 | -45.19466 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 438e4550-6af7-3ba8-a355-13313a6f910f | -6.97714 | -43.29698 | 2026-10-08 16:37:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| f1ee13c8-01cd-3f16-add3-e50d7522044e | -9.3693 | -45.94538 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 90b93af8-cb57-313d-b623-15fabcaf3853 | -8.21273 | -46.41879 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b0af03c2-71a2-3422-bb20-58d540ddccb5 | -10.90857 | -45.5385 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 02ffccc9-82d7-3f86-b39d-031eface688e | -6.18663 | -44.10735 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b77af963-4705-37d6-a457-abc08b4b64ef | -11.62801 | -43.07547 | 2026-10-08 16:37:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7044d9dd-3fba-3810-88ff-5c22347655ee | -6.88849 | -43.69276 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| de0970ec-9bb2-3ed0-bbfa-0971b4668680 | -7.75907 | -43.83441 | 2026-10-08 16:37:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7b164b95-de0b-3206-b158-cb96df8caf9c | -6.70423 | -45.29123 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5db14776-912c-3d4c-991a-7453662d734d | -9.44296 | -44.60611 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ae4346f0-4b4d-363b-bc6a-c9f9ea1725be | -8.23263 | -54.73148 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| af4fc9ae-0e2f-3c40-8661-02a1a54544ef | -13.64821 | -47.67742 | 2026-10-08 16:37:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 59cf397f-481e-3d84-86d7-58ec19f7a574 | -6.89804 | -44.91936 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e0a4a6f9-542b-3831-8112-4175fcae1266 | -9.97421 | -43.5024 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 00df5876-ecb8-3265-aac8-e1ea03516e15 | -12.02332 | -43.44966 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 313.3 |
| e72be95e-1d4c-36bd-a845-4c694bf1b5b3 | -6.88624 | -43.70082 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| a73daf43-3af9-388b-b3b0-de783b7b8607 | -11.80315 | -43.51904 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3905c942-0246-3ac5-850c-e64cacb0f463 | -12.22627 | -44.76451 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8311e911-1409-3232-8eff-d5e19a07603b | -5.98895 | -40.94406 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 48566e32-cef3-3a04-84e2-eb465d4328aa | -8.07518 | -45.62235 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 9ad4b1aa-d96b-3c98-b58a-92ae2ad5dd0c | -9.97626 | -45.9684 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c209b5d0-5551-38b2-a3a7-c8841181bda0 | -12.15262 | -44.72569 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |


[Clique aqui para ver as próximas entradas](README318.md)
