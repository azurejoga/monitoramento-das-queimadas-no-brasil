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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33e425f9-f93b-3612-93cb-8389dd5b9d30 | -4.1761 | -44.2716 | 2025-09-26 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 67b16421-a008-3bdc-802c-55a9d3447efd | -6.078 | -44.7418 | 2025-09-26 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e4d3d909-e554-3b50-9f79-bff9937e0015 | -11.044 | -45.9249 | 2025-09-26 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 280.0 |
| c648a159-d62b-391b-a6a9-3376bced92cb | -7.6775 | -45.9872 | 2025-09-26 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| c7b3580e-12aa-35c6-80b1-60ff6ea45e2a | -11.8168 | -47.6424 | 2025-09-26 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8b4c950c-28de-312f-b8f2-6860911afd06 | -9.4749 | -48.2479 | 2025-09-26 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 3ad5d9f2-2183-3c9b-bba7-8f23116968d7 | -3.0574 | -44.4148 | 2025-09-26 14:30:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| bae6dff6-d9a6-3ce3-a55b-04715767c8d7 | -6.9115 | -45.6947 | 2025-09-26 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 2c5c653b-214d-30f6-9335-5a197168f395 | -12.3424 | -50.5655 | 2025-09-26 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 975b7291-2039-3e1f-8f97-bb146b050804 | -20.7334 | -57.8293 | 2025-09-26 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 194.1 |
| 7d7e4ca5-1098-3fa9-aae4-f51b8bc76986 | -20.7338 | -57.8083 | 2025-09-26 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 212.8 |
| ba54465b-68a0-395b-a56e-7c865b8abe44 | -8.7139 | -47.358 | 2025-09-26 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 06ea7084-7d83-3174-b3df-d3a9f6ddf521 | -17.1939 | -56.3661 | 2025-09-26 14:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 7cb6d2e1-4efb-3b9d-9255-5d0da240bf76 | -20.7338 | -57.8083 | 2025-09-26 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.9 |
| 8c4094d1-ca74-3e1f-ae89-1ccfd2220fbb | -5.5335 | -42.8149 | 2025-09-26 14:40:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| aef11fe7-1263-34d3-8da8-9bd3cb4b2948 | -11.9655 | -47.8891 | 2025-09-26 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 3d6b4262-ca0c-3ee3-9515-da046e67e3b0 | -11.787 | -44.9262 | 2025-09-26 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 70e28766-fc7d-3684-81e7-1d4211c047ce | -7.6772 | -46.0097 | 2025-09-26 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 2631e04f-5fd4-3916-a077-8e129a4b7d62 | -11.4041 | -44.9359 | 2025-09-26 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| e4616fdd-839b-327b-a92f-b41503641f1f | -17.1743 | -56.3685 | 2025-09-26 14:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| c7647bf7-a815-36ff-a681-e563333e8420 | -13.3463 | -47.8732 | 2025-09-26 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 66f604e5-9266-3b73-ab4e-35dece125958 | -7.3371 | -46.2194 | 2025-09-26 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 1be44603-090e-3385-87af-ec4dce1a9b37 | -11.0631 | -45.9223 | 2025-09-26 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| dc02eecd-4ad5-3c69-9272-cd51838c9ac2 | -10.4129 | -46.142 | 2025-09-26 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 901c7c44-fb5b-30cc-88b1-60faea98ab7f | -11.0444 | -45.9021 | 2025-09-26 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 2ec1c9c8-3a7e-3804-8bda-0766c3dae610 | -14.1153 | -51.1753 | 2025-09-26 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| fe362eed-5a24-30b6-a2ab-f8b095cd3288 | -11.6622 | -44.4107 | 2025-09-26 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| cfa38fa1-4033-34bd-9bef-788f76174f71 | -14.7723 | -60.191 | 2025-09-26 14:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 067338b5-5b52-3418-8dc9-c0f3bc8bbed5 | -6.5801 | -45.1117 | 2025-09-26 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 2ed574c2-3576-3c04-859e-d2b9fffa2d85 | -11.4233 | -44.9331 | 2025-09-26 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e6bcee52-fed6-38c9-ac69-96f3e1a8bcad | -9.4749 | -48.2479 | 2025-09-26 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 4f9c3a00-1a3b-3079-abd8-feb193310491 | -20.7334 | -57.8293 | 2025-09-26 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 189.2 |
| 80397804-df2d-311a-8f6a-a9c9d134c20b | -13.201 | -47.4026 | 2025-09-26 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7b88e63c-e756-3718-bb20-0d34813afad5 | -6.8008 | -45.5236 | 2025-09-26 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 26ac5993-1cc3-3fb1-818a-32940765706d | -5.7795 | -42.5837 | 2025-09-26 14:40:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 0aceeaff-8e94-3a44-9ecc-abee24ed7ebb | -20.7537 | -57.8265 | 2025-09-26 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 796.6 |
| aa404b8e-904a-3a03-a571-f1241a306496 | -11.7977 | -47.6449 | 2025-09-26 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 28483d54-c09a-3b38-9d47-7c69ca3114d1 | -11.9659 | -47.8669 | 2025-09-26 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 4d00ddda-1aed-3499-b414-d8d15098a636 | -17.1746 | -56.3478 | 2025-09-26 14:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 38.7 |
| 4e2d3789-b678-3d9a-a3e8-2133ce78e610 | -4.3252 | -44.2863 | 2025-09-26 14:40:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 101f29f7-c2dd-32a7-98bd-b5448fd66103 | -10.4125 | -46.1647 | 2025-09-26 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 3d79fce1-ba0a-367f-8d13-9c25e17aaaed | -20.7533 | -57.8474 | 2025-09-26 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 0b896561-a389-35f2-81f8-034bba337c51 | -11.643 | -44.4135 | 2025-09-26 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 627288a8-8d6a-317d-b86f-179c9d3f8723 | -7.3559 | -46.2177 | 2025-09-26 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| cbe6bb2f-28d6-3635-82aa-fc8f0dab7ba6 | -7.3755 | -44.4478 | 2025-09-26 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1c8ed2d2-dcc8-3988-82dc-a108ddc7d3ff | -10.8051 | -45.3866 | 2025-09-26 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 8d4f5a46-9966-3023-8f31-108e327a2922 | -10.3938 | -46.1444 | 2025-09-26 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 94a5394e-017d-36cf-9241-7d36c21a2896 | -11.6262 | -45.3646 | 2025-09-26 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 927e0708-84b1-326d-90f0-8df714853772 | -5.3091 | -42.761 | 2025-09-26 14:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 142.2 |
| 1db3231f-8549-353f-b63d-751acc8719bd | -14.0964 | -51.1564 | 2025-09-26 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 5c298e36-2773-3d0d-98ae-f255af64d16f | -11.385 | -44.9386 | 2025-09-26 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| f851faa5-9651-3331-94f7-8e65fbe21fb2 | -11.0635 | -45.8996 | 2025-09-26 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 7c42787d-68bc-385b-86ea-628dbebee98b | -12.631 | -48.1313 | 2025-09-26 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 73907342-acc8-3b76-8922-8f20d5b58898 | -11.6425 | -44.4369 | 2025-09-26 14:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 10b7f9c4-18fa-3e83-ab13-6a951b6e6168 | -11.8168 | -47.6424 | 2025-09-26 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f550f0c5-a74d-39e4-a444-2a9afe4062f6 | -7.6141 | -46.6188 | 2025-09-26 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 60270636-aaa1-3bac-89ae-eab71c707e45 | -7.6584 | -46.0114 | 2025-09-26 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 1b99b4e6-3ef3-3f60-9a89-8a78677fd45f | -7.6775 | -45.9872 | 2025-09-26 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |


