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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7923b50d-c927-31c2-9892-4cdf43b2ef96 | -8.38848 | -46.45901 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 2206969b-f757-301a-895d-63c2f2def710 | -3.55777 | -56.84123 | 2026-08-31 16:33:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 2c0293e8-28b7-324c-b1ec-0150e4b3c906 | -5.66176 | -43.56044 | 2026-08-31 16:33:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 620a59ba-242c-30d7-8b73-7c435a34a2f3 | -6.4074 | -49.9283 | 2026-08-31 16:33:00 | NPP-375 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 4343e39b-464c-3ce2-b65b-1045fa70e87a | -7.67986 | -44.73776 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| df7c44f1-de67-3525-adb9-a7a124e1a4c3 | -7.22426 | -42.76462 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a51cce0e-8c51-34c6-85bf-08c47426f49f | -8.14549 | -45.51781 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ab9ff30a-7bac-3064-9339-028bc5d7b32f | -7.93099 | -45.00662 | 2026-08-31 16:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 19a6aab3-bcb1-3649-af7a-73f5b498b9a7 | -7.64829 | -46.71797 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 19c07ab9-2f36-35fd-b932-292d2e6f3178 | -2.88606 | -41.79799 | 2026-08-31 16:33:00 | NPP-375 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 49f18ade-7596-33d9-bff6-6c523d53ecf7 | -5.85216 | -52.0812 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2a397493-cd85-364c-bba8-b65e9c989371 | -6.8414 | -41.72388 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 22fd9aa0-e87a-38b1-bbd8-b1746b6689d8 | -7.35078 | -41.16026 | 2026-08-31 16:33:00 | NPP-375 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3f351ddb-5c3b-3da8-9b28-deefc5f0742b | -6.77054 | -52.92574 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2c589768-0495-39da-854f-f6bea508d081 | -3.39743 | -43.26662 | 2026-08-31 16:33:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e77016c3-b47c-3d06-8b28-e6f926c623fe | -2.0376 | -48.22972 | 2026-08-31 16:33:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 871d50be-ae50-3f7e-8f0f-904d74b11238 | -5.24633 | -55.90445 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 52291a26-ce89-304f-b318-da4e8feca6bd | -2.79547 | -49.57839 | 2026-08-31 16:33:00 | NPP-375 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 6c47c651-a735-3707-8c78-42510bb18a44 | -2.8647 | -44.93811 | 2026-08-31 16:33:00 | NPP-375 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a6631fe8-381d-3002-abef-78f666416ec7 | -6.06055 | -53.83501 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5125a7a6-c29f-376c-ab41-78189fd4bacd | -6.15832 | -52.63603 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b2e0e82e-da07-315b-ab07-1a5f45e163cb | -6.50245 | -45.12271 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 52220856-fd12-3169-ba9b-b7e2ba2615d8 | -7.78986 | -44.06511 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b487db17-282d-3b1c-b31d-3114133f1682 | -5.66852 | -40.72017 | 2026-08-31 16:33:00 | NPP-375 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4d39e03a-2b5d-3196-a6a7-d91a66f69e57 | -5.75993 | -44.12161 | 2026-08-31 16:33:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 16c3707d-41df-3352-84a1-0b55c6d02c7a | -5.87374 | -52.1571 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 08eba55f-a71c-3690-96d5-04540aaf24df | -6.21827 | -53.57807 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| fdbe52ce-9756-36e8-8199-6451d586f97d | -6.13887 | -53.5336 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| e90f5b04-af8f-3164-97cd-f0d7bc91e457 | -6.84264 | -41.68756 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 21b1af2e-1994-3cc5-82d1-9d713e419d87 | -7.21389 | -42.74125 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| a85c0c25-43ad-357d-a32e-08911ba88b4c | -8.41602 | -47.72393 | 2026-08-31 16:33:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8d18b8e-37d4-3b40-95a3-4be5cd751748 | -7.413 | -44.24679 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ebb2b967-06ad-381e-a29d-ea0eb0766acf | -6.33837 | -54.69014 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d8705619-b2a6-3944-a6c5-3f16173e0d46 | -7.79382 | -44.06828 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1ec4c566-6814-329c-ae90-364b1f32942a | -6.91634 | -55.72397 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| f35b9964-d589-394d-aabc-d4f3be7a90ec | -7.04723 | -45.40402 | 2026-08-31 16:33:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 87edf697-c885-38ea-802b-404e3a8ed6a2 | -8.14893 | -45.46465 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 4364be4f-d2fd-3ff1-805a-4801dccf3bad | -5.43915 | -48.98929 | 2026-08-31 16:33:00 | NPP-375 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e843d0e-06b8-3734-a0e3-5fc0d64f2929 | -6.77188 | -52.8974 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 565dc594-06ef-3e98-ad0c-8d6a54195759 | -6.84475 | -41.72335 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| aae7ddca-b5f0-3c72-be75-325381f875a0 | -7.76834 | -44.06062 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 95ff780b-32df-3a6c-b656-ba442915b64a | -8.39919 | -46.50666 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4a27f6f9-e1c2-3a68-a7dc-ca53394a4d3e | -4.95907 | -55.85107 | 2026-08-31 16:33:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 83aa1839-c5e4-3561-af32-8317d395e4e0 | -7.36566 | -45.07111 | 2026-08-31 16:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2b2cd8d3-4d6d-3b79-ae9c-a221c8f53272 | -8.12662 | -45.49007 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 06af29cf-026a-3f8e-a003-4b7fac5f0524 | -6.80423 | -43.5598 | 2026-08-31 16:33:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75a6bb0b-8b7c-3208-8c43-641d36cb5e0d | -0.22705 | -49.0879 | 2026-08-31 16:35:00 | NPP-375 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d29b265e-a4c6-3a4c-b231-65989ce63397 | 1.74188 | -50.91493 | 2026-08-31 16:35:00 | NPP-375 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1803221a-d771-3fe6-abee-c71f0bd00988 | 1.74156 | -50.90944 | 2026-08-31 16:35:00 | NPP-375 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1d44a812-0fb7-34c3-aef8-aa9199542b00 | 1.5627 | -56.07032 | 2026-08-31 16:35:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 328cb03e-54f2-36f6-b6c0-6a81f9de0422 | 2.19109 | -50.85196 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c1e34c62-8f02-38f0-87b7-4e92dcd6db41 | 1.74529 | -50.91447 | 2026-08-31 16:35:00 | NPP-375 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 28f0f18e-92fa-3a26-84d0-84cbb01f3dbd | 2.19141 | -50.84959 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 89c4b469-6b01-33e8-942c-3a950218dc55 | -1.21708 | -50.40017 | 2026-08-31 16:35:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b7af93ce-53cc-366f-97f2-f709cdbf5ef1 | 2.53486 | -50.94711 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f161b3e0-946b-35db-b02a-7ee52bf45b2d | -1.047 | -49.67098 | 2026-08-31 16:35:00 | NPP-375 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f1e492d4-1f87-3bd1-aaf3-a12927dcd31f | 1.55945 | -56.07295 | 2026-08-31 16:35:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| f3bf5b7e-124f-3c22-996f-ff750fe2409d | 2.33525 | -50.90415 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1deedfec-cc2b-3bee-8e6a-24eaf608daed | 2.19075 | -50.85386 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 06f47f91-1b2d-3bd7-8d05-42a42b1d9af5 | 1.74085 | -50.91379 | 2026-08-31 16:35:00 | NPP-375 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 261aecba-ce43-3c2b-a674-bdc6ba57c532 | 1.5556 | -56.07438 | 2026-08-31 16:35:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a8996fb7-e866-3ee1-825b-483644a8c2b3 | 2.72054 | -51.04787 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 10.9 |
| aa82f9cc-8a8c-3be0-8552-d81d528a5e23 | 2.51852 | -50.85389 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dabddd6b-0305-310f-b181-435e83b400aa | 1.56189 | -56.07536 | 2026-08-31 16:35:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 97370559-24be-3975-aee5-e4922a6a3fce | 1.37253 | -50.75132 | 2026-08-31 16:35:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 38.5 |
| f0961a55-3d8a-3139-8772-22c5a740fea5 | 1.74256 | -50.91058 | 2026-08-31 16:35:00 | NPP-375 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ea38252a-ec03-3532-96c7-a317d5cfa8bb | 3.2327 | -51.32628 | 2026-08-31 16:35:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29e7b609-c529-393b-8c04-09776d5cf7a4 | 2.04323 | -50.96724 | 2026-08-31 16:35:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 55241858-0cfe-3baa-9b99-5d47c0e0851c | 2.51415 | -50.85322 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bad2924f-d228-3127-9789-c82b7846d681 | 1.747 | -50.91127 | 2026-08-31 16:35:00 | NPP-375 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b7794f93-6253-3e79-8223-51eecb7832c1 | 2.5185 | -50.85424 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9d2c04b-ba58-37bd-a305-312988387195 | 2.04969 | -50.95497 | 2026-08-31 16:35:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e066e772-125d-3c5a-88e1-7211a58ebce0 | -0.8084 | -49.20476 | 2026-08-31 16:35:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f904e55e-9cc5-38c5-b3f4-9f0126396ce8 | 2.1904 | -50.85621 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8fa979a8-ea57-3169-b806-df0a67e8fee5 | 1.5564 | -56.06937 | 2026-08-31 16:35:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 9d6211c0-af72-371f-b452-89c4aa4d8c1d | 2.04525 | -50.95429 | 2026-08-31 16:35:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| babb7555-53e0-3721-9e24-2b2c1ee27653 | 2.18971 | -50.86045 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 33e0c1dd-46e2-3e05-8845-40e8cbaa6e2e | 1.56349 | -56.06537 | 2026-08-31 16:35:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8d13da04-45d6-305e-bd43-debb5a298422 | 2.70543 | -51.36858 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f5fabd6-ce02-377b-a090-e5a6a76a97ec | 2.19009 | -50.85811 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4af1caad-5d1f-33a2-8a26-26b18aaf53d6 | 1.13193 | -50.96813 | 2026-08-31 16:35:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e6db330-7cfa-3f53-a8aa-187e9395289c | 2.51915 | -50.85006 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d82f2e1c-aef7-3ce9-bc01-917f9af89f99 | 1.1035 | -50.97282 | 2026-08-31 16:35:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7adaf917-d1dc-3183-b5d4-d0277d7d5564 | -1.86583 | -56.28405 | 2026-08-31 16:35:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bcfb5117-49ec-3222-b37d-5ab8403b54f8 | -1.21641 | -50.39572 | 2026-08-31 16:35:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 23b98569-db05-3ec9-8799-257b1ac3f4b0 | 2.05278 | -50.96426 | 2026-08-31 16:35:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3c55d2f9-c8b8-343c-9cfc-fc87e4e032b5 | 2.53925 | -50.94779 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 840f105f-d6e6-3f5e-a8f4-140078ad7bce | -1.12082 | -49.70496 | 2026-08-31 16:35:00 | NPP-375 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b64440bc-f58a-3389-92cd-46a3d48cfa9a | -1.22091 | -50.39507 | 2026-08-31 16:35:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 184849d6-eba6-36bb-8adf-7f5a04556867 | -0.82981 | -48.08841 | 2026-08-31 16:35:00 | NPP-375 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 88d94034-372e-326d-be07-6c77d4a231b0 | 2.72495 | -51.04858 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 99e7f766-b3b8-3a39-92d7-6923a126c515 | 2.05345 | -50.95995 | 2026-08-31 16:35:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fea14bbb-84c5-336b-8918-27903e821b0a | 2.70614 | -51.36414 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b96d85a4-a433-3e29-9ff0-ff50d8146d3c | 1.74973 | -50.91514 | 2026-08-31 16:35:00 | NPP-375 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 565afa19-3f90-3536-91f1-e72d698275bd | 2.05412 | -50.95564 | 2026-08-31 16:35:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4d9a7940-f154-35bb-ac20-51ccb15a147e | 2.51413 | -50.85355 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 65c8fd68-208e-342b-8840-9e769687906c | -1.22158 | -50.39951 | 2026-08-31 16:35:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9868f6c0-5709-3113-9985-42de2073e903 | 1.56028 | -56.06796 | 2026-08-31 16:35:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| d677244f-140c-3d19-a9b3-9f6447940c23 | 1.37321 | -50.74706 | 2026-08-31 16:35:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 97202519-a097-3270-b241-a7dce17aaca0 | 2.33593 | -50.89991 | 2026-08-31 16:35:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |


[Clique aqui para ver as próximas entradas](README135.md)
