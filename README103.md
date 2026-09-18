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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dd5f4e3-7309-3b93-aa0f-1fab8c1723db | -11.3809 | -44.0788 | 2026-09-18 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 443a0a3c-b357-36ca-a94e-e04727288801 | -15.5926 | -56.5354 | 2026-09-18 14:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 121ec8a7-3ee9-3382-a3b3-b68b8b859b38 | -12.3954 | -48.4727 | 2026-09-18 14:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a6b635f0-5db4-3b59-9728-769f1d0172c1 | -11.2975 | -43.3851 | 2026-09-18 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 509.7 |
| 5ea624e3-95eb-3588-82bd-2cc657a02947 | -9.8505 | -48.3834 | 2026-09-18 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 15a17b77-5732-3b5b-bd93-1562289e8f89 | -14.1737 | -45.1641 | 2026-09-18 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 3bcae4a9-c3e9-3331-9941-c5532f0ec333 | -10.6189 | -50.2466 | 2026-09-18 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 815c0d9c-1a50-37cb-a9fa-a50254f3da4b | -10.623 | -46.0704 | 2026-09-18 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 6171379a-3c44-31bc-9d80-cf6061aed512 | -10.6726 | -50.4758 | 2026-09-18 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| cccf324a-038b-3c89-98fb-a2c61d49415b | -11.8746 | -47.6125 | 2026-09-18 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 2f33ad73-be38-39d6-83a6-9edd548ec3fa | -7.0352 | -44.6396 | 2026-09-18 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f6ddd6c0-76f3-325e-875f-78f7514ea418 | -7.8191 | -45.1145 | 2026-09-18 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 46.4 |
| d8f23f63-0890-309c-bdf6-97b35248c8da | -6.0194 | -51.81 | 2026-09-18 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 61c19734-b275-3a7b-8283-da2b7124a341 | -11.2787 | -43.3643 | 2026-09-18 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 25282cbd-3654-34de-a22f-a70c9744fcf2 | -8.3769 | -47.236 | 2026-09-18 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 30245b78-590f-32a9-8b79-8617ea77ccf8 | -11.3433 | -44.0376 | 2026-09-18 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 284.8 |
| 58767bee-0dc0-32cb-a689-3f0cf792d947 | -11.4541 | -51.4754 | 2026-09-18 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 246.3 |
| d9b26893-f6dd-3876-94ad-e01dcd711ec1 | -9.9768 | -50.2694 | 2026-09-18 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| fc7d752e-aeec-3d66-b3ea-974bd223a1bd | -11.3838 | -47.2982 | 2026-09-18 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 712bf223-c205-34b6-9afd-997f77acc54d | -8.6817 | -45.4359 | 2026-09-18 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 971fd4c7-93cc-315f-ac9d-c896573f5d02 | -11.3171 | -43.3585 | 2026-09-18 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 34f0b48f-f65d-3983-a4e1-5bb1cc0bdced | -3.7516 | -54.6494 | 2026-09-18 14:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 0e1cd4ab-c52f-3f7b-b061-2a0a2837bf81 | -11.064 | -48.2898 | 2026-09-18 14:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 19147396-6f2a-3365-9ff1-df10e71ff658 | -11.3617 | -44.0817 | 2026-09-18 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 6a972b6c-0322-3c37-80b0-097dd70a7b0b | -9.8316 | -48.3854 | 2026-09-18 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 2a452e40-a041-3edd-a70e-181ce9ca206c | -10.676 | -50.2192 | 2026-09-18 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 2731073d-c41b-3777-8180-021dcbef527a | -11.3437 | -44.0141 | 2026-09-18 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 397.1 |
| 91d43b40-504c-396e-aa03-881dfac78ca5 | -7.8216 | -44.909 | 2026-09-18 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 170.8 |
| c3d6a77e-ba2e-3957-8624-6cc7dde97a1c | -12.998 | -46.9381 | 2026-09-18 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| e5b170d4-f462-3a8a-b3d9-b6f26ed4d0e1 | -7.8036 | -44.8422 | 2026-09-18 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 280.2 |
| 19bda544-9206-38b5-ae91-6d275185e923 | -8.6835 | -45.2993 | 2026-09-18 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 4c972db5-6920-3491-8ba9-2f059d15b3b6 | -6.3102 | -55.2686 | 2026-09-18 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| c56ae604-3f00-3637-b7ed-720e5be5ed38 | -4.5961 | -42.95 | 2026-09-18 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 235.3 |
| 4df6a823-314b-3a98-a565-8f3d0df8658c | -9.788 | -46.0819 | 2026-09-18 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 35a35344-1508-3f24-8a93-0bdeba5907c5 | -13.4307 | -51.8823 | 2026-09-18 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2fc8df3a-c739-3a33-ac96-bed8eff326fd | -12.1256 | -44.246 | 2026-09-18 14:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 5ebf3bde-ad4a-3a78-8709-1ad0e9eb67c9 | -11.8119 | -46.7932 | 2026-09-18 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 5a9d7a63-c44a-39ef-b033-26c8e81e8db3 | -15.6752 | -52.7339 | 2026-09-18 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| cbd2e703-8015-3fa9-b0b4-641fb773fec1 | -14.8026 | -48.5622 | 2026-09-18 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 6bc9d12d-a77d-3ff0-a2ec-3be5d71b75dc | -9.2417 | -45.9185 | 2026-09-18 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 89b59dbc-c27f-397f-92df-ff75007bb8cd | -14.1732 | -45.1875 | 2026-09-18 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 1d033936-f6bb-3d09-a136-f844dc688cb8 | -2.0952 | -56.4083 | 2026-09-18 14:50:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| b6762180-4567-34d4-bf9d-95941a789b2b | -10.6755 | -50.262 | 2026-09-18 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 4b3420e6-479d-33e5-a467-b0543c17dbc8 | -14.8026 | -48.5622 | 2026-09-18 14:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| a9f2e0bf-b99f-3dcf-a5d6-b022be42f971 | -7.8038 | -44.8193 | 2026-09-18 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 1023c921-c054-329e-851a-39f757d51aa0 | -12.1527 | -46.9933 | 2026-09-18 14:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 16ca5802-ab56-3f02-badc-21d1a2ce3c63 | -11.2975 | -43.3851 | 2026-09-18 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 271.4 |
| c2815f8a-5c2e-38cd-815c-c333ee32fa2e | -11.3442 | -43.9906 | 2026-09-18 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 204.4 |
| 3c353e59-97a1-3758-aae2-698aa38cd245 | -1.2193 | -54.2192 | 2026-09-18 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f2a26f62-67e1-37ad-bbc6-34a47e52c1d5 | -8.6817 | -45.4359 | 2026-09-18 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 82202bf7-b2f6-393e-aa8a-4a2b9cb567a9 | -11.3809 | -44.0788 | 2026-09-18 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 51a302f8-fa4e-36a2-9f29-ce13f71ecb5c | -12.0238 | -51.4763 | 2026-09-18 14:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 8e0d337d-f064-39de-a56f-aa8d21bdddc9 | -11.2979 | -43.3614 | 2026-09-18 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.7 |
| f69334ad-61a4-3d30-b06a-65c157d2bc35 | -2.0769 | -56.4085 | 2026-09-18 14:50:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 92ac5d24-2608-35d1-ac1c-7c4e35812d19 | -11.3273 | -47.2609 | 2026-09-18 14:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 4d17cf9c-fbbe-3a89-ab2a-952c254d5f9c | -8.3769 | -47.236 | 2026-09-18 14:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 390e8f25-d1eb-330e-832a-3c8af78d3619 | -10.6187 | -50.268 | 2026-09-18 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 6f540854-3c94-35c4-ab18-456afcd44e67 | -8.6374 | -44.5029 | 2026-09-18 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 3c6153b7-b790-3ae6-8948-684ea8c12b2b | -10.2821 | -50.0035 | 2026-09-18 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 7452dbf4-8088-3967-8094-acfe59a93e3c | -9.9768 | -50.2694 | 2026-09-18 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 7e35693c-6661-320a-81d7-e404537ecde1 | -7.841 | -44.8614 | 2026-09-18 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 8e07d831-0a65-3ca1-b2a0-690e2db5de1c | -7.6394 | -44.3995 | 2026-09-18 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| da458c4b-4b02-3063-b255-8a9dab2423ab | -14.1547 | -45.1442 | 2026-09-18 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 85f85e0b-c4ab-3fa0-887f-c41930068f13 | -14.1542 | -45.1675 | 2026-09-18 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 178.5 |
| c720ce13-b7a5-3e9c-880b-0ddbbff771c0 | -1.6042 | -54.415 | 2026-09-18 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 161.5 |
| 16aab6f3-dcf7-347b-83f1-dd261eb69639 | -11.8115 | -46.8158 | 2026-09-18 14:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 0628d29b-93a4-3160-a0f0-a69a1ac119a0 | -9.5695 | -45.4729 | 2026-09-18 14:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6068cece-2e2e-31af-8af1-837b165ede1c | -12.0086 | -49.9606 | 2026-09-18 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 248.8 |
| 579fb309-8743-3956-91a5-618b0db4d2b6 | -9.6019 | -45.855 | 2026-09-18 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 17c883d7-7c6c-3044-87c0-76375a0aeee9 | -10.6189 | -50.2466 | 2026-09-18 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| fcdf5908-673a-334f-a847-6d142561eac2 | -11.3437 | -44.0141 | 2026-09-18 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 562.2 |
| fc73ff6e-9b37-322b-b610-302fd5a168a4 | -12.6427 | -50.893 | 2026-09-18 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 56f10507-21c8-394a-9e43-0482aecf0f00 | -10.5178 | -46.7366 | 2026-09-18 14:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 67cf903f-1391-3043-ac04-f14ad80fa1b6 | -4.596 | -42.9734 | 2026-09-18 14:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 9e79ba82-efd9-33fa-ba3a-3e3215656bb7 | -9.7497 | -46.1089 | 2026-09-18 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 5cb8c5e4-072b-3e5e-807e-f58272b09d21 | -12.1448 | -44.243 | 2026-09-18 14:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 138f6bb2-2e5c-3ac8-a174-eeccee3cfc0f | -9.7177 | -54.8162 | 2026-09-18 14:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 5eee7de9-60f2-3654-8c4f-511d68eb332e | -15.6557 | -52.7366 | 2026-09-18 14:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| bcc2ef2f-0db8-3148-a06d-6f07b0cfa0c2 | -10.6726 | -50.4758 | 2026-09-18 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| aae8f488-972e-39b7-9086-09d73faa8f1e | -9.9136 | -46.5621 | 2026-09-18 14:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 23bec1a1-b57c-362d-bfcd-65f8a3d67a7f | -10.6533 | -50.4991 | 2026-09-18 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 12bc964c-55e6-3643-9186-2d44443f5453 | -9.7494 | -46.1315 | 2026-09-18 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8cdf9561-17f7-35fd-8f39-2dbf5ea08a3f | -10.6729 | -50.4545 | 2026-09-18 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 776e6143-71e9-3ed2-9938-e5a04c605db3 | -6.3286 | -55.2877 | 2026-09-18 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 7c22016c-a9c6-3242-826a-7b173747ea7e | -7.8601 | -44.8366 | 2026-09-18 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 5fa37bbd-4cf4-3d70-8d25-b878f7744aa1 | -14.1742 | -45.1407 | 2026-09-18 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| a2171a0f-69a2-3003-b622-08c7e0bb4ff5 | -11.4541 | -51.4754 | 2026-09-18 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 324.5 |
| 76006fc3-7dea-3f4d-8850-134b2536908b | -6.3101 | -55.2886 | 2026-09-18 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| fab0d13b-5d02-3b18-a853-a005f9ddbaa5 | -11.8556 | -50.0006 | 2026-09-18 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| cb1feb3a-2284-3890-b290-2a4b5332ed3a | -11.0048 | -49.7325 | 2026-09-18 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| f9b1a000-8b07-36fc-a16b-857db8e9469e | -2.4814 | -49.4208 | 2026-09-18 14:50:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 55e963e7-61b1-35ec-ba32-5cc77358d01c | -5.8965 | -53.5178 | 2026-09-18 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b34b256b-1d5f-3b64-a377-2ca94bf8671e | -12.0902 | -50.8521 | 2026-09-18 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 2f3a5d6f-e5c5-3f62-a75f-0b2d9cf41e74 | -11.8746 | -47.6125 | 2026-09-18 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| d06df44b-8f46-319e-842c-0275751fdaa5 | -11.3617 | -44.0817 | 2026-09-18 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 5babbd18-23eb-3498-a78e-345724cdf947 | -8.4329 | -45.7337 | 2026-09-18 14:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| e5faf725-0e53-334a-9537-bf1e03de5a40 | -11.064 | -48.2898 | 2026-09-18 14:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 17251193-debc-3f7f-9127-f9a27c524da6 | -7.8598 | -44.8595 | 2026-09-18 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 02bed4e0-3be5-3632-8398-ef0b9a53a2af | -12.3954 | -48.4727 | 2026-09-18 14:50:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e38a8e98-6259-3bbc-80df-eb7570c783a6 | -12.998 | -46.9381 | 2026-09-18 14:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |


[Clique aqui para ver as próximas entradas](README104.md)
