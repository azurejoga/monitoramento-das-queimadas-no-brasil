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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a05971f9-3b38-3f9d-9a3a-241b31d1e69b | -7.92476 | -44.88758 | 2024-10-24 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0aa8d608-0b4f-3dcb-a204-039447ddb57c | -7.91924 | -44.88688 | 2024-10-24 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4519884-a9e8-3c8d-947a-26267f07a75a | -10.50799 | -44.90617 | 2024-10-24 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99ea163c-0dbc-3a33-8837-a8fd8c43857a | -10.50579 | -44.90767 | 2024-10-24 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a31c8a8-3250-34ef-82e1-f6ff06c49515 | -10.50227 | -44.90557 | 2024-10-24 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6d771e6-7c61-3e9a-8016-94e4c570ee4c | -10.49397 | -45.15965 | 2024-10-24 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e6e5f4b-a2c3-3b84-ab34-39dca8d582be | -10.4935 | -45.16343 | 2024-10-24 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25988583-b5dc-3ba2-853b-5e08ec83e811 | -10.3766 | -45.08798 | 2024-10-24 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 31e46b14-e469-3c61-8188-4d8bd4d548dc | -10.37611 | -45.0918 | 2024-10-24 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e1fbd997-032a-3046-8a33-e707368f1bcc | -10.37366 | -45.08776 | 2024-10-24 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6efbfa11-c358-38c5-9087-387c0a3b1b40 | -10.37319 | -45.09162 | 2024-10-24 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f78b0e8c-1728-381a-afbc-0a793b98db19 | -10.371 | -45.0871 | 2024-10-24 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ace39c16-5dcb-3f15-8b89-46612b01360e | -10.3705 | -45.09095 | 2024-10-24 04:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0ee89f61-2429-39d9-bc75-1c856171a5a6 | -11.62913 | -44.92461 | 2024-10-24 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9a81e82-e08a-3842-9e81-9106813faf84 | -11.62388 | -44.91948 | 2024-10-24 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c426b129-26c1-3cdb-958b-8eaa5f157807 | -11.62336 | -44.92372 | 2024-10-24 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20932d72-df51-3402-ae92-30d678105afb | -11.6176 | -44.92282 | 2024-10-24 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3d6c554-35b8-3cd4-88a0-6ab74f1ef4c0 | -14.48361 | -45.52787 | 2024-10-24 04:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cfba0753-d091-3ce4-9a58-50ec6e099a94 | -14.47739 | -45.53122 | 2024-10-24 04:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73e3e1dc-0be3-3373-99f7-cdf005a02e18 | -14.47694 | -45.53529 | 2024-10-24 04:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17a22ab9-b9b0-3c1b-866e-d2467e742d8d | -14.47648 | -45.53937 | 2024-10-24 04:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ebf4a68-39ed-310b-b857-a7f1c18dbcb5 | -13.10441 | -49.12009 | 2024-10-24 04:57:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 606406f1-7ab8-3736-a0e0-d1e9077c98a4 | -8.9236 | -47.04842 | 2024-10-24 04:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40aaefe6-433c-32db-a2cd-88c23a3f93dc | -8.92287 | -47.05369 | 2024-10-24 04:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c0e4fab-4a17-38ab-ad4f-4f7bbc28494a | -7.89454 | -46.68809 | 2024-10-24 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cf30b5cf-0f4c-3abe-b0e2-8ffe24d1c315 | -7.89339 | -46.73154 | 2024-10-24 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fbc744b-2ad4-3bb8-8a0d-7396e121b8ae | -7.89042 | -46.68199 | 2024-10-24 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8d0652a-ff15-3773-9c30-027be942f6de | -7.88967 | -46.68739 | 2024-10-24 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5376c4a-e770-3bf3-8d5c-dda7f0fdb30a | -10.68774 | -47.54837 | 2024-10-24 04:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34f08dee-8b07-3bfb-8271-439b3bf87f12 | -9.54239 | -46.76937 | 2024-10-24 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 163c256d-5773-3e44-bc3a-00f928bd1eb5 | -11.28039 | -47.58189 | 2024-10-24 04:57:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 512c23fe-3550-31f0-a2ad-61b836144152 | -18.26563 | -48.24656 | 2024-10-24 04:59:00 | NPP-375D | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 137ad54d-a281-308c-bd5a-d32d803e4319 | -18.26265 | -48.24627 | 2024-10-24 04:59:00 | NPP-375D | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ca7b0be-ef08-35d9-8dcd-33570244eed0 | -18.26058 | -48.24586 | 2024-10-24 04:59:00 | NPP-375D | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e622e897-71ef-37c2-ad26-8f92accba114 | -15.78681 | -50.51768 | 2024-10-24 04:59:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0856cf6-b327-3a4c-b412-f2ec031e5959 | -16.76036 | -50.70698 | 2024-10-24 04:59:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 941796ce-f151-3ac1-b3e6-063d14e06bfa | -16.75615 | -50.70641 | 2024-10-24 04:59:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f047132-5da4-3085-a929-a654f5fc5127 | -16.75042 | -50.71759 | 2024-10-24 04:59:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2935bab3-aaad-3365-8c03-213966e0eb03 | -16.74672 | -50.71309 | 2024-10-24 04:59:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53b6419e-d31e-38ac-9f6e-14200066e849 | -16.74622 | -50.717 | 2024-10-24 04:59:00 | NPP-375D | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b09c1e2-10de-3672-9e8d-ca4283b0d99c | -18.31353 | -56.23612 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| dd25866f-a4f8-3767-9507-cd0eef1ee75a | -15.02914 | -52.83444 | 2024-10-24 04:59:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e28e346a-d476-3011-afd1-947363140739 | -14.82386 | -52.86728 | 2024-10-24 04:59:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b228378c-f32c-3b81-9a05-112a72850731 | -14.72355 | -52.78836 | 2024-10-24 04:59:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26909208-da34-3406-a2ce-a0c4587397ad | -14.45386 | -52.87911 | 2024-10-24 04:59:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b2676e7-985d-3467-a810-369eaeea48bc | -14.45325 | -52.8833 | 2024-10-24 04:59:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f65bdb20-6082-39d1-8209-1db096c02604 | -14.45263 | -52.8875 | 2024-10-24 04:59:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c623fb5-784a-3c91-84ec-1f62e76938a3 | -14.45027 | -52.87852 | 2024-10-24 04:59:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f15806c-75cb-3d94-be22-c5007bc68b45 | -15.8709 | -53.26237 | 2024-10-24 04:59:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 091394f4-81c2-38d2-acf8-63deb2d36b7f | -15.87031 | -53.26653 | 2024-10-24 04:59:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ed368195-984c-38b2-b9ad-ecba6882603d | -15.3172 | -53.31266 | 2024-10-24 04:59:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ca7c163-edd0-3402-af7f-b9027dd68987 | -15.3166 | -53.31681 | 2024-10-24 04:59:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15630cc6-eca2-3d58-99de-c43cf97718ff | -15.30949 | -53.31567 | 2024-10-24 04:59:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f97d2e5-c964-3d20-be4c-9b78dc876edf | -17.3223 | -54.99988 | 2024-10-24 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5f1f0f22-740c-37c3-bf67-42271d1fee5e | -18.30329 | -54.60946 | 2024-10-24 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4875e69e-f2ee-3426-a1c1-869d246a8de9 | -18.3027 | -54.61346 | 2024-10-24 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 339d427b-79b2-3715-a607-28bb3db5e1b7 | -18.31132 | -56.22823 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4346d1f6-8d6d-3ea0-9c7c-513e226dd2b1 | -16.40545 | -55.91919 | 2024-10-24 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| da2d93de-86a6-3200-af3b-8cd35d392902 | -16.40212 | -55.91863 | 2024-10-24 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d5396a01-f0e7-34b8-941d-6978870384e6 | -17.03062 | -56.0071 | 2024-10-24 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 14694c0a-7dfc-3068-9c3e-c69c39699bcf | -17.02785 | -56.00291 | 2024-10-24 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 98c67328-209d-3060-9aae-0758b1caaad2 | -17.02652 | -55.9995 | 2024-10-24 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 71ab78b2-a58c-39ff-859a-ff198e1fb5b7 | -17.02595 | -56.00314 | 2024-10-24 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f80f5d84-fdec-390b-953c-953523d4917a | -17.02539 | -56.00676 | 2024-10-24 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d505e0ea-965d-3824-ba5c-18bfa7af85bb | -17.02318 | -55.99894 | 2024-10-24 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7fad6886-2a76-3c12-865b-b5b1432679f8 | -17.02262 | -56.00258 | 2024-10-24 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 80a3f20a-2a6c-332f-bd56-c2fd70cea64e | -17.02206 | -56.00621 | 2024-10-24 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4bc50d00-4f24-3e43-923d-ab86429620dc | -16.56428 | -56.24538 | 2024-10-24 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 028567b6-f78a-31df-bc09-052977c9054c | -18.31033 | -56.14526 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5589e986-6a3e-327c-b017-49ed9a528984 | -18.30742 | -56.23133 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b2300d0f-ae17-3a0e-b148-b6127ebe9b48 | -18.30643 | -56.14837 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a5fc0ecb-b300-3753-8bed-964353cf83bc | -18.30351 | -56.23443 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| f0a411ea-53f7-3d0a-a7b3-ec7653d79e27 | -18.30309 | -56.1478 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 12e6612d-8c50-3f1d-ae0a-1f77a798969c | -18.30193 | -56.14452 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d4133c35-b21e-3a26-8cd3-8ae769e03ae7 | -18.30137 | -56.14819 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 24368cfe-ba31-357a-8f80-c99576ee4114 | -18.29206 | -56.075 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 02a775f4-af2a-357b-a610-07cdb60c968c | -18.17412 | -56.30706 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f3680910-66f5-30fb-9646-27c849f6b84a | -18.17023 | -56.31015 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 424c1310-6cd8-3345-8321-c59f9e7b75b7 | -18.32528 | -56.20426 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| db3cf8e0-c678-3412-8212-ef13781bc6e0 | -18.32025 | -56.2147 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b02b1b0e-468f-3e47-8a4c-1906e61519ac | -18.31691 | -56.21414 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e7188b00-fa1e-3967-84f9-13690bf18271 | -18.31526 | -56.20257 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7dde4709-ccf2-316d-b223-9a9e5d040c30 | -18.31255 | -56.15316 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 96dd88a0-1b17-334e-ac41-bf732d2e9f67 | -18.30685 | -56.235 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 8dd0d079-9676-392c-9663-a352022c48e1 | -18.29803 | -56.14762 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d3c832a5-0379-3615-99bc-e4374eb2ec1f | -18.16793 | -56.31025 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2469336a-7927-39a5-af84-1bf1c1117b93 | -18.16685 | -56.33207 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e31c7227-e873-3e36-bd51-1e13703c5f60 | -18.32194 | -56.2037 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d3a79092-8fcf-3047-820e-214a236806e7 | -18.31582 | -56.1989 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4a033f6a-741e-3ff6-b17d-8d3b1e2075d0 | -18.3147 | -56.20624 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2a4a3ad1-5ddd-3777-a4af-55a79d334891 | -18.31075 | -56.2319 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| bde1d2af-2bbe-3179-8dbb-43483b149984 | -18.31019 | -56.23556 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| c2716118-c7ab-3fcc-9e32-8ba0aed0cfa5 | -18.30586 | -56.15204 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1f622096-d372-386d-9b7e-ee9cb6a1e4fb | -18.30464 | -56.2271 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 68b60c90-02c0-3b6e-bffe-a86075beeaca | -18.17347 | -56.35558 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3237b60f-e9ef-379f-9ddf-1ad7a77d8056 | -18.32081 | -56.21103 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3ba91952-f0a7-3512-b410-0aba5f22cfc0 | -18.31409 | -56.23246 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 7f5ff538-0742-3606-9b02-e4c3b53b05c5 | -18.30755 | -56.14102 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4b64c1b3-3f8b-357d-bbb8-c524ddb6eb63 | -18.30477 | -56.12616 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1f747d02-e89e-30c1-82ef-9e8dcb1d73b0 | -18.30408 | -56.23077 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |


[Clique aqui para ver as próximas entradas](README81.md)
