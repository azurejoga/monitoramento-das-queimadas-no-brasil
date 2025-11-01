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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff6bae61-9677-3a88-a41f-3c81471ea3eb | -6.46433 | -43.56248 | 2025-11-01 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6369533-be40-31f1-995a-41643a0eb32a | -13.71291 | -43.78168 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 930b1beb-1194-331a-a81b-196003c332ba | -15.72997 | -43.15989 | 2025-11-01 03:49:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7f22ddb0-7a62-3dbb-a547-b103b21907bc | -4.82251 | -45.79374 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1816bdb8-db46-366c-a353-1032d5f0bdb1 | -4.67134 | -45.81226 | 2025-11-01 03:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b814f8af-2cb2-346a-84ac-1db1eb18ead7 | -3.53138 | -47.55847 | 2025-11-01 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acfe76b3-6112-3026-b1f6-d536294c438c | -5.88633 | -44.52754 | 2025-11-01 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e7ebe2ca-4745-3a52-a4e4-5f579ce2ab07 | -5.70584 | -43.20751 | 2025-11-01 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1fc84db-1f18-34e7-93b9-320cd4a2a7b3 | -5.06934 | -45.11728 | 2025-11-01 03:49:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d77bc69b-3e2d-309f-8b10-a7f61d0bd72c | -3.88501 | -47.17934 | 2025-11-01 03:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2bfe578-fd10-31f2-92d7-13ea234c7a96 | -6.46732 | -43.19125 | 2025-11-01 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f2eb5d3-b2eb-39d3-9423-0048e7b7d846 | -12.2962 | -48.05359 | 2025-11-01 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 47e563f7-4bed-3680-8f0e-b6adb8848a9b | -5.53498 | -46.54153 | 2025-11-01 03:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6398f079-4fa0-35d8-aabc-60ef2698b183 | -4.43983 | -46.03857 | 2025-11-01 03:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ed10d7f-7bba-3bb4-91e1-ce4f6ad71870 | -4.75283 | -42.5692 | 2025-11-01 03:49:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 42a1f01b-1415-36a1-8b16-214aade6afa2 | -5.48241 | -43.085 | 2025-11-01 03:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98caf00b-249c-339e-babf-6a966208c5a7 | -13.29714 | -41.93032 | 2025-11-01 03:49:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 43abf8bf-7109-37dd-a245-2c44c2bca3a9 | -5.88731 | -44.52197 | 2025-11-01 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8eb4b203-1376-3c75-9b1b-0a6365f2e5c3 | -5.0361 | -43.60775 | 2025-11-01 03:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c89b1c0c-0a50-315b-be0e-f6cd8e41a1e8 | -5.92719 | -43.37106 | 2025-11-01 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8ecb5e7f-4293-3d18-9290-8a38de156f56 | -15.29363 | -41.6009 | 2025-11-01 03:49:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4f3061e5-a362-31e9-986b-902b1ccf74ba | -5.79409 | -35.38095 | 2025-11-01 03:49:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 85b91f3c-5e3b-31bb-8a0a-97eec56095b9 | -5.25999 | -45.61266 | 2025-11-01 03:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4702ad57-789d-345e-880b-0eac31a114c8 | -4.29544 | -46.26733 | 2025-11-01 03:49:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bc22b03-d692-30c8-b1c0-88cf24c59d9f | -4.56605 | -49.41653 | 2025-11-01 03:49:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dd04b23-901b-33cb-8684-9a6f4ef08e5c | -5.06989 | -45.11404 | 2025-11-01 03:49:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9b36a1f-e309-35fa-97b1-bd96b3a82072 | -4.56983 | -45.87747 | 2025-11-01 03:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1634158-dd22-353c-b512-43c244f2c624 | -5.11444 | -43.39013 | 2025-11-01 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c06dd3be-9365-3e5f-9668-283534f1df53 | -13.13471 | -44.0113 | 2025-11-01 03:49:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d38f053-d111-3c62-af1d-9e67ef75e6be | -14.02685 | -43.41312 | 2025-11-01 03:49:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df089e69-99c9-3b03-b174-9307f8c24681 | -4.67889 | -45.80693 | 2025-11-01 03:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e05cac1f-5bda-3113-a6ed-b42aec88cd48 | -13.29634 | -41.93491 | 2025-11-01 03:49:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eaa6fd12-0cf4-3365-849e-065e4670e08b | -15.39066 | -43.50241 | 2025-11-01 03:49:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8875a97b-138a-32ab-9c9a-a6bf6ecfbbfb | -13.51494 | -47.10911 | 2025-11-01 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3af84e28-965c-3ab0-af4d-8c69ad6617e6 | -4.82861 | -45.79087 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f10d0e83-6031-3732-9b63-75e5b6813c76 | -11.83273 | -46.00847 | 2025-11-01 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c3c0bb2e-7b22-393a-8be6-9a45bd146190 | -14.60387 | -42.88711 | 2025-11-01 03:49:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 325c23b4-5f78-36ec-a81c-5af847df47d7 | -16.07825 | -40.367 | 2025-11-01 03:49:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6dd3732c-5529-30f0-bd9f-e27a0e7b2e87 | -13.50793 | -47.1181 | 2025-11-01 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29f156fb-a0c6-3594-a02b-950e884024ce | -4.44724 | -44.21462 | 2025-11-01 03:49:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fdbc936-f426-3952-8c48-f4a8db190721 | -10.33648 | -44.65129 | 2025-11-01 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c281c654-d468-34f6-9639-aa352aab2ec4 | -11.8376 | -46.00949 | 2025-11-01 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e90e80d8-81dc-3515-a0a9-6c096efd46cd | -7.02572 | -38.82466 | 2025-11-01 03:49:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a1ea94e2-13bd-3744-8c87-9ae073d03227 | -4.56359 | -45.88102 | 2025-11-01 03:49:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd988c13-57b5-3d83-ac27-865d9efd7982 | -5.29975 | -45.34508 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6085388b-2403-3013-9f96-cf14a24cdd6e | -13.74592 | -43.60133 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a9c84c5-1116-37ca-8293-6ec056b3a139 | -11.73257 | -47.47077 | 2025-11-01 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d2fbbea0-9e18-3052-9fbd-dfed2003656d | -13.82513 | -44.44774 | 2025-11-01 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54203578-652b-3236-9dc5-b3ba0702603f | -13.71287 | -43.78656 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad9b764c-51e1-39f9-9c75-c0be6b3642a8 | -5.21293 | -45.92405 | 2025-11-01 03:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69d32212-2c3f-3b7b-a03f-8ff57baf1bf3 | -14.20709 | -42.86987 | 2025-11-01 03:49:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9ccb05e6-c882-3439-af67-21a88678c6c9 | -4.33626 | -44.53667 | 2025-11-01 03:49:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0c01d50-1257-39bc-81eb-323054a4f4b7 | -5.23731 | -45.05685 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c076d157-8a64-390b-b737-05cac7f24fda | -4.7768 | -46.5034 | 2025-11-01 03:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55d02120-98a1-3781-a34f-2ede68ff97a5 | -5.22045 | -44.80468 | 2025-11-01 03:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55ccbc34-be21-3762-872e-593ca9bd662a | -5.23495 | -45.05819 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de0d030a-ce65-36c9-a14f-428c57cf71de | -11.66229 | -41.68684 | 2025-11-01 03:49:00 | NOAA-20 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83a840f0-04e9-3555-a049-f94de2b72737 | -11.73007 | -47.47306 | 2025-11-01 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3d4d361b-5b3f-3f94-86b2-81d2886e6841 | -4.57826 | -44.99054 | 2025-11-01 03:49:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c50886ea-b1d5-3c72-85e4-ae723812e14e | -5.72422 | -44.5367 | 2025-11-01 03:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b8b895b-392b-38b0-a814-3fda913c9f96 | -4.18028 | -47.65831 | 2025-11-01 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c5d00616-16e6-3a0d-8976-731f9f416d91 | -4.433 | -45.91635 | 2025-11-01 03:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a3ef60f-a3b1-3b36-b029-ca3eb31cd7ae | -12.59919 | -48.33961 | 2025-11-01 03:49:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04e1350c-ee53-353c-af7b-77d778544e3d | -13.66702 | -47.22529 | 2025-11-01 03:49:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 833a9b0d-6ec1-3320-8ed6-1dcc50f859e8 | -6.85537 | -39.8113 | 2025-11-01 03:49:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a529ad1-07e1-3b2c-bffe-08f125a6dea5 | -13.37463 | -43.59316 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d9875ad-b3d9-33a9-89ca-cd81fb8c7d0a | -4.77497 | -46.50317 | 2025-11-01 03:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da62f134-dcd8-3da3-89bd-8f4978df997c | -5.76006 | -43.92073 | 2025-11-01 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe0dcdba-1523-31ec-86a2-dbaba9b3f8ac | -5.35194 | -45.03578 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc892925-644d-3a97-8bad-67767b11ee68 | -6.16364 | -40.26486 | 2025-11-01 03:49:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dbdc39d4-62c3-3c0b-a6b1-0c2634ed8e3e | -10.4084 | -44.32938 | 2025-11-01 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb5ed896-cc4e-38dc-9367-5faaf5cb3837 | -4.18112 | -47.65351 | 2025-11-01 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 885ead79-78e8-38fb-a5c2-15532028d621 | -13.71628 | -51.45794 | 2025-11-01 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 802fbbf6-3f16-3f9e-9cee-d88035acecea | -13.65508 | -44.40422 | 2025-11-01 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e14c5f08-138a-3458-aad0-0a6697f6a2cd | -4.45216 | -44.21545 | 2025-11-01 03:49:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8ab04e82-4eb1-3e8a-a399-8bd069a70a28 | -5.48688 | -43.08578 | 2025-11-01 03:49:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d2e917f-fdd2-3480-bc77-24d14bc08878 | -13.71222 | -43.7854 | 2025-11-01 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbb742b8-1a36-3afa-94df-1a2c5597556f | -13.21022 | -43.13177 | 2025-11-01 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2c956057-dda7-31a5-88ea-a3ba78d9b068 | -5.84808 | -44.65327 | 2025-11-01 03:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 613de82e-3152-35b8-9dd9-9f7e206675fa | -5.59843 | -49.08128 | 2025-11-01 03:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55f32b23-3d42-3569-b461-f8853fda1b84 | -11.73192 | -47.47409 | 2025-11-01 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ba22350e-687c-30df-b72d-766560227677 | -5.6734 | -43.23461 | 2025-11-01 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9613b350-8c87-3375-9ae2-b9d79fdad227 | -5.21592 | -44.80077 | 2025-11-01 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0eddceea-aedf-37b5-9741-e76cbf9313f7 | -10.53007 | -44.22985 | 2025-11-01 03:49:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ac8eee4-7125-393a-b338-db83b2bf92a8 | -13.65429 | -44.40853 | 2025-11-01 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3b3cc9b-b17a-3d57-a7bd-32ea920a6761 | -6.79722 | -42.21793 | 2025-11-01 03:49:00 | NOAA-20 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b7f994bd-c4a9-3bab-afe5-cd7bedaa7384 | -13.53019 | -47.11239 | 2025-11-01 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a1f96717-6ec4-3ca2-9708-ee0f219a469e | -4.79142 | -46.47534 | 2025-11-01 03:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85ea4c5b-805e-38cd-ad58-b4053b57de20 | -5.8798 | -44.52514 | 2025-11-01 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14e6b4eb-1560-38ea-ab9e-61f78f3d1f44 | -10.60725 | -44.66716 | 2025-11-01 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 318bb48e-b6db-3aab-917a-234b46daf41c | -11.83656 | -46.01507 | 2025-11-01 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 762dda8d-3448-3607-a0df-e83acb130ac7 | -11.28108 | -41.73839 | 2025-11-01 03:49:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5ec2e495-43d6-37b3-a15f-af987b40f6d2 | -13.63481 | -43.17015 | 2025-11-01 03:49:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ef499329-68b5-301f-b890-bce31a30a5eb | -4.66284 | -41.96066 | 2025-11-01 03:49:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c12b165a-0e3b-3303-b4eb-75ff729df676 | -5.13362 | -43.3886 | 2025-11-01 03:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4adffe59-ab88-396e-864f-91fe1b3570ae | -15.29335 | -41.59947 | 2025-11-01 03:49:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c126f0f-beb9-3185-a796-9b1d1e85500e | -5.10081 | -44.2727 | 2025-11-01 03:49:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2df580a1-da16-33ed-b508-03950d1624dc | -4.43246 | -45.91955 | 2025-11-01 03:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21062c5b-067a-30e1-8fb9-ee47687dc8d2 | -15.1145 | -42.25838 | 2025-11-01 03:49:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 842786ee-27df-3d03-b4e1-12de7eae0c8e | -4.63923 | -47.96107 | 2025-11-01 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README14.md)
