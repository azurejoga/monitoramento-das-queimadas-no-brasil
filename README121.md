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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f5bf01f-0dad-39b8-a92c-3aed8c29defa | -7.2908 | -45.3002 | 2025-09-03 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 3e79a080-1175-3b88-8a13-113ef46aec0a | -7.302 | -44.2936 | 2025-09-03 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| afafc920-48cd-3203-a17e-00f64297dbde | -6.3018 | -44.8384 | 2025-09-03 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 82348f7b-7f33-3ec0-9151-d716f95e00ad | -5.7004 | -45.1333 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| ccd6ac5d-b2bf-378b-871c-0db658ee9ce0 | -6.8465 | -52.8337 | 2025-09-03 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d37a0adf-20c6-31cf-bafd-d46740b64261 | -9.1373 | -49.6659 | 2025-09-03 14:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 153b1e70-2e95-38b4-9b4a-991383438f0f | -16.5501 | -55.0782 | 2025-09-03 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| d501e968-2c87-3c84-84a1-84c4014d3146 | -10.9136 | -50.8336 | 2025-09-03 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 6cee1947-909a-3a9c-847b-f5d9b301b530 | -5.7152 | -45.5838 | 2025-09-03 14:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 4cc018d4-d907-338d-8839-71bb1b435942 | -16.2949 | -52.9656 | 2025-09-03 14:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 39f8bd32-c90d-33cd-a459-d110f6f3f57e | -9.6229 | -47.0638 | 2025-09-03 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 140.2 |
| f1243b40-4654-38f0-a7b8-952dd2e10d99 | -5.8884 | -42.9753 | 2025-09-03 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 267.2 |
| c6b8f620-bb27-31c2-94de-608b626aebd1 | -11.9635 | -45.7741 | 2025-09-03 14:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 1d3821a3-5767-3750-a5a0-3db156971add | -7.4969 | -45.3495 | 2025-09-03 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 66b51db2-2afe-3509-9ffb-22c2935bc50d | -14.4146 | -51.7131 | 2025-09-03 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 94e73135-8b94-3cf9-84f7-1ce4c0455817 | -15.1771 | -52.356 | 2025-09-03 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 4f252db1-4392-32c4-b9ed-537d299112b8 | -7.7224 | -48.7572 | 2025-09-03 14:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 152.5 |
| a5815b0a-7668-3838-aa2d-e24e8d683be0 | -7.7226 | -48.7355 | 2025-09-03 14:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 52d0c54c-32d2-32a6-a782-f3b2e347a4da | -5.8882 | -42.9988 | 2025-09-03 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 154.8 |
| 0fe0a798-ae8f-3b58-b1fe-592f6d63f505 | -7.4969 | -45.3495 | 2025-09-03 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 2155d13a-b40a-3004-8609-3119512fd32e | -16.5505 | -55.0573 | 2025-09-03 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 39.6 |
| 6a1f4aa5-7868-3f46-92a9-231ef5417f1a | -8.0197 | -44.1072 | 2025-09-03 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| badf5415-6237-3491-8c76-c264181ff900 | -6.6535 | -45.2644 | 2025-09-03 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 0ba4d476-fe07-3775-8777-f4b5ecc6952e | -7.53 | -47.4662 | 2025-09-03 14:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| bf402698-a358-3b17-ac7f-afd4ef325128 | -6.2036 | -43.3709 | 2025-09-03 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 153.3 |
| d290d901-f488-34c8-a95f-749d2ca794e8 | -6.2038 | -43.3475 | 2025-09-03 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 187.4 |
| e3e24266-15e6-3fc5-a463-614d5716e222 | -11.3901 | -43.5602 | 2025-09-03 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 352.1 |
| 614a5752-94d1-3078-adc3-173a36a3d9c1 | -11.5969 | -52.113 | 2025-09-03 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 6a8028c8-9dc7-3f37-8c2a-34d6769f87a3 | -11.2005 | -55.0195 | 2025-09-03 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| acbfb283-fbc3-3afa-9d61-79338eb88d2e | -5.7004 | -45.1333 | 2025-09-03 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ab9ff4df-8c94-3792-a3f7-95616d859592 | -14.4075 | -53.2803 | 2025-09-03 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| fc0c29a6-693e-3720-96c5-eeecac64e870 | -9.402 | -48.0585 | 2025-09-03 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 7c00d7c5-1ef4-3816-b654-a7e573543d3f | -14.4146 | -51.7131 | 2025-09-03 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 9ccfbae8-47a3-3f62-84fe-be52a5c95a52 | -6.0966 | -46.8281 | 2025-09-03 14:30:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 82c2dd11-b0e1-3e35-99e8-ab08d40455eb | -7.5157 | -45.3478 | 2025-09-03 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| d1def390-81d6-3710-a269-3a5a578306ee | -6.8281 | -52.8143 | 2025-09-03 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 661ef376-5847-3ccf-808f-4202e436f4e2 | -6.8466 | -52.8132 | 2025-09-03 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 562844c0-c61e-3947-ad4a-05f06a6ae32c | -8.02 | -44.084 | 2025-09-03 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 12d2b3d0-3014-38cf-9243-7c00a98f0c1c | -11.3705 | -43.5868 | 2025-09-03 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| fb47350b-fcdc-31e1-8359-3bceba40ab41 | -8.0605 | -45.3863 | 2025-09-03 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 71534126-ffc0-3211-804f-130085e3d892 | -15.1771 | -52.356 | 2025-09-03 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 24f5a0b5-f398-3fa7-a276-46825ab7497e | -6.5546 | -43.9221 | 2025-09-03 14:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4f741bf0-8fe5-3470-a183-99fa29ec556e | -8.0206 | -44.0376 | 2025-09-03 14:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 6664076a-7d10-3c75-b7d6-b9ac036da4aa | -7.484 | -44.8272 | 2025-09-03 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 6f5b40ae-e470-3983-8d01-0a782827069a | -8.3644 | -48.3116 | 2025-09-03 14:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 151.9 |
| eb7141ab-7b80-3c61-9a04-e54d551059d5 | -5.7738 | -45.2865 | 2025-09-03 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 410.8 |
| ae6ae601-39e7-3312-97bd-6d6cab1de5f8 | -11.6156 | -52.132 | 2025-09-03 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 9d0cec14-e0f8-32c3-b2cf-baa95a5efce7 | -7.7226 | -48.7355 | 2025-09-03 14:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 886fd13e-9105-333b-bed9-61af83253509 | -10.0932 | -54.7667 | 2025-09-03 14:30:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 165.4 |
| 29b62c06-8f7f-3763-a6e1-c0b557954c45 | -6.8465 | -52.8337 | 2025-09-03 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d28bb8f2-5176-31d6-a5a2-47b0bb2b52aa | -9.6415 | -47.084 | 2025-09-03 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| e75dd1f5-3cab-37f9-8d44-27ab980a73a7 | -10.463 | -53.6338 | 2025-09-03 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 8546ced7-bc47-3f9c-ade4-947598c26892 | -5.7154 | -45.5613 | 2025-09-03 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 298.6 |
| df5bcb52-b658-3d65-a4a4-c1a24c26759c | -5.7925 | -45.2852 | 2025-09-03 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 5e5eea31-db1d-3393-9e44-1e1f52cb29d1 | -6.8381 | -45.543 | 2025-09-03 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 17cd2ae3-3e13-3784-b26f-1fb9a3a39200 | -11.9635 | -45.7741 | 2025-09-03 14:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| ae7aa8dd-39f2-3a3f-83cd-90bcf790b3c9 | -11.0181 | -51.5001 | 2025-09-03 14:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 02ed5d73-8017-3d92-a9d1-234378ed5969 | -15.7175 | -53.6376 | 2025-09-03 14:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| d3e2ce04-694e-33b9-bf94-b42e79251f17 | -7.549 | -47.4427 | 2025-09-03 14:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| a08be382-c2e2-375d-b76f-5f03cd5cfda1 | -6.635 | -45.2433 | 2025-09-03 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| fbd0df6f-a172-394a-9d8d-3bde1ac354fd | -11.3709 | -43.5631 | 2025-09-03 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 23ce325f-0f50-3e11-932c-2eb230e22576 | -7.7036 | -48.7587 | 2025-09-03 14:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 113.7 |
| cc8159aa-26a9-3eaa-b4c8-7a8609096c53 | -5.2575 | -44.4581 | 2025-09-03 14:30:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 0eb06de0-fc5e-3280-bf8f-e73d3115b6a9 | -6.3502 | -45.6498 | 2025-09-03 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| f563c1da-92e4-33d6-979e-46d96c675043 | -11.6647 | -57.3533 | 2025-09-03 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 5bf742f2-603f-3376-804a-ebca4271004c | -10.4816 | -53.6527 | 2025-09-03 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 38f6a825-3e4d-36e9-a3b0-bc3e6c0a80f0 | -5.9265 | -57.7108 | 2025-09-03 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 77c0c863-88a8-3215-8a21-2079ae2f5b73 | -6.8569 | -45.5415 | 2025-09-03 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 99bbfc71-8189-3182-9708-67d5cfab3a52 | -8.3837 | -48.2664 | 2025-09-03 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| d6dd8b93-90ef-3427-9eac-8f338d610980 | -8.4604 | -45.0495 | 2025-09-03 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 936062be-6373-3989-bfaa-7ffe271df210 | -5.7923 | -45.3078 | 2025-09-03 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 14254300-91e0-3d28-80ad-cc9e9e36ac75 | -11.9685 | -51.3554 | 2025-09-03 14:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 1f1f7dab-d1ba-3235-ba39-fb54b05d3439 | -8.2006 | -49.5559 | 2025-09-03 14:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 186.8 |
| 95bf26dc-024c-39bd-b6df-ae786a404960 | -7.4842 | -44.8043 | 2025-09-03 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 136.4 |
| bec3ed51-007b-3ecf-a36a-73daa1356d0c | -7.3793 | -49.4075 | 2025-09-03 14:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| c3b14a52-30ad-3c10-b269-d336c7cd498f | -8.3834 | -48.2882 | 2025-09-03 14:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| bd99e141-ed14-3006-9fe9-5b07223cb6b6 | -5.886 | -43.2331 | 2025-09-03 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 55feb06e-65f8-399e-9f06-36385b20e25f | -6.3315 | -45.6512 | 2025-09-03 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 2fac9a8d-0512-3feb-83de-d65ac2e61cfc | -7.7039 | -48.7371 | 2025-09-03 14:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 07fb52d2-3004-37a5-970d-59a0aca8154d | -8.8842 | -45.822 | 2025-09-03 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 6d273c4f-c674-3aed-b161-3517f78ccb6f | -10.5127 | -57.7957 | 2025-09-03 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 9c45b5c7-3392-3db9-8cb2-9b99435803b1 | -10.4818 | -53.6321 | 2025-09-03 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| ab9528ec-f63d-325f-a439-68166683d84a | -5.8884 | -42.9753 | 2025-09-03 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 144.5 |
| 4e92110b-1c4b-3999-ad66-402d57c8a098 | -6.8279 | -52.8348 | 2025-09-03 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 628b6312-6c3d-33a6-88ff-20a5fd586f16 | -8.8839 | -45.8446 | 2025-09-03 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 76e79a51-d605-38d4-b2f8-ca2f520658b6 | -8.0203 | -44.0608 | 2025-09-03 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 133.6 |
| a75007a2-1b2c-3a71-a6e0-55407c7d6ab3 | -10.4632 | -53.6132 | 2025-09-03 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f36e79b1-8203-3f25-a8fe-0cb0863cdac1 | -11.6836 | -57.3518 | 2025-09-03 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 206.3 |
| 133403ae-c9a2-31dc-b012-862e8f8fec8c | -6.7595 | -45.9095 | 2025-09-03 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| af249f7c-61f5-3714-b489-306d447c1c1d | -16.5305 | -55.0807 | 2025-09-03 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 135.6 |
| fd03fe59-fb55-3cbc-b149-fc99d5372bc0 | -13.0156 | -56.8781 | 2025-09-03 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 766ed865-f75d-3ab4-a3ad-0e0f91e65628 | -6.7928 | -44.4776 | 2025-09-03 14:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 3d9101bd-1ba3-3129-a685-8f523c5c5070 | -9.6232 | -47.0416 | 2025-09-03 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 17d32a43-7a2f-3d99-ad42-c0e9c3d94925 | -5.7551 | -45.2879 | 2025-09-03 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 5a52ca58-1c3b-33d0-8f6b-35a85310d34c | -16.2949 | -52.9656 | 2025-09-03 14:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| cb498252-77b0-3f26-8a87-320b6aac7612 | -6.2409 | -43.3911 | 2025-09-03 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8067f273-a26a-3d30-9f07-ceb6fe5ba2ac | -16.3145 | -52.9628 | 2025-09-03 14:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| fa2cf53e-d516-3b7b-99b3-0b2413e981d7 | -12.824 | -48.06 | 2025-09-03 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 8c34ae5f-df8d-32af-b629-220efb6cdcd4 | -12.9189 | -57.0074 | 2025-09-03 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 2069cfab-fa81-3074-84d2-4836a78be24f | -15.737 | -53.635 | 2025-09-03 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 133.5 |


[Clique aqui para ver as próximas entradas](README122.md)
