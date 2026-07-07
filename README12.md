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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0e17260-ee58-3349-b27d-b28771016436 | -13.27258 | -54.34948 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 870461cc-9d60-3039-895a-e7bb17dcc89c | -12.67662 | -47.68083 | 2026-07-07 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30f76f2f-9099-3f04-b344-a9030739d733 | -12.36196 | -47.42692 | 2026-07-07 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4475859a-4d83-3ab1-9101-a11a6dbbf77f | -11.66488 | -44.56801 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8cf425d1-24bf-35c0-9c6c-c1acca9230eb | -13.31503 | -54.37234 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9233e24-ec01-3059-8eca-eedcb535bc5d | -13.28814 | -54.39563 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d411853-df2a-30c8-a67e-5bedd288c71c | -13.2579 | -54.3392 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 766a45ec-622d-3123-8197-589ec3c6e131 | -11.67264 | -44.56206 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30823031-237a-33e9-863a-ec48af10f869 | -13.2692 | -54.33823 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7aa6272c-d408-3bc9-99dd-d96144a5d529 | -13.53237 | -52.91783 | 2026-07-07 04:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4750b2ee-591a-38b2-82d0-cd4793af229e | -11.66655 | -44.55745 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddd3604c-e05e-3b3f-be8a-1c6db72b21c9 | -10.321 | -49.92367 | 2026-07-07 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07d7a19f-903e-3648-b5e4-5618bb936f4b | -11.65823 | -44.56693 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf2f173c-9ec8-323f-b390-f063155721a6 | -9.6346 | -47.81034 | 2026-07-07 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f51aabe-c308-347e-bd07-a7a11259b0af | -13.27699 | -54.36773 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ff761bd-afc4-386d-be8e-3b3019a6324d | -9.37673 | -44.7199 | 2026-07-07 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c01c235c-764f-36a7-8128-01e58df5f9cc | -13.29108 | -54.35289 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a0b80e7-e870-3594-b235-b004386d17b8 | -13.28309 | -54.33721 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c63bbb1d-f76d-34f4-8e11-95b2fcb8faf8 | -13.32103 | -54.37014 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e525642c-b245-3c9e-8a11-5fdd5e41d7c5 | -11.67764 | -44.55204 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e78f788-9bf6-38d4-b2ab-e0e42f63d782 | -15.51148 | -42.20621 | 2026-07-07 04:25:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 235f6c8b-1a23-3944-b910-1d6411824d86 | -11.04617 | -49.59647 | 2026-07-07 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95cdeadc-55a5-3ae5-bcf6-515869b3024e | -10.92954 | -43.0638 | 2026-07-07 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7bcc0c36-fb04-3e55-9602-8ac383d6b28e | -13.53967 | -52.91794 | 2026-07-07 04:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 139b7f80-99b2-35f3-a432-bd87bb379d0d | -13.28172 | -54.34407 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 042bf60b-0aec-3da3-9194-a9cbedbe58e0 | -11.40466 | -46.58092 | 2026-07-07 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74614abf-30bf-3df6-b38a-d83ffdfa64b6 | -13.26438 | -54.34735 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92bd511c-32ca-3757-9af0-769999811cb7 | -13.27037 | -54.34521 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a1551d53-ec37-3189-a60a-4649ecd7f07b | -11.66379 | -44.55339 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1300ec6-766b-3d82-be6b-80054f9a1e6e | -13.27104 | -54.34187 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ab54fcd0-5da0-3096-b564-f7d6e8a5108f | -12.68248 | -48.2136 | 2026-07-07 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9af84d8-4b19-3e84-b0d7-8d8e2a5eab82 | -11.67043 | -44.55447 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eaa3697a-8425-364d-9727-3ef72dc49712 | -11.6732 | -44.55854 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7fe2631f-c7e5-30a7-9630-200ba3a64ee5 | -10.85231 | -46.38905 | 2026-07-07 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 550a8e1d-82f3-35a8-ae89-4a23517b941d | -12.50569 | -48.2667 | 2026-07-07 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38dc9e05-7f19-3fa2-a998-7e9b8e33ccc5 | -13.2637 | -54.3507 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 68e5dd0a-38b1-3d13-918b-2325bcf91d16 | -11.62245 | -46.35977 | 2026-07-07 04:25:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f35a685d-bd4f-37ff-83fa-5d78bd7ae1e7 | -13.27968 | -54.35425 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7d83f3b-f20d-3243-a812-59cf423cd65c | -13.27171 | -54.33852 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a71d9d8c-1ef3-37f3-b6fe-ff77104db099 | -13.2824 | -54.34065 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f29a8af6-663f-3581-a652-293cb7f1b70c | -11.66211 | -44.56395 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9a5e0f5-cb13-367c-8079-8c645bab53e0 | -12.78857 | -44.50137 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e371949c-5aaa-31e2-bcd7-83a820f57794 | -13.27502 | -54.34973 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed5d467a-bc7b-3f61-802e-6cf666e2025c | -13.28708 | -54.34504 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44dca79b-f6dc-3aed-a0dd-449ec019c761 | -11.67708 | -44.55556 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2c58a5fe-c824-3a0c-ae51-5b6c20398276 | -13.26768 | -54.3586 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6450447-3ec3-35c6-8b06-7c10f9afa4c2 | -11.6599 | -44.55636 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34e79831-ce59-3307-80c4-ede0ebf29aa4 | -13.25187 | -54.22806 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49c5bf69-7d43-3c00-b940-f411bd0f982b | -13.31898 | -54.38056 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11f3328c-7903-32b5-a235-4e5a5b0db62c | -13.26776 | -54.2314 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3951698-33d1-3155-971d-8edca85908a7 | -12.75695 | -44.55064 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd11905a-a384-34e0-99af-adcc8d4cd6e8 | -11.66764 | -44.57207 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6964796a-f5b3-3cb0-89d7-fb554d224767 | -13.25658 | -54.346 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ce251bda-5ba3-3163-91a9-465fc8a670db | -13.07944 | -48.16762 | 2026-07-07 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36eddc9b-78ee-3d49-881b-b86ec6f9afca | -9.20267 | -45.31762 | 2026-07-07 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d50430e-8552-3f49-ba27-f4557ee08a0b | -12.76027 | -44.55119 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41b7f8fa-8dba-3905-bdec-0043d2f79e14 | -13.2864 | -54.34847 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b33d98f4-6a55-3b7e-8547-dc6d98cfbc0b | -11.65602 | -44.55934 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aa613d0-6aea-3cb0-bc13-8f2caaa5d506 | -13.27987 | -54.34051 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74d024a6-7f97-3d61-9371-9f91e7d0fdcb | -9.2351 | -50.14212 | 2026-07-07 04:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a6ac5ea-167a-3a12-840a-f18acd482d2c | -9.28655 | -49.57747 | 2026-07-07 04:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c284632-93f5-3bf1-af72-9b4e7b8db991 | -13.28971 | -54.35973 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72e8edd7-7ea0-3cf4-8cf4-8a21a2e1320d | -11.68594 | -44.56422 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e319a0c7-9782-39b2-8d23-132a48bbd861 | -15.00916 | -48.31636 | 2026-07-07 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbcf8856-72e2-3732-be7d-19baf2a83d83 | -13.26903 | -54.35189 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81b97c07-824e-3d93-bb8f-b109cb3450b6 | -11.84635 | -48.25253 | 2026-07-07 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ae9c974-26b3-3aa0-ad62-b05e7d526967 | -9.40572 | -48.01957 | 2026-07-07 04:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 865aa6d7-07e6-3819-92d2-17bb61ac9dec | -9.52782 | -48.16067 | 2026-07-07 04:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86af8a87-0a06-360f-a3d9-781169085b7a | -13.60187 | -56.61537 | 2026-07-07 04:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6934cf2c-349a-3d5f-b0c9-08bc17e9c0f3 | -11.48694 | -52.91585 | 2026-07-07 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ea7139-d794-3c49-8483-ccdf33eabc8e | -13.32172 | -54.36665 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3518fb6-f5aa-3c97-8597-ee8013b746ab | -11.64053 | -50.37071 | 2026-07-07 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2b51d4c-9508-3e66-93ce-52ab7ccd891c | -10.93517 | -43.07212 | 2026-07-07 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 537e7222-de2a-3cd1-ba2d-924ecb1d72bc | -12.78469 | -44.50437 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e02f1227-1ac4-3b5b-99e7-652bcfef49f4 | -12.75418 | -44.54656 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 831f6399-8e57-3edc-88ab-ca8ee493f3f7 | -9.28589 | -49.58132 | 2026-07-07 04:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57063e4b-7ce0-3db9-bacd-cf5cfa4be2f9 | -13.27399 | -54.37101 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87ec2057-c461-31d8-b857-377c0b0f2ea3 | -12.68614 | -48.21426 | 2026-07-07 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 709c1b01-c3d0-3256-847d-a29c1ea80402 | -12.35964 | -47.4235 | 2026-07-07 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc33ec3b-96cb-3fca-b20a-97cb6a2d28fe | -13.27129 | -54.35618 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 250fca15-15a2-385f-81e9-ffe2f070ce5c | -13.27306 | -54.23252 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44871a16-129c-3da8-9e01-84fa05de9389 | -11.6865 | -44.56071 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44396451-8144-314b-9b67-1d53b2b5aba8 | -13.27856 | -54.34731 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6d8962b-66aa-36e9-b9e6-20f2109d525e | -12.51012 | -48.26294 | 2026-07-07 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 983408f1-3b4b-3f9e-8976-19d17aaeece5 | -11.6815 | -44.57072 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd414fdb-75f7-37c5-a0b8-ec22be6b1b29 | -11.65214 | -44.56232 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 597afc56-8ef6-3ace-82aa-6829eb1a1630 | -11.40121 | -46.58034 | 2026-07-07 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3915386-dc45-3c49-bd3d-aa5c86a5c54c | -13.26596 | -54.355 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5b71bb8f-7410-322c-b63e-8852fbae322b | -13.26193 | -54.34708 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 59d612c6-3229-3132-96bf-69fe27a6cf04 | -13.27921 | -54.34392 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c883c582-bd1c-3c21-a3b5-9b9cc96fbb26 | -11.68982 | -44.56125 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb5250e2-ed55-3264-84a8-b3ecdc0125f3 | -10.3189 | -49.9112 | 2026-07-07 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 975508f4-ca79-3867-9ec3-fa17b1816c2b | -9.37559 | -44.72694 | 2026-07-07 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c115aa8-9835-3884-8ee2-d3ebce1f6cbc | -9.19592 | -45.31649 | 2026-07-07 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af360791-6c20-3d2a-80c6-55341ff3bd55 | -11.55671 | -52.79488 | 2026-07-07 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59eec8a2-3344-3eb7-9757-25965ed0c6c0 | -12.75751 | -44.5471 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d356e1ea-75f3-3400-8f09-13ef6f2f4399 | -13.31572 | -54.36886 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 531c86e4-0305-3775-b81a-7727e1c93c43 | -12.44921 | -49.58325 | 2026-07-07 04:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ec7b793-4e97-39ef-8823-9bb4ca4ac3d3 | -12.79577 | -44.49892 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6918c4c4-aebb-3d39-b76e-fd34069418f1 | -12.50795 | -48.25344 | 2026-07-07 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README13.md)
