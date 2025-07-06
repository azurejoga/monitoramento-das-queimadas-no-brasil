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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7be4f41-592a-3059-b336-98a9a45ebc69 | -13.00436 | -55.97155 | 2025-07-06 04:53:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c62d06d-e56a-3bd5-adca-d19df8c4391b | -9.92173 | -59.91007 | 2025-07-06 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0307e5e1-8eb2-3228-bf9f-6712db8c7380 | -10.89202 | -56.45675 | 2025-07-06 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41c37ed6-fa42-386b-9335-8fd621b96f7a | -12.02313 | -57.08235 | 2025-07-06 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 00eccb64-5c8d-39f8-9c1f-403631cd6447 | -17.26754 | -49.00829 | 2025-07-06 04:53:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b08bda0f-9f20-3aa0-9d4e-e06c347192aa | -12.58411 | -56.98453 | 2025-07-06 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36681eee-8e55-3b81-be64-30fb2882c557 | -12.93742 | -47.82664 | 2025-07-06 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac986388-39f2-33b6-bef0-989410f8ed21 | -12.01873 | -47.78127 | 2025-07-06 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8476bffa-46a3-3be1-b199-e6ccf2a19182 | -13.66111 | -45.75426 | 2025-07-06 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1f8f8b7-4ff1-3f2e-b55a-af7d44f3f783 | -12.94237 | -47.82294 | 2025-07-06 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be05ba49-703b-3814-8c53-5200c6a4a3d1 | -10.29946 | -57.12505 | 2025-07-06 04:53:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 542a4f49-cfb6-3a03-aad1-428b1d54b73b | -9.93038 | -59.93815 | 2025-07-06 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 25b2e811-6a0e-3aaa-96aa-21d7c75b11bd | -12.03095 | -57.07943 | 2025-07-06 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2956ae38-473a-36bf-be28-bb21d4ad95cc | -13.39897 | -47.82928 | 2025-07-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e96a1b22-d3e6-3289-be8d-ad8e15ac27d3 | -12.03027 | -57.08356 | 2025-07-06 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b66fbd5f-261f-3016-aa01-cbd10f162e2d | -10.9505 | -54.37586 | 2025-07-06 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af732d72-4525-3027-8b83-b067b308ee8c | -11.32907 | -51.44845 | 2025-07-06 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c309ccdf-cdf2-3fb0-8357-2b0cf0eb9bee | -15.88402 | -48.33192 | 2025-07-06 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1840bf28-8a7f-30b8-bea4-c24c9cc94710 | -11.47058 | -61.94166 | 2025-07-06 04:53:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ae9d53a-3e94-317c-8b25-81f939ffedaf | -11.33547 | -51.45344 | 2025-07-06 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae318afd-cf1a-3efc-8ff8-adde0c4dc672 | -11.88067 | -58.73491 | 2025-07-06 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cff88e7f-1e80-3806-bbaa-21781cca65d3 | -15.02721 | -49.24467 | 2025-07-06 04:53:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da4f4fe9-b107-31a2-a298-f535eeb9b896 | -9.93475 | -59.93891 | 2025-07-06 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5e63ce2-da72-382f-a049-027a7c7a65db | -16.45046 | -51.1106 | 2025-07-06 04:53:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fb5d5b6-afd2-3a46-8b8a-8b710719fff5 | -10.30476 | -57.13779 | 2025-07-06 04:53:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb4e3e9b-af57-3272-9b4a-8a185ad03330 | -16.45119 | -51.11267 | 2025-07-06 04:53:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 705644f7-2be8-37d3-b3de-5424d256ae1f | -12.02958 | -57.0877 | 2025-07-06 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6664468e-59b6-33e3-80dd-925e48ccc87f | -11.75968 | -54.23021 | 2025-07-06 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 30631a9c-1c56-313e-bb0c-9c8ac699efdb | -12.58058 | -56.98392 | 2025-07-06 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff4c7810-d577-39c6-b663-fae937a12592 | -11.3285 | -51.45237 | 2025-07-06 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a10bca2a-9419-32c3-b35e-dc45d4696a7a | -11.88013 | -58.73814 | 2025-07-06 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3af6126-0e0d-3407-bbdb-477a9f99fe6a | -16.02824 | -48.14323 | 2025-07-06 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c72a707-8aa4-322e-b602-05d686131a3d | -12.58343 | -56.98859 | 2025-07-06 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f06375fb-5737-3696-a515-f567259e4766 | -12.58192 | -56.97582 | 2025-07-06 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69187de6-eb77-338d-91a1-24ba898ddad9 | -12.02807 | -57.07469 | 2025-07-06 04:53:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ad03a547-c8dd-35d2-8173-d1e9032e5105 | -11.83994 | -57.75283 | 2025-07-06 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e66f486-23f0-3004-8e8f-c175a2c5cad4 | -12.01613 | -47.76772 | 2025-07-06 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3be48f95-4c49-38e4-aeea-c3861096f26b | -11.32559 | -51.44791 | 2025-07-06 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49090a93-dbc9-386d-873b-531204421cc4 | -12.01932 | -47.77697 | 2025-07-06 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1565f0d0-1d7f-3eca-84e6-83cd56f745a7 | -10.67324 | -56.54932 | 2025-07-06 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 968ad9a2-3b0a-3893-b38d-00cc4381abe8 | -11.78069 | -62.92633 | 2025-07-06 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecf57232-faf2-3cc5-b73e-a54dec8d4dd6 | -9.4495 | -63.20728 | 2025-07-06 04:53:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49bc2534-c20c-327f-a3eb-695f00f3baf5 | -15.88348 | -48.33628 | 2025-07-06 04:53:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b05b4f76-9c9f-3893-8a68-0bd57120505d | -10.30403 | -57.14211 | 2025-07-06 04:53:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6530de26-001f-324d-9c73-662eb77ea194 | -11.98026 | -55.51744 | 2025-07-06 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d45fb329-6998-3366-bc1e-45fcd655b071 | -12.94181 | -47.82724 | 2025-07-06 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f780510f-8765-34de-991d-c911ab715475 | -21.68895 | -49.72244 | 2025-07-06 04:55:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e9067f2e-1262-3586-8e21-dd0627c7c503 | -21.32322 | -44.24082 | 2025-07-06 04:55:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4863d34a-3d19-3bc6-9c1e-282ef9467c7e | -20.19812 | -50.70661 | 2025-07-06 04:55:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 5eb4b449-770b-3b26-84e3-444ec509ca43 | -22.68041 | -42.85405 | 2025-07-06 04:55:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 257ae5c9-8c2b-332a-b5ca-ba6d012727e7 | -20.63059 | -55.3377 | 2025-07-06 04:55:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b3ea697b-514f-3b13-8c71-ca5baebc3889 | -20.76278 | -46.77026 | 2025-07-06 04:55:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| df26dde5-5e8a-3ec0-9681-ef13be18c694 | -17.76022 | -50.9364 | 2025-07-06 04:55:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12737800-d323-3af1-a635-aec8bfc47e5f | -21.32939 | -44.24159 | 2025-07-06 04:55:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 56ba92a8-3897-3ec4-a023-b9e62bac2501 | -20.3735 | -54.54187 | 2025-07-06 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8f4ae8e2-3c0b-34ca-afeb-937c8a196854 | -20.47835 | -53.67526 | 2025-07-06 04:55:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e49555d-b70f-3138-9b3a-fed8196c0e04 | -20.72484 | -56.65554 | 2025-07-06 04:55:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7a7cdfe-dde7-322c-9590-5bc3bcc6b082 | -17.69205 | -54.24552 | 2025-07-06 04:55:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e800bbf7-deb1-30d8-b867-91ca2055934c | -21.68794 | -49.72534 | 2025-07-06 04:55:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e0febba7-4161-3392-8f43-7c5d271ab605 | -19.22541 | -54.06533 | 2025-07-06 04:55:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6cd53b4-453c-383f-bb02-d0ca11811016 | -20.72874 | -56.65244 | 2025-07-06 04:55:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59502a0c-b267-3910-892b-3141217bb3b4 | -22.54006 | -48.81228 | 2025-07-06 04:55:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 498e65a3-7b80-3598-911b-b2a8e8a92107 | -30.09568 | -51.24145 | 2025-07-06 04:57:00 | NOAA-21 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 123877af-5ec0-32c4-a6d5-95b0fb4be7d7 | -30.09244 | -51.23884 | 2025-07-06 04:57:00 | NOAA-21 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| 484e7d12-dbe7-3b9c-8dc3-4a1927636f93 | -24.74529 | -53.80991 | 2025-07-06 04:57:00 | NOAA-21 | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3f9c1b1c-fa4a-3dd7-8a71-71a6ad6afa63 | -12.0266 | -57.0845 | 2025-07-06 05:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| f6e97cc1-6d49-37cb-ae75-e276bc9a0d0c | -12.0266 | -57.0845 | 2025-07-06 05:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9718e16b-d915-3f4e-ad6f-60f8db2d9eaf | -5.60143 | -45.18888 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 476d3ec7-9643-3ae4-ad27-d9067f7272e3 | -7.97035 | -47.23401 | 2025-07-06 05:18:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 597faa9d-7835-35ca-bf8d-103a9d2c1af6 | -5.6056 | -45.18829 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc8bcb55-7eeb-35ee-bab4-709d927bfb24 | -2.91015 | -54.48617 | 2025-07-06 05:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7115a3c6-0e4b-39c6-8699-f4306cd608f1 | -3.48803 | -48.44497 | 2025-07-06 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a0897a8-dc1f-3b17-acc3-e2fcf3b042d7 | -5.56838 | -45.21906 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1ab1d89e-afb3-3ca6-a933-ca5c1dcca899 | -7.17925 | -56.71762 | 2025-07-06 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c7310dda-81c4-3af7-80e1-db7709eb2eab | -5.59527 | -45.18106 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d296eb6-d533-3e95-8f7d-f514f32fb5c5 | -3.9822 | -48.41362 | 2025-07-06 05:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5a70423-4a7e-3fcd-bf4e-cd014db876fa | -5.60759 | -45.19664 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04536c2a-28af-3e53-8280-f223b3beeb31 | -2.90573 | -54.49012 | 2025-07-06 05:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4359bd55-ca8a-30c8-b55d-609979a6ec84 | -5.60237 | -45.18208 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46b2893e-9e8b-3e5c-a961-71ff63db7487 | -7.97038 | -47.22944 | 2025-07-06 05:18:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31b3841b-5754-38e6-b55b-78afeea9b388 | -3.86927 | -50.08384 | 2025-07-06 05:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 938ca899-e9a5-3e1b-ba7f-5ee46d238dab | -3.86584 | -50.0826 | 2025-07-06 05:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 683d9b72-27bb-3284-899d-0a9be112c54e | -2.90947 | -54.49065 | 2025-07-06 05:18:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b3e60bc-ff69-3328-be5f-cc341880a4e7 | -5.60948 | -45.18298 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 473b7425-d954-39bb-aad8-35e4de2d6a33 | -3.8642 | -50.08304 | 2025-07-06 05:18:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79737b4a-edaa-302e-810f-54c35c20815c | -5.60854 | -45.1898 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6c02da8-bf35-309b-baab-c4023e6408f2 | -7.97103 | -47.22887 | 2025-07-06 05:18:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ddcd349-6dcc-3220-b939-747d6e7574e7 | -3.32461 | -52.54736 | 2025-07-06 05:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78bb50c9-e2aa-3a82-ac49-9038aeaf36b1 | -5.56933 | -45.21215 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 66da2d46-65a6-3cc1-b8e5-a007335c4bb4 | -5.60332 | -45.17523 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5fcc9d7-905a-39bb-bd13-18e8b2ccb182 | -5.6065 | -45.18145 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9f557b9-dcd1-32bd-9413-47d84fa9cdd7 | -5.60469 | -45.19516 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e5a04c7-b548-33e9-94a0-0a57ae9aa2d6 | -3.32519 | -52.54351 | 2025-07-06 05:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e34bfac-a69c-393e-973b-1c03c645e9fc | -5.57025 | -45.20538 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6e69cc92-d08f-338d-ad2a-9fb60cd72035 | -5.6074 | -45.17457 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d49543d-e50a-3462-af04-52d6b378f771 | -5.5985 | -45.18725 | 2025-07-06 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5557fc56-ffe3-3166-929f-88b21d8075ec | -3.52348 | -48.43902 | 2025-07-06 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c1baa40-4a55-325f-bfcb-adca57d75683 | -2.58048 | -51.92472 | 2025-07-06 05:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96c404ed-9b10-32f8-b902-ab29861a02c5 | -2.58549 | -51.92126 | 2025-07-06 05:18:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f42691e-86e6-397b-82ea-fe2e2c3ef52d | -3.5291 | -48.43998 | 2025-07-06 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README9.md)
