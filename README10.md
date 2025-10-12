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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbe62d67-4feb-300e-8ec4-a2243ee23e1a | -6.98463 | -42.03551 | 2025-10-12 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8aed1261-651f-3956-9ca4-ca83efbcc8cb | -7.64772 | -42.58294 | 2025-10-12 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 37d9c5e8-d084-3c03-8339-15445eaa3fcb | -5.73881 | -40.76869 | 2025-10-12 03:21:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 26e1ab8c-cf9e-3000-9d7f-65b7daa6db0c | -5.55448 | -41.3242 | 2025-10-12 03:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1c65d476-3851-3249-ae5f-ecb205ea9944 | -9.55627 | -43.02314 | 2025-10-12 03:21:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0a80c2c1-e10a-3422-bedc-4d972b3b0687 | -9.55727 | -43.01801 | 2025-10-12 03:21:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4b074cbc-8218-311b-ad03-cb4fdfcb576b | -5.47727 | -43.40011 | 2025-10-12 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a719f2c1-b41c-3998-8a97-e6450bf440df | -7.85091 | -44.52577 | 2025-10-12 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7fb0c989-a58f-38ec-a39c-04f9f491eeab | -3.87269 | -42.51875 | 2025-10-12 03:21:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e19e3c13-aa35-356a-9ffd-081e7b4185b7 | -7.51522 | -44.60642 | 2025-10-12 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| af5ac2e4-c2ee-3cd3-bd75-16c7855c5587 | -3.34324 | -42.16103 | 2025-10-12 03:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 59e396ae-7071-37f5-ba90-d37fd292d2a0 | -6.94667 | -38.57588 | 2025-10-12 03:21:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4915fc18-9133-3cc7-852a-e4bd524c5067 | -10.182 | -39.83248 | 2025-10-12 03:21:00 | NOAA-20 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 571be957-1afb-3271-85ba-f538bb144b35 | -7.5139 | -44.61322 | 2025-10-12 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 364b34b1-6fda-3961-8083-e8c30ed179a6 | -7.64876 | -42.57729 | 2025-10-12 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dcd97641-a38e-3d86-9c96-7cbdb3c5bcba | -7.80043 | -42.44107 | 2025-10-12 03:21:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b1c8f570-4b19-34b9-b169-304d21c15ecb | -6.36949 | -39.10403 | 2025-10-12 03:21:00 | NOAA-20 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c62ada79-7478-321f-8f86-5f521a238321 | -6.7478 | -42.81412 | 2025-10-12 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4f4b6c4d-13a9-3f80-928e-4ef5a861c5ae | -3.86595 | -42.51757 | 2025-10-12 03:21:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1a3f6976-0d4b-3b5a-a23e-80c3dde4cee6 | -7.43317 | -42.98149 | 2025-10-12 03:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6b967051-e722-3f50-9c60-3a7e4d318a0e | -4.81837 | -43.15403 | 2025-10-12 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 318cbd20-47f5-3b7e-b77a-f46be824c250 | -7.67752 | -42.57302 | 2025-10-12 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b5699c03-184c-32c4-b7b5-dd449325568f | -6.25497 | -43.03192 | 2025-10-12 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9ca763e9-da30-3272-b423-873167479d6e | -5.48334 | -43.40323 | 2025-10-12 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f342325-9589-32d8-a5b3-1fdfe0ab294c | -3.34225 | -42.16684 | 2025-10-12 03:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 14738057-9c42-399b-87a4-180739ba6b8b | -3.53009 | -39.77776 | 2025-10-12 03:21:00 | NOAA-20 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2a433b36-2aa0-366a-95cc-adc4899d47a2 | -6.50281 | -42.4443 | 2025-10-12 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 59cbe68a-957e-3b13-94a3-9ab30dc880a3 | -7.67656 | -42.57807 | 2025-10-12 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e3b739e3-bdb8-3930-b0dc-3573413f4eec | -4.67834 | -43.26183 | 2025-10-12 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c261fd1f-82be-3eb7-945c-6769d705fdd1 | -5.23473 | -37.5849 | 2025-10-12 03:21:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 91aabf56-b24d-39b7-9864-bcfb5ea5d2f2 | -6.75329 | -42.82099 | 2025-10-12 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1e432817-af98-3ee1-85b3-2d9e0ed6da95 | -7.80473 | -42.43412 | 2025-10-12 03:21:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ad9aaab2-598b-3f15-a6d9-775aa25b0d76 | -6.25167 | -43.02849 | 2025-10-12 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| adcebf56-27b2-3ef2-98a1-477607d61f86 | -7.49263 | -42.7704 | 2025-10-12 03:21:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 118e5d1c-9c07-305c-afb4-d655def7bb16 | -6.76603 | -42.83456 | 2025-10-12 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 31c0d07a-4ce5-3ffd-ad0c-516a8966efd5 | -6.73419 | -42.16279 | 2025-10-12 03:21:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 455c900e-b4d9-3cc7-9111-eda9916c5de6 | -3.5285 | -39.77757 | 2025-10-12 03:21:00 | NOAA-20 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 301e1555-972d-32d2-b6c4-cc0897af8133 | -6.76715 | -42.82836 | 2025-10-12 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 353b0547-9f75-3065-aad0-faad1bd27e36 | -4.40621 | -43.46996 | 2025-10-12 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc8dded1-2407-34d2-ae7f-a19eb7cf3e01 | -7.01495 | -42.10348 | 2025-10-12 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6a4bc574-5e76-3694-a1e7-e7cdd26563b3 | -5.4863 | -43.07429 | 2025-10-12 03:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 049776ba-3fa8-3714-8239-013183362645 | -6.94767 | -38.57011 | 2025-10-12 03:21:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 746550ed-9e9b-328c-8e65-92fd38081fcf | -6.76536 | -42.82895 | 2025-10-12 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d6711019-8b7f-3c22-8877-4ac5fbbb4369 | -7.48615 | -42.76926 | 2025-10-12 03:21:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f459f5f-0bce-31fb-81d5-e31c755ab986 | -7.65744 | -42.57456 | 2025-10-12 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5ace20ef-8435-3b97-9ad7-5290433fc417 | -7.80571 | -42.42894 | 2025-10-12 03:21:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e44c6971-f2a5-3939-b410-94b3f4fb7e59 | -6.76491 | -42.84078 | 2025-10-12 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2979ebcc-6418-3b3f-8b8d-c02b12c0e10d | -7.21428 | -39.90451 | 2025-10-12 03:21:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| efb6731d-8a7f-3b32-afff-e29e42644a6e | -10.18252 | -39.82961 | 2025-10-12 03:21:00 | NOAA-20 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9e522b98-df47-3969-a87b-df536b5b9b38 | -7.21364 | -39.90807 | 2025-10-12 03:21:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 894a94c2-6a31-3359-85b5-4acc864cc925 | -5.93072 | -40.88745 | 2025-10-12 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 54b86b5b-b964-386a-ace4-66d7e95306f4 | -7.85789 | -44.52776 | 2025-10-12 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 78f94fae-b3bf-3963-80b9-a427f9015b17 | -4.90264 | -40.08799 | 2025-10-12 03:21:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7c62263a-5582-3c79-bafc-6465228177fc | -4.40911 | -43.46921 | 2025-10-12 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01becdf6-288a-3c0d-9677-31e40922c2bf | -9.56263 | -43.02431 | 2025-10-12 03:21:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 42c6a575-6748-3b2b-9bf3-53d02a555ee5 | -3.60517 | -42.7508 | 2025-10-12 03:21:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52cf6e62-0f9e-3b9e-81ef-0b5174500488 | -6.73523 | -42.15707 | 2025-10-12 03:21:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd95c35d-90ee-3a6b-8b35-e2ba90634027 | -4.41321 | -43.47155 | 2025-10-12 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 020ffe57-221d-39ca-bc2a-254d7cef84e0 | -7.0096 | -42.09748 | 2025-10-12 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3922964c-86b0-3ef4-86fd-feb128a6a343 | -3.60406 | -42.75716 | 2025-10-12 03:21:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad5f4ade-1313-314e-aac5-39d7d0e0557e | -14.96285 | -44.94113 | 2025-10-12 03:23:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75db5e24-be21-3a46-9be2-d51e9d5ba950 | -10.76619 | -44.10278 | 2025-10-12 03:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85381ec8-addf-3af1-b189-69dca37d3bf1 | -15.68049 | -46.62762 | 2025-10-12 03:23:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 756d75a4-90ac-3ee0-9313-caa12d93812b | -13.49046 | -43.04035 | 2025-10-12 03:23:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 854c8ffa-49dc-3106-9eb9-4483119f453a | -13.54369 | -43.70304 | 2025-10-12 03:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| bcf4ec77-ca90-33c2-83b5-0975809d4344 | -11.75064 | -43.31774 | 2025-10-12 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 128d752b-57d5-3f00-bbf2-f8b273a59eb3 | -14.01889 | -43.49155 | 2025-10-12 03:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| d78e3655-d6a5-32ed-90aa-eade0fd4dd0a | -11.75784 | -43.31408 | 2025-10-12 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62dd3eb7-8d1d-3454-8e6f-b47fbe9b376e | -14.02626 | -43.49183 | 2025-10-12 03:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b8af8d58-6fe4-3a6c-976f-1e27478ef7f6 | -11.36722 | -44.01369 | 2025-10-12 03:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8e10d29-f484-39a4-8e1f-445e00e24f78 | -13.57066 | -46.34528 | 2025-10-12 03:23:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ae55d357-c4ee-3d68-b87b-100f51c5af5b | -11.66898 | -43.78675 | 2025-10-12 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 42e1933e-8f0d-3100-90ad-091fa46a91af | -11.67117 | -43.77595 | 2025-10-12 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9dd341da-473d-3282-a25e-850ed00b3490 | -11.75164 | -43.31275 | 2025-10-12 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1b9c7e7-062b-343e-a363-20680507e2c6 | -13.49407 | -43.03752 | 2025-10-12 03:23:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6a851b16-5345-3554-bf78-43abc1e9823a | -10.76325 | -44.10274 | 2025-10-12 03:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06ae5e3a-8ab0-3aa5-ac4c-e04ff12323fe | -11.36072 | -44.01226 | 2025-10-12 03:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fb834ca-6ea0-332b-b2af-fe730eb97168 | -13.49319 | -43.04194 | 2025-10-12 03:23:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2679db00-2d0f-3c20-8c39-db29c6313d01 | -16.1919 | -43.67196 | 2025-10-12 03:23:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2369396-7d7b-34c9-9aba-7f10cb01fe91 | -14.96158 | -44.94695 | 2025-10-12 03:23:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a597bc2-24bb-36aa-8404-d5cfde3b06bb | -11.36188 | -44.00665 | 2025-10-12 03:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4092b67-b717-345e-a3e9-83ef38be2a3b | -11.36219 | -44.00991 | 2025-10-12 03:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4aec5266-433d-3781-adc2-7c7ddab74cf5 | -10.76985 | -44.10416 | 2025-10-12 03:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95990c25-cb46-397f-9ee6-948d0caf97f3 | -11.67755 | -43.77733 | 2025-10-12 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 00109766-3c1c-35fc-a0ff-531f623d8670 | -14.02491 | -43.49293 | 2025-10-12 03:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 101a9cb4-226d-3f72-a1fb-6f9c8f943b45 | -11.72599 | -44.29313 | 2025-10-12 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93f8dcd4-9eb1-3b35-ab89-f873557d05ae | -11.35537 | -44.00526 | 2025-10-12 03:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5202bfd-3d7f-3c93-8a54-caf40cb06d21 | -10.17084 | -44.54376 | 2025-10-12 03:23:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f58c2d1-b429-3bb7-90fc-8d9f7ebd2eff | -13.38503 | -41.33046 | 2025-10-12 03:23:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 199532b2-8e12-3d19-99b8-11692960ea85 | -13.5447 | -43.69816 | 2025-10-12 03:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4dcc16ac-329f-37dd-8fcd-ff190bdf0f76 | -15.28533 | -46.14939 | 2025-10-12 03:23:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb08b64c-eb68-3172-b2f5-23f407acdfbb | -11.67008 | -43.78134 | 2025-10-12 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 73a65ff1-fddd-36f8-8252-8eec68079e70 | -11.67646 | -43.78273 | 2025-10-12 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1337676c-a042-344a-a721-0364c847cec1 | -13.03368 | -40.51425 | 2025-10-12 03:23:00 | NOAA-20 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8b9cf8fb-2a06-30d0-bb4b-e461fcb4c1c0 | -12.23633 | -45.34059 | 2025-10-12 03:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dd33c1a9-d9b9-3ee2-be9d-f08ca6572134 | -13.54344 | -43.69847 | 2025-10-12 03:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f55e887b-814a-34d2-95d1-6d8d7e78b206 | -11.49961 | -43.49443 | 2025-10-12 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8242d928-243a-3447-a811-77918a1b3021 | -10.17088 | -44.54209 | 2025-10-12 03:23:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3d845032-b880-3fe0-bd94-2698a1f70d04 | -13.5424 | -43.70334 | 2025-10-12 03:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 772e0cac-39ee-3b8b-8ab1-f0cda7c7ddd4 | -13.56897 | -46.35293 | 2025-10-12 03:23:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README11.md)
