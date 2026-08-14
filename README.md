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
| e8197e04-a82b-30ce-b965-ed39df1aa8ea | -7.7123 | -46.2307 | 2026-08-14 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7d013eb8-0b20-3214-9e49-9bf7067c93d9 | -21.9054 | -55.3538 | 2026-08-14 00:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 61eebf58-7534-30e2-863a-4976360a91ef | -4.4868 | -42.5572 | 2026-08-14 00:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 194.8 |
| 025798e4-9ea1-3b34-977c-cd4509da841a | -6.7123 | -58.9412 | 2026-08-14 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1788e9ac-79f8-30dd-81f0-207abcff94e2 | -4.5244 | -42.5313 | 2026-08-14 00:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 169.1 |
| 8517abd1-c328-39d0-8935-f61f7bcfb17e | -4.5242 | -42.5549 | 2026-08-14 00:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 193.9 |
| b041de4f-7be9-36be-a13c-791e9a0f8121 | -6.6194 | -59.0609 | 2026-08-14 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 0c3d7346-962d-3fde-8e5b-b6fcef56ffeb | -4.5057 | -42.5325 | 2026-08-14 00:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 627.3 |
| 33f8d642-3568-3385-86f6-83832c8a8135 | -15.1362 | -41.561 | 2026-08-14 00:00:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| 728e8359-92f0-3f8e-a54c-0eeb61e065d7 | -11.5076 | -54.6051 | 2026-08-14 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 148.4 |
| ab432061-40fc-3491-9460-3e84c6f425e3 | -6.9145 | -43.6351 | 2026-08-14 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 7e8ec8fc-4781-3677-9b73-989539ebe629 | -9.1219 | -46.404 | 2026-08-14 00:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| b04fb64e-3881-3c76-a7f0-012455d36f84 | -11.4887 | -54.6068 | 2026-08-14 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 1d66b203-a2e1-318d-ac76-71607adbe14e | -11.5074 | -54.6256 | 2026-08-14 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 0f7d76ed-ad77-3d4f-87af-3a326919aef3 | -4.4869 | -42.5336 | 2026-08-14 00:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 186.5 |
| e7732816-7794-3294-9381-67131dffb49d | -9.9894 | -53.9608 | 2026-08-14 00:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| feb55eaf-a903-3a2c-bb12-a0e42ad24c4c | -14.4734 | -45.6914 | 2026-08-14 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 0f09be3a-8612-37a7-ba19-8daec0514c7b | -21.8848 | -55.3574 | 2026-08-14 00:00:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 0635e9f2-60c6-3a86-8420-98bf68269855 | -6.6195 | -59.0416 | 2026-08-14 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 163.5 |
| f8234adc-b56f-354e-805d-aadf8aa30bd9 | -14.4739 | -45.6682 | 2026-08-14 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 84ccf7ad-68ce-352b-8311-c33e9e757c86 | -21.9049 | -55.3755 | 2026-08-14 00:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 271.9 |
| 8afcf5ec-22a3-330a-a3cd-ce0e30c95f76 | -11.4885 | -54.6273 | 2026-08-14 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 77129ef7-3ca2-3bf4-9956-778f2b315c43 | -7.6158 | -46.4628 | 2026-08-14 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 98bbc83e-8966-3cbd-8fbb-ccdbfe247af2 | -4.5055 | -42.5561 | 2026-08-14 00:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 708.3 |
| 7dcc4bf0-2322-3864-a82b-5011d9109d68 | -21.8843 | -55.379 | 2026-08-14 00:00:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 74.7 |
| ae13d401-530c-302c-809a-9bb753845d07 | -21.8996 | -55.38972 | 2026-08-14 00:07:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a60f740e-965a-3a70-bbc5-0c4717789d52 | -21.45473 | -48.68763 | 2026-08-14 00:07:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| eca29f57-4879-3c8b-a45b-eb1479672e71 | -21.3919 | -48.63574 | 2026-08-14 00:07:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5ebb23d6-e3cf-3d0d-b642-d963068539c9 | -20.96529 | -47.41858 | 2026-08-14 00:07:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 60e5f364-9879-3ebe-9cff-451509197c8c | -23.31481 | -47.54287 | 2026-08-14 00:07:00 | TERRA_M-M | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 24a3f363-ebc7-32e8-a8c7-1a77ba29b804 | -20.96344 | -47.20721 | 2026-08-14 00:07:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 0f36bc00-9953-3ee0-9c90-803b34be9bbb | -21.49395 | -48.64252 | 2026-08-14 00:07:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 309a4eb2-38c0-395a-9515-243920d17976 | -20.96206 | -47.19764 | 2026-08-14 00:07:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 29e6ba81-c33b-3399-b134-7c35cb0e9103 | -21.38304 | -48.63713 | 2026-08-14 00:07:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a06d6b41-374e-3024-a2f3-c5e4acc533b3 | -20.31349 | -42.22612 | 2026-08-14 00:07:00 | TERRA_M-M | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.6 |
| 5431fee5-e979-3027-82db-87187e7a4041 | -21.9108 | -55.36512 | 2026-08-14 00:07:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ead7911f-7d24-3910-95b1-4ddfaf5e6266 | -21.90607 | -55.36039 | 2026-08-14 00:07:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 264.0 |
| b352e0cf-3dfd-36c0-a399-e17ff7a022f8 | -20.31744 | -42.03068 | 2026-08-14 00:07:00 | TERRA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 9037fa9b-f4a4-3a44-8301-e58db4a83b48 | -22.91997 | -49.206 | 2026-08-14 00:07:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 38a824fe-7fa5-3719-81c5-34cf96dbc6cd | -21.22963 | -47.13443 | 2026-08-14 00:07:00 | TERRA_M-M | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 91388150-86f4-33ea-ae29-c89eecbf39ce | -21.94172 | -49.80999 | 2026-08-14 00:07:00 | TERRA_M-M | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| c516a617-7f08-3953-99fe-8d34ebc76cde | -21.45345 | -48.67809 | 2026-08-14 00:07:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 61d6304e-c2a7-35fb-8ee0-0cf8c286b041 | -23.30609 | -48.8513 | 2026-08-14 00:07:00 | TERRA_M-M | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 534b2f33-caa5-334b-9e08-cfdbaa5b2117 | -20.42838 | -41.89766 | 2026-08-14 00:07:00 | TERRA_M-M | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| d3f31b16-31b9-3e75-a373-fe3c6c1523fa | -22.92127 | -49.21608 | 2026-08-14 00:07:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 26.3 |
| dd8e4d85-f7ec-3df5-b656-a0c8c8e06d4c | -21.49267 | -48.63301 | 2026-08-14 00:07:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fd31967c-f57f-3249-b921-7413c124a93a | -20.73964 | -46.99938 | 2026-08-14 00:07:00 | TERRA_M-M | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 66c89c24-5d1d-31f0-9285-6bff4f666d22 | -20.31429 | -42.01233 | 2026-08-14 00:07:00 | TERRA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 08032a46-3ee9-3641-8fcb-be306da39bf3 | -21.90812 | -55.38313 | 2026-08-14 00:07:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 112.7 |
| cbc2cbe6-981b-3718-8f63-b9882d2ca0b3 | -21.89738 | -55.36678 | 2026-08-14 00:07:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 461.1 |
| 9c064f89-96cb-3ce9-b2a5-0e2f3ffe5678 | -20.31661 | -42.24414 | 2026-08-14 00:07:00 | TERRA_M-M | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| 55a031f9-fa31-3645-8c92-b63eab6ba6c2 | -20.32026 | -42.02488 | 2026-08-14 00:07:00 | TERRA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.7 |
| ea68a9a1-a311-32a0-bfce-c8f0003d690e | -22.05548 | -52.18862 | 2026-08-14 00:07:00 | TERRA_M-M | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 875e63dc-63bf-3443-967c-6ee8ede7e83d | -20.31693 | -42.00624 | 2026-08-14 00:07:00 | TERRA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 4c18e59f-e8fb-3404-ba17-abfc9f195c63 | -11.48291 | -54.619 | 2026-08-14 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6b7255c3-a381-3405-8be0-c8e1bc071931 | -14.08507 | -53.67875 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 349ca972-d48c-3f7e-98be-46298feebe02 | -14.46608 | -45.69137 | 2026-08-14 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 3565cb1c-27d7-3be1-8ec3-ecd8ed44fd1d | -20.79344 | -48.97511 | 2026-08-14 00:09:00 | TERRA_M-M | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 6a279dcf-3045-33d9-a870-e4911da380e3 | -10.73629 | -47.92805 | 2026-08-14 00:09:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fe1985dc-8a46-3b31-b674-ac8008ebdcec | -14.33066 | -53.09516 | 2026-08-14 00:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bb745128-b0b2-3101-818d-9af4e48b5f1d | -15.70121 | -48.31856 | 2026-08-14 00:09:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 476d8b3a-84cc-3a9b-8726-cd80987a28ce | -15.51816 | -45.8564 | 2026-08-14 00:09:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9e934280-9e6c-3032-832a-3a624eeecb12 | -20.03411 | -48.00447 | 2026-08-14 00:09:00 | TERRA_M-M | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 25782880-5ad7-30a8-8aa1-712dd19f75b9 | -10.70805 | -50.51999 | 2026-08-14 00:09:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ffd88af8-a9a1-35be-b68c-63cb0dc0ef7e | -13.74283 | -42.56788 | 2026-08-14 00:09:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 7d0feb0f-191d-3ee9-a6c8-44c17aa1e9e0 | -16.88322 | -54.14341 | 2026-08-14 00:09:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d8acd82f-e3e5-34c2-87fc-badb54d19a81 | -18.54918 | -48.18661 | 2026-08-14 00:09:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 76a0d690-442d-3ac2-8cd8-314fcce07578 | -13.92546 | -53.96796 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5408a68a-7e5f-3b3a-b812-3c504a40940d | -16.88202 | -54.13756 | 2026-08-14 00:09:00 | TERRA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 8a47f6e2-a5b7-3858-bf62-14db976880ea | -15.13129 | -48.65801 | 2026-08-14 00:09:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5c1e8a8b-2414-3cbe-ab0e-bcf6e648f0a5 | -15.10952 | -50.44264 | 2026-08-14 00:09:00 | TERRA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 1f51c118-961d-32d6-9481-1b8a9579b317 | -14.72876 | -47.14849 | 2026-08-14 00:09:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 31.0 |
| b5474a1d-5eb9-3140-a6c8-c8976a3d16e6 | -11.48761 | -45.09744 | 2026-08-14 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5a2919af-b7a6-3e1c-a46b-2e7c49d16c7e | -10.52701 | -44.86147 | 2026-08-14 00:09:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7b958a26-2956-32b0-a8c6-38fafaeba365 | -14.32917 | -53.08321 | 2026-08-14 00:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 17b55572-6be5-3d7d-8122-5fc686cb26b6 | -13.25083 | -54.27113 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e544b5a5-9524-3b71-995d-2903dc4bd4d0 | -14.35789 | -53.31471 | 2026-08-14 00:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 62b7df40-6974-3c8b-83dc-6d2666b0c928 | -15.00566 | -41.95082 | 2026-08-14 00:09:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| ae7ea6fb-3fb0-311d-b5ba-b1af48fd6253 | -15.05438 | -52.68108 | 2026-08-14 00:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2a25c1f8-3554-3e27-8a5b-6349bd4f7107 | -11.50454 | -54.61634 | 2026-08-14 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 7e11a2c4-2680-3861-b570-0a8cd3f78835 | -11.48463 | -54.6329 | 2026-08-14 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 7941908a-eea9-3e20-84a1-9f5d94b853a2 | -12.56086 | -48.35089 | 2026-08-14 00:09:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cd2fa3ad-ba1a-3c4f-ab9e-dbe989c8e413 | -11.59362 | -54.68325 | 2026-08-14 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 05018e0d-ae55-3a7e-a04c-7dd8ff908f95 | -14.35946 | -53.3274 | 2026-08-14 00:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 7a7bc706-da5f-31a7-b1d2-1d9b5a1466ba | -11.32446 | -45.22416 | 2026-08-14 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| f069a4d7-efa1-3e7b-be1e-41bf77c85a55 | -18.47599 | -51.75429 | 2026-08-14 00:09:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 51c0d95a-c2d6-30a7-86f6-e4ff1d39ba36 | -13.23534 | -54.26474 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 16ce60c7-6a93-338f-beb7-3e9543d15119 | -15.1402 | -41.55089 | 2026-08-14 00:09:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 81.5 |
| 77944398-519a-3ca9-bcb1-680be2b4a192 | -12.71242 | -48.44052 | 2026-08-14 00:09:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 053f90d7-c587-3f36-b041-064ea734d341 | -13.2367 | -54.24456 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 90663e4a-38a4-327b-aa62-8f9c7492f0f1 | -15.08555 | -48.65551 | 2026-08-14 00:09:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f880f9b0-8bd2-3d9d-9c0f-caf5ec67ccab | -12.49518 | -43.77688 | 2026-08-14 00:09:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 3a4d1a91-8f5b-3ec9-a484-93b354e863b1 | -12.49079 | -43.76363 | 2026-08-14 00:09:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 93892947-f876-35b4-82bd-d197c01d9599 | -18.51575 | -44.17931 | 2026-08-14 00:09:00 | TERRA_M-M | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 01224dc4-98d0-3b26-9814-33c239958eb2 | -12.71379 | -48.45011 | 2026-08-14 00:09:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49030d7d-bb59-3646-bfe2-4b4fbf9053b2 | -20.90101 | -50.51512 | 2026-08-14 00:09:00 | TERRA_M-M | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| a9c3ae1c-179c-3d21-bf25-81cf52a8030d | -14.71162 | -52.88197 | 2026-08-14 00:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9049697f-9a4a-3c77-9097-8861f1b37f7b | -13.24418 | -54.21562 | 2026-08-14 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 8ba15495-60b8-3233-aa61-8b07c9413af0 | -15.15798 | -50.05301 | 2026-08-14 00:09:00 | TERRA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1780d707-5391-3c26-91e7-c314ed32bdd1 | -14.43944 | -45.70168 | 2026-08-14 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |


[Clique aqui para ver as próximas entradas](README2.md)
