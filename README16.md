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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be30a3ab-2581-3eb1-b71f-b650bb8906e8 | -10.36578 | -57.22677 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3303eab9-d0cc-3067-9e5b-d06ecb61c9aa | -9.122 | -46.93805 | 2025-06-14 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58335998-ef3f-3cd8-9a89-071cf477d9a8 | -15.99604 | -49.82198 | 2025-06-14 04:14:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2570c67c-3e3f-3813-b0a8-08679b46bac5 | -14.20243 | -57.41468 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a8586b22-8e55-323f-bd7c-ee8a1fe587c3 | -9.53003 | -46.29816 | 2025-06-14 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79a65364-eb95-35c5-839e-23873252b036 | -12.68455 | -52.40042 | 2025-06-14 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 5aa9fe1b-b9aa-3395-a60a-2033835fd9a4 | -12.6161 | -57.89275 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e05191f-7cc2-30e7-b3ed-65a99df4b9ef | -16.24874 | -43.7427 | 2025-06-14 04:14:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6542eed-ded8-35db-b384-1c66f0d03cfa | -11.12606 | -53.95093 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25ae2bd7-d8b8-35a0-bfe1-bf2b9c7a3592 | -9.56627 | -46.74052 | 2025-06-14 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eee1ce2c-63fe-337d-82f1-ff8ff06578f7 | -12.68555 | -52.39512 | 2025-06-14 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99b898e2-de30-3f3a-b36a-baa23e7b541c | -14.20277 | -57.40903 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2175ec52-b893-331f-ba6c-c44b5b6ea79c | -14.03648 | -55.13071 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1725b1bd-7544-3d52-a588-831342192f97 | -16.19837 | -46.46663 | 2025-06-14 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a99eefd5-b81f-3276-a352-85a3487af80e | -14.19639 | -57.40755 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24e1c4d7-0ffb-3be1-847c-16088f97114c | -14.20497 | -57.39859 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 197ce4aa-2a6e-3601-bfa2-f71f5c8bbcc7 | -10.60056 | -52.82942 | 2025-06-14 04:14:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c482ea57-0b02-3c10-b85f-00abe47fdbd2 | -9.56117 | -50.77432 | 2025-06-14 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05a71105-097c-31b9-a0e6-7c9b5ceefdd1 | -12.25731 | -51.4429 | 2025-06-14 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef083284-7863-38c3-8746-fa4dd35d38ed | -11.56522 | -54.57476 | 2025-06-14 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fee20f4-ea55-3106-baaa-5682015318f4 | -14.21774 | -57.40152 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41ce001c-1612-31f1-88c8-a6e87b6b5dae | -10.92359 | -56.83807 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 36ccc568-34cd-3706-96b5-e808b2cc71b2 | -14.21544 | -57.41249 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0033f9cd-cfec-3874-bdf7-806282be27b5 | -14.20798 | -57.41611 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c197722f-6ee3-312a-819c-e307bdf3774d | -10.34325 | -44.3096 | 2025-06-14 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c989b177-df1a-3502-8879-ffaf74de8081 | -11.80587 | -57.3519 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 568329fd-8820-3228-b4a9-564148a190c3 | -10.97708 | -42.18037 | 2025-06-14 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e7139a9a-c2fd-394f-a912-9c4a50823bb0 | -11.5634 | -47.43309 | 2025-06-14 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a22a5ef-008b-3037-b00a-d9e564c69bc0 | -10.41297 | -46.6837 | 2025-06-14 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17a78199-c108-34d2-9586-70cdafbcbb78 | -11.0038 | -55.0851 | 2025-06-14 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 26728248-8773-336d-8b3d-a1f77065b15c | -10.06953 | -52.74499 | 2025-06-14 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0b20c0f3-5c11-3dbc-83e2-02574075ba64 | -10.65431 | -44.48946 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 83c72f21-f8ae-3b34-b78e-519654c0af03 | -14.03884 | -55.13129 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9c78867-ba07-3e5c-b428-04830d59aca2 | -11.00967 | -55.08639 | 2025-06-14 04:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 55c04374-52bf-38f8-bf78-f6f5bb3a88e2 | -11.72907 | -48.87102 | 2025-06-14 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a982d35-030a-3706-8e4d-cbe3b07a833c | -8.56524 | -50.07853 | 2025-06-14 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a4ff175-ff2a-36e5-b16f-69a7cd7584b2 | -14.68044 | -53.37486 | 2025-06-14 04:14:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ed41e63-f1c4-36db-a038-ff4dc2222826 | -10.56722 | -52.01316 | 2025-06-14 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55bcf2e7-c07f-3f81-ae95-55f2e9089571 | -15.38394 | -47.86419 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9894fbc-2079-3be3-84bb-a8372aa9eff5 | -14.21662 | -57.40686 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f7d648a9-6aa4-3d44-ab15-6d3dce1ca926 | -15.38861 | -47.85997 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdc62523-186f-3c4d-bf62-93c03da0e226 | -14.21862 | -57.40182 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bf888845-0ff8-36fe-83e3-dc378cb0aa94 | -8.92027 | -49.85357 | 2025-06-14 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a26b996-888c-32ad-89bd-e1d9a3e34938 | -11.88194 | -54.6849 | 2025-06-14 04:14:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69587338-a5f9-388f-bd1b-b29f7ff63e67 | -10.617 | -52.58387 | 2025-06-14 04:14:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fc9f41a-8459-3520-9cd4-95495f055011 | -10.84436 | -53.7846 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17bef438-6c18-37a8-bd3e-7041c7d44f7b | -10.81246 | -44.34966 | 2025-06-14 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a69fe04-0790-360e-ad51-ed30c6ade166 | -15.38813 | -47.86075 | 2025-06-14 04:14:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13e875b0-8260-314f-9a05-9bf6b6727c03 | -10.41012 | -46.67909 | 2025-06-14 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e9b9bf8-3258-31b7-a008-19aaf6aec411 | -13.96058 | -54.4398 | 2025-06-14 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27bf718b-82c5-39af-b761-d56aaf5f51ab | -10.7049 | -46.56029 | 2025-06-14 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32ce01a8-51d0-3bab-8116-b803ccb1b29e | -9.40628 | -50.41598 | 2025-06-14 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d28a50c9-84e7-3b70-b08f-056b008dce21 | -11.89989 | -47.46109 | 2025-06-14 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aaa1e977-20e8-3813-bf04-eefbe70bd1c2 | -14.6683 | -53.3844 | 2025-06-14 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad000c4f-e75c-3aaf-be85-735be2f20a66 | -11.1322 | -53.94851 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0b9070a-e4a6-38f1-b8f1-eb580f207d79 | -9.39852 | -48.4228 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5b69e01d-a1d1-374d-8b6b-b565482d45ae | -13.49667 | -53.48823 | 2025-06-14 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20d58171-8fdc-397e-9fbc-24f3c63778b2 | -10.07469 | -52.74596 | 2025-06-14 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61395fb9-1317-3a2b-b722-5f1fa6401967 | -12.17255 | -44.34045 | 2025-06-14 04:14:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fad5fd5c-bcd3-3f73-b2b5-b0ac35680dd5 | -14.21624 | -57.41278 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 401df452-d241-333c-afed-530700e99947 | -10.93013 | -56.83945 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f9b697c4-4104-30c3-92c6-ae01b918cae3 | -9.39545 | -48.41711 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ca89555-76cf-37ae-a3a4-ca0601e2e9c2 | -14.21113 | -57.40546 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| df45b0b9-c39e-3e34-a03b-228f308a8056 | -12.2806 | -57.26838 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d08c319-656a-3a35-83b6-8af9d921586d | -9.3848 | -57.52948 | 2025-06-14 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d9a566ff-06c2-3bb6-8a11-412994e11e28 | -10.8498 | -53.7857 | 2025-06-14 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0585029e-3455-31c8-8440-0254b7795e05 | -12.55877 | -57.7631 | 2025-06-14 04:14:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54e6caf2-2725-358d-8148-4ae9c3b4fc06 | -11.91638 | -57.47248 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f31b7e82-b379-3db0-bc58-6c710073461f | -16.19443 | -46.4697 | 2025-06-14 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4e298fb-68c1-386e-9e62-f59e33dccbd2 | -11.8963 | -47.46046 | 2025-06-14 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e64c600-0b37-3a60-b0a8-b85507f0d8bc | -10.91822 | -56.83088 | 2025-06-14 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d991edfc-d86b-3603-88c7-fcb4bae49f82 | -8.84413 | -49.24208 | 2025-06-14 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d51e59b-3088-3607-828d-ab5c8748ac4e | -9.40104 | -48.40784 | 2025-06-14 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c0f3d26-07e3-353a-935d-e0a1f1304a7d | -13.50102 | -55.66122 | 2025-06-14 04:14:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b656b56d-5f85-3964-bd6b-1cb31050f98b | -13.49158 | -53.4872 | 2025-06-14 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ca196ad-7356-3d85-8b08-fbddd8aa5c43 | -22.67208 | -47.29585 | 2025-06-14 04:17:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1174d4eb-5aeb-3703-8d3f-16d5ec14a32c | -17.48245 | -46.89344 | 2025-06-14 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 702206f9-22af-3468-8961-1a67c0b221fe | -17.98294 | -44.26493 | 2025-06-14 04:17:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd9f856d-1309-3da4-adeb-8cf3b80f52f4 | -17.93382 | -52.69376 | 2025-06-14 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d72cbf29-3dc3-3ca0-9135-834cf8343088 | -29.72317 | -51.12157 | 2025-06-14 04:17:00 | NOAA-20 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| e9ecba7b-c098-3895-a45f-e41fac62084f | -20.37755 | -45.60158 | 2025-06-14 04:17:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 26b04148-b265-39d3-8aff-e1d9884c1dbb | -20.76211 | -46.76804 | 2025-06-14 04:17:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1adc9193-a63f-3cc0-ab87-8184a25af823 | -22.67505 | -42.85419 | 2025-06-14 04:17:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f58f3aa1-67a2-3404-8b75-c1296d53f3fd | -23.40631 | -46.55719 | 2025-06-14 04:17:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86c3cdd7-98d7-3de2-93de-e39d9697f8a3 | -17.64725 | -47.45143 | 2025-06-14 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7c38a07-f39d-3bfc-95e9-cb129b81f969 | -17.64661 | -47.45523 | 2025-06-14 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c8bea27-45cd-32bd-9da3-d058c2b00953 | -21.42636 | -48.64547 | 2025-06-14 04:17:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3f1e3b2-a474-3586-924f-c7a2948b5da4 | -20.60794 | -48.86736 | 2025-06-14 04:17:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 50b782c7-34ed-313e-9916-195709d7b704 | -22.67438 | -43.47913 | 2025-06-14 04:17:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| b37c1bd7-764d-3fe7-bf6c-e98878ed6dcc | -21.63218 | -45.84773 | 2025-06-14 04:17:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 50a228a5-d9c6-36e2-8368-ab6c83eb1528 | -18.03992 | -39.9243 | 2025-06-14 04:17:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0874c16d-9df6-30c2-b88d-fbbfdc60a882 | -21.10428 | -53.85616 | 2025-06-14 04:17:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5ac7488-c569-3849-be28-96258d99b57d | -16.72342 | -49.07861 | 2025-06-14 04:17:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7be3c78-fa39-3cc3-9d82-aa7a80cffe53 | -16.96954 | -45.68729 | 2025-06-14 04:17:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b9dda6b6-1650-3396-ae0b-0dada55967d8 | -19.52109 | -46.08915 | 2025-06-14 04:17:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cce1bcbf-b500-3166-ae54-f03732d1ee56 | -21.42294 | -48.64479 | 2025-06-14 04:17:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6571c1bd-ca0c-3ab0-acd7-8ec64ee2a441 | -29.95263 | -51.61501 | 2025-06-14 04:17:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 57c11f60-b3f2-3ab1-a9c4-af8b45f4277e | -23.45255 | -46.36748 | 2025-06-14 04:17:00 | NOAA-20 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1f0bf0ca-5e9d-3da1-9d99-7a3183086af6 | -22.7136 | -46.88578 | 2025-06-14 04:17:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 9bb3dfd6-ac98-33a4-9a01-616a73dec05a | -20.30941 | -45.58234 | 2025-06-14 04:17:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
