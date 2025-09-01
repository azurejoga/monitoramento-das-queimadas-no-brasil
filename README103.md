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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55ac5199-b214-3f5f-a683-6484fd92e4e7 | -14.77961 | -48.17381 | 2025-09-01 11:57:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 0e603d0c-5530-306c-a3d4-997a303b0020 | -12.79147 | -47.65575 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e4bebfe5-6127-316d-8b6b-e1e143c17fea | -8.45739 | -39.7933 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bf895f49-e935-382c-a892-49b2e2245b9b | -9.66595 | -47.03656 | 2025-09-01 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 489ac33b-cd93-3c20-abfa-8c9ef7cc819d | -9.24724 | -47.04733 | 2025-09-01 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f64f3086-b913-3124-9fed-358475cc2976 | -10.89616 | -45.80811 | 2025-09-01 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.2 |
| df0299dc-552a-3b8c-9f3f-a0432d8373bf | -14.77694 | -48.18976 | 2025-09-01 11:57:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| e1f034de-197a-3870-aba7-ff6d088bcc96 | -12.98948 | -48.10036 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 44360d6c-b095-3cec-a909-8c417a1d08d6 | -13.03727 | -45.10551 | 2025-09-01 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d4c97195-4343-374a-a7c8-73d53ac9e548 | -11.09149 | -44.61917 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1f569ce7-6d39-3fbf-82e6-0ab92a5aa7b1 | -11.041 | -47.05966 | 2025-09-01 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 00b0ec31-16e7-3eaf-9514-0f94b22370a6 | -12.97419 | -48.11712 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 352c02da-bcda-3e35-a38e-43b9dc8af3ed | -8.85687 | -47.50751 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 75a16aca-5350-3b5e-9f0f-a4d0b117adb4 | -12.95843 | -48.10619 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 449d0c1e-2add-3784-b98b-4d36982c0bc9 | -8.86494 | -45.74831 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4358e7e5-a8ad-3558-866e-f108b3b835fc | -12.59554 | -48.22415 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 2a969b15-e86d-36fa-ab44-dbe016afa5a1 | -14.04421 | -44.56361 | 2025-09-01 11:57:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 554b4d79-7fc4-3484-be7d-171d31e6aa25 | -12.9773 | -48.09894 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 7f5bb89f-739c-37bc-b8f6-31bbecdbff1a | -11.0603 | -47.014 | 2025-09-01 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| b3ef857c-7729-394a-a228-8f450c3a1314 | -9.22713 | -47.09668 | 2025-09-01 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 57ad523f-91dd-3cf5-84fd-dce791feb124 | -11.06286 | -46.99833 | 2025-09-01 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| bbfaf00c-b0d1-3fa3-a395-aaf075eaf61b | -11.47702 | -46.79225 | 2025-09-01 11:57:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 8e5472f9-e791-3af7-ba6b-d57a4b47dcfe | -8.28793 | -44.91973 | 2025-09-01 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 47a570a6-8420-349c-99c9-0e49fa038202 | -12.55865 | -48.21815 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 9e29b1a2-a661-3cf6-afb9-2dcba570aeef | -11.04012 | -45.15193 | 2025-09-01 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 393e77af-001f-3cfe-ae13-dd331988e53d | -9.64133 | -47.79571 | 2025-09-01 11:57:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 121dc27d-f220-39d9-8f9a-cc773042b343 | -9.66338 | -47.05311 | 2025-09-01 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 2b67f2ea-a0d8-3d27-b81b-09f3c01fb532 | -12.39247 | -46.47085 | 2025-09-01 11:57:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8bc87630-7467-3e20-8e7e-efc5062d2e74 | -13.29318 | -46.90508 | 2025-09-01 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 61867ed5-5bf8-334a-9daf-e20099777eb1 | -12.56486 | -48.25703 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| f5b7c876-3d8c-396d-a6ca-86e342bc1374 | -14.79841 | -46.73739 | 2025-09-01 11:57:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c9b38d12-cc9c-39ec-b7a7-7ca592a73a10 | -7.65191 | -45.39029 | 2025-09-01 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 9b139aa3-6b98-3004-ab7b-bf3d98d2f000 | -12.59251 | -48.24283 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 1cd1f017-274d-321c-be11-ad14d34b3448 | -11.37759 | -43.5867 | 2025-09-01 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 257.4 |
| 9b2ad25e-bdd1-3d76-9157-a4ac49f50e12 | -12.83625 | -48.06139 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| e2a2eb11-3a36-3d09-af59-f4ac89a73709 | -9.65751 | -47.05892 | 2025-09-01 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 3b9cf52a-1eb0-37d0-9b79-3f136971a924 | -12.58326 | -48.22206 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 9dcc99d4-a1d4-3fab-bedd-fd312dc321ef | -9.52919 | -45.84042 | 2025-09-01 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 565fe13a-2e35-3500-a817-9da6c0018e50 | -9.49013 | -46.45715 | 2025-09-01 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a80c1522-9551-3dbc-adc3-d22ddd76a5f2 | -12.65506 | -45.31791 | 2025-09-01 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 771323fc-7c73-3fb5-89fe-6e17bef30ce5 | -7.95789 | -46.46137 | 2025-09-01 11:57:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 6d82ee43-dcd9-3191-93f1-4342edc663cb | -12.79411 | -47.63926 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 985aee7c-c2d6-3b1d-afe5-b620c423069e | -11.05418 | -46.99063 | 2025-09-01 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 4fa33b7c-678a-3dd3-b437-c909ea79107b | -9.38057 | -40.24046 | 2025-09-01 11:57:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 6b3b88b0-6c4e-3b24-88ad-a0c5f6246fc2 | -11.05013 | -45.15345 | 2025-09-01 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 76b55ef6-e197-3d47-b8c6-00d1053e23fe | -14.63943 | -48.05155 | 2025-09-01 11:57:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 26f96579-18b8-32ab-8ac8-a3f6c603b2d8 | -11.87853 | -46.7323 | 2025-09-01 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4db1cc51-44a6-387c-803b-6685a85b14a8 | -7.48828 | -46.00121 | 2025-09-01 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 7909d8fc-55de-3894-80d1-628773fa53a3 | -12.31146 | -45.67865 | 2025-09-01 11:57:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c91f09b8-6271-3b2d-bf84-cb83d5311f3a | -9.65079 | -47.81669 | 2025-09-01 11:57:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 255ff72f-c986-35e1-9360-f1d84567ec90 | -7.88825 | -46.98592 | 2025-09-01 11:57:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 97185fa0-0431-358c-af55-72f61da56977 | -11.06423 | -46.91818 | 2025-09-01 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 9536deff-11aa-37ce-8b30-a87dcfe71dc6 | -14.74513 | -46.76304 | 2025-09-01 11:57:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0c12bc24-580d-3f7b-aee3-3411d141f761 | -8.44562 | -47.37804 | 2025-09-01 11:57:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 86213cdf-842e-3d44-be8e-331877ea95d1 | -12.58626 | -48.20375 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 9d15283c-6aad-348c-b5b6-5183974d25e5 | -12.56793 | -48.23846 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 238.9 |
| 60d673e9-8d1b-3e97-9b5a-37b5619b895a | -13.48487 | -46.93127 | 2025-09-01 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 188a96fb-bbb7-36ac-a0f0-a2b69bb71f1f | -12.58873 | -48.211 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 090ce87a-4afd-3991-873b-ee655f826b37 | -10.6015 | -44.33014 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f78b5254-1d6d-3db8-a4b3-d816bf07e390 | -7.39839 | -47.4296 | 2025-09-01 11:57:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a29a89d6-3632-3ba5-b868-9d5ebaaaee4a | -9.22436 | -47.11397 | 2025-09-01 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 6528864c-18dc-382e-8bab-33c58f43fd10 | -11.38103 | -43.62666 | 2025-09-01 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 41fa2950-8a8d-30de-aa61-ae74b541c91d | -8.83198 | -47.50337 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 5a4025c6-c881-38b0-b8cc-8916ff2c8b7e | -11.05145 | -46.99608 | 2025-09-01 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 5c57b677-fe5b-3129-a90f-2e1a744d42b4 | -11.3796 | -43.63634 | 2025-09-01 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| afef9946-29f1-3a94-bd6f-46878be8ec62 | -7.79649 | -44.71958 | 2025-09-01 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a94f8908-d68f-3c21-92ee-57fbcaa513ea | -11.95975 | -45.83717 | 2025-09-01 11:57:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9deada87-c94a-3ffb-b3fe-9b821794fbc4 | -11.05191 | -45.14178 | 2025-09-01 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 3d455f47-a4ff-3373-affc-e84d3e9f8d9c | -10.05281 | -48.09213 | 2025-09-01 11:57:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 1073fc62-bc9e-3c52-979c-fe0ccb6124e1 | -12.32613 | -45.7183 | 2025-09-01 11:57:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 338e22a2-842a-3a7e-b8cc-1e73d90cc4ad | -9.67202 | -47.04427 | 2025-09-01 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 813a05d0-8e3f-352e-b05e-87df1ddaa04b | -9.24452 | -47.06445 | 2025-09-01 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 82273231-c124-3c70-869c-77530bc86243 | -11.08814 | -44.64102 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| e9b039c1-a5e7-36c9-a1af-c8af6b6fe798 | -9.28278 | -47.09506 | 2025-09-01 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 2df4ea9e-c1f1-3800-87ae-f5644a559aa0 | -10.05052 | -48.10546 | 2025-09-01 11:57:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 20887920-56ae-3a06-989c-0f08a8e0cda4 | -10.61266 | -44.32103 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 81090a3f-e2b7-3aa9-931d-8d0817981de2 | -11.68837 | -47.56534 | 2025-09-01 11:57:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 366a62e2-4ebe-3df8-95ac-bb1db4780acb | -8.75346 | -46.67541 | 2025-09-01 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 86f91289-b6b7-3c1b-9f18-dcd8a44756a6 | -15.32958 | -46.12 | 2025-09-01 11:57:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 016b2948-6cd0-34bc-a2a9-978245812aa7 | -13.52121 | -46.98438 | 2025-09-01 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 01a93b49-e142-3c94-96a5-e4088a4948ed | -11.0568 | -45.146 | 2025-09-01 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 98896f58-8d4c-319e-9038-43ab46f8fd7a | -6.744 | -43.7666 | 2025-09-01 12:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 85fba6ba-2181-3a5b-9f37-95b53c81c0a7 | -6.824 | -43.3168 | 2025-09-01 12:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 433df031-e57b-3bef-beef-b6f74f5a6543 | -6.7626 | -43.7881 | 2025-09-01 12:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| bf5391ca-a7a4-33b2-8bfb-1a5104d48ec8 | -7.0948 | -44.3358 | 2025-09-01 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 5a640874-6317-319d-bf4d-47b1b2c64a3a | -11.3709 | -43.5631 | 2025-09-01 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 12d2f669-a51e-3de5-b0c0-c489874b3bca | -11.3888 | -43.6312 | 2025-09-01 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 71f45458-db9b-3be7-8ce2-8ac504284a1a | -7.076 | -44.3376 | 2025-09-01 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 5261a389-bbc6-32ce-82fd-3e1f6601e983 | -6.7438 | -43.7898 | 2025-09-01 12:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 4b9ead2a-0a7d-3180-80de-027ab97057b3 | -11.3705 | -43.5868 | 2025-09-01 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 650207eb-f99d-3d64-a516-852253151d7a | -6.8428 | -43.3151 | 2025-09-01 12:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 6e63a9da-509d-3884-ba74-1b248230a0f3 | -7.9539 | -46.4542 | 2025-09-01 12:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a0763477-b1e7-3acb-abaf-e844a42c6c6b | -11.0377 | -45.1487 | 2025-09-01 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| e344cb5c-ed4e-3053-b912-a7f6128a88bb | -7.0946 | -44.3589 | 2025-09-01 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 543675dc-6cc2-3738-92e1-5bbe9ff7cfb2 | -7.0572 | -44.3393 | 2025-09-01 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| d278b976-18c7-318d-85b8-f05b7c429a26 | -7.0757 | -44.3606 | 2025-09-01 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 0a265d6f-0d1c-3e96-aa10-5a4163bf2458 | -8.1945 | -46.7657 | 2025-09-01 12:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| f56c4f7a-d23f-34b4-8b26-a97102df328a | -6.8426 | -43.3385 | 2025-09-01 12:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| f46d44bb-deab-32e5-8799-7dfa43f7b0d4 | -12.9768 | -48.1049 | 2025-09-01 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d60648dd-127e-3958-a1ac-8e3b7e6edd9e | -19.49143 | -46.59821 | 2025-09-01 12:00:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 64.3 |


[Clique aqui para ver as próximas entradas](README104.md)
