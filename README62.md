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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86c16370-d892-324f-8066-e8df279765e7 | -9.83601 | -48.35663 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7ad93bcb-ab64-360a-9d4e-03ebd024e0e8 | -5.89466 | -52.06526 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cef0aecc-822b-3acd-9b5a-b90ac4e1c1a4 | -6.82415 | -59.18099 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 287d594b-6d6d-3aa8-ad1c-deccf7771564 | -6.20342 | -57.78004 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cf4ee22-0eb4-33ac-b183-35cce4d38d58 | -6.12585 | -57.82989 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| da43e2b0-cae2-367b-9e65-9c758567e8b1 | -3.48711 | -54.7127 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 05c5617a-631e-31ac-9e56-0c4d3284e1bd | -7.08716 | -43.46923 | 2026-09-17 05:16:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a11f646-fc04-37bc-aa44-5f8507346409 | -9.10707 | -45.72078 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 32.7 |
| bb12665f-09c6-37ad-badb-bcf26d4c5868 | -3.14313 | -58.64487 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b25ac24-4107-35ed-a72d-9922bf34bfe2 | -9.04027 | -47.75665 | 2026-09-17 05:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cad2dbfc-670f-3dc9-886c-4c3c0a69e88a | -9.8353 | -48.36215 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca1dd218-febd-34bc-a412-f45177c1ce18 | -3.54567 | -53.99364 | 2026-09-17 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 785b8595-39ae-3bfe-a301-466e95d74757 | -3.33422 | -57.8493 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 539b06c0-8424-3109-a14e-988b4beef6e0 | -4.41761 | -55.50077 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bd6ed34-85e9-3a8f-afa9-b976646710a1 | -4.95996 | -45.14042 | 2026-09-17 05:16:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81aea1f1-9359-33ff-8bc8-fb7fb30bc3fa | -6.77961 | -48.66161 | 2026-09-17 05:16:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22131cd7-db67-38f6-938c-dea007fa7a39 | -7.96648 | -44.82946 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5e03dd4-cd73-3af2-a2fc-6e0fb44a3dd5 | -7.27264 | -46.80032 | 2026-09-17 05:16:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9eb5786-6e88-31af-ad25-2437033f1239 | -4.36257 | -47.77918 | 2026-09-17 05:16:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e1b5a24d-d433-3b5e-9b74-d212e8be30af | -5.80312 | -47.24602 | 2026-09-17 05:16:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| cae20bbe-9c84-3341-a3de-89d3cad197df | -8.58481 | -44.5745 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 46581faa-5261-3f3c-b5f5-1da51e02905c | -3.04382 | -51.27132 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36a20566-6daf-321f-9a3a-4f95ae61d34c | -2.9042 | -54.18295 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eaaab634-8b4b-3985-b857-0eb7c3d1bfc5 | -9.11501 | -45.72789 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 3371a551-cc0f-34eb-8700-814c768fcef0 | -3.48989 | -54.71669 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b3d0d300-cb5a-3746-a364-b6bf35b2c578 | -6.79435 | -59.18121 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 014cfe76-15dc-3477-b1d3-8969623ccec3 | -5.1415 | -55.94959 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c01a9b7-3f37-3823-8e9d-0c1f83b8808d | -4.50481 | -54.97198 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5392bdd2-c2b3-3f3c-b454-452e8889f10c | -3.60073 | -59.06158 | 2026-09-17 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1415238-83ff-385d-bec2-ffb89af9a0c8 | -5.14593 | -55.94317 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf7829e6-c17c-338e-9113-a21b64e67551 | -7.38296 | -44.51643 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d99c4459-aa86-3b1b-84bf-9b0629605c27 | -7.03225 | -42.07293 | 2026-09-17 05:16:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 091a849f-72a5-336a-9b50-0572607fb684 | -10.61653 | -46.08932 | 2026-09-17 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b8d6b45-d454-31a2-b302-eb8da656803e | -9.10964 | -45.72261 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 7cd13378-0364-3e67-a179-750fab70cd47 | -2.75534 | -54.67529 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b996882-3393-364d-8024-93c1ff88b61d | -8.46227 | -44.55354 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 220c9a34-fa61-358b-8d52-19a00c80556b | -6.51464 | -44.05425 | 2026-09-17 05:16:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88fdb7a5-e692-3c7b-a4ac-5df1364405b0 | -8.09657 | -61.81971 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98cb4ce2-b862-3725-a4c9-d1a47ce857fe | -3.50479 | -53.20783 | 2026-09-17 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d235f7b-d679-33ab-8ccf-b6c8281c96a9 | -8.61319 | -44.50488 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec98139b-8117-3171-98d5-359afdfedb81 | -9.10853 | -45.73153 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| b282359c-483f-3c97-814e-4d3cd8d3461a | -4.56744 | -54.91411 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c5adb6f-4605-36ab-aac8-f0498f66b572 | -7.36829 | -44.48376 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30b72c11-645b-376a-8c97-7df376f80616 | -4.40638 | -55.08086 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d322ef2a-d8fa-3d58-8dcf-6e392942623c | -8.49436 | -57.63572 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c98ece5a-ff76-3942-9918-1d2c47789393 | -5.64873 | -44.80568 | 2026-09-17 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7e4c13ad-4721-38c3-95aa-6a8458be3595 | -8.41375 | -54.75165 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68318184-ae5c-3b1d-a972-c201aabac16e | -6.51534 | -44.04926 | 2026-09-17 05:16:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55f8ea38-b8a2-33de-9cde-a3f9cbe8510e | -6.81979 | -59.18464 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df2c8d01-fd8e-3c2c-b0a3-496104cfc731 | -3.80813 | -58.89941 | 2026-09-17 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02abac3b-b3d7-32a4-be31-01b6a9cb5576 | -4.5491 | -54.92916 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fd898ff4-1218-3710-b227-a2b22f5f7395 | -3.50765 | -53.21206 | 2026-09-17 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 398e63e4-41e4-300a-a938-06a6a7e3251b | -10.60952 | -46.09738 | 2026-09-17 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26cfb7a3-3a56-3d75-90d8-322a8867a475 | -6.312 | -62.66843 | 2026-09-17 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3522d5fe-db19-3737-b358-b8241041e35e | -7.9419 | -44.83844 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| ad132ce9-5187-3e5e-95d6-9f8254f20cf6 | -9.96633 | -45.32986 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48187f22-f18e-346a-a158-70b0fca72545 | -7.6532 | -45.83993 | 2026-09-17 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1df9a34d-61d2-3076-943b-f027c193a2d9 | -8.29058 | -45.64726 | 2026-09-17 05:16:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bac2fe8-7de7-3b35-b42b-27eb0839e0c7 | -4.88123 | -50.91554 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2514a18-5b4f-3b3d-a794-14b139bfef52 | -6.79719 | -59.18528 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb4b9d0c-22ac-35d9-96a7-7694e6f9afa5 | -4.56517 | -54.91386 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ded551e-fd63-3db2-918c-e2ddedc662fa | -7.0 | -43.33336 | 2026-09-17 05:16:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e4203eb8-131a-34d9-8ebc-c28b34978280 | -4.51202 | -54.96955 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ea01786-0a81-3b6d-9455-cfc0e4085040 | -7.97415 | -44.83261 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d9add07-e023-3d29-8354-e836337703b5 | -4.53252 | -54.96923 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d86b034b-2dca-3315-87d1-5b7567787d3d | -9.01007 | -57.12535 | 2026-09-17 05:16:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 917eb6d8-9514-341c-80d3-2085fbb3c01f | -6.69184 | -56.4141 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21b46b98-d99b-3d9a-b348-1e6d34e8f0cc | -3.42288 | -58.2322 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b52dbdba-92c6-378e-80f5-0dfb0912e2df | -8.47374 | -44.56451 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 62288412-e504-3e0b-8df2-26981df03d54 | -5.76688 | -45.11456 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 4353e88c-10f8-33ad-a92c-2450a04aea29 | -5.64274 | -44.80479 | 2026-09-17 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6b449cd7-074c-3dbf-b5c2-2ff490de2d6f | -2.89862 | -54.1749 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17010afe-a9eb-392d-88c2-73c57a7c533b | -10.1151 | -45.63203 | 2026-09-17 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 24640ea7-a543-333d-a68c-fb5c305e887a | -10.54552 | -44.85137 | 2026-09-17 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7cd89ee7-1ba6-33db-8be8-d4068e687d33 | -8.78731 | -46.89651 | 2026-09-17 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f43e88c-f6ff-3ee4-a158-f6b3efcdd1d0 | -6.11205 | -57.69655 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65ed63cc-4bf5-3781-ad3f-c6ebba56f39b | -1.84001 | -54.92075 | 2026-09-17 05:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95b0e8e0-df5d-34fd-961e-f586c2c40080 | -3.25955 | -54.27029 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8d98f7b-47fa-34aa-97a6-6b02e8617990 | -6.68456 | -58.85139 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f4901e9-d8eb-3f07-92f7-dbaed2de2a38 | -4.34088 | -46.61566 | 2026-09-17 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 977ce194-7d23-37d2-bcd3-8acd063fd4b3 | -3.48296 | -58.36904 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f63c39cb-30b2-3e32-8f83-94bf4f60aebd | -3.47434 | -54.70716 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5a99ee3-0097-3cea-b3f5-451f4a487303 | -8.48079 | -46.88847 | 2026-09-17 05:16:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22b8f780-983b-3497-9943-ca7fb5a400fa | -5.30731 | -56.09702 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fae13ab-9d3c-3505-b7c7-e9065e498921 | -3.73552 | -55.94114 | 2026-09-17 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 531e289d-2637-3892-bac7-cbc84f74e9fd | -3.32584 | -57.85616 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc8b968c-89f5-35f5-b196-7832cbf9c026 | -9.90398 | -46.5146 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72583a2f-329b-3f65-930f-551d0187c70f | -4.49481 | -55.50225 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3832e827-ee69-32ca-abf0-982f1b7c598d | -6.36217 | -58.28814 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6127b45-9fe5-3f96-984a-6a45cdb6c458 | -3.27113 | -54.25463 | 2026-09-17 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf72e997-3ff6-3c20-9a6a-30b97f1afd75 | -3.33727 | -59.82921 | 2026-09-17 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07e9aae3-d68e-31fa-90a2-0cb325236bf7 | -6.15725 | -55.71277 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 807ee8bb-5499-3e12-ada2-6d8961280f39 | -3.76208 | -51.13695 | 2026-09-17 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ef461aa-b05e-3ae7-9d55-23f178975519 | -3.47658 | -54.7146 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 396e2619-54b6-3e41-b208-92dd92c48713 | -2.96328 | -50.32405 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7bbb7465-1a0b-3e5d-ad5b-8cbdc39c59d3 | -7.09675 | -47.50952 | 2026-09-17 05:16:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc0b5e56-6355-3125-b7b8-89c7a04e286c | -3.57453 | -54.5624 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5f545fb3-40d3-3f39-aedb-db9915314710 | -4.49203 | -55.49826 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8151917e-536f-3c16-b86b-ff83f9c0fedf | -8.85443 | -46.97583 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34f7c22e-b540-356b-ab70-36094060c1d3 | -5.15592 | -55.94476 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README63.md)
