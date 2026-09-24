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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34b071af-2cdf-3988-b675-bbfc45945467 | -3.4459 | -50.069302 | 2026-09-24 00:16:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 326881a1-8a59-35de-bdf3-4a23338e97fc | -7.7529 | -50.056999 | 2026-09-24 00:16:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee25a182-6ecb-3e92-af4a-fbd50ebf61d2 | -12.0917 | -50.752499 | 2026-09-24 00:16:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65cce3c8-d237-3c07-a42c-1d018b7d553b | -6.68 | -55.043999 | 2026-09-24 00:16:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6930b523-8a34-377f-b8ef-7669b89cf422 | -3.7185 | -54.196899 | 2026-09-24 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2f705a8-7553-328d-8716-a4b55b034f7d | -12.1196 | -47.375702 | 2026-09-24 00:16:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec83ba0d-af4a-3dac-84ff-b2e49f25b570 | -15.2315 | -43.258999 | 2026-09-24 00:16:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 8581b3fe-6f0a-3c51-985a-6fa29f2ed19f | -10.8779 | -45.065899 | 2026-09-24 00:16:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e326e166-0005-3878-af75-6fd3cef5fb61 | -7.6734 | -45.472401 | 2026-09-24 00:16:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b810d6a-a0b7-331c-9067-8f3ad766109d | -2.9459 | -49.190102 | 2026-09-24 00:16:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d15799d7-06ca-3837-929b-32f0bb33c691 | -4.9828 | -45.549301 | 2026-09-24 00:16:00 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03cefa37-3874-3822-9213-9e3a17ba16cf | -9.8347 | -48.4725 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab0a5572-5d92-3830-b3c2-f3bd9046d978 | -9.8479 | -48.485199 | 2026-09-24 00:16:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7530054f-fb86-37b4-8a21-120499bc349d | -13.4538 | -46.2771 | 2026-09-24 00:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| df650942-fcc5-382d-9817-3934a083438f | -11.9389 | -50.7843 | 2026-09-24 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 87dcd8d6-c2a6-3757-84e5-272ee4c0ec5f | -3.1637 | -54.6054 | 2026-09-24 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 93e16201-60ca-3300-9df9-f2c8e6c358f4 | -6.4302 | -59.9724 | 2026-09-24 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| aa13db30-1bd9-3ccd-a1d5-fd9655643bd4 | -12.1487 | -50.7598 | 2026-09-24 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 98f5baa9-3488-3a5b-bc47-85634a373221 | -6.5962 | -59.9279 | 2026-09-24 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 2971efed-ff5e-3bee-ba29-c6ad71610449 | -5.6016 | -60.1919 | 2026-09-24 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f810530a-e5cd-3332-b2f5-b0a3931059ec | -15.2517 | -43.2501 | 2026-09-24 00:20:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 148.2 |
| 5aca3c62-884b-3d20-a39e-d08cea8ba88b | -15.2314 | -43.2784 | 2026-09-24 00:20:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 00bfe73c-f92e-3eb9-976d-9be3de6bae80 | -4.1181 | -51.0695 | 2026-09-24 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| f75bdfb6-a4cc-38a6-93a1-2a3550a74a3d | -15.2511 | -43.2743 | 2026-09-24 00:20:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 136.7 |
| 638f76e1-7c84-3b9a-95ca-b99055c46d35 | -3.4392 | -50.0896 | 2026-09-24 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| b023442a-94be-364f-808c-b9c3aff67fc9 | -9.0157 | -60.533 | 2026-09-24 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 7fb2bd18-2379-397e-ac07-c66ed38db7e1 | -12.4216 | -46.9551 | 2026-09-24 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| df154694-bd52-3fa5-b991-7c719db6da32 | -12.1109 | -50.7429 | 2026-09-24 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 35224aaa-3fd5-3b0e-b2da-c0fec42691c8 | -6.6331 | -59.9265 | 2026-09-24 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| f5ab0c32-1cdf-3541-83f9-627b1c78213b | -3.4577 | -50.089 | 2026-09-24 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 9c5d11be-4bd3-366d-bc9c-adf48471a5b2 | -9.868 | -48.4907 | 2026-09-24 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 3194a1b4-5254-3898-8742-3c13234f1514 | -8.4538 | -48.6944 | 2026-09-24 00:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e756424f-b331-3a4d-b96e-22217959f1e8 | -6.7703 | -48.6792 | 2026-09-24 00:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 86d17084-2022-39a5-b9d9-2f0fe14579d1 | -4.118 | -51.0903 | 2026-09-24 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 85541d61-6854-3afd-99f5-dccdf6e6362b | -12.0918 | -50.7451 | 2026-09-24 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 3e3d4c38-adb2-33f6-92bb-38470e5d8e0b | -15.232 | -43.2541 | 2026-09-24 00:20:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 119.3 |
| 6fd488c8-c644-3082-a8eb-26cf6f9a98e1 | -9.8491 | -48.4927 | 2026-09-24 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 1f3cd409-a5a2-3011-a328-2ed130d101b4 | -11.9392 | -50.7629 | 2026-09-24 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 149.2 |
| eff40056-7a9e-3eb7-a703-48a2a28afbd1 | -10.0917 | -46.0458 | 2026-09-24 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ba49e742-c1f1-3601-a9e4-62748281abb1 | -6.6146 | -59.9272 | 2026-09-24 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 1416c3ea-276c-3da2-b661-8ee6a041f798 | -3.6763 | -60.5839 | 2026-09-24 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a0997711-a78e-38ab-be9c-e7c6e373ad91 | -3.4578 | -50.0679 | 2026-09-24 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ead6be7b-a3e7-37ed-97a6-39d93d11b86d | -6.4486 | -59.9717 | 2026-09-24 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 0817b738-84e4-39b6-a735-ea514808a6fd | -11.958 | -50.7821 | 2026-09-24 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 825bfca8-607c-3a65-bd77-f8860087df8c | -6.4487 | -59.9526 | 2026-09-24 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 2a43412b-b21c-3474-bb76-a0884aaeef85 | -6.633 | -59.9457 | 2026-09-24 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2ea4436b-5ed7-3631-809f-010b9ff616a9 | -6.789 | -48.6779 | 2026-09-24 00:20:00 | GOES-19 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 82.9 |
| ef46a83d-98da-3333-9ef2-e859c4490c0b | -6.6145 | -59.9464 | 2026-09-24 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| efec5d38-9edf-34a8-a5c3-baf0784a89a5 | -5.7756 | -45.0826 | 2026-09-24 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 18842939-89e7-3e1d-957a-f40bc4ef1e9c | -5.7567 | -45.1067 | 2026-09-24 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 27605a53-bc48-3fa6-a1be-2e63b456cc1b | -9.0158 | -60.5138 | 2026-09-24 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 12c542a2-9e13-3bcf-a99f-500917ffcfb4 | -11.9583 | -50.7607 | 2026-09-24 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 318.9 |
| 7696d82e-9ca1-33cc-97d6-73405b8c8392 | -3.6764 | -60.5649 | 2026-09-24 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c5b8ec6e-e56d-38be-ab60-40063fd09a06 | -15.5686 | -42.3547 | 2026-09-24 00:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 1069b8fa-305b-3ef3-8267-bc188f6ac88c | -11.9774 | -50.7585 | 2026-09-24 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| cc8d510d-ba30-3069-bf0b-f8a0352b3b17 | -3.6765 | -60.5459 | 2026-09-24 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 6522d1a8-e8b9-389d-9c08-90317248e5ae | -3.6947 | -60.5645 | 2026-09-24 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 6c4e9b88-7541-374c-8cb9-670560504899 | -3.6947 | -60.5455 | 2026-09-24 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| f11fdd51-d0c3-334f-a046-340ad6782dcf | -10.0921 | -46.0232 | 2026-09-24 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| f5528e2e-f4e3-3421-a1b1-279a56faf9d3 | -5.7754 | -45.1053 | 2026-09-24 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| ed83f3a3-2904-3cde-8fa0-ad48be2f4fb1 | -10.2637 | -49.9626 | 2026-09-24 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 15ac7530-08d4-37c1-b0fd-5385b5774b43 | -12.0727 | -50.7474 | 2026-09-24 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b7f2c2de-4bfd-37cf-b2f9-0eb7f176c09b | -3.4393 | -50.0685 | 2026-09-24 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 0923bb8b-1b9d-38b7-9736-4c08cd733e08 | -8.0275 | -71.3619 | 2026-09-24 00:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 50.0 |
| f1f14042-523a-38e2-a02e-fdc73ebac203 | -3.1454 | -54.6059 | 2026-09-24 00:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 526025fa-7905-3349-af15-c3baef39cba7 | -3.4387 | -60.5695 | 2026-09-24 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| d91e6cd0-feab-336a-bf29-4ea85024b7e8 | -11.9586 | -50.7393 | 2026-09-24 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 9aee2413-1643-3346-8a73-f6c7846be046 | -9.8488 | -48.5146 | 2026-09-24 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| cd735f86-b094-39ee-a445-192cb70b144f | -3.6946 | -60.5835 | 2026-09-24 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 110d748a-ff7c-342d-9b3b-81712668a893 | -10.2827 | -49.9606 | 2026-09-24 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 462f8101-efaa-3bac-832d-f468701120e5 | -6.4303 | -59.9532 | 2026-09-24 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 58381d37-1ef0-3921-9553-9fc84f65a931 | -4.2951 | -49.1234 | 2026-09-24 00:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9fe2b5fd-42eb-3407-a836-c61728ec04ca | -6.3501 | -57.7717 | 2026-09-24 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 17b2e959-c313-3f9f-809c-5cf2fd24828d | -6.3501 | -57.7717 | 2026-09-24 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 0d00e2b1-4ed2-3b72-92e4-07ea5496f625 | -13.4538 | -46.2771 | 2026-09-24 00:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 84e89ade-2b7f-3553-8e90-dd8ed86a2545 | -3.4392 | -50.0896 | 2026-09-24 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| c0ebf4c8-d6a8-37e9-8d82-aaca7f062e8c | -5.7754 | -45.1053 | 2026-09-24 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 137.5 |
| b5d77bab-bf3e-3a1f-a09c-05359cc05984 | -6.6331 | -59.9265 | 2026-09-24 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 8b7e7d1a-07e7-3436-9cc0-42c1380a9f10 | -12.4212 | -46.9777 | 2026-09-24 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 9ab5cadf-f4d0-3ea4-a94a-3533d15e191c | -4.1181 | -51.0695 | 2026-09-24 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 6c5c58cf-1822-34f4-bd79-367f091825d6 | -6.6145 | -59.9464 | 2026-09-24 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 49a0930c-4a98-3ec5-9bb0-f75070472fbe | -11.9586 | -50.7393 | 2026-09-24 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| c567a3b9-9907-3c3c-abe9-2114ff35003e | -12.4024 | -46.9579 | 2026-09-24 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 0e0c4ea4-daaf-30e7-ae83-21699be2545b | -3.4578 | -50.0679 | 2026-09-24 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c60bd739-09ca-3d80-8717-9c8600a3a39e | -8.5951 | -62.4988 | 2026-09-24 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 42316812-dcd1-30db-98e0-ea124a2b5909 | -11.9774 | -50.7585 | 2026-09-24 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 30b98c4d-697a-3e65-bcec-df3416baeaa6 | -10.0921 | -46.0232 | 2026-09-24 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 27296e11-5bc1-36d8-88ca-bba774ee2f0d | -9.0157 | -60.533 | 2026-09-24 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| ee125b53-3c6c-3e10-8ba0-2b53dbf82983 | -6.4486 | -59.9717 | 2026-09-24 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 721ae452-7e20-30cb-8268-15d3c8014c50 | -11.9392 | -50.7629 | 2026-09-24 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 8bd73fbd-5cbb-3e61-93d0-7bdadf0cf9e4 | -12.0918 | -50.7451 | 2026-09-24 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 0acb0e8f-7e65-35c5-a5ad-4f43679ae942 | -12.1109 | -50.7429 | 2026-09-24 00:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 7bb4e8e2-d6c9-32e6-ac4c-e3765f8e2398 | -3.6764 | -60.5649 | 2026-09-24 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9f7061e2-66ef-34ad-9078-eb7c73d81ebb | -3.457 | -60.5692 | 2026-09-24 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| a9094bd0-17b5-3721-8400-59bdc793232d | -15.232 | -43.2541 | 2026-09-24 00:30:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 2c5243ba-8417-3e06-8d83-4b3f381c8955 | -6.6146 | -59.9272 | 2026-09-24 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 135.8 |
| bf07ea28-654b-3994-829d-c8ebc14d583e | -8.595 | -62.5178 | 2026-09-24 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| d8bf7ff1-8131-3f88-9f9f-89d0b75a52d7 | -10.2637 | -49.9626 | 2026-09-24 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 4096d929-d111-3802-927c-e084224ade4f | -6.633 | -59.9457 | 2026-09-24 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 12fb20af-09e7-3348-bada-5f30f0b558a2 | -3.4577 | -50.089 | 2026-09-24 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |


[Clique aqui para ver as próximas entradas](README10.md)
