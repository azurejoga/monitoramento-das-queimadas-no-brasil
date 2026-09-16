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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4158d9e2-84b7-3afd-b2fb-1b6b625ad42c | -6.77102 | -58.80235 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bd6d1a79-71e9-354a-bf0c-557014b303fb | -3.26434 | -54.5241 | 2026-09-16 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 958d022a-1d95-37e0-b403-11b9ff5c379e | -1.61139 | -55.56758 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c61554d0-a84e-3f6c-9580-2389d460413f | -5.83427 | -52.09299 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9327b631-72fc-3ccd-8d3d-7de1d40381db | -6.36675 | -55.13145 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b0fdc19-570b-31a9-b96e-32ec3e0c4a66 | -6.71553 | -58.80322 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 892d3a4b-866c-396a-96fb-60b1b522a1d5 | -3.83559 | -55.86452 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1692d15-dd5b-3a53-8c3f-5da4e7b417cc | -1.74342 | -55.26175 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adb24677-19a7-3173-a881-cb8203db0a67 | -6.62958 | -55.12681 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 836e46f5-44ea-3713-9011-fa0aaf98ccce | -5.11959 | -55.93835 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23325cbe-112d-3ea2-afc2-61292abb5789 | -6.95835 | -44.55066 | 2026-09-16 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1cbd231b-b1e7-3467-aa66-3ae52da7512c | -6.17022 | -53.27068 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4d69bb5-479e-363d-a728-fb48d220cb51 | -5.86073 | -52.03519 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 999dd789-04f8-3183-9ca5-e400d3f546c5 | -6.76639 | -58.80653 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c1ed9d58-d59f-3b03-b08c-40337dc178f1 | -3.01726 | -51.34412 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2f901f50-4ab5-3f1b-adec-d995d294ee9f | -6.29218 | -59.95997 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6804f253-88dc-3416-a3be-921281f0576d | -4.37506 | -55.03198 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3eb9e6e5-e3bc-3501-a3ac-abec828a2934 | -6.15461 | -57.69474 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ddc1c33-6002-38fb-be5b-596ed9f71f8c | -2.91381 | -50.43502 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9181aa92-0c31-31f4-af0a-f739754338f7 | -3.37084 | -61.32973 | 2026-09-16 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd5cc53e-e103-330e-a629-bc373fbb20a1 | -5.82164 | -52.08329 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c74511d-cc83-3040-9243-fa1c98096b95 | -6.339 | -62.69045 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ca5653f-71ec-3ca2-a840-2b1cae120fa6 | -2.89876 | -50.43699 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3149adb9-ef31-3cb0-9ee5-e33d074a8a95 | -8.84456 | -44.90512 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7fb438f5-c392-33fd-ad47-6eac4332845e | -3.60007 | -59.06397 | 2026-09-16 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 856cb5da-1382-3b17-ba80-b164011c50cf | -5.89504 | -51.64515 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc58e9ef-b9dd-3508-981e-92449a776d06 | -3.70423 | -60.6211 | 2026-09-16 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23e3f58d-1296-3594-bcc6-d2d969a1c1e6 | -2.91444 | -50.43089 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 731a3047-4d93-3a81-911e-4c3a2a2e25eb | -8.8533 | -44.9014 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3039b46-a83e-39c2-bfa7-6913e8926184 | -5.88307 | -52.09188 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e2a6222a-91da-3132-8403-cbde83f12f42 | -7.8766 | -54.72496 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0689d3dc-9da5-36a4-903b-e04556bb10dc | -2.90362 | -50.42924 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c26ed21-72c7-32a1-afc8-99086d91fdcb | -5.98253 | -46.63593 | 2026-09-16 04:57:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 06f30e46-7b6c-37e6-9abb-02d0920749ff | -9.23816 | -46.69575 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54155963-751f-3e8c-8803-dd2fbf7cfec9 | -2.09905 | -52.04659 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 696e9a5e-6af7-3587-ba7f-7171a2db487b | -2.91651 | -50.39296 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f28c0c3d-4797-3a9c-9894-0e706430687f | -8.32907 | -51.30863 | 2026-09-16 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 42233b75-c276-3dc4-93b8-d4ed88419825 | -6.3687 | -55.83191 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a20b65d4-a946-3f9e-b8ef-71ea689bc3b5 | -6.77173 | -58.80992 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd89a30e-da38-3c5f-b1f4-3fec33463e5c | -5.1344 | -55.93307 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b129aa1-dd05-381b-86d7-9ecb381a7b15 | -3.84874 | -49.05767 | 2026-09-16 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 114738f7-a649-3aef-8678-b24046a3b6b2 | -5.12525 | -55.94669 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 141a1952-a059-3da8-b84d-159fa5f52eb1 | -6.32699 | -55.25421 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6d846b2-423f-33d2-96d8-bb3341a82854 | -3.5783 | -55.55925 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05a6b639-3f42-352b-9a08-d3a47dd8a66b | -7.68493 | -55.05619 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2e6a23d-0b0d-349c-a8ed-662f062fe7b4 | -3.48098 | -54.68291 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f140600-d39c-3457-a9f8-f9d575dabf48 | -4.72313 | -55.73687 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92d19e75-a942-3ff7-91f5-0dc216d89b54 | -5.97347 | -55.36016 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fdb4f57-4351-35ff-ac77-83c021a02e33 | -3.3717 | -61.3245 | 2026-09-16 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 451b6189-c55f-309b-852e-e77549a53ddb | -7.6445 | -45.83819 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46b037a9-e245-34d2-bf55-02eea838f684 | -4.20003 | -47.89147 | 2026-09-16 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 444c9062-7d9e-3f90-b373-905aae3f308e | -5.39263 | -49.08159 | 2026-09-16 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e14a714b-403a-3d06-804d-982a90f82238 | -5.14805 | -55.9351 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b4990fe7-3723-3c68-bec0-a8afc36c4b11 | -5.86469 | -52.12447 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 909c04f7-47a1-3d86-b3b1-4d811c5eb305 | -7.27526 | -48.34919 | 2026-09-16 04:57:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41be626d-5704-3d70-ba57-a456b67d6b42 | -8.84676 | -44.9074 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1cc56567-8d1b-3bc9-b683-d6a192ff0cb4 | -7.36068 | -44.49721 | 2026-09-16 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0866790e-f550-38db-8e6c-499a074eff13 | -9.34028 | -44.39002 | 2026-09-16 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 11a23705-e3a1-3a3e-93e8-5d2fd57e960c | -6.15022 | -52.7812 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99c69fb8-351a-3031-867b-0abeb28ef7b8 | -3.1744 | -58.6495 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 579d550a-2c29-3616-b149-5a15e77abf21 | -6.28962 | -59.92437 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaff891d-726b-32b8-815d-02b33fe2f489 | -2.90646 | -54.85332 | 2026-09-16 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 125a2310-4783-3ca8-8218-0be6810199a8 | -2.88747 | -50.41401 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4cfb5c2-a323-322c-adbf-0008e223d72c | -7.07599 | -45.24221 | 2026-09-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b28ace5-a0ea-371f-99c8-d0d337235245 | -4.57074 | -54.91476 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fa22c69-c810-3fa4-a557-0e579f05549e | -5.14818 | -47.60221 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f81c43a-4b21-3c35-84ec-c6582511f1d8 | -4.57516 | -54.90835 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70c99952-0a73-3c20-84ef-8c7102922137 | -8.5458 | -44.49778 | 2026-09-16 04:57:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82728bd6-9340-3ffb-960c-1a258213ab01 | -4.29979 | -49.12367 | 2026-09-16 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cde0d013-d8f2-3992-be46-733bcb9fed0e | -3.09755 | -52.21048 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55cabb0d-f83e-3af6-9154-8aa98b07aa82 | -1.61832 | -55.56863 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a32ee0b0-6eed-332a-a1af-dbe4e5001399 | -1.28408 | -55.71082 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b9342bf1-f24b-32e9-98d9-8511db5656e3 | -4.51364 | -54.97412 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a24a01e-4aa5-3806-9f15-659f06de9f4b | -4.46248 | -55.05996 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da91b208-7c2c-34ab-b205-1750e4749a5f | -2.91335 | -50.41375 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03a50d6f-2b15-3f80-837b-c68357567e03 | -4.44114 | -55.52116 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed9a683b-71be-3919-b09f-a59868507c8f | -1.79316 | -47.83614 | 2026-09-16 04:57:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e42381f-b91d-33c8-9b5c-58fb13fa342e | -3.38121 | -50.83812 | 2026-09-16 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ea18a094-aa77-3e09-86ce-9f82edb45d71 | -4.84062 | -55.77046 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da1e3e46-2949-38f8-9b6b-c8b23d505e8d | -8.85622 | -44.90377 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d25ac94a-0938-3bf9-8f96-661e521ff8b1 | -9.49052 | -45.43767 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3c1bd2c-2746-3dbb-aa64-0ab3fd2fb786 | -9.48874 | -45.45133 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 466dfaa6-e11f-3289-b3e2-9bf185793e60 | -3.37767 | -50.83755 | 2026-09-16 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 24f77efd-cdc0-3cf0-b3b7-955eb119cfaa | -7.35445 | -44.50052 | 2026-09-16 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5273904b-f22c-3a3d-b5b5-98451ec15ef7 | -2.57852 | -55.9959 | 2026-09-16 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e208fa34-07e3-3a4f-8a9b-572477109024 | -3.07504 | -51.20046 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c0042b7-07b6-3eda-a44f-b8394b44906e | -8.30325 | -50.71469 | 2026-09-16 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65536af5-9aa9-3d9e-9913-2e864c8df324 | -6.75712 | -58.8149 | 2026-09-16 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45c40950-0d62-3c1d-840e-324f4ee11fb9 | -6.78581 | -47.87284 | 2026-09-16 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6e58dda-9c95-38d5-a9cf-f18f5aff3a9c | -3.12353 | -61.25053 | 2026-09-16 04:57:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8a260c89-4e04-36f9-91b3-d7c6febdc4a8 | -4.56742 | -54.91423 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94784b27-0a66-37a7-855e-b7d4bebe2a31 | -5.14862 | -55.93145 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 818ae240-4eec-33be-8a10-d82ea201ff34 | -4.60218 | -48.5101 | 2026-09-16 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08685eea-2c54-3d08-b59d-d681a4805d2b | -3.02535 | -51.33766 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c93f5ee1-d8a2-3210-978b-626881c30d00 | -5.15261 | -55.9283 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 72d8a541-c6d8-36e9-9da8-3bc400f6690d | -6.78573 | -48.65698 | 2026-09-16 04:57:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 615b04b9-f563-330a-a7c8-c3d29b8b5c87 | -5.99288 | -52.10795 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 349c4e04-122c-342b-8e0b-e759e2251b10 | -3.3753 | -59.53267 | 2026-09-16 04:57:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 184068a6-14d4-3a70-908d-39356679b8d1 | -8.11891 | -54.80559 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e27701db-1a4a-3b3e-8752-91e4892a1d61 | -8.86096 | -44.91164 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README37.md)
