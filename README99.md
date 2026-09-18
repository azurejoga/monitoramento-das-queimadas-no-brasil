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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 226d97c4-d11f-386a-8913-c67791995888 | -9.5505 | -45.4752 | 2026-09-18 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| be00d4ca-9615-3c69-86be-46905a9b63f4 | -15.6752 | -52.7339 | 2026-09-18 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| c7377cc7-458e-340e-8f96-9b8d8ff087af | -14.8026 | -48.5622 | 2026-09-18 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 1a7dbf01-801e-3361-a270-d86ed9ed3a32 | -12.5149 | -47.0991 | 2026-09-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| c961fe0a-4cb6-3b36-8524-b079375121fc | -11.8359 | -50.046 | 2026-09-18 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| c0800912-179b-3f83-a0d6-670e2d7d694f | -3.7333 | -54.6499 | 2026-09-18 14:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7d6dbaa6-955a-3145-9037-ff53d2ebdf9d | -12.1527 | -46.9933 | 2026-09-18 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 1ae41a9f-ef5e-3a60-a258-2995caad9924 | -8.3769 | -47.236 | 2026-09-18 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5c17ccb9-58d6-364b-8c4c-440fbec6146a | -6.7452 | -45.4604 | 2026-09-18 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| d7ea31e0-4b52-3571-b5ab-55219baf767b | -10.6758 | -50.2406 | 2026-09-18 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 167.3 |
| a3add199-8dd4-354f-89b6-34af1da5c581 | -9.7177 | -54.8162 | 2026-09-18 14:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 53fa3a3d-5340-35ef-9aaa-c08dc2faf805 | -11.3809 | -44.0788 | 2026-09-18 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 263.8 |
| ca102702-6dc3-339d-9f5f-9c139032d972 | -11.875 | -47.5902 | 2026-09-18 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 13b8d008-1ef3-3972-9dd0-594b1286a669 | -7.8036 | -44.8422 | 2026-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 309.7 |
| b8f81da4-4b81-36e9-9cb2-7438c2a03eba | -6.2949 | -41.7785 | 2026-09-18 14:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 7d4fcb4c-ff6e-389d-a5dd-e0cbcf894f85 | -10.6755 | -50.262 | 2026-09-18 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 42d87ffe-7319-3a49-9494-f45252c25a3c | -12.6235 | -50.8953 | 2026-09-18 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 404b0870-fc13-379b-8dd5-833132b025b4 | -9.8316 | -48.3854 | 2026-09-18 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 1f1ab5e1-3793-3c8a-b417-f2ea6738305e | -10.6944 | -50.26 | 2026-09-18 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 9b5facdc-19d8-3c0e-a9b4-fe2ef0d2ad07 | -11.3167 | -43.3822 | 2026-09-18 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 821d1d9c-b4da-39e0-b448-f6016be35ded | -12.5341 | -47.0964 | 2026-09-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 4ab46581-baa1-3f6a-9ecf-53c317a1af38 | -11.2979 | -43.3614 | 2026-09-18 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 402.0 |
| 01670ab9-06dc-3137-9bde-33104f6d6d1b | -11.8115 | -46.8158 | 2026-09-18 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| ebba239b-3ce7-3b2a-85bc-c0620e10e19d | -11.2783 | -43.388 | 2026-09-18 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 260.1 |
| 1f6968e6-e317-3ce1-b7b4-7ed03921b023 | -6.3287 | -55.2677 | 2026-09-18 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 4e2d0947-aa9e-3333-ab45-cb3afa818e91 | -12.5345 | -47.0738 | 2026-09-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| f48fdc85-26ff-3ad3-9df1-72d647be3d8f | -7.8219 | -44.8861 | 2026-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e47ce68f-32c0-3e98-b280-abecbacc2535 | -11.8934 | -47.6322 | 2026-09-18 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| d87eadd4-b808-37cd-952a-74b41ab98f99 | -7.1781 | -43.6105 | 2026-09-18 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 149eacdc-4a62-3647-9ad9-fce072c2fd94 | -8.5422 | -44.5593 | 2026-09-18 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 23096a62-159e-38a0-b154-d4cfbe3d6373 | -12.3954 | -48.4727 | 2026-09-18 14:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| c5156f9e-503b-34f3-a267-697392e04cc8 | -10.5966 | -46.5474 | 2026-09-18 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 0154ecf7-a28a-3c55-b155-88d76725221d | -14.1542 | -45.1675 | 2026-09-18 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 35a4bfd7-4459-39d2-bcf0-44221398abff | -9.9505 | -45.336 | 2026-09-18 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 65525085-11c9-38cb-9afd-2147ae0ec55f | -12.0461 | -49.9992 | 2026-09-18 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| f9288087-ca84-3f25-b11e-c188ca0dbcd4 | -9.699 | -54.8176 | 2026-09-18 14:00:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 259989c7-5e88-3a79-b958-13c6dc8d11dc | -12.0672 | -47.5198 | 2026-09-18 14:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 5de9962c-90d3-39ba-b4d0-f610326dd185 | -12.5153 | -47.0766 | 2026-09-18 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 099f212b-7696-3be0-be39-11d8fd862fd0 | -19.5539 | -47.6346 | 2026-09-18 14:00:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 009b5f06-05af-3547-b092-41d103691c6d | -9.7308 | -46.1112 | 2026-09-18 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| e9ff9a92-0c42-3efb-b327-45bc8c0c2293 | -12.0464 | -49.9776 | 2026-09-18 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| b25e5126-74e0-32da-9267-b819b92271b5 | -7.6765 | -46.0771 | 2026-09-18 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| a76ba3d5-26c9-388a-8bbf-6f5e5d3909b6 | -11.3437 | -44.0141 | 2026-09-18 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| f28e58dc-1b7c-38ef-87c9-5984e66902f1 | -12.1723 | -46.968 | 2026-09-18 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| a2dc9bbf-471f-3de7-9ec8-b1084b59ec0f | -6.3102 | -55.2686 | 2026-09-18 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 992b7b17-9058-3b02-83bd-59ff89b17392 | -12.5504 | -50.6902 | 2026-09-18 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5029e0c4-34b6-3918-a2df-1b793f1f9620 | -12.5876 | -50.7499 | 2026-09-18 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| e5e7303f-a3b2-3284-b63e-caae39b9a4e3 | -12.1531 | -46.9707 | 2026-09-18 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b903f6e0-8208-3175-bfe8-f87fb77d9ba1 | -11.8166 | -48.8331 | 2026-09-18 14:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 45f208c4-c45c-3a2c-99bb-aa652d3686e9 | -7.8038 | -44.8193 | 2026-09-18 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 4a8263eb-d295-3404-9db7-45d64772b4e2 | -12.0458 | -50.0208 | 2026-09-18 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 99e40e1f-6a03-39ca-9747-88819feb49bb | -10.6189 | -50.2466 | 2026-09-18 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 2a450eb9-91b0-3cb1-ac77-b9e2d15c1df6 | -12.0458 | -50.0208 | 2026-09-18 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d38880ee-27d3-3e52-8ad2-a0892696ed7e | -12.0267 | -50.0231 | 2026-09-18 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 43e79501-baf6-38ad-b53b-bed92b25681a | -10.6729 | -50.4545 | 2026-09-18 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 93ac6004-c672-3d84-8375-357ed61fe785 | -7.8219 | -44.8861 | 2026-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4f42da8c-d583-3dfc-a727-c34d2e3079c8 | -11.3433 | -44.0376 | 2026-09-18 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 9feeae77-dfa8-3a18-b455-9c53bf1b84ec | -12.027 | -50.0015 | 2026-09-18 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| eec5ec59-4949-3c40-88e5-819ebe065a41 | -6.3287 | -55.2677 | 2026-09-18 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| a2ddeb45-5423-3bee-9de4-0bbdff8314d5 | -11.3838 | -47.2982 | 2026-09-18 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 4707e9f1-a92f-3f4f-8400-0418bde4d494 | -13.4303 | -51.9036 | 2026-09-18 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 1a19eb94-b633-3230-83a4-55a8b56547f1 | -10.6755 | -50.262 | 2026-09-18 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 06f163a6-ff1e-376c-979a-f0b31b4bf40c | -14.1732 | -45.1875 | 2026-09-18 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 7f33330c-9451-3b29-affb-28dc424734e2 | -2.4815 | -49.3996 | 2026-09-18 14:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b24a8b94-c538-35dc-81c7-e13d8e3fa2f7 | -7.1781 | -43.6105 | 2026-09-18 14:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 2a7d6b6b-5cf7-386f-9222-709bf3ed92a2 | -11.3273 | -47.2609 | 2026-09-18 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| a2d072ae-28cc-325a-aa6e-bc36b7253557 | -10.3303 | -45.3341 | 2026-09-18 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 9730aaa2-f6c5-3d97-a133-a85163268b30 | -13.6341 | -46.9304 | 2026-09-18 14:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| fc6da1f3-854b-3ec9-a32b-47831911acd0 | -10.6536 | -50.4778 | 2026-09-18 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 87afda6a-57f2-3a5e-8cb3-658bd610eca9 | -11.8934 | -47.6322 | 2026-09-18 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0d2d6adb-2fdb-37c4-92aa-ce82cc423946 | -11.3835 | -47.3206 | 2026-09-18 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 5867e4eb-0751-370d-9362-3973614cca76 | -12.5879 | -50.7285 | 2026-09-18 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 35af3f63-5170-3f02-a3c6-0fee7d4bde48 | -13.249 | -46.8999 | 2026-09-18 14:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| fd4638f3-d6b9-3b90-b1c3-37832b691105 | -6.0196 | -51.7893 | 2026-09-18 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 009573d9-54e9-3ba1-9a68-e3193ebbb490 | -12.5153 | -47.0766 | 2026-09-18 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 145711da-4f8b-3878-820a-920db19830a2 | -7.0352 | -44.6396 | 2026-09-18 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| a0fb356a-5897-339f-942c-32ecb98928d9 | -12.5688 | -50.7308 | 2026-09-18 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 3e1a2ef0-62cd-32d9-ba7c-5b007fd5f13c | -9.8316 | -48.3854 | 2026-09-18 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 6e928440-d361-30f5-9b8d-b882df4dee48 | -6.3102 | -55.2686 | 2026-09-18 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d63727a1-090f-35e7-b6be-1bf65574cb87 | -11.2783 | -43.388 | 2026-09-18 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 8a4a54b3-f206-3965-bbdd-e6ab06f15e57 | -7.8038 | -44.8193 | 2026-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 8003e33a-8788-30c6-840f-c113120774f8 | -11.3442 | -43.9906 | 2026-09-18 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 136.9 |
| aeedc828-ff4c-352c-ba21-d5d6a67b3d1e | -11.8556 | -50.0006 | 2026-09-18 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 208.5 |
| 25a6d6b8-3803-3c7f-801b-6d164eec60de | -11.3437 | -44.0141 | 2026-09-18 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 7133360f-4d84-3325-8e25-172171ea7c63 | -10.3307 | -45.3112 | 2026-09-18 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 166.1 |
| b3198d57-f1ac-3b1b-b703-6fc0cc3c417c | -11.064 | -48.2898 | 2026-09-18 14:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 3fb16053-3fae-31a0-ace3-3c8eb0a4af78 | -8.7078 | -44.8857 | 2026-09-18 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 96a300ce-e89e-3b1c-8250-4077206e9e78 | -14.8026 | -48.5622 | 2026-09-18 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 64836f1a-5e5d-34ff-b7dc-f823ea62e24d | -11.2975 | -43.3851 | 2026-09-18 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 316.2 |
| 4ce0a614-8d45-35b1-a5d7-b9e474dd04d0 | -3.7333 | -54.6499 | 2026-09-18 14:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 3d10363b-edfb-310b-aef9-b837becb3a2b | -12.0464 | -49.9776 | 2026-09-18 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d02db690-f0e8-3670-8fe1-aae520cfad4f | -9.8505 | -48.3834 | 2026-09-18 14:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 54fe589f-accd-30d1-82f3-c867ba8ed6ab | -8.4503 | -45.8448 | 2026-09-18 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 09a8cecb-c9f8-3a4e-88e4-4417270a26b3 | -11.8115 | -46.8158 | 2026-09-18 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 174.4 |
| d871ff72-633d-3f3b-8811-711f661515a0 | -10.6758 | -50.2406 | 2026-09-18 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| fb2d7479-ebc2-3ebc-8397-ebe9dad67d98 | -2.6783 | -57.6087 | 2026-09-18 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 6089fe55-b5fc-3afe-9a04-5f1e543e634e | -7.1675 | -44.5589 | 2026-09-18 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a558a3b6-86ee-3d17-8971-9c8f139295cf | -9.9505 | -45.336 | 2026-09-18 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 75790207-8ae9-3244-a020-e7bf6a24c556 | -14.1547 | -45.1442 | 2026-09-18 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 149.3 |
| b7edc97b-df7a-3fca-bef8-f60e40081914 | -7.8036 | -44.8422 | 2026-09-18 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 180.7 |


[Clique aqui para ver as próximas entradas](README100.md)
