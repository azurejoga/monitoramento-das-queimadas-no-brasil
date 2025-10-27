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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5b27ae2-ec27-366a-814d-9b91c064aa6c | -1.35722 | -49.16728 | 2025-10-27 04:29:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25625fbc-f03c-3d88-932d-401cf57987a4 | -1.75129 | -46.53848 | 2025-10-27 04:29:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 015800cf-55e0-3141-afdf-b6d2af1535c6 | 1.14137 | -51.069 | 2025-10-27 04:29:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db338faf-e322-33c0-87fa-a5c79a96f7ef | -1.23766 | -49.35412 | 2025-10-27 04:29:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b17b3629-2d1e-3989-8cd5-72984379e840 | -4.4618 | -43.4248 | 2025-10-27 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| c49394ee-2259-3d41-8edb-73ad1c8e4f81 | -15.5132 | -49.9958 | 2025-10-27 04:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d79b791e-6d26-37a5-8138-55007e085c4c | -7.8413 | -46.4423 | 2025-10-27 04:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| b0633d5c-ea4b-3b43-83cf-fb517b49387e | -10.3594 | -47.18 | 2025-10-27 04:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 3fc8b465-702f-3b06-89ec-372b89a166c7 | -4.4665 | -45.4589 | 2025-10-27 04:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 116818b3-ee52-3cdd-a21c-5100ab05b3a9 | -7.8408 | -46.487 | 2025-10-27 04:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 4f2e5437-cf41-3a55-98a9-6467d77ce66f | -7.8223 | -46.4664 | 2025-10-27 04:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 55f3dc58-e1e1-39e2-a6c1-99078895f30d | -7.822 | -46.4887 | 2025-10-27 04:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 9e9b2420-61e1-3a94-b9c1-cf6cfbd26a80 | -4.4805 | -43.4237 | 2025-10-27 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 19bd05eb-0488-35c4-ad0a-61f81a329c02 | -4.4807 | -43.4005 | 2025-10-27 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 598b0bf5-bfd1-3b8c-951b-b635d6620c2e | -4.448 | -45.4374 | 2025-10-27 04:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 3435c31c-2184-35f9-8d18-6b71067d28ed | -15.5128 | -50.0178 | 2025-10-27 04:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| a03bfe9c-324a-3b4b-a4aa-b9da358ff780 | -7.8411 | -46.4646 | 2025-10-27 04:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| b157ba9b-7626-38bb-961d-f163016fefa7 | -4.4479 | -45.4599 | 2025-10-27 04:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| a679cc8a-0348-3094-bdff-eef9aa143a87 | -7.43417 | -41.87012 | 2025-10-27 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| bcc55e21-bce4-37b7-bf9b-bd379c88a420 | -7.92124 | -45.6568 | 2025-10-27 04:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a6a2e35-e81e-3204-b10b-a159d1b706ab | -7.34023 | -48.4875 | 2025-10-27 04:32:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ac37ae4-1a63-3e68-b839-cd2cb0163173 | -7.33434 | -44.02753 | 2025-10-27 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5c25b87-1936-3967-af53-672e20c992f5 | -9.13197 | -45.8597 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bbdd9f1f-486a-3616-a651-cc719b276a7f | -8.88247 | -44.84153 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e66e46c7-a309-3728-84bf-300ec3f7996f | -9.57199 | -46.89935 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d3ae95b-1f31-343b-aaf8-241e7894229f | -6.89149 | -45.15299 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1143cde-d1fc-319c-91c2-896d0e9142e9 | -9.72888 | -45.42222 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86a022cb-3887-32f6-a800-b58577465959 | -3.47296 | -41.3083 | 2025-10-27 04:32:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9d3efcd2-c06f-3788-aabc-0823ff8af446 | -5.24782 | -44.8632 | 2025-10-27 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 771d91f8-891e-304c-bd81-250d874562ab | -7.34422 | -42.43983 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 21f15b3d-f79f-3975-ab10-432138867b34 | -6.59492 | -42.67109 | 2025-10-27 04:32:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e27883b1-782a-3613-bb3f-372bb0c922be | -8.89081 | -47.99664 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5db62e16-b1d1-3165-8e28-315d6d36457e | -8.86566 | -44.97906 | 2025-10-27 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a933c101-4871-3e59-992d-a72682e895b1 | -4.57199 | -49.81329 | 2025-10-27 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e01bd1d-cf11-3f4d-88d3-c4b60dac3b6c | -5.52914 | -41.71342 | 2025-10-27 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 52f09a7d-b03d-3b56-b727-54e69463d263 | -6.29289 | -43.81414 | 2025-10-27 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a15ba953-e53c-34cb-b4af-e340c8e52215 | -4.86985 | -48.65442 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa925703-de46-3e77-8600-89d8cf84a10e | -3.73859 | -51.64574 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 598a6f7b-f60f-3f24-92c9-305a23350537 | -9.56871 | -46.92111 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf76b9c1-6f80-3990-b48e-dc9bf38a159d | -8.30848 | -46.18464 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b9ec2cc2-1021-34e5-8e2b-684d38deed45 | -3.94797 | -49.01548 | 2025-10-27 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdd117c7-ebab-3bf7-892a-29df291202e0 | -10.01801 | -45.00471 | 2025-10-27 04:32:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0f417ca-ec27-3775-81a1-7bdac5103def | -9.21981 | -45.60985 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e88c7976-ab1d-30b9-8a0c-c413f4c882c6 | -9.14004 | -51.3043 | 2025-10-27 04:32:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 0d48a916-9a25-3f0b-b974-b8e3ad58562a | -4.46486 | -43.4214 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8053ffaa-555c-32a9-9cf2-b035bfb39244 | -6.09953 | -41.77702 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7b4e4004-b198-3168-ae2f-4072691cf5ba | -6.14086 | -41.81781 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 09bc4754-1278-39a6-a4cc-5f4ef7c617b3 | -3.98546 | -49.28662 | 2025-10-27 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71a26bf3-7fe5-314e-b596-2736d1aa36b7 | -2.69694 | -48.46712 | 2025-10-27 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1f91da3-ce59-3a64-a2cc-7e548866d03a | -7.53001 | -46.25376 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dba45e6d-70df-3ac9-bc59-3b59172156b7 | -7.55222 | -42.52692 | 2025-10-27 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 05ffbe53-40f2-3ad1-9399-362fd12e7ebd | -7.81443 | -45.39748 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 233ea63e-951c-384f-a5d9-98446cddc7cf | -2.95887 | -49.18266 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f617923-60a0-3390-9bfc-e2f9eedcb123 | -2.23147 | -51.99562 | 2025-10-27 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcb9437b-0855-3e22-90c0-a5a4708ef251 | -10.01462 | -47.16739 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98c7560b-5e89-3016-a1ea-d6f813e2b6f2 | -3.9453 | -48.08718 | 2025-10-27 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f5862fd-f327-3c2b-a9e2-00220b50e121 | -7.42137 | -46.39003 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed6b1db8-9a42-3163-9d62-3aa81aecd6ca | -4.35794 | -48.66461 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b9be60f-ed61-3aa7-802b-279f934a7c99 | -6.17908 | -49.87072 | 2025-10-27 04:32:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4188067f-306c-3e0a-a8b7-9105c4bb4532 | -9.98835 | -47.18184 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ed648df-b27f-3307-b355-9f94204ecaf6 | -5.65473 | -51.10048 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79f38390-0599-36a7-9891-8b644fba3a55 | -8.69618 | -44.42983 | 2025-10-27 04:32:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0706333d-85d3-3449-b50a-862fe868b011 | -4.22291 | -48.35641 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dce5617-76f3-3ea8-abc9-90229261e777 | -6.86382 | -43.80297 | 2025-10-27 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18c7fee5-9841-30a6-b669-5cf568bd417b | -3.27101 | -50.05166 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ce2fda2-a946-332a-bac2-de20e560e81a | -7.84917 | -46.4146 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9ebd256a-cf0e-3684-9b95-f60b2dc98b22 | -4.46284 | -43.43499 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6839445-941b-3832-98b8-3fbaa0696ecd | -9.9878 | -47.18544 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b33da35-3d03-3cc2-9666-9b6f36e1f016 | -6.54841 | -41.6081 | 2025-10-27 04:32:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 24b8218e-4a98-3ffa-a89a-6d2d8ee8d732 | -7.33793 | -42.45421 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8e95435a-60c5-3d48-be86-fb0327fa9499 | -6.43304 | -42.03963 | 2025-10-27 04:32:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 46c1f239-1ed3-3e5d-8ef0-0e6b3952ee13 | -3.43255 | -50.10467 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ceb23aa-b11f-372f-9d4b-4767bfab3363 | -4.51713 | -44.04661 | 2025-10-27 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da26b2f7-9fc5-3f6d-8713-3dabbb996915 | -7.85771 | -46.4493 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eeca8a22-3c32-3571-afee-dd286c70bf74 | -3.14099 | -50.16283 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d391c9f7-e664-3031-81e1-4db9c712b163 | -6.10344 | -41.7754 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0790827c-f185-38aa-974e-886b32b8a9b7 | -6.61852 | -44.6372 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0170ff24-ee7e-3e4b-a0b1-62a5ba72c2ea | -7.2488 | -46.95969 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e243bd7e-58e1-3025-bfcd-33b90b6984ab | -4.90516 | -42.99223 | 2025-10-27 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54d39d26-b722-3e6d-a295-d32a4f13f756 | -7.96623 | -38.28391 | 2025-10-27 04:32:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bf412ab1-b7f7-3aa4-9a61-7d1421773568 | -4.45553 | -43.66156 | 2025-10-27 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d8af5cb-2b39-35de-be7e-bfec01c41ff6 | -3.97836 | -55.74711 | 2025-10-27 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b35a3668-f4b0-3a71-a9f6-74874c404b65 | -8.65352 | -47.2425 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d1b5af5-54de-3d71-868c-f0f622848738 | -4.48358 | -43.42437 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c254876a-79f7-3364-a2be-9f7a119902eb | -7.16693 | -44.85993 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70e02237-764c-3212-8414-d86632c6a453 | -9.60327 | -45.48848 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0436aa63-9673-3c37-a831-b1fa43594d84 | -7.339 | -42.44672 | 2025-10-27 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6d4a2956-afd4-3f44-9f32-e558df4bce8b | -1.38542 | -55.3472 | 2025-10-27 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3b5901a-af70-3ecc-aa38-9ce6af2a1744 | -7.96254 | -45.47506 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 61ce4932-08dd-39a3-ab37-1069f9636069 | -6.30903 | -44.73991 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5974916-a202-35f0-9ab5-5c3013a4784e | -7.86094 | -45.37918 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9dfa1a3d-d2db-370e-8a00-fda9dc2a7b27 | -7.87695 | -47.25152 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5695da9-540a-3c6c-b30c-b9a9c296b5c4 | -4.9595 | -44.87348 | 2025-10-27 04:32:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a819153-5320-3a6b-9ec3-6c94a67482d7 | -8.94902 | -47.17964 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5555fd5-fa68-3bea-b662-42721751abb2 | -7.83003 | -46.42659 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1ae219d9-065a-319e-aa45-fc27a378c4f1 | -6.63776 | -44.63172 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2534fc53-2bd9-3d6c-b63a-d1c909660aa8 | -9.13488 | -45.86412 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 884dd909-2470-302d-af30-ca4cd1060638 | -7.85029 | -46.40726 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57345144-7758-35a9-917e-501ec058fd3f | -9.33723 | -46.95645 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdd62ea9-e293-31b0-9fbc-54b343766bf4 | -7.4245 | -47.79951 | 2025-10-27 04:32:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
