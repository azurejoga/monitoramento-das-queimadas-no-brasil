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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1497214-ea7d-3607-ae78-6016e768f3b1 | -9.4381 | -45.3972 | 2026-09-21 03:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 19042a29-5a53-39a2-b6d6-f0669e5096f0 | -7.5889 | -57.6757 | 2026-09-21 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ce16d1df-a79d-3b12-9701-8a9b4355bf52 | -11.8014 | -49.8129 | 2026-09-21 03:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| a91da01b-9668-314d-b1a2-5ac091da2171 | -9.5593 | -66.0545 | 2026-09-21 03:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 912b2486-b4bc-391a-9742-91781b53c7e6 | -16.03 | -52.5135 | 2026-09-21 03:50:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| bd9ca5eb-5f58-3be3-ae53-ec9bf9f87fbd | -16.0491 | -52.532 | 2026-09-21 03:50:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| def0be0b-43ba-354b-80f7-65143e6d76bc | -16.0495 | -52.5106 | 2026-09-21 03:50:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| d98359d6-b163-3269-b4e1-36f5ee4b5ac3 | -3.424 | -59.2726 | 2026-09-21 03:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 38675d9b-eefb-3c61-97d6-d96180310227 | -10.0898 | -50.2795 | 2026-09-21 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 2b52d5f9-0a62-342a-8328-a86e6ee0353a | -7.5703 | -57.6962 | 2026-09-21 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 38b40de8-b86c-3eeb-9590-ea3d674d24af | -9.457 | -45.395 | 2026-09-21 03:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| acf1cdde-2a96-3861-8889-68185e6a7b2c | -7.5888 | -57.6953 | 2026-09-21 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d099fc50-0ba7-3bdf-9886-23c22b9d994b | -7.5703 | -57.6962 | 2026-09-21 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 48eb1d60-04e9-3c2d-8407-82b850d96ccd | -16.0491 | -52.532 | 2026-09-21 04:00:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 138.7 |
| bb10bd4d-0f59-3993-8b3d-bd44c58e2e52 | -3.0717 | -61.2764 | 2026-09-21 04:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 606efd59-0263-3df7-9584-adb5fe2fbc07 | -9.5594 | -66.0359 | 2026-09-21 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.9 |
| eb6cf87e-d876-3bcf-97d4-f74a3545cefe | -16.0296 | -52.5349 | 2026-09-21 04:00:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 9b6b0165-e92d-3bba-ac7f-314d9fc8c99e | -16.03 | -52.5135 | 2026-09-21 04:00:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 127.6 |
| caf9164f-1af7-3c3e-a915-6ea16c187067 | -16.0495 | -52.5106 | 2026-09-21 04:00:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 198.9 |
| f01d5196-7a83-386b-886c-eba69657b29e | -7.5704 | -57.6766 | 2026-09-21 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 79dfd9b3-33e5-35f8-aeff-a0676a868fcc | -10.0898 | -50.2795 | 2026-09-21 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 6e16093c-5c1e-3b8d-bf99-7b2a40a53c95 | -7.5889 | -57.6757 | 2026-09-21 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2e91bccb-0080-3570-90a3-d326b189ac4b | -7.5888 | -57.6953 | 2026-09-21 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 32437e2a-1b6c-3608-a0d3-9f7cbe8f6be4 | -11.8014 | -49.8129 | 2026-09-21 04:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 18d42d05-6629-3174-a1b8-6d192de67ddd | -9.5593 | -66.0545 | 2026-09-21 04:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 2eea16b6-9a2c-367a-a855-b81e6d66ec62 | -10.09 | -50.2581 | 2026-09-21 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 234.8 |
| cb4a9f0a-4bf7-3e9f-8ea9-29492ce636e9 | -3.74463 | -40.30072 | 2026-09-21 04:00:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a5427e0c-30a8-3336-923e-6c38154d5f10 | -3.34775 | -42.76334 | 2026-09-21 04:00:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f736e218-57dd-3c29-b529-bb15b2e0778b | -4.34025 | -46.37085 | 2026-09-21 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dfaf20e-3801-365c-9165-1540b9e4717a | -4.036 | -39.45917 | 2026-09-21 04:00:00 | NPP-375D | GENERAL SAMPAIO | CEARÁ | Brasil | 2304608 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5578a6fd-6f00-3b65-8568-a9d49c7ddd28 | -6.39478 | -39.48795 | 2026-09-21 04:00:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 574aef55-5d26-3462-9b9f-2a20b5e56e78 | -2.46287 | -49.22729 | 2026-09-21 04:00:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69336a51-854d-3713-8b3f-33542f1599d9 | -7.09527 | -39.28984 | 2026-09-21 04:00:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8dc8c41-aa24-36da-b804-4fe84e0e8ad5 | -6.55992 | -45.55281 | 2026-09-21 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76e9a6bc-d46c-36f4-921a-a93016cf0b89 | -6.88525 | -41.70861 | 2026-09-21 04:00:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 20d5df1c-0bd4-359a-a269-5194234baa3b | -6.88607 | -41.71019 | 2026-09-21 04:00:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 374db842-8ace-342f-a82f-d6ef9a73684e | -4.85012 | -40.52581 | 2026-09-21 04:00:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 229498f0-2268-354b-8e79-d31adc8c8793 | -6.55416 | -45.58501 | 2026-09-21 04:00:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91f8ba34-8fb7-3608-beca-82f03a5ba751 | -6.46776 | -48.44495 | 2026-09-21 04:00:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c024326-c2af-350e-aaf9-367f6e4eeba6 | -6.97979 | -45.82151 | 2026-09-21 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 87a5d0e7-8eae-3a44-ae7c-96eb0cf2b066 | -2.17274 | -48.3204 | 2026-09-21 04:00:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f99c1fc-ea2b-3ee6-932d-d9bcbd60a467 | -6.91947 | -43.73352 | 2026-09-21 04:00:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e90a965-d46e-3b49-9cf8-1acfe33e4e54 | -7.09816 | -42.07638 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f68262c4-6c76-331f-b5ce-e3c1f74c34ac | -3.16986 | -48.61231 | 2026-09-21 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 598cd85a-9f1f-3bb1-9053-8d2122e8ffd6 | -6.46855 | -42.76511 | 2026-09-21 04:00:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 143b327e-1d41-30c5-ba14-79ae5b0a98ce | -4.68411 | -40.14906 | 2026-09-21 04:00:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0fdc3fef-22b9-3fa4-b65c-44223c4444bb | -6.91116 | -43.7272 | 2026-09-21 04:00:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4719b33-2e5b-3b3e-b19b-e0605eb95aa7 | -7.16791 | -43.01767 | 2026-09-21 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 990526f0-d3c7-3fb0-8dcb-2185fe23e7be | -6.69379 | -43.62781 | 2026-09-21 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7671cf77-04b9-3ccc-8f08-8609c913de94 | -4.67732 | -40.1435 | 2026-09-21 04:00:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5dfb3fb0-a474-3e43-9990-0a89398864f0 | -3.33646 | -42.77547 | 2026-09-21 04:00:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c0ba6ee-9e68-36e9-9a3e-db8f4e08ed7a | -6.93057 | -38.22507 | 2026-09-21 04:00:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6fd7ea5d-2270-331f-ace0-084ab13597ee | -6.57597 | -42.55825 | 2026-09-21 04:00:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cb0bb6d3-400d-3691-8632-c30611779b3e | -4.86188 | -43.5646 | 2026-09-21 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d76f178-5343-3767-bf75-c47957b6770a | -6.83814 | -45.55823 | 2026-09-21 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 915978df-bd8a-3f47-98c4-c916de280099 | -2.45708 | -49.21935 | 2026-09-21 04:00:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1eea800-210d-329c-9c6f-f864e6f1be7d | -7.02683 | -42.08383 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 48dd59d9-6b54-3637-adc4-53ec64480beb | -6.91652 | -43.72333 | 2026-09-21 04:00:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7eadb14-4016-33d0-8dcb-b86d539823e1 | -7.09408 | -42.07569 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3281d3fd-3d85-3037-80ee-3d4a809a75a1 | -6.37194 | -35.16012 | 2026-09-21 04:00:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 950d6410-e9f0-3422-be41-5003a4152d4d | -7.13134 | -42.07851 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8e3eb0dd-42ed-3f77-9f62-b8d409c8f139 | -6.93235 | -42.89777 | 2026-09-21 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d315b5fc-710c-32ca-a5fc-726fb5456220 | -2.45848 | -49.2203 | 2026-09-21 04:00:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c825ed1-9367-3ca8-a79f-ef1f4de2583b | -4.68354 | -46.41346 | 2026-09-21 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 449a8549-8a0d-3f4a-852a-2695645c1c84 | -5.15196 | -45.64455 | 2026-09-21 04:00:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7fb2c62c-4171-3782-9143-2ff441c1293e | -7.13541 | -42.07922 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8b115898-3538-3e8a-a6ed-a619af1f2082 | -7.13193 | -42.07493 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 059360ca-6fc4-3196-a3c1-0ca52a196e0a | -6.57948 | -42.56329 | 2026-09-21 04:00:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 365f8fae-cdb4-36a4-8153-20656e777f35 | -6.84226 | -41.02187 | 2026-09-21 04:00:00 | NPP-375D | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 22bb2b37-dcf6-33f2-bff1-c38196a3d3ac | -6.31307 | -41.75235 | 2026-09-21 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f92d514-5689-384e-8569-0e183484c1d3 | -4.8463 | -40.52514 | 2026-09-21 04:00:00 | NPP-375D | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 85750a55-5eaa-3dca-a64c-cf0e0aefacab | -4.11578 | -46.39212 | 2026-09-21 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbd59a77-6b49-3ad7-a1fa-c2b3e14ec9a2 | -4.82884 | -43.52223 | 2026-09-21 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6743540-dc9d-379e-b5a7-5db833ba7901 | -6.91196 | -43.72253 | 2026-09-21 04:00:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc6f609a-55c9-3078-bab2-97663c72e8b0 | -3.34248 | -42.76714 | 2026-09-21 04:00:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 72671bca-6c4d-3b76-b376-b4ebc472e57e | -6.8376 | -45.56131 | 2026-09-21 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0d5c6b4-61d2-3bfa-9a22-06a26bd658db | -6.03642 | -46.6076 | 2026-09-21 04:00:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7438f52-14bf-3769-bb6b-461e29fe475c | -3.3372 | -42.77092 | 2026-09-21 04:00:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5c969bd0-de0d-3d86-ae2a-e26559f960a6 | -6.32377 | -43.37935 | 2026-09-21 04:00:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 675dd6a0-08c2-3076-9074-9d9094275c83 | -4.68143 | -46.41414 | 2026-09-21 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 835c3790-d134-3354-8b07-432ba030802b | -6.83299 | -46.04135 | 2026-09-21 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0125c481-855d-3c6d-8104-009662ecaf03 | -4.22456 | -48.61771 | 2026-09-21 04:00:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ff479108-9539-30ff-aa4b-59900e12dba0 | -7.02742 | -42.08029 | 2026-09-21 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 25b73306-4a27-3738-b39f-6dd0ce190a55 | -4.6879 | -40.14944 | 2026-09-21 04:00:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1813bda-ff3c-3594-bcb3-719641d53cb1 | -7.13854 | -43.68688 | 2026-09-21 04:00:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 590c5b00-465b-343f-b422-2845a39bfac9 | -6.91866 | -43.73821 | 2026-09-21 04:00:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3cee8ca6-3772-3e75-a172-945e6a1594ba | -2.45735 | -49.22696 | 2026-09-21 04:00:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b98cf70d-ef77-389c-9a30-5a05c2437d45 | -4.33816 | -46.37637 | 2026-09-21 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67c67e51-d31f-33f8-8e75-9ea84f43e2bc | -3.34321 | -42.76262 | 2026-09-21 04:00:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebe92eb0-021e-3a2a-b966-bc0d3108bcaa | -6.83239 | -45.56063 | 2026-09-21 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0c25c78-c4ec-3aa9-b257-c44f93a10f7f | -6.47152 | -42.77383 | 2026-09-21 04:00:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2cea66d2-79ee-3386-a468-29c3db791552 | -6.4722 | -42.76974 | 2026-09-21 04:00:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 74a2198f-5484-3417-a3bc-0d7dba1756ff | -6.47239 | -42.7764 | 2026-09-21 04:00:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d7206b99-d62f-31f0-96db-e0f991666b2e | -5.85609 | -49.78423 | 2026-09-21 04:00:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38f737f9-8b89-3144-aed5-b00588778489 | -4.17227 | -42.00748 | 2026-09-21 04:00:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ac2215d3-cb2a-35aa-9d1e-ec972f3cdf89 | -5.85494 | -49.79049 | 2026-09-21 04:00:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaf44327-12d8-337e-8142-886be4b6f990 | -6.98142 | -39.88942 | 2026-09-21 04:00:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 039fefae-23b5-3f75-95d8-c627dc97fa6e | -6.9108 | -42.91961 | 2026-09-21 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e8a2fd5c-8355-3a1d-a62c-2203cc6ddff3 | -6.29975 | -41.75753 | 2026-09-21 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d308bc39-353e-3e32-ab4b-a927c2cc2c00 | -5.27818 | -49.34203 | 2026-09-21 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README21.md)
