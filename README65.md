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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6c38797-ee26-3b0c-84cb-b417bed7a82a | -9.71827 | -44.51642 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60087c39-9d12-3db6-a4f9-9dee709a9125 | -10.80883 | -47.97633 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc1ab277-552b-360d-8122-88f461632e7d | -9.71775 | -44.52028 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06953c36-8a2d-3347-9085-092ceee58d35 | -10.16654 | -47.11023 | 2025-10-16 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 729bb25a-d85b-30d5-95fd-8448fbe3b11f | -13.65654 | -43.92904 | 2025-10-16 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4a0968b3-92ab-36f8-970a-a08a32fad17c | -11.57262 | -48.56246 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92bcac95-2963-3c6e-85ad-3aadaea829fb | -14.43542 | -52.76567 | 2025-10-16 04:40:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91ae70d6-fc09-31ed-9185-bf13aca10fd5 | -11.13199 | -45.84943 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07a72d23-4dfc-3583-980c-a5e6b5cc955b | -8.39867 | -46.25964 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2a11cbd-edc2-3b5a-9516-583d0ea82666 | -8.83355 | -44.40781 | 2025-10-16 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59dc44b3-8134-3577-be8e-ed3e15f33ead | -8.45867 | -44.18571 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7072c9da-8470-3516-b927-2219a0dd41cd | -11.46019 | -47.6349 | 2025-10-16 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28d09b69-6f17-3b0c-987e-31117cd6c7f7 | -8.46352 | -44.18869 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1aa33c8-402c-37d2-8a09-ed69dc98c69a | -15.60523 | -42.66636 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc89f5b5-cc87-3c56-ade1-95470beed2e5 | -9.23294 | -48.59572 | 2025-10-16 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9342ae2-88f1-388c-9f5e-4bf015d88f57 | -14.27041 | -44.61403 | 2025-10-16 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ef8eab1-fc42-3d3f-93cd-96c1d4c388ea | -15.59921 | -42.39751 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de23a061-8ef7-3dbb-a8ea-0a5719f16c8f | -10.52691 | -43.37154 | 2025-10-16 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 898e40ee-32cd-3369-8dae-7c835569a994 | -12.06713 | -48.53436 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1550b501-702f-3844-af12-05cc634ded41 | -10.61598 | -45.23936 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13e08602-55ff-3f6b-b37b-0c2f791a7002 | -12.06404 | -51.20093 | 2025-10-16 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1be8b7d7-17e9-3b0e-a09a-e23b158707a9 | -11.46989 | -44.14595 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d947e0c8-bec0-35a3-91ae-c61f7f2f0c2b | -8.28582 | -45.40099 | 2025-10-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e546e9b9-259f-3e93-80c1-429f0972edf7 | -10.81612 | -44.00007 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 570b7e88-0f01-3e92-bfd5-2af3f710cc29 | -8.45984 | -44.18432 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f9c5ed6d-1f9f-3db0-a058-0ea2334380e1 | -8.46526 | -46.2426 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef8013a7-cd81-30d6-bc2a-c2a7ee179158 | -13.65257 | -43.92354 | 2025-10-16 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 611b363f-8f1e-397e-af3e-5e1f1a62e4f1 | -10.12669 | -44.55372 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| faee6dca-812c-318b-afe8-ed03fff66629 | -11.45624 | -44.014 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01bd4cf0-4e7c-344f-a0ca-ef877e19e410 | -10.97968 | -48.75306 | 2025-10-16 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3fcfccf-4a00-3066-b165-4796888a153c | -15.80634 | -42.45266 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49f96fa6-ee0d-3c54-9714-92258546b00f | -10.65586 | -45.24891 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa744763-31cb-3210-a12e-97135c6fd423 | -8.83302 | -44.41148 | 2025-10-16 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ae26d18-8322-3449-b895-6f88b53d5334 | -14.47151 | -43.83081 | 2025-10-16 04:40:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9f4efe5e-2d15-38b8-878a-9a018927342e | -11.58613 | -44.08467 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 98256655-1822-3e38-8955-3369f1af7abd | -11.43999 | -44.16824 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 898d68d4-e801-3103-a98f-f3c92b42c7fa | -10.92978 | -57.63625 | 2025-10-16 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 572efd62-2627-34ec-86f0-f80fed9ac56a | -10.1278 | -44.55329 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 09a53774-58eb-3522-ba6e-662a3c4afbd6 | -11.4891 | -44.10416 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa4d407a-8a25-3293-87fb-7da8a05d9202 | -11.57661 | -48.5592 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45992968-c2ad-3f66-8517-e7db771272cc | -11.75768 | -61.07655 | 2025-10-16 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb7b1bd8-dc87-3289-a34c-25ee53584f9a | -10.70067 | -44.43055 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7533578f-3ba3-3670-86bd-cd98499415b6 | -11.60173 | -48.55533 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d146690a-3771-38f4-b9aa-1eb0c28b9aca | -9.15209 | -41.06251 | 2025-10-16 04:40:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| e2d15920-18ae-3a5a-ba23-cba0f649ee4a | -11.42766 | -44.12658 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2afd8115-ca4b-38ed-a694-348372d500d4 | -9.68519 | -44.52872 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f9f507b0-31c1-3690-872e-9a30b447feb7 | -11.50379 | -44.05952 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fa411d1-5573-3256-82ce-cfadd4662f8a | -8.45617 | -44.17987 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ad189edd-e58c-38f4-b51e-289a18546bc0 | -10.85565 | -43.64017 | 2025-10-16 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c24ce20a-09d6-3d43-a8d0-21811be437ca | -9.23788 | -48.56301 | 2025-10-16 04:40:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49ffe3d0-1e06-38b9-b194-16cba15b421a | -11.35559 | -45.27025 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d95aeb84-637d-3499-b4bb-ceef91a079a3 | -10.89017 | -47.91971 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44d140f6-feb4-34db-802d-3a7ae0831dcd | -8.29575 | -44.96593 | 2025-10-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44613a17-a79e-3f77-bb6d-9fef3889a361 | -8.46772 | -44.18924 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 26033a52-624a-3f04-b639-6a4347eb64ad | -15.02536 | -47.31623 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61a8b173-bfee-36aa-a025-99aca09a62c9 | -10.15676 | -48.74043 | 2025-10-16 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99d22239-52c7-389d-b0c7-ae30474a01cd | -11.75453 | -61.07314 | 2025-10-16 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9881b7c6-b31b-35c0-8f82-d8a42d343043 | -10.12759 | -44.57748 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 67d9b81a-f9f0-37b8-8fc1-1d0de99f4610 | -10.13308 | -44.57755 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8fa9787b-7043-319c-97e0-e1cddddf5f83 | -8.56587 | -44.59042 | 2025-10-16 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aca2d162-3795-3156-a1ed-891e7b8411ad | -13.89758 | -50.65907 | 2025-10-16 04:40:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67be7690-c246-37c1-bcef-0d9ba9d89aaf | -11.59176 | -44.07647 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12321064-3e02-3e32-a4dc-625bcc03126f | -15.78439 | -43.65181 | 2025-10-16 04:40:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 136c57f3-cba7-3e21-af91-ec5864faf9d0 | -10.05872 | -43.85725 | 2025-10-16 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adeab6a5-10c6-3478-8ba2-22f38ba9397d | -11.44556 | -44.16018 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca796bd8-6f90-345e-a6a1-4f2c0faaf4be | -9.7188 | -44.51256 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b4259186-a8ea-3002-86ed-465879bd563e | -8.56178 | -44.58977 | 2025-10-16 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 353d3393-09be-315b-8fa9-2d8caf9330b2 | -10.12396 | -44.57296 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6e87d7e-3d90-3d2b-8566-f8f62830050c | -10.97685 | -48.74886 | 2025-10-16 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02a7a2c1-50ba-3a71-9bf4-b9e6fc77b6b0 | -9.68683 | -44.51719 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ced71590-fa37-3fdb-ac91-cfc7e32a0be8 | -10.832 | -43.94952 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dec49bc4-5bbd-3717-8419-fdba010b36bb | -10.12521 | -44.57255 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 93b1c63d-76ad-3ddf-b14b-a2b7fcda10d1 | -14.03144 | -50.56434 | 2025-10-16 04:40:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3780399-9053-30db-bd8a-33ded52dd296 | -11.47857 | -44.14986 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3c6d101-1b13-32ef-9b62-3507ca296e19 | -10.89365 | -47.92031 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca9fd6f9-dc0c-3516-b82d-84ef9c7d83b1 | -10.66377 | -45.30906 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cf78237-bcbd-3a56-9177-41cdf69ed4b9 | -11.3269 | -41.67162 | 2025-10-16 04:40:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5e84d415-5587-393e-b8d8-dae5ebbc0dcf | -12.03177 | -47.65919 | 2025-10-16 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9bf64f11-815f-3782-9fe9-2bbd4e818ee4 | -11.44027 | -54.09636 | 2025-10-16 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b368fd0a-94ce-38db-bbdb-af819121c706 | -11.44058 | -44.1639 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b538a0f0-3fb6-39cc-a544-97f03c76e2c0 | -10.05548 | -43.84804 | 2025-10-16 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ac18b99-b66d-3142-9b91-ba4558bed022 | -10.63421 | -44.41453 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b1954bd-3e87-3237-bd19-f231d1f22526 | -13.69727 | -43.71001 | 2025-10-16 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 011512d0-4468-34b5-aa4d-a707e2ee22cd | -9.06583 | -48.84924 | 2025-10-16 04:40:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b74183c-d9a8-364a-a405-297a5341ba24 | -12.22647 | -43.30042 | 2025-10-16 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82660846-7f7a-3a9b-a781-771c4250762e | -11.54265 | -49.92276 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4bf9002c-a7f5-3783-be75-48b2d589d23a | -12.22805 | -43.31031 | 2025-10-16 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af1afc20-47c2-30b3-9f39-e130ccca137c | -15.59395 | -42.39693 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0e64ebb-e49e-3e26-b9c0-872814216ef2 | -10.61903 | -45.24711 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41a482f4-4b97-3536-b8fe-54564bb95d8d | -9.6812 | -44.49669 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d48ba51-0bb1-307b-bbe7-a7f82cd4c71a | -9.26033 | -44.35632 | 2025-10-16 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 118bcd3f-4353-3826-8a55-960039f6278a | -8.30272 | -44.97392 | 2025-10-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 358262d6-23fb-3895-a94b-f7662b0d576e | -15.59432 | -42.39362 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72e884b7-8748-3e24-98eb-4a9ffdce9ee9 | -8.45503 | -44.18129 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f0deffc9-f40b-3b0b-a7ba-13d5fd8401c6 | -11.42973 | -44.14465 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f3a0c7c-0738-368d-ba62-318cd56a53b7 | -9.16332 | -46.86606 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c14de85c-a7cb-3f6d-a03d-bab4d04c4376 | -12.71914 | -48.65051 | 2025-10-16 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46e8ed6c-732d-3d1b-accb-5b7bcd62bd4c | -10.90647 | -47.93013 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aab18213-2e06-39a7-bdb9-16ab551d1fd1 | -9.73829 | -48.07767 | 2025-10-16 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9f7c1be-f631-3fea-9e45-0a32ed0c9c19 | -12.05907 | -51.21095 | 2025-10-16 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README66.md)
