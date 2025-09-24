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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29526b29-6588-36b9-a76a-f16a9121bb52 | -18.6936 | -52.01291 | 2025-09-24 12:19:00 | TERRA_M-T | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 7460473f-0bcf-33fb-8d1f-9a520ea2a04a | -14.21507 | -42.06887 | 2025-09-24 12:19:00 | TERRA_M-T | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 40.4 |
| bc72eed6-1828-35bf-9dc1-2aa4f91d2635 | -12.31237 | -44.22171 | 2025-09-24 12:19:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f36523a4-0629-3559-81ab-cb1e7f6e27ab | -11.66982 | -44.37829 | 2025-09-24 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 3f792b10-9153-3911-b81d-e99d97eccdf1 | -12.09697 | -43.41652 | 2025-09-24 12:19:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 5c439db5-8128-3f54-bd61-7cbc58b711aa | -12.10791 | -43.41802 | 2025-09-24 12:19:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 105e9028-be33-33cf-a331-3e20f8edb423 | -13.91961 | -40.38388 | 2025-09-24 12:19:00 | TERRA_M-T | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 41437e9e-bc52-3c3d-b47e-b9397bc4909b | -12.06019 | -44.81705 | 2025-09-24 12:19:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 808ec8d1-1e7d-34f0-bfe4-01cbf22ccb8e | -13.634 | -40.91391 | 2025-09-24 12:19:00 | TERRA_M-T | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 26.2 |
| a1613226-32ea-3d28-9fc4-20347b33fc16 | -12.51546 | -48.09964 | 2025-09-24 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| df8ecb15-e653-36f4-b734-c347a16c9af3 | -11.6432 | -45.32588 | 2025-09-24 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d81121d3-5108-3b27-9f3a-2a6f6c9fce0e | -13.27967 | -43.28943 | 2025-09-24 12:19:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 216753fb-7c71-3208-9776-ed6a13aac4cd | -18.1184 | -47.12238 | 2025-09-24 12:19:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| aafd4344-1f08-3162-ac8e-131bde0707ca | -11.90429 | -44.76034 | 2025-09-24 12:19:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f5d0b059-ed81-37e4-be41-51cea3b38aaf | -11.43195 | -44.94618 | 2025-09-24 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| b0a5a971-0816-3f9c-8e3d-d15da074d754 | -18.56518 | -47.29 | 2025-09-24 12:19:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a144a279-b167-3060-bcfd-de295eede0aa | -11.67825 | -44.38531 | 2025-09-24 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| c45c6864-2bee-39a3-b69c-9a0d02a77467 | -18.56653 | -47.27973 | 2025-09-24 12:19:00 | TERRA_M-T | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 406ddcbd-6843-33c6-86ad-a24cc72c60f9 | -11.70007 | -44.37602 | 2025-09-24 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fe84a6e9-5f1b-3695-ac41-a3cd26f8c858 | -13.28148 | -43.27432 | 2025-09-24 12:19:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 43e5da81-113f-3716-9aad-d5251aef81ec | -8.2611 | -44.4052 | 2025-09-24 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 332.1 |
| a2511701-19a3-3e70-af6e-02be195b596b | -8.3139 | -46.2183 | 2025-09-24 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 158.6 |
| b70e2366-b6bf-3e7d-a507-8e19b32f3b8a | -8.2614 | -44.3821 | 2025-09-24 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| cdf114be-2b7d-314f-a276-639ce3e7c151 | -9.5595 | -47.5581 | 2025-09-24 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 9ab0e76b-b4be-36aa-a9be-37ad9ce0d2b3 | -9.5781 | -47.5782 | 2025-09-24 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 2c6769c5-5885-310c-848b-a19da9254dbd | -22.36875 | -49.49158 | 2025-09-24 12:21:00 | TERRA_M-T | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 124c3005-4444-323b-a35e-becf849eb39e | -23.3388 | -51.5736 | 2025-09-24 12:21:00 | TERRA_M-T | SABÁUDIA | PARANÁ | Brasil | 4122701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| bc4cc2f7-778d-3b2b-9d67-f24e2a58b874 | -22.37902 | -49.48334 | 2025-09-24 12:21:00 | TERRA_M-T | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 971a04af-620d-34b9-bead-c081362e2a73 | -20.54978 | -57.13357 | 2025-09-24 12:21:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 83d85d48-1e37-3767-b569-403443556e2c | -22.04167 | -47.03589 | 2025-09-24 12:21:00 | TERRA_M-T | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 016ce63e-cc69-34be-9bf0-6750b2c6377a | -25.8157 | -51.16095 | 2025-09-24 12:21:00 | TERRA_M-T | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| e0739c59-81ce-34f6-94c3-1b44c93c6f34 | -30.56087 | -52.6939 | 2025-09-24 12:23:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 5.6 |
| f66e0599-a7dc-3a9f-a7f0-6941b0d9314a | -30.55935 | -52.7042 | 2025-09-24 12:23:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 4.4 |
| 97dd6f33-8865-35f9-9fa0-1f5f579ac654 | -8.3139 | -46.2183 | 2025-09-24 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 1a314c7f-8f02-3d72-b767-0341ac91b86d | -9.5781 | -47.5782 | 2025-09-24 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 8a0bccab-8de6-3ae4-8b13-a1eaeb40400e | -11.5225 | -43.658 | 2025-09-24 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 05bca9fa-34ae-328d-b2f8-23daf86196e2 | -9.5595 | -47.5581 | 2025-09-24 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 173.0 |
| b3ab067b-27b1-321b-8d3d-6295c5bae98c | -11.6246 | -44.3697 | 2025-09-24 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| ff6d2f5a-4683-35aa-9b7c-f9a9ab8440bb | -8.5176 | -44.9977 | 2025-09-24 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 9aaa3a74-f398-3390-b4c2-978d1d0dc5c1 | -8.2611 | -44.4052 | 2025-09-24 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| d1c7373e-a3a8-31c8-ac30-de0d01effe19 | -11.6626 | -44.3873 | 2025-09-24 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 426a1f50-2374-3155-85ac-c51ae1a4b757 | -6.4129 | -43.0958 | 2025-09-24 12:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 2938098a-ef2c-3955-a2c8-0b7ea4c84020 | -11.6822 | -44.361 | 2025-09-24 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 7015a865-2d3e-36e9-82fb-6d3b64bf08df | -8.3139 | -46.2183 | 2025-09-24 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 2d101bdf-45f7-3dca-8b30-7979e722b3f8 | -9.5781 | -47.5782 | 2025-09-24 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 38c92f36-a759-38a0-bdc8-0dc0c5b63097 | -11.4233 | -44.9331 | 2025-09-24 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 4564934c-3d2b-3f76-bd8a-ac34ba28a5ec | -6.4317 | -43.0942 | 2025-09-24 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6d79416d-bbd9-3e09-98a6-40991dd4687f | -11.6438 | -44.3668 | 2025-09-24 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 3cb65649-a496-371b-908d-93f30a52902f | -9.9555 | -46.2876 | 2025-09-24 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| f0aa5bd3-e9a5-3c7f-a90d-ccd0e76d9319 | -8.8417 | -46.187 | 2025-09-24 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 8c98acbd-3af1-3593-a4c0-b8a0a5c228d2 | -8.2614 | -44.3821 | 2025-09-24 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 9c19a9d0-179a-3ed2-b403-d6905dfd4581 | -9.5595 | -47.5581 | 2025-09-24 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 133.9 |
| b91a4581-f5b5-36c8-989c-f538a957c846 | -11.663 | -44.3639 | 2025-09-24 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 015b21eb-a574-338e-b04d-ab9ec05fc3c8 | -8.2611 | -44.4052 | 2025-09-24 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 208.4 |
| e47b1950-d265-34b7-80de-276a68c717d7 | -4.7848 | -42.7502 | 2025-09-24 13:00:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 5e18782e-c21d-3dd1-b7d1-6fff0d46dd2c | -8.8417 | -46.187 | 2025-09-24 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 35088685-800d-333e-a9c3-870c0028602f | -11.7014 | -44.3581 | 2025-09-24 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2cca88b4-202a-35ef-8430-72f11adf6944 | -11.663 | -44.3639 | 2025-09-24 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| ef935724-b593-3c04-b973-84b43f09576c | -9.9555 | -46.2876 | 2025-09-24 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 2ac594c2-c0e2-3c68-af00-5d4cd857c574 | -11.6442 | -44.3434 | 2025-09-24 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| ac8a6b6a-3694-3ec5-8fab-b53fcd38bd08 | -11.6822 | -44.361 | 2025-09-24 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 965ac159-3904-3eb4-b52b-2b57c30e4bcd | -11.6438 | -44.3668 | 2025-09-24 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 96103458-9f4f-346d-8256-4d97bd294146 | -11.6246 | -44.3697 | 2025-09-24 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 8e2878f0-a5a0-362f-90d6-372b7227b82d | -9.5595 | -47.5581 | 2025-09-24 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 179.9 |
| d0be0305-05f5-385d-828e-6c95faddf320 | -8.3139 | -46.2183 | 2025-09-24 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 16989de3-4a50-34c5-8792-a73e2a00aa4f | -10.8429 | -45.4044 | 2025-09-24 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d0928045-cb5c-3013-8316-cb575a9fae07 | -8.2614 | -44.3821 | 2025-09-24 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| a3ccded1-e18a-35d6-a76d-63c042cba405 | -4.7846 | -42.7737 | 2025-09-24 13:00:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 147.4 |
| f72d58fe-5b38-3b63-b527-f0b3c1bc3a73 | -10.8425 | -45.4274 | 2025-09-24 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| b3a903b3-0307-3bdc-9f3e-05737227e337 | -11.4233 | -44.9331 | 2025-09-24 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| fe4146ec-8a05-3f93-bb1c-e9de5ac4b31e | -10.8616 | -45.4248 | 2025-09-24 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 7a13de7f-cc9d-3792-ae6a-d8918628adf7 | -6.4317 | -43.0942 | 2025-09-24 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| e902deab-1ef6-3ee6-a646-783123dce476 | -5.2074 | -43.7251 | 2025-09-24 13:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| ccc4620a-75db-3dbe-a2d4-f0cfde8a3d67 | -10.8616 | -45.4248 | 2025-09-24 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9af0b549-2573-3739-b32f-9fa5af8a1f4b | -11.0253 | -45.9046 | 2025-09-24 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8cc81060-246d-31af-88ec-d9a4eb043208 | -7.5649 | -44.3376 | 2025-09-24 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 832ffd4e-dafc-3ef9-85e3-e071e15e39f7 | -8.5176 | -44.9977 | 2025-09-24 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 17b32571-58ff-3b5e-93ae-308afdaf9a94 | -9.5595 | -47.5581 | 2025-09-24 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 43e19410-68e0-38e6-a315-de1360883bb9 | -8.3139 | -46.2183 | 2025-09-24 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 47f8397f-10f1-38b0-90fb-b5fca1b76ab8 | -10.8429 | -45.4044 | 2025-09-24 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b7f83661-aa29-3dd1-98d5-468902168b31 | -11.0249 | -45.9274 | 2025-09-24 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 87686423-808b-3b48-9170-8cc52e0b3a3e | -8.8417 | -46.187 | 2025-09-24 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 3049df48-1be3-3647-8fba-979c7239a833 | -9.9555 | -46.2876 | 2025-09-24 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 72c20703-77ad-3a40-a6ab-b5379edd8b7a | -10.8425 | -45.4274 | 2025-09-24 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| ee713025-a5c4-394d-901c-d03eb82da2cf | -11.4233 | -44.9331 | 2025-09-24 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 68d3e062-2390-3013-afa5-1327b34e6ef4 | -8.5176 | -44.9977 | 2025-09-24 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 873d9c99-a07e-3470-86fd-b0dcd14cdf7e | -11.0249 | -45.9274 | 2025-09-24 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 6ad3c98c-be2b-3a9f-a329-e8431a6279c2 | -8.3139 | -46.2183 | 2025-09-24 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 47952957-1ca5-30ef-90cd-d2c2f998c08e | -6.4317 | -43.0942 | 2025-09-24 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e4a7e1e0-98c9-3c31-8693-4cce69c75831 | -9.5595 | -47.5581 | 2025-09-24 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 79cf1ab6-118b-3645-8b8d-29b9a841e71a | -6.4129 | -43.0958 | 2025-09-24 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2aae36f2-dc85-3035-ba65-be19794c1188 | -12.3184 | -44.2154 | 2025-09-24 13:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 3ed03c10-031c-342c-9f88-86c85549bebe | -9.5781 | -47.5782 | 2025-09-24 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 2a816304-0d0e-3b6e-b05e-47b310fa31e3 | -11.4229 | -44.9563 | 2025-09-24 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| f29b90af-a467-3532-bffc-a14f75b67e4a | -5.2261 | -43.7238 | 2025-09-24 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| eb4a6749-c8b7-39bb-a018-dd5319917ab9 | -5.2074 | -43.7251 | 2025-09-24 13:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| e9a4c1f5-8881-32ff-bce6-bff36154700f | -11.5225 | -43.658 | 2025-09-24 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 17891f9b-b8a4-38d3-b37b-d79aa530575e | -10.8336 | -44.808 | 2025-09-24 13:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| b40a5c07-7709-313a-bc9b-94840bb7cb21 | -11.4233 | -44.9331 | 2025-09-24 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| abb0ba82-375b-3204-9ed0-25a2207c5a8d | -10.8332 | -44.8311 | 2025-09-24 13:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |


[Clique aqui para ver as próximas entradas](README23.md)
