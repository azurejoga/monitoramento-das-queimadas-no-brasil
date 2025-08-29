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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fff69c7-3b08-3530-ad2f-3bf644100279 | -12.098 | -44.7244 | 2025-08-29 00:31:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2708bbac-67be-314e-a59b-6af81fa36612 | -16.375099 | -39.2579 | 2025-08-29 00:31:00 | METOP-C | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dd98c827-7ef3-3004-8e88-26907ef9e9e3 | -13.5528 | -46.9394 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3b46bf70-7c17-3990-854f-d1bdc5115793 | -8.7134 | -47.8694 | 2025-08-29 00:31:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4fae7049-ff29-3859-b389-d0ca8e8c0916 | -11.0935 | -44.750301 | 2025-08-29 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c977bf3e-cf06-38b5-af57-847d057823ce | -7.7358 | -50.291599 | 2025-08-29 00:31:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb493056-ba7d-30da-8e2d-9583acf6ab9b | -11.3365 | -43.558701 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6383e5c-413f-3291-927c-6114d4791caa | -5.6075 | -45.2076 | 2025-08-29 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 116f1dfa-1255-3b7d-97af-cf1c80f7f69b | -13.5407 | -46.883202 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f0f5ddd-aed5-3f62-badb-711ef7ce58be | -13.5258 | -46.861401 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1da50c52-5fa3-34d4-bc3b-13c7c4f354d1 | -18.737301 | -49.158298 | 2025-08-29 00:31:00 | METOP-C | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 974ec9a8-fd62-3f2f-a5a6-dccd8ea02212 | -12.4101 | -46.4991 | 2025-08-29 00:31:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61700c8c-61a6-31f4-b2c2-8a66baeb114c | -11.5867 | -44.651699 | 2025-08-29 00:31:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 37f51520-0df2-3676-b28a-d880218e454f | -17.359501 | -42.637402 | 2025-08-29 00:31:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95fbb4ae-232b-31cb-802f-4037bc135c64 | -5.8694 | -42.9603 | 2025-08-29 00:31:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1f9cef7e-3fde-3d40-88b0-15fbae960611 | -8.4654 | -43.642899 | 2025-08-29 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 244cb358-5fd6-3fc0-91e0-8a63e22d9f79 | -11.3561 | -43.554199 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79ec57fe-f4ae-3462-82a0-8328234d445c | -19.1723 | -46.591801 | 2025-08-29 00:31:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 26375db5-cf16-38b7-9c77-441ceb03bed7 | -13.5586 | -46.870899 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8eef8a41-2821-35ac-8779-93f779b0d69f | -6.7039 | -49.467899 | 2025-08-29 00:31:00 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d924355-0462-3b28-b5dc-1966c7777af6 | -3.9919 | -47.882599 | 2025-08-29 00:31:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7441228-3dd1-302d-b97c-7e2bebf380d7 | -13.9068 | -43.878601 | 2025-08-29 00:31:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5608759a-abdb-37b5-9b39-7cba33637326 | -5.8655 | -42.944 | 2025-08-29 00:31:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 774dc142-87e7-311d-a37b-cc00288bdc79 | -7.0629 | -44.360199 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7da827a7-56bd-3c22-a232-c143079ddd07 | -11.0404 | -45.0616 | 2025-08-29 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 25bc81ea-20f3-3914-9440-330fcf1f90de | -9.409 | -48.229301 | 2025-08-29 00:31:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e689fed-96d9-3df8-b252-5b589d2db64d | -11.5851 | -44.644699 | 2025-08-29 00:31:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4928d7e2-c521-3316-bdc2-37e3eb7b379a | -24.169701 | -49.5704 | 2025-08-29 00:31:00 | METOP-C | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| dd2aff2d-ab2a-3928-b931-243b09a87559 | -7.0514 | -44.355301 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa0a91a8-153f-306f-8b50-6e68d42c81dc | -7.5719 | -47.500702 | 2025-08-29 00:31:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0408a297-9489-38ae-be65-08172a9ef71f | -11.5638 | -47.613098 | 2025-08-29 00:31:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c11d3934-651a-339b-bb24-521f31bc509a | -6.1173 | -43.313801 | 2025-08-29 00:31:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 2446fde6-21c3-3299-856f-94b1f18cce1c | -5.7075 | -45.9575 | 2025-08-29 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5619f207-9b27-3c26-a452-f4bfb75f45a4 | -11.5784 | -49.506001 | 2025-08-29 00:31:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4c1fc23-b764-3aff-882f-784ab9373496 | -6.7079 | -49.4394 | 2025-08-29 00:31:00 | METOP-C | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb6924d2-e188-318b-b870-d7436a358c46 | -5.5408 | -42.660599 | 2025-08-29 00:31:00 | METOP-C | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b1ebe3d4-61e7-3bb5-81d6-a260fb708c05 | -5.5989 | -45.528599 | 2025-08-29 00:31:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d892f8f9-6395-3403-82a5-fd66ec053c75 | -7.7238 | -50.283501 | 2025-08-29 00:31:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28da4591-60f3-310a-aa64-7f9ca93cd00f | -10.9465 | -46.855598 | 2025-08-29 00:31:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5652b16-ab4a-3a60-a31d-a83e0b1acc17 | -13.4913 | -46.843899 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a2dd69ea-ab69-335a-b2cf-3b6d8c65e406 | -5.7091 | -45.964401 | 2025-08-29 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c2f17ca-37ef-3d99-bc56-4a4b71083dfb | -7.0531 | -44.3624 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fdc307b2-58df-3a48-8654-e8dae8781985 | -7.6224 | -42.6889 | 2025-08-29 00:31:00 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e11df281-1eae-31dc-80c3-ce4aa9709ae8 | -11.5915 | -46.376701 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9b3dd465-2c97-32da-bc09-51017b08625b | -7.3306 | -46.1115 | 2025-08-29 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce239c0c-8a00-3dfe-8e7f-586b2e91a6a1 | -4.1143 | -48.013401 | 2025-08-29 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f1e374a-be95-3307-8eaf-5e15aeb6b91f | -13.5666 | -46.860699 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8da233e5-ece8-33a0-a27b-4c1639ac1bdb | -17.921499 | -39.950802 | 2025-08-29 00:31:00 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7bbcd7d3-c26b-37f6-936b-75242c2e462d | -5.8722 | -38.288898 | 2025-08-29 00:31:00 | METOP-C | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ac2fc9cf-e025-3011-802e-356a4792c459 | -11.1033 | -44.748001 | 2025-08-29 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39d27ea2-2bc4-3bae-9c9d-b3f1514ccf8c | -7.4219 | -42.0588 | 2025-08-29 00:31:00 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e2724289-6420-32c5-b0aa-3e631805103f | -9.8711 | -44.680698 | 2025-08-29 00:31:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 19833a6f-f417-3f2a-8b95-7572051b7648 | -12.8262 | -48.098301 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc51828b-1de5-3281-8161-d5d4da8ad517 | -13.1989 | -45.270901 | 2025-08-29 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f6e60c0-5a90-32a9-b38b-ea11b1470259 | -13.202 | -45.285198 | 2025-08-29 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3c00da1-6e18-39c9-b4ff-23b21eaea7ec | -13.4192 | -46.843201 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6846e46d-b1dc-310d-9105-82a848d4c88b | -15.0721 | -48.375401 | 2025-08-29 00:31:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c486bd1a-6e0d-361c-aa0d-5d21b3ff0e5b | -5.6367 | -45.244701 | 2025-08-29 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e0343c9-cbed-3e28-9161-e74815675666 | -4.9216 | -43.187401 | 2025-08-29 00:31:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0aeeba87-a5db-3d15-9d5c-01f0f3ac4c90 | -6.4389 | -44.5625 | 2025-08-29 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02b7810e-2cab-30da-be3c-a9c8970aad4c | -5.7228 | -45.529499 | 2025-08-29 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1320f40a-3ac0-3501-9519-5bcde71d8034 | -7.0596 | -44.345901 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8574963-c736-366a-ab26-fecf5ac3f002 | -13.4156 | -46.969501 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff004e0d-da73-3686-b73e-307b81d039a3 | -12.0995 | -44.7314 | 2025-08-29 00:31:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 03016946-5acc-37c3-8227-0456b872a3ef | -10.0326 | -48.076099 | 2025-08-29 00:31:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37c68588-62b5-38b6-aedc-bad28ba2f51e | -14.9061 | -46.4562 | 2025-08-29 00:31:00 | METOP-C | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fa8abec6-251a-312e-a172-e506730e7934 | -14.6321 | -41.7411 | 2025-08-29 00:31:00 | METOP-C | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c583b7d9-ada2-3cf1-8224-c99566abb840 | -5.5957 | -45.5149 | 2025-08-29 00:31:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc02f28d-c30d-3545-8a9a-3a83eebb9bd9 | -11.3202 | -43.577499 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe2d403f-a6f9-374a-88a8-2641e2bb4e67 | -13.5978 | -46.862301 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 67d2d202-f393-3613-a52d-af767b31569a | -5.6059 | -45.200699 | 2025-08-29 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6731dd7-5009-3aed-8bd1-b53990adc1dc | -13.4174 | -46.9776 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3a2c2395-649a-378e-862b-ea5cba890fa3 | -6.8177 | -44.326401 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e0c4ca8-754c-38a2-bd9b-92f4961557cd | -8.4475 | -43.6548 | 2025-08-29 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d28d595e-863c-3f27-97d5-5789e735e084 | -4.08 | -47.953098 | 2025-08-29 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed8500d2-af7f-38b3-9daf-51f64d7c157c | -12.8256 | -48.192402 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c388c28-46bc-3f71-a7a8-be898a0b21a2 | -6.0465 | -44.4725 | 2025-08-29 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 121de70e-858d-3c0e-8593-e79ec511901c | -20.2964 | -41.297298 | 2025-08-29 00:31:00 | METOP-C | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ced1a136-25f4-32c5-a9e3-936681946d8b | -10.9842 | -46.886799 | 2025-08-29 00:31:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4fb99079-d342-33b4-8176-81566aa7ecce | -24.186501 | -49.5504 | 2025-08-29 00:31:00 | METOP-C | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| 31e238b0-f287-3837-b5d8-53f377027307 | -11.0884 | -44.7733 | 2025-08-29 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ffc0826-d014-3446-ba44-00e7b40baebf | -22.687799 | -46.853802 | 2025-08-29 00:31:00 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7db68025-422e-3101-a31b-6dc152e9136b | -13.5275 | -46.869301 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c22dfd90-fca7-37a8-9432-860fa6310849 | -11.5753 | -44.646999 | 2025-08-29 00:31:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2c960656-52ca-3ebc-a6ef-5e266725fc5c | -7.4009 | -45.9221 | 2025-08-29 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e19c4c2-ce5d-33c6-86e6-f8fa8e3a7ab4 | -12.0671 | -46.622799 | 2025-08-29 00:31:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d226bbe9-7a3c-3848-87c2-f5faf9c2ea84 | -11.3267 | -43.561001 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2137a06c-6b7d-398a-9358-9dfce2574224 | -7.0774 | -44.289398 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2858df0-9c8d-33d8-8eb5-4af9aa3f2e96 | -16.2731 | -39.476299 | 2025-08-29 00:31:00 | METOP-C | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8d2bd7cc-69ec-31d6-a378-ddf05aefb82e | -6.8869 | -43.603001 | 2025-08-29 00:31:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4f7b6190-2c47-3a73-b2b2-c4c7c3203846 | -14.0014 | -46.353199 | 2025-08-29 00:31:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 248fb11c-ae11-3754-9987-729460adda0f | -20.701401 | -43.929501 | 2025-08-29 00:31:00 | METOP-C | QUELUZITO | MINAS GERAIS | Brasil | 3153806 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4938db1e-8b43-31c6-8986-eaf6e9418bb2 | -10.0308 | -48.067902 | 2025-08-29 00:31:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3af7953-4cde-3902-ac1c-991a55a2c156 | -11.3349 | -43.551498 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7de2775f-287d-3c16-bb2b-6380fd89e911 | -13.5655 | -46.902901 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1cb5c0db-1bd5-3077-9ac0-69a6b6ac764e | -13.5471 | -46.865002 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45b3c753-8a78-3e78-b3cf-f17e216abc33 | -13.6732 | -46.8792 | 2025-08-29 00:31:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d899e6e3-bc0d-3cf9-88c1-f6c74d9396e6 | -6.5503 | -43.9305 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea73fc80-8e1a-3c6a-8eaa-15590537fd62 | -9.8727 | -44.687599 | 2025-08-29 00:31:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 87c9bc12-8095-3284-a96b-96c7aae8b283 | -17.9312 | -39.9482 | 2025-08-29 00:31:00 | METOP-C | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README8.md)
