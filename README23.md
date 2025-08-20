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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36f01620-b2a4-37c9-90ca-1b75169c9052 | -22.69586 | -47.33966 | 2025-08-20 04:12:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2f976679-f088-371f-8a84-17b39e75269a | -21.2747 | -45.40434 | 2025-08-20 04:12:00 | NOAA-21 | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 93f08d40-ddf2-34a2-91cd-8d0b3ebdd04c | -21.89358 | -47.23494 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c8f76644-2a13-3068-8f4d-60751aa033c7 | -23.39823 | -47.00975 | 2025-08-20 04:12:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b0438dc7-e42a-3b85-9e6f-05b9ae536ee1 | -21.19654 | -50.65982 | 2025-08-20 04:12:00 | NOAA-21 | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| affd6379-40fc-3a6b-a1d7-a5835bebaa44 | -20.34036 | -51.70339 | 2025-08-20 04:12:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fae64583-1978-3c61-915d-15e6af6558fa | -19.92924 | -43.9934 | 2025-08-20 04:12:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 69fcd8c1-7f99-3236-8857-7bed53e85717 | -20.54654 | -47.42164 | 2025-08-20 04:12:00 | NOAA-21 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d7546905-4324-30f5-86d3-dc65bcdae1e1 | -17.63814 | -52.20119 | 2025-08-20 04:12:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 883d697a-cb2d-3de1-a40a-db750b271463 | -19.87921 | -49.83689 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a986f567-b7fe-3ccf-9c31-bc057d3cf0f4 | -20.09551 | -47.59753 | 2025-08-20 04:12:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e237ec7e-cb4c-31e0-be9f-065fada395dc | -19.83977 | -47.32951 | 2025-08-20 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f81af23-f59d-3fb8-82a8-eb45369beca3 | -21.31979 | -48.67584 | 2025-08-20 04:12:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a4cddb0c-c7a3-3732-9b49-c9db22923b9f | -20.33946 | -51.7079 | 2025-08-20 04:12:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6eeb9b84-869a-3ff4-9461-418469506893 | -21.90573 | -47.22523 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 57de24f1-1aba-3489-8ad1-52b141265d41 | -18.67731 | -46.98335 | 2025-08-20 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b63c88d5-0bf0-3e06-b058-91129c173e25 | -20.34292 | -51.71346 | 2025-08-20 04:12:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a544b728-e7fe-3713-9991-88ee44c36227 | -23.97485 | -49.65066 | 2025-08-20 04:12:00 | NOAA-21 | SÃO JOSÉ DA BOA VISTA | PARANÁ | Brasil | 4125407 | 41 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a558c752-c858-33ca-8462-f414361efbec | -23.18843 | -47.10639 | 2025-08-20 04:12:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 13301267-c057-3974-a428-28f495964c17 | -21.84967 | -45.44571 | 2025-08-20 04:12:00 | NOAA-21 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e4893117-545f-35af-b6b9-05ddd7c5bbdc | -20.33767 | -51.71693 | 2025-08-20 04:12:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8e29fd1a-6876-3a33-a939-135d7728c10b | -19.88511 | -49.84914 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0e2c68e4-5167-358a-b4ee-2175cc29427d | -21.89633 | -48.18433 | 2025-08-20 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a99162f8-a0b8-37b4-95c5-9d7561372114 | -20.95535 | -46.10296 | 2025-08-20 04:12:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cef1c316-56f3-3457-aaef-5d7c745812bc | -21.90168 | -47.22848 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e532bcaa-16b1-38de-8cbc-ea180731a7a2 | -19.86154 | -49.82219 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| f3086508-1521-325c-b55d-5919c809e57e | -22.69247 | -47.339 | 2025-08-20 04:12:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bba937e5-1e88-30ad-b809-54726a38bec9 | -20.66267 | -43.24427 | 2025-08-20 04:12:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e480cc74-3dbe-3b79-829a-cf41b99b7663 | -19.01526 | -46.65299 | 2025-08-20 04:12:00 | NOAA-21 | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0fc3e34-ae73-3985-9cff-dbd96c193914 | -22.55572 | -49.77283 | 2025-08-20 04:12:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 8f9186a4-2d2e-3d07-80b7-c267d61ac5c2 | -18.67802 | -46.97925 | 2025-08-20 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3f12dc14-bd74-34ee-82c5-a61f5468918a | -20.52981 | -46.10358 | 2025-08-20 04:12:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f46434dd-31ba-3700-a7f1-8356598cf42a | -22.45507 | -47.55674 | 2025-08-20 04:12:00 | NOAA-21 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a21bbe93-149e-3d7a-bfe6-e91f798bcf7d | -19.85861 | -49.83804 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b7687348-63a2-343c-8318-37cd84b2b394 | -22.55631 | -49.77022 | 2025-08-20 04:12:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4f9fc61c-0704-3270-9ce1-c5f4fbdb9983 | -23.70064 | -50.23398 | 2025-08-20 04:12:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 91335a43-8f9b-3bd9-9164-50628a73249e | -19.45174 | -47.19305 | 2025-08-20 04:12:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 17aff3d1-b45a-3168-9735-c77a0ed45f08 | -20.95596 | -46.09921 | 2025-08-20 04:12:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16c3fcbe-dd2b-36ad-9528-532c77086e4a | -19.86842 | -49.82906 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 885f1e6b-5573-31bd-8bcb-d33874a1e02f | -18.67615 | -46.97985 | 2025-08-20 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| efb07c08-28d2-3d43-a5bf-ee0b37815569 | -19.87136 | -49.83522 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 75ffdf9b-a31b-3b8d-ba89-8375e672df3c | -21.29967 | -41.51236 | 2025-08-20 04:12:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 959b3f48-8aa4-3900-b6f1-5030d68127a8 | -23.19195 | -45.00746 | 2025-08-20 04:12:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f3645dd9-9671-331a-b1ce-be34405e3047 | -23.19655 | -46.68029 | 2025-08-20 04:12:00 | NOAA-21 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a0cad440-f2fd-3f7e-bdb9-80d2522aa106 | -21.31563 | -43.25461 | 2025-08-20 04:12:00 | NOAA-21 | RIO POMBA | MINAS GERAIS | Brasil | 3155801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 96809d7d-9062-35bd-beef-006a7f8f24b9 | -21.63363 | -49.84362 | 2025-08-20 04:12:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0c90c033-6294-3e0a-84c1-fc014e2a1d33 | -19.35641 | -47.93829 | 2025-08-20 04:12:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7023ff30-6404-3b0f-bf46-39a6b7db2fd7 | -19.73052 | -48.98014 | 2025-08-20 04:12:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df555d04-790b-3a6d-ad6d-5cfc759d9693 | -20.46912 | -45.07766 | 2025-08-20 04:12:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d3b5e441-112b-3033-864f-828411e64e21 | -20.95068 | -41.14514 | 2025-08-20 04:12:00 | NOAA-21 | ATÍLIO VIVACQUA | ESPÍRITO SANTO | Brasil | 3200706 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dafc4f83-749b-3335-8b03-c379427e290c | -20.10796 | -44.33782 | 2025-08-20 04:12:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 49696ab6-36c1-3ed3-8761-b76c64c9d173 | -20.47243 | -45.07824 | 2025-08-20 04:12:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 459b5c68-0771-3eac-9763-ddbaeb2c3dfa | -21.90748 | -47.23682 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 29a9fd81-37ee-397f-aa48-5a69f311c0a6 | -19.45521 | -47.19371 | 2025-08-20 04:12:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d27dd1b5-572d-366d-b9ce-e62b3120b18b | -21.90822 | -47.25319 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 49fa14da-124e-3822-8baf-f816fd50785a | -22.68908 | -47.33833 | 2025-08-20 04:12:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3e9ab367-c493-30f8-b17f-d0fa808f26fd | -23.35539 | -46.35536 | 2025-08-20 04:12:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f3855c9c-d291-324d-b8c4-22444196ac8c | -18.17836 | -47.89769 | 2025-08-20 04:12:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4e08495-21ae-319b-9c59-cf52c2f17d30 | -23.77127 | -48.86882 | 2025-08-20 04:12:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0271156-ba48-3ffe-b89c-33264d8de887 | -23.13751 | -46.92148 | 2025-08-20 04:12:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7ad4ad49-f8dd-3bb0-93ff-7fff85e911b2 | -23.39203 | -47.25642 | 2025-08-20 04:12:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 14335061-704b-3717-ac94-11336a3c2eb2 | -18.6822 | -46.97575 | 2025-08-20 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08c3fbe7-5260-347b-8f12-afb18577c8fe | -18.67872 | -46.97517 | 2025-08-20 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fe9946da-d957-355c-8a16-7a8a7195f453 | -19.11536 | -46.60173 | 2025-08-20 04:12:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bd5f169-ec94-355a-bf93-f4db793bee2f | -22.37272 | -42.87071 | 2025-08-20 04:12:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3f67c7e3-6620-3850-a5c8-75500d8c8a88 | -19.87234 | -49.8299 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2c282e30-1c22-3abc-a0f7-4d8c336ed9a0 | -18.6815 | -46.97984 | 2025-08-20 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b582eb14-4132-3c9e-979c-1fb1de21692e | -17.64289 | -52.20217 | 2025-08-20 04:12:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9da0acc7-ec9d-351f-9a08-77dab78b2d43 | -19.85763 | -49.82132 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 2155bc90-a5fc-37ba-a97e-3ce833b34cd3 | -23.18789 | -51.20106 | 2025-08-20 04:12:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b8e30107-c03e-35db-a929-8312c2b597da | -24.13276 | -49.12943 | 2025-08-20 04:12:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28fe1566-c3c3-3035-8e05-10f2bf7a2055 | -19.11877 | -46.60233 | 2025-08-20 04:12:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a904dcf-5378-38dd-b9a8-6361ccae9151 | -21.89705 | -48.18018 | 2025-08-20 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f72d53c-66c4-393d-9f07-1035af8b7559 | -22.71417 | -42.13718 | 2025-08-20 04:12:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4de117b1-f8fd-38c6-bdeb-61c34c832e7f | -18.313 | -48.86391 | 2025-08-20 04:12:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8dfe4c4a-65ff-32c4-896f-f34da96b47d2 | -20.93656 | -46.47198 | 2025-08-20 04:12:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c202fd64-6afe-3041-900c-b1bd65b37657 | -17.66811 | -54.05897 | 2025-08-20 04:12:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f807b3fc-2065-3d3d-8eda-798559c4f430 | -20.20329 | -44.68918 | 2025-08-20 04:12:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dd438675-5b86-33f3-8a38-d248952e518d | -23.99273 | -48.56195 | 2025-08-20 04:12:00 | NOAA-21 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2d20341d-21ad-338d-9eb8-3e5a759fbc5b | -19.85468 | -49.83718 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 80d9f89b-e8fd-3ee7-9f76-c5d4e92e35b8 | -18.67384 | -46.98274 | 2025-08-20 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4933055c-644f-3580-989a-1f7e1fedd3bd | -19.89097 | -49.83945 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a0b79a69-daa7-3f71-a4a8-a8d03475bd42 | -20.34381 | -51.70893 | 2025-08-20 04:12:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a4ece168-aad0-31b8-9da5-054ca6468ff5 | -23.98924 | -48.56124 | 2025-08-20 04:12:00 | NOAA-21 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c41d9d7b-6c89-3f72-bd33-ed5ee12635b2 | -23.3116 | -46.43639 | 2025-08-20 04:12:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e343ab69-28cf-334d-900d-b84b42e60d87 | -23.60667 | -46.37798 | 2025-08-20 04:12:00 | NOAA-21 | FERRAZ DE VASCONCELOS | SÃO PAULO | Brasil | 3515707 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5795f1ee-9256-33a2-a55b-4208fce72970 | -21.72528 | -46.49469 | 2025-08-20 04:12:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8c02f664-e749-3443-9853-1fd45d7d8cda | -20.22148 | -44.12987 | 2025-08-20 04:12:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f943f86a-b167-37e0-80b3-287c967fa825 | -18.18198 | -47.89844 | 2025-08-20 04:12:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2926b045-11b9-3e48-9674-d87c00469f7d | -20.01156 | -42.22598 | 2025-08-20 04:12:00 | NOAA-21 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4a0205c3-43ad-35b9-b8ae-f662eded0e35 | -20.04144 | -48.87826 | 2025-08-20 04:12:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85600448-2104-3606-8ab4-e89b9146ad8c | -18.8312 | -48.56359 | 2025-08-20 04:12:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87d618df-47f1-300e-bf4b-57d1b8ea3eb0 | -17.67088 | -54.06007 | 2025-08-20 04:12:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91c256da-33b9-3a36-a10f-9b0bc7410bb0 | -19.74321 | -47.90628 | 2025-08-20 04:12:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3db95af1-7644-3452-9d9a-2385d10d7122 | -19.8841 | -49.83248 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 54981a6e-711a-317b-9bdf-4eeca03a4336 | -21.13186 | -47.0363 | 2025-08-20 04:12:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e0d266a-5ec2-3588-9349-e1d02d327ee0 | -23.79522 | -48.87859 | 2025-08-20 04:12:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd208e03-bcc5-37e5-8007-7709be7436f0 | -22.44823 | -47.5554 | 2025-08-20 04:12:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5e5f2066-1ecd-307c-a4c4-b7e324e8db44 | -21.91162 | -47.25385 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1ca459e8-8c40-3748-8748-f5801b2ef2ec | -22.69313 | -47.33505 | 2025-08-20 04:12:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README24.md)
