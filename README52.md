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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fcdd4e9-14d1-3c18-ab08-459d542a4a4f | -5.19111 | -45.06724 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6aa0f50a-8c29-3dc2-af4f-81b6a9f82eb5 | -4.31804 | -48.09507 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 02ff2140-2767-3650-9389-7ca29a7e9df0 | -5.29802 | -43.10896 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a49356c-c05c-38dd-b962-afafb8ba6574 | -5.93478 | -42.88443 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6375933f-a179-32e7-9b9f-78a601adda02 | -7.80098 | -42.54929 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 75d117b2-0393-3bd5-9a78-fa4803941cb0 | -7.73745 | -42.60742 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5cb1ef6b-6bc3-39e4-bfcd-8443f0d0074e | -7.70669 | -42.56679 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0241a61d-97fc-3ae0-adf0-202634c3261e | -6.52649 | -43.37527 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a82960a2-5a12-3b32-bd13-cf325935bae2 | -5.98111 | -44.15126 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2ed56d3-eb5c-36e3-8780-7d115f003f11 | -5.37452 | -43.59169 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85fb9edf-dc32-36b1-88a3-f1cb28426e9c | -6.76785 | -43.60973 | 2025-10-04 04:12:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a64342b-283e-3a6a-928a-c0e4df273569 | -7.69563 | -42.57223 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 497390d0-034b-3a31-b938-c5ab95bea08b | -6.65352 | -42.80704 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03259eba-0667-394c-9536-cfc8ac6f6915 | -4.40928 | -41.46201 | 2025-10-04 04:12:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 14742edd-c509-3a0e-830e-514ec3f4ea21 | -5.09346 | -49.0627 | 2025-10-04 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad4fdd9c-5d37-3296-aee4-fb763339ec28 | -7.72495 | -42.5589 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0467156c-b034-35a4-931c-15c67eb5a60c | -5.27493 | -42.65335 | 2025-10-04 04:12:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6449b24f-6217-3fbd-bd23-1adfc66c2bee | -6.34649 | -43.43877 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f25ad474-abc8-3ca1-a182-b2a71fc19215 | -7.5576 | -42.629 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8739c5ca-ebc2-3270-a45c-bea71f247900 | -6.61209 | -44.30655 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a7cda06b-daf5-36f1-9aa8-d849e1e7d3de | -4.42388 | -46.41396 | 2025-10-04 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8b3e61be-e1bf-3189-ba95-2a7a356e7422 | -7.71174 | -42.59981 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3fea42ba-db1e-3cc1-93d0-08b9a621279b | -7.04418 | -44.34589 | 2025-10-04 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8fdb138-b374-3b85-87c1-ea88e62275f8 | -6.17431 | -43.92423 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e38c4e34-6b65-34d7-976d-eadbedb46263 | -6.70972 | -42.79461 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d0fc1134-4d5a-378b-aab1-8fe776f01f65 | -7.75831 | -42.53898 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43d67e13-de1a-36f0-9a6a-aa5f8c89af7c | -6.46309 | -44.57805 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48371be9-c502-34e1-aec8-87ca60092e4a | -7.05493 | -42.78162 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2fc2ae39-4beb-315d-8652-4e3383160a1b | -7.15082 | -44.21031 | 2025-10-04 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 793cb51e-a9f7-3443-8a7f-30bf938de2f3 | -7.54594 | -42.39769 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6f1a6f1c-de91-33b7-89c5-d936ed10232b | -6.36821 | -43.90041 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 40dfd892-180f-31ef-8861-49b06e0ada0e | -7.77067 | -42.61263 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 428b8660-dab7-342e-a4c9-9277114b7797 | -6.23235 | -44.21981 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcd20ecb-2120-32ba-854c-0ce363109b91 | -6.69681 | -41.9448 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4f98ccdd-07e4-3e29-9fa6-0f87815a26d6 | -5.31345 | -43.09721 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94e9fc55-658e-3660-b458-d99a405abf01 | -7.04275 | -42.77257 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 072b323a-105c-386e-960e-ed0d4783cc28 | -5.86868 | -43.55898 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44e3c92d-30e5-3d41-aba0-8ca27d74d653 | -6.5298 | -43.37579 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 62a63135-aa7e-3876-8d8f-a4c4a82aee27 | -6.27383 | -42.45637 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6dab4489-194a-33d2-b849-6ba6beb3078e | -7.6995 | -42.56925 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d5b53483-c896-39e2-8bdf-dcd97ee6332a | -7.53864 | -42.40441 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9c59f487-9d59-3ae9-b359-9404c5147022 | -6.76841 | -43.60626 | 2025-10-04 04:12:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4d551d6-ee07-346f-81be-7dcae3b6d2e4 | -7.72334 | -42.59091 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ac71a12-f76a-3cf7-8c0f-1db0e47921fb | -7.16391 | -44.99373 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98d1787c-86f9-3694-bdaa-96c8567c44f2 | -6.22655 | -44.27769 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 27575c70-8a61-345a-a72b-5780219e857c | -4.99371 | -38.85729 | 2025-10-04 04:12:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 37e69c3a-3eb6-3f02-9e62-a4e27e7ed98e | -7.77747 | -44.162 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e01cdab2-af0c-3091-806b-d70647bab283 | -5.47939 | -45.54591 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52326b52-aa4b-3386-8993-240e12057433 | -7.3278 | -41.44359 | 2025-10-04 04:12:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bcdac003-bfc0-3818-8660-76096aff8324 | -5.77917 | -45.75269 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0c9b7ee-ea74-3abe-b349-22985e6eab0d | -5.95111 | -44.83713 | 2025-10-04 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 451e1888-c155-3ba0-9f0b-728bb62de7d2 | -7.33178 | -41.44042 | 2025-10-04 04:12:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c6f01faa-3660-32c2-96cd-46ce165baaed | -5.46915 | -42.77909 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a3d85b29-f9dd-3787-a1c5-3ec82b7d7236 | -6.67287 | -42.83491 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e74d1b64-8012-337b-a902-68fe8d43912a | -7.79492 | -42.56628 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d79d7128-0eac-3926-9a4c-d64af53dfdf5 | -6.0631 | -42.52229 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e6f20611-c9b1-3143-bb4e-a02dbde1eaee | -6.22305 | -42.93028 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 221b881f-584a-360e-9d27-a227220d817c | -5.9355 | -43.30955 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af780d5c-8496-33ed-a342-70bd764c76c7 | -6.34318 | -43.43825 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45c8da02-3632-3435-9f69-9fc4f92f693b | -5.29157 | -43.29968 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11a64519-c1e7-36e6-8d97-b43ad23e38d7 | -6.27906 | -43.62758 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d10ad4d-6f1a-33fd-ab69-2405b1ec0cb5 | -5.72818 | -44.03805 | 2025-10-04 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aefb178a-fe0a-38fa-82d5-21e026dd2e2a | -6.38302 | -46.50953 | 2025-10-04 04:12:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d86f551-2a83-3d97-8b90-2359664dacf0 | -6.87659 | -47.22861 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26fd17dd-0695-3b5a-b748-b4a73c837e40 | -6.67341 | -42.83147 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 55b28db6-ffb1-3564-bfe8-81bea562db02 | -5.50276 | -42.78083 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cddb2ade-1f83-3e7a-9899-0542c647b8a5 | -5.6898 | -42.69399 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c32aac2b-2f22-3a7e-a088-3c692b25a0e5 | -5.96286 | -44.22179 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d6e0905-164e-369e-9202-43bf04e2de80 | -6.60653 | -44.29834 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de180af1-1f95-336b-82f4-de3c7eed8424 | -5.47132 | -42.7653 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| dba806b8-9343-3212-a218-c61ad9ae159e | -7.16365 | -46.21057 | 2025-10-04 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 458f2de9-7480-3fe1-92a9-f05bce3b864c | -5.46375 | -43.1567 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2cd9871-35bb-3324-a27c-d6d36fb768de | -4.44813 | -43.24106 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af1e5c70-19d9-3e6c-96a1-d36ab3cb4e93 | -6.33544 | -43.8916 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ca6cea1-f84f-3253-8967-1393763796de | -6.39014 | -43.61343 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43d1e7d2-b457-3cfb-8750-0ff8fbe7782a | -6.64691 | -42.806 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e9119109-03de-30aa-89ea-0aa93d3abdc8 | -5.86506 | -44.13298 | 2025-10-04 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 745cff50-acc7-38de-aef2-736031cd5520 | -6.29235 | -43.65102 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd4e69e4-854b-3b80-ae36-0a15ca48daf5 | -7.80152 | -42.54578 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 202871d8-3290-3f6c-927d-12447b0063eb | -6.2481 | -45.34139 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4061005d-c01b-3b65-b5ae-be771ed9842d | -5.48776 | -45.40448 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a8d8390-2e9a-3ffd-9e12-9bccb4f7edc6 | -7.01043 | -42.30747 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a2d8a0a-a8fc-36b4-b8a9-846468ecb760 | -5.96152 | -43.48838 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 662da6fb-3025-318f-a382-38ad2643f687 | -6.26852 | -42.7923 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e0d0857e-ae03-33b3-95d0-af5c1112edd8 | -2.69162 | -48.3933 | 2025-10-04 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53f41749-ef1b-36ca-bd48-df7d338565f0 | -6.12569 | -45.93396 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdc84e3b-3e4b-3962-a596-be5304816890 | -6.24561 | -45.3567 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0eea7a4c-1942-324e-8152-f7c96c6aa4f7 | -6.63256 | -45.00457 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 807ac95e-5478-3a27-9f6b-378003f23cf4 | -7.73135 | -42.60288 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 606e3895-5a24-3908-8284-04d80f234381 | -5.87251 | -42.52458 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 88f19fb6-7b83-3d94-8fb8-1511c35567dd | -6.27045 | -43.10448 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 812eb221-6190-3ec0-a070-a93f31991f18 | -3.68907 | -50.89254 | 2025-10-04 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2c39492-1c39-33c6-9aaf-d3c38b8d4d64 | -7.7106 | -42.58532 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 39ccdff4-65f2-3cf6-b870-e8e35219592a | -6.37415 | -44.30498 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39940bbd-a3cb-39ad-90f8-3658b4d6c955 | -6.69271 | -42.83805 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 588e40c2-b3e5-3033-b4af-3f2d9ae0970f | -6.66673 | -44.20176 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f99e400b-54fd-346b-8877-e4ef6cff6c9c | -7.04166 | -42.7795 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b390f521-bd4c-33ed-bffe-8d726a2c15f4 | -5.34672 | -43.70232 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7410c883-4228-33c5-b7f0-06ab31be3174 | -6.91837 | -46.39973 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 764be300-f0cc-3df5-b4f3-9c8a41b16b73 | -2.68725 | -48.39253 | 2025-10-04 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README53.md)
