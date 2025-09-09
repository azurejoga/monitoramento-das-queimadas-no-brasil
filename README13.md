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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08e8c69b-ece7-3577-acee-b054c44d927e | -6.03842 | -45.01407 | 2025-09-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6aa36f8-a0b6-3216-ad7b-26988b5c5f26 | -5.57396 | -45.0408 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7eebdc52-bd9b-3e8c-9fe1-f051b10a5241 | -7.56413 | -44.6626 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32a933e1-d9c7-3d7c-b3c4-e66a3d8add56 | -5.88199 | -43.95173 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 777f69ae-cc4d-342f-83fd-262f3c57eca7 | -5.68074 | -43.8994 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9c42c9d-9a2f-359b-9a92-04bf13f4ccf9 | -5.84828 | -44.20441 | 2025-09-09 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10fb6611-6734-3a23-9233-580aa421dc33 | -11.43617 | -43.68825 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62e182f8-12af-3099-9dcc-9a5a144f179f | -8.19816 | -44.76789 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 73812317-4248-33c4-8634-4a458511d413 | -6.86572 | -45.60229 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d5952d0-c1cb-3f74-bd31-590fc31d0fc3 | -7.72148 | -35.13448 | 2025-09-09 03:42:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8b18eb8b-05d5-3288-b6a5-a62cd139234e | -5.6982 | -43.89381 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad3a2a41-0a7d-33f9-82b3-3f286ea4cbcf | -8.42675 | -47.29044 | 2025-09-09 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fe028a4b-c3ad-3bf6-a53b-a41c156699f9 | -8.21244 | -44.77051 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9d80ff8-d324-3648-82b5-1bd1926aabb7 | -8.40436 | -49.10344 | 2025-09-09 03:42:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34edcbba-4fdb-3feb-a561-25acbbf889bf | -8.04466 | -44.06253 | 2025-09-09 03:42:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d44c36c4-09de-30aa-96f7-217cfb5ceed8 | -10.33839 | -47.73841 | 2025-09-09 03:42:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fcf14dc-7dcb-3ee4-94d3-af089e2ce279 | -10.17389 | -46.22299 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea955f1f-3bf2-32f2-b606-9a25632f0add | -10.7443 | -47.73886 | 2025-09-09 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f474eb03-3dc0-3ce8-8197-61414aae99f0 | -9.1526 | -45.57971 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f339c33-b3bc-3346-a719-5a575039a3a5 | -5.71628 | -45.40976 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6248e6b1-5266-305c-ac3a-db9813137082 | -5.54325 | -45.16875 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 889c23ee-c832-308a-9c5a-ce1135530f8a | -8.37713 | -45.01722 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 957394f1-f709-304a-9304-b039eac36dc0 | -5.57743 | -45.03838 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d8344ed3-e0b4-303d-a9ef-284842e8d08b | -10.74281 | -46.33091 | 2025-09-09 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50b03180-ef1c-3932-8001-f80174bd78d8 | -6.41415 | -44.48959 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f92841b-21f6-339e-a1e8-12e15d22caaf | -6.35661 | -43.03271 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 423f84e7-e442-3ded-aea0-e37748b54cd5 | -10.96457 | -45.09678 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 81fd995a-6144-3e02-af89-ab3df96c3afb | -9.13546 | -45.58003 | 2025-09-09 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c07fa3a9-865d-3737-8574-dc9e4417410a | -6.83157 | -44.89269 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 025df89b-fb50-3dbd-a386-d8571614a5c5 | -6.39678 | -44.431 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 88104b59-a830-39ae-b886-8d89a01efd1a | -5.8182 | -43.97798 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d17f1b8b-e492-3d6b-8cf2-690608ae46a5 | -5.83528 | -44.09856 | 2025-09-09 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5512d331-6dd3-39f6-9200-1836da98e690 | -10.96945 | -45.12191 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 3478ca9b-8432-3d68-aadc-28063e5c9cb0 | -8.03547 | -48.62167 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbe073ca-4f24-3332-b9eb-6595eca7b2cd | -10.98073 | -45.09621 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0859b3e0-c5b3-3e56-b2f6-74f34dd2ae86 | -6.17378 | -43.38208 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9419ffe6-5069-32b3-9eb7-2ee623dd85ea | -8.40308 | -49.10997 | 2025-09-09 03:42:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f71dc54-c100-354b-9f0a-8e6b1ee8777c | -5.67505 | -43.90298 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc525ffd-2cea-3ff0-9296-8f9c687b9e17 | -6.0602 | -43.11852 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bb042554-3563-30f5-abb1-ecf803b01996 | -11.42272 | -43.60307 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8420fca4-9b11-3f74-a625-f2fb196a9929 | -10.73716 | -46.33003 | 2025-09-09 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1314331-caae-3cae-a53b-67a808184e08 | -6.19589 | -43.37312 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 014b8ff8-702a-357d-b37e-0d40e21f3356 | -5.93538 | -44.8926 | 2025-09-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc65a37f-6ff3-36a2-880e-872597834eb2 | -5.57963 | -45.04166 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 3f8d6204-ecb3-3ef3-b9f0-19aa59877d2d | -6.40039 | -44.44186 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 051b391e-07a2-3627-989a-e9a92ce180a2 | -7.71476 | -44.74974 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a573e97-9b43-3b22-a523-3d9f15905029 | -5.72206 | -45.41067 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1dd7630-64ef-31ea-b5a2-7bbada03a570 | -11.37053 | -43.52264 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 742ccbf3-672c-39f6-abfe-ebfc1b3db3b7 | -6.61779 | -43.99956 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51a1070a-2206-3a5f-a525-9cfd7cc873d8 | -6.4804 | -41.76408 | 2025-09-09 03:42:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 96dbbac1-f73d-390c-acc0-d92fc2cb48e8 | -5.98505 | -43.70053 | 2025-09-09 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84c6cb04-ece0-32a5-b48d-567b21641c6e | -5.94206 | -44.89328 | 2025-09-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6600449f-344e-30f7-84ff-05c08afea170 | -11.43344 | -43.68954 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 374c605a-7fb8-3271-a996-c50b57603bf3 | -11.42736 | -43.60394 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 098f8cbe-9e0d-37a8-a4b0-db0b746063d9 | -7.25351 | -44.82064 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81c540e5-3a72-3a36-bf77-da22dff88960 | -10.96428 | -45.12094 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 17e1c339-03cc-367b-9ebb-2eaa224e0364 | -5.83638 | -44.2097 | 2025-09-09 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6744a335-b9e1-398b-9e28-c730d0c43f02 | -8.37426 | -45.02032 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03a84290-45d7-323f-9e21-51dd83025c4f | -5.72415 | -45.40123 | 2025-09-09 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a0643c9-699e-32f7-9860-2a75eaa7438c | -8.11337 | -44.87165 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a52ef61d-bfc2-327b-90e2-2b84a0cd4c94 | -10.96073 | -46.81057 | 2025-09-09 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64e6138d-6b32-3285-8731-cadc3a2747dc | -5.35715 | -44.80153 | 2025-09-09 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 316d203e-c3ee-3832-bc1e-0380edbabddd | -8.33715 | -45.07178 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 795703dc-1687-30e9-9d26-b96160843ebe | -9.82195 | -46.03498 | 2025-09-09 03:42:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0823838d-1358-33b1-83fb-ea319b89b7c0 | -8.37308 | -45.02694 | 2025-09-09 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c3ad770-d989-3c66-b960-7b67614f75fc | -6.87481 | -47.90858 | 2025-09-09 03:42:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08844678-0323-31fc-b1d8-5f434a3ec55c | -6.38713 | -44.45449 | 2025-09-09 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8d877a5-43db-3e61-837f-2baebccb261c | -10.96669 | -45.11365 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 898cfcfa-a7d7-3cf7-a8e2-617f2c9bf9c1 | -6.10277 | -44.13955 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a94fdf3-3ad5-3799-bafa-20d0de345722 | -8.04412 | -44.06548 | 2025-09-09 03:42:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01c11e20-4cd6-35fd-ab6b-8b5ed6de1daf | -5.92108 | -45.76818 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a5fd080-f16b-3e5a-b06a-378a83d8dd64 | -10.96888 | -45.12505 | 2025-09-09 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 17977e94-3ad5-3be6-ac07-758f7d7ef781 | -7.24578 | -44.82225 | 2025-09-09 03:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a20a351b-ad39-366b-a398-8828e1321570 | -5.69764 | -43.897 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f294550e-c13e-379f-bee0-f1e528772d02 | -5.83205 | -44.21306 | 2025-09-09 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 844d7700-ce85-3514-a14d-85c2fbc39e40 | -8.03168 | -48.63048 | 2025-09-09 03:42:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7716f339-7ce1-345b-a01c-1b7a29f5c59f | -11.41705 | -43.5816 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a940505-7bb7-32ea-b7d9-41ef95512858 | -6.20288 | -43.39185 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88e4ad0b-4b11-3bba-a82f-699ad7938537 | -11.43243 | -43.68225 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc263f91-7d7b-3617-8c23-4d41e934cc15 | -6.89354 | -45.80795 | 2025-09-09 03:42:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cb362cc-44f0-30ce-9bf2-5020fdc20dd3 | -7.28329 | -44.5659 | 2025-09-09 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46bc587f-660a-3dec-83da-06f2d3cab211 | -11.37502 | -43.53078 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ba927d2-1d96-37a7-997e-656c239245b2 | -6.61726 | -44.00265 | 2025-09-09 03:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25217dd0-aedf-3ea6-9869-13f4afdccd6b | -6.21887 | -43.50709 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4b0643c-3ad9-328b-80a6-20589e9b75b1 | -6.48351 | -41.76305 | 2025-09-09 03:42:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9fc51837-0c3a-31fe-9898-29b3e140665e | -6.30353 | -43.82178 | 2025-09-09 03:42:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10ccaedf-3e45-3c65-97e3-3c50bc371170 | -6.83154 | -43.62096 | 2025-09-09 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fd3b10a-85bf-3485-9de0-53123738f224 | -9.43594 | -46.73738 | 2025-09-09 03:42:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a6743ed-9fe4-3101-b1a2-110fa90ccef1 | -7.07519 | -45.20685 | 2025-09-09 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3771cde1-0618-3970-8be6-c287b9c89889 | -7.07586 | -45.20319 | 2025-09-09 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a6b3d04a-6a66-3d9e-a95b-e65c72504c8a | -5.88762 | -43.9521 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf34a311-df23-3c73-ae78-a143da76291f | -11.36873 | -43.53231 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b1362da-2fc9-3a0b-8b9e-3833ae992509 | -5.48072 | -44.12215 | 2025-09-09 03:42:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b75e1e1-abe7-339c-955b-53863e10c549 | -6.20615 | -43.31528 | 2025-09-09 03:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fec1378b-84bd-3cc9-b748-3a6dcb5d6856 | -11.37127 | -43.52504 | 2025-09-09 03:42:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6434cee-6589-329c-ac7e-3d24a9236faf | -5.69185 | -43.89931 | 2025-09-09 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 587ce1df-8b3d-3efb-867a-ac2cd71f477c | -6.20456 | -41.01827 | 2025-09-09 03:42:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4edda49d-9b70-30a5-b7f0-d4ccbca58f14 | -8.40561 | -49.09707 | 2025-09-09 03:42:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4d5621a-ae58-3d3d-abca-08ee9392f23c | -5.81161 | -45.65102 | 2025-09-09 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d177e18-3d11-31c8-9122-8fb62c997885 | -6.56252 | -42.94602 | 2025-09-09 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README14.md)
