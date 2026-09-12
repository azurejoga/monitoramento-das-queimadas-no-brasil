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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0119f33-9587-379a-b716-1f72593cc901 | -7.2147 | -43.7001 | 2026-09-12 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 4f2d68f2-ee1c-3471-94a3-93bf7f02a274 | -8.5415 | -54.7187 | 2026-09-12 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 3fcda47f-1f51-3eca-a045-49b882c6ca04 | -11.8193 | -46.3633 | 2026-09-12 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| ec2d447e-477f-3910-9ef0-c0663fd58753 | -8.002 | -44.0163 | 2026-09-12 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| c50821dc-0c43-3e49-bbc4-d92d3eba1094 | -12.5969 | -53.9854 | 2026-09-12 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 9722a036-950b-364c-b2bf-8b7b4cbd83a2 | -7.6008 | -46.1288 | 2026-09-12 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 352.1 |
| 507c2f06-d828-346d-9095-ddad9d58ed61 | -7.9645 | -43.9971 | 2026-09-12 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 60af3408-113a-37e3-877b-55dcec2e046f | -10.5664 | -51.356 | 2026-09-12 13:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 9bd16f25-06b3-35ad-84b1-01f5c3595902 | -10.9491 | -48.3474 | 2026-09-12 13:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 869a299e-813d-3f5e-bb3c-f8278412f294 | -10.2933 | -45.2702 | 2026-09-12 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 3f38b2a6-30ae-3819-b6de-4a3be7390b01 | -11.8189 | -46.386 | 2026-09-12 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 7c878e2f-c666-33cd-b61f-ed8ca3ddd265 | -10.2929 | -45.2932 | 2026-09-12 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 17ddc10c-aa51-3b0e-9392-6e9c4d38a899 | -12.1388 | -48.9672 | 2026-09-12 13:20:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| aa96f1e3-5017-3165-8909-4acdadef67d4 | -11.3723 | -46.8299 | 2026-09-12 13:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 00e5bdc2-53f7-3c3f-a96a-99af4cff03bc | -8.2201 | -55.2627 | 2026-09-12 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| bd7f6528-d8a5-39ae-a66a-b0aecf37f03b | -12.1391 | -48.9453 | 2026-09-12 13:20:00 | GOES-19 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 678e6131-5ed8-3625-8e6a-510811104bb2 | -13.5652 | -51.8656 | 2026-09-12 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| da8e646a-89b6-3c5c-a1f3-f13a5db64f9d | -5.7756 | -45.0826 | 2026-09-12 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 0cedcd56-1497-3cba-b01c-8b79a198097b | -11.3727 | -46.8074 | 2026-09-12 13:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 290.4 |
| 9c9f5b61-82a9-33d9-a7a2-307d0c6f0c2b | -6.8755 | -47.4313 | 2026-09-12 13:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 206.7 |
| aba79ddb-4c37-3fa3-9eeb-e92413f19a9a | -9.16566 | -71.84186 | 2026-09-12 13:27:00 | TERRA_M-T | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0df7edb5-c749-3092-a991-aa1e29d7f5eb | -10.27851 | -68.75082 | 2026-09-12 13:27:00 | TERRA_M-T | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bafb9003-62f5-3f82-a1b3-5a3e6383da8f | -10.28172 | -68.74309 | 2026-09-12 13:27:00 | TERRA_M-T | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6fb07257-6dc7-30cd-adad-325e7f12dddc | -9.50072 | -68.48561 | 2026-09-12 13:27:00 | TERRA_M-T | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 46.4 |
| d5cd20c5-76ad-34b9-94b1-d1cba0433ea6 | -7.83668 | -71.98885 | 2026-09-12 13:27:00 | TERRA_M-T | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 274d978a-9efa-3752-8b5d-6dbc58099301 | -9.49889 | -68.50004 | 2026-09-12 13:27:00 | TERRA_M-T | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 895f892b-b012-3e68-a6b7-be8bd7de8446 | -9.31311 | -68.77729 | 2026-09-12 13:27:00 | TERRA_M-T | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9a1fd5d4-a0b2-31a7-93f6-68bd3265e68e | -12.5969 | -53.9854 | 2026-09-12 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| b6a3ec9b-ee30-3dfe-96ad-d5e1db6fa0b4 | -11.3536 | -46.8099 | 2026-09-12 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 4a1d28c0-ecb1-32f7-b64a-e796e2309c5e | -10.5664 | -51.356 | 2026-09-12 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 253.3 |
| 5b69515b-1f41-3090-aa3e-c74a895b0196 | -9.6951 | -43.3981 | 2026-09-12 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 36c86c37-8b0e-3050-b6e7-f9845cbc6a1c | -7.0164 | -44.6413 | 2026-09-12 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 269.3 |
| 05189cf9-e0ab-3c83-a17f-b80724ddc92c | -7.6008 | -46.1288 | 2026-09-12 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 269.9 |
| 77ba42a4-9f14-39a3-88dd-138532ad389c | -12.1391 | -48.9453 | 2026-09-12 13:30:00 | GOES-19 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ab9e2d63-f4bd-32a2-b9fe-b2066317deba | -5.7754 | -45.1053 | 2026-09-12 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d4aa6c61-e804-3960-b51b-123ed5f68677 | -13.5649 | -51.8869 | 2026-09-12 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| fa2ad66f-fe9e-30a1-8ae9-7ae391740bee | -11.4026 | -43.935 | 2026-09-12 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 6fefd879-9acd-3ee8-a5c2-166d58483ab2 | -11.3727 | -46.8074 | 2026-09-12 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 0b969076-66e5-3dd4-9381-9f2169c97d2c | -11.7997 | -46.3887 | 2026-09-12 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| b2cc45ea-1407-3404-8695-fba5701500fd | -7.9645 | -43.9971 | 2026-09-12 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 5c776895-8f46-3cb2-b18e-c18b53cb19f5 | -12.1388 | -48.9672 | 2026-09-12 13:30:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 602a5928-fdb7-36ca-8179-28a46bcf7364 | -7.0166 | -44.6184 | 2026-09-12 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 487.6 |
| e1462b96-ebc8-33ff-8e5f-53baafe8c775 | -11.3723 | -46.8299 | 2026-09-12 13:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 5b549c83-707a-3d92-9b3a-876aa85759f7 | -7.2147 | -43.7001 | 2026-09-12 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 61b20669-7645-3b5b-8df4-646601e9048e | -10.2926 | -45.3161 | 2026-09-12 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| abf128c1-b33e-36a7-9101-5ab330c53fe1 | -8.5415 | -54.7187 | 2026-09-12 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| fd6067fa-6aa2-378f-a7a7-4661bcc1cbb5 | -11.8193 | -46.3633 | 2026-09-12 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 7c68e2df-5eba-38c3-8301-64b239f89874 | -8.002 | -44.0163 | 2026-09-12 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 696a2b10-f2ce-3131-b966-15701c388008 | -10.3472 | -48.022 | 2026-09-12 13:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 049504e3-a42f-3b3b-8971-8037f1c2038e | -6.8755 | -47.4313 | 2026-09-12 13:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ba67ccf3-d8fd-305a-9953-499d306fe57f | -10.9491 | -48.3474 | 2026-09-12 13:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| e0b60f59-b838-388b-8ab3-a699d279702f | -12.1579 | -48.9647 | 2026-09-12 13:40:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b87f092a-48f9-32ec-b840-fc6b649467f1 | -10.6413 | -46.1133 | 2026-09-12 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 39c06fdc-f5fa-373a-95a2-22dfa916bc4d | -10.5664 | -51.356 | 2026-09-12 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 94162a8a-ad9c-3f6d-8c52-5f20e759150d | -6.2243 | -51.6949 | 2026-09-12 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a4b1d207-05a7-3f46-969e-4c85f5c33adc | -10.5413 | -45.2153 | 2026-09-12 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| aa76b119-9082-3162-b1d5-c0fe83f451e6 | -11.8193 | -46.3633 | 2026-09-12 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| d78022cc-2279-3355-9b03-12ae4fb89a9a | -10.9491 | -48.3474 | 2026-09-12 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 751adf1c-2990-38dc-952b-6653902c1d26 | -10.2206 | -50.373 | 2026-09-12 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 82efcff9-ad72-3cf9-b8d8-31e03428cd73 | -11.4026 | -43.935 | 2026-09-12 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 7ecf2114-a419-366e-8703-abcd68a67a44 | -8.2201 | -55.2627 | 2026-09-12 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2915a2bb-650b-3416-9e4e-f66ec8374b9d | -12.1391 | -48.9453 | 2026-09-12 13:40:00 | GOES-19 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 27a3b42d-0a37-3ee7-a17f-4409f8547b08 | -10.6223 | -46.1157 | 2026-09-12 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| c23fc773-eebf-3478-a8a8-3d5bf60e15e4 | -11.3723 | -46.8299 | 2026-09-12 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| b4552651-7f09-3807-af3b-9993598c49f8 | -4.8676 | -56.0039 | 2026-09-12 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 31f1b47a-c854-3cba-b671-91a31df286c0 | -10.2926 | -45.3161 | 2026-09-12 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 925fc42c-6cae-3420-bd09-88d6c3c698bf | -7.9645 | -43.9971 | 2026-09-12 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| f483a62a-1a29-3d04-9141-c6c4cccb1fd0 | -7.2147 | -43.7001 | 2026-09-12 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 91a1e846-c08d-39b6-b6ee-f6b50dd90ca9 | -11.3727 | -46.8074 | 2026-09-12 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 028094b9-1b73-3ed7-ac1d-fc1fde116996 | -7.0166 | -44.6184 | 2026-09-12 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 452.0 |
| 1add314a-f274-38f8-8938-57699304744a | -11.4218 | -43.9321 | 2026-09-12 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 164.5 |
| f95f1cb1-f8ba-3ed0-abbe-17a23597fc2b | -11.7997 | -46.3887 | 2026-09-12 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 6f127535-a0bd-3e09-b8a5-8845755c3450 | -10.7539 | -46.212 | 2026-09-12 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 31cf489f-251c-3cda-93f8-27ba4a2153e4 | -10.6827 | -54.1679 | 2026-09-12 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 32d6385b-fc80-3bad-88e4-3165429e899e | -11.3731 | -46.7849 | 2026-09-12 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 17f2f177-7883-3990-b39c-d9a4805246cd | -10.7018 | -54.1458 | 2026-09-12 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| adf939cf-6a2f-38a4-ba58-406e168d4f58 | -8.5415 | -54.7187 | 2026-09-12 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| d7ae827e-a4e6-3cf8-9300-1301177bc3c6 | -7.6008 | -46.1288 | 2026-09-12 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 395.5 |
| c927b3dc-91df-300f-a426-64621f7b2e71 | -12.1388 | -48.9672 | 2026-09-12 13:40:00 | GOES-19 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 8d91620b-f02d-366c-8a0a-33a279db56d2 | -10.6829 | -54.1475 | 2026-09-12 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 480b05f2-9987-3db3-864d-27e03ff224ed | -7.0164 | -44.6413 | 2026-09-12 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 304.4 |
| 1523fb10-d2bb-3664-aed2-ae45b9ae18b6 | -10.7015 | -54.1663 | 2026-09-12 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| bf091d65-5226-386e-8e42-05122e444ba6 | -10.2186 | -45.1881 | 2026-09-12 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| dffdf8c4-12e6-39c1-89b6-40f17855dac7 | -11.4218 | -43.9321 | 2026-09-12 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 341.8 |
| b694dd60-d2de-3bfe-a1da-15327381bb4c | -10.6827 | -54.1679 | 2026-09-12 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 9db63d8d-aef2-3e91-bac0-4333f18b6577 | -4.8676 | -56.0039 | 2026-09-12 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 549b62cc-ca3d-3466-9999-e97237abb188 | -9.6951 | -43.3981 | 2026-09-12 13:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 3bc26769-66bb-39e8-8996-491797a232ae | -11.4021 | -43.9585 | 2026-09-12 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 191.4 |
| a3cb9cbd-c1e3-3bc4-8132-bb516db49d9c | -10.7542 | -46.1894 | 2026-09-12 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 46988e20-6216-3157-ab42-56f32de689d7 | -6.5004 | -47.5909 | 2026-09-12 13:50:00 | GOES-19 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3489bfe9-6495-3d90-aaf5-df4e78f45099 | -7.2147 | -43.7001 | 2026-09-12 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| f497b0a6-ea61-3f3d-a564-5b925c696faf | -8.2201 | -55.2627 | 2026-09-12 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 48fe6ae6-77a6-3b4e-8de8-91be5442820a | -10.5664 | -51.356 | 2026-09-12 13:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 06ef5ae5-498b-31e6-870d-19c0abb88599 | -11.3825 | -43.9849 | 2026-09-12 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 189.0 |
| f1dcd462-4788-3cf1-9067-5e22947ec6f4 | -8.5417 | -54.6985 | 2026-09-12 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 044ee74e-fa69-3aa5-bcd5-c126ca60f277 | -10.2182 | -45.2111 | 2026-09-12 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| efc11288-51fd-3ded-9538-e1aa97f5821a | -11.4213 | -43.9556 | 2026-09-12 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| a06bf61a-90db-3196-86d9-f955ff8301aa | -6.2243 | -51.6949 | 2026-09-12 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b24600f3-0693-315b-9dbe-2dd223ba396d | -7.0164 | -44.6413 | 2026-09-12 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 268.3 |
| b21d31a5-d698-3a13-8856-a102cbab1fae | -10.9491 | -48.3474 | 2026-09-12 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |


[Clique aqui para ver as próximas entradas](README60.md)
