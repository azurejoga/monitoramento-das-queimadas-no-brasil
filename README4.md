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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2835b85-25fd-3213-8d41-09a533e020ad | -12.08047 | -48.20365 | 2026-05-22 04:06:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cd8f33a-53c5-3567-94f8-98f6a2da624e | -12.23346 | -44.25182 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7c37a32-c4fb-3584-b40d-546906882f3f | -12.23345 | -44.26325 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de24eb9e-b696-329d-af65-43592f836e68 | -10.79849 | -49.40656 | 2026-05-22 04:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b271315f-28cd-346c-8c13-1242d25004f0 | -16.35614 | -43.87686 | 2026-05-22 04:06:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf403747-f8c4-3bf6-8555-1c1b175dac1f | -12.23774 | -44.2597 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0062aff1-bd07-387a-b1af-e7cd3d7596d2 | -12.07591 | -48.20278 | 2026-05-22 04:06:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec4e5685-2042-35d0-a54c-9c66ace38bfc | -13.23861 | -43.39295 | 2026-05-22 04:06:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2d4a545-36a0-3468-ba84-2e8636ae2d24 | -11.14854 | -48.11068 | 2026-05-22 04:06:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c8cee2d-494f-3369-9a29-7aa44c5c56ee | -11.95353 | -43.39064 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 313d8f6a-95de-3143-b225-650ebd47df41 | -12.59511 | -44.51337 | 2026-05-22 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23ca7097-c490-3651-a622-4af24196ae92 | -12.23206 | -44.2602 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5370495-0798-33ec-bddb-afbfbb18f016 | -11.95417 | -43.38679 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0947f683-b93f-3585-9ef2-307237a2e9e1 | -14.75416 | -41.70653 | 2026-05-22 04:06:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 27a1ded9-e0ae-3415-ab8e-f43a7ee4afc6 | -12.59583 | -44.50912 | 2026-05-22 04:06:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 750e8522-0524-3140-a706-6e37a85995e7 | -14.22654 | -43.65694 | 2026-05-22 04:06:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05728a00-0fc7-3465-89c5-a82201525e90 | -12.18173 | -47.86041 | 2026-05-22 04:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95af0a57-ed81-33b2-84e9-b737e878a353 | -12.23495 | -44.265 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35ef95d3-767c-33f8-8605-4fc9f5a25835 | -14.48623 | -42.21667 | 2026-05-22 04:06:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 72fa107d-a181-383f-8225-c598c7411c8d | -12.08105 | -48.20174 | 2026-05-22 04:06:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99c7b06a-8b60-31df-9717-918b5faa490e | -12.27058 | -43.51132 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fef0efaf-ceb2-323d-9177-cc83dc6efb42 | -12.27339 | -43.5158 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05ee18f3-9aca-3210-bbd5-def362d0385f | -12.26234 | -43.51788 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84c8aaee-5832-3f01-a680-3db2dfa15a75 | -12.81163 | -44.87128 | 2026-05-22 04:06:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 958704b4-af41-323a-98fe-f44cf360535a | -12.27404 | -43.51192 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a4b951f-f2b6-3309-8f95-8381ec2fc843 | -12.26581 | -43.51847 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49181d6f-33f7-3526-8a48-7f44c0401fa3 | -13.95135 | -42.687 | 2026-05-22 04:06:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 33a65ee0-36be-3e74-be3b-a74653831370 | -11.18451 | -48.0181 | 2026-05-22 04:06:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55ad9435-906c-3c9f-a17f-e070e65c7986 | -15.54215 | -39.91761 | 2026-05-22 04:06:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1feaa8e0-36e5-3a49-819d-dcfd142fa5ba | -11.61136 | -47.90612 | 2026-05-22 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b3af5184-b2f3-322d-86a5-7c23db27f9d0 | -12.08017 | -48.20641 | 2026-05-22 04:06:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eaec2025-c924-3f7f-bc0c-098240eda430 | -11.70158 | -44.15802 | 2026-05-22 04:06:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1096e22-ca83-371b-83be-16cce02bb5f9 | -12.23273 | -44.26744 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bccbb615-2df3-3c8d-b836-b941ba101999 | -12.23203 | -44.25009 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6c1a671-3cea-3324-8ec5-1bbd0abeee44 | -11.61222 | -47.90148 | 2026-05-22 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf549406-3436-3c7d-afaa-b38d4d77bffe | -12.88228 | -47.24009 | 2026-05-22 04:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84f07266-08d0-35e5-9431-b783adacf629 | -12.27274 | -43.51969 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 075aba2d-53c3-3a81-af86-77851e7fa604 | -12.23417 | -44.25908 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74961dcb-a58a-3d95-b65d-fe64c63bc109 | -12.23564 | -44.26081 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcb7af7b-8c3b-3d10-b0fb-e58b5bcaf2dc | -12.23703 | -44.26386 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9d4bf14b-0445-375c-a6e7-c8def13b7846 | -11.61673 | -47.90228 | 2026-05-22 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09d07ad2-082c-3bdd-a3c7-ee03cc67bc72 | -12.26993 | -43.5152 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fa34a4a-4c80-354b-bd5a-4a115d95accf | -12.0765 | -48.20087 | 2026-05-22 04:06:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9930df10-6e8e-3885-ba83-c1d944e4606f | -12.26646 | -43.5146 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79e5d5ce-5723-35e0-8ded-f7b0df0ba8b0 | -11.99839 | -45.1449 | 2026-05-22 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcf81bd5-2f04-320b-8e0b-0fbc12d549e4 | -12.26365 | -43.51011 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9df4d709-90f7-3cfb-bbfc-b8b47117f0ea | -12.263 | -43.51399 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f89764a-4822-3ab2-806d-6603f94585df | -12.23631 | -44.26805 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b89415c-fe32-3ede-9109-3dd8f25c71a4 | -12.23131 | -44.25428 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b469d87-9363-3ed6-9f37-7d96297c97ed | -12.26711 | -43.51071 | 2026-05-22 04:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dfb0e4ca-af74-3289-9910-70b604afd9b3 | -18.62275 | -45.13297 | 2026-05-22 04:08:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccd5a232-8823-3b1f-828b-3f16e42c674c | -19.17508 | -47.35736 | 2026-05-22 04:08:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec1a98a1-225a-350c-9a6a-e748a4fdc9e0 | -19.76139 | -54.06806 | 2026-05-22 04:08:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f955cdf6-696b-3284-b96a-6716141a94c6 | -19.76706 | -54.06968 | 2026-05-22 04:08:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6b871838-a7bd-3043-8279-305708997444 | -19.76234 | -54.06379 | 2026-05-22 04:08:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 31524ff5-e4b5-3cfa-a771-b586301f763f | -18.62691 | -45.1296 | 2026-05-22 04:08:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a29201ec-2352-3a9b-a572-2299581dd1fe | -21.18198 | -45.87194 | 2026-05-22 04:08:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8124455-5b9d-3232-ae27-fde412ea6136 | -21.18127 | -45.87609 | 2026-05-22 04:08:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a24ef46b-36a3-3d92-890c-3a791e3d52bd | -19.76801 | -54.0654 | 2026-05-22 04:08:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 717bbded-669a-3c6d-a52e-fea2890b559e | -19.7804 | -54.0533 | 2026-05-22 04:10:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 58.4 |
| ac9bc2df-a309-32b1-9c9f-dcb2a70b7b65 | -19.7799 | -54.0749 | 2026-05-22 04:10:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 91935caa-b8cd-3233-af9d-168ead57ba3c | -27.68686 | -48.74794 | 2026-05-22 04:10:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5c692e1e-7869-38df-85cb-55cee0f38b8a | -27.44821 | -48.44767 | 2026-05-22 04:10:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c2341f67-9f92-376f-a63e-614e157c5d2e | -29.19204 | -49.85254 | 2026-05-22 04:10:00 | NOAA-20 | SÃO JOÃO DO SUL | SANTA CATARINA | Brasil | 4216404 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b1e87cd9-4abb-3399-870d-2b4065c5b07d | -27.57631 | -48.42725 | 2026-05-22 04:10:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0cd603d0-d313-3a9a-972b-29aa9a8006ed | -29.07696 | -50.735 | 2026-05-22 04:10:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 513f8a4b-6bef-30e8-bb3a-a68ebe46ae6c | -28.01382 | -49.01586 | 2026-05-22 04:10:00 | NOAA-20 | SÃO BONIFÁCIO | SANTA CATARINA | Brasil | 4215901 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 385465ec-da9a-35b4-a57f-4cdb503e8fff | -27.68716 | -48.72491 | 2026-05-22 04:10:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 18959f32-d498-30ad-8b2e-5e5ffa356d71 | -29.07422 | -50.72824 | 2026-05-22 04:10:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 08b0dffd-e766-3140-83f8-cffaced38e2d | -27.68761 | -48.72311 | 2026-05-22 04:10:00 | NOAA-20 | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0064a756-6886-3ee8-a775-4f442d3b4497 | -8.92098 | -46.91723 | 2026-05-22 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eebeb340-f651-363d-8cf5-69593ee7f6dc | -7.61892 | -56.74116 | 2026-05-22 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0f96d2d-0b1e-33dc-9a3d-366326d6f9fa | -9.40401 | -47.36593 | 2026-05-22 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 997e2e51-627d-3ee0-b5c0-006ae8b3456e | -8.71253 | -54.99784 | 2026-05-22 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48a6cec6-417e-321e-b574-e718cb1cd5ef | -9.92773 | -48.00558 | 2026-05-22 04:51:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7679e391-9863-378e-a4af-0611a7061d47 | -9.30446 | -45.49219 | 2026-05-22 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3ac64b84-02e1-36f6-af0b-f877c789e491 | -8.92791 | -46.91908 | 2026-05-22 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f05d73c-5df9-39b3-bb54-25e5d696125c | -9.39952 | -47.3675 | 2026-05-22 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62a23595-7e8e-3a8b-9b34-a77ab2d0fc76 | -9.29073 | -45.48499 | 2026-05-22 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7f0fff14-7bd4-38bc-800f-913c02db0374 | -9.07865 | -49.67603 | 2026-05-22 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d21f1133-bab3-3a2e-9cd2-387a62f11a9e | -8.55022 | -45.97804 | 2026-05-22 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67b50c69-f652-3c93-8ec5-174452079d60 | -7.63917 | -45.30626 | 2026-05-22 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a8103ade-bcc3-33c4-b139-732b49f65c34 | -5.95645 | -43.4906 | 2026-05-22 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f682c06e-8cb6-3a30-b750-cbf12f16c4ce | -8.60023 | -45.95566 | 2026-05-22 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29eec2c6-306f-38f3-9fae-e8030d02e3a4 | -5.95645 | -43.49109 | 2026-05-22 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e50ed7c7-8dcb-3445-a4eb-912e0ea7febf | -9.22876 | -48.5809 | 2026-05-22 04:51:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9da9aeeb-a518-3397-9981-9e0a14109cb9 | -9.075 | -49.67547 | 2026-05-22 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00eb8451-4d20-3708-84c2-1c8dfad498ba | -6.56405 | -47.90565 | 2026-05-22 04:51:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3e6aad84-3d07-33c1-ad54-551b64e2fb15 | -9.81668 | -47.9978 | 2026-05-22 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13c03cb5-e644-34a3-ba24-d4562e5c58cd | -9.29483 | -45.49094 | 2026-05-22 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aa3c8d28-34ee-3d0f-8f83-b3e322a2642c | -9.29892 | -45.49689 | 2026-05-22 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9ab0b3fe-6bcf-3867-8234-8af07d907dbb | -8.11894 | -44.17447 | 2026-05-22 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9be1f2c-0107-3614-8562-3fef7e5d5a56 | -9.29001 | -45.4903 | 2026-05-22 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 033da1b2-8ff1-3c58-9a8f-21c222f2581e | -8.68417 | -48.83471 | 2026-05-22 04:51:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d82ff341-cea9-3bae-912a-d4dc64ae94b9 | -7.0514 | -45.06266 | 2026-05-22 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f307c75-ff29-3906-a351-5d6603019451 | -5.77038 | -45.12642 | 2026-05-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10d4796b-328f-3431-a6cf-1e28e02713b5 | -6.56797 | -47.90625 | 2026-05-22 04:51:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9bf1907e-3057-37ca-a4b1-c940d221f3e9 | -5.92627 | -43.47704 | 2026-05-22 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d5e3c764-970a-31f3-8919-6d600776ccca | -8.1196 | -44.18354 | 2026-05-22 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 675fa4b4-a340-3bb0-90fe-2f78c56bd85b | -8.92967 | -46.91839 | 2026-05-22 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README5.md)
