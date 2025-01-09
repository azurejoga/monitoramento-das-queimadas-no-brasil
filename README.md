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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a28ccdbf-9910-33e2-af43-e26bcc81b851 | -10.1562 | -36.5694 | 2025-01-09 00:00:00 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 131.1 |
| e6beb962-a56d-39ff-8fb9-ecb937f83d6c | -10.1557 | -36.5963 | 2025-01-09 00:00:00 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 533468da-ca7c-3a78-b1fb-a5e3932da317 | -10.1755 | -36.5659 | 2025-01-09 00:00:00 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 112.3 |
| 7f45d660-c9a4-3aa9-bef0-c5504ad89d85 | -10.175 | -36.5928 | 2025-01-09 00:00:00 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.1 |
| e16a9a88-8d29-3f2d-9c47-cdaa60d92f0a | -10.15 | -36.57 | 2025-01-09 00:00:00 | MSG-03 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| a767e6f1-1298-3c0f-a429-f85aa9bcabb7 | -9.9691 | -36.2802 | 2025-01-09 00:10:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 96.1 |
| b1aa4439-655f-3e42-b03f-125e7c209244 | -10.35225 | -37.08282 | 2025-01-09 00:11:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 6cd2927c-f6d0-3d19-b9b9-7b733e7f7676 | -10.10788 | -36.27705 | 2025-01-09 00:11:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ff947d52-8653-35e7-b09a-ce90f7a68d55 | -10.16755 | -36.57431 | 2025-01-09 00:11:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 42.5 |
| c1ecab18-e02d-31ba-8af1-21c8b02b5e25 | -11.60576 | -38.19338 | 2025-01-09 00:11:00 | TERRA_M-M | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 89dc1c27-67d6-35a5-ba6d-904ebf643039 | -10.35359 | -37.09211 | 2025-01-09 00:11:00 | TERRA_M-M | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| b48166a9-92fa-3f4f-960d-99ab3e3d3529 | -10.25898 | -36.68824 | 2025-01-09 00:11:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| f32d078d-bb60-3114-b2be-b7646fa9bef7 | -10.16896 | -36.58395 | 2025-01-09 00:11:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 85.2 |
| b8e8486e-fc6f-3c4c-a7ef-d2cda405ad10 | -9.84931 | -37.17575 | 2025-01-09 00:11:00 | TERRA_M-M | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 5f352880-a3a1-3c9c-b7f5-800c7a574899 | -13.35554 | -39.36089 | 2025-01-09 00:11:00 | TERRA_M-M | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 2ac121c5-fd6b-3a28-aacf-e97a3f58075f | -10.16232 | -36.59066 | 2025-01-09 00:11:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8a104fff-1f48-3ae0-beea-e9a8102bda3b | -9.97048 | -36.29464 | 2025-01-09 00:11:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.7 |
| fea8b231-9498-3760-b311-1f7437d66aa7 | -9.97981 | -36.2932 | 2025-01-09 00:11:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 88320488-64d4-3fe1-aaff-69256472c7a6 | -11.48525 | -37.7957 | 2025-01-09 00:11:00 | TERRA_M-M | CRISTINÁPOLIS | SERGIPE | Brasil | 2801702 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| ad3ca568-5c97-3b2f-a1f7-3717e25cbdc5 | -9.21999 | -35.64982 | 2025-01-09 00:11:00 | TERRA_M-M | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| c1915af5-7080-3fc7-b461-0bfd9de1e312 | -11.48651 | -37.80468 | 2025-01-09 00:11:00 | TERRA_M-M | CRISTINÁPOLIS | SERGIPE | Brasil | 2801702 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 0a938a3a-b0a5-3dda-8451-670130ae3588 | -11.61337 | -37.5252 | 2025-01-09 00:11:00 | TERRA_M-M | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 276c3ea2-509b-3d63-96d4-2fc6c599cf7f | -8.70967 | -36.16687 | 2025-01-09 00:11:00 | TERRA_M-M | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 3cb95b00-a8b9-35d3-8555-d5f697ce8f34 | -10.09069 | -36.28995 | 2025-01-09 00:11:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| df270fa2-bd32-3298-a475-7372f284d2b0 | -13.04745 | -39.74033 | 2025-01-09 00:11:00 | TERRA_M-M | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 442684da-fadb-3ca6-8f9c-a8a8da33cf06 | -10.23655 | -36.66219 | 2025-01-09 00:11:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 0994812d-9850-366d-83ed-812fb8e75421 | -8.70817 | -36.15648 | 2025-01-09 00:11:00 | TERRA_M-M | JUREMA | PERNAMBUCO | Brasil | 2608404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 9f11f3b0-599a-3676-aa13-1393ec05d4a0 | -11.18781 | -37.45243 | 2025-01-09 00:11:00 | TERRA_M-M | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 03375d53-d07b-3fa3-b155-e763a0e50be7 | -9.96902 | -36.28464 | 2025-01-09 00:11:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| 09c7b8a8-57ef-3bc2-a560-02bb2b9f7f2c | -10.16095 | -36.58102 | 2025-01-09 00:11:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 37.4 |
| ecd5b35c-7af9-33fe-b93a-6a62794ab564 | -8.69696 | -35.23705 | 2025-01-09 00:11:00 | TERRA_M-M | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| d9c075f6-0608-39de-964c-4319b8a3083d | -9.97835 | -36.2832 | 2025-01-09 00:11:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 510bd250-b541-3d1d-858f-0015ba067f4f | -9.98875 | -36.48427 | 2025-01-09 00:11:00 | TERRA_M-M | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| c9dd637d-3b6f-3652-8a87-9cb39f67891a | -6.99577 | -35.21618 | 2025-01-09 00:13:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 3aa4c7f4-9926-38a5-82ee-b88caa1e5e2e | -4.33403 | -39.37019 | 2025-01-09 00:13:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b74fb78e-19a2-3ba3-9ee3-e0eee0cd848c | -5.60919 | -35.54306 | 2025-01-09 00:13:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 35a255b5-1fc3-3254-a31d-cb23e5887843 | -5.00697 | -37.60427 | 2025-01-09 00:13:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a452884b-1805-3c37-9c32-7f274bafe683 | -7.47706 | -35.09312 | 2025-01-09 00:13:00 | TERRA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 577565b5-58c3-3d3a-92a2-37a5d0e86416 | -4.41256 | -42.54953 | 2025-01-09 00:13:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| dbf70204-4330-3283-b610-6c77975f6a22 | -6.4116 | -35.14635 | 2025-01-09 00:13:00 | TERRA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| c754c4c3-2291-38c1-bac2-10c2f62aee03 | -6.40871 | -35.19962 | 2025-01-09 00:13:00 | TERRA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| c87c7371-dae0-37e4-987f-28431e7eaf59 | -7.71526 | -38.70089 | 2025-01-09 00:13:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1a696057-9c92-3d56-adbe-3cdbe8cd8a3a | -7.45333 | -37.1117 | 2025-01-09 00:13:00 | TERRA_M-M | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a1e893f0-669c-38fc-b533-760c303a0166 | -5.47782 | -37.22939 | 2025-01-09 00:13:00 | TERRA_M-M | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 432f8d5b-3749-3f62-90bd-5ba9168000c0 | -6.40969 | -35.13344 | 2025-01-09 00:13:00 | TERRA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 3ec6afe7-6d0c-3d7c-9b38-d4ca55082554 | -7.31767 | -34.97342 | 2025-01-09 00:13:00 | TERRA_M-M | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 67.5 |
| c155321a-6fb0-3425-a6ac-132edde9e522 | -7.56209 | -37.04393 | 2025-01-09 00:13:00 | TERRA_M-M | AMPARO | PARAÍBA | Brasil | 2500734 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 702b385c-b7cd-3975-91ee-6efd2a48cd42 | -6.4068 | -35.18674 | 2025-01-09 00:13:00 | TERRA_M-M | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 67894ae6-d9b1-3993-a5ae-0ae3805c3982 | -4.4012 | -42.53975 | 2025-01-09 00:13:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 5d1e7a32-085f-3630-9726-045bc0c3292b | -4.33281 | -39.36137 | 2025-01-09 00:13:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 71315e0d-940a-36f6-a116-c358f29503c0 | -5.59883 | -35.54469 | 2025-01-09 00:13:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 1ce2ce1d-60c2-3b0e-b870-577e3b327e8e | -7.13667 | -39.91378 | 2025-01-09 00:13:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2abe4559-d1ec-369d-ac4d-6e04e44c5b9b | -3.80914 | -43.22755 | 2025-01-09 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 08ef95c1-ed67-3180-9015-733f23f2e1d6 | -6.80515 | -35.24495 | 2025-01-09 00:13:00 | TERRA_M-M | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5e9172dc-bcf3-3bbb-ba89-529717462a7a | -2.99166 | -40.38498 | 2025-01-09 00:13:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 8f6be455-7a88-34b9-a1a8-73ae35c37872 | -4.79167 | -40.54621 | 2025-01-09 00:13:00 | TERRA_M-M | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 153a6c49-3150-31d3-a358-d7e395d428a0 | -8.15837 | -35.33363 | 2025-01-09 00:13:00 | TERRA_M-M | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 390d3bde-2f1f-3162-826d-76f38c706b3f | -7.43424 | -35.06724 | 2025-01-09 00:13:00 | TERRA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 27932b38-4fd7-3ba9-8c9f-c1dfcde5c695 | -4.41104 | -42.53839 | 2025-01-09 00:13:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 0c46f8d3-998d-3d3d-bbdf-3ca391a3529f | -7.31956 | -34.98623 | 2025-01-09 00:13:00 | TERRA_M-M | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 353723dd-ff06-3468-9808-f23b8ab741bf | -7.13544 | -39.90471 | 2025-01-09 00:13:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| eb4bcc81-ade4-3de3-83d5-58e774141362 | -4.40271 | -42.55088 | 2025-01-09 00:13:00 | TERRA_M-M | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 8c5afeb7-4ae0-3a64-8b4d-ad94c925e18c | -7.43237 | -35.05448 | 2025-01-09 00:13:00 | TERRA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 16a5af73-e899-375c-859c-6b24b745a6ac | -5.60069 | -35.55714 | 2025-01-09 00:13:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 883eb2a2-8efa-368d-9a74-aa2a4a77d14c | -2.99289 | -40.39384 | 2025-01-09 00:13:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ea84e875-b17e-39f9-bbd7-c58fa1a2fbe4 | -4.4121 | -42.5382 | 2025-01-09 00:20:00 | GOES-16 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 3cd09108-2add-36f0-8bed-e156627cf610 | -4.344 | -42.541302 | 2025-01-09 00:31:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 619e32af-4477-3e4f-855c-254756c0b437 | -7.0773 | -39.9062 | 2025-01-09 00:31:00 | METOP-C | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 62b69dc8-fd33-3e7c-ab1f-1423aa0d4a04 | -4.346 | -42.550098 | 2025-01-09 00:31:00 | METOP-C | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 40de777f-8278-32d6-ad56-c3af994c45cd | -4.0996 | -42.027802 | 2025-01-09 00:31:00 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 17edca45-42df-3b77-9fdd-6e1aaada8102 | -7.3314 | -42.786098 | 2025-01-09 00:31:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2752b11d-17aa-38b5-b1da-1cee6f390236 | -9.707 | -36.189301 | 2025-01-09 00:31:00 | METOP-C | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cbfcc950-d348-34f1-bec7-b85f27f9f032 | -9.7119 | -36.208199 | 2025-01-09 00:31:00 | METOP-C | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 70234d4d-077c-34f5-8b98-7f7b60320709 | -7.3295 | -42.778099 | 2025-01-09 00:31:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef86c92e-0c6e-390c-9649-1bbeb2cff9a8 | -5.3683 | -40.6856 | 2025-01-09 00:31:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 951e2931-2e40-3633-a207-fc3640018311 | -5.3656 | -40.6745 | 2025-01-09 00:31:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 981d43f3-2ed4-3d7c-b017-76d245fa8804 | -19.3057 | -53.7227 | 2025-01-09 01:10:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 131a749f-a5b2-33eb-bef1-82b822c00bb8 | -19.3052 | -53.7443 | 2025-01-09 01:10:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 5ba2b42b-feae-30f7-9a7e-9dcccf1f931b | -19.307899 | -53.728001 | 2025-01-09 01:13:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 724c6e15-1adc-394e-99b9-306380a94559 | -20.978701 | -49.730099 | 2025-01-09 01:13:00 | METOP-B | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8e4f3d5-e018-3343-92ef-2de948a03659 | -19.317699 | -53.7253 | 2025-01-09 01:13:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7312e039-fea2-396c-bd27-d4d9d0a20ddf | -19.310301 | -53.737801 | 2025-01-09 01:13:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bfb5dc36-fdff-3367-b225-ef5362c29f1d | -19.315399 | -53.7155 | 2025-01-09 01:13:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| efd1933d-e433-33f9-8943-2ff72e1e1e9a | 4.1742 | -60.523499 | 2025-01-09 01:13:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 93504f05-1556-31ca-a413-8258c3c1a130 | -19.305599 | -53.718201 | 2025-01-09 01:13:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cbfc0a2a-2f39-36d6-8eb3-dfd4b697aca6 | 4.1858 | -60.517601 | 2025-01-09 01:13:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f6ce152e-4c72-39bf-8031-bd4ecca9b274 | 4.176 | -60.5154 | 2025-01-09 01:13:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 001e89ab-5972-3c0b-9c4f-ab377cc4c61d | 4.1876 | -60.509499 | 2025-01-09 01:13:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fb1669fb-485f-3b8d-b386-a55b3cbe8277 | 2.5654 | -60.681099 | 2025-01-09 01:13:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c68ce19b-4b6f-3ab3-82fa-1b9ce1444e4e | 4.1778 | -60.507301 | 2025-01-09 01:13:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9d47a0e9-c214-3a20-b0bd-ff016fbd4cb6 | 3.869 | -60.878899 | 2025-01-09 01:13:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f963c504-8638-3260-b6e3-086e439cbf0d | -19.303101 | -53.708302 | 2025-01-09 01:13:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fe058ee3-bb48-333a-ad90-4cfb529d64a9 | -18.7691 | -55.949699 | 2025-01-09 01:13:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6aea4026-008e-3e54-bf9f-87f223d31ae4 | 4.3426 | -60.876801 | 2025-01-09 01:13:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0453b067-d6e7-36f3-8da3-78ca1bb90afd | 4.0534 | -61.16 | 2025-01-09 01:13:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f9141bde-8faa-3e3a-8bdc-63e41bf7e3f1 | 1.9387 | -60.859901 | 2025-01-09 01:13:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 649680ad-8085-3b1b-92ab-de89735eb5be | 4.0517 | -61.167599 | 2025-01-09 01:13:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5ea5cd36-bfee-3811-a9a5-2d111488cda6 | 4.1218 | -60.991001 | 2025-01-09 01:13:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 68fd187a-759e-32aa-a569-77c5dc4b8c28 | 4.1317 | -60.993099 | 2025-01-09 01:13:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 14e1381c-4062-3a18-8b55-a1f9be0f6ac7 | -9.9086 | -36.4254 | 2025-01-09 01:20:00 | GOES-16 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 252.6 |


[Clique aqui para ver as próximas entradas](README2.md)
