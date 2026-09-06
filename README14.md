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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4f4006b-89a3-36f4-9869-c32bc35eda57 | -12.43576 | -43.41486 | 2026-09-06 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83142c20-8f72-3532-bd9c-6772a4d48741 | -13.43577 | -41.88738 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d8d53db0-dbcc-3d15-87ba-8a398586abf8 | -11.28838 | -45.70807 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3148cbc1-2de1-3d9e-b7b6-12beac21c25c | -13.87027 | -44.3052 | 2026-09-06 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f009aa8-994a-3d8d-bba9-841743119ed2 | -11.28317 | -45.10695 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59e2d057-c12a-3b94-ad43-3b9b6544f431 | -11.29484 | -45.11288 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 139ecb86-523e-3034-aa1b-ccd691d83c11 | -9.57468 | -40.3555 | 2026-09-06 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| f0158f5a-134f-3b18-abcf-bd0b4beb9802 | -11.28337 | -45.71136 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef115185-5f84-355e-8139-f3eb7eaac109 | -7.37399 | -47.02447 | 2026-09-06 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 081b062b-ca73-3d40-b07a-c430001f6ea0 | -13.43298 | -41.8831 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 32ceed8b-8a3e-3efb-ad90-4d557d7e6f8e | -10.70563 | -45.90097 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f96fee85-9837-3b1d-b9b2-b59dec7eeaca | -11.30044 | -45.71464 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b60e5e2-e7e4-3478-b625-f9847f55d71a | -9.39471 | -40.50622 | 2026-09-06 04:02:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 11b2a817-f170-3910-a5d5-2044b48c7c64 | -11.27478 | -45.71006 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4ce28a0c-f95a-311f-8182-6dca33d7a262 | -13.32267 | -44.03671 | 2026-09-06 04:02:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e10da545-097a-364a-96eb-af02dcfbcd70 | -8.04343 | -37.55551 | 2026-09-06 04:02:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 87c13750-1705-310c-9117-2c4a5c5754ca | -11.33093 | -45.07631 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b748a074-1e58-373a-a9c6-a5d85d74908e | -11.55381 | -42.50666 | 2026-09-06 04:02:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf010cea-0d99-3f25-a187-e0db460d61be | -9.63414 | -47.68789 | 2026-09-06 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8779f13-3e1c-35c1-81d9-7c29ae2bab01 | -5.92313 | -47.89608 | 2026-09-06 04:02:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58a7a4fd-2b07-3301-8cbb-2d6ecac73e1c | -7.36901 | -47.02353 | 2026-09-06 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83513637-5491-35d1-81a9-f0dd5895322b | -9.52937 | -41.99239 | 2026-09-06 04:02:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b762cd0c-b815-33b1-80d4-8c934728e34b | -6.85948 | -46.46317 | 2026-09-06 04:02:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1ff58e1-70f2-39f9-a2b2-8c7ec29ce8aa | -11.32816 | -45.068 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9f68cff4-7feb-320b-97ec-f5b122fff24d | -8.98124 | -44.41317 | 2026-09-06 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9061e286-2c79-37dd-934b-8140d65f8af8 | -12.71068 | -42.33989 | 2026-09-06 04:02:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6456daa1-181b-341c-9fc3-5f5b4da73a9e | -11.32748 | -45.07189 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bfed4278-eff1-3221-b1d6-b2065901a0b1 | -11.22212 | -41.86303 | 2026-09-06 04:02:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 84b7f36f-789e-3f3d-b988-0f7dc8a7cd95 | -11.94542 | -44.8604 | 2026-09-06 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16fdaf0c-10f1-3589-afe1-5f7c05c37967 | -8.97369 | -44.40812 | 2026-09-06 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e243422-e845-3796-b3dd-28070d003f08 | -8.04164 | -37.55518 | 2026-09-06 04:02:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4fca3b3c-c8e8-3759-84f4-9f1ccf8256ea | -8.97779 | -44.40876 | 2026-09-06 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4f53219-192c-39b4-bb2f-2abfa1a7ffee | -10.93 | -38.81596 | 2026-09-06 04:02:00 | NOAA-20 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 33c592f6-aa0e-3839-9948-bd2d454c56d3 | -11.29337 | -45.70488 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 526e8c20-53d5-32ac-af84-3d1038623b36 | -14.60845 | -41.04572 | 2026-09-06 04:02:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fcf34178-275f-395f-89d2-6d8fa5b5c6d0 | -12.95062 | -42.41992 | 2026-09-06 04:02:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 67094362-9b9c-3b71-a4a0-f87a4b8411cd | -11.29138 | -45.10846 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04a347be-7b16-32b7-9500-de5628756430 | -13.43118 | -41.89407 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1030e85f-b07d-399d-bf33-3e039d08ae85 | -11.82687 | -45.3219 | 2026-09-06 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8be9bc1a-bd9c-3480-b34e-bcfbd89a3910 | -13.4256 | -41.88558 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 72be5bef-e6d4-3c29-9d8f-12bbb2052015 | -11.33228 | -45.0686 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a82a06e4-9d56-3b44-8620-1331bbe5e0da | -12.85812 | -44.61401 | 2026-09-06 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 855f7a02-4861-35c3-90c6-b5c710f1d83c | -11.81924 | -45.31685 | 2026-09-06 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c8b18d1-fa9c-3df6-8193-802c4b10b473 | -8.95202 | -44.41211 | 2026-09-06 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2aba1686-149c-343e-9505-6bd6573ee302 | -12.7159 | -43.20435 | 2026-09-06 04:02:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8bcd66b-a47c-344e-9bb0-2269a7b3d36a | -9.63468 | -47.68498 | 2026-09-06 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57b36c10-541c-36f1-bbeb-bd32b196e801 | -9.53576 | -41.99759 | 2026-09-06 04:02:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f35ec6f1-f56d-3e9f-aded-6b0dbfa87441 | -8.9696 | -44.4075 | 2026-09-06 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35320480-32af-3aae-a4ba-f80b0a5b01ec | -8.98589 | -44.41051 | 2026-09-06 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c0235bb-f3f8-3575-8011-d9b49512fbc9 | -7.69853 | -44.3111 | 2026-09-06 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62918363-2aa4-393f-92e7-d6babf4ee367 | -11.27909 | -45.71064 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 499eae27-0737-3d17-b781-6ec8faf159ff | -10.6899 | -45.93781 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8794835-e343-34f9-9d1d-91f19f214852 | -9.57076 | -40.35852 | 2026-09-06 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 42cc2237-ae47-37fd-945c-f5a25f7a3a5e | -13.55712 | -43.91943 | 2026-09-06 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 321ecb6e-a1e5-3003-a694-ed923014b99c | -11.29691 | -45.70973 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1e6ead3-cef0-3ca3-bbe3-56f56d237b72 | -13.43457 | -41.89468 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2ac21e7b-c358-39e7-896b-b695df43f50f | -7.36952 | -47.02066 | 2026-09-06 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4cb74495-a28d-3e0f-ba28-ff825862e713 | -11.28765 | -45.71211 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a388e80-a23e-39f7-a092-5af15e35ee25 | -13.43057 | -41.89778 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5691278a-b51c-398e-a55e-114cfccc5b67 | -12.43657 | -43.27875 | 2026-09-06 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e42a54cb-8187-3dc3-8e27-17f2ba6ef21e | -7.67388 | -46.05211 | 2026-09-06 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6be91e90-50ca-3fe6-a439-1e92c5e565c2 | -7.44491 | -49.73026 | 2026-09-06 04:02:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9e38948-873e-328a-b6e8-69505517ff2c | -8.98185 | -44.40956 | 2026-09-06 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 841745a8-55de-38fe-8dec-640bba0a3d4c | -9.57134 | -40.35495 | 2026-09-06 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 98fcdd04-0eb9-3c43-9baa-72ecd47a87af | -13.43408 | -43.82582 | 2026-09-06 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71ec0764-1510-3351-8f02-252925cc3a2c | -11.82337 | -45.3176 | 2026-09-06 04:02:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 485ad9f7-003f-3ad4-a6ae-fad35e9d53e3 | -13.37697 | -41.34834 | 2026-09-06 04:02:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5639418f-cb48-3337-a4f6-f609892c8cbd | -14.61175 | -41.80146 | 2026-09-06 04:02:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 52040818-3240-3214-8e6e-6558ffb49e02 | -8.92188 | -40.78371 | 2026-09-06 04:02:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 65222e4d-503b-3ff0-bc88-0375af2a1513 | -7.24775 | -39.33617 | 2026-09-06 04:02:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a4f0a84a-7e6e-3949-a1cb-530afae40e67 | -10.03839 | -48.21684 | 2026-09-06 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99c09c10-4352-3dca-a01f-f7f88341041e | -10.65368 | -45.09872 | 2026-09-06 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2a499b4-8c23-3bdb-9427-a8b1fab25829 | -15.36663 | -42.12389 | 2026-09-06 04:04:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f1eb330a-0ae7-3312-be52-0d71b29da06d | -18.57634 | -39.79343 | 2026-09-06 04:04:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 81e0b0c0-17fd-32cc-9bee-e957cd34bff1 | -13.74645 | -51.67299 | 2026-09-06 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7523763d-01ff-3dce-bfdd-9ca23fcbe167 | -15.43494 | -40.93517 | 2026-09-06 04:04:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d3b0b7b4-d962-3fdc-ae8b-9d7fbec1dd2b | -14.90538 | -44.67778 | 2026-09-06 04:04:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74b24267-2772-3370-bb24-66046189f9bc | -15.33195 | -43.64902 | 2026-09-06 04:04:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e53ed873-7890-3993-a06a-acda619564cc | -14.86492 | -40.90863 | 2026-09-06 04:04:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 17d25c1f-a209-3f67-af00-85cde67a14fc | -14.91082 | -44.66898 | 2026-09-06 04:04:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 59dcbad9-b379-32b3-9d2e-39a9125c6bff | -15.81064 | -42.57568 | 2026-09-06 04:04:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 31e2a2a9-e54b-39f0-a39a-69ad3deeffe9 | -13.76127 | -51.66198 | 2026-09-06 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5be937f9-9d14-3196-84b3-b977e0c6d6a5 | -17.94941 | -50.36614 | 2026-09-06 04:04:00 | NOAA-20 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65e3ab5f-067d-3274-a60b-7763e416bf98 | -16.75291 | -41.71724 | 2026-09-06 04:04:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7e742a91-7d33-3b38-b4dd-8238539cc965 | -17.42809 | -40.02109 | 2026-09-06 04:04:00 | NOAA-20 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6d3eb736-86e8-3694-9563-7ad546d9ca6b | -16.24557 | -44.15884 | 2026-09-06 04:04:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb0d49a4-da04-3157-b992-26cd077129b9 | -16.14315 | -40.68679 | 2026-09-06 04:04:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 12f7e46c-faf4-3d44-8fd8-04d4667bf1a7 | -14.67698 | -48.92234 | 2026-09-06 04:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78cca53e-fd41-3caa-beb7-21b364bbab30 | -14.9016 | -44.67705 | 2026-09-06 04:04:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e9789565-fedc-3f0b-addb-466bddf12a4c | -16.40229 | -49.20289 | 2026-09-06 04:04:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90285dd2-ada7-3f4a-9669-04c6cad7e96f | -15.71341 | -43.69339 | 2026-09-06 04:04:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15a4b2c3-1c18-363c-b605-33c24635a9e2 | -14.90999 | -44.67373 | 2026-09-06 04:04:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| a82bf33f-7ea0-3d1a-830a-488d1bedb35b | -14.91837 | -44.67043 | 2026-09-06 04:04:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 30951e2a-13e1-3bc7-befc-1a555330f1b0 | -17.42474 | -40.02054 | 2026-09-06 04:04:00 | NOAA-20 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 904c5309-7b2b-36a8-933e-753dafd2f290 | -17.58516 | -43.7405 | 2026-09-06 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| feeebef8-9d50-3de9-a3b8-710889701feb | -18.38679 | -39.95768 | 2026-09-06 04:04:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c47ccc16-e908-38ef-b367-26c2f42fda10 | -14.86766 | -40.91276 | 2026-09-06 04:04:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c80c52c9-a17c-330a-85d2-2429e0ac77d6 | -13.75625 | -51.6559 | 2026-09-06 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1366dec3-de9d-31f7-9914-803fa74e83e6 | -17.42531 | -40.01685 | 2026-09-06 04:04:00 | NOAA-20 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f3d278be-0080-3d82-a486-c7cfad3e660d | -18.47258 | -41.41722 | 2026-09-06 04:04:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | MINAS GERAIS | Brasil | 3163300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README15.md)
