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

## Dados Diários - Página 286

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbc14bf4-a7ae-376f-849c-9248a78609c3 | -9.7559 | -45.6783 | 2026-10-09 17:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 315.3 |
| 7a512bba-14a2-320f-a5bb-cafd9b81583c | -10.4334 | -47.3046 | 2026-10-09 17:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 188.0 |
| c56e0329-6069-3706-a89c-699a15465c1b | -15.3825 | -41.9277 | 2026-10-09 17:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1716.4 |
| ca08e41f-fee8-3ffb-8311-e346ba310f72 | -3.5193 | -58.0183 | 2026-10-09 17:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| de0e8c3b-a41a-3e4e-b50d-ad4ef6e92846 | -10.4727 | -47.211 | 2026-10-09 17:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 2341a26f-5223-377e-831b-78f19d7b4bb4 | -11.0558 | -44.0796 | 2026-10-09 17:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 176.3 |
| b2e2cc6e-73ab-31a6-b01a-dacc820e08b8 | -3.5893 | -59.0773 | 2026-10-09 17:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 806d17a8-b606-3a80-b7a8-5792cdfe28e0 | -15.0516 | -41.8024 | 2026-10-09 17:50:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 210.7 |
| 1746baf2-38d7-3464-abfe-6dc03f707a90 | -5.9791 | -41.3733 | 2026-10-09 17:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 6a174aee-7f40-3a8d-a990-34bfe3bd2bbf | -1.549 | -54.5356 | 2026-10-09 17:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 78b37cb8-dc7d-3fed-b063-55afb8059a7a | -11.7772 | -45.4806 | 2026-10-09 17:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| a36e2318-c6ed-3d8e-97b4-51fdcf8da008 | -7.0038 | -47.6843 | 2026-10-09 17:50:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 3962a245-c68b-3e3e-bdc7-ea3633da2bcb | -9.737 | -45.6805 | 2026-10-09 17:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 7b650e03-53e7-36d3-820b-9fe5056de1c5 | -9.9198 | -44.8585 | 2026-10-09 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 232.7 |
| 3b00ca4c-d736-3e9a-8ed4-c5d267917102 | -3.6252 | -59.3259 | 2026-10-09 17:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| def2bf1f-0f8e-3451-ab40-7d4437804cbc | -11.014 | -45.4272 | 2026-10-09 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 304.0 |
| 2a351f92-db05-394d-b494-8b6dc730b7c6 | -4.7404 | -55.6522 | 2026-10-09 17:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 19abd469-3de2-3c8c-b1d0-730b3aa11d29 | -11.3103 | -44.8337 | 2026-10-09 17:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 6fdfc872-52d6-3cdb-b0b1-3506271eb678 | -3.6435 | -59.3064 | 2026-10-09 17:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a555c8fb-e7c0-3c00-80ab-b95f9dc2f007 | -2.568 | -57.7852 | 2026-10-09 17:50:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 0e341e17-7961-3ecd-bc9d-50db8a77845e | -11.0562 | -44.0561 | 2026-10-09 17:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| c08049c5-ce2f-3097-9e4f-d5c107564f56 | -2.7335 | -57.4717 | 2026-10-09 17:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 0c771cad-e9cf-31a5-a352-e2a2900004ab | -8.9308 | -45.1584 | 2026-10-09 17:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| bd338d96-94df-3378-a1ea-e02eb9ebc2cb | -13.1636 | -54.3591 | 2026-10-09 17:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 272.9 |
| 12106e80-d625-3348-a114-7e147f62306a | -16.2353 | -44.053 | 2026-10-09 17:50:00 | GOES-19 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 0a711dd0-a081-3611-827f-1f916b10c7a4 | -12.1952 | -44.6321 | 2026-10-09 17:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 232.9 |
| 00cbb7db-0bef-32f5-b93d-9c9477182d70 | -12.3712 | -46.5562 | 2026-10-09 17:50:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| a60e41a3-61b3-3e5e-afd3-90339d64e1bc | -2.5689 | -57.4163 | 2026-10-09 17:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e960cfdf-91a6-3dc2-aa24-14ae571c8cc0 | -10.8123 | -47.3479 | 2026-10-09 17:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| adea1b89-1c46-38ec-ae1f-b97d1dc8a8cc | -8.5501 | -46.9091 | 2026-10-09 17:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| fc56f724-db14-3bc1-adb2-5e83173d4f2b | -12.2316 | -44.7427 | 2026-10-09 17:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 767eceb9-9544-3fad-8945-ea9cdbedd272 | -13.3865 | -43.8708 | 2026-10-09 17:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| da6e28ff-8f5f-3a50-a0e0-e195d5311330 | -10.1766 | -48.0412 | 2026-10-09 17:50:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 1c9c81c9-d207-33b8-9c67-9d67a1640751 | -10.4724 | -47.2333 | 2026-10-09 17:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 158.3 |
| e3d237b7-a0b0-329f-bde6-4cecf450d7e2 | -9.9018 | -44.7917 | 2026-10-09 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| b55873fd-7109-3cc9-9321-b6db3180187a | -9.183 | -43.3688 | 2026-10-09 17:50:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 143.7 |
| 832aeee3-b733-31ed-804c-b5ca379ffdfd | -3.1879 | -58.6433 | 2026-10-09 17:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 174.3 |
| 725d99d2-4fe0-35a6-aee1-bacdc6ed71a9 | -2.572 | -56.1646 | 2026-10-09 17:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d8672b9d-c21d-356a-a148-ccfbad5bedf7 | -2.4806 | -56.0678 | 2026-10-09 17:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 4ae5fd18-00cc-3b36-b280-12a00a2b1291 | -3.1697 | -58.6244 | 2026-10-09 17:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 532c59d5-c95b-30f7-b979-e7046783255c | -2.0403 | -56.3895 | 2026-10-09 17:50:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 773fea54-a23f-3a81-b18c-6d4da54f5318 | -12.2119 | -44.769 | 2026-10-09 17:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 4a05b392-f78b-3a85-9b79-d39d774e768c | -8.3022 | -44.1467 | 2026-10-09 17:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 0b7af18d-4e24-3fd6-8136-7f243a020827 | -14.5109 | -41.4727 | 2026-10-09 17:50:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 2e8bdd28-a93f-3d29-9d31-dbb61cd13a73 | -10.4914 | -47.231 | 2026-10-09 17:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 6d911e40-8cae-3079-82f7-08b88d0d48e6 | -2.5903 | -56.1839 | 2026-10-09 17:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c009b39f-8d08-3051-9085-5dc6e61aeddb | -5.2274 | -48.4113 | 2026-10-09 17:50:00 | GOES-19 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9e4865b0-605b-3c4e-9733-6dee1334d841 | -10.8317 | -47.3233 | 2026-10-09 17:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 75e9f718-5d71-3148-88f3-2aba52b766c4 | -11.47 | -43.3824 | 2026-10-09 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 87a70400-4163-3c14-85e4-ff27938fe4bf | -1.8757 | -56.3133 | 2026-10-09 17:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| fcf36900-d6fa-349e-b683-3763cdef509b | -13.1639 | -54.3385 | 2026-10-09 17:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 171.4 |
| 0d8d1b21-57f0-366d-bbda-23ddf654e346 | -12.2123 | -44.7457 | 2026-10-09 17:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 290.3 |
| f224a335-2dcb-344a-94c5-dfc391f6f2d4 | -17.4581 | -45.0511 | 2026-10-09 17:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 8d252319-26f1-3265-a2d3-6de026b73933 | -10.8313 | -47.3456 | 2026-10-09 17:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| cf1d9aa5-efe1-35c8-8823-5753f4b58310 | -12.2145 | -44.6291 | 2026-10-09 17:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 371.7 |
| d5b8a999-3445-3c53-ac36-c057a70719e7 | -9.1015 | -45.1164 | 2026-10-09 17:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 88da4a0a-e6fd-3547-9029-65dbb533da2a | -11.7736 | -46.7985 | 2026-10-09 17:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 59994c79-242e-389d-881d-86eda4affe57 | -5.7133 | -41.6364 | 2026-10-09 17:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 54821428-9002-3f54-b9b5-7915d3bb4ac2 | -11.0137 | -45.4501 | 2026-10-09 17:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 9228777d-19da-3365-a1c7-ccb2041abe54 | -11.075 | -44.0768 | 2026-10-09 17:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 3fab24f3-c037-3408-ad51-3668520f22de | -6.8602 | -41.7494 | 2026-10-09 17:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| b29ae7ce-9b4a-3d7d-b669-d79c4a051e3c | -11.0366 | -44.0824 | 2026-10-09 17:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| a8f35655-5437-3975-934b-2a223c76941e | -3.6623 | -59.1525 | 2026-10-09 17:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 92485084-1f25-371c-a167-4c515df456db | -2.9979 | -54.7692 | 2026-10-09 17:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 0ecb07da-983a-3cdf-938e-fefa321885d9 | -2.5171 | -56.1262 | 2026-10-09 17:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a11e6eca-26a7-3621-a1e9-02a988d8b6b1 | -15.0713 | -41.7982 | 2026-10-09 17:50:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1088.9 |
| 715678ff-22d3-395a-b420-0813e605a548 | -2.4623 | -56.0682 | 2026-10-09 17:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 6f58d2cf-77e3-3bc4-a73e-ad21bab3c90a | -5.6934 | -53.4667 | 2026-10-09 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 37a53f9d-8edc-3d7f-9b19-6eb073c901fd | -2.5903 | -56.1839 | 2026-10-09 18:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 14f3998e-3cdc-3df4-8e7f-5e6a01930ad1 | -12.1435 | -45.3576 | 2026-10-09 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 017aa08c-43af-3c7a-a535-85b00f4e6711 | -13.6896 | -49.107 | 2026-10-09 18:00:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 039d045c-e8fe-329e-a5e1-3376ea6011ee | -10.9957 | -45.3839 | 2026-10-09 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| c8add739-4dd5-3ec0-83e9-7b38ff5e75a7 | -3.1879 | -58.6433 | 2026-10-09 18:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 165.2 |
| e805e4e5-4c96-3ad2-ba43-00ecef5d4386 | -12.2316 | -44.7427 | 2026-10-09 18:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 7f037472-018b-38e4-a94c-2532c596427a | -12.2123 | -44.7457 | 2026-10-09 18:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 425f39d5-285a-347a-9c41-905458f3b8bc | -13.1641 | -54.3178 | 2026-10-09 18:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 24517042-4ac4-3205-9a10-6193f280c82b | -5.8166 | -42.628 | 2026-10-09 18:00:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 4b792a5a-3238-3dd2-98db-3d0577f54df0 | -12.0448 | -43.434 | 2026-10-09 18:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| e83f12dc-ff19-303a-b71b-1be08e81dc47 | -10.9953 | -45.4068 | 2026-10-09 18:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 90d40dc8-b759-3f19-a163-0e41f6647db5 | -12.0453 | -43.4102 | 2026-10-09 18:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 155.1 |
| b1cf1697-99e9-3830-8d6a-ae7e1f8e0574 | -11.0366 | -44.0824 | 2026-10-09 18:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| b7719cce-c55f-3eba-92b5-26829a9907a6 | -11.0558 | -44.0796 | 2026-10-09 18:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 374aa113-c40f-388d-a20b-e91377f724f8 | -11.0554 | -44.103 | 2026-10-09 18:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 9712fbed-073d-3833-aeb7-d69fe6ef4124 | -2.9327 | -58.3011 | 2026-10-09 18:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 9159d6a0-7bac-3dcd-a255-6ca266f2b1a3 | -3.6692 | -57.0617 | 2026-10-09 18:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ae6954e1-04d8-35c0-af49-9a578b75dedc | -8.3583 | -44.187 | 2026-10-09 18:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 18fb6327-f8fc-303e-99e9-93e6ee0bbe77 | -3.1697 | -58.6244 | 2026-10-09 18:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| bccc217e-1c1c-358f-8e36-2dbdc2d8e502 | -18.3132 | -42.365 | 2026-10-09 18:00:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 190.4 |
| 9ee17bce-bd8e-323c-8af1-4d94ff776151 | -3.188 | -58.6241 | 2026-10-09 18:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 160cddee-7164-3323-a4f0-0df039b72262 | -8.358 | -44.2101 | 2026-10-09 18:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 0ee44f3c-edb0-30e3-a4a0-4f580907c514 | -3.2532 | -50.4108 | 2026-10-09 18:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 404f6833-1129-39be-8402-edda08dd9f9b | -4.3797 | -41.8282 | 2026-10-09 18:00:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 5a6c52db-7ffd-3d1b-8f20-7170bd04e27e | -12.1948 | -44.6554 | 2026-10-09 18:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 1c8e342f-b28f-377d-aa41-45142f400343 | -5.0945 | -46.2282 | 2026-10-09 18:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 93334af7-2554-3f2c-9c17-a50f33b83fc7 | -9.9398 | -44.7869 | 2026-10-09 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| ac3862df-403d-3219-87a2-6955c74d62cc | -11.5874 | -45.3931 | 2026-10-09 18:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 93af1a33-230e-33fd-b8f8-3f71559ff51b | -9.8828 | -44.794 | 2026-10-09 18:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 1bc8f945-4b58-300d-b82c-2025b0badb20 | -15.8531 | -42.0202 | 2026-10-09 18:00:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 246.5 |
| 8b5ba760-9089-3c48-90cb-511ae6ff0bea | -1.2907 | -55.7098 | 2026-10-09 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 4c673c31-13b7-30a2-adcc-5e9f3aa6a55e | -10.4914 | -47.231 | 2026-10-09 18:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 159.5 |


[Clique aqui para ver as próximas entradas](README287.md)
