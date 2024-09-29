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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cf1e178-695e-328d-b6e1-ebd94165a65f | -13.66054 | -42.13636 | 2024-09-29 04:04:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a277572d-3f48-3d22-96c8-3b406673895c | -13.37832 | -42.04863 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a05ca52d-0ecb-3a26-aec1-a5e20cbeaa13 | -13.36012 | -42.05647 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 057240da-2c2b-3b10-a9df-4a52b7ec78f8 | -13.35955 | -42.06004 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| de836caa-740a-3d01-9f3b-79e9e9a25651 | -13.35899 | -42.0636 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c601c956-0798-3264-88c4-1c33a2e02f43 | -13.35625 | -42.05947 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9a8d1194-0cda-31d8-bcd9-65165f1ad4d7 | -13.35238 | -42.06249 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 76ce2b1f-ef75-3c6f-bbd3-910da5a76be5 | -13.35181 | -42.06607 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 954feae2-ca33-3b76-b9fb-f6b2687d9ca4 | -13.34907 | -42.06194 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f42ad442-d33a-3e9f-bec1-59ff4cc7fa74 | -13.34851 | -42.06552 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2ca79ef9-d35f-34c5-9ffe-793c7df2fd79 | -13.3452 | -42.06496 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8bcbb456-ce5d-3e13-bf7d-f81323c88430 | -13.34463 | -42.06855 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 279b96a8-8b27-3841-949f-239c113265d4 | -13.3419 | -42.06441 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 5706ef75-dc62-3ac1-bb0a-91a04e220272 | -13.34132 | -42.06799 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| a5b6488c-640a-3a88-9dbf-49c35e927c54 | -13.32812 | -42.06571 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4cc1992d-3777-3cc9-a95d-7f225dd1a61c | -13.32152 | -42.06455 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 99fd9ba4-2365-3c64-b11a-64578cd7e11d | -13.31821 | -42.06401 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c16d2b77-c4de-3a3e-89f6-63a8be4633ba | -13.31764 | -42.06761 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a048ac7a-812a-38db-825b-a9df047f0e73 | -13.31159 | -42.06298 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47b84973-cd39-3afc-b810-60d663e773a5 | -13.19999 | -42.2495 | 2024-09-29 04:04:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d73ba489-7301-304d-860a-379ef66046ef | -13.19667 | -42.24895 | 2024-09-29 04:04:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 079eb81a-b574-322c-852d-0ad4d697a45d | -13.54776 | -43.44484 | 2024-09-29 04:04:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08e6ecbf-7ab0-3de0-a5b6-edc2d717878d | -13.54436 | -43.44426 | 2024-09-29 04:04:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5445ee3c-0a27-312e-96d3-dd321e68d28f | -14.75547 | -42.42215 | 2024-09-29 04:04:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 28908de7-d5ab-39a3-8c18-47d31262ea2a | -14.50377 | -42.97122 | 2024-09-29 04:04:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 15d74659-8ddc-36d6-9e3a-67d77a084f4a | -14.24286 | -42.77435 | 2024-09-29 04:04:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 682fcdf0-b30c-3c96-a4e6-543ac733d3a1 | -13.76749 | -42.61628 | 2024-09-29 04:04:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5728fe62-f424-312e-b318-8ed748c27cd0 | -14.86161 | -42.77886 | 2024-09-29 04:04:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 328e7643-c190-3e1e-98b6-58d5661cc5f0 | -13.73852 | -43.46158 | 2024-09-29 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16450f42-2db0-3fd4-a552-df2e16a5eafc | -13.73789 | -43.46535 | 2024-09-29 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44a3de1f-72bc-3045-9f83-b2991e402209 | -15.67629 | -43.23883 | 2024-09-29 04:04:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d884e6c8-1b60-3a03-a2ff-69433317214d | -16.49693 | -43.13173 | 2024-09-29 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 9a033e7e-3d6a-3257-9dda-32dcb72f8ec8 | -16.49361 | -43.13115 | 2024-09-29 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e576646-da45-3067-81cd-1dfb460f416f | -16.19519 | -43.12448 | 2024-09-29 04:04:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84691f2d-53b7-3b4c-8494-80c051ab162a | -15.20188 | -43.84271 | 2024-09-29 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f413d607-e390-3bee-a1ce-29187294e83d | -15.20125 | -43.84652 | 2024-09-29 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9bf2665-a187-30d1-a3ea-d4f9f6933dff | -15.19721 | -43.84973 | 2024-09-29 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0d18498-a64e-3abf-afab-945e00975205 | -15.19657 | -43.85354 | 2024-09-29 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d7176f4-bc46-3140-9d81-f09dfa230e19 | -15.19317 | -43.85294 | 2024-09-29 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f74fe64-25a2-3b29-b008-292c9142802c | -15.10695 | -43.84176 | 2024-09-29 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d84c6cb5-3e72-375b-8ed2-65c929919258 | -18.00334 | -43.69409 | 2024-09-29 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0ce3ff3-ffe9-3ab7-b2b8-784f18791709 | -17.94002 | -44.23928 | 2024-09-29 04:04:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b388930-3211-33bb-a3dc-b8470853da14 | -17.93941 | -44.24298 | 2024-09-29 04:04:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc0796c5-5e31-328d-b5ac-f8040b90dbb0 | -17.93604 | -44.24234 | 2024-09-29 04:04:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42fad237-47e5-3a1d-87a4-fd013b0502ef | -17.84309 | -44.43803 | 2024-09-29 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cfe2158-4b08-3ccb-80a0-970f667a8776 | -17.83436 | -44.44838 | 2024-09-29 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7feb9864-ecb4-3fda-8820-40867c42b9c6 | -17.83372 | -44.45223 | 2024-09-29 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38d98485-456f-3d95-a51c-0873749ba2da | -17.83289 | -44.43625 | 2024-09-29 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb059621-cc81-39ca-a9ce-eb94cd1b0be6 | -17.80195 | -44.47451 | 2024-09-29 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7014932e-a9be-3a28-bbd1-816a5673771f | -17.79596 | -43.31146 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff5f1aab-1a99-374c-9674-eb512667d532 | -17.79265 | -43.31089 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e84214f-d916-3c7d-ba78-537bea40e177 | -17.78875 | -43.31395 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| edb3072d-7bab-3bdb-bcb1-c4c4c68c60cb | -17.78543 | -43.31337 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41f3670b-8015-3cdf-8fec-87943316fef8 | -17.78505 | -43.29461 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35e26936-2460-35a0-a18c-2dec64331381 | -17.78446 | -43.29824 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a0e76de-79d7-3ffe-bff5-39865a4bb75b | -17.78387 | -43.30188 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d21bd13f-6641-3ed8-965f-3329989e9970 | -17.78329 | -43.30552 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c221280-b5ee-3d88-819e-9d7154141194 | -17.78173 | -43.29402 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 282fea9c-2e1f-378c-97d2-67a7e6b9069b | -17.78056 | -43.3013 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6da13f5a-598a-3c7c-adf5-83e4d7fd9df7 | -17.77802 | -43.33821 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8d411c3-14db-3eeb-b170-5035403d358e | -17.77763 | -43.31947 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29dc2ef1-660d-39d2-b99c-e48f79e22225 | -17.77684 | -43.34547 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6d60dd8-e849-310f-86fa-abeeeb280320 | -17.77645 | -43.32674 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ec156ee-a31f-3cd6-b19c-651a5de1f215 | -17.77528 | -43.334 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fd13d71-0f73-3011-962d-93816ad2e5b2 | -17.7747 | -43.33764 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a97c7e2-996a-33a7-9fd5-ff3e626ce725 | -17.77411 | -43.34127 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 259d4f89-8657-354c-a323-d2b2278337ab | -17.77353 | -43.3449 | 2024-09-29 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e16aeca9-3fc1-31cf-be87-e3d87519067b | -17.77294 | -43.34853 | 2024-09-29 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 755c22a9-133c-31db-ab21-bf610e4ce282 | -17.77276 | -43.3074 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8618f65b-cdad-35f0-b6b0-f085cdfc2cff | -17.77217 | -43.31102 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cef430d3-fd4a-3c3b-bd08-56f3aa153df9 | -17.77197 | -43.33342 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 490b9401-523d-35c3-8ef4-b8fd12c1c063 | -17.77159 | -43.31465 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b5643c5-625b-38ab-a2bb-b9d89599d6f0 | -17.7702 | -43.34433 | 2024-09-29 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ce6fc3f8-51e4-3fcf-b0b3-8323d0ab3798 | -17.76962 | -43.34797 | 2024-09-29 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6e22b2ad-2d89-3d5b-bc45-570c00e1e4dd | -17.76827 | -43.31406 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27ad28b7-5812-34e9-9c7c-3b61484c8092 | -17.76769 | -43.3177 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c1128a5-8444-3d76-aa83-b882bc153291 | -17.7671 | -43.32132 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9da2fb8b-d42f-34aa-bec8-83fa33857e94 | -17.76651 | -43.32495 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bfe2451a-5506-3409-9b70-c7ee4717e681 | -17.76496 | -43.31348 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a51d99b8-e587-318e-87ad-6d47239511cc | -17.76437 | -43.31711 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3df7b1b4-a118-3d69-ba5b-5d99f2ea6bb6 | -17.76379 | -43.32074 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7da2cc1-b94c-349a-a9fa-980b22d87554 | -17.76367 | -43.59557 | 2024-09-29 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 517f160b-55e1-309a-90c0-aad4fe9d115b | -17.7632 | -43.32437 | 2024-09-29 04:04:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b30d9d9-1b40-33e3-8e0c-bf576e0d98be | -17.63173 | -43.25345 | 2024-09-29 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c2d5bd0-56c5-3012-8199-8a0b3ea5d6fb | -17.63115 | -43.2571 | 2024-09-29 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b9f54963-6e46-3ac2-939a-1e3cc98d13f4 | -17.62783 | -43.25652 | 2024-09-29 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| badae6c4-e9cf-372c-9c45-9cdb0bc0e799 | -17.62724 | -43.26019 | 2024-09-29 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a847b8d8-4f6b-3d9f-bb5b-4c0a12e27e67 | -17.62452 | -43.25592 | 2024-09-29 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6c8171eb-2793-3dff-9964-63723998f63f | -17.51947 | -43.65146 | 2024-09-29 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6181b53-01b8-3e79-a590-9af0a00881b1 | -17.27358 | -43.17292 | 2024-09-29 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f17a9c4-af21-30d3-9887-f3ef2c9c2f61 | -17.26968 | -43.17596 | 2024-09-29 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fd4a2a3-c89e-341b-b431-a2cd4261cdb5 | -17.26072 | -43.18929 | 2024-09-29 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3286aa6-4ccd-3448-b2b3-17d9dbb2769d | -16.68008 | -43.88337 | 2024-09-29 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0117551-7e30-3332-989c-9f6955318276 | -18.28249 | -43.4825 | 2024-09-29 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a7ea47f-611e-3334-aed9-10466f46d34a | -19.20715 | -43.38525 | 2024-09-29 04:04:00 | NOAA-21 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ff65adc-4e44-33c8-9cad-c791d6458d1d | -18.09399 | -43.9684 | 2024-09-29 04:04:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64e0a479-9104-3b72-b305-9421da82bb4d | -18.09338 | -43.97211 | 2024-09-29 04:04:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 474aa869-9832-3972-93c2-9ac608e9242d | -18.05484 | -44.39231 | 2024-09-29 04:04:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee23c060-c0ee-30eb-b908-8cf2cd013e8a | -18.05421 | -44.39608 | 2024-09-29 04:04:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 04a31504-4e3e-3f53-b0a4-7bac835f7546 | -18.01383 | -44.31867 | 2024-09-29 04:04:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README34.md)
