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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbbb7808-c581-3866-985e-1623b950d517 | -6.06804 | -44.05914 | 2024-10-13 05:01:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af4c6ac8-f7c4-3a47-bd95-33bd34afeff7 | -6.06508 | -44.63568 | 2024-10-13 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b290c0f-f7d5-3abf-9705-cb5ca0ba6ed6 | -6.06449 | -44.63998 | 2024-10-13 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f3cc4d2-cc6f-39bc-8110-ba4c7440fdbf | -6.06414 | -44.0571 | 2024-10-13 05:01:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e479140b-04f3-3447-8c4b-b3a4856b90b3 | -5.89133 | -44.31406 | 2024-10-13 05:01:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23b5eb45-a830-3f6a-a08f-442671c71364 | -5.89066 | -44.31888 | 2024-10-13 05:01:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc582e3f-b65c-33ce-acf5-62bc9f5c51bb | -4.88183 | -45.7641 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a13ae97-af73-32e5-83d7-4a97e5f717d4 | -4.8813 | -45.76772 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07e5c98c-120d-3c7e-bca4-e285eba87734 | -4.88104 | -45.7629 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68754478-ef31-3c5a-9233-2712406547e0 | -4.88053 | -45.76654 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 397e2e6a-39dd-3e31-bf8a-5c355512f260 | -4.87625 | -45.76375 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc0bf739-2833-3eb9-aa2a-19e0532d5f1d | -4.8757 | -45.76755 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd0ab1c4-b82e-342c-8cff-4c850cbb1f54 | -4.87547 | -45.7625 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b070494-1006-322c-88ae-64b809fb2c86 | -4.87494 | -45.76631 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbbfcd50-eac7-3ca5-9cde-39fb8757bbc2 | -4.86237 | -45.74303 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 117fb5ba-e8fd-3a2e-944c-a9f583bb0c06 | -4.86182 | -45.74679 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64420192-c690-36a0-8fb5-4a82defe2fa8 | -4.85688 | -45.74201 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75245bd9-fc3b-3185-a31f-e83a21a80070 | -4.85632 | -45.74585 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2ec7ad8-fd90-328b-b7f1-591ba1c898ff | -4.85167 | -45.85498 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e78ccb19-7f8f-3811-a320-90383d11c3d1 | -4.85117 | -45.85841 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b10809f-1281-3e91-9ff9-a5afa7597622 | -4.08241 | -45.54724 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4f99cc0c-ef5b-3535-8603-df18a76942bf | -4.08189 | -45.55087 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4682d50c-0bfa-3300-b8b1-44dd837787c4 | -4.07844 | -45.54389 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ff21a47a-71e2-3a12-9408-bb29d762c010 | -4.0779 | -45.54752 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1291123f-bda7-3b76-afe8-dc7f11bec6a2 | -4.07735 | -45.55116 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| b20ff3b0-241d-3d6b-9fe8-cc48f8cbb2ac | -4.07688 | -45.54637 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 01cb4761-683a-30d2-8834-8b6f496e8439 | -4.07636 | -45.55003 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1b44e56b-9f1f-3889-8234-40839a2207cc | -5.04885 | -44.8537 | 2024-10-13 05:01:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b0c1830-fdef-3bea-8705-4181c61fb342 | -5.04828 | -44.85781 | 2024-10-13 05:01:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 458f0a22-ad99-306c-95cb-79d53ea6dfe3 | -4.864 | -45.03676 | 2024-10-13 05:01:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17d815a7-5997-3b1a-9992-5c61a7aef6b6 | -4.86342 | -45.04076 | 2024-10-13 05:01:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5d984e55-9a26-3915-8926-3ac96d206085 | -4.85188 | -45.03886 | 2024-10-13 05:01:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd722cfb-e74b-3990-a530-ad0b94b9892a | -4.84671 | -45.03382 | 2024-10-13 05:01:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45143d28-cd80-3d37-b811-b3de89533337 | -4.84611 | -45.03797 | 2024-10-13 05:01:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53753bfe-6254-3416-8d0e-38c2dc2bc0ec | -3.73716 | -44.66436 | 2024-10-13 05:01:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e4dca1e-605d-3521-83cd-49341bd11823 | -6.48174 | -46.0616 | 2024-10-13 05:01:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09f569b0-2f7e-393b-a787-2fe5d78de885 | -6.47623 | -46.06068 | 2024-10-13 05:01:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1708e609-284d-319d-83de-1c04f9b0374e | -5.77356 | -46.11155 | 2024-10-13 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94e21f3b-9d78-3211-85e2-132b9a286ccb | -5.76763 | -46.11408 | 2024-10-13 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45ebc862-9cde-33c1-9b5f-58ce58de2281 | -5.70136 | -45.67404 | 2024-10-13 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d4f0129-593a-3c56-9d94-ed90a76a8e48 | -5.57061 | -46.16787 | 2024-10-13 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 73243338-8870-3c44-b630-0a7ed9b130fe | -5.57013 | -46.17131 | 2024-10-13 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4db0f9c8-a9ae-3303-9a6c-7fc90fa95c99 | -5.56904 | -46.1664 | 2024-10-13 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c80d72ce-b4f8-3501-8d89-de1b208bbe22 | -5.56854 | -46.16986 | 2024-10-13 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| daeaaa3e-daec-3bf6-a415-51ba89315806 | -5.56804 | -46.17326 | 2024-10-13 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 923fa165-d88a-31e1-9102-52d724d5fc9a | -5.47148 | -45.83417 | 2024-10-13 05:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db89058f-305d-39d7-adeb-7469fa98eec6 | -5.16876 | -46.15164 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b40a57a5-abd9-36b6-b03a-61da3207de7a | -5.16337 | -46.15076 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 408f7d49-2a26-32ca-b03d-aced3f04bc73 | -5.14262 | -45.39738 | 2024-10-13 05:01:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9213c16b-ca0a-32c6-8d27-a7ef40b75486 | -5.14207 | -45.40117 | 2024-10-13 05:01:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3654ac67-1c06-383c-9e7c-1f30eedbf763 | -5.13909 | -45.39342 | 2024-10-13 05:01:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5b22fdfb-510d-3f86-a56c-9de50a1fb386 | -5.13856 | -45.39724 | 2024-10-13 05:01:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5db75e9b-4109-3b29-a78a-6ee8419fae8c | -5.13804 | -45.40102 | 2024-10-13 05:01:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 260cf903-c941-3037-a409-fb9529f364e1 | -5.13752 | -45.40484 | 2024-10-13 05:01:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96710c88-2f0f-3b57-bf21-0ba5a34994ba | -5.1375 | -45.39274 | 2024-10-13 05:01:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a37e38e5-2404-3c11-b537-bdb729d28cfd | -5.13695 | -45.39658 | 2024-10-13 05:01:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 95d7ed34-6e3b-3a8d-88a7-e1550cc32f62 | -5.1364 | -45.40038 | 2024-10-13 05:01:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 181ba98e-0339-31e7-931b-0ca17d1c1499 | -5.13584 | -45.40419 | 2024-10-13 05:01:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f15cceae-5859-3a6e-b9c2-1e983b1c4194 | -5.13179 | -45.39221 | 2024-10-13 05:01:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e678f14b-242e-3945-bce4-c0118c5229b3 | -5.13067 | -45.39992 | 2024-10-13 05:01:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a031543f-3ea3-32ca-a90c-ee84a16d3105 | -5.13012 | -45.40373 | 2024-10-13 05:01:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9ee259a-0bac-36e1-a496-8fdfbcb2a5f7 | -5.08883 | -45.84367 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02a81593-81c3-33c4-a0f9-6d88f479f5ef | -5.08831 | -45.84721 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e118545c-4adf-39f3-b745-990d97378465 | -5.0881 | -45.84449 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c88a272-e732-32f5-8eb4-9734e7d9811a | -5.08761 | -45.84797 | 2024-10-13 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b43bb7b8-9a83-3ad6-b81c-da8b587e7b3c | -5.19115 | -44.93906 | 2024-10-13 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 342a5f8e-712d-3320-93f5-05e9e5bd005f | -2.2421 | -45.87793 | 2024-10-13 05:01:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5a3d3f6-16a5-3a73-a71b-0535da1e6868 | -2.23683 | -45.87716 | 2024-10-13 05:01:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0f3e4aa-a98d-33c9-96fc-1d50a2c0e72b | -2.61026 | -47.34305 | 2024-10-13 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb65d4f5-5823-3a9c-97e9-88026fc304dc | -2.60999 | -47.34438 | 2024-10-13 05:01:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 877a0d22-8ae6-3764-a2e9-fa1bf05f697e | -2.53011 | -47.26515 | 2024-10-13 05:01:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30887705-1431-3bd0-93f1-838471488cc4 | -2.52929 | -47.27037 | 2024-10-13 05:01:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 12924c81-2418-34ed-bc36-81bca40f3c6e | -2.52856 | -47.26731 | 2024-10-13 05:01:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 16bcae2a-9600-35bb-91b4-70a6a4c01baa | -2.52848 | -47.27556 | 2024-10-13 05:01:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7df42fa5-fe30-3656-9999-5a346b85fcfb | -2.52779 | -47.27252 | 2024-10-13 05:01:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 50f377af-6d8e-349e-8807-5c25e0f220c6 | -2.27431 | -45.98338 | 2024-10-13 05:01:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ac11c31-20c9-3d1b-8774-31403879d6b4 | -3.35183 | -47.31105 | 2024-10-13 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dbd2c5ec-80c7-341c-b0ac-d6a4e2e402d7 | -3.35103 | -47.31637 | 2024-10-13 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1d810c79-2dd9-35fe-b669-287a1acc9301 | -3.35022 | -47.32169 | 2024-10-13 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 798d9ab0-0f34-310e-8d8a-e3757fb33b72 | -3.34696 | -47.3105 | 2024-10-13 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dbfad532-7a14-3cd8-8543-1d0561db4003 | -3.34615 | -47.31586 | 2024-10-13 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a4e5e993-e416-389d-b465-2c3553582cac | -3.34534 | -47.32123 | 2024-10-13 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 73158b61-226d-327c-9ff6-e0a808ac8065 | -2.96252 | -47.36506 | 2024-10-13 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8b72e62-eee8-31d9-aac4-e578ec59a465 | -2.96176 | -47.3702 | 2024-10-13 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd559193-21d8-3960-add0-78265e135c60 | -4.90095 | -47.66468 | 2024-10-13 05:01:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 457248ad-79b3-36a0-b91c-67cb332cf16d | -4.32544 | -47.31575 | 2024-10-13 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3bf947d-6661-30e9-8cb4-6266b87591ca | -4.28864 | -47.29249 | 2024-10-13 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 968dfee7-fb12-315c-8000-296d8efc47e2 | -4.28782 | -47.29805 | 2024-10-13 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2552aea4-841b-3b64-b77f-05ce59eb5961 | -4.28699 | -47.30372 | 2024-10-13 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5efbbef3-4613-3305-baeb-32bb45896c56 | -4.28372 | -47.29172 | 2024-10-13 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 342abbd7-766d-3496-a9a4-6f8ccfa36af2 | -4.2829 | -47.2973 | 2024-10-13 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d54abc5a-d506-3130-a4cd-3f15aaffec3a | -3.60783 | -47.51543 | 2024-10-13 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f839200f-d003-3404-9292-e1f7d6017045 | -4.81997 | -46.86765 | 2024-10-13 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e652789-c946-364e-be71-8441ee1ec727 | -4.81953 | -46.87059 | 2024-10-13 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94e48401-7744-3d63-9988-dd8382e3fd85 | -4.68851 | -46.75227 | 2024-10-13 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f41f1cf4-8792-3c89-924a-0671895ac924 | -4.53555 | -46.55516 | 2024-10-13 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 192a942a-5ecc-3b4c-bdcd-b5d1ee952d73 | -4.53508 | -46.55832 | 2024-10-13 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c1d8f012-d932-3e2b-9f5d-d17be6e58e9c | -4.53461 | -46.56147 | 2024-10-13 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b91d11cd-7f4f-31d4-9ed2-c0028822038a | -4.53082 | -46.55116 | 2024-10-13 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e69f9ee-8357-32e1-9ff0-b763279560bc | -4.53036 | -46.5543 | 2024-10-13 05:01:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README75.md)
