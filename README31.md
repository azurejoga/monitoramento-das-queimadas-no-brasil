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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f038656d-d666-3c6a-aaa0-ed781870cfc5 | -5.86327 | -46.11796 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ae2d220-3c5f-3177-89c2-0bf7cfe31301 | -5.55997 | -43.08815 | 2025-09-04 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fd8986ef-7ff7-3c07-81fa-5f0c4baa863f | -6.27338 | -43.32633 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53a9f7b5-f675-3b5c-87b0-68e4e410bf53 | -6.78228 | -44.49623 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f52ab090-69c5-3f66-9cec-e456f00e0e12 | -6.54394 | -43.91502 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 865633ae-e48f-3744-a8f7-39de08512f43 | -6.12439 | -45.9259 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a01390b-b12c-33cb-ad56-37a4b0ff9d4f | -6.28313 | -43.60313 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37dcf426-fe98-3ef6-b6f3-95ce595bf3e1 | -6.49977 | -44.09033 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 980bb500-62b1-3341-9a01-d6fa0a231fe4 | -5.90559 | -45.95501 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a16250e-8eed-3055-9643-8d7e3ea86931 | -6.23717 | -42.71422 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 18e997ea-c83e-3036-9272-31ba46e2bd6f | -6.83732 | -46.39213 | 2025-09-04 04:25:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c82b6638-c1a8-386d-abf2-d0ea933fc0c1 | -6.46959 | -43.97221 | 2025-09-04 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7516910-f66a-36a5-956f-bd83794f76fd | -6.7857 | -44.49678 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91348d20-eb20-347b-b971-0f25b6dfe499 | -4.83369 | -42.73929 | 2025-09-04 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a76a2fa2-ceca-3013-8886-7d0796f86771 | -5.80652 | -45.40976 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac3b5376-ef9c-34a8-9558-2b29ea59cf0b | -6.79081 | -44.48626 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3752779-25a7-33db-84a0-c7bfc7c1353f | -6.1627 | -43.31557 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 52dfe4d8-bcf6-3b51-a9fd-b65c4d40f798 | -5.87264 | -46.12295 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4475a335-398b-3173-b4fe-0b4ab95111e0 | -5.89281 | -43.01449 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f2e35aa2-a270-3bfb-9395-7ef37682284b | -5.80388 | -45.6235 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c719a1d-6fb2-32b5-b718-79aa185ea4f0 | -6.35659 | -43.76405 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 440851ea-5b61-3705-93dd-e799be96a5bd | -5.87359 | -45.63447 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3908e574-4156-3f44-9034-6b5065677b3e | -5.72891 | -47.29685 | 2025-09-04 04:25:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b040771-6675-34f0-b740-a9a702803a31 | -5.88395 | -43.24779 | 2025-09-04 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f51fbf9e-32e4-3c89-ab95-315bc540f348 | -6.82488 | -48.00408 | 2025-09-04 04:25:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25465e66-9800-3490-9ceb-811eeec09f82 | -7.05579 | -50.86063 | 2025-09-04 04:25:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 47ebbc13-4d1d-3c2a-8bd2-d5f0d38aa742 | -6.24851 | -42.63924 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8dad2eeb-6373-3e1b-a5f9-a0e9700529a8 | -7.44318 | -42.03674 | 2025-09-04 04:25:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4e80dc54-815a-3011-b09b-98f482ac3308 | -8.01849 | -44.78294 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a60c351c-604d-34df-bec9-768acb7e1d28 | -7.80146 | -45.43186 | 2025-09-04 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dd99609-9b63-37ee-8e04-034f090d5805 | -6.26785 | -43.58429 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0e02ffa-acb5-3e7b-8775-80b4d74719f8 | -6.20203 | -43.34681 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 460a2f92-ab34-345a-a0b0-6e48fdd2c84a | -6.85802 | -44.27596 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6ac744a-adc3-31b5-98c2-735214df0102 | -5.70894 | -45.16039 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74b63dd1-af23-3149-aa4b-cd79db4f97ea | -5.81029 | -43.85606 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0ad4e1f-4825-3cab-bf4b-3ae189780a91 | -6.39741 | -44.69975 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1eb6fcc1-5109-3a49-89a3-dd7994ce9798 | -7.02511 | -44.35093 | 2025-09-04 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aaeed891-6e40-314c-9f59-07f42acd58a4 | -4.99905 | -56.25155 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| aa49c667-4042-31ac-be3a-c27008d864c1 | -6.40553 | -43.26542 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94b82565-0298-3c7f-823e-8e98d8e32fcb | -5.83545 | -42.9945 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ab5b5016-8b9c-3271-b9be-aeac7811a50d | -6.78393 | -44.46215 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ea8ff7b4-58db-371d-9d9b-5f6a5c6db4b5 | -5.74503 | -45.5432 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c098832-b577-39bc-a539-605d86e61542 | -6.24137 | -42.61085 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c9cd9f8-8ad6-3dba-8e37-a54e2ab108a6 | -6.19256 | -43.99017 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c07d0597-f58e-3b64-9006-f2fd27d437a9 | -6.67818 | -48.39662 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| aff8219f-06ee-3744-a3d1-d17a60c75ff1 | -7.04339 | -42.37652 | 2025-09-04 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 812af2fd-976f-3775-a384-492190b821c5 | -5.90804 | -44.15915 | 2025-09-04 04:25:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b35470e7-ed3b-3b60-8628-165623c8b225 | -5.87413 | -45.63099 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16fccf6b-bbd8-3485-a2e9-e68c2db45dd4 | -6.64321 | -44.09594 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d135077c-b613-3e60-950a-a7861cdcca51 | -5.8571 | -45.65323 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3feffe8f-b502-32d0-b9b9-e6b6e7d3fc20 | -5.96839 | -44.40576 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cddba9c-04b3-3d1f-b0ae-6117334821f4 | -5.50112 | -42.65635 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f6101463-1185-3c18-bf7d-034607becdd3 | -5.00331 | -56.26072 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 190f2404-ac20-36b2-8583-b1e73baf941b | -5.97695 | -44.11961 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 9bb29784-c12f-3ebf-8cd9-2a2fd175b4af | -6.92305 | -45.55411 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 607ef268-c17d-3add-a26e-4b2cd182a88a | -7.05185 | -46.23869 | 2025-09-04 04:25:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 416fbb78-3537-3898-9f42-2ef09dda740f | -5.89168 | -42.99697 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6aab6a80-3301-33dd-9161-115b9d4bf9a7 | -5.80304 | -49.13272 | 2025-09-04 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d865150-5d6e-37de-a68c-419b612e89ed | -7.36923 | -44.32384 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d19ef893-f83f-3ac6-a6d3-5006200e0cea | -3.48503 | -43.33118 | 2025-09-04 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 283a907e-3bf9-3373-a984-86d00a02d5da | -8.02639 | -44.14431 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b1c5466c-7a3f-3a2f-8c30-035d781934c9 | -5.74943 | -45.53674 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8e517237-3c7e-3091-9b2d-6e9684817381 | -7.93799 | -44.94308 | 2025-09-04 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5a269ae3-272d-3f36-b4fb-2690283b0443 | -6.18517 | -43.08166 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 737dffbf-be2d-3242-90d6-2b4dce4b3d62 | -5.60399 | -45.02473 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9c0edcc3-2b0c-3c8b-a38f-6f5ea26f15b0 | -8.03753 | -44.14194 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e81cd9a6-db58-3c24-8397-dd9f345ea567 | -6.25676 | -43.30019 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28e7311f-c937-30e0-86bb-d0e2f6b77dc0 | -7.07536 | -46.19633 | 2025-09-04 04:25:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c54b486a-2da8-398e-9ead-166492c21ad9 | -5.65477 | -51.27147 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f2e74d3-bd7a-38c7-a5b5-1c9b85a7a2c6 | -7.49093 | -47.08455 | 2025-09-04 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c378a84-665b-3b59-acd6-c6368d456a20 | -6.21607 | -43.39944 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59fba146-ca68-3797-8836-6cf64ddaada5 | -6.72572 | -44.15089 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52433cf6-a652-36c7-9db3-abfca50eae5b | -5.90666 | -45.9481 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1755476-48b3-3ba2-8a07-3db15d63e883 | -6.76644 | -45.931 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92dc1952-e739-3882-9331-c443a2262cf5 | -6.69373 | -48.41055 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23b1a344-0ad2-3bd6-a758-2ab0c2b00f91 | -5.68619 | -45.17491 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d6b542e-cbef-303f-b4f9-f0c30997b7d7 | -6.25973 | -43.30486 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f3fae19-f3c2-3be2-9b92-10110c70f501 | -5.67431 | -43.65683 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a24e7dd-6791-3cf6-b8ce-5703324b3b0f | -6.77139 | -44.47547 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73196261-9de8-33dc-84c1-fc60aff62ab8 | -6.25785 | -43.31718 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 436af798-fb84-3717-8d39-1582ef865504 | -6.20819 | -45.05616 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d10e5ac-77ca-3dc5-9846-19a1202288e7 | -6.40677 | -43.25706 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8b5836b-b250-3796-8ed9-736077cac263 | -6.35028 | -43.37601 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89ca7e44-a565-36f6-add7-724756f99ef1 | -6.64669 | -44.09648 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2192f211-d774-3b8b-8516-65f70ab03353 | -6.23691 | -43.40659 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e9c54e6-fba5-348e-8f5c-455b623f3133 | -6.23544 | -43.53395 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d5f6479-d8f5-3d46-90b4-41959bf087da | -7.71426 | -45.00721 | 2025-09-04 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb2265c3-76da-3a3f-a4a9-dd44c3935fba | -5.90505 | -45.95845 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8d4fff9-c8d4-3780-98bb-ca356e682cbe | -8.37127 | -39.38646 | 2025-09-04 04:25:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31d8e40f-9378-3a9f-af7b-a35812bbcbcb | -6.27017 | -43.59295 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 139fb24c-df79-39bc-9d2e-85023db5a2b0 | -6.24271 | -42.6019 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 92d19bbe-be50-3d82-ad2f-f93371fb7a2b | -7.47379 | -45.64322 | 2025-09-04 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44d3b6a7-ffce-3a80-8fef-f45f0abb6919 | -6.78376 | -44.09651 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96e5322d-e6a9-33c1-ad3d-065cf90f01b7 | -6.08101 | -43.28349 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 24e932d3-ff60-3371-9ef5-32f21494ab47 | -5.90922 | -43.22612 | 2025-09-04 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a3d26332-9c6c-3eb1-b294-bac4d48f1aeb | -7.04509 | -43.26696 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 058241ba-ba1c-3fd8-9767-ae8008d84150 | -6.20265 | -43.34268 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cef4931-c358-3252-90cc-5c0f656b8ae0 | -5.74665 | -45.53275 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27334983-49a1-3020-b25d-1bef9a27ba36 | -5.74889 | -45.54023 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b326a6cf-beef-3657-a784-1cc9a3213ddf | -6.45737 | -43.98216 | 2025-09-04 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README32.md)
