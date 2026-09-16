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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4d5753e-2b57-3a70-a433-7d5eee5e5748 | -10.45955 | -44.94765 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5db63c12-dd15-34e9-8840-9109bda2b2b0 | -11.13465 | -40.47742 | 2026-09-16 04:14:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 640914b4-3ec7-38db-bb91-edf2b93624af | -10.41194 | -48.65375 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e83724a9-0b59-3f2a-bb0f-10416ff92e94 | -2.90578 | -50.42829 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3754bf43-517c-3d6e-b395-ef4dab183db0 | -8.78266 | -45.9016 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44b4dd2b-4a39-381b-8ccb-5d35fd175a30 | -10.31841 | -45.27525 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e92cda7-73db-390b-9b40-8fc8c0a26e2c | -8.47359 | -44.56791 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5859db46-b03a-3cb8-9727-7b26515e5bd1 | -5.71994 | -45.20633 | 2026-09-16 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9031c77a-cf3c-3e94-bcc0-9cbbab0dacc9 | -6.31003 | -41.6832 | 2026-09-16 04:14:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2bc27533-f7d9-3fdb-8189-0d8acfa6f4af | -7.08622 | -47.49688 | 2026-09-16 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d14632de-38c4-3bb9-99b6-c189715603a6 | -6.00217 | -47.39104 | 2026-09-16 04:14:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fcb27136-9a64-35ba-8a3e-98ba0b01c641 | -6.35398 | -55.56501 | 2026-09-16 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d03e3aac-70f9-3608-a432-f96f63ba6e78 | -9.84588 | -48.3601 | 2026-09-16 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c220ff16-1eac-3385-a422-69ddcbbd759b | -7.08622 | -43.56392 | 2026-09-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 883a041e-5930-31db-a488-9cc2b8116aae | -8.80503 | -46.89489 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5dffa57-a263-37a7-83d6-18b8c3676eaf | -10.76745 | -46.22716 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc150c43-cfb0-3c05-8bd5-a2e0659e3292 | -10.80551 | -46.18019 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9392e73c-aca2-318a-b64f-5bfd1e22a277 | -5.10116 | -47.61728 | 2026-09-16 04:14:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a0264240-a9ac-3f88-82af-5ff79fe8acc5 | -8.37181 | -54.73477 | 2026-09-16 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2bf3ea7-4b2a-3fd6-8ea0-38aa2bd60c38 | -7.26218 | -46.67235 | 2026-09-16 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51b35d6c-4c67-38f5-bba9-e890a374f4d8 | -11.82751 | -37.57186 | 2026-09-16 04:14:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 542261f5-7c0c-3216-bab7-7cb9b0710b72 | -7.03801 | -42.04037 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f0cc1105-cb76-3e32-be80-5f62d5734e4e | -9.77894 | -46.48861 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 85f3778c-f85a-30f9-ab2b-debe71eec671 | -7.08674 | -42.09816 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ab150e01-64a8-3a09-8f33-6a0ed9f926e3 | -5.17081 | -39.74342 | 2026-09-16 04:14:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 178c5124-ed21-3f9c-bd72-5df89eb6a0b2 | -5.64142 | -40.861 | 2026-09-16 04:14:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9114cd73-85a3-34eb-9257-abbc4dced7b0 | -7.33946 | -44.48135 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d100b50-9a4b-3588-8883-74eaeebc0a82 | -6.36534 | -55.82993 | 2026-09-16 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98da559f-7fe3-308f-82a4-e71865639111 | -10.84284 | -46.20168 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53c123bb-37d0-3019-83cb-87c8b4597bd8 | -2.95566 | -50.40374 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5344b1de-93b4-3309-8d2f-f31434beaa13 | -5.77692 | -45.08966 | 2026-09-16 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1a48638-5762-3331-a61a-9778bf54b8a4 | -6.95755 | -44.5551 | 2026-09-16 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 644997e1-e290-39e1-a933-2245b33ff956 | -7.11542 | -42.08852 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c32bdaa8-cd4c-30f0-be8a-52396d44f2ea | -3.37977 | -50.83868 | 2026-09-16 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 08e0ef7f-4f4c-3083-b368-c31cd38fd38f | -7.17725 | -46.12453 | 2026-09-16 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 107cc2a5-6c33-3c7d-bc8a-5a09451592b4 | -4.3903 | -43.31707 | 2026-09-16 04:14:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15dc54db-f5f0-3a96-bcb6-5d2e3cdf7aa3 | -3.21465 | -48.78665 | 2026-09-16 04:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db3c533d-9fbb-3e89-968d-062abaf1f88f | -9.84165 | -48.35936 | 2026-09-16 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68182b6b-6ad5-3e25-ad4a-59dedb55c98d | -3.75744 | -51.14583 | 2026-09-16 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbc7166d-204f-3098-8d22-59d3c2b21a3a | -9.81585 | -48.91214 | 2026-09-16 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c315af88-29cb-3820-89d5-b0ff16a36955 | -9.55128 | -45.42271 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0428d2a-6c33-3e59-8a4c-0de194785857 | -7.17116 | -42.10099 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2b423867-ce8b-38e8-8071-1f64ca8d7bda | -9.09389 | -45.72133 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bc4aa17f-cb43-3e6f-aedb-ad6f7b635276 | -8.6222 | -44.48836 | 2026-09-16 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd72dd15-863f-3999-8231-7e23730235cc | -2.95626 | -50.40025 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| febee8b8-f529-3d0b-ad05-ab7bb8953aa1 | -9.69762 | -52.01591 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 330f4756-6f76-3631-b1ad-dc2ff1dea8b7 | -7.09151 | -41.83276 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5e831a00-788d-3c45-b9d5-6270b528d911 | -10.40539 | -48.66617 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bde88ef-a43c-376c-9cca-eeedff908056 | -6.19236 | -44.02984 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 394df0c1-9cbb-375d-8c91-9a3c91913183 | -9.85427 | -48.36205 | 2026-09-16 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c832b8af-e842-3d98-9e4f-e8a026f79bae | -5.10044 | -47.62153 | 2026-09-16 04:14:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29338973-7179-3702-8877-5e8ec3f08996 | -4.00018 | -44.82587 | 2026-09-16 04:14:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e46f42f-5999-3b9d-bcf5-7e39ffb7cd81 | -4.29883 | -49.1048 | 2026-09-16 04:14:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80b627b4-81bb-321a-80e8-2fdcf633b5b4 | -9.76429 | -46.10106 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b77a39d-7a1e-32aa-9489-d4353f6c321a | -8.39968 | -42.21565 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0a4cda0d-2f16-32df-92f6-8ee8e5016f00 | -7.43303 | -45.49846 | 2026-09-16 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 231845fa-42b8-3994-a131-be3173026efa | -5.53446 | -43.37809 | 2026-09-16 04:14:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5ec7f0a-1d2d-312c-9ebf-2ec178ef1f2e | -6.9582 | -44.55114 | 2026-09-16 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e38883a9-0df7-324d-a9f5-4cc80815fce9 | -7.03415 | -42.04331 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f976bd70-5063-3240-98bb-350cec471fb9 | -9.85865 | -49.82381 | 2026-09-16 04:14:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a4b6f15-310f-307d-9780-bfd69af52970 | -6.32565 | -44.09859 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55fbd6a2-ef90-33a0-8e09-53edce3ff1ed | -7.54405 | -42.66007 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 414e76fe-442c-3924-9e17-a70bc4782e67 | -10.11183 | -45.57785 | 2026-09-16 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fe9ac98-8fda-3ad4-a681-390c3d5f4a85 | -10.40353 | -48.64191 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 251b5eac-5252-3317-9e7d-cbd0467e0e19 | -7.16785 | -42.10047 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bf409dc9-3a49-3726-b31c-d0f76ca9a830 | -7.15737 | -44.24475 | 2026-09-16 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f72dfb8f-c619-37de-a9f0-222ee90e765e | -6.94237 | -42.57769 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9803bc10-1108-39a6-8219-1f42664efeca | -7.03746 | -42.04383 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 17b3b941-2bbc-3eaf-a319-bd99edeaf701 | -8.39361 | -42.21112 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cfae3cf8-c3fd-3fa4-a153-fa1b74454eed | -9.4822 | -45.44038 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c068334f-43df-3f5f-9f30-17284e37484c | -7.46112 | -46.14925 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2deff811-ffdc-3c50-bc02-e129ee28ef86 | -9.8048 | -48.92353 | 2026-09-16 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52193c0c-aadf-368d-8b87-79566429bf01 | -2.90092 | -50.4238 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a115517-802e-38cb-a904-8f090eb53211 | -11.13753 | -40.48188 | 2026-09-16 04:14:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 2c889ee5-554a-3cf9-94d4-277bd7115053 | -9.57033 | -46.59475 | 2026-09-16 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1299bfdf-567f-3e8a-926f-787b14357767 | -6.34339 | -55.56316 | 2026-09-16 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cb4ce45-3c72-3818-89a8-73c446c852cb | -7.29883 | -42.36665 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74ab0522-5379-3b0a-be66-2fb575fe538e | -5.62868 | -40.8554 | 2026-09-16 04:14:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 674b4672-aa8f-3110-9494-19c878b76a33 | -5.10478 | -47.62233 | 2026-09-16 04:14:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 75946640-18f0-3c76-9542-89ea880f7e49 | -3.07969 | -50.57204 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d8d8913f-99a8-3c0d-80a0-3cf942f6b761 | -11.23041 | -43.46781 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be9dddd3-16df-30fe-844f-6ef8df76bc52 | -8.79634 | -46.89855 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12ec5610-355c-3edc-98ef-fe34ee798cf1 | -8.0094 | -38.338 | 2026-09-16 04:14:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0fb4600-7296-39c7-bead-f34c39c0c7ab | -7.51444 | -47.33223 | 2026-09-16 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cbc3698-8e92-3acb-83ae-1685ff3a92a0 | -5.76885 | -45.09287 | 2026-09-16 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 703e886a-aca8-307a-b77c-9e94a2a2a4c0 | -5.99663 | -46.63345 | 2026-09-16 04:14:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4485a95c-ee7b-3827-9ce0-335cbfd161d2 | -3.21553 | -48.78127 | 2026-09-16 04:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5314220d-9e8a-3a29-8aa0-8d7c15d64e9e | -9.10411 | -45.72741 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a5ab5ebc-70a6-34c1-9100-7b88d57d3d78 | -6.11064 | -46.10093 | 2026-09-16 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3dccac66-b3cf-37b9-91f8-af5f39d6f1e5 | -7.08691 | -47.49279 | 2026-09-16 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfc86784-ccfe-30c6-bea4-fe6a48f28055 | -9.22884 | -46.70414 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aa60dac7-d418-3923-84a0-28ad76efb493 | -10.10247 | -45.56792 | 2026-09-16 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3716309-bd2d-3be6-b569-58793d99547e | -9.76032 | -46.57608 | 2026-09-16 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2f0ee28a-5297-3182-b023-69bfe45c6799 | -6.38001 | -43.85237 | 2026-09-16 04:14:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a4714a7-36b5-3e4c-a511-d6d368f3c993 | -2.91611 | -50.43377 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 251ea619-2df1-3856-b6d4-049b3f533b9f | -10.4099 | -48.65547 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e959a34-a145-35f8-9a59-c15a90b90bd1 | -6.31389 | -41.68026 | 2026-09-16 04:14:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a5dc9be2-fb52-3397-8f2d-6a4be6fee359 | -3.07429 | -51.20137 | 2026-09-16 04:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c65f2671-92a3-3ad0-ae21-1e88a311edbd | -6.78605 | -41.46501 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a95c04a3-6ae3-3796-8da0-039a59beba61 | -7.5455 | -44.88194 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README22.md)
