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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4e12532-8ac5-3b33-8521-176cb4456fd0 | -3.41413 | -39.28224 | 2026-09-19 04:00:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9adab324-5ddb-347c-94ae-85f94a8ed73b | -2.29553 | -47.88643 | 2026-09-19 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 216f6453-87c6-3a46-8b77-36c81b11f7c4 | -1.21872 | -47.71622 | 2026-09-19 04:00:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97a56125-8007-3718-9cc4-d5040ff289df | 1.13895 | -50.99472 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d57f8d6d-0daa-3566-bcf0-c508ec52e3e1 | 1.21949 | -51.00491 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 36020a6f-c19a-3370-8774-d37d79452e8d | -1.41763 | -49.42699 | 2026-09-19 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c00de657-bd21-309f-bdc4-855e70d75671 | 1.25595 | -50.97595 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7bf823ba-26ae-3dd1-bfa8-1ad6789a71ce | -2.14526 | -50.90609 | 2026-09-19 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e42a8d08-a11a-38c1-9d18-01a705aa38f9 | 1.24928 | -50.97691 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9d9f39f0-2570-385b-9ea5-a697a3ae2af5 | -3.49396 | -43.31441 | 2026-09-19 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f398ace-d28f-3e0b-a2c4-984db6dd9da2 | 1.22254 | -51.00616 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ea4170ec-9bf3-3971-b9f6-e7ed28bc5e66 | -4.02614 | -38.49396 | 2026-09-19 04:00:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d6f1ccfd-d32d-3118-bbc9-bdce7a4bf7ad | 1.22036 | -51.01066 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 83e7a5f5-2b82-396e-a38d-5da1fb4ff940 | -3.49469 | -43.30993 | 2026-09-19 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 325ed0d3-9eb5-3026-9688-4dd8ec16f509 | -2.39223 | -48.52478 | 2026-09-19 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b614307-0588-3a8c-81c4-168ad15d305b | -1.42346 | -49.42785 | 2026-09-19 04:00:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73339936-fb2c-3b78-9ddf-236785f8c08c | -2.29167 | -47.88685 | 2026-09-19 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4dbfa58-0e6c-37f4-aefe-01b6a3996c3f | -2.02882 | -48.77687 | 2026-09-19 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e7d5f8d8-efab-36d4-9bd2-bc2fd1203b39 | -2.39278 | -48.52135 | 2026-09-19 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e41dd1f-5b2a-3a88-b63b-fd703699c28b | 1.21678 | -51.01286 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 90c2da3a-3f63-3a19-8113-6ac3decc994c | -2.02824 | -48.78052 | 2026-09-19 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ae3b5b3-4f36-310f-821e-c76e270fc501 | 1.22162 | -51.00036 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 66484277-a2f3-3520-86af-2919da6108da | -9.95125 | -46.5449 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28fa502e-ecf9-3910-835b-eae05684aaeb | -6.99423 | -42.17174 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e0fbc912-5f9a-320c-81ac-4893cb8e03ab | -7.87312 | -46.43926 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17cc3db6-171c-3d1e-8a4b-f5e060f1a43c | -2.82869 | -50.46237 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 5ecbe4ab-b7a7-3b17-9ebd-abe38084b68a | -7.82893 | -44.97411 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e93a45ca-6e18-317a-9f7f-f4da2b99ca39 | -7.19228 | -50.82789 | 2026-09-19 04:02:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef89572e-9569-37fd-ac8f-f8e7b6ede640 | -9.78403 | -45.04346 | 2026-09-19 04:02:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba83e8ba-a6aa-3518-8853-69b73a7ea406 | -8.33874 | -50.74922 | 2026-09-19 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1361833b-23b9-3985-b107-bee55608644d | -6.91099 | -41.70718 | 2026-09-19 04:02:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3807c2ac-c990-3581-b1d1-c3180508e54b | -7.61006 | -45.4355 | 2026-09-19 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42974c51-8d5b-3818-a15a-7c4ecf081dec | -11.22452 | -42.82488 | 2026-09-19 04:02:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 9ddd8c32-2872-37d5-9d22-1e1af5bfd64d | -9.78776 | -48.34073 | 2026-09-19 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5ed03cb6-0b2b-3d2b-ab37-46fefef8fa12 | -8.37047 | -45.66138 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abb8aec3-50c9-3c78-b14e-c2abfed56c8c | -10.54481 | -46.59181 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e33dbc6a-b499-3786-b303-569f1c15d0b5 | -10.20384 | -46.58987 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5d651b2-05d6-3aae-8404-0c03200f3952 | -3.37491 | -50.44297 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71e6ab67-f415-3dfd-bf46-c5ad7d96b8d6 | -9.23597 | -46.20392 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 28cc9c93-8ae8-3993-a5ed-97e8161309e2 | -7.0548 | -42.05951 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 253a554c-6311-315e-9e58-fc9d614dd864 | -8.37471 | -47.24977 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22835d76-58b9-3cce-80b9-7ecd8b40baa0 | -9.95754 | -46.55809 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 343c8f69-164f-3179-926e-e68275fad4f1 | -6.2756 | -41.6589 | 2026-09-19 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f179c511-bcb4-35c2-a7ea-e0f9b82cce10 | -3.23146 | -46.94349 | 2026-09-19 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c3d7a3b5-9aed-3519-90e0-2f94b76ee265 | -10.13455 | -45.57093 | 2026-09-19 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd566326-6623-3111-8269-2319bd12ee33 | -7.85686 | -44.87794 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 97612019-21b1-3488-908b-d27a85e34716 | -4.85611 | -48.30098 | 2026-09-19 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50a60277-c61d-33b1-8b82-8a9527001bcb | -10.12446 | -45.55948 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 75a885eb-243f-366d-bb01-d0f20f7b88df | -10.58953 | -46.60388 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1aac7a9f-20b4-3a06-a82f-f2b545b1d250 | -7.78083 | -44.88076 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eae397ee-c1c3-3562-94d4-bd61c61aa321 | -10.48289 | -46.30185 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e521698-a4c9-345f-a4cd-9d2cce5da683 | -5.8262 | -47.77878 | 2026-09-19 04:02:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59461590-2dd6-391e-9c14-89ddad26063e | -7.39959 | -49.84836 | 2026-09-19 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 853ba805-6cde-35e4-b071-bb21c616b37e | -7.8681 | -46.44283 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a481153-63ba-30c2-a9cd-127d3b95103d | -8.37577 | -47.21761 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ad5c516-4ba3-306d-a853-8aac1ad706d8 | -5.62181 | -45.24891 | 2026-09-19 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3923f9f-73de-34b0-a9c4-1132b75f8a34 | -2.82101 | -50.47066 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 48389e3e-480c-3e96-9848-0549517dfe79 | -9.97294 | -50.27231 | 2026-09-19 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7302f4b7-6f2e-3862-bcb8-aca7232b8b74 | -2.82034 | -50.46818 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b0c2c5b0-26e6-3913-a8fd-ce483073a766 | -9.81393 | -46.4008 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a10ea46a-718b-361c-9819-ecacff8a7fd5 | -2.73607 | -49.46362 | 2026-09-19 04:02:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ac6b1479-6f28-34a3-b91e-1600749974a0 | -10.53234 | -46.73449 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 293c9fce-d18a-3e33-acf1-00eabae2d67e | -10.00292 | -50.2783 | 2026-09-19 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6be8fd4-f1b5-3b9a-b0ac-86bdb4b70ad8 | -7.77772 | -44.86741 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4323bc32-a7b4-3de8-aa8b-9bfa6515d8ea | -8.66515 | -45.44497 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e869216-dac1-3af7-8b2f-e474ae15c64e | -10.62936 | -46.05448 | 2026-09-19 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36c47c59-0656-3493-bf1a-a91ebf23c396 | -7.54786 | -45.67755 | 2026-09-19 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5142f860-570d-3b64-a274-7f3f7eff3375 | -9.74951 | -46.08845 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a42a3abb-eef9-3daf-9841-a97114357010 | -7.5288 | -44.93741 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6beb90ef-983a-39f7-aee3-7184e052e8ce | -6.00184 | -51.80135 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 781939d9-e067-3a29-a1f4-1add96a1b4a0 | -10.52535 | -44.84924 | 2026-09-19 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 96aec813-d38b-325a-877f-019481260f31 | -8.36708 | -45.65691 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f5afcc27-cc4c-3312-bf51-2684b9175bdf | -7.60604 | -45.43486 | 2026-09-19 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5fe0662-106a-314b-b772-df31c0abc6db | -6.98782 | -42.18993 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 233ab077-a060-3e0f-a1b3-6358646070ac | -8.38785 | -47.20133 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94b9505c-eed6-30d1-b8c1-f557268863a5 | -3.45749 | -50.61551 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6df4b010-56be-3c2d-96e1-541a4137fe44 | -4.98472 | -45.05773 | 2026-09-19 04:02:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c82bca8e-67d8-3f0a-8e5f-a615359a4af2 | -7.6427 | -46.1087 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 41e55765-3aa0-39f4-8d8a-c80e64e43075 | -8.39083 | -45.63879 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 411fd089-19b3-3ad4-b0a5-b58cf1a9df21 | -8.76798 | -48.67918 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ab2f6cd9-4549-3b59-a252-6135090c5115 | -7.40024 | -49.84478 | 2026-09-19 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 766b8270-70d8-389a-82e5-f095d7fb6d5c | -8.72068 | -44.87052 | 2026-09-19 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08a87bae-f0a4-3f9a-b847-3555cec5ebca | -7.68923 | -46.08838 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12d0ac5c-3322-3eef-8e62-4b08852a2b48 | -7.02278 | -44.65977 | 2026-09-19 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ee6fee81-8290-304a-b182-f9be668f697f | -9.96037 | -46.56657 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f248cd43-369d-3ad3-a3e4-bb54031ea11c | -10.32464 | -45.33753 | 2026-09-19 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66949e08-de57-3979-97f3-4d1ea013b478 | -7.58581 | -43.45088 | 2026-09-19 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d162296-e689-3028-b51c-c76b9bd9dd1e | -9.89148 | -46.54334 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d560638-c6c0-3ce7-8118-e45e9a184af4 | -5.85684 | -51.93931 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4f5547d-222e-3055-90f0-dbc8f937eb4d | -2.8325 | -50.47013 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ee8a8f35-b37e-3b4d-866b-f171856579c5 | -6.9856 | -42.18191 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7ee89e37-352e-3828-a0d3-7e4ccd8b4301 | -9.45994 | -45.43728 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db001c0c-d081-3702-b987-cd9ad86e8ebf | -9.95127 | -45.27343 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d54fff3c-6461-3a64-be30-5e162b72b85e | -9.93044 | -46.59052 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0fb112c-d575-3037-b4f2-e9ed37f8b153 | -10.61025 | -46.09451 | 2026-09-19 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf11791d-c6c9-3f95-9178-85c6301344eb | -10.53355 | -44.84598 | 2026-09-19 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08d674dc-156e-34ba-9577-1ff675ce7161 | -8.36073 | -47.23553 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5d4bf21-ce71-3b68-892c-3cbaf13d5e00 | -7.78446 | -44.83617 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0773745b-e979-3620-b0b3-1a63532065db | -3.52124 | -50.80061 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 142ec301-2466-3226-90ee-cbe42279df19 | -7.19708 | -50.83386 | 2026-09-19 04:02:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README27.md)
