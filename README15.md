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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c8ad585-1584-3557-a14d-860a3951ef7c | -8.51336 | -46.5313 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9609182-3472-37aa-832b-048704ba19f4 | -6.99718 | -44.83208 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ac847e8-a61c-37de-8bd3-5cd398f20c10 | -11.49826 | -54.62411 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7568655-005f-348d-a226-ff843bc71485 | -8.48846 | -44.73652 | 2026-08-15 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dbaaf5f-e624-3d22-a168-96d8c7dd6433 | -9.10967 | -46.39951 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d57f079d-552c-374c-9fb6-2eb74e35a3b2 | -8.51417 | -46.5265 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a57e1fa4-7601-3cb5-9b35-741af127f6b5 | -9.11034 | -46.39687 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43ad8fb8-3b2f-30e7-826c-0ec2d5d41f70 | -12.69263 | -48.4549 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 96fde828-a7fb-3bf2-805c-7eb9a7616da3 | -12.70396 | -48.43856 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fe4fc82-7740-31c0-b61d-0d7ebbab7615 | -9.57326 | -45.36917 | 2026-08-15 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86bac5ea-07e4-3ea6-b698-0fac8f930b72 | -11.58372 | -54.66998 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fa9db48-4e7f-3020-a1e0-79c4933a0cb3 | -12.69595 | -48.45979 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb2624a4-cbfd-3a8e-a038-ac183925a645 | -11.40881 | -46.34346 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8cb2bbf0-0bf5-3e29-994e-3e9c9c49962f | -7.45179 | -55.30786 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| edf51687-411f-34f3-8e04-35d84f1295be | -7.72744 | -46.24532 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0b6c7083-2918-3c39-a9a6-baa3b4d42bec | -11.49781 | -54.6337 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c5bfcb0-f40c-3f4b-9afc-161ca7e9883c | -7.62302 | -44.15123 | 2026-08-15 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33cc9efa-0ee3-348a-925d-5453e429eabb | -8.48781 | -44.74046 | 2026-08-15 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ad781bbc-fdc6-3f01-ae58-33bb1e8e1b52 | -11.72476 | -47.00697 | 2026-08-15 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b2a7835-740d-3de7-8736-7b1452b6da62 | -8.0331 | -55.1371 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a303f30-f94f-3530-aec8-c58e5a3bc2fe | -9.47567 | -51.61902 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 220e7a5c-53bc-33fe-979f-b6bbd904a18b | -6.87679 | -41.95567 | 2026-08-15 04:14:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eb70fc9d-4902-3387-be7a-b93b0c625e98 | -9.97993 | -53.944 | 2026-08-15 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3f528303-9c36-3d2f-be2c-8db6769e0eb8 | -8.62288 | -45.8535 | 2026-08-15 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47023e3f-4676-3a27-8237-000e58e75a80 | -8.79779 | -47.92697 | 2026-08-15 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe218e14-f7a3-37e5-ada3-9e4de15b82ff | -10.65387 | -49.20601 | 2026-08-15 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 670c1eb9-dd4f-3222-85a3-e2c5d6421407 | -11.40959 | -46.339 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b454e567-98dd-3b00-98da-dd3537248bc8 | -8.21874 | -45.78353 | 2026-08-15 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bf59797-fc62-3a36-9e87-df4c1f72b309 | -9.58393 | -45.37106 | 2026-08-15 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ea6c4dc-63ca-3162-b93f-b67853f60b80 | -11.58992 | -54.67115 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 268f620e-3375-3197-a66a-c0eadd19c8e2 | -11.58479 | -54.67372 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f10662e-a6e7-35b3-bafc-46b325c1b93f | -12.02174 | -46.42543 | 2026-08-15 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 902e0aab-abfb-3ff7-b632-6c62cea7e4e3 | -6.31556 | -47.33751 | 2026-08-15 04:14:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86a19b9b-df4f-32eb-80fb-78a634acdba5 | -6.99262 | -45.90095 | 2026-08-15 04:14:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ab11169-430c-358a-8239-2af4fd0b9a0e | -9.11643 | -46.4055 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2fab0e32-cbbd-38fe-aa8f-aec784827761 | -9.12021 | -46.40618 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3598ebe-1a2d-3bae-9efb-54f7e8ac7278 | -11.43229 | -43.91785 | 2026-08-15 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09ff0e5d-dfc2-30fb-ba99-71e147565760 | -11.40747 | -46.32948 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a04015d0-6d87-3745-a444-86276d28e593 | -11.40668 | -46.33403 | 2026-08-15 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 377ebc3d-659f-3279-812a-b2078e47924b | -6.92992 | -43.64239 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 64f9d6b0-75eb-3482-9289-5434b72f70e9 | -13.69441 | -46.27027 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 309d959c-d8dc-35a6-9a8f-a444c542a357 | -11.5024 | -54.63536 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9f4734b-f94b-3295-934a-bb10bb22dc86 | -8.52267 | -46.523 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 281cc36a-8068-3bcf-93d5-5e6ee0f31d61 | -9.10957 | -46.4015 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a2763477-7eca-3283-b462-1cd38fbeeab5 | -13.47553 | -44.04054 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8e5ba62a-039b-3ea4-b04e-9c67963212b9 | -9.22602 | -40.56366 | 2026-08-15 04:14:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 55a16a59-9c74-33da-a6c9-73fc50d225a4 | -10.52507 | -44.85351 | 2026-08-15 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e3e7bc1-23bf-3f23-a87c-57c2a3429f27 | -12.70867 | -48.43568 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e60b614-8a32-38af-9d30-ed15ac75db75 | -10.60984 | -46.57406 | 2026-08-15 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22bbc813-8744-3725-89f4-7fdfae87caf5 | -9.57188 | -45.37748 | 2026-08-15 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80109fb7-639d-3513-89c3-7213056390a2 | -12.69806 | -48.44806 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d47b4b14-c670-3d16-acce-fbb9150c3e1a | -12.72216 | -48.43055 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 798c9e53-c0b7-3ad5-a9c7-adc523d7432b | -11.5044 | -54.62555 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb640aa9-8198-33ea-a444-414b881e9aee | -8.45509 | -45.11853 | 2026-08-15 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 944c60c5-a4c0-3a5e-8149-c7528f9c0ab0 | -6.24813 | -47.71339 | 2026-08-15 04:14:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0a551e8a-b814-356f-ad8f-ca66dc9568ad | -10.41788 | -47.981 | 2026-08-15 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d9eb5b5a-205f-31ed-88b5-c04b8878efb0 | -10.41852 | -47.97732 | 2026-08-15 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6ab56689-a84c-3a0b-b121-74bf53401f18 | -6.91348 | -43.63593 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea8827ae-e89e-377e-9634-00795f231ce7 | -11.49975 | -54.62384 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d51d08e5-b487-3cb3-818e-b96ac63e6202 | -9.11141 | -49.2609 | 2026-08-15 04:14:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c3215eb-6ad3-3656-8fec-7880777e5963 | -10.49342 | -50.15567 | 2026-08-15 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dd50524-6e51-3523-a32b-59df5ccf7a85 | -6.86519 | -43.86879 | 2026-08-15 04:14:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a9f1c3d-f646-3471-89c9-baa5fa853d6e | -7.80872 | -44.10735 | 2026-08-15 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9983e4bb-2ebf-32f5-9fe1-a2bbbd6e91fc | -11.49926 | -54.61925 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 162db8d8-75b8-3c9b-9d21-61de922022d3 | -7.28048 | -44.67716 | 2026-08-15 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3840fb9d-726b-3e24-8bb2-1178ee09c42b | -12.7028 | -48.44501 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 315ecef2-beb1-38a3-b22f-f5fe60522a3a | -8.36331 | -46.37939 | 2026-08-15 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bca0084-c104-30d8-8d50-756ca46e2a26 | -6.7847 | -55.85431 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d899d1fb-6f14-3904-be26-3d56daf445d2 | -9.11514 | -49.26637 | 2026-08-15 04:14:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04b249d7-8523-3b5c-a14f-d6ca72190edc | -6.79463 | -55.84121 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd662b13-3487-3279-9565-cf922f87d991 | -6.78232 | -55.85247 | 2026-08-15 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e78f769e-46ce-3e10-ae58-42750a406cdc | -13.43113 | -48.34714 | 2026-08-15 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db504995-1a2c-3772-ae49-0b2dbbb5c331 | -12.05202 | -41.05838 | 2026-08-15 04:14:00 | NOAA-20 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9db22e60-1794-3a4f-beba-f87f1693899b | -7.01402 | -41.43127 | 2026-08-15 04:14:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| df8f88b5-8733-379e-bb22-b45ffef8ad2d | -11.50072 | -54.61897 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c53f0591-0671-3f59-9d7f-c50f8dd73996 | -9.11047 | -46.39488 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 734896f5-d6da-34ac-ab3d-f26563a65891 | -13.541 | -46.25363 | 2026-08-15 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 744fedf1-f95b-34b5-8828-12e10067fa80 | -13.47942 | -44.03753 | 2026-08-15 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cdb24042-35cc-31c0-aaee-633ef3449160 | -12.30432 | -49.34279 | 2026-08-15 04:14:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e24d9167-6f19-3355-825c-91557671d7e5 | -12.70339 | -48.44176 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc2c5fcb-5689-3919-b572-479e78159dcc | -9.11723 | -46.40084 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f0a6047b-056c-31fa-9859-ea8bf29fe85a | -12.01224 | -46.41501 | 2026-08-15 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 98dbccd9-f426-3298-b6be-5c9e45530622 | -6.91408 | -43.63222 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7b6c2d4-ce40-36be-82c0-bdb37181e93a | -8.71507 | -49.60741 | 2026-08-15 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5dc60a6-4e77-3953-a4d2-519ba2a5dcca | -7.01955 | -41.43923 | 2026-08-15 04:14:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c54b1ebd-faf0-3b38-a904-5fbf30e5e24c | -10.72191 | -50.55133 | 2026-08-15 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a39461cb-9021-3f93-be97-d9a15c0d8cf2 | -12.73444 | -48.4321 | 2026-08-15 04:14:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59e0aec5-a082-3135-a11d-0698080c3d77 | -9.13317 | -46.39878 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7f61f17-770d-352d-966a-675ce7f0c47c | -11.50137 | -54.64038 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a10d9811-8e0e-32c3-8cae-d711e20ce1cd | -6.54306 | -55.18156 | 2026-08-15 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74787331-b411-3fbc-a0a6-16118ebcf1d6 | -9.12102 | -46.40146 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f7564f27-1db2-392a-a6ca-f4f322c3dbdd | -11.48381 | -44.56968 | 2026-08-15 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efbaff58-c973-3e3d-8d74-8934b46a2c22 | -6.92149 | -43.62961 | 2026-08-15 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b281a118-e2bd-3cd6-b4ba-177499f2dc69 | -11.58079 | -54.69388 | 2026-08-15 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1995fb6-4912-3c94-a72f-f866ddc0fa4a | -12.45842 | -46.52672 | 2026-08-15 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 091ace31-b64d-3018-8fbb-5b84df513878 | -12.31219 | -49.98598 | 2026-08-15 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59f1a7cf-34da-3552-a810-43b91591a37e | -10.61104 | -46.57242 | 2026-08-15 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 73ed88a1-6802-3980-939e-4f626b7b1204 | -12.14425 | -47.16465 | 2026-08-15 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11bcf465-df0e-3378-8791-05a387c7491b | -9.11265 | -46.40485 | 2026-08-15 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 112d1120-c659-3894-a73b-9129770045f6 | -8.76308 | -47.4506 | 2026-08-15 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README16.md)
