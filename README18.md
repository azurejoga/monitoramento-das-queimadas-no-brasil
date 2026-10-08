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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73018e39-fadd-3bfb-b9d5-4e0d76dd6e01 | -7.3128 | -55.294498 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 528687c0-9d8d-3113-8b4c-7fa1c0393550 | -2.5228 | -58.091499 | 2026-10-08 00:26:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2bddb0fd-21eb-3013-8f52-80a9dcb611f8 | -3.6359 | -59.5382 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6b30cfd-7b0b-38e4-9259-a6abb6015a6f | -1.1016 | -54.164101 | 2026-10-08 00:26:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a50a8f6d-d90c-3b55-b53c-d71fa1aad9bd | -3.2625 | -54.054401 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fd3ae9e-4209-39db-9fe5-373f50acca09 | -7.2229 | -55.1217 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2e62bd3-7b2b-3bf8-a071-bc2ac62eba2d | -3.2934 | -54.054699 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d083e70f-b29a-3ecc-b6f0-501f8050e8b2 | -2.0434 | -56.369701 | 2026-10-08 00:26:00 | METOP-B | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df63036c-b2db-38da-a427-fe8e9b8a7303 | -2.6143 | -57.580799 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48a7af53-60df-3b55-9955-4d0cba72febc | -3.0218 | -54.129902 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dd081ce-d917-3016-9d19-e7dce968cab8 | -3.5931 | -54.649601 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fed47d68-06d0-302f-8c25-7eb779a705c6 | -3.5719 | -54.647202 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2259fec4-56da-3a84-909a-f1951088b937 | -2.9833 | -54.051399 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2140793b-63fc-376e-bfcb-7f2584c8479d | -3.219 | -53.409401 | 2026-10-08 00:26:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39460834-ca4d-3a3f-b73b-73d716e222e3 | -1.4775 | -54.640099 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fecdfeb-60f2-35e9-88fe-e9538c02b521 | -8.2058 | -46.338402 | 2026-10-08 00:26:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50479e00-023f-314e-8fd2-dec2b919d214 | -3.5862 | -54.2999 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8edb8b4-2bd6-3940-87e1-8f8742a51f21 | -6.1163 | -55.700699 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2887ce5-4959-3ab5-8f76-484cd34ede0b | -2.7788 | -54.104301 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec3adfc6-b9d6-3a67-b870-777cddf3cd43 | -5.897 | -52.041599 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 897dd382-420e-325d-a792-f92fa89bd59c | -3.0755 | -54.139702 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 291a426e-6948-32a6-bc02-7a161fb48560 | -2.9272 | -54.122002 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d1a0d35-46e3-35ce-8e7d-7c8dd7bf457e | -3.0156 | -54.102299 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2784bc78-2ebd-3b00-8f4c-fe611f42cc55 | -2.9803 | -51.239601 | 2026-10-08 00:26:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccc4a251-14bf-37ec-94a9-e26011bc700d | -2.4706 | -56.070301 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c365cc9-2707-30c2-aa7d-8d9f8339a231 | -7.8929 | -54.7085 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f328e358-7275-3c76-bc56-6d7660f3aa16 | -5.3 | -60.071499 | 2026-10-08 00:26:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21ce99b9-8703-3b44-8696-0fec06e69141 | -2.935 | -54.156502 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d08d0c40-0d14-37fe-bc0f-d399b3abcc0d | -3.0003 | -57.7425 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ec0e6f1-f69a-3a1d-8043-6238747cc7e3 | -2.8628 | -54.201599 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d1f73f9-42bc-3c54-a46c-9b208b951f43 | -3.0223 | -54.0863 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25ecada8-d1f7-35c2-aac0-097b82e87ae9 | -11.356 | -51.867802 | 2026-10-08 00:26:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad20ccd-5a27-3f8a-a524-c4a335192e98 | -3.0891 | -54.245098 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 794298fe-61b6-3b1f-9e0e-9dd029b2af8f | -2.7969 | -54.092999 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe014d4b-2f68-3517-9f85-beff1f379a47 | -5.8368 | -50.134899 | 2026-10-08 00:26:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70fde72b-71de-3a14-b9d1-49454c1b8aa2 | -3.0206 | -53.897301 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a19623e-826f-3fb1-adbf-73400a1ad272 | -3.027 | -54.106998 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7cf1ccf-77a9-33e9-a637-7e3d36231e1e | -14.2284 | -48.5457 | 2026-10-08 00:26:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 10af5e1f-99ed-3d80-8502-87fbd5dd9b87 | -3.3146 | -54.057301 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 885e16d8-1fb8-3b5d-8398-16c7504bc774 | -3.05 | -53.8908 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7d6e73b-5c9f-3d86-bd63-c68b0bb54d56 | -3.0139 | -53.913399 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16ae1284-8c42-3ffe-8f19-b173a7b5f94d | -3.0465 | -53.920799 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff667489-45cd-3a54-845e-a47c1d32c3b0 | -6.2511 | -52.867699 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d78e1ad0-8b13-3d8e-8da7-d89f848587b3 | -8.7079 | -45.1656 | 2026-10-08 00:26:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2a0fa069-8a7b-39f3-bf3f-5c8fa8b0ec8f | -7.7484 | -54.938702 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 996d5bc2-c5a6-3a29-a828-22c5d11f485d | -5.8245 | -53.5308 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0657547-7596-36a9-b209-3213ccbfa153 | -6.4821 | -62.837002 | 2026-10-08 00:26:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c488f67f-4b6f-3218-95b4-bc2e7f0a6f77 | -6.4658 | -55.466801 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9b5e582-87ab-3a8e-ac1e-f23eea5b5814 | -3.0033 | -54.1847 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1f40b67-d80a-3550-a67a-c356810d088e | -3.0285 | -54.113899 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42e5ce0b-0647-35b2-8dcf-0e2b2134f4a7 | -6.1328 | -47.9426 | 2026-10-08 00:26:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f0f3e31-e918-379e-b25d-9195da371538 | -15.6824 | -50.5662 | 2026-10-08 00:26:00 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3ce3b3c4-2b51-3828-88b3-34d253350773 | -4.9867 | -56.221001 | 2026-10-08 00:26:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21381003-099b-3eac-8b71-f25697c552c8 | -2.8439 | -57.4576 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48a435ed-f941-35a1-8875-d1442b6059cc | -3.5398 | -59.474899 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a2cc5f6-f2ed-3497-b1ec-88ffba0e581d | -1.7989 | -57.113998 | 2026-10-08 00:26:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f2a41e8-a0f8-32d7-bbd0-7a515dc9894e | -6.2201 | -52.867298 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aa4a04a-eb18-301a-9176-ade6ae1e2b4f | -4.3377 | -43.7929 | 2026-10-08 00:26:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6c36a7f-eaed-3118-8c01-d3d3ae3c8a6d | -3.2919 | -54.047798 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 094f4fea-af89-3e9e-9908-d9ea05d4e540 | -2.7694 | -54.062801 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05dc4c75-a176-3292-bdd4-eb3c2909a8ab | -2.8813 | -54.146801 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e6a532c-9737-3cfa-bb54-0364d5b61666 | -5.8693 | -50.097698 | 2026-10-08 00:26:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70ccfa47-8bcb-3006-9260-d57cc648867e | -7.3764 | -46.231602 | 2026-10-08 00:26:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1390bed-00e6-31a8-8f47-7ee600773b59 | -3.3508 | -50.479 | 2026-10-08 00:26:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb57640b-565b-34b8-9f3c-511e924d5139 | -2.8181 | -54.0956 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5e68a53-b268-32df-a122-e62251d69ebd | -3.5281 | -54.635502 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5692b6df-fc0c-39fa-8cac-1bd51f857771 | -10.2957 | -46.616402 | 2026-10-08 00:26:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 871e73d0-6be1-3a68-b48b-c3bf7510d504 | -6.2136 | -52.838902 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1a26e2d-ea84-3e2a-acd5-c9a95daae653 | -3.019 | -53.890301 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6f45997-3e17-32a0-8c9d-6d4c468537b1 | -7.1827 | -52.611099 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32cd60c0-49bb-3887-8dcf-c9f4625ba97e | -6.2593 | -52.858398 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 096ff8a1-cdf1-392f-a34f-2d7632696906 | -1.4358 | -53.229401 | 2026-10-08 00:26:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29bf07ea-2675-3604-99d2-94e6ed454b3c | -3.0146 | -54.1894 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a126fc79-96a9-3ebd-9a77-ab6bb61949d7 | -4.1216 | -59.881001 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 975d9057-bdaf-317a-b1bc-74c6b886e7c9 | -3.5358 | -54.669601 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6acd6383-69c0-3201-b707-55260d6a62f3 | -3.1031 | -53.761501 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8573159b-d451-376e-a41e-0257bf7ea156 | -2.999 | -54.120499 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b8c1e9f-cff2-39cd-8be0-2e0b10a0c607 | -3.6757 | -59.625401 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb260dc2-c6da-36ee-8828-24e743588135 | -3.0476 | -57.493801 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f99e6ae5-fd32-3205-bbaf-2554952dbbb9 | -1.526 | -54.8088 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0155adf4-a2a4-3c30-ab5f-b007628c1ee2 | -1.2797 | -55.406502 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e507cd5b-fee6-3f63-af61-9d15f3c395f3 | -3.0771 | -54.146599 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2041e599-b8f9-382a-b54f-72740d8557d1 | -10.4211 | -48.791199 | 2026-10-08 00:26:00 | METOP-B | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3d953a1-c639-3bde-a722-27fa53b32871 | -2.937 | -53.937901 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f75629c-31f1-3d32-b0fe-079e68b884e5 | -4.5578 | -54.9505 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a1fdc0a-b981-3e02-8b84-83a76e4c46c9 | -3.4826 | -54.617001 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37a79c92-4799-34cf-b6cf-1ababc358596 | -22.0221 | -49.571899 | 2026-10-08 00:26:00 | METOP-B | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc279346-6297-366b-81d8-7b24160e6381 | -3.541 | -54.6469 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 986b1148-9d31-31f8-8e1e-0e8f29f17259 | -2.7659 | -54.092701 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0d4ac3a-74e2-38e9-a59b-681d4263b34f | -11.7536 | -61.0522 | 2026-10-08 00:26:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b9e434d9-ac3b-346a-98c2-82dc441afff9 | -3.2629 | -54.010799 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae785796-9370-36ed-b702-7409ef1fc4ef | -3.0021 | -57.750401 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b3a486d-6026-3491-ad52-cc576b445391 | -6.2217 | -52.874401 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa2c6c4b-a380-3ac0-b332-fc3e924aaed9 | -3.1459 | -53.7225 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58bca250-376f-3846-921a-86f71b157484 | -9.461 | -64.3283 | 2026-10-08 00:26:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 77b6c451-3aef-3cb3-bfae-3eadf3710f4c | -1.0542 | -53.591499 | 2026-10-08 00:26:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28450bac-82a5-367f-9657-5b2458941246 | -3.0123 | -53.906502 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a6def25-9829-3134-b847-a6f6229704e6 | -4.2438 | -51.043701 | 2026-10-08 00:26:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05d5bace-97a8-3526-8426-3f7fbcfec477 | -2.9779 | -54.118 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36e82f4c-1da5-3eb0-b4b8-3bc0a5ca58fa | -6.3217 | -55.328602 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
